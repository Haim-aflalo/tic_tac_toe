def create_board(size = 3):
    rows = []
    for i in range(size):
        cols = []
        for j in range(size):
            cols.append(0)
        rows.append(cols)
    return rows

def show_board(size=3, symbol=" "):
    board = ""
    board += " --- " * size + "\n"
    for i in range(size):
        line = "| "
        for j in range(size):
            line += symbol + " | "
        board += line + "\n"
        board += " --- " * size + "\n"
    return board
