'''
Created on Jul 23, 2014

@author: Jermell Beane
'''

import praw
import sqlite3
import sys
import time
from datetime import datetime
import settings
from urllib2 import HTTPError
import emailer
import threading
try:
    import cPickle as pickle
except:
    import pickle
import kivyGui

class RedditUpdateBotV1App(kivyGui.RedditUpdateBotV1App):

    def updateSettingsEventHandler(self, instance):
        settings = self.settings
        settings.wordList = []
        settings.username = self.rUsernameInput.text
        settings.password = self.rPasswordInput.text
        settings.from_addr = self.eUsernameInput.text
        settings.login = self.eUsernameInput.text
        settings.emailPassword = self.ePasswordInput.text
        settings.smtpserver = self.eServerAddressInput.text

        settings.to_addr_list = self.eToEmailAddressInput.text.split(',')

        settings.subredditList = self.subredditInput.text.split(',')

        settings.wordList = self.wordsInput.text.split(',')

        print settings.wordList
        print settings.to_addr_list
        print settings.subredditList

        settings.postLimit = self.numberOfPostsInput.text
        settings.timeToWait = self.minutesToWaitInput.text
        settings.postLimit = int(self.settings.postLimit)
        settings.timeToWait = int(self.settings.timeToWait)*60

        settingsObject = self.settings
        settingsObject_open = open(self.pickleFile,'w')
        print self.pickleFile
        print "time between runs: ", settings.timeToWait
        pickle.dump(settingsObject,settingsObject_open)

    def startButtonEventHandler(self, instance):
        self.aBot = Bot()
        #set bot params
        self.aBot.username = self.settings.username
        self.aBot.password = self.settings.password
        self.aBot.postLimit = self.settings.postLimit
        self.aBot.subredditList = self.settings.subredditList
        self.aBot.wordList = self.settings.wordList
        self.aBot.login = self.settings.login
        self.aBot.emailPassword = self.settings.emailPassword
        self.aBot.to_addr_list = self.settings.to_addr_list
        self.aBot.smtpserver = self.settings.smtpserver
        
        #Todo: Bot objects class and, add process to a list that will hold new bot Objects. 
        self.botThread = threading.Thread(name="botThread",target=self.aBot.main)
        self.botThread.setDaemon(True)
        self.botThread.start()
        print "Thread started"

    def stopButtonEventHandler(self, instance):
        self.aBot = None
        sys.exit(0)

    def on_start(self):
        self.pickleFile = "settings.obj"
        self.settings = settings.Settings()
        
        try:
            settingsObject = open(self.pickleFile,'r')
            self.settings = pickle.load(settingsObject)

        except pickle.UnpicklingError:
            pass

        except IOError as e:
            print e
            print "Just enter the settings and hit update settings."
            pass

        except:
            e = sys.exc_info()
            print e

        finally:
            print self.settings.wordList
            self.rUsernameInput.text = self.settings.username
            self.rPasswordInput.text = self.settings.password
            self.eUsernameInput.text = self.settings.from_addr
            self.ePasswordInput.text = self.settings.emailPassword
            self.eServerAddressInput.text = self.settings.smtpserver
            to_addr_list = ','.join(self.settings.to_addr_list)
            self.eToEmailAddressInput.text = to_addr_list.strip()
            subredditList = ','.join(self.settings.subredditList)
            self.subredditInput.text = subredditList.strip()
            print self.settings.wordList
            wordList = ','.join(self.settings.wordList)
            self.wordsInput.text = wordList
            self.numberOfPostsInput.text = str(self.settings.postLimit)
            self.minutesToWaitInput.text = str(self.settings.timeToWait/60)
            self.settings.username = self.rUsernameInput.text
            self.settings.password = self.rPasswordInput.text
            self.settings.from_addr = self.eUsernameInput.text
            self.settings.login = self.eUsernameInput.text
            self.settings.emailPassword = self.ePasswordInput.text
            self.settings.smtpserver = self.eServerAddressInput.text
            self.settings.db_filename = self.settings.username + ".db"
            self.settings.to_addr_list = self.eToEmailAddressInput.text.split(',')
            self.settings.subredditList = self.subredditInput.text.split(',')
            self.settings.wordList = self.wordsInput.text.split(',')

            print self.settings.wordList

            self.settings.postLimit = self.numberOfPostsInput.text
            self.settings.timeToWait = self.minutesToWaitInput.text
            self.settings.postLimit = int(self.settings.postLimit)
            self.settings.timeToWait = int(self.settings.timeToWait)*60
            print self.settings.timeToWait
            print type(self.settings.postLimit)
            print type(self.settings.timeToWait)

