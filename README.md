RScanBot.Gen
============

Reddit comment scanning bot derived from Bot.Gen

Features:

-Email Reports

-Scanning for any subreddits and submissions/comments you would like.



Run and forget kind of thing, emails you only the url's for comments and submissions that matter to you.

Gui for windows, buggy as hell used currently for configuring data persistence, alternate to this is described below.

#todo examples


-> Run bot by command line for now. "python Main.py"


Notes:

  Hover over fields in GUI for example of how the data should be put in.
  
  Only tested the email script with google SMTP servers.
  
  
Alternative to using the GUI is to first set the settings with the desired fields.

go to the if name == main block and uncomment the commented lines except for the print dir(frame)

Comment the currently uncommented lines there. 

