# The script of the game goes in this file.

define config.history_current_dialogue = True

#_history_list[]
# Declare characters used by this game. The color argument colorizes the
# name of the character.


define mc = Character("Clear Fairy", color="aafffc")

define other = Character("Blizzard Fairy", color = "FF0000")

define boss = Character("Boss Fairy")

define wife = Character("Clear's Wife")

define otherwife = Character("OtherWife")

# Storage for the flags for all the important comments the player has marked.
define important_comments = {}

# The game starts here.

init python:
    def mark_important(str):
        #renpy.say(test_aelita, "bruh")
        important_comments[str] = True

screen make_important_comment(str):
    key 'K_x' action Function(mark_important, str)


label start:

    # Show a background. This uses a placeholder by default, but you can
    # add a file (named either "bg room.png" or "bg room.jpg") to the
    # images directory to show it.

    scene bg room

    # This shows a character sprite. A placeholder is used, but you can
    # replace it by adding a file named "eileen happy.png" to the images
    # directory.

    

    # These display lines of dialogue.

    ###### TEST CONVERSATION ########

    # Detect whether a comment that was capture is part of the list of important comments
    # make the function make_important_comment(str)
    # make_important_comment(str) takes a phrase and will remember that phrase
    # as something important

    show nov normal

    mc "Hello, and welcome to the Winter Fairy Court"

    mc "I'm Novae HEYYYYYYYYYYY"

    hide nov normal

    show ael normal

    other "And I'm Aelita"

    hide ael normal

    show nov normal
    
    mc "Winter Fairy Court is a peaceful place to live!"

    define NewOption = "third-option"

    show screen make_important_comment(NewOption)

    mc "Or at least, it used to be"

    menu:
        "Option 1":
            jump test_option1
        "Option 2":
            jump test_option2
        "Option 3" if NewOption in important_comments:
            jump test_option3

    # This ends the game.

    jump test

label test_option1:
    "You selected option 1."
    jump s1_start

label test_option2:
    "You selected option 2."
    jump test

label test_option3:
    "You selected option 3."
    jump test

label test:
    # This ends the game.
    return

