# Adds new songs from discover weekly to best weekly list

import sys
import spotipy
import spotipy.util as util
import json
from tracks import Playlist, UserPlaylist

def getUserPlaylistID(username,name):
    '''Converts human readable name to spotify id'''
    playlists = sp.user_playlists(username)
    for playlist in playlists['items']:
        if playlist['owner']['id'] == username and playlist['name'] == name:
            return playlist['id']


if __name__ == '__main__':
    username='thorriors'
    token = util.prompt_for_user_token(username, scope= 'playlist-modify-public')

    if token:
        sp = spotipy.Spotify(auth=token)
        discoverWeekly = Playlist(sp, '37i9dQZEVXcXAN5Q9WscX1') 
        bestWeekly = UserPlaylist(sp, username, 'Best Weekly')
        bestWeekly.mergePlaylist(discoverWeekly)
    else:
        print("Can't get token for", username)