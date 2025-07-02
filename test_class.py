import tkinter as tk
from battle_animation import battle_anim

class main(tk.Tk):
    def __init__(self):
        super().__init__()
        self.title("Grid-Based Window Switcher")
        self.geometry("800x450")
        # make row/column 0 expandable so pages fill the window
        self.grid_rowconfigure(0, weight=1)
        self.grid_columnconfigure(0, weight=1)

        self.current_page = None
        self.show_page(battle_anim)

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