# Spotify Liked To Playlist
![Python](https://img.shields.io/badge/Python-3.x-blue.svg)
![Spotipy](https://img.shields.io/badge/Spotipy-2.19.0-green.svg)
![License](https://img.shields.io/badge/License-MIT-yellow.svg)

## Overview

**Spotify Liked To Playlist** is a Python application that automates the process of organizing your Spotify liked songs by adding them to a specific playlist. This tool allows you to gather all your liked songs in one place, avoiding duplicates and keeping your library clean by unliking the songs after they've been added to the playlist.

## Features

- Automatically creates a playlist if it doesn’t exist or adds songs to an existing one.
- Checks for duplicates to avoid adding the same song multiple times.
- Unlikes songs after they’ve been added to the specified playlist.
- Simple and user-friendly output indicating the status of each song added.

## Prerequisites

To run this application, you'll need:

- Python 3.x installed on your system.
- A Spotify account (free or premium).
- An application registered on the Spotify Developer Dashboard to obtain your API credentials.

## Installation

1. **Clone the repository**:

   ```bash
   git clone https://github.com/yourusername/spotify-liked-to-playlist.git
   cd spotify-liked-to-playlist
   ```

2. **Set up a virtual environment** (optional but recommended):

   ```bash
   python -m venv venv
   source venv/bin/activate  # On Windows: venv\Scripts\activate
   ```

3. **Install the required packages**:

   ```bash
   pip install -r requirements.txt
   ```

4. **Create a `.env` file** in the project directory and add your Spotify API credentials:

   ```plaintext
   SPOTIPY_CLIENT_ID='your_spotify_client_id'
   SPOTIPY_CLIENT_SECRET='your_spotify_client_secret'
   SPOTIPY_REDIRECT_URI='http://localhost:8888/callback'
   ```

## Usage

1. Modify the `playlist_name` variable in the script to the desired playlist name where liked songs will be stored.
2. Run the script:

   ```bash
   python spotify_liked_to_playlist.py
   ```

3. Complete the authentication process in your browser to authorize the app with your Spotify account.

## Notes

- This application works with all songs in your liked songs library.
- Ensure an active internet connection to add songs to Spotify.

## License

This project is licensed under the MIT License. See the [LICENSE](LICENSE) file for details.

## Acknowledgments

- [Spotipy](https://spotipy.readthedocs.io/en/2.19.0/) - A Python library for the Spotify Web API.

