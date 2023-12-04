import time

def introduction():
    print("Welcome to the Quest for the Legendary Treasure!")
    print("You find yourself in a small village. The villagers talk about a treasure hidden in a distant cave.")
    print("Your quest is to find this legendary treasure. Your journey begins now...\n")

def make_choice(choices):
    print("Choose your action:")
    for i, choice in enumerate(choices, start=1):
        print(f"{i}. {choice}")

    while True:
        try:
            user_choice = int(input("Enter the number of your choice: "))
            if 1 <= user_choice <= len(choices):
                return user_choice
            else:
                print("Invalid choice. Please try again.")
        except ValueError:
            print("Invalid input. Please enter a number.")

def explore_village():
    print("You decide to explore the village.")
    time.sleep(1)
    print("As you wander, you hear rumors of a mystical cave hidden in the nearby mountains.")
    time.sleep(1)
    print("The villagers speak of a legendary treasure guarded by ancient creatures.")
    time.sleep(1)

def enter_cave():
    print("You decide to enter the cave in search of the legendary treasure.")
    time.sleep(1)
    print("The cave is dark and damp. You can hear strange noises echoing through the tunnels.")
    time.sleep(1)

def face_dragon():
    print("As you venture deeper into the cave, you encounter a fierce dragon!")
    time.sleep(1)
    print("What will you do?")
    choices = ["Fight the dragon", "Try to sneak past", "Offer a peace offering"]
    user_choice = make_choice(choices)

    if user_choice == 1:
        print("You draw your sword and face the dragon in a fierce battle.")
        time.sleep(1)
        print("It's a tough fight, but you manage to defeat the dragon!")
    elif user_choice == 2:
        print("You attempt to sneak past the dragon, but it notices you!")
        time.sleep(1)
        print("The dragon attacks, and you barely escape with your life.")
    elif user_choice == 3:
        print("You offer a peace offering to the dragon.")
        time.sleep(1)
        print("Surprisingly, the dragon accepts and allows you to pass peacefully.")

def find_treasure():
    print("You continue deeper into the cave and finally discover the legendary treasure!")
    time.sleep(1)
    print("Congratulations! You have successfully completed your quest.")

def game_over():
    print("Unfortunately, your journey comes to an end.")
    print("Thank you for playing!")

def main():
    introduction()
    explore_village()

    choices = ["Enter the cave", "Leave the village"]
    user_choice = make_choice(choices)

    if user_choice == 1:
        enter_cave()
        face_dragon()
        find_treasure()
    elif user_choice == 2:
        game_over()

if __name__ == "__main__":
    main()
