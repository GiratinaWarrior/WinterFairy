# Scene 2: Vent at Home

label s2_start:
    scene bedroom

    wife "You are back early?"
    mc "You would not believe what happened with (Blizzard)!"
    wife "Oh dear."
    mc "She barged in and insisted that we do a blizzard for Long Night!"
    wife "And you wanted to let it be a clear night this year."
    mc "But no, let's work to the bone again this year, just to have a fancy blizzard!"
    wife "Did she try to give better reasons for it?"
    mc "Tradition, as always. Ignoring the realities of what we are doing."
    wife "What did she actually say?"
    mc "Just that I am lazy all the time and want to slack off!"
    wife "My dearest snowflake, please focus."
    jump s2_tutorial

label s2_tutorial:
    # This should be unlocked via the actual mechanism.
    # Say how to do it in the text box.
    $ important_comments["tut-comment"] = True
    wife "Remember to focus when people are saying something important."
    wife "Just plowing ahead will not serve you well."
    menu:
        "Rant about (Blizzard)'s Views":
            mc "Slacking off, I made a three year reform plan because I'm lazy."
            mc "As opposed to just doing the same thing we always did. Except when we make things fancier."
            wife "That might be true, but..."
            jump s2_tutorial
        "Rant about (Blizzard)'s Approach":
            mc "And she didn't bring anything up when I was assigned the weather this time."
            wife "It would have been good if she had done that. But..."
            jump s2_tutorial
        "Focus on what (Wife) is saying." if "tut-comment" in important_comments:
            mc "Very well, um... Of course, you were saying?"
            jump s2_main

label s2_main:
    wife "What actually happened?"
    mc "(Blizzard) came by and asked me why we weren't having a blizzard on Long Night."
    wife "And then?"
    mc "She wanted to do it because of tradition and I didn't want to do it because of the amount of work it takes everybody."
    mc "And then we went back and forth with nastier and nastier language. She stormed out and I came here."
    wife "Thank-you for explaining."
    wife "..."
    wife "Would you like to rant a bit more?"
    mc "I got it out, we can move on."
    wife "Then, to sorting this out."
    mc "Am I going to have to appologize to (Blizzard)?"
    wife "Even though I am not her biggest fan either, eventually you are both going to have to appologize to each other."
    wife "But what are you doing about the weather on Long Night?"
    mc "I suppose we are still on a clear night, but (Blizzard) probably isn't done trying to change that."
    wife "Are you going to try and convnce her not to?"
    mc "That is hard, we know what the difference is here. There is no surprise information about weather we are missing."
    mc "She just wants it for different reasons."
    mc "(Blizzard) is always excited about the tradition and ceremony of any event."
    # "likes-snow"
    wife "She also really loves snow, especially a fresh snowfall."
    mc "I forgot about that."
    mc "But I don't think that is worth it, not considering how much work it is."
    # "wants-holiday"
    mc "I just don't want another year where the celebrations can't start until people get back from brewing a storm."
    mc "But it seems that (Blizzard) is happy to do that."
    wife "That does sound like her."
    mc "I don't know how to convince her."
    wife "You are going to have to try though, it is your responsibility."
    mc "And if it doesn't work?"
    wife "Isn't this your decision, unless the queen decides to step in."
    mc "I didn't talk to the queen."
    mc "I should go tell her what happened."
    mc "Maybe she can patch this up."
    wife "That would be nice."
    mc "Thanks for talking to me about it."
    mc "Bye love."
    wife "Take care, my snowflake."
    jump s2_end

label s2_end:
    jump test
