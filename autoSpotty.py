# shows a user's playlists (need to be authenticated via oauth)

import sys
import spotipy
import spotipy.util as util

def getTrackUris(tracks):
    '''Parses track Ids into list of spotify ids'''
    allIds = []
    for item in tracks['items']:
        track = item['track']
        allIds.append(track['uri'])
    return allIds

def getUserPlaylistID(username,name):
    playlists = sp.user_playlists(username)
    for playlist in playlists['items']:
        if playlist['owner']['id'] == username and playlist['name'] = name:
            return playlist['id']


if __name__ == '__main__':
    username='foo'
    token = util.prompt_for_user_token(username)

    if token:
        sp = spotipy.Spotify(auth=token)
        discoverWeekly = sp.playlist('37i9dQZEVXcXAN5Q9WscX1')
        bestWeekly = getUserPlaylistID(username, 'Best Weekly')
        print(bestWeekly)
        tracks = discoverWeekly['tracks']
        newSongs = getTrackUris(tracks)
        playlists = sp.user_playlists(username)
    else:
        print("Can't get token for", username)