import random
import string
from tqdm import tqdm
from time import sleep


seats = [" -- "] * 9
screen = '''
----------------------
|       SCREEN       |
|                    |
----------------------
1 -> 3
|
v
7
'''

ticket_template = '''
 -----------------------
|screen1:  VB multiplex |
|Seat:{0} time: 10:30     |
|TK No: {1}          |
 -----------------------        
'''
def  select_seat():

    display_seats = ["  " + i  if i =="X" else i for i in seats]
    seating_chart = "    ".join(["\n" + seat if count % 3 == 0 else seat for count, seat in enumerate(display_seats)])
    print(screen + seating_chart)
    seats_selected =input('Please enter the seats you want to book separated by comma - MAX 2 seats per request')
    seats_selected = seats_selected.split(",")
    if len(seats_selected) > 2:
        print("You cannot book more than 2 tickets")
        return
    proceed = check_availability(seats_selected)
    if not proceed:
        print("Seats selected not available - Please select different seats")
        return
    book_seats(seats_selected)
    return is_housefull()


def is_housefull():
    global seats
    for i in seats:
        if i == " -- ":
            return False
    return True

def book_seats(seats_selected):
    global seats
    for i in seats_selected:
        seats[int(i) - 1] = "X"
    create_tickets(seats_selected)

def create_tickets(seats_selected):
    print("Booking confirmed")
    for i in tqdm(range(0, 100), desc="Generating your tickets"):
        sleep(0.01)
    print("Here are your tickets. Enjoy the show!  \n")
    for i in seats_selected:
        tikcet_no = random_string_generator()
        ticket = ticket_template.format(i, tikcet_no)
        print(ticket)

def random_string_generator():
    letters = string.ascii_letters
    return ''.join(random.choice(letters) for i in range(6))


def check_availability(seats_selected):
    global seats
    for i in seats_selected:
        if seats[int(i)-1] == "X":
            return False
    return True


def tikcet_counter():
    while True:
        is_Housefull = select_seat()
        if is_Housefull:
            print("The show is HouseFull")
            break
        more_tickets = input("Do you want to book more tickets - Y/N")
        if more_tickets =="N" or more_tickets == 'n':
            break


if __name__ == "__main__":
    tikcet_counter()

