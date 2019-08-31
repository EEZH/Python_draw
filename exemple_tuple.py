from collections import namedtuple

UIM435 = namedtuple("UIM435", ["start", "stop", "move_right", "move_left"])

def uim_right(velocity):
    print(f"uim rigth: {velocity}")

def uim_left(velocity):
    print(f"uim left: {velocity}")

def uim_start():
    print(f"uim start")

def uim_stop():
    print(f"uim stop")

uim = UIM435(start=uim_start, stop=uim_stop, move_right=uim_right, move_left=uim_left)
