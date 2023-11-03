#Trick or treating with classes

class TrickOrTreater():
    def giveBag(self):
        print("Give Bag.")
    def shout(self):
        print("Shout Trick Or Treat!")
    def getCandy(self):
        print("Get Candy")
    def nextHouse(self):
        print("Go to next house.")

numOfTreaters = 4
treaters = []

for i in range(0, numOfTreaters):
    treaters.append(TrickOrTreater())

print(treaters)


#dallis = TrickOrTreater()
#dallis.giveBag()


        
