class Star_Cinema:
    hall_list =[]
    @classmethod
    def entry_hall(cls,hall):
        cls.hall_list.append(hall)


class Hall(Star_Cinema):
    def __init__(self,row,cols,hall_no)->None:
        self.seats = {}
        self._show_list = []
        self._rows = row
        self._cols = cols
        self._hall_no = hall_no
        #super().__init__()
        #self._entry_hall(self)
        Star_Cinema.entry_hall(self)

    
    def entry_show(self,id,movie_name,time):
        show_info = (id,movie_name,time)
        self._show_list.append(show_info)

        #allocate seats
        seats =[]
        for i in range(self._rows):
            col =[]
            for j in range(self._cols):
                col.append(None)
            seats.append(col)
        self.seats[id] = seats
    def book_seats(self,id,row,col):
        row=row-1
        col = col-1
        if id not in self.seats:
            print("Doesn't exist")
            return
        seats = self.seats[id]
        
        if row<0 or (self._rows<=row) or col <0 or (self._cols <= col):
            print(f"Invalid seat ({row+1},{col+1})")
            return
        if seats[row][col] is None:
            seats[row][col] = "Booked"
            print(f"seats ({row+1,col+1}) is successfully booked)")
        else:
            print(f"Seat ({row+1,col+1}) is already booked)")
    
    def view_show_list(self):
        print(f"----Available Show----")
        for show_info in self._show_list:
            print(f"Show Id : {show_info[0]}, Movie_Name : {show_info[1]},Time:{show_info[2]}")
    
    def view_available_seats(self,id):
        if id not in self.seats:
            print(f"Invalid!")
            return
        seats = self.seats[id]
        print(f"Available Seats for show {id}")
        for row in range(self._rows):
            for col in range(self._cols):
                if seats[row][col] is None:
                    print("Empty",end=" ")
                else:
                    print("Booked",end=' ')
            print()
#create cinema hall
cinema_hall = Hall(10,10,3)
#Star_Cinema.entry_hall(cinema_hall)
cinema_hall.entry_show("113","Jawan","2.30PM")
cinema_hall.entry_show("115","Avatar","3.30PM")
while True:
    print("\n ===== Star Cineplex Website ====")
    print("1.View show")
    print("2.View Available Seat")
    print("3.Book Tickets")
    print("4.Exit")
    op = int(input("\n Enter Choice: "))
    if op ==1:
        cinema_hall.view_show_list()
    elif op==2:
        id = input("Enter movies id : ")
        cinema_hall.view_available_seats(id)
    elif op==3:
        id = input('Enter id: ')
        seat_amount = int(input('Enter amount of seat: '))
        for _ in range(seat_amount):
            row = int(input('Enter row: '))
            col = int(input('Enter col: '))
            cinema_hall.book_seats(id, row, col)
        # id = input("Enter movies id : ")
        # row =  int(input("Enter row : "))
        # col = int(input("Enter col : "))
    elif op==4:
        break
    


        
    
    

           


    