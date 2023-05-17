import tkinter as tk
from tkinter import messagebox, StringVar

board = [[0] * 9 for _ in range(9)]
ans_loc = []
blank_loc = []

def update_board():
    for i in range(9):
        for j in range(9):
            entry_list[i][j].set(str(board[i][j]))

def clear_board():
    for i in range(9):
        for j in range(9):
            entry_list[i][j].set("")

def fill():
    global board, ans_loc, blank_loc
    
    if not blank_loc:
        return True
    
    curr_i, curr_j = blank_loc[0]
    cek = [True] * 10
    
    for i in range(9):
        if i != curr_i:
            cek[board[i][curr_j]] = False
    
    for j in range(9):
        if j != curr_j:
            cek[board[curr_i][j]] = False
    
    for i in range((curr_i // 3) * 3, (curr_i // 3) * 3 + 3):
        for j in range((curr_j // 3) * 3, (curr_j // 3) * 3 + 3):
            if i != curr_i or j != curr_j:
                cek[board[i][j]] = False
    
    for i in range(1, 10):
        if cek[i]:
            board[curr_i][curr_j] = i
            ans_loc.append((curr_i, curr_j))
            blank_loc.pop(0)
            
            if fill():
                return True
    
    if ans_loc:
        blank_loc.insert(0, ans_loc.pop())
    
    board[curr_i][curr_j] = 0
    return False

def solve_sudoku():
    global board, ans_loc, blank_loc
    
    for i in range(9):
        for j in range(9):
            temp = entry_list[i][j].get()
            
            if not temp.isdigit():
                board[i][j] = 0
                blank_loc.append((i, j))
            else:
                board[i][j] = int(temp)
    
    if fill():
        update_board()
        status_label.config(text="Sudoku is valid!", fg="green")
    else:
        status_label.config(text="Sudoku is invalid!", fg="red")

def create_layout():
    root = tk.Tk()
    root.title("Sudoku Solver")

    entry_list = []
    for i in range(9):
        row_entries = []
        for j in range(9):
            entry_var = StringVar()
            entry = tk.Entry(root, width=2, justify='center', textvariable=entry_var)
            entry.grid(row=i, column=j, padx=3, pady=3)
            row_entries.append(entry_var)
        entry_list.append(row_entries)

    # Add vertical grid lines
    for j in range(1, 9):
        if j % 3 == 0:
            root.grid_columnconfigure(j, minsize=3)
        else:
            root.grid_columnconfigure(j, minsize=1)

    # Add horizontal grid lines
    for i in range(1, 9):
        if i % 3 == 0:
            root.grid_rowconfigure(i, minsize=3)
        else:
            root.grid_rowconfigure(i, minsize=1)

    solve_button = tk.Button(root, text="Solve Sudoku", command=solve_sudoku)
    solve_button.grid(row=9, columnspan=9, pady=10)

    clear_button = tk.Button(root, text="Clear", command=clear_board)
    clear_button.grid(row=10, columnspan=9)

    status_label = tk.Label(root, text="Enter the Sudoku puzzle", fg="black")
    status_label.grid(row=11, columnspan=9, pady=10)

    # Add horizontal grid lines
    for i in range(1, 9):
        if i % 3 == 0:
            root.grid_rowconfigure(i, minsize=3)
        else:
            root.grid_rowconfigure(i, minsize=1)

    return entry_list, status_label, root

entry_list, status_label, root = create_layout()

root.mainloop()
