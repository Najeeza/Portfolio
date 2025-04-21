# Created by: Najee Jones

# Instructions to the player
def show_instructions():
    print("🏴‍☠️ Pirate Adventure Game")
    print("Collect 6 items to defeat the ghost of Blackbeard and win the treasure!")
    print("Move commands: go North, go South, go East, go West")
    print("Add to Inventory: get 'item name'")
    print("Type 'exit' to quit the game.")
    print("------------------------------------------")


# Player's current status
def show_status(current_room, inventory, rooms):
    print(f"\nYou are in the {current_room}")
    print("Inventory:", inventory)
    if 'item' in rooms[current_room]:
        print(f"You see a {rooms[current_room]['item']}")
    print("------------------------------------------")


# Main game function
def main():
    # The map and items in each room
    rooms = {
        'Main Deck': {
            'North': 'Galley',
            'South': 'Map Room',
            'East': 'Crow’s Nest',
            'West': 'Cargo Hold'  # Starting place
        },
        'Galley': {
            'South': 'Main Deck',
            'East': 'Island Shore',
            'item': 'Rum'
        },
        'Island Shore': {
            'West': 'Galley',
            'item': 'Hat'
        },
        'Crow’s Nest': {
            'West': 'Main Deck',
            'item': 'Magic Compass'
        },
        'Cargo Hold': {
            'East': 'Main Deck',
            'North': 'Brig',
            'South': 'Captain’s Quarters',
            'item': 'Sword'
        },
        'Brig': {
            'South': 'Cargo Hold',
            'item': 'Key'
        },
        'Map Room': {
            'North': 'Main Deck',
            'item': 'Map'
        },
        'Captain’s Quarters': {
            'West': 'Map Room',
            'item': 'Blackbeard'  # Villain!
        }
    }

    # Start the game
    current_room = 'Main Deck'
    inventory = []

    show_instructions()

    # Gameplay loop
    while True:
        show_status(current_room, inventory, rooms)

        # Get player name
        user_input = input("Enter your move: ").strip()

        # Exit the game
        if user_input.lower() == 'exit':
            print("Thanks for playing!")
            break

        # Movement
        if user_input.lower().startswith("go "):
            direction = user_input[3:].capitalize()

            if direction in rooms[current_room]:
                current_room = rooms[current_room][direction]
            else:
                print("You can't go that way!")

        # Item collection
        elif user_input.lower().startswith("get "):
            item_requested = user_input[4:].strip()

            # If the item in the current room matches the input
            if 'item' in rooms[current_room] and rooms[current_room]['item'].lower() == item_requested.lower():
                inventory.append(rooms[current_room]['item'])
                print(f"{rooms[current_room]['item']} retrieved!")
                del rooms[current_room]['item']  # Remove the item from the room
            else:
                print(f"Can't get {item_requested}!")

        else:
            print("Invalid command. Try again.")

        # Check for victory
        if current_room == 'Captain’s Quarters':
            if len(inventory) == 6:
                print("\nYou enter the Captain’s Quarters and face the ghost of Blackbeard!")
                print("You use your items to defeat him and claim the treasure!")
                print("Congratulations! You have collected all items and won the game! SWEEET!")
            else:
                print("\nYou enter the Captain’s Quarters too soon...")
                print("ARRRRG...GAME OVER! The ghost of Blackbeard has defeated you.")
            print("Thanks for playing the game. Hope you enjoyed it. :)")
            break


# This makes sure main() runs
if __name__ == "__main__":
    main()