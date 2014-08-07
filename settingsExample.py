'''
Created on Jul 25, 2014

@author: Jermell Beane
'''

class Settings(object):
    '''
    various settings for the bot
    '''


    def __init__(self):
        '''
        Constructor
        '''
        self.db_filename = None
        self.username = "swedishbotmafia"
        self.password = "******"
        self.userAgent = "Comment scanning bot created by /u/swedishbotmafia used by /u/%s v1" % self.username
        self.postLimit = 100
        self.submissionIdList = None
        self.subredditList = ["all","worldnews","python","news"]
        self.botName = "Rbot scanner"
        self.wordList = ["netflix ","comcast ","verizon ","israel ","net neutrality "]
        self.timeToWait = 600
        
        self.from_addr = "swedishbotmafia@gmail.com"
        self.to_addr_list = ["swedishbotmafia@gmail.com","someotheremail@gmail.com","dontuse@yahoo.com"]
        self.cc_addr_list = []
        self.login = "swedishbotmafia@gmail.com"
        self.emailPassword = "******"
        self.smtpserver ='smtp.gmail.com:587'
