import tkinter as tk
from tkinter import messagebox, PhotoImage
from PIL import Image, ImageTk
import json
import random

import tkinter as tk

class start_question(tk.Frame):
    def __init__(self, master):
        super().__init__(master)

        with open("battle_temp.txt", "r", encoding="utf-8") as f:
            self.battle_list = json.load(f)
        self.act_point = self.battle_list

        # --- memanggil background image dari folder assets dan dijadikan background wallpaper ---
        # mengambil file dari folder assets dan menaruhnya di label
        bg_pil = Image.open("assets/question_bg.png")
        bg_pil = bg_pil.resize((1584, 864))
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
        random_soal_num = random.randint(1, 5)  # Simulasi soal acak, bisa diubah sesuai kebutuhan
        soal_path = f"soal/BAB {random_soal_num}/Soal.png"
        soal = Image.open(soal_path)
        soal_img = soal.resize((400,225))  # Optional resize
        question = ImageTk.PhotoImage(soal_img)

        jawaban = [f"soal/BAB {random_soal_num}/Jawaban Benar.png", f"soal/BAB {random_soal_num}/Jawaban Salah 1.png", f"soal/BAB {random_soal_num}/Jawaban Salah 2.png", f"soal/BAB {random_soal_num}/Jawaban Salah 3.png"]

        randomized_jawaban = random.sample(jawaban, 4)  # Mengacak urutan jawaban

        self.imgs = []
        for p in randomized_jawaban:
            pil = Image.open(p).resize((200,113))
            self.imgs.append(ImageTk.PhotoImage(pil))

        # *soal
        self.question_lbl = tk.Label(self, image=question, bg="#090F1F", fg='#FFFFFF')
        self.question_lbl.grid(row=1, column=1, columnspan=2, padx=10, pady=10)
        # image reference untuk mencegah garbage collection
        self.question_lbl.image = question

        # --- informasi jawaban ---
        self.selected = tk.IntVar()

        # 1. pick a random slot (1–4) for the correct answer
        self.correct_value = random.randint(1, len(self.imgs))
        self.test = tk.Label(self, text=f"{self.act_point}\n{self.correct_value}")
        self.test.grid(row=1, column=0, padx=10, pady=10)

        # 2. make a pool of wrong images
        wrongs = self.imgs[1:].copy()

        # 3. build radiobuttons in a 2×2 grid
        for slot in range(1, len(self.imgs) + 1):
            if slot == self.correct_value:
                img = self.imgs[0]
            else:
                # take a random wrong image
                img = wrongs.pop(random.randrange(len(wrongs)))

            rb = tk.Radiobutton(
                self,
                variable=self.selected,
                value=slot,
                image=img,
                text=chr(ord("A") + slot - 1),  # "A", "B", "C", "D"
                compound="right",
                bg="#F2C152"
            )
            rb.image = img  # prevent GC
            row, col = divmod(slot-1, 2)
            rb.grid(row=row+2, column=col+1, padx=10, pady=10)

        # Submit button
        submit = tk.Button(self, text="Submit", command=self.on_select)
        submit.grid(row=4, column=1, columnspan=2, pady=15)

    def on_select(self):
        choice = self.selected.get()
        if choice == 0:
            messagebox.showwarning("Perhatian", "Silakan pilih salah satu jawaban terlebih dahulu.")
        elif choice == self.correct_value:
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
