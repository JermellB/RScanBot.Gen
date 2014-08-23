RScanBot.Gen
============

Reddit comment scanning bot derived from Bot.Gen

Features:

-Email Reports

-Scanning for any subreddits and submissions/comments you would like.



Run and forget kind of thing, emails you only the url's for comments and submissions that matter to you.

Gui for windows, buggy as hell used currently for configuring data persistence, alternate to this is described below.

To run GUI you need Praw and Kivy installed on your computer.

Todo:Executables for Mac,Linux,Win/potentially android(we'll see)

:::todo examples


-> Run bot by command line for now. "python Main.py"


you should get the nice shiny GUI if you have everything set up correctly, then from there you can setup the settings

file by filling in the GUI fields and hitting update settings, then select run bot. Watch magic occur.

Stop bot button kills the bot in an effective manner now.


Notes:

  
  Only tested the email script with google SMTP servers.
  
 ::: 
  
Alternative to using the GUI is to first set the settings with the desired fields.
then update if name = main: to create an aBot object then run the main method.
look at the settingsExample.py folder for a template on how to create settings.py correctly.




