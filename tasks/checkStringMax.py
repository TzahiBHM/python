#------------------TASK-----------------
"""
- given the following list: ["abcabcabcabc","abcabc","abababab"]
- get from the user a string as input
- print the index of the element that contains the given input - the highest times
"""

#----------------CLASSES-----------------
def check(mainS,st):
    rezef = 0
    count = 0
    for i in range(0,len(mainS)-len(st)+1):
        for j in range(0,len(st)):
            if(mainS[i+j]==st[j]):
                count+=1
        if(count==len(st)):
            rezef+=1
        count=0
    return rezef




#------------------------------MAIN-------------------------
arr = ["abcabcabcabc","abcabc","abababab"]
rez = [0,0,0] #rez = 3*[0]

str_usr = input("Enter Your String: ")
for i in range(len(arr)):
    rez[i] = check(arr[i],str_usr)

#print(rez)
max = rez[0]
for i in range(1,len(rez)):
    if(rez[i]>max):
        max = rez[i]
for i in range(len(rez)):
    if(rez[i]==max):
        print(i)
