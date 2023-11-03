# This weeks lesson is FUNCTIONS
# A function is a piece of code we can reuse over and over again

def functionName(parameter):
    print("do action")

def trickOrTreat(goodieBag):
    print("knock or ring the door bell")
    print("Say 'Trick Or Treat!'")
    print("Take some candy from the bowl.")
    candy = input("What candy do you take from the bowl?")
    goodieBag.append(candy)
    
bag = []

while True:
    trickOrTreat(bag)
    print(bag)



