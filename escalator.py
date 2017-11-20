"""Creates the escalator class"""


class Escalator:
    """
    Each escalator is an instance of the escalator class.
    Methods:
    __init__: creates a new escalator
    rate: calculates the rate people leave the escalator
    """

    def __init__(self):
        self.stand_time = eval(input("Enter a standing escalator transit time: "))
        #testfunction() a function that will test if this is a positive number
        self.stand_space = eval(input("Enter the number of stairs between standing people: "))
        #testfuntion()
        self.walk_time = eval(input("Enter a walking escalator transit time: "))
        #testfuntion()
        self.walk_space = eval(input("Enter the number of stairs between walking peopld: "))
        #testfuntion()

    
    @property
    def rate(self):
        return (self.stand_time * self.stand_space) + (self.walk_time * self.walk_space)
