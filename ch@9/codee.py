import random

def game():
    print("You are playing game...")
    score = random.randint(1, 75)

    # Read the high score safely
    try:
        with open("highscore.txt", "r") as f:
            highscore_data = f.read().strip()
            if highscore_data.isdigit():
                highscore = int(highscore_data)
            else:
                highscore = 0
    except FileNotFoundError:
        highscore = 0

    print(f"Your score: {score}")

    if score > highscore:
        print("New high score!")
        with open("highscore.txt", "w") as f:
            f.write(str(score))

    return score

game()