def stringAnagram(dictionary, query):
    result = []
    my_dict = {i:dictionary.count(i) for i in dictionary}
    for i in query:
        count = 0
        print(str(sorted(query)))
        if str(sorted(query)) in my_dict.keys():
            print(str(sorted(query)))
            result.append(my_dict.get(sorted(query)))
    return result


dictionary = ['heater', 'cold', 'clod', 'reheat', 'docl']

query = ["codl", "heater", "abcd"]

print(stringAnagram(dictionary, query))