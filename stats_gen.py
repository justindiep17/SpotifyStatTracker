def create_track_list(data_dict):
    all_tracks_played = []  # Keeps Track of Every Track Played This Week
    for i in range(0, len(data_dict['albums'])):
        new_track = (data_dict['song_names'][i], data_dict['albums'][i], data_dict['artists'][i], data_dict['track_ids'][i])
        all_tracks_played.append(new_track)
    return all_tracks_played


def equal_tracks(track1, track2):
    if track1[3] == track2[3]:
        return True
    else:
        return False

def calc_most_freq_played_song(tracks: list):
    freq_tracker = {}
    ans = ()
    max_freq = 0
    for track in tracks: # Loop Through Each Track in Tracks
        if track in freq_tracker: # If Track In freq_tracker (Already In Dict)
            freq_tracker[track] += 1
        else:
            freq_tracker[track] = 1
        if freq_tracker[track] > max_freq:
            max_freq = freq_tracker[track]
            ans = track
    return ans, max_freq


def calc_most_freq_played_album(tracks: list):
    freq_tracker = {}
    ans = ()
    max_freq = 0
    album_lst = [(track[1], track[2]) for track in tracks]
    for album in album_lst:
        if album in freq_tracker:
            freq_tracker[album] += 1
        else:
            freq_tracker[album] = 1
        if freq_tracker[album] > max_freq:
            max_freq = freq_tracker[album]
            ans = album
    return ans


def calc_most_freq_played_artist(tracks: list):
    freq_tracker = {}
    ans = ()
    max_freq = 0
    artist_lst = [track[2] for track in tracks]
    for artist in artist_lst:
        if artist in freq_tracker:
            freq_tracker[artist] += 1
        else:
            freq_tracker[artist] = 1
        if freq_tracker[artist] > max_freq:
            max_freq = freq_tracker[artist]
            ans = artist
    return ans

