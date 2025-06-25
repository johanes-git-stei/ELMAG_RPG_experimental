import tkinter as tk

class PageTwo(tk.Frame):

    def __init__(self, master):
        super().__init__(master)

        self.grid_rowconfigure(0, weight=1)
        self.grid_rowconfigure(3, weight=1)
        self.grid_columnconfigure(0, weight=1)
        self.grid_columnconfigure(2, weight=1)

        lblb = tk.Label(self, text="This is Page Two").grid(row=1, column=1, pady=10)
        btnb = tk.Button(self,
                  text="Back to Page One",
                  command=self.go_to_page_one
                 ).grid(row=2, column=1, padx=10, pady=15)

    def go_to_page_one(self):
        from page1 import PageOne
        self.master.show_page(PageOne)
