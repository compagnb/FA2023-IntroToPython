def functionNames(parameter):
    print("do action")

def trickOrTreat(goodieBag):
    print ("knock or ring the doorbell")
    print("Say 'Trick-Or-Treat!'")
    print("Take some candy from the bowl.")
    candy = input("What candy do you take from the bowl?")
    goodieBag.append(candy)

bag = []
while True:
    trickOrTreat(bag)
    print(bag)
