import os

class HighScore:
    def __init__(self):
        try:
            with open("hs.txt", "r+") as hs:
                pass
        except FileNotFoundError:
            with open("hs.txt", "w+") as hs:
                hs.write("0")

    def high_score(self, score):
        with open("hs.txt", "r+") as hs_file:
            lines = hs_file.readlines()
            for line in lines:
                if float(line.lstrip("\x00")) < score:
                    hs_file.truncate(0)
                    hs_file.write(str(score))

    def get_highscore(self):
         with open("hs.txt", "r+") as hs_file:
            lines = hs_file.readlines()
            for line in lines:
                return((float(line.strip("\x00"))))
