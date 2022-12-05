name = input("Type your name: ")
print("Welcome", name, "to your adventure!")

answer = input("You're on a dirt road, it has come to an end and you can go left or right. Which way do you choose? ").lower()

if answer == "left":
    answer = input("You come to a river, you can walk around it or swim across. Type walk to walk and swim to swim: ")

    if answer == "swim":
        print("You almost make it but half way through the currents got too strong and you drowned, you lose.")
    elif answer == "walk":
        print("A pack of wild wolves ran up and killed you.")
    else:
        print("Not a valid answer. YOU L O S E! ")
elif answer == "right":
    answer = input("You come across an abandoned shack, there might be food but you have no weapons and you don't know if there's any danger, do you want to risk it and go to the shack or keep walking? Type risk it or keep walking: ")

    if answer == "risk it":
        print("""There wasn't any danger! You find a pantry with cans of chili and corn beside some potatos.
Another night survived!""")
        print("You wake the next morning and hear noises outside. You look around for a weapon incase it's a threat and find some rusty knives and some broken chairs.")
        answer = input("Do you choose to take a rusty knife or chair leg? Type knife or chair leg: ")

        if answer == "knife":
            print("The noise schadders away for now but you now have a weapon. You walk outside and have a heart attack. R.I.P")
        elif answer == "chair leg":
            print("""The noise quites down for now but you now have a weapon. You creep outside and someone comes up by surprise and stabs you.
You wake up feeling drowzy and someones dragging you down a path you don't recognize. You try to move but your hands and feet are tied.""")
            answer = input('Do you want to ask them who they are or scream? Type ask them or scream: ')

            if answer == "ask them":
                print("You seem to frighten them a bit, they didn't expect you to be awake yet.")
                print(""" "I'm the one who saved you" """)
            elif answer == "scream":
                print("The stranger didn't see you ass benefical any more and slices your throat.")
            else:
                print("Not a valid answer. YOU L O S E! ")
        else:
            print("Not a valid answer. YOU L O S E!")

    elif answer == "keep walking":
        print("There were no other sources of food along the road, you die.")
    else:
        print("Not a valid answer. YOU L O S E! ")
else:
    print("Not a valid answer. YOU L O S E! ")
