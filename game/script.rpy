# The script of the game goes in this file.

define config.history_current_dialogue = True

#_history_list[]
# Declare characters used by this game. The color argument colorizes the
# name of the character.

define e = Character("Eileen", color="aafffc")

define test_novae = Character("Novae", color="aafffc")

define test_aelita = Character("Aelita", color = "FF0000")

# Storage for the flags for all the important comments the player has marked.
define important_comments = {}

# The game starts here.

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

    test_novae "Hello, and welcome to the Winter Fairy Court"

    test_novae "I'm Novae"

    hide nov normal

    show ael normal

    test_aelita "And I'm Aelita"

    hide ael normal

    show nov normal
    
    test_novae "Winter Fairy Court is a peaceful place to live!"

    test_novae "Or at least, it used to be"

    # Uncomment this line to make it so we found the third-option.
    # $ important_comments["third-option"] = True

    menu:
        "Option 1":
            jump test_option1
        "Option 2":
            jump test_option2
        "Option 3" if "third-option" in important_comments:
            jump test_option3

    # This ends the game.

    jump test

label test_option1:
    "You selected option 1."
    jump test

label test_option2:
    "You selected option 2."
    jump test

label test_option3:
    "You selected option 3."
    jump test

label test:

    scene bg room

    show ael normal 

    define something = [
                        ["Index One", False],
                        ["Index Two", True]
                        ]

    #e "[something[0]]"

    python:

        for a in something:
            txt = a[0]
            renpy.say(e, "[txt]")

        
        

    return

