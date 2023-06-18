import pygame

def MusicStoppingFunction():
    pygame.mixer.music.stop()

def MusicPlayingFunction(file_path):
    pygame.mixer.init()
    pygame.mixer.music.load(file_path)
    pygame.mixer.music.play()
    

MusicList=['Aathma Raama 2023','Maan Meri Jaan']

for i in range(len(MusicList)):
    song=MusicList[i]
    print(str(song)+' is playing.')
    file_path ="C:/Users/VCM/Desktop/code clause Internship project/Music Player in Python/"+str(song)+".mp3"
    MusicPlayingFunction(file_path) 
    # if(input("For skip this song, type 'y'else 'n': ")=='y'):
    #     MusicStoppingFunction()
    while pygame.mixer.music.get_busy():
        continue
    MusicStoppingFunction()
print('Your Music List is over.')