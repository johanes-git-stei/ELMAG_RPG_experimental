import tkinter as tk
from tkinter import messagebox, PhotoImage
from PIL import Image, ImageTk
import os

import tkinter as tk

class start_battle(tk.Frame):

    def __init__(self, master):
        super().__init__(master)

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
        self.grid_rowconfigure(3, weight=2)
        self.grid_rowconfigure(6, weight=1)
        self.grid_columnconfigure(0, weight=1)
        self.grid_columnconfigure(3, weight=3)

        # --- penempatan label ---
        self.enemyinfo_lbl = tk.Label(self, text="Monster", font=("Arial", 20))
        self.enemyinfo_lbl.grid(row=1, column=1, columnspan=2, padx=10, pady=10)
        self.enemyinfo_lbl = tk.Label(self, text="100/100", font=("Arial", 15))
        self.enemyinfo_lbl.grid(row=2, column=1, columnspan=2, padx=10, pady=10)

        # --- penempatan tombol return to menu ---
        self.return_btn = tk.Button(self, text="Return to menu",command=self.goto_main_menu, height=2)
        self.return_btn.grid(row=0, column=0, padx=(10,20), pady=15, sticky="w")

        # --- penempatan tombol battle system ---
        self.attack_btn = tk.Button(self, text="Attack!", command=self.goto_attack_menu, width=20, height=2)
        self.attack_btn.grid(row=4, column=1, padx=(10,20), pady=15)

        self.block_btn = tk.Button(self, text="Block!", width=20, height=2)
        self.block_btn.grid(row=4, column=2, padx=(20,10), pady=15)

        self.heal_btn = tk.Button(self, text="Heal!", width=20, height=2)
        self.heal_btn.grid(row=5, column=1, padx=(10,20), pady=15)

        self.surrend_btn = tk.Button(self, text="Surrender!",command=self.goto_main_menu, width=20, height=2)
        self.surrend_btn.grid(row=5, column=2, padx=(20,10), pady=15)

    def goto_main_menu(self):
        from main_menu import open_menu
        self.master.show_page(open_menu)

    def goto_attack_menu(self):
        self.master.show_page(start_attack)

class start_attack(tk.Frame):

    def __init__(self, master):
        super().__init__(master)

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
        self.grid_rowconfigure(7, weight=1)
        self.grid_columnconfigure(0, weight=1)
        self.grid_columnconfigure(3, weight=3)

        # --- penempatan label ---
        self.enemyinfo_lbl = tk.Label(self, text="Pilihlah Bab yang ingin kamu kerjakan!", font=("Arial", 15))
        self.enemyinfo_lbl.grid(row=2, column=1, columnspan=2, padx=10, pady=10)

        # --- penempatan tombol return to menu ---
        self.return_btn = tk.Button(self, text="Return to battle menu", command=self.goto_battle_menu, height=2)
        self.return_btn.grid(row=0, column=0, padx=(10,20), pady=15, sticky="w")

        # --- penempatan tombol battle system ---
        self.bab1_btn = tk.Button(self, text="Bab I", command=self.goto_attack_diffc, width=20, height=2)
        self.bab1_btn.grid(row=4, column=1, padx=(10,20), pady=15)

        self.bab2_btn = tk.Button(self, text="Bab II", command=self.goto_attack_diffc, width=20, height=2)
        self.bab2_btn.grid(row=4, column=2, padx=(20,10), pady=15)

        self.bab3_btn = tk.Button(self, text="Bab III", command=self.goto_attack_diffc, width=20, height=2)
        self.bab3_btn.grid(row=5, column=1, padx=(10,20), pady=15)

        self.bab4_btn = tk.Button(self, text="Bab IV", command=self.goto_attack_diffc, width=20, height=2)
        self.bab4_btn.grid(row=5, column=2, padx=(20,10), pady=15)

        self.bab5_btn = tk.Button(self, text="Bab V", command=self.goto_attack_diffc, width=20, height=2)
        self.bab5_btn.grid(row=6, column=1, padx=(10,20), pady=15)

        self.random_btn = tk.Button(self, text="Pilih acak!", command=self.goto_attack_diffc, width=20, height=2)
        self.random_btn.grid(row=6, column=2, padx=(20,10), pady=15)

    def goto_battle_menu(self):
        self.master.show_page(start_battle)

    def goto_attack_diffc(self):
        self.master.show_page(attack_diffc)

class attack_diffc(tk.Frame):

    def __init__(self, master):
        super().__init__(master)

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
        self.grid_rowconfigure(4, weight=1)
        self.grid_columnconfigure(0, weight=1)
        self.grid_columnconfigure(3, weight=3)

        # --- penempatan label ---
        self.enemyinfo_lbl = tk.Label(self, text="Pilih tipe soal yang ingin kamu kerjakan!", font=("Arial", 15))
        self.enemyinfo_lbl.grid(row=2, column=1, columnspan=2, padx=10, pady=10)

        # --- penempatan tombol return to menu ---
        self.return_btn = tk.Button(self, text="Return to attack menu",command=self.goto_attack_menu, height=2)
        self.return_btn.grid(row=0, column=0, padx=(10,20), pady=15, sticky="w")

        # --- penempatan tombol battle system ---
        self.bab1_btn = tk.Button(self, text="Pilihan ganda (Spell level: easy, 50 atk dmg)", command=self.goto_pilgan, wraplength=150, width=20)
        self.bab1_btn.grid(row=3, column=1, padx=(10,20), pady=15)

        self.bab2_btn = tk.Button(self, text="Esai singkat (Spell level: advance, 100 atk dmg)", command=self.goto_esai_singkat, wraplength=150, width=20)
        self.bab2_btn.grid(row=3, column=2, padx=(20,10), pady=15)

    def goto_attack_menu(self):
        self.master.show_page(start_attack)

    def goto_pilgan(self):
        from spell_question import pilgan
        self.master.show_page(pilgan)

    def goto_esai_singkat(self):
        from spell_question import esai_singkat
        self.master.show_page(esai_singkat)