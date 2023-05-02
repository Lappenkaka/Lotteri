import random

class lotteri:
    def __init__(self):
        self.list_vinster = [
        "solstol",
        "röd porsche",
        "handduk",
        "10 liter tvål",
        "BMX cykel",
        "surf bräda",
        "burton snowboard",
        "ockelbo 500",
        "lyx yatch",
        "iphone 1"
        ]

    def get_vinst(self):
        slumptal = random.randint(0,9)
        return self.list_vinster[slumptal]
    