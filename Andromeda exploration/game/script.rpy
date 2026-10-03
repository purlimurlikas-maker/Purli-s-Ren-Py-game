define e = Character("Eileen")
define sm = Character("Space Monster")
define you = Character("You")


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
            jump galaxy_explore

label galaxy_explore:
    e "Wow, look at all the stars! This is amazing."
    e "I can't wait to see what else is out there."


    menu:
        "Keep exploring.":
            jump keep_exploring
        "Return to the spaceship.":
            jump return_spaceship

label keep_exploring:
    e "Look at that interesting planet. Shall we go explore it?"

    menu: 
        "Land on the planet.":
            jump land_planet
        "Keep flying in space.":
            jump keep_flying_outside

label keep_flying_outside:
    e "Isn't space so vast? I wonder what people haven't discovered yet."
    e "Do you see that? I think I see a space monster! We might be in danger, but if you don't risk, you won't discover anything new."

    menu:
        "Return to the spaceship.":
            jump return_spaceship
        "Go see the space monster.":
            jump see_space_monster

label see_space_monster:
    e "Woah, that monster is huge! It looks cute though. I think it wants to be friends with us."
    e "Should we go talk to it?"

        
    menu:
        "Let's go talk to the space monster.":
            jump talk_space_monster
        "Let's go back to the spaceship.":
            jump return_spaceship

                    
label talk_space_monster:
    e "Hiii, Space Monster, we come from another Galaxy, would you like to be friends with us?"
    sm "7757644332312358707078552341"
    e "It's speaking in numbers, what could that mean?"
    you "I don't know, I think we should go back to the spaceship."
    e "I don't know, maybe let's try to understand what it's telling us?"

    menu:
        "Try to understand what the monster is telling you.":
            jump try_to_understand
        "Go back to the spaceship":
            jump return_spaceship


label try_to_understand:
    sm "75685754434532434765658769867987"
    you "I think it's trying to eat us."
    e "I don't know about that."
    you "Let's just return to the spaceship before we get eaten."

    menu:
        "Stay with the monster":
            jump stay_monster
        "Return to the spaceship":
            jump return_spaceship

label return_spaceship:
    e "We should head back to the spaceship, it might be dangerous out here."
    e "I can't wait to tell everyone about our adventure!"

    return

                            
label stay_monster:
    
    sm "1"
    you "Yep, it's gonna eat us, I don't know why we decided to stay."
    e "You're right."
    sm "0"
    "The monster ate you."

    return
                    

label stay:
    e "It's cozy in here."

    menu:
        "Explore the controls.":
            jump explore
        "Explore the galaxy.":
            jump galaxy_explore


label explore:
    show eileen curious
    e "These controls are fascinating. Aren't they?"
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
            jump galaxy_explore
        "Return to the spaceship.":
            jump return_spaceship

label explore_galaxy:
    e "Wow, look at all the stars! This is amazing."
    e "I can't wait to see what else is out there."

    menu:
        "Keep exploring.":
            jump keep_exploring_inside
        "Return to the spaceship.":
            jump return_spaceship
            

label keep_exploring_inside:
    e "Look at that planet! It looks like it has life on it."

    e "Let's go check it out!"

    menu: 
        "Land on the planet.":
            jump land_planet

        "Keep flying.":
            jump keep_flying_inside

            label keep_flying_inside:
                e "I guess we can keep flying in the spaceship for a bit longer."
                return

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
    e "It's really cool, but I think we should return to the spaceship, atleast for now, it could be dangerous out there."

    menu: 
        "Return to the spaceship.":
            jump return_spaceship


