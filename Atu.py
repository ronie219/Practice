class Atul:

    # constructor
    def __init__(self, FirstName, LastName, Age):
        self.Fn = FirstName
        self.Ln = LastName
        self.Ag = Age

    def PrintDetails(self):
        print('Your FirstName is {FirstName} and LastName is {LastName} and Age is {Age}'.format(FirstName=self.Fn, LastName=self.Ln,Age=self.Ag))


    def FirstName(self):
        print("welcome " + self.Fn)

    def __str__(self):
        return self.Fn


# a = Atul()
# a.FistName = "Atul"
# a.LastName = "Shrivastav"
#
#
# b = Atul()
# b.FistName = "Abhishek"
# b.LastName = "Biswas"
#
# print(a.FistName)
# print(b.FistName)



a= Atul("Abhishek","Shrivastav",25)
a.Name ="Biswas"
a.PrintDetails()
a.FirstName()
print(a)



