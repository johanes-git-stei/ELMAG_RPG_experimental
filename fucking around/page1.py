import tkinter as tk

class PageOne(tk.Frame):

    def __init__(self, master):
        super().__init__(master)

        self.grid_rowconfigure(0, weight=1)
        self.grid_rowconfigure(3, weight=1)
        self.grid_columnconfigure(0, weight=1)
        self.grid_columnconfigure(2, weight=1)

        # your widgets…
        lbla = tk.Label(self, text="This is Page One").grid(row=1, column=1, pady=10)
        btna = tk.Button(self,
                  text="Go to Page Two",
                  command=self.go_to_page_two
                 ).grid(row=2, column=1, padx=10, pady=15)

    def go_to_page_two(self):
        # import here to avoid circular import at module load time
        from page2 import PageTwo
        self.master.show_page(PageTwo)
