#ImportUsername's SMS Spammer GUI
import sys
import Tkinter as tk
from Tkinter import *
import ttk
import smtplib
from time import sleep as delay
import threading
from config import *


class SMSspammerMain:

    def __init__(self, root):
        self.root = root
        self.frame = Frame(self.root)
        self.frame.pack()
        
        self.carrierEntry = StringVar(self.frame)
        self.carrier = StringVar(self.frame)
        self.carriers = ["Verizon","AT&T","Sprint","T-mobile","Boost","Comcast","Tracfone","Virgin Mobile","Telus Mobile","US Cellular","Rogers Wireless","Qwest","Orange","O2","Nextel","Metro PCS","Edge Wireless","Bellsouth","Ameritech",\
                         "T-mobile AU",\
                         "Mtel","Globul",\
                         "Aliant","Bell mobility","Fido","MTS Mobility","Saskell Mobility","President's Choice",\
                         "T-Mobile DE","Vodafone DE","O2 DE","E-Plus",\
                         "OgVodafone","Siminn",\
                         "Meteor",\
                         "TIM",\
                         "AU by KDDI","NTT DoCoMo",\
                         "Orange NL","M1",\
                         "Vodacom ZA",\
                         "Telefonica Movistar","Vodafone ES"]
        self.carriersDict = {'Verizon':'@vtext.com','AT&T':'@text.att.net','Sprint':'@messaging.sprintpcs.com','T-mobile':'@tmomail.net','Boost':'@myboostmobile.com','Comcast':'@comcastpcs.textmsg.com','Tracfone':'@text.att.net','Virgin Mobile':'@sms.wcc.net','Telus Mobile':'@email.telus.com','US Cellular':'@email.uscc.net','Rogers Wireless':'@pcs.rogers.com','Qwest':'@qwestmp.com','Orange':'@mobile.celloneusa.com','O2':'mobile.celloneusa.com','Nextel':'@messaging.nextel.com','Metro PCS':'@mymetropcs.com','Edge Wireless':'@sms.edgewireless.com','Bellsouth':'@bellsouth.cl','Ameritech':'@paging.acswireless.com',\
                             'T-mobile AU':'@optusmobile.com.au',\
                             'MteL':'@sms.mtel.net','Globul':'@sms.globul.bg',\
                             'Aliant':'@wirefree.inf5orme.ca','Bell Mobility':'@text.bellmobility.ca','Fido':'@fido.ca','MTS Mobility':'@text.mtsmobility.com','Saskell Mobility':'@pcs.sasktelmobility.com','President\'s Choice':'@mobiletext.ca',\
                             'T-Mobile DE':'@t-dt-sms.de','Vodafone DE':'@vodafone-sms.de','O2 DE':'@o2online.de','E-Plus':'@smsmail.eplus.de',\
                             'OgVodafone':'@sms.is','Siminn':'@box.is',\
                             'Meteor':'@sms.mymeteor.ie',\
                             'TIM':'@timnet.com',\
                             'AU by KDDI':'@ezweb.ne.jp','NTT DoCoMo':'@docomo.ne.jp',\
                             'Orange NL':'@sms.orange.nl',\
                             'M1':'@m1.com.sg',\
                             'Vodacom ZA':'@voda.co.za',\
                             'Telefonica Movistar':'@movistar.net','Vodafone ES':'@vodafone.es',\
                             }
        self.message = ""
        self.times = 0
        self.delay = 0

        self.configF = Config()
        self.defaultmsg = self.configF.Default_spam_message
        self.targetGet()
        self.messageGet()
        self.send()

    def targetGet(self):
        targetFrame = LabelFrame(self.frame,text="Target Information",padx=5,pady=15)
        targetFrame.grid(sticky=E+W)

        toL = Label(self.frame,text="Target Phone Number: ").grid(in_=targetFrame)
        self.targetEntry = Entry(self.frame)
        self.targetEntry.grid(in_=targetFrame,row=0,column=1,sticky=W)

        self.carrierEntry.set("carrier")
        self.carrier.set("carrier")
        self.carrierPick = apply(OptionMenu, (self.frame, self.carrierEntry) + tuple(self.carriers))
        self.carrierPick.grid(in_=targetFrame,row=0,column=4,sticky=W)

        Label(self.frame, text="   ").grid(in_=targetFrame, row=0, column=5)
        Label(self.frame, text="   ").grid(in_=targetFrame, row=0, column=2)

        
    def messageGet(self):
        messageFrame = LabelFrame(self.frame, text="Message", padx=5, pady=15)
        messageFrame.grid(sticky=E+W)

        self.messageEntry = Text(self.frame,width=60,height=5)
        self.messageEntry.grid(in_=messageFrame)
        self.messageEntry.insert('1.0',self.defaultmsg)

    def send(self):
        sendFrame = LabelFrame(self.frame, text="Additional Information", padx=5, pady=15)
        sendFrame.grid(sticky=E+W)

        amountL = Label(self.frame, text="Number of Messages to Send: ").grid(in_=sendFrame, row=0, column=1, sticky=W)
        self.amountEntry = Entry(self.frame, width=4)
        self.amountEntry.grid(in_=sendFrame, row=0, column=2, sticky=W)

        delayL = Label(self.frame, text="Delay Between Messages: ").grid(in_=sendFrame, row=1, column=1, sticky=W)
        self.delayEntry = Entry(self.frame, width=4)
        self.delayEntry.grid(in_=sendFrame, row=1, column=2, sticky=W)

        self.delayEntry.grid(in_=sendFrame, row=1, column=2, sticky=W)
        Label(self.frame, text="   ").grid(in_=sendFrame, row=0, column=0)
        Label(self.frame, text="   ").grid(in_=sendFrame, row=1, column=0)
        Label(self.frame, text="                              ").grid(in_=sendFrame, row=1, column=7)
        sendB = Button(self.frame, command=self.begin, text="Begin").grid(in_=sendFrame, row=1, column=8, sticky=W+E+N+S)

    def begin(self):
        self.times = int(self.amountEntry.get())
        self.target = self.targetEntry.get()
        self.carrier = self.carrierEntry.get()
        self.message = self.messageEntry.get('1.0','end')
        self.delay = int(self.delayEntry.get())

        self.target = self.target+self.carriersDict[self.carrier]

        self.Runroot = Tk()
        self.Runroot.geometry("350x100+400+150")
        run = SMSspammerRun(root=self.Runroot,total=self.times,mesg=self.message,target=self.target,delay=self.delay,config=self.configF)
        self.Runroot.title("Spammer Running")
        self.Runroot.mainloop()


