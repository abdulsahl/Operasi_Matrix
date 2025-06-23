import tkinter as tk
from tkinter import messagebox

def get_matrix(entry_matrix, rows, cols):
    return [[int(entry_matrix[i][j].get()) for j in range(cols)] for i in range(rows)]

def set_matrix(result_matrix, matrix, rows, cols):
    for i in range(rows):
        for j in range(cols):
            result_matrix[i][j].config(state='normal')
            result_matrix[i][j].delete(0, tk.END)
            result_matrix[i][j].insert(0, str(matrix[i][j]))
            result_matrix[i][j].config(state='readonly')

def add_matrices():
    matrix1 = get_matrix(matrix1_entries, rows1, cols1)
    matrix2 = get_matrix(matrix2_entries, rows2, cols2)
    if rows1 != rows2 or cols1 != cols2:
        messagebox.showerror("Error", "Ukuran matriks harus sama untuk penjumlahan!")
        return
    result = [[matrix1[i][j] + matrix2[i][j] for j in range(cols1)] for i in range(rows1)]
    set_matrix(result_entries, result, rows1, cols1)

def subtract_matrices():
    matrix1 = get_matrix(matrix1_entries, rows1, cols1)
    matrix2 = get_matrix(matrix2_entries, rows2, cols2)
    if rows1 != rows2 or cols1 != cols2:
        messagebox.showerror("Error", "Ukuran matriks harus sama untuk pengurangan!")
        return
    result = [[matrix1[i][j] - matrix2[i][j] for j in range(cols1)] for i in range(rows1)]
    set_matrix(result_entries, result, rows1, cols1)

def multiply_matrices():
    matrix1 = get_matrix(matrix1_entries, rows1, cols1)
    matrix2 = get_matrix(matrix2_entries, rows2, cols2)
    if cols1 != rows2:
        messagebox.showerror("Error", "Jumlah kolom Matriks 1 harus sama dengan jumlah baris Matriks 2 untuk perkalian!")
        return
    result = [[sum(matrix1[i][k] * matrix2[k][j] for k in range(cols1)) for j in range(cols2)] for i in range(rows1)]
    set_matrix(result_entries, result, rows1, cols2)

def setup_matrices():
    global rows1, cols1, rows2, cols2, matrix1_entries, matrix2_entries, result_entries

    rows1 = int(rows1_var.get())
    cols1 = int(cols1_var.get())
    rows2 = int(rows2_var.get())
    cols2 = int(cols2_var.get())

    for widget in frame.winfo_children():
        widget.destroy()

    matrix1_entries = [[tk.Entry(frame, width=5) for j in range(cols1)] for i in range(rows1)]
    matrix2_entries = [[tk.Entry(frame, width=5) for j in range(cols2)] for i in range(rows2)]
    result_entries = [[tk.Entry(frame, width=5, state='readonly') for j in range(cols2)] for i in range(rows1)]

    # Menempatkan Matriks 1
    tk.Label(frame, text="Matriks 1").grid(row=0, column=0, columnspan=cols1)
    for i in range(rows1):
        for j in range(cols1):
            matrix1_entries[i][j].grid(row=i+1, column=j, padx=5, pady=5)

    # Menempatkan Matriks 2
    tk.Label(frame, text="Matriks 2").grid(row=0, column=cols1+1, columnspan=cols2)
    for i in range(rows2):
        for j in range(cols2):
            matrix2_entries[i][j].grid(row=i+1, column=j+cols1+1, padx=5, pady=5)

    # Menempatkan Tombol
    add_button = tk.Button(frame, text="Tambah", command=add_matrices)
    add_button.grid(row=max(rows1, rows2)+2, column=1, pady=10)

    subtract_button = tk.Button(frame, text="Kurangi", command=subtract_matrices)
    subtract_button.grid(row=max(rows1, rows2)+2, column=2, pady=10)

    multiply_button = tk.Button(frame, text="Kalikan", command=multiply_matrices)
    multiply_button.grid(row=max(rows1, rows2)+2, column=3, pady=10)

    # Menempatkan Matriks Hasil
    tk.Label(frame, text="Hasil").grid(row=max(rows1, rows2)+3, column=1, columnspan=cols2)
    for i in range(rows1):
        for j in range(cols2):
            result_entries[i][j].grid(row=i+max(rows1, rows2)+4, column=j+1, padx=5, pady=5)

root = tk.Tk()
root.title("Operasi Matriks")

top_frame = tk.Frame(root)
top_frame.pack(padx=10, pady=10)

tk.Label(top_frame, text="Baris Matriks 1:").grid(row=0, column=0)
rows1_var = tk.StringVar(value="2")
tk.Entry(top_frame, textvariable=rows1_var).grid(row=0, column=1)

tk.Label(top_frame, text="Kolom Matriks 1:").grid(row=0, column=2)
cols1_var = tk.StringVar(value="2")
tk.Entry(top_frame, textvariable=cols1_var).grid(row=0, column=3)

tk.Label(top_frame, text="Baris Matriks 2:").grid(row=1, column=0)
rows2_var = tk.StringVar(value="2")
tk.Entry(top_frame, textvariable=rows2_var).grid(row=1, column=1)

tk.Label(top_frame, text="Kolom Matriks 2:").grid(row=1, column=2)
cols2_var = tk.StringVar(value="2")
tk.Entry(top_frame, textvariable=cols2_var).grid(row=1, column=3)

setup_matrices_button = tk.Button(top_frame, text="Set Matriks Size", command=setup_matrices)
setup_matrices_button.grid(row=2, columnspan=4, pady=10)

frame = tk.Frame(root)
frame.pack(padx=10, pady=10)

rows1, cols1, rows2, cols2 = 3, 3, 3, 3
matrix1_entries = [[tk.Entry(frame, width=5) for j in range(cols1)] for i in range(rows1)]
matrix2_entries = [[tk.Entry(frame, width=5) for j in range(cols2)] for i in range(rows2)]
result_entries = [[tk.Entry(frame, width=5, state='readonly') for j in range(cols2)] for i in range(rows1)]

setup_matrices()

root.mainloop()
