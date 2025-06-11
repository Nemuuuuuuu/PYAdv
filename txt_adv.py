def market():
    print("As you approach it, the cacophony of the market seemed to... fade.")
    print("Upon arrival, you look around. A chill runs down your spine as you see nothing but smooth white sufaces where complexions should have been...")
    print("Or perhaps once were.")

def explore():
    print("Ignoring the sounds, you continue your trek across the Abyssal Fog.") #Monster, death. (for now)

name = input("Enter player name: ")
print("The sun rises on your fifth day wandering the Abyssal Fog, Veyne by your side, on your nerves as usual.")
print("Veyne: It's been so long... are we doomed to die here?")
print(f"{name}: Stop your complaining, it's not help-")
print("Veyne: Shut up. Hear that?")
print("Though Veyne's interruption irked you, you close your eyes, listening for any signs of life.")
print("Sure enough... you hear the noise of a bustling market, faint but there.")
print(f"{name} (thinking): Finally, some sign of civilization... but are they to be trusted?")
# can use f before quotation to insert a name or .format() at the end.
choice1 = input("You have a choice. Visit the supposed market, or continue exploring the fog, despite the possible danger? Visit/Explore: ")
if choice1 == "Visit":
    market()
elif choice1 == "Explore":
    explore()
else:
    print("Please type in one of the two choices")


