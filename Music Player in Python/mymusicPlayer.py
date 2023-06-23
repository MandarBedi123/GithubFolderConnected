import os
import pygame

def MusicPlayingFunction(file_path):
    pygame.mixer.init()
    pygame.mixer.music.load(file_path)
    pygame.mixer.music.play()

MusicList=os.listdir()
for Song in MusicList:
    if Song.endswith('.mp3')==True:
        print(Song+' is playing.')
        MusicPlayingFunction(Song)
        while pygame.mixer.music.get_busy():
            print("\nIt is infinity input loop so it will ask you untill the list stops.")
            print("When the song stops playing, type 'c' to play next song.")
            a=input("Type 'y' for skip this song, Type 'q' to quit the list, Type 'c' to continue with this song, Type 'p' to pause song: ")
            if a=='y':
                print(Song+'.mp3 is skipped.\n')
                break
            while a=='p':
                pygame.mixer.music.pause()
                print('The song is paused.')
                if input("Type 'r' to resume song: ")=='r':    
                    pygame.mixer.music.unpause()
                    break
                else: print('Invalid value.') 
            if a=='q':
                print('The list is over.')
                exit()    
            else: 
                print('Plz type the correct value')
print('The list is over.')