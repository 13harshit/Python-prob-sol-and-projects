import random
import os

def game(): 
    print("You are playing the game..")
    score = random.randint(1, 62)

    # Locate hiscore.txt relative to this script file so the file is found
    # even if Python is executed from a different working directory.
    base_dir = os.path.dirname(os.path.abspath(__file__))
    hiscore_path = os.path.join(base_dir, "hiscore.txt")

    # Ensure the hiscore file exists (create it with 0 if missing)
    if not os.path.exists(hiscore_path):
        with open(hiscore_path, "w") as f:
            f.write("0")

    # Fetch the hiscore
    with open(hiscore_path) as f:
        hiscore = f.read().strip()
        if hiscore != "":
            hiscore = int(hiscore)
        else:
            hiscore = 0

    print(f"Your score: {score}")
    if score > hiscore:
        # write this hiscore to the file
        with open(hiscore_path, "w") as f:
            f.write(str(score))

    return score

if __name__ == "__main__":
    game()