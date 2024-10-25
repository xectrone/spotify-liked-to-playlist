import spotipy
from spotipy.oauth2 import SpotifyOAuth
import os
from dotenv import load_dotenv

load_dotenv()


# Spotify credentials and scopes
SPOTIPY_CLIENT_ID = os.getenv("SPOTIPY_CLIENT_ID")
SPOTIPY_CLIENT_SECRET = os.getenv("SPOTIPY_CLIENT_SECRET")
SPOTIPY_REDIRECT_URI = os.getenv("SPOTIPY_REDIRECT_URI")
SCOPE = 'user-library-read user-library-modify playlist-modify-private playlist-modify-public'

# Initialize Spotify client
sp = spotipy.Spotify(auth_manager=SpotifyOAuth(
    client_id=SPOTIPY_CLIENT_ID,
    client_secret=SPOTIPY_CLIENT_SECRET,
    redirect_uri=SPOTIPY_REDIRECT_URI,
    scope=SCOPE
))

def get_liked_songs():
    liked_songs = []
    results = sp.current_user_saved_tracks(limit=50)
    while results:
        liked_songs.extend(results['items'])
        results = sp.next(results)
    return [(track['track']['id'], track['track']['name']) for track in liked_songs]

def get_or_create_playlist(playlist_name):
    playlists = sp.current_user_playlists(limit=50)
    for playlist in playlists['items']:
        if playlist['name'] == playlist_name:
            return playlist['id']
    
    new_playlist = sp.user_playlist_create(sp.me()['id'], playlist_name, public=False)
    return new_playlist['id']

def add_songs_to_playlist(playlist_id, song_ids):
    existing_tracks = set(item['track']['id'] for item in sp.playlist_tracks(playlist_id)['items'])
    new_tracks = [track_id for track_id in song_ids if track_id not in existing_tracks]
    if new_tracks:
        sp.playlist_add_items(playlist_id, new_tracks)

def unlike_songs(song_ids):
    sp.current_user_saved_tracks_delete(song_ids)

def main():
    playlist_name = 'WORKOUT'
    
    # Get all liked songs
    liked_songs = get_liked_songs()
    song_ids = [song_id for song_id, _ in liked_songs]
    
    if not song_ids:
        print("No liked songs found.")
        return

    # Get or create the target playlist
    playlist_id = get_or_create_playlist(playlist_name)
    
    # Add songs to playlist without duplicates
    add_songs_to_playlist(playlist_id, song_ids)
    
    # Unlike the songs that were added to the playlist
    unlike_songs(song_ids)
    
    print(f"Added {len(song_ids)} songs to '{playlist_name}' and unliked them.")

if __name__ == '__main__':
    main()
