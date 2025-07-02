import tkinter as tk
from tkinter import messagebox, PhotoImage
from PIL import Image, ImageTk
from battle_mode import start_battle
import os
import json
import random

import tkinter as tk

class start_question(tk.Frame):
    def __init__(self, master):
        super().__init__(master)

        #randomizer
        from rng import lcg

        from main import resource_path

        with open("battle_temp.txt", "r", encoding="utf-8") as f:
            self.battle_list = json.load(f)
        self.act_point = self.battle_list

        # --- memanggil background image dari folder assets dan dijadikan background wallpaper ---
        # mengambil file dari folder assets dan menaruhnya di label
        bg_pil = Image.open(resource_path("assets/test-image2.jpg"))
        bg_pil = bg_pil.resize((450, 450))
        bg_img = ImageTk.PhotoImage(bg_pil)
        bg_lbl = tk.Label(self, image=bg_img)
        # image reference untuk mencegah garbage collection
        bg_lbl.image = bg_img
        # posisi label background image relatif pada window
        bg_lbl.place(x=0, y=0, relwidth=1, relheight=1)

        # --- formatting penempatan label dan tombol ---
        self.grid_rowconfigure(0, weight=1)
        self.grid_rowconfigure(4, weight=1)
        for i in range(4):
            self.grid_columnconfigure(i, weight=1)

        # --- pemanggilan file image untuk soal dan jawaban ---
        # *soal
        soal_path = "assets/test-image3.png"
        soal = Image.open(resource_path(soal_path))
        soal_img = soal.resize((300,160))  # Optional resize
        question = ImageTk.PhotoImage(soal_img)

        paths = ["assets/test-image3.png","assets/test-image3.png", "assets/test-image3.png", "assets/test-image3.png"]
        self.imgs = []
        for p in paths:
            pil = Image.open(resource_path(p)).resize((50, 50))
            self.imgs.append(ImageTk.PhotoImage(pil))

        # --- penempatan label ---
        self.correct_answer = max(1, lcg(0) % 5) # Simulasi jawaban benar, bisa diubah sesuai kebutuhan
        self.test = tk.Label(self, text=f"{self.act_point}\n{self.correct_answer}")
        self.test.grid(row=1, column=0, padx=10, pady=10)

        # *soal
        self.question_lbl = tk.Label(self, image=question)
        self.question_lbl.grid(row=1, column=1, columnspan=2, padx=10, pady=10)
        # image reference untuk mencegah garbage collection
        self.question_lbl.image = question

        # --- informasi jawaban ---
        self.selected = tk.IntVar()

        # --- Radiobutton ---
        self.opt1_rb = tk.Radiobutton(self, variable=self.selected, image=self.imgs[0], value=1, text="A", compound="right")
        # --- image reference untuk mencegah garbage collection ---
        self.opt1_rb.image = self.imgs[0]
        self.opt1_rb.grid(row=2, column=1, padx=10, pady=10)

        self.opt2_rb = tk.Radiobutton(self, variable=self.selected, image=self.imgs[1], value=2, text="B", compound="right")
        # --- image reference untuk mencegah garbage collection ---
        self.opt2_rb.image = self.imgs[1]
        self.opt2_rb.grid(row=3, column=1, padx=10, pady=10)

        self.opt3_rb = tk.Radiobutton(self, variable=self.selected, image=self.imgs[2], value=3, text="C", compound="right")
        # --- image reference untuk mencegah garbage collection ---
        self.opt3_rb.image = self.imgs[2]
        self.opt3_rb.grid(row=2, column=2, padx=10, pady=10)

        self.opt4_rb = tk.Radiobutton(self, variable=self.selected, image=self.imgs[3], value=4, text="D", compound="right")
        # --- image reference untuk mencegah garbage collection ---
        self.opt4_rb.image = self.imgs[3]
        self.opt4_rb.grid(row=3, column=2, padx=10, pady=10)

        # Tombol Submit untuk memanggil pengecekan
        self.submit_btn = tk.Button(self, text="Submit", command=self.on_select)
        self.submit_btn.grid(row=4, column=1, columnspan=2, pady=15)

    def on_select(self):
        choice = self.selected.get()
        if choice == 0:
            messagebox.showwarning("Perhatian", "Silakan pilih salah satu jawaban terlebih dahulu.")
        elif choice == self.correct_answer:
            messagebox.showinfo("Hasil", "Jawaban Benar!")
            self.goto_battle_anim()
        else:
            messagebox.showerror("Hasil", "Jawaban Salah.")
            with open('data.json', 'w', encoding='utf-8') as f:
                json.dump({}, f, ensure_ascii=False, indent=2)

            self.act_point[0] = int(self.act_point[0]/2)
            self.act_point[1] = int(self.act_point[1]/2)
            self.act_point[2] = int(self.act_point[2]/2)

            with open("battle_temp.txt", "w", encoding="utf-8") as f:
                json.dump(self.act_point, f)

            self.goto_battle_anim()

    def goto_battle_anim(self):
        from battle_animation import battle_anim
        self.master.show_page(battle_anim)
