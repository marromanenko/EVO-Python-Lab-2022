def direction(facing, turn):
    try:
        pos = arr.index(facing)
        if turn % 45 == 0:
            step = int(turn/45)
            res = pos + step
            while abs(res) > 7:
                res = (pos + step) % 8
            return arr[res]
        else:
            return "check the entered data"
    except ValueError:
        return "check the entered data"


arr = ["NE", "E", "SE", "S", "SW", "W", "NW", "N"]
print(direction("S", 180))
print(direction("SE", -45))
print(direction("W", 495))
print(direction("NE", -90))
print(direction("M", 100))
