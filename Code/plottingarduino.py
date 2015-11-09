#import serial
#import numpy as np
#from matplotlib import pyplot as plt


import matplotlib
matplotlib.use('TKAgg')
import numpy as np
import matplotlib.pyplot as plt
import matplotlib.animation as animation
import serial

#ser = serial.Serial('/dev/cu.usbmodem1411', 115200)
#
#plt.ion() # set plot to animated
#
#ydata = [0] * 50
#ax1=plt.axes()
#
## make plot
#line, = plt.plot(ydata)
#plt.ylim([1,400])
#
## start data collection
#while True:
#    plt.ion() # set plot to animated
#
#    ydata = [0] * 50
#    ax1=plt.axes()
#
## make plot
#    line, = plt.plot(ydata)
#    plt.ylim([1,400])
#
#    data = ser.readline().rstrip() # read data from serial
#
#    print data
#
#    ymin = float(min(ydata))-100
#    ymax = float(max(ydata))+100
#    plt.ylim([ymin,ymax])
#    ydata.append(data)
#    del ydata[0]
#    line.set_xdata(np.arange(len(ydata)))
#    line.set_ydata(ydata)  # update the data
#    plt.draw() # update the plot
#    plt.show()

# import matplotlib.pyplot as plt
# import matplotlib.animation as animation
# import time
#
# fig = plt.figure()
# ax1 = fig.add_subplot(1,1,1)
#
# def animate(i):
#     pullData = open("sampleText.txt","r").read()
#     dataArray = pullData.split('\n')
#     xar = []
#     yar = []
#     for eachLine in dataArray:
#         if len(eachLine)>1:
#             x,y = eachLine.split(',')
#             xar.append(int(x))
#             yar.append(int(y))
#     ax1.clear()
#     ax1.plot(xar,yar)
# ani = animation.FuncAnimation(fig, animate, interval=1000)
# plt.show()
#
fig, ax = plt.subplots()
line, = ax.plot(np.random.rand(10))
ax.set_ylim(0, 1000)
ax.set_xlim(0,1000)
xdata, ydata = [0]*100, [0]*100
raw = serial.Serial("/dev/cu.usbmodem1411",57600)
# raw.open()

def update(data):
    line.set_ydata(data)
    return line,

def run(data):
    t,y = data
    del xdata[0]
    del ydata[0]
    xdata.append(t)
    ydata.append(y)
    line.set_data(xdata, ydata)
    return line,

def data_gen():
    t = 0
    while True:
        t+=1
        try:
            dat = int(raw.readline())
        except:
            dat = 0
        yield t, dat

ani = animation.FuncAnimation(fig, run, data_gen, interval=100, blit=True)
plt.show()


     #
#
# import sys, serial, argparse
# import numpy as np
# from time import sleep
# from collections import deque
#
# import matplotlib.pyplot as plt
# import matplotlib.animation as animation
#
#
# # plot class
# class AnalogPlot:
#   # constr
#   def __init__(self, strPort, maxLen):
#       # open serial port
#       self.ser = serial.Serial(strPort, 9600)
#
#       self.ax = deque([0.0]*maxLen)
#       self.ay = deque([0.0]*maxLen)
#       self.maxLen = maxLen
#
#   # add to buffer
#   def addToBuf(self, buf, val):
#       if len(buf) < self.maxLen:
#           buf.append(val)
#       else:
#           buf.pop()
#           buf.appendleft(val)
#
#   # add data
#   def add(self, data):
#       assert(len(data) == 2)
#       self.addToBuf(self.ax, data[0])
#       self.addToBuf(self.ay, data[1])
#
#   # update plot
#   def update(self, frameNum, a0, a1):
#       try:
#           line = self.ser.readline()
#           data = [float(val) for val in line.split()]
#           # print data
#           if(len(data) == 2):
#               self.add(data)
#               a0.set_data(range(self.maxLen), self.ax)
#               a1.set_data(range(self.maxLen), self.ay)
#       except KeyboardInterrupt:
#           print('exiting')
#
#       return a0,
#
#   # clean up
#   def close(self):
#       # close serial
#       self.ser.flush()
#       self.ser.close()
#
# # main() function
# def main():
#   # create parser
#   parser = argparse.ArgumentParser(description="LDR serial")
#   # add expected arguments
#   parser.add_argument('--port', dest='port', required=True)
#
#   # parse args
#   args = parser.parse_args()
#
#   #strPort = '/dev/tty.usbserial-A7006Yqh'
#   strPort = args.port
#
#   print('reading from serial port %s...' % strPort)
#
#   # plot parameters
#   analogPlot = AnalogPlot(strPort, 100)
#
#   print('plotting data...')
#
#   # set up animation
#   fig = plt.figure()
#   ax = plt.axes(xlim=(0, 100), ylim=(0, 1023))
#   a0, = ax.plot([], [])
#   a1, = ax.plot([], [])
#   anim = animation.FuncAnimation(fig, analogPlot.update,
#                                  fargs=(a0, a1),
#                                  interval=50)
#
#   # show plot
#   plt.show()
#
#   # clean up
#   analogPlot.close()
#
#   print('exiting.')
#
#
# # call main
# if __name__ == '__main__':
#   main()
