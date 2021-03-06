from Phidget22.PhidgetException import *
from Phidget22.Phidget import *
from Phidget22.Devices.Log import *
from Phidget22.LogLevel import *
from Phidget22.Devices.VoltageRatioInput import *
import matplotlib.pyplot as plt
import matplotlib.animation as animation
import pandas as pd
import seaborn as sns
import csv
import traceback
import time

def onVoltageRatioInput0_VoltageRatioChange(self, voltageRatio):
	#print("VoltageRatio [0]: " + str(voltageRatio))
	if voltageRatio != v[0]:
		v2[0] = "{:.0f}".format(round(voltageRatio * 100000000))
		v[0] = "{:.0f}".format(round(voltageRatio * 100000000))

def onVoltageRatioInput0_Attach(self):
	print("Attach [0]!")

def onVoltageRatioInput0_Detach(self):
	print("Detach [0]!")

def onVoltageRatioInput0_Error(self, code, description):
	print("Code [0]: " + ErrorEventCode.getName(code))
	print("Description [0]: " + str(description))
	print("----------")

def onVoltageRatioInput1_VoltageRatioChange(self, voltageRatio):
	#print("VoltageRatio [1]: " + str(voltageRatio))
	if voltageRatio != v[1]:
		v2[1] = "{:.0f}".format(round(voltageRatio * 100000000))
		v[1] = "{:.0f}".format(round(voltageRatio * 100000000))

def onVoltageRatioInput1_Attach(self):
	print("Attach [1]!")

def onVoltageRatioInput1_Detach(self):
	print("Detach [1]!")

def onVoltageRatioInput1_Error(self, code, description):
	print("Code [1]: " + ErrorEventCode.getName(code))
	print("Description [1]: " + str(description))
	print("----------")

def onVoltageRatioInput2_VoltageRatioChange(self, voltageRatio):
	#print("VoltageRatio [2]: " + str(voltageRatio))
	if voltageRatio != v[2]:
		v2[2] = "{:.0f}".format(round(voltageRatio * 100000000))
		v[2] = "{:.0f}".format(round(voltageRatio * 100000000))

def onVoltageRatioInput2_Attach(self):
	print("Attach [2]!")

def onVoltageRatioInput2_Detach(self):
	print("Detach [2]!")

def onVoltageRatioInput2_Error(self, code, description):
	print("Code [2]: " + ErrorEventCode.getName(code))
	print("Description [2]: " + str(description))
	print("----------")

def onVoltageRatioInput3_VoltageRatioChange(self, voltageRatio):
	try:
		#print("VoltageRatio [3]: " + str(voltageRatio))
		prev = 0
		if voltageRatio != v[3]:
			v[3] = "{:.0f}".format(round((voltageRatio) * 100000000))
			v2[3] = "{:.0f}".format(round((voltageRatio) * 100000000))
		prev = f2.tell()
		print(v2)
		f2.write(str(v[0]) + ' ')
		f2.write(str(v[1]) + ' ')
		f2.write(str(v[2]) + ' ')
		f2.write(str(v[3]) + '\r\n')
		f2.seek(prev)
		d = f2.readline()
		d = d.split(' ')
		f2.seek(prev)
		d[3] = d[3][:-1]
		d[3] = d[3][:-1]
		v[0] = round((float(v[0])) / 240) + 6
		v[1] = round((float(v[1])) / 240) + 1
		v[2] = round((float(v[2])) / 240) - 1
		v[3] = round((float(v[3])) / 240) + 5
		v2[0] = round((float(v2[0])) + -4.264) / 72.9
		v2[1] = round((float(v2[1])) + -26.4) / 63.02
		v2[2] = round((float(v2[2])) + 378) / 67.1
		v2[3] = round((float(v2[3])) + -1141) / 52.4
		writer.writerow('my')
		writer.writerow(v)
		writer.writerow('their')
		writer.writerow(v2)
	except:
		pass
	
	

def onVoltageRatioInput3_Attach(self):
	print("Attach [3]!")

def onVoltageRatioInput3_Detach(self):
	print("Detach [3]!")

