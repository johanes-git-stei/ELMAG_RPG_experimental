import tkinter as tk
from tkinter import messagebox, PhotoImage
from PIL import Image, ImageTk
import os

class open_menu(tk.Frame):

    def __init__(self, master):
        super().__init__(master)

        from main import resource_path

        # --- memanggil background image dari folder assets dan dijadikan background wallpaper ---
        # mengambil file dari folder assets dan menaruhnya di label
        bg_pil = Image.open(resource_path("assets/test-image.jpg"))
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
        for j in range(3):
            self.grid_columnconfigure(j, weight=1)

        # --- penempatan tombol menu ---
        self.start_btn = tk.Button(self, text="Start", command=self.goto_start_battle, width=30, height=2)
        self.start_btn.grid(row=1, column=1, padx=10, pady=15)

        self.achiv_btn = tk.Button(self, text="Statistics and Achievement", width=30, height=2)
        self.achiv_btn.grid(row=2, column=1, padx=10, pady=15)

        self.quit_btn = tk.Button(self, text="Quit Game", command=self.kill_game, width=30, height=2)
        self.quit_btn.grid(row=3, column=1, padx=10, pady=15)

    def goto_start_battle(self):
        # import here to avoid circular import at module load time
        from battle_mode import start_battle
        self.master.show_page(start_battle)

    def kill_game(self):
        if messagebox.askokcancel("Quit?", "Do you want to quit the game?"):
            self.master.destroy()