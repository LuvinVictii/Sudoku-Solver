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

def print_board():
    for row in board:
        print(row)
    print()

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

def check_duplicate():
    global board

    for row in range(9):
        for col in range(9):
            num = board[row][col]
            if num != 0:
                # Check for duplicate number in the same row
                if board[row].count(num) > 1:
                    return True

                # Check for duplicate number in the same column
                for i in range(9):
                    if board[i][col] == num and i != row:
                        return True

                # Check for duplicate number in the same 3x3 grid
                start_row = (row // 3) * 3
                start_col = (col // 3) * 3

                for i in range(start_row, start_row + 3):
                    for j in range(start_col, start_col + 3):
                        if board[i][j] == num and (i != row or j != col):
                            return True
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
    
    if check_duplicate():
        status_label.config(text="Sudoku is invalid!", fg="red")
    else:
        if fill():
            update_board()
            status_label.config(text="Sudoku is valid!", fg="green")
            print_board()


def create_layout():
    root = tk.Tk()
    root.title("Sudoku Solver")
    root.geometry("400x500")
    root.configure(padx=10, pady=10,bg="white")
    root.resizable(False, False)

    entry_list = []
    for i in range(9):
        row_entries = []
        for j in range(9):
            entry_var = StringVar()
            #entry = tk.Entry(root, width=3, font=("Arial", 14), justify='center', textvariable=entry_var)
            row_entries.append(entry_var)
        entry_list.append(row_entries)

    solve_button = tk.Button(root, text="Solve Sudoku",  borderwidth=0, command=solve_sudoku, font=("Arial", 12, "bold"), fg="#D5E8FF", bg="#001B3C")
    solve_button.grid(row=9, columnspan=12, pady=10)

    clear_button = tk.Button(root, text="Clear", borderwidth=0, command=clear_board, font=("Arial", 12,"bold"), fg="#D5E8FF", bg="#001B3C")
    clear_button.grid(row=10, columnspan=12)

    status_label = tk.Label(root, text="Enter the Sudoku puzzle", fg="#001B3C", font=("Arial", 12,"bold"), bg="white")
    status_label.grid(row=11, columnspan=9, pady=10)

    root.grid_columnconfigure((0, 1, 2, 3, 4, 5, 6, 7, 8), weight=1, minsize=40)
    root.grid_rowconfigure((0, 1, 2, 3, 4, 5, 6, 7, 8), weight=1, minsize=40)

    for i in range(0, 9, 3):
        for j in range(0, 9, 3):
            frame = tk.Frame(root, bg="#86B8F3")
            frame.grid(row=i, column=j, rowspan=3, columnspan=3, padx=0, pady=0)
            frame.grid_columnconfigure((0, 1, 2), weight=1, minsize=20)
            frame.grid_rowconfigure((0, 1, 2), weight=1, minsize=20)
            for x in range(3):
                for y in range(3):
                    entry = tk.Entry(frame, width=2, font=("Arial", 21), justify='center',bg="#00455A",fg="#86B8F3", textvariable=entry_list[i+x][j+y])
                    entry.grid(row=x, column=y, padx=0.5, pady=0.5)

    return entry_list, status_label, root

entry_list, status_label, root = create_layout()

root.mainloop()
