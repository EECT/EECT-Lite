import tkinter as tk

def main_window():
    root = tk.Tk()
    root.title("EECT Lite v0.0.0.0")
    root.geometry("500x300")

    EECT_title = tk.Label(root, text="EECT Lite", font=22, anchor="nw").place(x=10, y=10)
    aotu_shutdown = tk.Button(root, text="定时关机").place(x=10, y=40)

    root.mainloop()


if __name__ == "__main__":
    main_window()
