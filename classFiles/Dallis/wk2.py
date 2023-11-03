#Trick or treating with classes

class TrickOrTreater():
    def __init__(self):
    def giveBag(self):
        print("Give Bag.")
    def shout(self):
        print ("Say Trick-or-Treat!")
    def getCandy(self):
        print("Get Candy.")
    def nextHouse(self):
        print ("Go to the next house")
    def knock(self):
        print ("Knock on the door")
    def trickOrTreat(self):
        self.knock()
        self.shout()
        self.giveBag()
        self.nextHouse()

numOfTreaters = 4
treaters = []

for i in range(0, numOfTreaters):
    treaters.append(TrickOrTreater())

for treater in treaters:
    treater.trickOrTreat()

print(treaters)
## dallis = TrickOrTreater()
## kesten = TrickOrTreater()
## mom = TrickOrTreater()
## dad = TrickOrTreater()
##
##    dallis.trickOrTreat()
##    kesten.trickOrTreat()
##    mom.trickOrTreat()
##    dad.trickOrTreat()

