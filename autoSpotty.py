'''
Author: Joao Alberto de Faria
Takes in 'Discover Weekly' Playlist and Adds
all new unique songs to 'Best Weekly' playlist
'''

import sys
import spotipy
import spotipy.util as util
import json
from tracks import Playlist, UserPlaylist

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