def onVoltageRatioInput3_Error(self, code, description):
	print("Code [3]: " + ErrorEventCode.getName(code))
	print("Description [3]: " + str(description))
	print("----------")
#Declare any event handlers here. These will be called every time the associated event occurs.


def main():
	try:
		Log.enable(LogLevel.PHIDGET_LOG_INFO, "phidgetlog.log")
		#Create your Phidget channels
		voltageRatioInput0 = VoltageRatioInput()
		voltageRatioInput1 = VoltageRatioInput()
		voltageRatioInput2 = VoltageRatioInput()
		voltageRatioInput3 = VoltageRatioInput()
	
		#Set addressing parameters to specify which channel to open (if any)
		voltageRatioInput0.setChannel(0)
		voltageRatioInput1.setChannel(1)
		voltageRatioInput2.setChannel(2)
		voltageRatioInput3.setChannel(3)

		#Assign any event handlers you need before calling open so that no events are missed.
		voltageRatioInput0.setOnVoltageRatioChangeHandler(onVoltageRatioInput0_VoltageRatioChange)
		voltageRatioInput0.setOnAttachHandler(onVoltageRatioInput0_Attach)
		voltageRatioInput0.setOnDetachHandler(onVoltageRatioInput0_Detach)
		voltageRatioInput0.setOnErrorHandler(onVoltageRatioInput0_Error)
		voltageRatioInput1.setOnVoltageRatioChangeHandler(onVoltageRatioInput1_VoltageRatioChange)
		voltageRatioInput1.setOnAttachHandler(onVoltageRatioInput1_Attach)
		voltageRatioInput1.setOnDetachHandler(onVoltageRatioInput1_Detach)
		voltageRatioInput1.setOnErrorHandler(onVoltageRatioInput1_Error)
		voltageRatioInput2.setOnVoltageRatioChangeHandler(onVoltageRatioInput2_VoltageRatioChange)
		voltageRatioInput2.setOnAttachHandler(onVoltageRatioInput2_Attach)
		voltageRatioInput2.setOnDetachHandler(onVoltageRatioInput2_Detach)
		voltageRatioInput2.setOnErrorHandler(onVoltageRatioInput2_Error)
		voltageRatioInput3.setOnVoltageRatioChangeHandler(onVoltageRatioInput3_VoltageRatioChange)
		voltageRatioInput3.setOnAttachHandler(onVoltageRatioInput3_Attach)
		voltageRatioInput3.setOnDetachHandler(onVoltageRatioInput3_Detach)
		voltageRatioInput3.setOnErrorHandler(onVoltageRatioInput3_Error)

		#Open your Phidgets and wait for attachment
		voltageRatioInput0.openWaitForAttachment(5000)
		voltageRatioInput1.openWaitForAttachment(5000)
		voltageRatioInput2.openWaitForAttachment(5000)
		voltageRatioInput3.openWaitForAttachment(5000)

		#Do stuff with your Phidgets here or in your event handlers.
#################################################################

##################################################################
		try:
			input("Press Enter to Stop\n")
		except (Exception, KeyboardInterrupt):
			f.close()
			f2.close()
			pass

		#Close your Phidgets once the program is done.
		voltageRatioInput0.close()
		voltageRatioInput1.close()
		voltageRatioInput2.close()
		voltageRatioInput3.close()

	except PhidgetException as ex:
		#We will catch Phidget Exceptions here, and print the error informaiton.
		traceback.print_exc()
		print("")
		print("PhidgetException " + str(ex.code) + " (" + ex.description + "): " + ex.details)

v = [0, 0, 0, 0]
v2 = [0,0,0,0]
d = ''
fig = plt.figure()
ax1 = fig.add_subplot(1,1,1)
fileName2 = 'data.txt'
f2 = open(fileName2, 'r+') 
header = ['Channel 0','Channel 1' , 'Channel 2', 'Channel 3']
fileName = 'data.csv'
with open(fileName, 'r+', newline = '', encoding = 'UTF-8') as f:
	writer = csv.writer(f)
	writer.writerow(header)
	main()