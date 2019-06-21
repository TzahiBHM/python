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

* int - ממיר ערך מסויים למספר
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
* startwith - פונקציה בוליאנית בודקת אם מחרוזת אחת מתחילה במחרוזת אחרת <br />
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




</div><!-- rtl -->
