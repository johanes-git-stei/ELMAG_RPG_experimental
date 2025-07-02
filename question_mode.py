import tkinter as tk
from tkinter import messagebox
from PIL import Image, ImageTk
import json
import random

class start_question(tk.Frame):
    def __init__(self, master):
        super().__init__(master)

        from rng import lcg
        from main import resource_path

        # Load data battle
        with open("battle_temp.txt", "r", encoding="utf-8") as f:
            self.act_point = json.load(f)

        # --- Background setup ---
        bg_pil = Image.open(resource_path("assets/question_bg.png")).resize((1584, 864))
        bg_img = ImageTk.PhotoImage(bg_pil)
        bg_lbl = tk.Label(self, image=bg_img)
        bg_lbl.image = bg_img  # Prevent GC
        bg_lbl.place(x=0, y=0, relwidth=1, relheight=1)

        # --- Layout grid config ---
        self.grid_rowconfigure(0, weight=1)
        self.grid_rowconfigure(4, weight=1)
        for i in range(4):
            self.grid_columnconfigure(i, weight=1)

        # --- Load random soal dan jawaban ---
        random_soal_num = max(1, lcg(0) % 6)  # Nomor soal 1–5
        soal_path = f"soal/BAB {random_soal_num}/Soal.png"
        jawaban_benar_path = f"soal/BAB {random_soal_num}/Jawaban Benar.png"
        jawaban_paths = [
            jawaban_benar_path,
            f"soal/BAB {random_soal_num}/Jawaban Salah 1.png",
            f"soal/BAB {random_soal_num}/Jawaban Salah 2.png",
            f"soal/BAB {random_soal_num}/Jawaban Salah 3.png"
        ]

        randomized_jawaban = random.sample(jawaban_paths, 4)
        self.index_benar = randomized_jawaban.index(jawaban_benar_path)

        # --- Load gambar soal ---
        soal_img = Image.open(resource_path(soal_path)).resize((400, 225))
        self.question_img = ImageTk.PhotoImage(soal_img)
        self.question_lbl = tk.Label(self, image=self.question_img, bg="#090F1F")
        self.question_lbl.grid(row=1, column=1, columnspan=2, padx=10, pady=10)

        # --- Load gambar jawaban ---
        self.imgs = []
        for path in randomized_jawaban:
            img_pil = Image.open(resource_path(path)).resize((200, 113))
            self.imgs.append(ImageTk.PhotoImage(img_pil))

        # --- RadioButton jawaban ---
        self.selected = tk.IntVar()

        for i, img in enumerate(self.imgs):
            rb = tk.Radiobutton(
                self,
                variable=self.selected,
                value=i,
                image=img,
                text=chr(ord("A") + i),  # A, B, C, D
                compound="right",
                bg="#F2C152"
            )
            rb.image = img
            row, col = divmod(i, 2)
            rb.grid(row=row + 2, column=col + 1, padx=10, pady=10)

        # --- Tombol Submit ---
        submit = tk.Button(self, text="Submit", command=self.on_select)
        submit.grid(row=4, column=1, columnspan=2, pady=15)

    def on_select(self):
        choice = self.selected.get()

        if choice == -1 or self.selected.get() is None:
            messagebox.showwarning("Perhatian", "Silakan pilih salah satu jawaban terlebih dahulu.")
        elif choice == self.index_benar:
            messagebox.showinfo("Hasil", "Jawaban Benar!")
            self.goto_battle_anim()
        else:
            messagebox.showerror("Hasil", "Jawaban Salah.")
            with open('data.json', 'w', encoding='utf-8') as f:
                json.dump({}, f, ensure_ascii=False, indent=2)

            # Kurangi act point separuh
            self.act_point = [int(p / 2) for p in self.act_point]

            with open("battle_temp.txt", "w", encoding="utf-8") as f:
                json.dump(self.act_point, f)

            self.goto_battle_anim()

    def goto_battle_anim(self):
        from battle_animation import battle_anim
        self.master.show_page(battle_anim)
