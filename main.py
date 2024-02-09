name = input("Enter name: ")
person = {
    "Darth Vader": "father",
    "Leia": "sister",
    "Han": "brother in law",
    "R2D2": "droid"
}
def find_relatives(ism, inson):
    for people in inson.keys():
        if ism == people:
            print(f"Luke i'm your {inson[people]}")
            break
    else:
        print("Nope")
find_relatives(name, person)
