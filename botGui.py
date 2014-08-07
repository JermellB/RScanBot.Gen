# -*- coding: utf-8 -*- 

###########################################################################
## Python code generated with wxFormBuilder (version Jun  5 2014)
## http://www.wxformbuilder.org/
##
## PLEASE DO "NOT" EDIT THIS FILE!
###########################################################################

import wx
import wx.xrc

###########################################################################
## Class BotFrame
###########################################################################

class BotFrame ( wx.Frame ):
	
	def __init__( self, parent ):
		wx.Frame.__init__ ( self, parent, id = wx.ID_ANY, title = u"Reddit Word Notifier Bot V1", pos = wx.DefaultPosition, size = wx.Size( 297,529 ), style = wx.DEFAULT_FRAME_STYLE|wx.SIMPLE_BORDER|wx.TAB_TRAVERSAL )
		
		self.SetSizeHintsSz( wx.Size( 297,529 ), wx.Size( 297,529 ) )
		self.SetFont( wx.Font( wx.NORMAL_FONT.GetPointSize(), 74, 90, 90, False, wx.EmptyString ) )
		self.SetForegroundColour( wx.SystemSettings.GetColour( wx.SYS_COLOUR_BTNHIGHLIGHT ) )
		self.SetBackgroundColour( wx.SystemSettings.GetColour( wx.SYS_COLOUR_ACTIVECAPTION ) )
		
		self.m_statusBar1 = self.CreateStatusBar( 1, wx.ST_SIZEGRIP, wx.ID_ANY )
		self.m_menubar1 = wx.MenuBar( 0 )
		self.m_fileMenu = wx.Menu()
		self.m_QuitOption = wx.MenuItem( self.m_fileMenu, wx.ID_ANY, u"Quit", wx.EmptyString, wx.ITEM_NORMAL )
		self.m_fileMenu.AppendItem( self.m_QuitOption )
		
		self.m_RunBotOption = wx.MenuItem( self.m_fileMenu, wx.ID_ANY, u"Run Bot", wx.EmptyString, wx.ITEM_NORMAL )
		self.m_fileMenu.AppendItem( self.m_RunBotOption )
		
		self.m_AboutOption = wx.MenuItem( self.m_fileMenu, wx.ID_ANY, u"About", wx.EmptyString, wx.ITEM_NORMAL )
		self.m_fileMenu.AppendItem( self.m_AboutOption )
		
		self.m_menubar1.Append( self.m_fileMenu, u"File" ) 
		
		self.SetMenuBar( self.m_menubar1 )
		
		Sizer1 = wx.BoxSizer( wx.VERTICAL )
		
		SizerToHoldSizers = wx.GridSizer( 0, 2, 1, 0 )
		
		RedditAndEmailSizer = wx.BoxSizer( wx.VERTICAL )
		
		self.m_RedditLabel = wx.StaticText( self, wx.ID_ANY, u"Reddit Credentials", wx.DefaultPosition, wx.Size( -1,20 ), 0 )
		self.m_RedditLabel.Wrap( -1 )
		self.m_RedditLabel.SetFont( wx.Font( wx.NORMAL_FONT.GetPointSize(), 75, 90, 90, False, "Aharoni" ) )
		
		RedditAndEmailSizer.Add( self.m_RedditLabel, 0, wx.ALIGN_CENTER|wx.ALL, 5 )
		
		self.RedditUsernameLabel = wx.StaticText( self, wx.ID_ANY, u"Username", wx.DefaultPosition, wx.DefaultSize, wx.ALIGN_CENTRE )
		self.RedditUsernameLabel.Wrap( -1 )
		RedditAndEmailSizer.Add( self.RedditUsernameLabel, 0, wx.ALIGN_CENTER|wx.ALL, 5 )
		
		self.RUnameBox = wx.TextCtrl( self, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, 0|wx.SIMPLE_BORDER )
		self.RUnameBox.SetToolTipString( u"Reddit Username Goes Here" )
		
		RedditAndEmailSizer.Add( self.RUnameBox, 0, wx.ALL, 5 )
		
		self.RedditPasswordLabel = wx.StaticText( self, wx.ID_ANY, u"Password", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.RedditPasswordLabel.Wrap( -1 )
		RedditAndEmailSizer.Add( self.RedditPasswordLabel, 0, wx.ALIGN_CENTER|wx.ALL, 5 )
		
		self.RedditPasswordBox = wx.TextCtrl( self, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, wx.TE_PASSWORD|wx.SIMPLE_BORDER )
		self.RedditPasswordBox.SetToolTipString( u"Reddit Password Goes here" )
		
		RedditAndEmailSizer.Add( self.RedditPasswordBox, 0, wx.ALL, 5 )
		
		self.m_staticText15 = wx.StaticText( self, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText15.Wrap( -1 )
		RedditAndEmailSizer.Add( self.m_staticText15, 0, wx.ALL, 5 )
		
		self.EmailCredentialsLabel = wx.StaticText( self, wx.ID_ANY, u"Email Credentials", wx.DefaultPosition, wx.Size( -1,20 ), 0 )
		self.EmailCredentialsLabel.Wrap( -1 )
		self.EmailCredentialsLabel.SetFont( wx.Font( wx.NORMAL_FONT.GetPointSize(), 75, 90, 90, False, "Aharoni" ) )
		
		RedditAndEmailSizer.Add( self.EmailCredentialsLabel, 0, wx.ALIGN_CENTER|wx.ALL, 5 )
		
		self.EmailUsernameLabel = wx.StaticText( self, wx.ID_ANY, u"Username", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.EmailUsernameLabel.Wrap( -1 )
		RedditAndEmailSizer.Add( self.EmailUsernameLabel, 0, wx.ALIGN_CENTER|wx.ALL, 5 )
		
		self.EmailUsernameBox = wx.TextCtrl( self, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, 0|wx.SIMPLE_BORDER )
		self.EmailUsernameBox.SetToolTipString( u"Email Username.\n\nE.g., someGoogleEmail@gmail.com\n\nI have only tested this with google SMTP servers, I know they work. I don't know and can't provide support for if your smtp servers will work. I used the standard python smtp library to add email functionality." )
		
		RedditAndEmailSizer.Add( self.EmailUsernameBox, 0, wx.ALL, 5 )
		
		self.EmailPasswordLabel = wx.StaticText( self, wx.ID_ANY, u"Password", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.EmailPasswordLabel.Wrap( -1 )
		RedditAndEmailSizer.Add( self.EmailPasswordLabel, 0, wx.ALIGN_CENTER|wx.ALL, 5 )
		
		self.EmailPasswordBox = wx.TextCtrl( self, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, wx.TE_PASSWORD|wx.SIMPLE_BORDER )
		self.EmailPasswordBox.SetToolTipString( u"Email Password Goes Here" )
		
		RedditAndEmailSizer.Add( self.EmailPasswordBox, 0, wx.ALL, 5 )
		
		self.SmtpServerAddressLabel = wx.StaticText( self, wx.ID_ANY, u"Server Address", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.SmtpServerAddressLabel.Wrap( -1 )
		RedditAndEmailSizer.Add( self.SmtpServerAddressLabel, 0, wx.ALIGN_CENTER|wx.ALL, 5 )
		
		self.SmtpServerAddressBox = wx.TextCtrl( self, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, 0|wx.SIMPLE_BORDER )
		self.SmtpServerAddressBox.SetToolTipString( u"Enter the smtp server address here.\n\nE.g., smtp.gmail.com:587" )
		
		RedditAndEmailSizer.Add( self.SmtpServerAddressBox, 0, wx.ALL, 5 )
		
		self.ToEmailAddressesLabel = wx.StaticText( self, wx.ID_ANY, u"To Email Addresses", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.ToEmailAddressesLabel.Wrap( -1 )
		RedditAndEmailSizer.Add( self.ToEmailAddressesLabel, 0, wx.ALIGN_CENTER|wx.ALL, 5 )
		
		self.ToEmailAddressesBox = wx.TextCtrl( self, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, 0|wx.SIMPLE_BORDER )
		self.ToEmailAddressesBox.SetToolTipString( u"Enter the email addresses reports will be sent to separated by commas.\n\nE.g., This_is_fun@gmail.com,somethingUnprofessional@yahoo.com,DontUse@bing.com" )
		
		RedditAndEmailSizer.Add( self.ToEmailAddressesBox, 0, wx.ALL, 5 )
		
		
		SizerToHoldSizers.Add( RedditAndEmailSizer, 1, wx.ALIGN_CENTER_HORIZONTAL|wx.TOP, 5 )
		
		UpdateRuntimeSizer = wx.BoxSizer( wx.VERTICAL )
		
		self.SettingsLabel = wx.StaticText( self, wx.ID_ANY, u"Settings", wx.DefaultPosition, wx.Size( -1,20 ), 0 )
		self.SettingsLabel.Wrap( -1 )
		self.SettingsLabel.SetFont( wx.Font( wx.NORMAL_FONT.GetPointSize(), 75, 90, 90, False, "Aharoni" ) )
		
		UpdateRuntimeSizer.Add( self.SettingsLabel, 0, wx.ALIGN_CENTER|wx.ALL, 5 )
		
		self.SubredditLabel = wx.StaticText( self, wx.ID_ANY, u"Subreddits", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.SubredditLabel.Wrap( -1 )
		UpdateRuntimeSizer.Add( self.SubredditLabel, 0, wx.ALIGN_CENTER|wx.ALL, 5 )
		
		self.SubredditBox = wx.TextCtrl( self, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, 0|wx.SIMPLE_BORDER )
		self.SubredditBox.SetToolTipString( u"Enter the subreddits you would like to track separated by commas. \n\nE.g., all,worldnews,news,android,technology,funny" )
		
		UpdateRuntimeSizer.Add( self.SubredditBox, 0, wx.ALL, 5 )
		
		self.WordLabel = wx.StaticText( self, wx.ID_ANY, u"Words", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.WordLabel.Wrap( -1 )
		UpdateRuntimeSizer.Add( self.WordLabel, 0, wx.ALIGN_CENTER|wx.ALL, 5 )
		
		self.WordBox = wx.TextCtrl( self, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, 0|wx.SIMPLE_BORDER )
		self.WordBox.SetToolTipString( u"Enter the words you would like to track separated by commas.\n\nE.g., israel,comcast,queen elizabeth,china,ameristralium" )
		
		UpdateRuntimeSizer.Add( self.WordBox, 0, wx.ALL, 5 )
		
		self.NumberOfPostsLabel = wx.StaticText( self, wx.ID_ANY, u"Number of posts", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.NumberOfPostsLabel.Wrap( -1 )
		UpdateRuntimeSizer.Add( self.NumberOfPostsLabel, 0, wx.ALIGN_CENTER|wx.ALL, 5 )
		
		self.NumberOfPostsBox = wx.TextCtrl( self, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, 0|wx.SIMPLE_BORDER )
		self.NumberOfPostsBox.SetToolTipString( u"Number of top posts to grab from each subreddit.\n\nAny number between 10-200. Might be able to try more." )
		
		UpdateRuntimeSizer.Add( self.NumberOfPostsBox, 0, wx.ALL, 5 )
		
		self.MinutesToWaitLabel = wx.StaticText( self, wx.ID_ANY, u"Minutes to wait", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.MinutesToWaitLabel.Wrap( -1 )
		UpdateRuntimeSizer.Add( self.MinutesToWaitLabel, 0, wx.ALIGN_CENTER|wx.ALL, 5 )
		
		self.MinutesToWaitBox = wx.TextCtrl( self, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, 0|wx.SIMPLE_BORDER )
		self.MinutesToWaitBox.SetToolTipString( u"Enter the minutes to wait between bot cycles" )
		
		UpdateRuntimeSizer.Add( self.MinutesToWaitBox, 0, wx.ALL, 5 )
		
		self.m_staticText13 = wx.StaticText( self, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.Size( -1,20 ), 0 )
		self.m_staticText13.Wrap( -1 )
		UpdateRuntimeSizer.Add( self.m_staticText13, 0, wx.ALL, 5 )
		
		self.update_settings_button = wx.Button( self, wx.ID_ANY, u"Update Settings", wx.DefaultPosition, wx.Size( 100,30 ), 0|wx.SIMPLE_BORDER )
		self.update_settings_button.SetDefault() 
		self.update_settings_button.SetMinSize( wx.Size( 100,30 ) )
		self.update_settings_button.SetMaxSize( wx.Size( 100,30 ) )
		
		UpdateRuntimeSizer.Add( self.update_settings_button, 0, wx.ALIGN_CENTER|wx.ALL, 5 )
		
		self.start_bot_button = wx.Button( self, wx.ID_ANY, u"Start Bot", wx.DefaultPosition, wx.Size( 100,30 ), wx.BU_EXACTFIT|wx.SIMPLE_BORDER )
		self.start_bot_button.SetMinSize( wx.Size( 100,30 ) )
		self.start_bot_button.SetMaxSize( wx.Size( 100,30 ) )
		
		UpdateRuntimeSizer.Add( self.start_bot_button, 0, wx.ALIGN_CENTER|wx.ALL, 5 )
		
		self.stop_bot_button = wx.Button( self, wx.ID_ANY, u"Stop Bot", wx.DefaultPosition, wx.Size( 100,30 ), wx.BU_EXACTFIT|wx.SIMPLE_BORDER )
		self.stop_bot_button.SetMinSize( wx.Size( 100,30 ) )
		self.stop_bot_button.SetMaxSize( wx.Size( 100,30 ) )
		
		UpdateRuntimeSizer.Add( self.stop_bot_button, 0, wx.ALIGN_CENTER|wx.ALL, 5 )
		
		
		SizerToHoldSizers.Add( UpdateRuntimeSizer, 1, wx.ALIGN_CENTER_HORIZONTAL|wx.TOP, 5 )
		
		
		Sizer1.Add( SizerToHoldSizers, 1, wx.EXPAND, 10 )
		
		
		self.SetSizer( Sizer1 )
		self.Layout()
		
		self.Centre( wx.BOTH )
		
		# Connect Events
		self.Bind( wx.EVT_MENU, self.m_QuitOptionOnMenuSelection, id = self.m_QuitOption.GetId() )
		self.Bind( wx.EVT_MENU, self.m_RunBotOptionOnMenuSelection, id = self.m_RunBotOption.GetId() )
		self.Bind( wx.EVT_MENU, self.m_AboutOptionOnMenuSelection, id = self.m_AboutOption.GetId() )
		self.Bind( wx.EVT_CLOSE, self.m_QuitOptionOnMenuSelection)
		self.update_settings_button.Bind( wx.EVT_BUTTON, self.update_settings_buttonOnButtonClick )
		self.start_bot_button.Bind( wx.EVT_BUTTON, self.start_bot_buttonOnButtonClick )
		self.stop_bot_button.Bind( wx.EVT_BUTTON, self.stop_bot_buttonOnButtonClick )
	
	def __del__( self ):
		pass
	
	
	# Virtual event handlers, overide them in your derived class
	def m_QuitOptionOnMenuSelection( self, event ):
		event.Skip()
	
	def m_RunBotOptionOnMenuSelection( self, event ):
		event.Skip()
	
	def m_AboutOptionOnMenuSelection( self, event ):
		event.Skip()
	
	def update_settings_buttonOnButtonClick( self, event ):
		event.Skip()
	
	def start_bot_buttonOnButtonClick( self, event ):
		event.Skip()
	
	def stop_bot_buttonOnButtonClick( self, event ):
		event.Skip()
	

