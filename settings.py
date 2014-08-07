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
        self.username = ""
        self.password = ""
        self.userAgent = "Comment scanning bot created by /u/swedishbotmafia used by /u/%s v1" % self.username
        self.postLimit = 10
        self.submissionIdList = None
        self.subredditList = []
        self.botName = "Rbot scanner"
        self.wordList = []
        self.timeToWait = 600
        
        self.from_addr = ""
        self.to_addr_list = []
        self.cc_addr_list = []
        self.login = ""
        self.emailPassword = ""
        self.smtpserver ='smtp.gmail.com:587'