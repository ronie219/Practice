pattern = 'abcdef'
# pattern = 'abcdabca'
# pattern = 'gigummcnu'
text = 'ababcdezabcdef'
lookup_array = [0] * len(pattern)
print(lookup_array)

start = 0
end = 1
while end < len(pattern):
    if pattern[start] == pattern[end]:
        lookup_array[end] = start + 1
        end += 1
        start += 1
    elif start != 0:
        start = lookup_array[start - 1]
    else:
        lookup_array[end] = 0
        end += 1
print(lookup_array)

idx = 0
for ele in text:
    if ele == pattern[idx]:
        idx += 1
    else:
        idx = lookup_array[idx]
    if idx == len(pattern):
        print("Found")
        break
else:
    print("Not Found")