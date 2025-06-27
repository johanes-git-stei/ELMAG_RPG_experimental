# honestly i m clueless here 

import tkinter as tk
from tkinter import messagebox, PhotoImage
from PIL import Image, ImageTk
import os

class boost():
    def __init__(self, master):
        super().__init__(master)

        # randomizer
        from rng import lcg

        # randomly choose which stat to be boosted
        stat_draw = lcg(0) % 3

        # the idea is if the total stat is 100, max boost should be 10 percent
        self.rng_boost = max(1, lcg(0) % 11)

        # maybe not the best idea to put stat here, better to fetch it somewhere else
        self.player_attack_stat = 0
        self.player_heal_stat = 0
        self.player_block_stat = 0

        if stat_draw == 0:
            self.player_attack_stat += self.rng_boost
        elif stat_draw == 1:
            self.player_heal_stat += self.rng_boost
        elif stat_draw == 2:
            self.player_block_stat += self.rng_boost

        ## need return self.player_stat or smth

# basically the minus version of boost, for enemy
class debuff():
     def __init__(self, master):
        super().__init__(master)

        # randomizer
        from rng import lcg

        # randomly choose which stat to be debuffed
        stat_draw = lcg(0) % 3

        # the idea is if the total stat is 100, max debuff should be 10 percent
        # prioritizing the least amount this time because why not lol
        self.rng_debuff = min(lcg(0) % 10, 10)

        # maybe not the best idea to put stat here, better to fetch it somewhere else
        self.enemy_attack_stat = 100
        self.enemy_heal_stat = 100
        self.enemy_block_stat = 100

        if stat_draw == 0:
            self.enemy_attack_stat += self.rng_boost
        elif stat_draw == 1:
            self.enemy_heal_stat += self.rng_boost
        elif stat_draw == 2:
            self.enemy_block_stat += self.rng_boost