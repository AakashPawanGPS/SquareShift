#Importing Functions required
from AirplaneFunctions import orderSeating, AisleSeats, WindowSeats, MiddleSeats


#Inputs
seating_arrangement = input()
passenger_id = input().split(" ")
passenger_id = [int(x) for x in passenger_id]

seating_arrangement_list = []
matrix = []

for i in seating_arrangement:
    try:
        i = int(i);
        matrix.append(i)
        if(matrix.index(i)):
            seating_arrangement_list.append(matrix)
            matrix = []
    except:
        continue


#Output list
aeroplane_seating = []
for dim in seating_arrangement_list:
    seat_grid = []
    for i in range (int(dim[0])):
        seat_grid.append(['xx'] * int(dim[1]))
    aeroplane_seating.append(seat_grid)

passenger_id = orderSeating(passenger_id)

aeroplane_seating, index = AisleSeats(
    aeroplane_seating, passenger_id)
if(index < len(passenger_id)):
    aeroplane_seating, index = WindowSeats(
        aeroplane_seating, passenger_id[index:])
if(index < len(passenger_id)):
    aeroplane_seating = MiddleSeats(
        aeroplane_seating, passenger_id[index:])

for block in aeroplane_seating:
    for rows in block:
        print(rows)
    print("\n")

