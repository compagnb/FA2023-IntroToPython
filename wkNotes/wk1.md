## Commands we used in python's shell:

### Print Hello
`print("hello world")`

### Python Operators (Basic Math)

```print(50 + 50)
   print(150 - 50)
   print(10 * 10)
   print(100 / 25)
```

* **+** is for **Addition**
* **-** is for **Subtraction**
* ***** is for **Multiplication**
* **/** is for **Division**

### Order of Operations
* Computers will follow PEMDAS. This means they will always complete **parenthesis** or groups first, then perform **exponents**, then **multiplication** and **division**, and **addition** and **subtraction** in the end.
* Follow PEMDAS for the following equations:
```5 + 30 * 20 #this will equal 605
   (5 + 30) * 20 #this will equal 700
   ((5 + 30) * 20) / 10 #this will equal 70
   5 + 30 * 20 / 10 #this will equal 65
```

### Challenge: How many Minecraft Boxes?
If I find 200 Mincraft Boxes and make 10 more a day for a year, but loose 3 of them a week. How many will I have?
* Here is a breakdown of the math:
```20 + 10 * 365 #how many boxes I find and make
   3 * 52 #how many boxes I loose
   3670 - 156 #how many boxes I find/make subtracting how many I lost
   20 + 10 * 365 - 3 * 52 #All the math in one line
```
* Here we can do it with variables (placeholders for values)
```foundBoxes = 20
   madeBoxes = 10
   lostBoxes = 3
   foundBoxes + madeBoxes * 365 - lostBoxes * 52
```
