from tkinter import *
from tkinter.ttk import *
import requests
import json

class Weather:
    def __init__(self):
        self.root = Tk()
        self.root.title("Weather app")
        self.root.geometry('400x120')
        # self.apiKey = "https://www.airnowapi.org/aq/observation/zipCode/current/?format=application/json&zipCode=89129&distance=5&API_KEY=A580AE09-EE82-46B7-A44A-1158D8D7F92C"
        # self.api_req = requests.get("https://www.airnowapi.org/aq/observation/zipCode/current/?format=application/json&zipCode=89129&distance=5&API_KEY=A580AE09-EE82-46B7-A44A-1158D8D7F92C")
        # self.user = StringVar()
        self.zipCode = Entry(self.root)
        self.zipCode.pack()
        self.items = ["zipCode", "State", "City"]
        self.tryMe = Combobox(self.root, values=self.items)
        self.tryMe.current(0)
        self.tryMe.pack()
        self.zipButton = Button(self.root, text="Look up {}".format(self.tryMe.get()), command=self.check)
        self.zipButton.pack()
        self.label = Label(self.root)
        self.root.mainloop()

    def check(self):
        self.label.destroy()
        try:
            self.api_req = requests.get("https://www.airnowapi.org/aq/observation/zipCode/current/?format=application/json&" + self.tryMe.get() + "="+ self.zipCode.get() +"&distance=5&API_KEY=A580AE09-EE82-46B7-A44A-1158D8D7F92C")
            self.api = json.loads(self.api_req.content)
            # print(self.api)
            self.city = self.api[0]['ReportingArea']
            self.quality = self.api[0]['AQI']
            self.category = self.api[0]['Category']['Name']
            
            if self.category == "Good":
                self.state = 'Green'
            elif self.category == "Moderate":
                self.state = "Yellow"
            elif self.category == "Unhealthy for Sensitive Groups":
                self.state = "Orange"
            elif self.category == "Very Unhealthy":
                self.state = "Purple"
            elif self.category == "Unhealthy":
                self.state = "Red"
            elif self.category == "Hazardous":
                self.state = "Maroon"

            self.label = Label(self.root, text=self.city + " Air Quality: " + str(self.quality) + " " + str(self.category), font=('Helvetica', 20), background=self.state)
            self.label.pack()
        except:
            self.label = Label(self.root, text="Ooops, We do not have any information about this {}".format(self.tryMe.get()))
            self.label.pack()
Weather()