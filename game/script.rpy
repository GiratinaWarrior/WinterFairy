# The script of the game goes in this file.

define config.history_current_dialogue = True

#_history_list[]
# Declare characters used by this game. The color argument colorizes the
# name of the character.


define mc = Character("Clear Fairy", color="3F718D")

define other = Character("Blizzard Fairy", color = "7377DC")

define boss = Character("Boss Fairy")

define wife = Character("Clear's Wife")

define otherwife = Character("OtherWife")

# Storage for the flags for all the important comments the player has marked.
define important_comments = {}

# The game starts here.

# mark_important(str) takes an arbitrary string and maps it to True on important_comments
init python:
    def mark_important(str):
        #renpy.say(test_aelita, "bruh")
        important_comments[str] = True

# make_important_comment(str) is a screen that display a prompting overlay
# indiciating that the X key (or any chosen key) can be pressed to continue
# a conversation based on the last thing a character just said
# used for when a character says something insightful that may give more information
screen make_important_comment(str):
    key 'K_x' action Function(mark_important, str)
    imagebutton:
        auto "EmptyButton_%s.png"

# Images

# declarations of images, images have Normal appended to them by convention to indicate
# the emotion they signifiy
image mc = "MC_Sketch.png"
image other = "Blizzard_Fairy_Sketch.png"
image boss = "Queen_Sketch.png"

label start:

    jump s1_start

    # display the background, can be changed at any point
    scene room


    show mc at left
    with dissolve

    mc "Testing testing. Clear Fairy Testing"

    show other at right
    with dissolve

    other "Blizzard Fairy Testing. 1 2 3 4 5."
    
    show boss
    with dissolve

    define NewOption = "Winter Solstice"

    show screen make_important_comment(NewOption)

    other "A wonderous blizzard"

    hide screen make_important_comment

    menu:
        "Indeed, it shalt be a clear day" :
            jump test_option1
        "A wonderous what now?" if NewOption in important_comments:
            jump test_option2

    # This ends the game.

    jump test

label test_option1:
    "You selected option 1."
    jump s1_start

label test_option2:
    "You selected option 2."
    jump s1_start

label test:

    return