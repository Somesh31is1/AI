
# Simple Reflex Vacuum Cleaner Agent

def vacuum_agent(location, status):
    if status == "Dirty":
        print(location, "is Dirty. Cleaning...")
        return "Suck"
    else:
        print(location, "is Clean.")
        return "Move"


# Environment
rooms = {
    "A": "Dirty",
    "B": "Dirty"
}

location = "A"

while "Dirty" in rooms.values():
    action = vacuum_agent(location, rooms[location])

    if action == "Suck":
        rooms[location] = "Clean"

    elif action == "Move":
        if location == "A":
            location = "B"
        else:
            location = "A"

print("Final Room Status:", rooms)
print("All rooms are clean!")
