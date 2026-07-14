database_finished_menu = """
=================================
      SETUP COMPLETE
=================================
Database setup has been completed.

Thank you for using the
Database Setup Utility.

=================================
"""

database_setup_menu = """
    =================================
            DATABASE SETUP
    =================================
    1. Name of Database
    2. Finished
    =================================
    """
createdatabase = """
    =================================
          CREATE DATABASE
    =================================
    Enter the name of the database.
    Enter (Back) to return to main menu.

    Database Name:
    =================================
    """

createdatabase2 = """
    =================================
          DATABASE CREATED
    =================================
    The database has been created
    successfully.

    Press Enter to continue.
    =================================
    """


menuholder = {database_setup_menu: {"1": createdatabase,"2":database_finished_menu},
                createdatabase: {"back": database_setup_menu},
                createdatabase2: {"": database_setup_menu},
                database_finished_menu: False


              }










