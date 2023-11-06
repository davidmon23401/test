import tkinter as tk

def close_window():
    root.destroy()

root = tk.Tk()
root.title("Ari")
root.geometry("500x500")

label = tk.Label(root, text="Ari is fucking mine and ill fuck her whenever i want even if she on her period idgaf ;)!")
label.pack()

button = tk.Button(root, text="Close", command=close_window)
button.pack()

root.mainloop()
