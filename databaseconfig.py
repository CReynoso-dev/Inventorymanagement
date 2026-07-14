import menus


def config():
    menu_continue = True
    current_screen = menus.database_setup_menu
    while menu_continue:
        userchoice = input(current_screen)
        current_screen = menus.menuholder[current_screen][userchoice]
        print(current_screen)
        if current_screen == menus.database_finished_menu:
            menu_continue = menus.menuholder[menus.database_finished_menu]
            break
        database_name = input()
        if current_screen == menus.createdatabase and database_name != "back":
            menus.menuholder[menus.createdatabase][database_name] = menus.createdatabase2
            #print(menus.menuholder[menus.createdatabase])
            current_screen = menus.menuholder[menus.createdatabase][database_name]
            userreturn = input(current_screen)
            current_screen = menus.menuholder[current_screen][userreturn]
        elif database_name == "back":
            current_screen = menus.database_setup_menu
            #this is where option 1 code ends reminder to improve this dogshit
    return f"{database_name}.db"




print(config())