# hangman

def hangman(word):
    wrong = 0
    stages = ["______      ",
              "|     |     ",
              "|     |     ",
              "|     O     ",
              "|    /|\\    ",
              "|    / \\    ",
              "|___________"]
    rletters = list(word)
    board = ["_"] * len(word)
    win = False
    print("Welcome to Hangman!")
    
    while wrong < len(stages):
        print()
        msg = "Guess one charactor : "
        char = input(msg)
        if char in rletters:
            cind = rletters.index(char)
            board[cind] = char
            rletters[cind] = "$"
        else:
            wrong += 1
        
        print(" ".join(board))
        print("\n".join(stages[0:wrong]))

        if "_" not in board:
            print("\nYou win!")
            print(" ".join(board))
            win = True
            break
    
    if not win:
        print("You lose!")
        print("It's the correct answer is {}".format(word))

hangman("dog")
