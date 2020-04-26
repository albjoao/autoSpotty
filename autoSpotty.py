# shows a user's playlists (need to be authenticated via oauth)

import sys
import spotipy
import spotipy.util as util
import json

def track_id_helper(tracks, uri):
    for track in tracks['items']:
        uri.append(track['track']['uri'])

def getTracks(playlistID):
    '''Gets track uris from playlist ID'''
    trackURIS = []
    playlist = sp.playlist(playlistID)
    tracks = playlist['tracks']
    track_id_helper(tracks, trackURIS)
    while tracks['next']:
        tracks = sp.next(tracks)
        track_id_helper(tracks, trackURIS)
    return trackURIS

def getUserPlaylistID(username,name):
    '''Converts human readable name to spotify id'''
    playlists = sp.user_playlists(username)
    for playlist in playlists['items']:
        if playlist['owner']['id'] == username and playlist['name'] == name:
            return playlist['id']

def showTracks(trackUris):
    '''Prints all tracks added'''
    tracks = sp.tracks(trackUris)
    for track in tracks['tracks']:
        print(track['name'])
    print()

def addNewSongs(username, playlistID, newSongs):
    playListURIS = getTracks(playlistID)
    actuallyNew = [uri for uri in newSongs if not uri in playListURIS]
    if actuallyNew:
        print("Adding: ")
        showTracks(actuallyNew)
        sp.user_playlist_add_tracks(username, playlistID, actuallyNew)
    else:
        print('No New songs to Add')


if __name__ == '__main__':
    username='thorriors'
    token = util.prompt_for_user_token(username, scope= 'playlist-modify-public')

    if token:
        sp = spotipy.Spotify(auth=token)
        discoverWeeklyUris = getTracks('37i9dQZEVXcXAN5Q9WscX1') 
        bestWeekly = getUserPlaylistID(username, 'Best Weekly')
        addNewSongs(username,bestWeekly,discoverWeeklyUris)

    else:
        print("Can't get token for", username)