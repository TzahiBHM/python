class Movie:
    def __init__(self,name,length):
        self.name=name
        self.length=length
class Saloon:
    def __init__(self,movieName):
        self.movieName=movieName    
    #build matrix for seats
    seats = []
    cols = 10
    rows = 8
    for i in range(0,cols):
        seats.append([])
        for j in range(0,rows):
            seats[i].append(0)     
    #print available seats
    def PrintSeats(self):
        print("X", end="|")
        for j in range(0,Saloon.rows):
            print(j, end=" ")
        print()
        for i in range(0,Saloon.cols):
            print(i, end="|")
            for j in range(0,Saloon.rows):
                print(Saloon.seats[i][j], end=" ")
            print()





"""-----------------MAIN-----------------"""    
s1 = Saloon("Shrek")
#print(s1.movieName,s1.seats)
s1.PrintSeats()
lin = int(input("Select line: "))
row = int(input("Select row: "))
s1.seats[lin][row]=1
s1.PrintSeats()

    

