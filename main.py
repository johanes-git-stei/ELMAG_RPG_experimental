import tkinter as tk
import json
from main_menu import open_menu
import sys
import os

# completely new way to load files
# use this pyinstaller main.py --onefile --add-data "assets;assets"
def resource_path(relative_path):
    try:
        base_path = sys._MEIPASS
    except Exception:
        base_path = os.path.abspath(".") 

    return os.path.join(base_path, relative_path)


class main(tk.Tk):
    def __init__(self):
        super().__init__()
        self.title("Grid-Based Window Switcher")
        self.geometry("800x450")
        # make row/column 0 expandable so pages fill the window
        self.grid_rowconfigure(0, weight=1)
        self.grid_columnconfigure(0, weight=1)

        self.current_page = None
        self.show_page(open_menu)

        self.protocol("WM_DELETE_WINDOW", self.on_close)
    
    def on_close(self):
        with open("battle_temp.txt", "w", encoding="utf-8") as f:
                json.dump([0,0,0], f)

        with open("player_stat_temp.txt", "w", encoding="utf-8") as f:
                json.dump([10,0], f)

        with open("enemy_stat_temp.txt", "w", encoding="utf-8") as f:
                json.dump([3,0], f)
        
        self.destroy()

    def show_page(self, page_class):
        """Destroy current page and show a new one."""
        if self.current_page is not None:
            self.current_page.destroy()
        # instantiate and grid the new page
        self.current_page = page_class(self)
        self.current_page.grid(row=0, column=0, sticky="nsew")

    



if __name__ == "__main__":
    app = main()
    app.mainloop()