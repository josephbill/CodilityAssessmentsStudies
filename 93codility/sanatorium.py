def solution(A):
    # Sort the guest preferences in ascending order.
    sorted_guests = sorted(A)
    
    # List to keep track of current occupancy of each room.
    rooms = []
    
    for pref in sorted_guests:
        placed = False

        # Check existing rooms to see if the guest can be accommodated.
        for i, room in enumerate(rooms):
            if len(room) + 1 <= pref and len(room) + 1 <= rooms[i][0]:  # Check if adding guest doesn't exceed room's and guest's preference.
                rooms[i].append(pref)
                placed = True
                break

        # If the guest couldn't be accommodated in existing rooms, create a new room.
        if not placed:
            rooms.append([pref])

    return len(rooms)