import random 
dice = "Y"
dice = input("Do you wish to roll the dice, Y or N?")
while dice == "N" or dice == "n" :
    
    dice = input("Do you wish to roll the dice, Y or N?")
no = random.randint(1,6)
if dice == "Y" or dice == "y":

    if no ==  1: 
        print(["------"]) 
        print(["       "])
        print(["   0  "])
        print(["      "])
        print(["------"])

    if no == 2:

        print(["------"]) 
        print(["      "])
        print([" 0  0 "])
        print(["      "])
        print(["------"])

    if no ==3:

        print(["------"]) 
        print(["       "])
        print(["  000 "])
        print(["      "])
        print(["------"])

    if no == 4:

        print(["------"]) 
        print([" 0  0 "])
        print(["      "])
        print([" 0   0"])
        print(["------"])

    if no == 5:

        print(["------"]) 
        print([" 0   0"])
        print(["   0  "])
        print([" 0   0"])
        print(["------"])

    if no == 6:

        print(["------"]) 
        print([" 0 0 0 "])
        print(["      "])
        print([" 0 0 0 "])
        print(["------"])




