## FA2023-IntroToPython
* Instructor: Barbara Compagnoni
* Email: compagnb@gmail.com
* Class Repo: https://github.com/compagnb/FA2023-IntroToPython
* [Vocabulary Sheet](wkNotes/vocab.md)
* [Keywords Sheet](wkNotes/keywords.md)
* [Students Folders](studentWork)

## Week 1: Idle & Variables

### Types of Variables
* String (words, letters, sentences, etc.)
* Integer (whole numbers)
* Float (decimals)
```name = "Barb"
   age = 23
   pi = 3.14
```

### Strings
* Strings are surrounded by single or double quotes ("" or '')
* Use double quotes if you are using contractions
```
firstHere = "Bryce & Kurt"
said = "said, 'There won't be vocabulary words today.'"
```
* Three single quotes in a row (''') will give multiple lines
```
joke = '''How do dinosaurs pay their bills?
With tyrannosaurus checks!'''
```

### Adding Strings
* Strings can only add strings
```name = "Barb"
   age = "23"
   hi = "Hello! My name is"
   iAm = "and I am"
   yrsOld = "years old."
   space = " "
   sentence = hi + space + name + space + iAm + space + age + space + yrsOld
   print(sentence)
```

### Class Code: Hello World!

```# This is a comment

name = input("What is your name?")
print("hello " + name + "!")

ans2 = input("What is your age?")
print("Wow, you are "+ ans2 +" years old!")

```

## Week 2: Lists

### Variable types we have learned so far:
* Integer = whole number like 1, 13, or 3
* Float = not a whole number like 1.5, 1.6, 1.7
* String = word letters or sentence start and end with "
* character = is one letter in "

### Rules of Naming Variables
* You cannot start with a **capitol letter**, **number**, **symbol** or **space**
* You cannot have spaces in names, instead use **camelCase** or an **under_score**

### Arrays
* A list of any of the other variable types, or objects
* Indexes (spaces in the list) start with 0, not one

### Class Code: Candy Bags
```
trickOrTreatBag=["starburst", "candy corn", "kit kat", "Hershey's bar with almonds" ]
print(trickOrTreatBag)
print(trickOrTreatBag[0])

trickOrTreatBag.append("twix - left")
trickOrTreatBag.append("twix - right")
print(trickOrTreatBag)
print(trickOrTreatBag[len(trickOrTreatBag)-1])
trickOrTreatBag.remove("twix - right")
print(trickOrTreatBag[len(trickOrTreatBag)-1])
```

## Week  3: Functions

### Functions
* A function is a piece of code we can reuse over and over again
```
def functionName(parameter):
    print("do action")
```

### Class Code: Trick Or Treat Robot
```
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
```

## Week 4: Conditionals
