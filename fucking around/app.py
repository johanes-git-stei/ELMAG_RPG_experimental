import tkinter as tk

root = tk.Tk()
root.geometry("300x300")  # overall window size

# 1. Configure 3 rows and 3 columns to share space equally
for i in range(3):
    root.grid_rowconfigure(i, weight=1)
    root.grid_columnconfigure(i, weight=1)

# 2. Add some widgets and make them fill their cells
for r in range(3):
    for c in range(3):
        btn = tk.Button(root, text=f"{r},{c}")
        # sticky="nsew" makes it stretch North/South/East/West
        btn.grid(row=r, column=c, sticky="nsew", padx=2, pady=2)

root.mainloop()
