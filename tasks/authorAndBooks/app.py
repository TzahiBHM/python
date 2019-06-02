#---------------------------CLASSES-------------------------------
class DDate:
    def __init__(self,d,m,y):
        self.date = d
        self.month = m
        self.year = y
    
    def DDateInfo(self):
        return str(self.date) + "/" + str(self.month) + "/" + str(self.year)

class Author(DDate):
    def __init__(self,d,m,y,name):
        DDate.__init__(self,d,m,y)
        self.name = name
    def AuthorInfo(self):
        return self.name + "|" + self.DDateInfo()

class Book(Author):
    def __init__(self,d,m,y,name,bName):
        self.bookName = bName
        Author.__init__(self,d,m,y,name)
    def BookInfo(self):
        return self.bookName + "|" + self.AuthorInfo()

#--------------------------------MAIN-----------------------------------
bookrr = []
#add Books to arr
bookrr.append(Book(14,2,95,"Moshe","smell"))    #0
bookrr.append(Book(18,3,91,"Dani","food"))     #1
bookrr.append(Book(14,1,88,"Moshe","fruits"))    #2
bookrr.append(Book(14,7,89,"Shimo","Malgeza"))    #3
bookrr.append(Book(15,2,88,"Moshe","Traktor"))    #4
bookrr.append(Book(12,1,75,"David","Fraud"))  #5
bookrr.append(Book(14,2,95,"Moshe","Capit"))    #6
bookrr.append(Book(14,2,95,"Shimi","Tree"))    #7
bookrr.append(Book(14,2,95,"Moshe","C"))    #8
bookrr.append(Book(14,2,95,"Peleg","Ferrari"))    #9
    
scan_name = input("Enter Name: ")
for x in range(0,10):
    if(bookrr[x].name==scan_name):
        print(bookrr[x].bookName)
        
