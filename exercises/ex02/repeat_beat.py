"""Repeating a beat in a loop."""

__author__ = "730281821"


beat: str = str(input("What beat do you want to repeat? "))
repeat: int = int(input("How many times do you want to repeat it? "))
if 0 < repeat:
    song: str = (beat + " ") * repeat
    print(str(song))
    repeat = repeat - repeat
else:
    repeat < 1
    print("No beat...")
    repeat = repeat + 1