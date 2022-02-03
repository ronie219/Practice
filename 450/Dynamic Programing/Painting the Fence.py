def paint(colour, fence):

    same_colour = colour
    diff_colour = 2 * colour
    total = same_colour + diff_colour

    for idx in range(2, fence):
        same_colour = diff_colour
        diff_colour = total * (colour - 1)
        total = same_colour + diff_colour
    print(total)


paint(2, 4)
