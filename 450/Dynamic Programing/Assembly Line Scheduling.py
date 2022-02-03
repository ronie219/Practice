def carAssembly(station, time, entry, exit):

    # we know that if we enter from as1 then we have to pay the cost of entry at level 1 vise versa
    # so we add entry[0] + station[0][0] and entry[1] + station[1][0]
    # same at the end of the exit arr

    # start
    station[0][0] += entry[0]
    station[1][0] += entry[1]
    # end
    station[0][-1] += exit[0]
    station[1][-1] += exit[1]

    as1 = [None for _ in range(len(station[0]))]
    as2 = [None for _ in range(len(station[0]))]
    as1[0] = station[0][0]
    as2[0] = station[1][0]

    for idx in range(1, len(station[0])):

        # for Line one we can come from line1 and line2
        line1 = min(
            as1[idx - 1] + station[0][idx],
            as2[idx - 1] + station[0][idx] + time[1][idx],
        )
        line2 = min(
            as2[idx - 1] + station[1][idx],
            as1[idx - 1] + station[1][idx] + time[0][idx],
        )
        as1[idx] = line1
        as2[idx] = line2
    print(as1)
    print(as2)


if __name__ == "__main__":
    station = [[4, 5, 3, 2], [2, 10, 1, 4]]
    time = [[0, 7, 4, 5], [0, 9, 2, 8]]
    e = [10, 12]
    x = [18, 7]
    carAssembly(station, time, e, x)
