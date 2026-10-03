define e = Character("Eileen", color="#c8ffc8")


label start:

    scene bg room with dissolve

    show eileen happy
 
    e "Hello, and welcome to the Andromeda Exploration game!"
    e "I've been waiting for someone to talk to."

    return

menu:
 
    "Exit the spaceship.":
        jump outside
 
    "Stay in the spaceship.":
        jump stay


label outside:

    scene bg whitehouse with dissolve
    show eileen concerned

    e "It's freezing out here!"
    return

menu: 

"Go back inside.":
jump stay

"Stay outside.":
jump outside

label stay:

    show eileen happy

    e "Much better. It's warm in here."
    return

menu: 

    "Explore the controls.":
         
        scene bg controlroom with dissolve
        show eileen curious




