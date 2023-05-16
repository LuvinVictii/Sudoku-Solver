# board sudoku
board = [[0] * 9 for _ in range(9)] 

# array menyimpan pair (i, j) kotak yang sudah terisi
ans_loc = []                    

# array menyimpan pair (i, j) kotak yang belum terisi
blank_loc = []

# print board sudoku functinn
def print_board():
    count_i = 0
    for i in board:
        if(count_i % 3 == 0):
            print("+", "-"*5, "+", "-"*5, "+", "-"*5 , "+") 
        count_i += 1
        count_j = 0
        for j in i:
            if(count_j % 3 == 0):
                print("| ", end="")
            count_j+= 1
            print(j, end=" ")
        print("|")
    print("+", "-"*5, "+", "-"*5, "+", "-"*5, "+") 

# backtrack filling function
def fill():
    # if there is no more blank sudoku boxes, return true
    if len(blank_loc) == 0:
        return True
    
    # at first, all number (1-9) is acceptable in that empty sudoku boxes
    cek = [True] * 10

    # store empty sudoku boxes coordinate
    curr_i, curr_j = blank_loc[0]

    # vertically checking
    for i in range(0, 9):
        if i == curr_i:
            continue
        cek[board[i][curr_j]] = False

    # horizontaly checking
    for j in range(0, 9):
        if j == curr_j:
            continue
        cek[board[curr_i][j]] = False

    # 3x3 box checking
    for i in range((curr_i // 3) * 3, (curr_i // 3) * 3 + 3):
        for j in range((curr_j // 3) * 3, (curr_j // 3) * 3 + 3):
            if i == curr_i and j == curr_j:
                continue
            cek[board[i][j]] = False

    # check all possibel number for this current boxes
    for curr_ans in range(1, 10):
        # if empty boxes can be filled with curr_ans
        if cek[curr_ans]:
            # fill the box
            board[curr_i][curr_j] = curr_ans

            # keep track location of boxes 
            ans_loc.append((curr_i, curr_j))

            # remove this box from list of blank/empty boxes
            blank_loc.pop(0)

            # if all boxes is filled with correct numbers return True
            # else it will check for other available numbers
            if fill():
                return True
    
    # if still there is no correct numbers, do backtracking
    # add again currnet boxes to the list of blank boxes
    if ans_loc:
        blank_loc.insert(0, ans_loc.pop())

    # set numbers in board to 0
    board[curr_i][curr_j] = 0

    # return fakse
    return False


# user prompting
print("Input unsolved sudoku")
print("Input without spaces")
print("You can seperate each rows with new line (enter)")
print("You can replace blank boxes with any character except 1-9")

# user input
for i in range(0, 9):
    row = input().split()
    for j in range(0, 9):
        temp = int(row[j])

        if(temp < 1 or temp > 9 ):
            board[i][j] = 0
            blank_loc.append((i, j))
        else:
            board[i][j] = temp

# start the alg
if(fill()):
    print_board()
else:
    print("Sudko is invalid")
