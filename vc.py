def clean_check(rooms):
    return rooms['A'] == 'Clean' and rooms['B'] == 'Clean'

# Starting
rooms = {'A': 'Dirty', 'B': 'Dirty'}
location = 'A'

print(f"Start: {rooms} | Agent at {location}")

steps = 0
while steps < 10:
    print(f"\nStep {steps+1}: At {location} - {rooms[location]}")

    if rooms[location] == 'Dirty':
        # SUCK Operation
        print(f"ACTION: SUCK at {location}")
        rooms[location] = 'Clean'
    else:
        # MOVE Operation
        if location == 'A':
            print("ACTION: RIGHT -> B pe jao")
            location = 'B'
        else:
            print("ACTION: LEFT -> A pe jao")
            location = 'A'

    print(f"Rooms Now: {rooms}")

    if clean_check(rooms):
        print("\n>>> FINAL: Dono Rooms Clean! Kaam Khatam.")
        break

    steps += 1
