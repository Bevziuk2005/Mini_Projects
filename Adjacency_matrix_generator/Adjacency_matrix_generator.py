from itertools import combinations
import numpy as np
import tkinter as tk
from tkinter import scrolledtext

# отримує вершину і ребро та генерує з ними матриці
def generate_matrice(v, e):
    edges = list(combinations(range(v), 2))  # список УСІХ можливих пар по 2
    if e > len(edges):
        return ["Задана кількість ребер перевищує можливу для даної кількості вершин."]
    matrices = []
    for selected_edges in combinations(edges, e):
        matrix = np.zeros((v, v), dtype=int)
        for matrix_u, matrix_v in selected_edges:
            matrix[matrix_u][matrix_v] = 1
            matrix[matrix_v][matrix_u] = 1
        matrices.append(matrix)
    return matrices

# функція створює підказку для ребер
def update_hint(*args):
    try:
        n = int(entry_v.get())
        if n <= 0:
            hint.config(text="Кількість вершин має бути більше 0.")
            return
        if n > 8:
            hint.config(text="Кількість вершин не може перевищувати 8.")
            return
        max_edges = n * (n - 1) // 2
        hint.config(text=f'Максимальна кількість ребер: {max_edges} \n"всі" виведе всі можливі варіанти')
    except ValueError:
        hint.config(text="")

def generate():
    try:
        v = int(entry_v.get())
        e = entry_e.get().strip().lower()
        if v <= 0:
            area.delete(1.0, tk.END)
            area.insert(tk.END, "Кількість вершин має бути більше 0.")
            return
        if v > 8:
            area.delete(1.0, tk.END)
            area.insert(tk.END, "Кількість вершин не може перевищувати 8.")
            return

        max_edges = v * (v - 1) // 2

        if e == "all" or e == "всі":
            matrices = []
            for m in range(max_edges + 1):
                matrices.extend(generate_matrice(v, m))
        else:
            m = int(e)
            matrices = generate_matrice(v, m)
        area.delete(1.0, tk.END)
        if isinstance(matrices, list) and isinstance(matrices[0], str):
            area.insert(tk.END, matrices[0])
        else:
            area.insert(tk.END, f"Знайдено {len(matrices)} можливих графів:\n")
            for idx, matrix in enumerate(matrices, 1):
                area.insert(tk.END, f"Граф {idx}:\n{matrix}\n\n")
    except ValueError:
        area.delete(1.0, tk.END)
        area.insert(tk.END, "Будь ласка, введіть коректні числа.")

root = tk.Tk()
root.title("Adjacency matrix generator")
tk.Label(root, text="Кількість вершин:").grid(row=0, column=0)
entry_v = tk.Entry(root)
entry_v.grid(row=0, column=1)
entry_v.bind("<KeyRelease>", update_hint)
hint = tk.Label(root, text="")
hint.grid(row=0, column=2)
tk.Label(root, text="Кількість ребер:").grid(row=1, column=0)
entry_e = tk.Entry(root)
entry_e.grid(row=1, column=1)
generate = tk.Button(root, text="Генерувати", command=generate)
generate.grid(row=2, column=0, columnspan=2)
area = scrolledtext.ScrolledText(root, width=40, height=30)
area.grid(row=3, column=0, columnspan=2)
root.mainloop()