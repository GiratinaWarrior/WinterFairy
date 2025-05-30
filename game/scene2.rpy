# Scene 2: Vent at Home

label s2_start:
    scene bedroom
    
    play sound "door_sf.ogg"
    
    show wife at flip:
        xcenter 0.75
    wife "You are back early?"
    
    play music "gamejam_2025_w_home.ogg"
    
    show mc eyes_closed:
        xcenter 0.25
    with dissolve
    mc "You would not believe what happened with Alyssa!"
    wife "Oh dear."
    show mc annoyed
    mc "She barged in and insisted that we do a blizzard for Long Night!"
    show wife concerned
    wife "And you wanted to let it be a clear night this year."
    mc "But no, let's work to the bone again this year, just to have a fancy blizzard!"
    show mc neutral
    show wife conflicted
    wife "Did she try to give better reasons for it?"
    show mc eyes_closed
    mc "Tradition, as always. Ignoring the realities of what we are doing."
    show wife conflicted
    wife "What did she actually say?"
    show mc angry
    mc "Just that I am lazy all the time and want to slack off!"
    show wife serious
    wife "My dearest snowflake, please focus."
    show mc
    jump s2_tutorial

label s2_tutorial:
    show screen make_important_comment("tut-comment")
    wife "Remember to focus when people are saying something important."
    if "tut-comment" not in important_comments:
        "(Press x to mark statements you think are important, they can open up new paths in the future.)"
    hide screen make_important_comment
    wife "Just plowing ahead will not serve you well."
    menu:
        "Rant about Alyssa's Views":
            show mc annoyed
            mc "Slacking off, I made a three year reform plan because I'm lazy."
            mc "As opposed to just doing the same thing we always did. Except when we make things fancier."
            wife "That might be true, but..."
            show mc
            jump s2_tutorial
        "Rant about Alyssa's Approach":
            show mc annoyed
            mc "And she didn't bring anything up when I was assigned the weather this time."
            wife "It would have been good if she had done that. But..."
            show mc
            jump s2_tutorial
        "Focus on what Lyra is saying." if "tut-comment" in important_comments:
            show mc sheepish
            mc "Very well, um... Of course, you were saying?"
            jump s2_main

label s2_main:
    show mc
    wife "What actually happened?"
    mc "Alyssa came by and asked me why we weren't having a blizzard on Long Night."
    wife "And then?"
    mc "She wanted to do it because of tradition and I didn't want to do it because of the amount of work it takes everybody."
    mc "And then we went back and forth with nastier and nastier language. She stormed out and I came here."
    wife "Thank-you for explaining."
    wife "..."
    show wife conflicted
    wife "Would you like to rant a bit more?"
    show mc sheepish
    mc "I got it out, we can move on."
    wife "Then, to sorting this out."
    show mc sheepish
    mc "Am I going to have to apologize to Alyssa?"
    wife "Even though I am not her biggest fan either, eventually you are both going to have to apologize to each other."
    wife "But what are you doing about the weather on Long Night?"
    show mc eyes_closed
    mc "I suppose we are still on a clear night, but Alyssa probably isn't done trying to change that."
    wife "Are you going to try and convince her not to?"
    show mc
    mc "That is hard, we know what the difference is here. There is no surprise information about weather we are missing."
    mc "She just wants it for different reasons."
    mc "Alyssa is always excited about the tradition and ceremony of any event."
    # "other-likes-snow"
    wife "She also really loves snow, especially a fresh snowfall."
    mc "I forgot about that."
    mc "But I don't think that is worth it, not considering how much work it is."
    # "mc-wants-holiday"
    mc "I just don't want another year where the celebrations can't start until people get back from brewing a storm."
    mc "But it seems that Alyssa is happy to do that."
    wife "That does sound like her."
    show mc eyes_closed
    mc "I don't know how to convince her."
    wife "You are going to have to try though, it is your responsibility."
    show mc
    mc "And if it doesn't work?"
    wife "Isn't this your decision, unless the queen decides to step in."
    show mc sheepish
    mc "I didn't talk to the queen."
    mc "I should go tell her what happened."
    mc "Maybe she can patch this up."
    show wife happy
    wife "That would be nice."
    mc "Thanks for talking to me about it."
    show mc happy
    mc "Bye love."
    show wife
    wife "Take care, my snowflake."

    scene black with dissolve
    jump s2_end

label s2_end:
    jump s3_start
