import tkinter as tk
from tkinter import messagebox, PhotoImage
from PIL import Image, ImageTk
import os

class pilgan(tk.Frame):

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
        self.grid_rowconfigure(5, weight=1)
        self.grid_columnconfigure(0, weight=1)
        self.grid_columnconfigure(3, weight=3)

        # --- pemanggilan file image untuk soal dan jawaban ---
        # *soal
        soal_path = "assets/test-image3.png"
        soal = Image.open(soal_path)
        soal_img = soal.resize((300,160))  # Optional resize
        question = ImageTk.PhotoImage(soal_img)

        # *jawaban
        # a.
        jwb_path = "assets/test-image3.png"
        jawab = Image.open(jwb_path)
        jawab_img = jawab.resize((100,50))  # Optional resize
        answerA = ImageTk.PhotoImage(jawab_img)
        # b.
        jwb_path = "assets/test-image3.png"
        jawab = Image.open(jwb_path)
        jawab_img = jawab.resize((100,50))  # Optional resize
        answerB = ImageTk.PhotoImage(jawab_img)
        # c.
        jwb_path = "assets/test-image3.png"
        jawab = Image.open(jwb_path)
        jawab_img = jawab.resize((100,50))  # Optional resize
        answerC = ImageTk.PhotoImage(jawab_img)
        # d.
        jwb_path = "assets/test-image3.png"
        jawab = Image.open(jwb_path)
        jawab_img = jawab.resize((100,50))  # Optional resize
        answerD = ImageTk.PhotoImage(jawab_img)

        # --- penempatan label ---
        # *soal
        self.enemyinfo_lbl = tk.Label(self, image=question)
        self.enemyinfo_lbl.grid(row=2, column=1, columnspan=2, padx=10, pady=10)
        # image reference untuk mencegah garbage collection
        self.enemyinfo_lbl.image = question

        # --- penempatan tombol return to menu ---
        self.return_btn = tk.Button(self, text="Return to attack difficulty tab",command=self.goto_attack_difc, height=2)
        self.return_btn.grid(row=0, column=0, padx=(10,20), pady=15, sticky="w")

        # --- penempatan tombol battle system ---
        self.ans1_btn = tk.Button(self, image=answerA, text="Jawaban A")
        self.ans1_btn.grid(row=3, column=1, padx=(10,20), pady=15)
        # image reference untuk mencegah garbage collection
        self.ans1_btn.image = answerA

        self.ans2_btn = tk.Button(self, image=answerB, text="Jawaban B")
        self.ans2_btn.grid(row=3, column=2, padx=(20,10), pady=15)
        # image reference untuk mencegah garbage collection
        self.ans2_btn.image = answerB

        self.ans3_btn = tk.Button(self, image=answerC, text="Jawaban C")
        self.ans3_btn.grid(row=4, column=1, padx=(10,20), pady=15)
        # image reference untuk mencegah garbage collection
        self.ans3_btn.image = answerC

        self.ans4_btn = tk.Button(self, image=answerD, text="Jawaban D")
        self.ans4_btn.grid(row=4, column=2, padx=(20,10), pady=15)
        # image reference untuk mencegah garbage collection
        self.ans4_btn.image = answerD

    def goto_attack_difc(self):
        from battle_menu import attack_diffc
        self.master.show_page(attack_diffc)

class esai_singkat(tk.Frame):
    
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
        self.grid_rowconfigure(5, weight=1)
        self.grid_columnconfigure(0, weight=1)
        self.grid_columnconfigure(3, weight=3)

        # --- pemanggilan file image untuk soal dan jawaban ---
        # *soal
        soal_path = "assets/test-image3.png"
        soal = Image.open(soal_path)
        soal_img = soal.resize((300,160))  # Optional resize
        question = ImageTk.PhotoImage(soal_img)

        # --- penempatan label ---
        # *soal
        self.enemyinfo_lbl = tk.Label(self, image=question)
        self.enemyinfo_lbl.grid(row=2, column=1, columnspan=2, padx=10, pady=10)
        # image reference untuk mencegah garbage collection
        self.enemyinfo_lbl.image = question

        # --- penempatan tombol return to menu ---
        self.return_btn = tk.Button(self, text="Return to attack difficulty tab",command=self.goto_attack_difc, height=2)
        self.return_btn.grid(row=0, column=0, padx=(10,20), pady=15, sticky="w")

        # --- penempatan label untuk input jawaban ---
        tk.Label(self, text="Jawaban:").grid(row=3, column=1, padx=5, pady=5)
        self.jawaban_soal = tk.Entry(self, width=30)
        self.jawaban_soal.grid(row=3, column=2, padx=5, pady=5)

        # --- penempatan tombol untuk submit jawaban ---
        tk.Button(self, text="Sumbit Jawaban").grid(row=4, column=1, pady=5)

    def goto_attack_difc(self):
        from battle_menu import attack_diffc
        self.master.show_page(attack_diffc)