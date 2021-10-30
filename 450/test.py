class Employee:

    def __init__(self, name, age):
        self.age = age
        self.name = name

    def __str__(self):
        return f'{self.name} having age of {self.age}'


if __name__ == '__main__':
    e1 = Employee("Rohit", 25)
    print(e1)
    setattr(e1, "name", "Satyam")
    print(e1)
    a = ["Abhishek",]
    print(isinstance(a, list))

    from itertools import islice

    print(islice("hello",2))
