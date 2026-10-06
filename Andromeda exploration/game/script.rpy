define d = Character("Destiny")
define sm = Character("Space Monster")
define you = Character("You")
define y = Character("Yellow creature")
define spacegoblin = Character("Space Goblin")

image destiny = "images/Destiny.png"
image destiny cold = "images/Destiny-cold.png"
image destiny shocked = "images/Destiny-shocked.png"
image spaceship = im.Scale("images/spaceship.jpg", 1920, 1080)
image controls = im.Scale("images/controls.jpg", 1920, 1080)
image planetfar = im.Scale("images/planetfar.png", 1920, 1080)
image planet = im.Scale("images/planet.png", 1920, 1080)
image space = im.Scale("images/space.gif", 1920, 1080)
image spacemonster = "images/SpaceMonster.png"
image goblin = "images/goblin.png"
image yellowcreature = "images/cute-creature.png"


label start:
    scene spaceship
    show destiny
    d "Hello, and welcome to the Andromeda Exploration game!"
    d "I've been waiting for someone to talk to."
    d "What do you want to do?"

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
    show spacemonster
    d "Woah, that monster is huge! It looks cute though. I think it wants to be friends with us."
    d "Should we go talk to it?"

        
    menu:
        "Let's go talk to the space monster.":
            jump talk_space_monster
        "Let's go back to the spaceship.":
            jump return_spaceship

                    
label talk_space_monster:
    scene space
    show spacemonster
    d "Hiii, Space Monster, we come from another Galaxy, would you like to be friends with us?"
    sm "7757644332312358707078552341"
    d "It's speaking in numbers, what could that mean?"
    you "I don't know, I think we should go back to the spaceship."
    d "Maybe let's try to understand what it's telling us?"

    menu:
        "Try to understand what the monster is telling you.":
            jump try_to_understand


label try_to_understand:
    scene space
    show spacemonster
    sm "75685754434532434765658769867987"
    d "I think it's trying to eat us."
    you "I don't know about that."
    d "Let's just return to the spaceship before we get eaten."

    menu:
        "Stay with the monster":
            jump stay_monster
        "Return to the spaceship":
            jump return_spaceship

label return_spaceship:
    scene spaceship
    show destiny
    d "It sure was fun exploring with you, and talking to you."
    d "Till the next adventure, comrade."

    return

                            
label stay_monster:
    scene space
    show destiny shocked
    
    you "I'll try petting it."
    d "No! Don't, it might sense danger."

    menu:
        "Pet the creature":
            jump pet
        "Don't pet it":
            jump dont_pet

label pet:
    scene space
    show spacemonster
    you "I'll try petting the creature."
    d "Okay, but if we get eaten, it's your fault."
    sm "388888888"
    "Destiny was right"
    "You shouldn't have pet the creature"
    "You didn't listen"
    "Both of you were eaten"

    return

label dont_pet:
    scene space 
    show spacemonster
    sm "8383940843708270870987493480787295028663976"
    scene space
    show destiny
    d "I think it's harmless unless we go very close to it."
    you "Me too."
    d "Let's return to the spaceship, shall we?"
    you "Okay. Bye, space monster."
    d "Have a nice unit of time, Space Monster."
    scene space
    show spacemonster
    sm "76408740317483676957683740875473374875402748047"

    menu:
        "Return to the spaceship.":
            jump return_spaceship



                    

label stay:
    scene spaceship
    show destiny
    d "It's cozy in here."
    d "Do you want me to show you around?"
    you "Sure, why not?"
    d "Okay, I'll show you the cockpit."

    menu:
        "Explore the controls.":
            jump explore
       


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
        "Explore the galaxy.":
            jump galaxy_explore
        

label explore_galaxy:
    scene space
    show destiny
    d "Wow, look at all the stars! This is amazing."
    d "I can't wait to see what else is out there."

    menu:
        "Keep exploring.":
            jump keep_exploring_inside
       
            

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

    d "Should we go and see?"

    menu: 
        "Explore the planet.":
            jump explore_planet


label explore_planet:
    scene planet
    show destiny
    d "Isn't this planet fascinating? Look at all the beautiful nature."
    d "What's that right there?"

    menu: 
        "Go and see.":
            jump go_see

label go_see:
    scene planet
    show yellowcreature

    d "Aww! It's a yellow creature. What is it saying?"

    y "mrrrppp"

    d "Isn't it so cute?"

    you "It sure is."

    d "I don't think we can take it with us though, it belongs on this planet."

    you "I agree."

    menu:
        "Keep exploring the planet":
            jump keep_exploring_the_planet

label keep_exploring_the_planet:
    scene planet
    show destiny

    d "Do you think we'll spot another cute creature?"
    you "I sure hope so. Let's just hope this planet is safe."

    scene planet
    show goblin
    d "What's that right there? Is that a.. space goblin?"
    you "Ehh.. It's probably harmless."

    menu:
        "Approach it.":
            jump approach
        "Return to the spaceship.":
            jump return_spaceship

label approach:

    d "I don't think it's harmless."
    you "Don't be such a scaredy-cat. Let's try to talk to it."
    spacegoblin "grrrpp"
    "The goblin in fact wasn't harmless"
    "You were eaten by it."

    return