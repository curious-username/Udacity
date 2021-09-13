import time
import random

while True:
    def print_style(story):
        '''
        This function receives text from the story_text function.
        After processed, it is given a sleep timer of 0.05,
        then processed with end and sep print arguements
        to allow the text to be printed horizontal.
        0.05 was chosen as a metroid style print.
        '''
        for text in story:
            print(text, end='', sep=' ', flush=True)
            time.sleep(0.02)
        return text

    def story_text(selection):
        '''
        story_text contains all the basic story parts.
        It also processes the entire box of text,
        fed to print style to give it the desired feel.
        '''

        start = ("You've been asleep, or so you thought.\n"
                 "You open your eyes from darkness, to a bright sunny day, "
                 "clear sky, and green grass\n"
                 "It's like the Windows XP default "
                 "background with the rolling hills\n"
                 "It is a lovely day\n"
                 "In this game you will roll a die "
                 "to see if you are successful or not\n"
                 "Higher than 5 will always mean success, "
                 "5 or lower will fail.\n\n")

        menu_story = ("In the distance you observe smoke straight ahead\n"
                      "To your left you see a bunch of holes\n"
                      "To your right you see "
                      "a trail leading to the "
                      "unknown\n\n")

        menu = ("Press 1. To head to the smoke\n"
                "Press 2. To go to the holes\n"
                "Press 3. To go down the trail\n"
                "Press 4. To Quit\n\n")

        smoke = ("You walk towards the smoke, "
                 "you see there is a BBQ in the middle of a grassy "
                 "field.\n Concerned it would start a fire, you dig a hole "
                 "with your hands\n The ground is dry, "
                 "but there is a random bucket full of water\n\n")

        holes = ("You walk a small distance towards the many holes you saw\n"
                 "They look like holes randomly placed, but there "
                 "is a cartoon sized mallot next to them\n"
                 "Cartoon style moles start laughing at you\n"
                 "You hate being laughed at and "
                 "pickup the mallet and start swinging\n"
                 "The only way to win here, is rolling "
                 "the same number as the mole\n\n")

        trail = ("You walk down the trail to realize "
                 "there is nothing anywhere but grass\n"
                 "You try to go back, but the holes and smoke are gone\n"
                 "You are now stuck in the Windows XP background... "
                 "forever\n\n")

        if selection == 'start':
            print_style(start)
        elif selection == 'menu_story':
            print_style(menu_story)
        elif selection == 'menu':
            print_style(menu)
        elif selection == 'smoke':
            print_style(smoke)
        elif selection == ' holes':
            print_style(holes)
        elif selection == 'trail':
            print_style(trail)

    def story_path(selection):
        '''
        story_path provides the outcomes of the player choice,
        fed through from the player function
        '''
        holes_success = ("You rolled the same number as the mole\n"
                         "After bonking the mole, "
                         "the holes disapear like it was never there\n\n")
        holes_fail = ("You failed to match the "
                      "same number as the mole\n"
                      "After hitting the first empty hole, "
                      "the world blew up! yikes!\n\n")
        smoke_fail = ("You failed to roll high enough\n"
                      "You try to pick up the bucket, "
                      "but you have butterfingers "
                      "and drop the bucket full of water.\n"
                      "After digging the hole, "
                      "you realize you don't want to get burned "
                      "and leave the BBQ alone\n\n")
        smoke_success = ("You successfully rolled higher than 5.\n"
                         "You fill the hole with the active bbq ashes "
                         "and dump water on top\n"
                         "Like Smokey always said, "
                         "'Only you can prevent forest fires'\n\n")

        if selection == 'holes_success':
            print_style(holes_success)
        elif selection == 'holes_fail':
            print_style(holes_fail)
        elif selection == 'smoke_fail':
            print_style(smoke_fail)
        elif selection == 'smoke_success':
            print_style(smoke_success)

    def dice_roll():
        '''
        dice_roll was made to provide a random integer
        between 1 and 10, including those numbers
        then returning the result.
        '''
        roll = random.randint(1, 10)
        return roll

    def player(choice):
        '''
        player is where the descisions are made
        after the player picks a path, they will be prompted
        with an extension of the story and call the
        dice_roll function then branching statements are used
        to descide on the path which is selected.
        '''
        dice = dice_roll()
        if choice == '1':
            story_text('smoke')
            if dice > 5:
                story_path('smoke_success')
            else:
                story_path('smoke_fail')
        elif choice == '2':
            story_text('holes')
            if dice > 5:
                story_path('holes_success')
            else:
                story_path('holes_fail')
        elif choice == '3':
            story_text('trail')
        elif choice == '4':
            exit(0)
        else:
            story_text('menu')
        play_again()

    def player_input():
        choice = input('> ')
        return choice

    def play_again():
        '''
        play_again, asking if the player wants to play again.
        '''
        print("Play again? y or n")
        choice = player_input()
        if choice == 'n':
            print('Thanks for playing! Goodbye!')
            exit(0)
        elif choice == 'y':
            main()
        else:
            play_again()

    def main():
        '''
        the main enterance to the game
        '''
        while True:
            story_text('start')
            story_text('menu_story')
            story_text('menu')
            select = player_input()
            player(select)
    break

main()
