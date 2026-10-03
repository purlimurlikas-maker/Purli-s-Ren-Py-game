define e = Character("Eileen")


label start:
    scene bg room with dissolve
    show eileen happy
    e "Hello, and welcome to the Andromeda Exploration game!"
    e "I've been waiting for someone to talk to."

    menu:
        "Exit the spaceship.":
            jump outside
        "Stay in the spaceship.":
            jump stay

label outside:
    scene bg whitehouse with dissolve
    show eileen concerned
    e "It's freezing out here!"

    menu:
        "Go back inside the spaceship.":
            jump stay
        "Explore the galaxy.":
            jump explore

label stay:
    show eileen happy
    e "Much better. It's warm in here."

    menu:
        "Explore the controls.":
            scene bg controlroom with dissolve
            show eileen curious
            e "These controls are fascinating."

label explore:
    e "You set off to explore the galaxy."
    return