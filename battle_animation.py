import tkinter as tk
from tkinter import messagebox, PhotoImage
from PIL import Image, ImageTk
import random
import time
import json

import tkinter as tk

from matplotlib import text

class battle_anim(tk.Frame):
    def __init__(self, master):
        super().__init__(master)

        with open("battle_temp.txt", "r", encoding="utf-8") as f:
            self.battle_list = json.load(f)
        self.action = self.battle_list

        with open("player_stat_temp.txt", "r", encoding="utf-8") as f:
            self.player_stat = json.load(f)
        self.my_stat = self.player_stat

        with open("enemy_stat_temp.txt", "r", encoding="utf-8") as f:
            self.enemy_stat = json.load(f)
        self.enm_stat = self.enemy_stat

        # --- memanggil background image dari folder assets dan dijadikan background wallpaper ---
        # mengambil file dari folder assets dan menaruhnya di label
        bg_pil = Image.open("assets/test-image2.jpg")
        bg_pil = bg_pil.resize((450, 450))
        bg_img = ImageTk.PhotoImage(bg_pil)
        bg_lbl = tk.Label(self, image=bg_img)
        # image reference untuk mencegah garbage collection
        bg_lbl.image = bg_img
        # posisi label background image relatif pada window
        bg_lbl.place(x=0, y=0, relwidth=1, relheight=1)      

        # --- formatting penempatan label dan tombol ---
        self.grid_rowconfigure(1, weight=2)
        self.grid_rowconfigure(6, weight=1)
        for i in range(5):
            self.grid_columnconfigure(i, weight=1)

        # --- penempatan label ---
        self.enemyinfo_lbl = tk.Label(self, text="Monster\n3 HP", font=("Arial", 20))
        self.enemyinfo_lbl.grid(row=0, column=3, padx=10, pady=10, sticky="e")

        self.playerinfo_lbl = tk.Label(self, text="[Kimi No Nawa]\n10 HP", font=("Arial", 20))
        self.playerinfo_lbl.grid(row=0, column=1, padx=10, pady=10, sticky="e")

        self.battleinfo_lbl = tk.Label(self, text="", font=("Arial", 12), anchor='center', width=50)
        self.battleinfo_lbl.grid(row=3, column=1, columnspan=3)

        # --- penempatan tombol battle system ---
        self.player_act_anim()

        if self.enm_stat[0] <= 0:
            self.update_battle_info("Monster telah dikalahkan!")
            messagebox.showinfo("Battle Result", "Anda telah mengalahkan monster!")
            self.goto_main_menu()


        self.enemy_act_anim()

        if self.my_stat[0] <= 0:
            self.update_battle_info("Anda kalah!")
            messagebox.showinfo("Battle Result", "Anda telah kalah!")
            self.goto_main_menu()
        
        self.update_battle_info("")


    def update_my_stat(self,word):
        self.playerinfo_lbl.config(text=word)

    def update_enemy_stat(self,word):
        self.enemyinfo_lbl.config(text=word)

    def player_act_anim(self):
        if self.action[0] != 0:
            self.update_battle_info(f"Anda menyerang monster sebanyak {self.action[0]} HP!")
            time.sleep(2)

        if self.action[1] != 0:
            self.update_battle_info(f"Anda menyerang monster sebanyak {self.action[1]} HP!")
            time.sleep(0.1)
            self.update_my_stat(f"[Kimi No Nawa]\n{self.my_stat[0]} HP (+{self.action[1]})")
            time.sleep(2)

        if self.action[2] != 0:
            self.update_battle_info(f"Anda menyerang monster sebanyak {self.action[2]} HP!")
            time.sleep(0.1)
            self.update_my_stat(f"[Kimi No Nawa]\n{self.my_stat[0] + self.action[2]} HP")
            time.sleep(2)
    
    def enemy_act_anim(self):
        self.enemy_action = random.randint(1,7)
        if self.enemy_action == 1 or self.enemy_action == 2 or self.enemy_action == 3 or self.enemy_action == 4:
            self.update_battle_info("Monster menyerang Anda!")
            time.sleep(0.1)
            attack_damage = random.randint(1, 3)  # Simulasi kerusakan serangan monster
            self.update_my_stat(f"[Kimi No Nawa]\n{self.my_stat[0] - attack_damage} HP")
            time.sleep(2)
        elif self.enemy_action == 5 or self.enemy_action == 6:
            block_value = random.randint(1, 2)  # Simulasi nilai blokir monster
            self.update_battle_info("Monster memblokir serangan Anda!")
            time.sleep(2)
        elif self.enemy_action == 7:
            self.update_battle_info("Monster menyembuhkan diri!")
            time.sleep(0.1)
            self.update_enemy_stat(f"Monster\n{self.act_point[0] + 1} HP")
            time.sleep(2)

    def update_action_info(self, word):
        self.actioninfo_lbl.config(text=word)

    def update_battle_info(self, word):
        self.battleinfo_lbl.config(text=word)

    def reset_action(self):
        self.action = ['','','']
        self.update_action_info(f"Action Anda:\n{self.action[0]}\n{self.action[1]}\n{self.action[2]}")
        self.update_battle_info("")

    def goto_main_menu(self):
        from main_menu import open_menu
        self.master.show_page(open_menu)
        