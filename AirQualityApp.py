# Created by: MHagarGIS
# For: GEOG470
# 3/13/2021
# This code was developed by following a tutorial and thus nearly all the code was developed
# by John Elder from Codemy.com on the YouTube channel Codemy.com in the playlist "Python GUI's With TKinter.
# This application is a simple air quality checker that provides an example of connecting
# to an API with tkinter from https://www.airnow.gov/

# Import everything from tkinter
# You'll still have to import individual modules sometimes. 
from tkinter import *
# PIL = Python Image Library but it uses Pillow.
from PIL import ImageTk, Image
# Need to import filedialog from tkinter
from tkinter import filedialog
# Need to import requests. It does not come with Python.
# Must be installed with pip from cmd line.
import requests
# Need to import json
import json

# This happens before doing anything else with tkinter.
root = Tk()
root.title("Air Quality Application")
root.iconbitmap("C:/Users/HagarMichael/Pictures/Saved Pictures/Mugshot.ico")
# Set the geometry of the root widget window.
root.geometry("600x100")


def clear():
		root.configure(background=weather_color)
		myLabel.destroy()                                                                                    

# Create Zipcode lookup function.
def zipLookup():
	global myLabel
	global weather_color
	#zip.get()
	# Create a zipLabel for testing purposes and pack to the root widget.
	# zipLabel = Label(root, text=zip.get())
	# zipLabel.grid(row=1, column=0, columspan=2)
	try:
		# API query url https://www.airnowapi.org/aq/observation/zipCode/current/?format=application/json&zipCode=99004&distance=5&API_KEY=DB14DE66-F360-4F60-8B06-38DAE0E51906
		api_request = requests.get("https://www.airnowapi.org/aq/observation/zipCode/current/?format=application/json&zipCode=" + zip.get() + "&distance=5&API_KEY=DB14DE66-F360-4F60-8B06-38DAE0E51906")
		# Create a new variable and set equal to the return content from the previous request.
		api = json.loads(api_request.content)
		city = api[0]["ReportingArea"]
		quality = api[0]["AQI"]
		category = api[0]["Category"]["Name"]

		if category == "Good":
			weather_color = "#0C0"
		elif category == "Moderate":
			weather_color = "#FFFF00"
		elif category == "Unhealthy for Sensitive Groups":
			weather_color = "#ff9900"
		elif category == "Unhealthy":
			weather_color = "#FF0000"
		elif category == "Very Unhealthy":
			weather_color = "#990066"
		elif category == "Hazardous":
			weather_color = "#660000"
		# Set the background color or root widget to green.
		root.configure(background=weather_color)
		# Put the label in the try so it doesn't error twice is there's an issue.
		myLabel = Label(root, text=city + " " + "Air Quality: " + str(quality) + " - " + category, font=("Helvetica",20), background=weather_color)
		myLabel.grid(row=1, column=0, columnspan=2)

	# If something goes wrong throw and error with an output.
	except Exception as e:
		api = "Error..."



zip = Entry(root)
zip.grid(row=0, column=0, stick=W+E+N+S)

zipButton = Button(root, text="Enter Zipcode", command=zipLookup)
zipButton.grid(row=0, column=1, stick=W+E+N+S)

clrButton = Button(root, text="Clear", command=clear)
clrButton.grid(row=0, column=2, stick=W+E+N+S)

root.mainloop()
