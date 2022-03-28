def generateBracket(number):
    answer = []

    def inner(open_bracket, closed_bracket, string=''):
        if not closed_bracket:
            answer.append(string)
            return
        # we have 2 option we can select the open bracket and the closed bracket
        # if we have closed bracket < open then after we can choose the close bracket

        # option one to choose the open bracket and send the next call by doing --open
        # if (open_bracket,closed_bracket) in memo.keys():
        if open_bracket:
            inner(open_bracket - 1, closed_bracket, string + '(')

        if open_bracket < closed_bracket:
            inner(open_bracket, closed_bracket - 1, string + ')')



    inner(number, number)
    return answer


print(generateBracket(3))
