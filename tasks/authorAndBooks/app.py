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



# authro1 = Author(14,2,95,"moshe")
# print(authro1.AuthorInfo())

# bookrr = 10*[]
# bookrr[0] = Book(14,2,95,"Moshe","smell")
# bookrr[1] = Book(18,5,92,"Yair","Food")
# bookrr[2] = Book(11,1,98,"Robin","Rogatka")

b1 = Book(14,2,95,"Moshe","Smell")
print(b1.BookInfo())
