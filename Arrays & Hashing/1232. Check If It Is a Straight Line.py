def checkStraightLine(coordinates):
    x0, y0 = coordinates[0]
    for x, y in coordinates[1:]:
        if((y - y0) * (coordinates[1][0] - x0) != (x - x0) * (coordinates[1][1] - y0)):
            return False
    return True