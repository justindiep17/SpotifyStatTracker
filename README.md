## What Is SpotifyStatTracker?
SpotifyStatTracker is a Python program that analyzes and tracks a user's Spotify listening habits and statistics. At the end of every week, an email is sent to the user detailing various statistics about their listening habits. Tracked statistics include stats like a user's most played song, how many minutes of music they listened to, and their current favorite artist. 

## How Does It Work?
This program utilises the Spotify API and the Spotipy library in order to collect data about the user's Spotify listening history. In order for this data to be collected regularly so accurate weekly statistics can be calculated, this program runs every 10 minutes on a  PythonAnywhere cloud. User data from the Spotify API is fetched by the program every time it run. The program then compares the new data to the current data and appends the new data points not yet stored. This data is stored in a local json file for easy access.

At the end of every week, the program will parse the data from the json file and calculate various statistics from it. More specifically, these stats would be:
  - Most Played Song
  - Most Played Artist
  - Most Played Album
  - Number of Songs Played
  - Number of Minutes Listened

In addition to generating stats about a user's listening habits, the program will generate a custom playlist of each unique song played by the use that week. This playlist will then be added directly to the user's Spotify profile. Using the smtplib library, a custom email with the listenings stats and a link to the playlist are sent to the user's email. Once this is all complete, the program wipes the previous week's data and starts tracking anew.

**NOTE**

In order for this program to work, a config.py needs to be implemented by the current user. All constants from config.py, such as TO_EMAIL and FROM_EMAIL, must be filled in by that user. As well, the user must connect themselves to the Spotify API.
