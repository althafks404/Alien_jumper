import pygame
from util import Loader
class Assets:
    def background_image():
        background_image = Loader.load_image('/ground.png')
        return background_image
    
    def background_sky():
        background_sky = Loader.load_image('/Sky.png')
        return background_sky
    
    def score_font():
        score_font  = Loader.load_font('/Pixeltype.ttf')
        return score_font
    
    def background_audio():
        backgrou_audio =  Loader.load_sound('music.wav')
        return backgrou_audio
    
    def jump_audio():
        jump_audio = Loader.load_sound('jump.mp3')
        return jump_audio
        