class GUI:

    def __init__(self,root,total):
        self.ProgBar = ttk.Progressbar(root, orient="horizontal", length=300, mode="determinate")
        self.ProgBar.grid(padx=20, pady=20)
        self.total = total

    def stepIt(self):
        self.ProgBar.step(100/self.total)


class SMSspammerRun:
    
    def __init__(self, root,total,mesg,target,delay,config):
        self.total = total
        self.root = root
        self.running = True
        self.target = target
        self.mesg = mesg
        self.rem = self.total
        self.delay = delay

        self.gui = GUI(root,self.total)

        self.Google_server = config.Google_server

        threading.Thread(target=self.workerThread).start()
        threading.Thread(target=self.totalUpdate).start()

    def workerThread(self):
        for x in range(self.total):
            delay(self.delay)
            self.rem = self.total-x-1
            self.Google_server.sendmail(" ",self.target,self.mesg)
            self.gui.stepIt()
        self.running = False

    def totalUpdate(self):
        curRem = self.rem
        while True:
            if curRem != self.rem or self.rem == self.total:
                curRem = self.rem
                if self.rem != 0:
                    delay(0.5)
                    w = Label(self.root,text=str(self.total-self.rem)+" out of "+str(self.total)+" sent")
                else:
                    w = Label(self.root,text="process completed")
                    w.place(x=116,y=45)
                    break
                w.place(x=116,y=45)
            delay(self.delay/4)


if __name__ == "__main__":
    root = Tk()
    root.geometry("500x350+350+100")
    SMSspammerMain(root=root)
    root.title("ImportUsername's SMSspammer")
    root.mainloop()
