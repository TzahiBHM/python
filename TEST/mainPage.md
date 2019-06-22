<div dir="rtl">

# דף עזרה למבחן
## קלט
### input
 מחזיר קלט מהמשתמש בתור מחרוזת

<div dir="ltr">

```python

name = input("Enter Name: ")
```
</div>

### int
ממיר ערך מסויים למספר
<div dir="ltr">

```python
age = input("Enter Age: ")
age = int(age)
print(age)

# or
age = int(input("Enter Age: "))
print(age)
```

</div>

## מחרוזות
### startswith
פונקציה בוליאנית בודקת אם מחרוזת אחת מתחילה במחרוזת אחרת <br />
תחביר:

<div dir="ltr">

```python

varStr.stratwith(value,start,end)

```
</div>
varStr - המחרוזת המקורית <br />
value - המחרוזת שנבדוק אם קיימת <br />
start - אינדקס התחלה <br />
end - אינדקס סוף <br />
הבדיקה מתבצעת מאינדס start <u>עד</u> אינדקס end

<div dir="ltr">

```python

string = "Hello World"
print(string.startswith("He")) # --> True
print(string.startswith("el",1,3)) # from index 1 to index 2 --> True
print(string.startswith("Wo",6,8)) # from index 6 to index 7 --> True
print(string.startswith("wo",6,8)) # 'w' not equal to 'W' --> False 

```

</div>

### endswith
בדיוק כמו startswith רק שהבדיקה מתבצעת מהסוף

<div dir="ltr">

```python
string = "Hello World"
print(string.startswith("d")) # --> False
print(string.endswith("d")) # --> True
print(string.endswith("o",0,5)) # string[4]='o' --> True
```
</div>

## לולאות
### while
תחילת לולאה עם המילה while אחר כך בסוגריים נכתוב את התנאי ואחרי הסוגריים נקודותיים

<div dir="ltr">

```python

while(condition):
    code...
```
</div>


נשתמש ב else אם נרצה לבצע משהו שלא מתקיים בלולאה

<div dir="ltr">

```python

x = 3
y = 2

while(x>y):
    print("TRUE")
else:
    print("FALSE")

# this loop dosn't stop

```

</div>


### for
תחביר לולאת for

<div dir="ltr">

```python

for x in range(start,end,howToContinue)
```

</div>

* x - שם המשתנה עבור כל איטרציה בלולאה
* start - ערך התחלתי ללולאה
* end - ערך סופי לסיום הלולאה לא כולל הערך הנכתב
(הערך הנכתב פחות אחד)
* howToContinue - בכמה לקדם את x בכל איטרציה ? <br />

דוגמאות:

<div dir="ltr">

```python

for x in range(2,5):
    print(x)

"""
OUTPUT:
2
3
4
"""

```

```python

for x in range(0,10,2):
    print(x)

"""
OUTPUT:
0
2
4
6
8
"""

```
</div>


נשתמש ב else אם נרצה להוסיף פקודה נוספת אחרי סיום הלולאה

<div dir="ltr">

```python

for x in range(0,10,2):
    print(x)
else:
    print("THE END")
"""
OUTPUT:
0
2
4
6
8
THE END
"""

```

</div>

#### מעבר על מערך
ניתן לעבור על מערך בשתי צורות
* דרך שם המערך
* דרך גודל המערך

##### דרך שם המערך
<div dir="ltr">

```python

arr = ["Hello", "World"]
for x in arr:
    print (x)

"""
OUTPUT:
Hello
World
"""
```

</div>

##### דרך גודל המערך

<div dir="ltr">

```python

arr = ["Hello", "World"]
for x in range(len(arr)):
    print (arr[x])

"""
OUTPUT:
Hello
World
"""
```

</div>

### עצירת לולאה
נשתמש ב break כדי לעצור לולאה
<div dir="ltr">

```python

cnt = 3
while(cnt>0):
    print(cnt, end=",")
    

    if(cnt==10):
        break
    cnt+=1
"""
OUTPUT:
3,4,5,6,7,8,9,10,
"""

```

</div>

### דילוג על איטרציה
אם נרצה לדלג על איטרציה מסויימת נשתמש ב continue

<div dir="ltr">

```python

for i in range(9):
  if i == 3:
    continue
  print(i, end=" ")
  
"""
OUTPUT:
0 1 2 4 5 6 7 8
"""

```

</div>

## מערכים
נגדיר מערך בתוך סוגריים מרובעים

<div dir="ltr">

```python
arr = ["A","C","B","E","D"]
```

</div>



</div><!-- rtl -->
