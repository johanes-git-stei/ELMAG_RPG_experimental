import tkinter as tk
from PIL import Image, ImageTk

root = tk.Tk()
root.title("Checkbox & Radiobutton with Images")

# --- Prepare images ---
# Replace these with your actual image paths
paths = ["assets/test-image3.png", "assets/test-image3.png", "assets/test-image3.png"]
imgs = []
for p in paths:
    pil = Image.open(p).resize((50, 50))
    imgs.append(ImageTk.PhotoImage(pil))

# --- Multiple-choice (Checkbox) ---
cb_frame = tk.LabelFrame(root, text="Multiple Choice")
cb_frame.pack(side="left", padx=10, pady=10)

cb_vars = []
for i, img in enumerate(imgs):
    var = tk.IntVar()
    cb = tk.Checkbutton(
        cb_frame,
        variable=var,
        image=img,
        compound="right",   # image to the right of text (indicator–text–image)
    )
    cb.pack(anchor="w", pady=2)
    cb_vars.append(var)

# --- Single-choice (Radiobutton) ---
rb_frame = tk.LabelFrame(root, text="Single Choice")
rb_frame.pack(side="right", padx=10, pady=10)

rb_var = tk.StringVar(value="0")
for i, img in enumerate(imgs):
    rb = tk.Radiobutton(
        rb_frame,
        variable=rb_var,
        value=str(i),
        image=img,
        compound="right",   # keeps the dot, then text, then image
    )
    rb.pack(anchor="w", pady=2)

# --- Show selections ---
def show():
    chosen_cbs = [i+1 for i, v in enumerate(cb_vars) if v.get()==1]
    chosen_rb = int(rb_var.get()) + 1
    print("Checkboxes selected:", chosen_cbs)
    print("Radiobutton selected:", chosen_rb)

tk.Button(root, text="Show", command=show).pack(pady=10)

root.mainloop()
