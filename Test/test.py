class Account:

    def __init__(self, cb, otb):
        self.currentBalane = cb
        self.otb = otb

    def get_acountInfo(self):
        print(
            f"Current Balance is {self.currentBalane} and Open to Buy {self.otb} ")


class AccountHolderDetail:

    def __init__(self, name, address):
        self.name = name
        self.address = address

    def get_accountHolderDetail(self,):
        print(f"Account Holder Name is {self.name} and Address {self.address}")


class Consumer(Account, AccountHolderDetail):

    def __init__(self, cb, otb, name, address):
        Account.__init__(self, cb, otb)
        AccountHolderDetail.__init__(self, name, address)

    def get_Detail(self):
        self.get_accountHolderDetail()
        self.get_acountInfo()


cs = Consumer(500, 20, "Abhishek", "Bhopal")
cs.get_Detail()


def fuc1():
    pass


print("Hello")


def func(num):
    return True if num % 2 == 0 else False


print(func(5))
"""
Input : ThisIsInCamelCase
Output : this_is_in_camel_case
"""


def convertion(string):
    answer = []
    curr = string[0]
    for idx in range(1, len(string)):
        char = string[idx]
        if char.isupper():
            answer.append(curr.lower())
            curr = char
        else:
            curr += char
    if curr:
        answer.append(curr.lower())
    # print(answer)
    print('_'.join(answer))


convertion('ThisIsInCamelCase')

"""
substring = "shek"
string = "Abhishek is good in python"
"""


def findSubstring(string, target):

    for oidx in range(len(string)):

        if string[oidx] == target[0]:
            start = 0
            while start < len(target):
                if target[start] != string[start + oidx]:
                    break
                start += 1
            else:
                return oidx
    return -1


print(findSubstring("Abhishek is good in python", "good"))
