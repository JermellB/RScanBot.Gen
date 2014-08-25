'''
Created on Jul 30, 2014

@author: Jermell Beane
'''

import smtplib


class Email(object):
    '''
    classdocs
    '''


    def __init__(self):
        '''
        Constructor
        '''
        pass

    
    def sendEmail(self, from_addr, to_addr_list, cc_addr_list,subject, message, login, password, smtpserver='smtp.gmail.com:587'):
        addressList = to_addr_list
        header  = 'From: %s\n' % from_addr
        header += 'To: %s\n' % ','.join(to_addr_list)
        header += 'Cc: %s\n' % ','.join(cc_addr_list)
        header += 'Subject: %s\n\n' % subject
        message = header + message
        
        server = smtplib.SMTP(smtpserver)
        server.starttls()
        server.login(login,password)
        for address in addressList:
            print "emailing" 
            print address + "\n"
            server.sendmail(from_addr, address, message)
        server.quit()