Setup
======
You will need a throwaway/spam gmail account to send the text messages from. It is HIGHLY recommended that you don’t use your real email, as the email address will appear as part of the text message. I suggest you make the account address relevant to whatever you will be using the spammer for (ex: freeservice@gmail.com, troll@gmail.com, etc.)

Once you have created an account, open the config.py file. Put the account information in the marked places. You have nothing to worry about with your password - it is a local variable to the class and can’t be called from other files, it is just used in the config file to connect to the google API. If you want you can read the source for the spammer in the main file to see that it doesn’t read your password or send it anywhere. In the config file you can also set a default message. This will appear in the message box when you open up the spammer GUI. If you have a message that you use often, you don’t have to re-type it every time you want to use it, just add it in the config file.

Running
=======
To run the spammer you will need to have Python 2.x installed with tkinter. When it starts up you will see a window asking for the target cell phone number, the cell phone carrier, the message, the number to send, and the delay. You can look up the carrier of a cell phone at www.carrierlookup.com if you don’t already know it. The delay should be set to 2 or above, but put a lower number at your own discretion. The other input fields should be self explanatory. Hit send and that’s it! Watch the progress bar as you spam your helpless target! Feel free to run multiple at once, or to run it again once it has finished. There is no need to restart the whole program.

- Note: This program is for educational purposes only and I do not take responsibility for what you do with it.
