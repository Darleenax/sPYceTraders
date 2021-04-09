import requests
from tkinter import *

# TODO
# - Empty window
# - Display status
# - Enter a name
# - Display player's info
# - Display list of available ship


def getstatus():
    return requests.get('https://api.spacetraders.io/game/status').json()


if __name__ == '__main__':
    window = Tk()
    window.title("Welcome to LikeGeeks app")
    window.mainloop()
    print(getstatus())
