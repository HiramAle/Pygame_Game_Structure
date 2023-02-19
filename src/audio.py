import os

import pygame
from src.config import Config


class Audio:
    sounds: dict[str, pygame.mixer.Sound] = {}
    music: dict[str, pygame.mixer.Sound] = {}
    volume = 0.06

    def __init__(self):
        for sound_path in os.listdir(Config.SOUNDS_PATH):
            sound_name = sound_path.split(".")[0]
            self.sounds[sound_name] = pygame.mixer.Sound(f"{Config.SOUNDS_PATH}/{sound_path}")

    def play_sound(self, sound: str):
        self.sounds[sound].set_volume(self.volume)
        pygame.mixer.Sound.play(self.sounds[sound])

    def stop_sound(self, sound: str):
        self.sounds[sound].stop()

    def fade_out_sound(self, sound: str, time_seconds: int):
        self.sounds[sound].fadeout(time_seconds * 1000)
