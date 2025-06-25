import tkinter as tk
from page1 import PageOne
from page2 import PageTwo

class App(tk.Tk):
    def __init__(self):
        super().__init__()
        self.title("Grid-Based Window Switcher")
        self.geometry("400x200")
        # make row/column 0 expandable so pages fill the window
        self.grid_rowconfigure(0, weight=1)
        self.grid_columnconfigure(0, weight=1)

        self.current_page = None
        self.show_page(PageOne)

    def show_page(self, page_class):
        """Destroy current page and show a new one."""
        if self.current_page is not None:
            self.current_page.destroy()
        # instantiate and grid the new page
        self.current_page = page_class(self)
        self.current_page.grid(row=0, column=0, sticky="nsew")


if __name__ == "__main__":
    app = App()
    app.mainloop()
