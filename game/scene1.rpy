# Scene 1: Intro + Catfight

label s1_start:
    
    play music "gamejam_2025_w_winter1.ogg"
    scene black
    
    "Welcome to the Court of Winter Fairies!"
    "My name is Sylvie, and I am a advisor to the Winter Queen."
    "I have various duties, but the one important to this story is coordinating the winter weather."
    "But, as you will learn, that duty is not mine alone."

    scene office
    show other:
        xcenter 0.75
    with dissolve
        
    other "Hello, Sylvie."
    show mc:
        xcenter 0.25
    with dissolve
    
    mc "Hi, Alyssa, I'm guessing you are visiting on business?"
    other "Yes, I was looking at your notes about the upcoming weather plans."
    mc "Go on."
    other "And there is nothing about the weather for Long Night?"
    show mc annoyed
    mc "I didn't forget if that is what you are asking."
    other "What about the Long Night blizzard?"
    show mc
    mc "I was planning on just letting that night be clear. Have an easy day for everyone."

    jump s1_catfight

label s1_catfight:
    
    other "But it is our greatest Long Night tradition."
    show mc happy
    mc "Along with the treats at home."
    other "That isn't the work of the court."
    show mc
    mc "It is a tradition of us - the members of the court."
    show other angry
    other "The winter weather is our main duty, we don't need to just stay at home and eat treats!"
    show mc annoyed
    mc "Is working to the bone any better?"
    other "It's Long Night! The most important night of the year!"
    show mc neutral
    mc "How does that make it any better?"
    other "How did you become an advisor? Every interesting call you make is just to do work less!"
    mc "That isn't even- And your call, don't make interesting calls, is better?"
    other "Is respecting tradition supposed to be boring!"
    mc "Never changing is boring!"
    show other furious:
        xcenter 0.65
    with move
    other "You crazy upstart!"
    show mc angry:
        xcenter 0.35
    with move
    mc "You old hag!"

    scene black 
    with Dissolve(1.0)
    
    stop music fadeout 1.0
    
    "..."
    "It got even less polite after that."
    "Alyssa stormed out and I was too angry to get anything else done. So I decided to stop by home."

    jump s1_end

label s1_end:
    jump s2_start
