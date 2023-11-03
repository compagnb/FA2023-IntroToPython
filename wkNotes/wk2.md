## Variables !!!

### Types of Variables
* String (words, letters, sentences, etc.)
* Integer (whole numbers)
* Float (decimals)
```name = "Barb"
   age = 23
   pi = 3.14
```

### Rules of Naming
* You cannot start with a **capitol letter**, **number**, **symbol** or **space**
* You cannot have spaces in names, instead use **camelCase** or an **under_score**

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
* You can mask ints as strings by using **str()**
```name = "Barb"
   age = 23
   hi = "Hello! My name is"
   iAm = "and I am"
   yrsOld = "years old."
   space = " "
   sentence = hi + space + name + space + iAm + space + str(age) + space + yrsOld
   print(sentence)
```

### keyboard input & [Madlibs] Challenge (https://swantonpubliclibrary.org/sites/default/files/mad%20lib%20moon.jpg)
```x = input('enter your name.')
   print('Hello, ' + x)
```

