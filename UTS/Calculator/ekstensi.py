import tkinter as tk

# Fungsi untuk tombol angka
def press(num):
    current = entry.get()
    entry.delete(0, tk.END)
    entry.insert(0, current + num)

# Fungsi untuk tombol sama dengan
def calculate():
    entire_string = entry.get()
    try:
        result = eval(entire_string)
        entry.delete(0, tk.END)
        entry.insert(0, str(result))
    except:
        entry.delete(0, tk.END)
        entry.insert(0, "Error")

# Fungsi untuk tombol bersihkan (clear)
def clear():
    entry.delete(0, tk.END)

# Membuat window
root = tk.Tk()
root.title("Kalkulator Sederhana")

# Membuat input/output untuk kalkulator
entry = tk.Entry(root, width=35, borderwidth=5)
entry.grid(row=0, column=0, columnspan=4)

# Membuat dan menempatkan tombol angka
buttons = [
    '7', '8', '9', '/',
    '4', '5', '6', '*',
    '1', '2', '3', '-',
    '0', 'C', '=', '+'
]

row = 1
col = 0
for button in buttons:
    if button != '=':
        tk.Button(root, text=button, padx=40, pady=20, command=lambda b=button: press(b)).grid(row=row, column=col)
    else:
        tk.Button(root, text=button, padx=40, pady=20, command=calculate).grid(row=row, column=col)
    col += 1
    if col > 3:
        col = 0
        row += 1

# Tombol bersihkan (clear)
tk.Button(root, text='Clear', padx=40, pady=20, command=clear).grid(row=5, column=0, columnspan=4)

# Menjalankan program
root.mainloop()
