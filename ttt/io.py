def choose_player():
    while True:
        player = input("choose player c for computer m fot you ").lower()
        if player not in ["c","m"]:
            continue
        return player

def choose_position(size = 3):
    while True:
        line = input("choose the line")
        if not line.isdigit():
            print("only numbers...")
            continue
        else:
            lin = int(line)
        if lin > size:
            print("out of the board")
            continue
        col = input("choose the column")
        if not col.isdigit():
            print("only numbers...")
            continue
        else:
            coll = int(col)
        if coll > size:
            print("out of the board")
            continue

        return lin,coll
print(choose_position())
