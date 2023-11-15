def solution(A):
    # Sort the guest preferences in ascending order.
    sorted_guests = sorted(A)
    
    # List to keep track of current occupancy of each room.
    rooms = []
    
    for pref in sorted_guests:
        # track a current room status 
        placed = False

        # Check existing rooms to see if the guest can be accommodated.
        for i, room in enumerate(rooms):
            # if the r
            if len(room) + 1 <= pref:  # Check if adding guest doesn't exceed room's and guest's preference.
                rooms[i].append(pref)
                placed = True
                break

        # If the guest couldn't be accommodated in existing rooms, create a new room.
        if not placed:
            rooms.append([pref])

    return len(rooms)

# idea is to check the size of the room i.e. the array rooms and counter check it against the pref array values 
A = [5,2,5,6]

print(solution(A))
