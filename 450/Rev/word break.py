from sre_constants import RANGE


def wordBreak(line, dictionary):
    dictionary = set(dictionary)
    dp = [0 for _ in range(len(line))]
    for i in range(len(line)):
        count = 0
        for j in range(i+1):
            if line[j:i+1] in dictionary:
                if j > 0:
                    dp[i] += dp[j-1]
                else:
                    dp[i] += 1
        dp[i] = count

    print(dp)


n = 12
B = {"i", "like", "sam",
     "sung", "samsung", "mobile",
     "ice", "cream", "icecream",
     "man", "go", "mango"}
A = "ilike"
wordBreak(A, B)
