def eggDrop(eggs, floors):
    def _solve(egg, sf, tf):

        # base case
        if tf - sf == 0 or egg == 0 or tf < 0 or sf < 0:
            return 0
        if egg == 1 or tf - sf == 1:
            return 1
        values = []
        for floor in range(sf, tf):
            # at each floor we have 2 option does egg break or survive so we take max attent
            attempt = max(_solve(egg - 1, 0, floor - 1), _solve(egg, floor + 1, floors))
            values.append(attempt)

        return min(values) + 1

    print(_solve(eggs, 0, floors))


if __name__ == "__main__":
    eggs = 2
    floors = 10
    eggDrop(eggs, floors)
