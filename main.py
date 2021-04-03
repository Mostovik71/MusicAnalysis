import spotipy
import spotipy.util as util
import pandas as pd
from tabulate import tabulate
CLIENT_ID = "3f131c5c52924d64bfd7bea065bedb7a"
CLIENT_SECRET = "ba50aa7ff4ee4e448e221def07f7feee"
token = spotipy.oauth2.SpotifyClientCredentials(client_id=CLIENT_ID, client_secret=CLIENT_SECRET)
cache_token = token.get_access_token()
sp = spotipy.Spotify(cache_token)
playlist_creator = "spotify"
playlist_id = "37i9dQZF1EM9Lq3EzxxeM3"
#sp.user_playlist_tracks("spotify", "37i9dQZF1DWTcqUzwhNmKv")
pd.set_option('display.max_rows', None)
pd.set_option('display.max_columns', None)
def analyze_playlist(creator, playlist_id):
    # Create empty dataframe
    playlist_features_list = ["artist", "album", "track_name", "track_id", "danceability", "popularity", "energy", "key", "loudness",
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
playlist_df = analyze_playlist(playlist_creator, playlist_id)
#print(tabulate(playlist_df))
#playlist_df.to_csv('mybest2020new')
print(tabulate(playlist_df,headers='keys',tablefmt='psql'))
