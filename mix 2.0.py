import pygame
filepath = r"H:\CloudMusic\Wolfgang Amadeus Mozart - 小星星变奏曲.mp3"
pygame.mixer.init()
pygame.mixer.music.load(filepath)
pygame.mixer.music.play(start=0.0)
#pygame.mixer.music.stop()