import time
class Star_Cinema:
    hall_list = []

    def entry_hall(self, Hall):
        Star_Cinema.hall_list.append(Hall)


class Hall(Star_Cinema):
    seats = {}
    show_list = []

    def __init__(self, rows, cols, hall_no):
        self.__rows = rows
        self.__cols = cols
        self.__hall_no = hall_no
        Star_Cinema.hall_list.append(self)

    def entry_show(self, id, movie_name, time):
        show = (id, movie_name, time)
        self.show_list.append(show)
        show = [[0 for i in range(self.__cols)] for j in range(self.__rows)]
        self.seats[id] = show

    def book_seats(self, name, phone_number, id, seat_list):
        if id in self.seats:
            tickets = []
            booked_tickets = []
            for seat in seat_list:
                if(self.seats[id][seat[0]][seat[1]] == 1):
                    print("-"*50, end="\n")
                    tickets.append(chr(seat[0]+65)+str(seat[1]))
                else:
                    self.seats[id][seat[0]][seat[1]] = 1
                    booked_tickets.append(chr(seat[0]+65)+str(seat[1]))
            print("#####  TICKET BOOKED SUCCESSFULLY #####", end="\n")
            print("-"*70, end="\n")
            print(f"NAME: {name}")
            print(f"PHONE NUMBER: {phone_number}")
            print("\n")
            for movie in Sugandha_Cinema.show_list:
                if(movie[0] == id):
                    print(f"MOVIE NAME: {movie[1]}" +
                        " "*5 + f" MOVIE TIME: {movie[2]}")
            print("TICKETS: ", end="")
            for ticket in booked_tickets:
                print(ticket,end=" ")
            print("\n")
            print(f"HALL: {id}\n")
            print("-"*70, end="\n")
            if(len(tickets)>0):
                print("THESE SEATS WERE BOOKED - ", end=" ")
                for x in tickets:
                    print(x, end=" ")
                print("\n")
                print("-"*50)
        else:
            print("-"*50)
            print("It didn't match with any show!",end="\n")
            print("-"*50)
            
    def view_show_list(self):
        print("-"*70)
        for show in self.show_list:

            print(f"MOVIE NAME:{show[1]}"+" "*5 +
                  f"SHOW ID: {show[0]}" + " "*5 + f"TIME: {show[2]}")
        print("-"*70)

    def view_available_seats(self, id):
        flag = False
        for show in self.show_list:
            if(show[0] == id):
                flag = True
                print(f"MOVIE NAME:{show[1]}"+" " *
                      5 + " "*5 + f"TIME: {show[2]}")
                print("X for already booked seats")
                print("-"*50)
                print("\n")
                j = 65

                for seat in self.seats:
                    if seat == id:
                        for i in range(self.__rows):
                            k = 0
                            for l in range(self.__cols):
                                if(self.seats[seat][i][l] == 0):
                                    print(chr(j)+str(k)+" "*8, end="")
                                else:
                                    print("X"+" "*8, end="")
                                k += 1
                            j += 1
                            print("\n")
        if(flag==False):   
            print("-"*50)
            print("It didn't match with any show!",end="\n")
            print("-"*50)


Sugandha_Cinema = Hall(3, 4, 2)  # rows cols hall_no
Star_Cinema = Star_Cinema()
Sugandha_Cinema.entry_show("ae1020", "Black Adam",
                           time.ctime())  # id, movie_name, time
Sugandha_Cinema.entry_show("ae1030", "White Adam",
                           time.ctime())  # id, movie_name, time

while(True):
    print("1. VIEW ALL SHOWS TODAY")
    print("2. VIEW AVAILABLE SEATS")
    print("3. BOOK TICKET")
    print("ENTER OPTION: ", end="")
    option = int(input())
    if option == 1:
        Sugandha_Cinema.view_show_list()
    if option == 2:
        id = input("ENTER SHOW ID: ")
        Sugandha_Cinema.view_available_seats(id)
    if option == 3:
        print("ENTER CUSTOMER NAME: ", end="")
        name = input()
        print("ENTER CUSTOMER PHONE NO: ", end="")
        phone = input()
        id = input("ENTER SHOW ID: ")
        print("ENTER NUMBER OF TICKETS: ", end="")
        ticket_no = int(input())
        ticket_list = []
        tickets=[]
        for i in range(ticket_no):
            print("ENTER SEAT NO: ", end="")
            ticket = input()
            if(len(ticket)>3 or ord(ticket[0])>68 or ticket[0].islower()):
                print("-"*40, end="\n")
                print(f"INVALID SEAT NO. TRY AGAIN!")
                print("-"*40, end="\n")
                break
            tickets.append(ticket)
            ticket_list.append((ord(ticket[0])-65, int(ticket[1])))
       # print(ticket_list)
        Sugandha_Cinema.book_seats(name, phone, id, ticket_list)
