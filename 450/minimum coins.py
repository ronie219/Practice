
def coin_count(target, coins):

    if target <= 0:
        return 0
    arr = target + 1
    for i in range(len(coins)):
        if target - coins[i] >= 0:
            temp = coin_count(target - coins[i], coins)
            arr = min(arr, temp + 1)
    return arr


coins = [1, 7, 10]
target = 39
<<<<<<< HEAD
print(coin_count(target, coins))

class Test:
    
    def __init__(self,name):
        self.name = name
    
    
    def print_name(self):
        print(self.name)
       
       
object = Test("Abhishek")
object.print_name()
=======
print(coin_count(target, coins))
>>>>>>> 7f688d62f8ef42d5982882d6981075fb426ea81a
