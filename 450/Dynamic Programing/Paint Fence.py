"""
1. You are given a number n and a number k in separate lines, representing the number of fences and number of colors.
2. You are required to calculate and print the number of ways in which the fences could be painted so that not more than two fences have same colors.
"""


def paint_fence(nf, colour):

    # In the same_colour we store the count which end rr gg, bb....
    # in diff_colour we store the count whose last two values are differnt

    same_colour = colour  # like for 3 colour rr, bb, gg
    diff_colour = 2 * colour  # like for 3 colour rg,rb, bg,br, gr,gb
    total = same_colour + diff_colour

    # for next itteration if we add same no. of colour at the end of diff it will become
    # same_colour for next itter
    # Also if we add differrent color on both same_colour and differ_color it will become
    # diff_col for next iter
    for _ in range(2, nf):
        same_colour = diff_colour
        diff_colour = total * (colour - 1)
        total = same_colour + diff_colour

    print(same_colour + diff_colour)


if __name__ == "__main__":
    n, k = map(int, input().split())
    paint_fence(n, k)
