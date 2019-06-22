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

### הדפסת מערך
נדפיס מערך באמצות print
הפלט יהיה בסוגריים מרובעים עם גרש/יים מסביב לכל איבר
<div dir="ltr">

```python
arr = ["A","C","B","E","D"]
print(arr)
"""
OUTPUT:
['A', 'C', 'B', 'E', 'D']
"""
```
</div>

אם נרצה להדפיס רק את איברי המערך נשתמש בלולאה ונדפיס כל איבר
<div dir="ltr">

```python
arr = ["A","C","B","E","D"]

for x in arr:
    print(x, end=" ")
"""
OUTPUT:
A C B E D
"""
```
</div>

### הוספת תא למערך
כדי להוסיף תא חדש למערך נשתמש ב append<br />
אין אפשרות לגשת לאינדקס בגודל המערך ולבצע השמה אליו!!!

<div dir="ltr">

```python
arr = ["A","C","B","E","D"]
for x in arr:
    print(x, end=" ")
print() # break row
arr.append("Z")
for x in arr:
    print(x, end=" ")
"""
OUTPUT:
A C B E D
A C B E D Z
"""
```
</div>

### שינוי ערך התא
ניתן לגשת לתא במערך ולשנות את ערכו<br />
** בפייתון יש כמה סוגים של מערכים(רשימות) . אם ניצור את המערך בסוגריים מרובעות כמו שלמדנו לא תהיה בעיה לשנות את ערך התא<br />

<div dir="ltr">

```python
arr = ["A","C","B","E","D"]
for x in arr:
    print(x, end=" ")
print() # break row
arr[0] = "X"
arr[1]="X"
for x in arr:
    print(x, end=" ")
"""
OUTPUT:
A C B E D
X X B E D
"""
```
</div>

### מיון מערך לפי האלף-בית
כדי למיין מערך לפי האלף-בית נשתמש בפונקציה שנקראת sort

<div dir="ltr">

```python
arr = ["A","C","B","E","D"]
for x in arr:
    print(x, end=" ")
print() # break row
arr.sort()
for x in arr:
    print(x, end=" ")
"""
OUTPUT:
A C B E D
A B C D E
"""
```
</div>

### מחיקת תא במערך
מחיקת תא במערך משנה את גודל המערך, נשתמש ב del כדי לבצע את המחיקה

<div dir="ltr">

```python
arr = ["A","C","B","E","D"]
for x in arr:
    print(x, end=" ")
print() # break row
del arr[3]
for x in arr:
    print(x, end=" ")
"""
OUTPUT:
A C B E D
A C B D
"""
```
</div>

## אובייקטים
ניצור אובייקט על ידי התחביר הבא

<div dir="ltr">

```python
objName = {
    Property:Value
}
```
</div>

* objName - שם האובייקט
* proprty - שם המאפיין
* value - ערך המאפיין<br />

דוגמה: ניצור אובייקט חדש בשם person ונאפיין אותו על ידי שם, שם משפחה, וסוגי המוסיקה שהוא שומע

<div dir="ltr">

```python
person = {
    "name": "Bob",
    "LastName": "Abanai",
    "age":18,
    "sounds":["pop","jazz","rock"]
}
```

</div>

### הדפסת פרטי האובייקט
כדי להדפיס את כל פרטי האובייקט נשתמש ב print ונדפיס את שם האובייקט

<div dir="ltr">

```python
print(person)

"""
OUTPUT:
{'name': 'Bob', 'LastName': 'Abanai', 'age': 18, 'sounds': ['pop', 'jazz', 'rock']}
"""
```

</div>

### הדפסת מאפיין ספציפי
כמו במערך, במקום לכתוב את האינדקס אותו אנו רוצים להדפיס נכתוב את שם המאפיין

<div dir="ltr">

```python

print(person["name"],person["LastName"])

"""
OUTPUT:
Bob Abanai
"""
```
</div>

### עריכת מאפיין
ניתן לערוך מאפיין בצורה הבאה:

<div dir="ltr">

```python
person = {
    "name": "Bob",
    "LastName": "Abanai",
    "age":18,
    "sounds":["pop","jazz","rock"]
}
person["name"] = "Sami"
person["LastName"] = "Acabai"

print(person["name"], person["LastName"], "is ",person["age"],"years old")
"""
OUTPUT:
Sami Acabai is  18 years old
"""
```

</div>

### מחיקת מאפיין
נשתמש ב del כדי למחוק מאפיין

<div dir="ltr">

```python
person = {
    "name": "Bob",
    "LastName": "Abanai",
    "age":18,
    "sounds":["pop","jazz","rock"]
}
print("BEFOR",person)
del person["sounds"]

print("AFTER",person)
"""
OUTPUT:
BEFOR {'name': 'Bob', 'LastName': 'Abanai', 'age': 18, 'sounds': ['pop', 'jazz', 'rock']}
AFTER {'name': 'Bob', 'LastName': 'Abanai', 'age': 18}
"""
```
</div>

### בדיקה האם מאפיין נמצא
נשתמש בתנאי ובמילה השמורה in כדי לבדוק אם קיים מאפיין באובייקט

<div dir="ltr">

```python
if "name" in person:
    print("yes")

"""
OUTPUT:
yes
"""
```
</div>
אין אפשרות להשתמש ב else אך אפשר להשתמש ב elif

### הוספת מאפיין לאובייקט
נוסיף מאפיין מקצוע על ידי כתיבת המאפיין החדש וביצוע השמה

<div dir="ltr">

```python
person = {
    "name": "Bob",
    "LastName": "Abanai",
    "age":18,
    "sounds":["pop","jazz","rock"]
}
person["profession"] = "singer"
print(person)

"""
OUTPUT:
{'name': 'Bob', 'LastName': 'Abanai', 'age': 18, 'sounds': ['pop', 'jazz', 'rock'], 'profession': 'singer'}
"""

```
</div>



</div><!-- rtl -->
