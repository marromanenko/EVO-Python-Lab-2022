def direction(facing, turn):
    arr = ["NE", "E", "SE", "S", "SW", "W", "NW", "N"]
    pos = -1
    for i in range(8):
        if facing == arr[i]:
            pos = i
            break
    if pos != -1 and turn % 45 == 0:
        step = int(turn/45)
        res = pos + step
        while abs(res)>7:
            if res>0:
                res -= 8
            else:
                res += 8
        return arr[res]
    else: return "check the entered data"
 

print(direction("S", 180))
print(direction("SE", -45))
print(direction("W", 495))
print(direction("NE", -90))
print(direction("M", 100))

