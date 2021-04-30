import requests
from tkinter import *

# TODO
# - Empty window
# - Display status
# - Enter a name
# - Display player's info
# - Display list of available ship


def get_status():
    """Check the server's status.

    :return: JSON
    """
    return requests.get('https://api.spacetraders.io/game/status').json()


def post_username(_username: str):
    return requests.post('https://api.spacetraders.io/users/' + _username + '/token').json()


def get_loan(_token: str):
    return requests.get('https://api.spacetraders.io/game/loans token==' + _token).json()


def post_loan(_username: str, _token: str):
    return requests.post('https://api.spacetraders.io/users/' + _username + '/loans token==' + _token + ' \ type=STARTUP').json()


def init_window(_window: Tk):
    """Initialise the main window.

    :param _window: Tk
    :return: None
    """
    _window.geometry("720x480")
    _window.minsize(720, 480)
    _window.maxsize(720, 480)
    _window.title('sPYceTraders')

def frame_login(_window):
    Frame(_window,bg="blue").pack(fill=BOTH,expand=True)


if __name__ == '__main__':
    window = Tk()
    init_window(window)
    frame_login(window)
    print(get_status())
    username = 'darleenax'
    token = 'fb4ba70e-a0ba-4f8e-9152-b4f3ba378dc7'
    token = '139a6675-2870-4734-89e0-d0aa44d64e81'
    print(post_loan(username, token))
    print(post_username(username))
    window.mainloop()

    # token : cde3bb98-0e31-4a0b-8041-cf701070a775
