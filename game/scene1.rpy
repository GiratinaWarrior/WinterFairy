# Scene 1: Intro + Catfight

label s1_start:
    scene office
    
    play music "gamejam_2025_w_winter1.ogg"
    
    "Welcome to the Court of Winter Fairies!"
    "My name is (Clear), and I am a advisor to the Winter Queen."
    "I have various duties, but the one important to this story is coordinating the winter weather."
    "But, as you will learn, that duty is not mine alone."

    show other:
        xcenter 0.75
    with dissolve
        
    other "Hello, (Clear)."
    show mc:
        xcenter 0.25
    with dissolve
    
    mc "Hi, (Blizzard), I'm guessing you are visiting on business?"
    other "Yes, I was looking at your notes about the upcoming weather plans."
    mc "Go on."
    other "And there is nothing about the weather for Long Night?"
    mc "I didn't forget if that is what you are asking."
    other "What about the Long Night blizzard?"
    mc "I was planning on just letting that night be clear. Have an easy day for everyone."

    jump s1_catfight

label s1_catfight:
    other "But it is our greatest Long Night tradition."
    mc "Along with the treats at home."
    other "That isn't the work of the court."
    mc "It is a tradition of us - the members of the court."
    other "The winter weather is our main duty, we don't need to just stay at home and eat treats!"
    mc "Is working to the bone any better?"
    other "It's Long Night! The most important night of the year!"
    mc "How does that make it any better?"
    other "How did you become an advisor? Every interesting call you make is just to do work less!"
    mc "That isn't even- And your call, don't make interesting calls, is better?"
    other "Is respecting tradition supposed to be boring!"
    mc "Never changing is boring!"
    other "You crazy upstart!"
    mc "You old hag!"

    hide mc with dissolve
    hide other with dissolve

    scene black 
    with dissolve(3)
    
    "..."
    "It got even less polite after that."
    "(Blizzard) stormed out and I was too angry to get anything else done. So I decided to stop by home."

    jump s1_end

label s1_end:
    jump s2_start
