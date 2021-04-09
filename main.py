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
    window.minsize(480, 360)
    window.title("Welcome to LikeGeeks app")
    print(getstatus())
    username = 'fulldada'
    print(requests.post('https://api.spacetraders.io/users/' + username + '/token').json())
    window.mainloop()

    # token : cde3bb98-0e31-4a0b-8041-cf701070a775

