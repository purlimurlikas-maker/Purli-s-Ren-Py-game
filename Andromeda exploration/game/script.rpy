define d = Character("Destiny")
define sm = Character("Space Monster")
define you = Character("You")

image destiny = "images/Destiny.png"
image destiny cold = "images/Destiny-cold.png"
image destiny shocked = "images/Destiny-shocked.png"
image spaceship = im.Scale("images/spaceship.jpg", 1920, 1080)
image controls = im.Scale("images/controls.jpg", 1920, 1080)
image planetfar = im.Scale("images/planet?.png", 1920, 1080)
image planet = im.Scale("images/planet.png", 1920, 1080)
image space = im.Scale("images/space.gif", 1920, 1080)
image space monster = "images/SpaceMonster.png"


label start:
    scene spaceship
    show destiny
    d "Hello, and welcome to the Andromeda Exploration game!"
    d "I've been waiting for someone to talk to."

    menu:
        "Exit the spaceship.":
            jump outside
        "Stay in the spaceship.":
            jump stay

label outside:
    scene space
    show destiny cold
    d "It's freezing out here, it's okay, though, we are immune to the cold after all."

    menu:
        "Go back inside the spaceship.":
            jump stay
        "Explore the galaxy.":
            jump galaxy_explore

label galaxy_explore:
    scene space 
    show destiny
    d "Wow, look at all the stars! This is amazing."
    d "I can't wait to see what else is out there."


    menu:
        "Keep exploring.":
            jump keep_exploring
        "Return to the spaceship.":
            jump return_spaceship

label keep_exploring:
    scene planetfar
    show destiny
    d "Look at that interesting planet. Shall we go explore it?"

    menu: 
        "Land on the planet.":
            jump land_planet
        "Keep flying in space.":
            jump keep_flying_outside

label keep_flying_outside:
    scene space
    d "Isn't space so vast? I wonder what people haven't discovered yet."
    d "Do you see that? I think I see a space monster! We might be in danger, but if you don't risk, you won't discover anything new."

    menu:
        "Return to the spaceship.":
            jump return_spaceship
        "Go see the space monster.":
            jump see_space_monster

label see_space_monster:
    scene space
    show space monster
    d "Woah, that monster is huge! It looks cute though. I think it wants to be friends with us."
    d "Should we go talk to it?"

        
    menu:
        "Let's go talk to the space monster.":
            jump talk_space_monster
        "Let's go back to the spaceship.":
            jump return_spaceship

                    
label talk_space_monster:
    scene space
    show space monster
    d "Hiii, Space Monster, we come from another Galaxy, would you like to be friends with us?"
    sm "7757644332312358707078552341"
    d "It's speaking in numbers, what could that mean?"
    you "I don't know, I think we should go back to the spaceship."
    d "I don't know, maybe let's try to understand what it's telling us?"

    menu:
        "Try to understand what the monster is telling you.":
            jump try_to_understand
        "Go back to the spaceship":
            jump return_spaceship


label try_to_understand:
    scene space
    show space monster
    sm "75685754434532434765658769867987"
    you "I think it's trying to eat us."
    d "I don't know about that."
    you "Let's just return to the spaceship before we get eaten."

    menu:
        "Stay with the monster":
            jump stay_monster
        "Return to the spaceship":
            jump return_spaceship

label return_spaceship:
    scene spaceship
    show destiny
    d "We should head back to the spaceship, it might be dangerous out here."
    d "I can't wait to tell everyone about our adventure!"

    return

                            
label stay_monster:
    scene space
    show destiny shocked
    
    sm "1"
    you "Yep, it's gonna eat us, I don't know why we decided to stay."
    d "You're right."
    sm "0"
    "The monster ate you."

    return
                    

label stay:
    scene spaceship
    show destiny
    d "It's cozy in here."

    menu:
        "Explore the controls.":
            jump explore
        "Explore the galaxy.":
            jump galaxy_explore


label explore:
    scene controls
    show destiny 
    d "These controls are fascinating. Aren't they?"
    d "Wait, what are you doing? You can't just start pressing the buttons."
    d "STOP!"

    menu:
        "Keep pressing the buttons.":
            jump keep_pressing
        "Stop pressing the buttons.":
            jump stop_pressing

label keep_pressing:
    scene controls
    show destiny shocked
    d "Yeah, we are done for. I can't believe you did that. We are going to die!"
    return

label stop_pressing: 
    scene controls
    show destiny shocked
    d "Phew! That was a close one. I can't believe you almost destroyed the spaceship."
    
    menu:
        "Continue exploring the galaxy.":
            jump galaxy_explore
        "Return to the spaceship.":
            jump return_spaceship

label explore_galaxy:
    scene space
    show destiny
    d "Wow, look at all the stars! This is amazing."
    d "I can't wait to see what else is out there."

    menu:
        "Keep exploring.":
            jump keep_exploring_inside
        "Return to the spaceship.":
            jump return_spaceship
            

label keep_exploring_inside:
    scene planetfar
    d "Look at that planet! It looks like it has life on it."

    d "Let's go check it out!"

    menu: 
        "Land on the planet.":
            jump land_planet

        "Keep flying.":
            jump keep_flying_inside

            label keep_flying_inside:
                d "I guess we can keep flying in the spaceship for a bit longer."
                return

label land_planet:
    scene planet
    show destiny
    d "This planet is beautiful! Look at all the colors."

    d "I wonder what kind of creatures live here."

    menu: 
        "Explore the planet.":
            jump explore_planet

        "Return to the spaceship.":
            jump return_spaceship

label explore_planet:
    scene planet
    show destiny
    d "Isn't this planet fascinating? Look at all the beautiful nature."
    d "It's really cool, but I think we should return to the spaceship, atleast for now, it could be dangerous out there."

    menu: 
        "Return to the spaceship.":
            jump return_spaceship