class Bot(object):
    '''
    Scans subreddits for certain keywords, sends email if found.
    Bot has-a Username, Password, Database, SettingsProfile
    '''

    def __init__(self):
        '''
        Constructor
        '''
        self.pickleFile = "settings.obj"
        #Load settings from pickle file
        self.settings1 = settings.Settings()
        try:
            settingsObject = open(self.pickleFile,'r')
            self.settings1 = pickle.load(settingsObject)

        except pickle.UnpicklingError:
            pass

        except IOError as e:
            print e
            print "Just enter the settings and hit update settings."
            pass

        except:
            e = sys.exc_info()
            print e
            
        self.emailer1 = emailer.Email()
        self.db_filename = None
        self.username = self.settings1.username
        self.password = self.settings1.password
        self.userAgent = "Comment scanning bot created by /u/swedishbotmafia used by /u/%s v1" % self.username
        self.postLimit = self.settings1.postLimit
        self.submissionIdList = []
        self.emailList = []
        self.subredditList = self.settings1.subredditList
        self.botName = "Rbot scanner"
        self.conn = None
        self.c = None
        self.r = None
        self.wordList = self.settings1.wordList
        self.currentTime = str(datetime.now())
        self.endTime = str(datetime.now())
        self.emailText = ""
        self.wordListDict = {}
        self.firstEmailLine = "Here's the word report. \r\n" 
        self.emailPassword = self.settings1.emailPassword
        self.login = self.settings1.login
        self.to_addr_list = self.settings1.to_addr_list
        self.smtpserver = self.settings1.smtpserver
        self.count = 0
        print self.settings1.timeToWait
        
    def getTime(self):
        nowTime = str(datetime.now())
        return nowTime
  
    def connectToDatabase(self):
        '''
        Connects to DB, saves class connection state
        '''
        
        try:
            self.db_filename = self.botName + '.db'
        
            print "\n" + self.db_filename + "\n"

            conn = sqlite3.connect(self.db_filename)
            c = conn.cursor()
            print 'Connection Successful'
            self.c = c 
            self.conn = conn
            
        except:
            e = sys.exc_info()
            print e
              
    def createDatabase(self):
        '''
        Creates database if one isn't created already.
        '''
        
        try:
            print 'creating table checksAndBalances \n creating word table'   
            
            self.c.executescript("""CREATE TABLE checksAndBalances(id INTEGER PRIMARY KEY AUTOINCREMENT,postId text UNIQUE, postTitle text, done integer, time text)""")
            self.c.executescript("""CREATE TABLE wordsTable(id INTEGER PRIMARY KEY AUTOINCREMENT,urlCol text, time text, emailed integer, word text, commentId text UNIQUE)""")
            self.conn.commit()  
                
        except sqlite3.OperationalError:
            print '\tTable was probably already created.\n'
            pass

        except:
            e = sys.exc_info()
            print e
            
    def checkDatabase(self, pSubmissionId):
        #sqlite3 scripts accept tuples for string formatting
        submissionIdTup = tuple([pSubmissionId])
        
        try:  
            self.c.execute('SELECT * FROM checksAndBalances WHERE postId = ?', submissionIdTup)
            self.conn.commit() 
            
            row = self.c.fetchone()
            
            if row == None:
                return 0
            else:
                return True
            
        except:
            e = sys.exc_info()
            print e
            
    def checkCommentId(self,pCommentId):
         #sqlite3 scripts accept tuples for string formatting
        commentIdTup = tuple([pCommentId])
        
        try:   
            self.c.execute('SELECT * FROM wordsTable WHERE commentId = ?', commentIdTup)
            self.conn.commit() 
            
            row = self.c.fetchone()
            
            if row == None:
                return 0
            else:
                return True
            
        except:
            e = sys.exc_info()
            print e

    def loginToReddit(self):
        '''
        Logs into reddit, returns a praw.Reddit object uses r.login()
        ''' 
        
        username = self.username
        password = self.password
        userAgent = self.userAgent
        
        r = praw.Reddit(user_agent=userAgent)
    
        try:
            r.login(username,password)
            print 'Logged in as:\n\t %s \n' % username
            
        except HTTPError as e:
            print e
            pass
                
        except:
            e = sys.exc_info()
            print e
            pass
               
        self.r = r
    
    def getTopSubredditPosts(self, subreddit):
        '''
        will get the top x posts from a subreddit, inserts post title and post Id into a db
        '''
        try:
            postLimit = self.postLimit
            submissions = self.r.get_subreddit(subreddit).get_hot(limit=postLimit)
            for submission in submissions:

                autoInc = None    
                postIdVar = submission.id
                postTitleVar = submission.title
                done = 0
                dateTimeNow = str(datetime.now())
                postIdListTup = (autoInc,postIdVar,postTitleVar,done,dateTimeNow)

                #check if id is in db already before trying to save
                if self.checkDatabase(postIdVar):
                    pass
                
                else:
                    print postIdListTup
                    print 'inserting data from %s into table' % postIdVar
                            
                    try:  
                        with self.conn: 
                            self.c.execute('INSERT INTO checksAndBalances values (?,?,?,?,?)', postIdListTup)
                            self.conn.commit()
                                    
                    except:
                        e = sys.exc_info()
                        print e
                        print "\n"
                        
                    else:
                        pass
            print "\n"

        except HTTPError:
            print "Encountered non-serious HTTP Error, continuing."
            pass

        except:
            e = sys.exc_info()
            print e
            print "\n"

    def iterateTopSubredditPosts(self):
        for subreddit in self.subredditList:
            self.getTopSubredditPosts(subreddit)
        
    def getSubmissionsNotProcessed(self):
        #select submission id's from checksAndBalances where postBoolDone == 0, save result submissionId's to list
        with self.conn:
            self.c.execute('SELECT postId FROM checksAndBalances WHERE done == 0')
            self.conn.commit()
            while True:
                row = self.c.fetchone()

                if row == None:
                    break

                self.submissionIdList.append(str(row[0])) 

    def searchSubmissionComments(self, submissionId):
        '''
        Gets all submission comments
        '''
        try:
            submission = self.r.get_submission(submission_id=submissionId)
            print "Checking comments of submission id: %s for targeted words" % submission.id
            submission.replace_more_comments(limit=32,threshold=10)
            flat_comments = praw.helpers.flatten_tree(submission.comments)

            for comment in flat_comments:
                self.count += 1

                for word in self.wordList:
                    if word in comment.body.lower():
                        try:
                            #refactor this into a function later that returns a tuple for the query
                            autoInc = None
                            permalink = comment.permalink
                            wTime = str(datetime.now())
                            wEmailed = 0
                            wWord = word
                            wComment = comment.id
                            #make vars into tup
                            commentWordTup = (autoInc,permalink,wTime,wEmailed,wWord,wComment)
                            print "found word! " + word[:-1] + " at: " + permalink
                            #add permalink to db with timestamp and set emailed flag to 0 and the word that it found also set the time
                            with self.conn:
                                #check if comment id is in database if it exists pass
                                if self.checkCommentId(wComment):
                                    print "Duplicate, will skip insertion."
                                    pass
                                else:    
                                    self.c.execute('INSERT INTO wordsTable values (?,?,?,?,?,?)', commentWordTup)
                                    self.conn.commit()
                        except:
                            e = sys.exc_info()    
                            print e
                            print "\n"

        except HTTPError as e:
            print e
            pass

        except:
            e = sys.exc_info()    
            print e
            print "\n"

    def checkTitleForKeywords(self, postId):
        submission = self.r.get_submission(submission_id=postId)
        title = submission.title
        Spermalink = submission.permalink
        wSubmissionId = submission.id
        try:
            print "checking title for targeted words"
            for word in self.wordList:
                if word in title.lower():
                    #refactor this into a function later that returns a tuple for the query
                    autoInc = None
                    permalink = Spermalink
                    wTime = str(datetime.now())
                    wEmailed = 0
                    wWord = word
                    wComment = wSubmissionId
                    #make vars into tup
                    commentTitleTup = (autoInc,permalink,wTime,wEmailed,wWord,wComment)
                    print "found word: " + word[:-1] + " at: " + permalink
                    with self.conn:
                        if self.checkCommentId(wComment):
                            pass
                        #add permalink to db with timestamp and set emailed flag to 0 and the word that it found also set the time
                        else:
                            self.c.execute('INSERT INTO wordsTable values (?,?,?,?,?,?)', commentTitleTup)
                            self.conn.commit()
                        
        except HTTPError:
            pass
                
        except:
            e = sys.exc_info()
            print e
            print "\n"
                    
        
        print "checked %s" % str(self.count) + " comments!"
        print "done \n\n"
        self.count = 0

    def iterateSubmissionIds(self):
        '''
        Cycle through each submission Id
        '''

        for ids in self.submissionIdList:
            # change done flag to 1
            self.searchSubmissionComments(ids)
            self.checkTitleForKeywords(ids)
            tupId = tuple([ids]) 
            with self.conn:
                self.c.execute("UPDATE checksAndBalances SET done = 1 WHERE postId = ?",(tupId))

    def getCommentsforEmailNotProcessed(self):
        #select urls from wordsTable where emailed = 0, save results to a list

        with self.conn:
            #query the words from the words list individually
            #create dictionary of lists with words being the key 
            #wordDict = {'word1':self.emailList,'word2':[someurllist2]}

            for word in self.wordList:
                self.c.execute('SELECT urlCol FROM wordsTable WHERE emailed == 0 AND word = ?',([word]))

                while True:
                    row = self.c.fetchone()
                    try:
                        if row == None:
                            break

                        else:
                            self.emailList.append(str(row[0]))
                             #create word dictionary from loop
                            self.addToWordListDict(word,self.emailList)

                    except UnicodeEncodeError:
                        pass

                    except: 
                        e = sys.exc_info()   
                        print e
                        print "\n"

                self.resetEmailList()

        print "showing words and related URLs:\n" + "="*30 
        for key, value in self.wordListDict.iteritems():
            print key + "\n" + "="*30
            for urls in value:
                print urls
            print "\n"

    def createEmailReport(self):
        self.emailText = ""
        #iterate through word dictionary doing a += for each word then a \n + =*30, iterate through list in the dictionary += listItem\n
        #ex. Word\n=*30
        self.emailText += self.firstEmailLine  + "\r\n \r\n"
        for word, dictlist in self.wordListDict.iteritems():
            self.emailText += word + "\r\n" + "="*30 + "\r\n"
            for urls in dictlist:
                self.emailText += urls + "\r\n"
            self.emailText += "\r\n"

    def checkIfEmailHasAnythingNew(self):
        if self.emailText == self.firstEmailLine  + "\r\n \r\n":
            print "Nothing new not sending an email \n"
        else:
            print "sending email:\n"
            print self.smtpserver
            
            self.emailer1.sendEmail(from_addr=self.settings1.from_addr, to_addr_list=self.to_addr_list, cc_addr_list=[],subject="Word Report for:%s" % str(datetime.now()), 
                message=self.emailText, login=self.login, password=self.emailPassword, smtpserver=self.smtpserver)
            #Set all posts that have been emailed to emailed = 1
            print "updating the words and urls that have been emailed..."
            self.setEmailedtoTrue()

    def iterateEmailList(self):
        #compile all urls not emailed yet
        self.getCommentsforEmailNotProcessed()
        #create email text from words and urls
        print "creating the email report... \n"
        self.createEmailReport()
        self.checkIfEmailHasAnythingNew()
        self.resetSubmissionIdList()
        self.resetEmailList()
        self.resetCurrentWordReport()
        self.resetWordListDict()

    def checkWordList(self):
        pass

    def setEmailedtoTrue(self):
        with self.conn:

            self.c.execute('SELECT urlCol FROM wordsTable WHERE emailed == 0')

            while True:
                row = self.c.fetchone()

                if row == None:
                    break

                else:
                    self.c.execute('UPDATE wordsTable SET emailed = 1 WHERE emailed = 0')

    def resetSubmissionIdList(self):
        self.submissionIdList = []

    def resetEmailList(self):
        self.emailList = []

    def addToWordListDict(self, wordString, dictValue):
        self.wordListDict[wordString] = dictValue

    def resetCurrentWordReport(self):
        del self.emailText

    def resetWordListDict(self):
        self.wordListDict.clear()

    def main(self):
        '''
        Do the harry potter.
        '''
        self.connectToDatabase()
        self.createDatabase()
        self.loginToReddit()

        #main loop
        while True:
            print self.to_addr_list
            print "getting hot posts from subreddits. \n"
            self.iterateTopSubredditPosts()
            print "Getting submissions that haven't been processed. \n"
            self.getSubmissionsNotProcessed()
            print "checking comments of hot posts from desired subreddits. \n"
            self.iterateSubmissionIds()
            print "resetting submission Id list for next loop.\n"
            self.resetSubmissionIdList()
            print "Compiling data for transmission. \n"
            self.iterateEmailList()
            print "waiting %s" % str(self.settings1.timeToWait/60) + " minutes... \n"
            time.sleep(self.settings1.timeToWait)
            

if __name__ == '__main__':
    app = RedditUpdateBotV1App()
    app.setOrientation(orient="vertical")
    app.run()

#todo: Check to see if I'm resetting submissionId List when I reload the pickle after updating settings