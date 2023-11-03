def tracking():
    points = [(0, 0), (1, 0), (1, -1)]#, (0, -1), (0, 0)]
    coordinates = []
    for coordinate in range(len(points) - 1):
        x = points[coordinate][0]
        y = points[coordinate][1]
        a = points[coordinate + 1][0]
        b = points[coordinate + 1][1]

        change_in_x = x + a
        change_in_y = y + b
        total_change = abs(change_in_x) + abs(change_in_y)

    for piece in range(total_change + 1):
        if change_in_x != 0:
            if change_in_x > 0:
                temp = x + piece
                if (temp, y) in coordinates:
                    return print(abs(temp) + abs(y))
                coordinates.append((temp, y))

            else:
                temp = x - piece
                if (temp, y) in coordinates:
                    return print(abs(temp) + abs(y))

                coordinates.append((temp, y))

        else:
            if change_in_y > 0:
                temp = y + piece
                if (x, temp) in coordinates:
                    return print(abs(temp) + abs(x))
                coordinates,append((x, temp))

            else:
                temp = y - piece
                if (x, temp) in coordinates:
                    return print(abs(temp) + abs(x))
                coordinates,append((x, temp))

    print (x, y, a, b)
    print(change_in_x)
    print(change_in_y)
    print(coordinates)


tracking()