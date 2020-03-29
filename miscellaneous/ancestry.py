def playlist(songs, current_song_index, target_song_name):
    # Write your code here
    songs_len = len(songs) - 1
    target_indexes = [i for i,v in enumerate(songs) if str(v) == target_song_name] #All the index for the target_song_name
    #direction
    #diff_abs_current = abs(current_song_index-songs_len) #index with respect to the actual songs
    #diff_abs_target = [abs(current_song_index-ti) for ti in target_indexes]
    #diff_abs_target_len = [abs(songs_len-ti) for ti in target_indexes]
    #print(diff_abs_current, diff_abs_target, diff_abs_target_len) #6 [2, 3, 5]
    min_dist = min(target_indexes)
    max_dist = max(target_indexes)
    min_dist_start = abs(current_song_index-min_dist)
    current_song_index_last = songs_len + current_song_index
    min_dist_end = abs(current_song_index_last - max_dist)
    return min(min_dist_start,min_dist_end+1)

    # 5 [2, 3, 5] [3, 2, 0]
pl = ['dancinginthedark','rio','t','liveoak','liveoak','0','liveoak','3']
pl = ['4','wheniseeyouagain','borntorun','othingelsematters','cecelia','1','cecelia']
playlist(pl,2,'cecelia')
#playlist(pl,0,'liveoak')