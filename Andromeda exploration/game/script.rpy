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
            e "These controls are fascinating. Arent they?"

label explore:
    e "Wait, what are you doing? You can't just start pressing the buttons."
    e "STOP!"
    
    menu: 
        "Keep pressing the buttons.":
            jump keep_pressing

        "Stop pressing the buttons.":
            jump stop_pressing

label keep_pressing:
    e "Yeah, we are done for. I can't believe you did that. We are going to die!"
    return

label stop_pressing: 
    e "Phew! That was a close one. I can't believe you almost destroyed the spaceship."
    
menu:  
    "Continue exploring the galaxy.":
        jump explore_galaxy

        label explore_galaxy:
            e "Wow, look at all the stars! This is amazing."
            e "I can't wait to see what else is out there."
            
        menu: 
            "Keep exploring.":
                jump keep_exploring

            "Return to the spaceship.":
                jump return_spaceship
            

label keep_exploring:
    e "Look at that planet! It looks like it has life on it."

    e "Let's go check it out!"

    menu: 
        "Land on the planet.":
            jump land_planet

        "Keep flying.":
            jump keep_flying

label land_planet:
    e "This planet is beautiful! Look at all the colors."

    e "I wonder what kind of creatures live here."

    menu: 
        "Explore the planet.":
            jump explore_planet

        "Return to the spaceship.":
            jump return_spaceship

label explore_planet:
    e "Isn't this planet fascinating? Look at all the beautiful nature."

label return_spaceship:
    e "We should head back to the spaceship before it gets dark."

    e "I can't wait to tell everyone about our adventure!"

    return
