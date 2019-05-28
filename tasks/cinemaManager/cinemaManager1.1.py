class Movie:
    def __init__(self,name,length):
        self.name=name
        self.length=length

class Saloon:
    seats=80
    #init
    def __init__(self,movieName):
        self.movieName=movieName

    #print seats amount
    def AmountSeats(self):
        print(self.seats)
    #decrease amount by number
    def DecSeats(self,num):
        self.seats-=num

class Planet:
    #create 6 Saloon
    PlanetSaloon=[]
    for x in range(0,6):
        PlanetSaloon.append(Saloon("x"))
    #define 100 movies
    PlanetMov=[]
    for x in range(0,100):
        PlanetMov.append(Movie("0",0))
    #Invite tickets
    #print movies
    def PrintMovies(self):
        for x in range(0,6):
            print(x, self.PlanetSaloon[x].movieName, end="|")
            print()

    def InvTickets(self):
        print("Please Choose Your Movie: ")
        self.PrintMovies()
        x = int(input())
        print("Please Enter How Many Tickets You Want: ")
        y = int(input())
        if(self.PlanetSaloon[x].seats>=y):
            self.PlanetSaloon[x].DecSeats(y)
        else:
            print("NO ENOUGH TICKETS")
    #print all details Planet:
    def PrintDetails(self):
        for i in range(0,6):
            if(self.PlanetSaloon[i].movieName!="x"):
                print("Saloon Number",i,"---",self.PlanetSaloon[i].movieName,"---",80-self.PlanetSaloon[i].seats)

#------------------------MAIN--------------------------
#create Planet
p = Planet()
#create Avatar movie
m1 = Movie("Avatar",120)
#add movie to saloon #0
s0 = Saloon(m1.name)
#Insert Saloon in planet
p.PlanetSaloon[0].movieName = s0.movieName

#create Alis Movie
m2 = Movie("Alis",150)
#add movie to saloon #1
s1 = Saloon(m2.name)
#Insert Saloon in Planet
p.PlanetSaloon[1].movieName=s1.movieName

#Invite 4 tickets for Avatar
p.PlanetSaloon[0].DecSeats(4)
#Invite 6 tickets for Alis
p.PlanetSaloon[1].DecSeats(6)


p.PrintDetails()

            






