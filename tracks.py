class Playlist():
    '''Responsible for Aggregating Tracks'''
    def __init__(self, spotify, playListId):
        self.sp = spotify
        self.id = playListId
    def _track_id_helper(self, tracks, uri):
        for track in tracks['items']:
            uri.append(track['track']['uri'])
    def getTracks(self):
        '''Gets track uris from playlist ID'''
        trackURIS = []
        playlist = self.sp.playlist(self.id)
        tracks = playlist['tracks']
        self._track_id_helper(tracks, trackURIS)
        while tracks['next']:
            tracks = self.sp.next(tracks)
            self._track_id_helper(tracks, trackURIS)
        return trackURIS
    def showTracks(self, trackUris):
        '''Prints all tracks added'''
        tracks = self.sp.tracks(trackUris)
        for track in tracks['tracks']:
            print(track['name'])
        print()

class UserPlaylist(Playlist):
    '''User Defined PlayList'''
    def __init__(self, spotify, username, playlistname):
        self.sp = spotify
        self.username = username
        self.id = self._getId(playlistname)

    def _getId(self,name):
        playlists = self.sp.user_playlists(self.username)
        for playlist in playlists['items']:
            if playlist['owner']['id'] == self.username and playlist['name'] == name:
                return playlist['id']
    
    def mergePlaylist(self, playlist):
        newSongs = playlist.getTracks()
        self.addNewSongs(newSongs)

    def addNewSongs(self, newSongs):
        playListURIS = self.getTracks()
        actuallyNew = [uri for uri in newSongs if not uri in playListURIS]
        if actuallyNew:
            print("Adding: ")
            self.showTracks(actuallyNew)
            self.sp.user_playlist_add_tracks(self.username, self.id, actuallyNew)
        else:
            print('No New Songs to Add')
