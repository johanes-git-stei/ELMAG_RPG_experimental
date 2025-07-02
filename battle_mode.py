import tkinter as tk
from tkinter import messagebox, PhotoImage
from PIL import Image, ImageTk
import os
import json

import tkinter as tk

from matplotlib import text

class start_battle(tk.Frame):
    def __init__(self, master):
        super().__init__(master)

        with open("battle_temp.txt", "w", encoding="utf-8") as f:
            json.dump([0,0,0], f)

        self.action = ['','','']
        self.act_point = [0,0,0]
        
        # Load player stats
        with open("player_stat_temp.txt", "r", encoding="utf-8") as f:
            self.my_stat = json.load(f)
        
        # Load enemy stats
        with open("enemy_stat_temp.txt", "r", encoding="utf-8") as f:
            self.enm_stat = json.load(f)

        self.att_val = 1
        self.blk_val = 1
        self.hel_val = 1

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
        if self.enm_stat[1] != 0:
            self.enemyinfo_lbl = tk.Label(self, text=f"Monster\n{self.enm_stat[0]} HP (+{self.enm_stat[1]})", font=("Arial", 20))
            self.enemyinfo_lbl.grid(row=0, column=3, padx=10, pady=10, sticky="e")
        else:
            self.enemyinfo_lbl = tk.Label(self, text=f"Monster\n{self.enm_stat[0]} HP", font=("Arial", 20))
            self.enemyinfo_lbl.grid(row=0, column=3, padx=10, pady=10, sticky="e")

        if self.my_stat[1] != 0:
            self.playerinfo_lbl = tk.Label(self, text=f"[Kimi No Nawa]\n{self.my_stat[0]} HP (+{self.my_stat[1]})", font=("Arial", 20))
            self.playerinfo_lbl.grid(row=0, column=1, padx=10, pady=10, sticky="e")
        else:
            self.playerinfo_lbl = tk.Label(self, text=f"[Kimi No Nawa]\n{self.my_stat[0]} HP", font=("Arial", 20))
            self.playerinfo_lbl.grid(row=0, column=1, padx=10, pady=10, sticky="e")

        self.actioninfo_lbl = tk.Label(self, text=f"Action Anda:\n{self.action[0]}\n{self.action[1]}\n{self.action[2]}", width=25, wraplength=200, height=6, font=("Arial", 15))
        self.actioninfo_lbl.grid(row=0, column=2)

        self.battleinfo_lbl = tk.Label(self, text="", font=("Arial", 12), anchor='center', width=50)
        self.battleinfo_lbl.grid(row=3, column=1, columnspan=3)

        # --- penempatan tombol battle system ---
        self.attack_btn = tk.Button(self, text="Attack!", command=lambda: self.add_action('Attack'), width=25, height=2)
        self.attack_btn.grid(row=4, column=1, padx=(5,5), pady=15)

        self.block_btn = tk.Button(self, text="Block!", command=lambda: self.add_action('Block'), width=25, height=2)
        self.block_btn.grid(row=4, column=2, padx=(5,5), pady=15)

        self.heal_btn = tk.Button(self, text="Heal!", command=lambda: self.add_action('Heal'), width=25, height=2)
        self.heal_btn.grid(row=4, column=3, padx=(5,5), pady=15)

        self.surrend_btn = tk.Button(self, text="Surrender!",command=self.goto_main_menu, width=25, height=2)
        self.surrend_btn.grid(row=5, column=1, padx=(5,5), pady=15)

        self.commitact_btn = tk.Button(self, text="Commit!", command=self.goto_start_question, width=25, height=2)
        self.commitact_btn.grid(row=5, column=2, padx=(5,5), pady=15)

        self.resetact_btn = tk.Button(self, text="Reset Action.",command=self.reset_action, width=25, height=2)
        self.resetact_btn.grid(row=5, column=3, padx=(5,5), pady=15)

    def goto_main_menu(self):
        if messagebox.askokcancel("Surrender?", "Do you want to surrender the game?"):
            self.reset_action()
            from main_menu import open_menu
            self.master.show_page(open_menu)

    def goto_start_question(self):
        if self.action == ['','','']:
            messagebox.showwarning("Warning", "You must select at least one action before committing.")
            return
        elif self.action != ['','','']:
            if messagebox.askokcancel("Commit?", "Are you sure you want to commit your action?"):  
                for i in range(3):
                    if self.action[i] == 'Attack':
                        self.act_point[0] += self.att_val
                    elif self.action[i] == 'Block':
                        self.act_point[1] += self.blk_val
                    elif self.action[i] == 'Heal':
                        self.act_point[2] += self.hel_val

                # Open (or create) 'battle_temp.txt' in write mode and write the text
                with open("battle_temp.txt", "w", encoding="utf-8") as f:
                    json.dump(self.act_point, f)

                self.act_point = [0,0,0]  # Reset action points after committing
                self.reset_action()
                from question_mode import start_question
                self.master.show_page(start_question)

    def update_action_info(self, word):
        self.actioninfo_lbl.config(text=word)

    def update_battle_info(self, word):
        self.battleinfo_lbl.config(text=word)

    def add_action(self, words):
        for t in range(3):
            if self.action[t] == '':
                self.action[t] = f"{words}"
                self.update_action_info(f"Action Anda:\n{self.action[0]}\n{self.action[1]}\n{self.action[2]}")
                break
            elif self.action[2] != '':
                self.update_battle_info(f"Anda tidak memiliki action point lagi!")
                break
                # FU*CKDKCKKCCKk
    
    def reset_action(self):
        self.action = ['','','']
        self.update_action_info(f"Action Anda:\n{self.action[0]}\n{self.action[1]}\n{self.action[2]}")
        self.update_battle_info("")
        