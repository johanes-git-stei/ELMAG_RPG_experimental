import tkinter as tk
from tkinter import messagebox
from PIL import Image, ImageTk
import random
import json

class battle_anim(tk.Frame):
    def __init__(self, master):
        super().__init__(master)
        


        # Load battle actions
        with open("battle_temp.txt", "r", encoding="utf-8") as f:
            self.action = json.load(f)
        
        # Load player stats
        with open("player_stat_temp.txt", "r", encoding="utf-8") as f:
            self.my_stat = json.load(f)
        
        # Load enemy stats
        with open("enemy_stat_temp.txt", "r", encoding="utf-8") as f:
            self.enm_stat = json.load(f)

        # Background image
        bg_pil = Image.open("assets/test-image2.jpg").resize((450, 450))
        bg_img = ImageTk.PhotoImage(bg_pil)
        bg_lbl = tk.Label(self, image=bg_img)
        bg_lbl.image = bg_img
        bg_lbl.place(x=0, y=0, relwidth=1, relheight=1)

        # Grid configuration
        self.grid_rowconfigure(1, weight=2)
        self.grid_rowconfigure(6, weight=1)
        for i in range(3):
            self.grid_columnconfigure(i, weight=1)

        # Labels
        if self.enm_stat[1] != 0:
            self.enemyinfo_lbl = tk.Label(self, text=f"Monster\n{self.enm_stat[0]} HP (+{self.enm_stat[1]})", font=("Arial", 20))
            self.enemyinfo_lbl.grid(row=0, column=2, padx=10, pady=10, sticky="e")
        else:
            self.enemyinfo_lbl = tk.Label(self, text=f"Monster\n{self.enm_stat[0]} HP", font=("Arial", 20))
            self.enemyinfo_lbl.grid(row=0, column=2, padx=10, pady=10, sticky="e")

        if self.my_stat[1] != 0:
            self.playerinfo_lbl = tk.Label(self, text=f"[Kimi No Nawa]\n{self.my_stat[0]} HP (+{self.my_stat[1]})", font=("Arial", 20))
            self.playerinfo_lbl.grid(row=0, column=0, padx=10, pady=10, sticky="w")
        else:
            self.playerinfo_lbl = tk.Label(self, text=f"[Kimi No Nawa]\n{self.my_stat[0]} HP", font=("Arial", 20))
            self.playerinfo_lbl.grid(row=0, column=0, padx=10, pady=10, sticky="w")

        self.battleinfo_lbl = tk.Label(self, text="", font=("Arial", 12), width=50, anchor='center')
        self.battleinfo_lbl.grid(row=3, column=0, columnspan=3)

        # Start the first player action after a short delay
        self.after(2000, self.player_att_check)

    def update_my_stat(self,word):
        self.playerinfo_lbl.config(text=word)

    def update_enemy_stat(self,word):
        self.enemyinfo_lbl.config(text=word)

    def update_battle_info(self, word):
        self.battleinfo_lbl.config(text=word)

    def player_att_check(self):
        if self.action[0] != 0:
            dmg = self.action[0]
            self.update_battle_info(f"Anda menyerang monster sebanyak {dmg} HP!")
            if self.enm_stat[1] != 0:
                if dmg < self.enm_stat[1]:
                    self.enm_stat[1] -= dmg
                    self.after(2000, lambda: self.update_battle_info(f"serangan anda diblokir sebanyak {self.enm_stat[1]} HP!"))
                    self.update_enemy_stat(f"Monster\n{self.enm_stat[0]} HP (+{self.enm_stat[1]})")
                elif dmg == self.enm_stat[1]:
                    self.enm_stat[1] = 0
                    self.after(2000, lambda: self.update_battle_info(f"serangan anda diblokir sebanyak {self.enm_stat[1]} HP!"))
                elif dmg > self.enm_stat[1]:
                    self.enm_stat[0] -= (dmg - self.enm_stat[1])
                    self.enm_stat[1] = 0
                    self.after(2000, lambda: self.update_battle_info(f"serangan anda diblokir sebanyak {self.enm_stat[1]} HP!"))
                    self.update_enemy_stat(f"Monster\n{self.enm_stat[0]} HP)")
            else:
                self.enm_stat[0] -= dmg
                self.update_enemy_stat(f"Monster\n{self.enm_stat[0]} HP")
            self.after(2000, lambda: self.player_blk_check())
        else:
            # proceed to enemy turn
            self.after(2000, lambda: self.player_blk_check())

    def player_blk_check(self):
        if self.action[1] != 0:
            self.my_stat[1] += self.action[1]
            self.update_battle_info(f"Anda dapat memblokir serangan monster sebanyak {self.action[1]} HP!")
            self.update_my_stat(f"[Kimi No Nawa]\n{self.my_stat[0]} HP (+{self.action[1]})")
            self.after(2000, lambda: self.player_hel_check())
        else:
            # proceed to enemy turn
            self.after(2000, lambda: self.player_hel_check())

    def player_hel_check(self):
        if self.action[2] != 0:
            heal = self.action[2]
            self.update_battle_info(f"Anda menyembuhkan diri sebanyak {heal} HP!")
            self.my_stat[0] += heal
            if self.my_stat[0] > 10:  # Assuming max HP is 10
                self.my_stat[0] = 10
            if self.my_stat[1] != 0:
                self.update_my_stat(f"[Kimi No Nawa]\n{self.my_stat[0]} HP (+{self.my_stat[1]})")
            else:
                self.update_my_stat(f"[Kimi No Nawa]\n{self.my_stat[0]} HP")
            self.after(2000, lambda: self.enemy_act_step())
        else:
            # proceed to enemy turn
            self.after(2000, lambda: self.enemy_act_step())

    def enemy_act_step(self):

        #randomizer
        from rng import lcg

        action = max(1, lcg(0) % 8)
        if action <= 4:
            self.after(0, lambda: self.finish_enemy_attack())
        elif action <= 6:
            self.after(0, lambda: self.finish_enemy_block())
        else:
            self.after(0, lambda: self.finish_enemy_heal())

    def finish_enemy_attack(self):
        self.update_battle_info("Monster menyerang Anda!")

        #randomizer
        from rng import lcg

        dmg = max(1, lcg(0) % 4)
        if self.my_stat[1] != 0:
            if dmg < self.my_stat[1]:
                self.my_stat[1] -= dmg
                self.update_my_stat(f"[Kimi No Nawa]\n{self.my_stat[0]} HP (+{self.my_stat[1]})")
            elif dmg == self.my_stat[1]:
                self.my_stat[1] = 0
                self.update_my_stat(f"[Kimi No Nawa]\n{self.my_stat[0]} HP")
            elif dmg > self.my_stat[1]:
                self.my_stat[0] -= (dmg - self.my_stat[1])
                self.my_stat[1] = 0
                self.update_my_stat(f"[Kimi No Nawa]\n{self.my_stat[0]} HP")
        else:
            self.my_stat[0] -= dmg
            self.update_my_stat(f"[Kimi No Nawa]\n{self.my_stat[0]} HP")
        self.after(2000, lambda: (self.update_battle_info(""), self.after(0, self.check_end_conditions())))

    def finish_enemy_heal(self):
        self.update_battle_info("Monster menyembuhkan diri!")
        self.enm_stat[0] += 1
        if self.enm_stat[0] > 3:  # Assuming max HP is 3
            self.enm_stat[0] = 3
        if self.enm_stat[1] != 0:
            self.update_enemy_stat(f"Monster\n{self.enm_stat[0]} HP (+{self.enm_stat[1]})")
        self.update_enemy_stat(f"Monster\n{self.enm_stat[0]} HP")
        self.after(2000, lambda: (self.update_battle_info(""), self.after(0, self.check_end_conditions())))

    def finish_enemy_block(self):

        #randomizer
        from rng import lcg

        self.update_battle_info("Monster memblokir serangan Anda!")
        block = max(1, lcg(0) % 3)
        self.enm_stat[1] += block
        self.update_enemy_stat(f"Monster\n{self.enm_stat[0]} HP (+{block})")
        self.after(2000, lambda: (self.update_battle_info(""), self.after(0, self.check_end_conditions())))

    def check_end_conditions(self):
        if self.enm_stat[0] <= 0:
            self.update_battle_info("Monster telah dikalahkan!")
            messagebox.showinfo("Battle Result", "Anda telah mengalahkan monster!")
            self.reset_all_stat()
            self.goto_main_menu()
        elif self.my_stat[0] <= 0:
            self.update_battle_info("Anda kalah!")
            messagebox.showinfo("Battle Result", "Anda telah kalah!")
            self.reset_all_stat()
            self.goto_main_menu()
        else:
            self.update_battle_info("")
            self.goto_start_battle()

    def reset_all_stat(self):
        self.reset_action = [0,0,0]  # Reset action points
        with open("battle_temp.txt", "w", encoding="utf-8") as f:
                json.dump(self.reset_action, f)

        with open("player_stat_temp.txt", "w", encoding="utf-8") as f:
                json.dump([10,0], f)

        with open("enemy_stat_temp.txt", "w", encoding="utf-8") as f:
                json.dump([3,0], f)

    def goto_start_battle(self):
        self.reset_action = [0,0,0]  # Reset action points
        with open("battle_temp.txt", "w", encoding="utf-8") as f:
                json.dump(self.reset_action, f)

        with open("player_stat_temp.txt", "w", encoding="utf-8") as f:
                json.dump(self.my_stat, f)

        with open("enemy_stat_temp.txt", "w", encoding="utf-8") as f:
                json.dump(self.enm_stat, f)

        from battle_mode import start_battle
        self.master.show_page(start_battle)



    def goto_main_menu(self):
        from main_menu import open_menu
        self.master.show_page(open_menu)
