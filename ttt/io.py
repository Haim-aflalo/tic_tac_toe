def choose_player():
    while True:
        player = input("choose player c for computer m fot you ").lower()
        if player not in ["c","m"]:
            continue
        return player
