import random

total_rooms = int(input('Total Room Count? > '))
room_layouts = int(input('Number of Room Layouts? >'))

check = True

while check is True:

    room_counts = random.choices(range(5,51), K= room_layouts)

    if sum(room_counts) == total_rooms: 
        
        print(room_counts)
        print(sum(room_counts))
        for unit in enumerate(room_counts):
            print(unit)
        check = False
    
    else:
        continue