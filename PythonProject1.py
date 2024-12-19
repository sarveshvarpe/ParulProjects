rooms = ["Available"] * 10

def display_rooms():
    available_rooms = rooms.count("Available")
    booked_rooms = rooms.count("Booked")
    print("\nRoom Status Summary:")
    print(f"Available rooms: {available_rooms}")
    print(f"Booked rooms: {booked_rooms}")
    print("Room List:")
    for i in range(len(rooms)):
        print(f"Room {i + 1}: {rooms[i]}")

def check_availability():
    print("\nChecking room availability...")
    available_rooms = [i + 1 for i in range(len(rooms)) if rooms[i] == "Available"]
    if available_rooms:
        print(f"Available rooms: {', '.join(map(str, available_rooms))}")
    else:
        print("No rooms available.")

def book_room():
    room_number = int(input("\nEnter the room number to book (1-10): "))
    if 1 <= room_number <= len(rooms):
        if rooms[room_number - 1] == "Available":
            rooms[room_number - 1] = "Booked"
            print(f"Room {room_number} has been booked.")
        else:
            print(f"Room {room_number} is already booked.")
    else:
        print("Invalid room number.")

def cancel_booking():
    room_number = int(input("\nEnter the room number to cancel booking (1-10): "))
    if 1 <= room_number <= len(rooms):
        if rooms[room_number - 1] == "Booked":
            rooms[room_number - 1] = "Available"
            print(f"Booking for Room {room_number} has been canceled.")
        else:
            print(f"Room {room_number} is not booked.")
    else:
        print("Invalid room number.")

def hotel_management():
    while True:
        print("\nHotel Room Management System")
        print("1. Check Room Availability")
        print("2. Book a Room")
        print("3. Cancel a Booking")
        print("4. Exit")

        choice = input("\nEnter your choice (1/2/3/4): ")

        if choice == "1":
            check_availability()
        elif choice == "2":
            book_room()
        elif choice == "3":
            cancel_booking()
        elif choice == "4":
            print("Exiting the program.")
            break
        else:
            print("Invalid choice. Please try again.")

        display_rooms()

hotel_management()
