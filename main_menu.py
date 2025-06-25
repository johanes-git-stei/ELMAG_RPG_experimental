import tkinter as tk
from tkinter import messagebox, PhotoImage
from PIL import Image, ImageTk
import os

class open_menu(tk.Frame):

    def __init__(self, master):
        super().__init__(master)

        # --- memanggil background image dari folder assets dan dijadikan background wallpaper ---
        # mengambil file dari folder assets dan menaruhnya di label
        bg_pil = Image.open("assets/test-image.jpg")
        bg_pil = bg_pil.resize((450, 450))
        bg_img = ImageTk.PhotoImage(bg_pil)
        bg_lbl = tk.Label(self, image=bg_img)
        # image reference untuk mencegah garbage collection
        bg_lbl.image = bg_img
        # posisi label background image relatif pada window
        bg_lbl.place(x=0, y=0, relwidth=1, relheight=1)      

        # --- formatting penempatan label dan tombol ---
        self.grid_rowconfigure(0, weight=3)
        self.grid_rowconfigure(4, weight=1)
        self.grid_columnconfigure(0, weight=1)
        self.grid_columnconfigure(2, weight=1)

        # --- penempatan tombol menu ---
        self.start_btn = tk.Button(self, text="Start", command=self.go_to_page_two, width=30, height=2)
        self.start_btn.grid(row=1, column=1, padx=10, pady=15)

        self.achiv_btn = tk.Button(self, text="Statistics and Achievement", width=30, height=2)
        self.achiv_btn.grid(row=2, column=1, padx=10, pady=15)

        self.quit_btn = tk.Button(self, text="Quit Game", width=30, height=2)
        self.quit_btn.grid(row=3, column=1, padx=10, pady=15)

    def go_to_page_two(self):
        # import here to avoid circular import at module load time
        from battle_menu import start_battle
        self.master.show_page(start_battle)