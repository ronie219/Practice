# intervals = [[1, 3], [2, 6], [8, 10], [15, 18]]
intervals = [[1,4],[2,3]]
sub_interval = []
output = []
intervals.sort(key = lambda x: x[0])
print(intervals)
for i in intervals:
    if not sub_interval:
        sub_interval = i
    else:
        if sub_interval[1] >= i[0]:
            sub_interval[1] = max(i[1],sub_interval[1])
        else:
            output.append(sub_interval)
            sub_interval = i
output.append(sub_interval)
print(output)