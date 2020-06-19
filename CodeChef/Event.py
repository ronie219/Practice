
# Event
days = {'monday': 1, 'tuesday': 2, 'wednesday': 3, 'thursday': 4, 'friday': 5, 'saturday': 6, 'sunday': 7}
for _ in range(int(input())):
    S, E, L, R = input().split()
    day_interval = (days[E] + 1) - days[S]
    shows = []
    while day_interval <= int(R):
        if day_interval > 0 and day_interval in range(int(L), int(R)+1):
            shows.append(day_interval)
        day_interval += 7
    if len(shows) == 1:
        print(*shows)
    elif len(shows) > 0:
        print('many')
    else:
        print('impossible')
