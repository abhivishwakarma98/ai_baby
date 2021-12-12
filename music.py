import os


def music1():
    music_dir ="C:\\New folder\\SONG"
    songs = os.listdir(music_dir)
    print(songs)    
    os.startfile(os.path.join(music_dir, songs[0]))
        