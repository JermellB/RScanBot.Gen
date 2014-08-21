from kivy.app import App
from kivy.uix.button import Button
from kivy.uix.label import Label
from kivy.uix.boxlayout import BoxLayout
from kivy.properties import ObjectProperty
from kivy.uix.textinput import TextInput

class RedditUpdateBotV1App(App):


	def setOrientation(self, orient):
		self.orient = orient

	#Event Handlers Override in class
	def updateSettingsEventHandler(self, instance):
		print "updating settings"

	def startButtonEventHandler(self, instance):
		pass

	def stopButtonEventHandler(self, instance):
		pass

	def build(self):

		layout = BoxLayout(orientation="horizontal")
		layoutL = BoxLayout(padding = [20,10], orientation=self.orient, size_hint_x = 50)
		layoutR = BoxLayout(padding = [20,10], orientation=self.orient, size_hint_x = 50)

		#Right Settings and Fields
		self.redditCredentialsLabel = Label(text="Reddit Credentials")
		self.rUsernameLabel = Label(text="Username")
		self.rUsernameInput = TextInput()
		self.rPasswordLabel = Label(text="Password")
		self.rPasswordInput = TextInput(password=True)
		self.emailCredentialsLabel = Label(text="Email Credentials")
		self.eUsernameLabel = Label(text="Username")
		self.eUsernameInput = TextInput()
		self.ePasswordLabel = Label(text="Password")
		self.ePasswordInput = TextInput(password=True)
		self.eServerAddressLabel = Label(text="SMTP Server Address")
		self.eServerAddressInput = TextInput()
		self.eToEmailAddressLabel = Label(text="To Email Addresses")
		self.eToEmailAddressInput = TextInput()

		#Left Settings and Fields
		self.settingsLabel = Label(text="Settings")
		self.subredditLabel = Label(text="Subreddits")
		self.subredditInput = TextInput()
		self.wordsLabel = Label(text="Words to Track")
		self.wordsInput = TextInput()
		self.numberOfPostsLabel = Label(text="Number of posts to retrieve")
		self.numberOfPostsInput = TextInput()
		self.minutesToWaitLabel = Label(text="Minutes to wait between runs")
		self.minutesToWaitInput = TextInput()

		#Left Buttons
		self.updateButton = Button(text="Update Settings")
		self.startBotButton = Button(text="Start Bot")
		self.stopBotButton = Button(text="Stop Bot")

		#button Callbacks
		self.updateButton.bind(on_press=self.updateSettingsEventHandler) 
		self.startBotButton.bind(on_press=self.startButtonEventHandler)
		self.stopBotButton.bind(on_press=self.stopButtonEventHandler)

		#add left widgets to layout
		layoutL.add_widget(self.redditCredentialsLabel)
		layoutL.add_widget(self.rUsernameLabel)
		layoutL.add_widget(self.rUsernameInput)
		layoutL.add_widget(self.rPasswordLabel)
		layoutL.add_widget(self.rPasswordInput)
		layoutL.add_widget(self.emailCredentialsLabel)
		layoutL.add_widget(self.eUsernameLabel)
		layoutL.add_widget(self.eUsernameInput)
		layoutL.add_widget(self.ePasswordLabel)
		layoutL.add_widget(self.ePasswordInput)
		layoutL.add_widget(self.eServerAddressLabel)
		layoutL.add_widget(self.eServerAddressInput)
		layoutL.add_widget(self.eToEmailAddressLabel)
		layoutL.add_widget(self.eToEmailAddressInput)

		#add right widgets to layout
		layoutR.add_widget(self.settingsLabel)
		layoutR.add_widget(self.subredditLabel)
		layoutR.add_widget(self.subredditInput)
		layoutR.add_widget(self.wordsLabel)
		layoutR.add_widget(self.wordsInput)
		layoutR.add_widget(self.numberOfPostsLabel)
		layoutR.add_widget(self.numberOfPostsInput)
		layoutR.add_widget(self.minutesToWaitLabel)
		layoutR.add_widget(self.minutesToWaitInput)

		#add button widgets to layout
		layoutR.add_widget(self.updateButton)
		layoutR.add_widget(self.startBotButton)
		layoutR.add_widget(self.stopBotButton)

		#add boxlayouts to main container
		layout.add_widget(layoutL)
		layout.add_widget(layoutR)

		return layout

if __name__=="__main__":
	app = RedditUpdateBotV1App()
	app.setOrientation(orient="vertical")
	app.run()
