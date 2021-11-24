import spotipy
import spotipy.util as util
import pandas as pd
import random
import seaborn as sns
from tabulate import tabulate
CLIENT_ID = "smth"
CLIENT_SECRET = "smth"
token = spotipy.oauth2.SpotifyClientCredentials(client_id=CLIENT_ID, client_secret=CLIENT_SECRET)
cache_token = token.get_access_token()
sp = spotipy.Spotify(cache_token)
#playlist_creator = "spotify"
#playlist_id = "37i9dQZF1EM9Lq3EzxxeM3"
playlist_creator2 = "Spotify"
#playlist_id2="5p3sjl2UqWTrhvUYPYvyt6"
playlist_id2='37i9dQZF1DWTXGqmP0bfT3'
#sp.user_playlist_tracks("spotify", "37i9dQZF1DWTcqUzwhNmKv")
pd.set_option('display.max_rows', None)
pd.set_option('display.max_columns', None)
def analyze_playlist(creator, playlist_id):
    # Create empty dataframe
    playlist_features_list = ["artist", "album", "track_name", "track_id", "danceability", "energy", "key", "loudness",
                              "mode", "speechiness", "instrumentalness", "liveness", "valence", "tempo", "duration_ms"
                              ]

    playlist_df = pd.DataFrame(columns=playlist_features_list)

    # Loop through every track in the playlist, extract features and append the features to the playlist df

    playlist = sp.user_playlist_tracks(creator, playlist_id)["items"]

    for track in playlist:
        # Create empty dict

        playlist_features = {}
        # Get metadata
        playlist_features["artist"] = track["track"]["album"]["artists"][0]["name"]
        playlist_features["album"] = track["track"]["album"]["name"]
        playlist_features["track_name"] = track["track"]["name"]
        playlist_features["track_id"] = track["track"]["id"]
        playlist_features["popularity"] = track["track"]["popularity"]
        # Get audio features

        audio_features = sp.audio_features(playlist_features["track_id"])[0]
        for feature in playlist_features_list[4:]:
            playlist_features[feature] = audio_features[feature]


        # Concat the dfs
        track_df = pd.DataFrame(playlist_features, index=[0])

        playlist_df = pd.concat([playlist_df, track_df], ignore_index=True)

    return playlist_df

playlist_df = analyze_playlist(playlist_creator2, playlist_id2)


#print(playlist_df)
playlist_df.to_csv('energy')
#print(tabulate(playlist_df,headers='keys',tablefmt='psql'))
