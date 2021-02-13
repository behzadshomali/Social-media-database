from socialApp import *
import time

PRIMARYCOLOR = '\033[1m\033[95m'
SECONDARYCOLOR = '\033[1m\033[92m'
RESETCOLOR = '\033[0m'

def print_grid(commands, definitions):
    print()
    print()
    time.sleep(.1)
    print(PRIMARYCOLOR+'-'*105 + RESETCOLOR)
    time.sleep(.1)
    print(PRIMARYCOLOR+'| ' + RESETCOLOR + '{:25s}{}|{} {:75s}{}|{}'.format('Command'.center(25), PRIMARYCOLOR, RESETCOLOR, 'Definition'.center(75), PRIMARYCOLOR, RESETCOLOR))
    print(PRIMARYCOLOR+'-'*105+RESETCOLOR)
    for i in range(len(commands)):
        time.sleep(.1)
        print(PRIMARYCOLOR+'| ' + RESETCOLOR + '{:25s}{}|{} {:75s}{}|{}'.format(commands[i], PRIMARYCOLOR, RESETCOLOR, definitions[i], PRIMARYCOLOR, RESETCOLOR))
    print(PRIMARYCOLOR+'-'*105+RESETCOLOR)


def setup():
    commands = [
    'P_posts',
    'P_actions',
    'P_skill_connections',
    'P_same_nationality',
    'P_view_like',
    'P_hashtag_friend_trend',
    'S_hashtag_trend',
    'S_hashtag',
    'S_post_trend',
    'S_ip_gender_group',
    'S_print_queries',
    'S_exit',
    'S_clear',
    'S_insert_post',
    'S_insert_event',
    'S_insert_person',
    'S_update_post',
    'S_update_event',
    'S_update_person',
    'S_create_poll',
    'S_create_influencer',
    'S_get_tables',
    'S_delete_post',
    'S_delete_event',
    'S_delete_person'
    ]
    definitions = [
        'Retrieve all the posts of intended person',
        'Retrieve all info about like/comment of intended person by the input date',
        'Retrieve all connections who are skilful at the intended skill',
        'Retrieve all the posts containing intended hashtag',
        'Retrieve all the posts in conjunction with View/Like # of intended person',
        'Retrieve top-K hashtags highly used by intended person connection',
        'Retrieve all people who are from the same nation of the intended person',
        'Retrieve top_K trend hashtags since the intended time',
        'Retrieve all trend post in the intended hashtag',
        'Retrieve the count and age_avg of the people grouped by their ip and gender',
        'Show the table of queries',
        'Close the connection to database and exit the program',
        'Clear the terminal screen',
        'Insert a new post to database',
        'Insert a new event to database',
        'Insert a new person to database',
        'Update the intended post details',
        'Update the intended event details',
        'Update the intended person details',
        'Create Poll table (if not existed)',
        'Create an imaginary table called Influencer (if not existed)',
        'Retrieve all available tables in the database',
        'Delete the intended post from database',
        'Delete the intended event from database',
        'Delete the intended person from database'
    ]

    return commands, definitions

def introduction(commands, definitions):
    print(PRIMARYCOLOR+'''
Hello everyone! This is a basic implemention of a social app database.
This database has been developed by Behzad Shomali, you can find me on Github,
LinkedIn and Twitter by just searching my full name on the net! Hope you like it :)
Following table is indicates the list of queries:\
'''+RESETCOLOR, end='')
    print_grid(commands, definitions)





if __name__ == '__main__':
	commands, definitions = setup()
	introduction(commands, definitions)
	time.sleep(.2)
	socialApp = SocialApp()


	while True: # Main loop
	    command = input(SECONDARYCOLOR + 'Command > ' + RESETCOLOR)
	    if commands[0].lower() in command.lower():
	        socialApp.get_posts()
	    elif commands[1].lower() in command.lower():
	        socialApp.get_recent_like_comment()
	    elif commands[2].lower() in command.lower():
	        socialApp.get_skilful_connections()
	    elif commands[3].lower() in command.lower():
	        socialApp.get_same_nationality_people()
	    elif commands[4].lower() in command.lower():
	        socialApp.get_post_views_likes()
	    elif commands[5].lower() in command.lower():
	        socialApp.get_connection_top_k_used_hashtags()
	    elif commands[6].lower() in command.lower():
	        socialApp.get_trend_hashtags()
	    elif commands[7].lower() in command.lower():
	        socialApp.get_posts_with_hashtag()
	    elif commands[8].lower() in command.lower():
	        socialApp.get_trend_posts_in_hashtag()
	    elif commands[9].lower() in command.lower():
	        socialApp.groupby_ip_gender()
	    elif commands[10].lower() in command.lower():
	        print_grid(commands, definitions)
	    elif commands[11].lower() in command.lower():
	        socialApp.exit()
	        exit(0)
	    elif commands[12].lower() in command.lower():
	        print(chr(27) + "[2J")
	        print("\033[0;0H")
	    elif commands[13].lower() in command.lower():
	        socialApp.insert_post()
	    elif commands[14].lower() in command.lower():
	        socialApp.insert_event()
	    elif commands[15].lower() in command.lower():
	        socialApp.insert_person()
	    elif commands[16].lower() in command.lower():
	        socialApp.update_post()
	    elif commands[17].lower() in command.lower():
	        socialApp.update_event()
	    elif commands[18].lower() in command.lower():
	        socialApp.update_person()
	    elif commands[19].lower() in command.lower():
	        socialApp.create_poll()
	    elif commands[20].lower() in command.lower():
	        socialApp.create_influencer()
	    elif commands[21].lower() in command.lower():
	        socialApp.show_tables()
	    elif commands[22].lower() in command.lower():
	        socialApp.delete_post()
	    elif commands[23].lower() in command.lower():
	        socialApp.delete_event()
	    elif commands[24].lower() in command.lower():
	        socialApp.delete_person()
	    else:
	        pass

