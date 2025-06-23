name = input("Enter player name: ")

def encounter():
    second_choice = input("Your heart races as the creature approaches you. Will you fight, or run? Fight/Run: ")
    if second_choice == "Fight":
        print("Your heart races as you approach the creature, knife ready.")
        print("Branches extend from its head like horns, dead leaves decorating them.")
        print("Its face is hollow and black, two red dots resembling eyes stare into your soul from its abyss.")
        print("You hear the thumps of its stick-like legs hitting the ground, the creaking of wood shakes your soul.")
        print("Mixed with Veyne's pants are the sounds of echoing screams, perhaps previous victims.")
        print("Veyne: What is that??")
        print("He plants his feet, hands shaking, holding his worn blade. Fear turns his complexion pale as he starts to walk backwards.")
        print("More loud creaking sounds drown out Veyne's escape as you take a deep breath, ready to face what it, whatever 'it' is, throws at you.")
        print("It swings a blade-like arm at you at a speed unreal for its size, leaving you with a scar across your chest, even after just barely evading the attack.")
        print("Putting your years of training to use, you disappear into the shadows, swiftly circling the beast, attacking the moment you find a blind spot.")
        print("You lunge forward, driving your blade into its back... where the heart should be.")
        print("Though it roared in pain and anger, the creature did not fall.")
        print("A branch extends from its back, and you try to escape, but it grabs you by the leg.")
        print("Pain surges through your body as the branch starts to thicken, swallowing you entirely...")
        death()
        start()

def market():
    print("As you approach it, the cacophony of the market seemed to... fade.")
    print("Upon arrival, you look around. A chill runs down your spine as you see nothing but smooth white sufaces where complexions should have been...")
    print("Or perhaps once were.")

def explore():
    print("Ignoring the sounds, you continue your trek across the Abyssal Fog.") #Monster, death. (for now)
    print("After what felt like hours of walking, a deafening creaking sound shakes the ground.")
    print("Veyne gasps.")
    print("Veyne: What the--")
    print("A shadow emerges from the fog.")
    encounter()

def death():
    print("You open your eyes, finding yourself in the fog once more. A daydream?")

def start():
    print("The sun rises on your fifth day wandering the Abyssal Fog, Veyne by your side, on your nerves as usual.")
    print("Veyne: It's been so long... are we doomed to die here?")
    print(f"{name}: Stop your complaining, it's not help-")
    print("Veyne: Shut up. Hear that?")
    print("Though Veyne's interruption irked you, you close your eyes, listening for any signs of life.")
    print("Sure enough... you hear the noise of a bustling market, faint but there.")
    print(f"{name} (thinking): Finally, some sign of civilization... but are they to be trusted?")
# can use f before quotation to insert a name or .format() at the end.
def choice1():
    first_choice = input("You have a choice. Visit the supposed market, or continue exploring the fog, despite the possible danger? Visit/Explore: ")
    if first_choice == "Visit":
        market()
    elif first_choice == "Explore":
        explore()
    else:
        print("Please type in one of the two choices")
        choice1()


# THIS IS THE START OF THE GAME

start()
choice1()





