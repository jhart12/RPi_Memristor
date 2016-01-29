#!/usr/bin/python

'''
Created on Mon Jun 22 14:26:11 2015

@author: Joe Hart
jhart12@umd.edu

'''

"""
simpletriangle(period)
Makes voltage signal with period T=period for measuring 
the pinched hysteresis curve of a memristor.
Each period consists of three positive voltage triangles of 
period t=T/6 each followed by three negative voltage triangles of
period t=T/6 each.
The wave will repeat until the user hits ENTER on the keyboard.
EXPERIMENTAL SETUP:
Since the ADCDACPi can only output positive voltages, ADC1 outputs
a positive triangle voltage while ADC2 outputs 0, then ADC2 outputs a 
positive triangle voltage while ADC1 outputs 0. These two signals are
subtracted using a differential amplifier, which creates the desired
bipolar triangle wave. 

"""
import numpy as np
import time, sys, select
#this library must be downloaded from
# https://github.com/abelectronicsuk/ABElectronics_Python_Libraries/blob/master/ADCDACPi/ABE_ADCDACPi.py
from ABE_ADCDACPi import ADCDACPi

def simpletriangle(period):
	period=period * 2

	#simple triangle wave
	def f(t,period,slope):
	    t=t%(period/3)
	    if t<=period/6:
		output = slope * t
	    else:
		output = 1 - slope * (t-period/6)
	    return output

	t0=time.time()
	t=0
	out=0
	n=0
	i=0
	period=.5*period
	slope2 = 1.0/(period/6)

	#initialize DAC
	dac=ADCDACPi()
	#infinite loop
	print "Press ENTER to quit.\n"
	while(True):
	    #exit when user presses enter
	 if sys.stdin in select.select([sys.stdin],[],[],0)[0]:
	     line = raw_input()
	     break
	 #get time
	 t=time.time()-t0
	 #make signal bipolar
	 if ((t//period)%2)==1:
	     out=f(t,period,slope2)
	     dac.set_dac_voltage(1,.55*out)
	 else:
	     out=f(t,period,slope2)
	     dac.set_dac_voltage(2,.55*out)

"""
complextriangle(period)
 Makes complex triangle wave with period T=period
 for measuring how the resistance changes as a function
 of the largest current to pass through the memristor.
 
 Each period consists of series of three voltage triangles
 of different amplitudes and polarities. The amplitudes are
 (in order) positive small, medium, large, medium, small;
 then negative small, medium, large, medium, small. The wave
 then repeats indefinitely until the user hits ENTER on the keyboard.

EXPERIMENTAL SETUP:
Since the ADCDACPi can only output positive voltages, ADC1 outputs
a positive voltage while ADC2 outputs 0, then ADC2 outputs a 
positive voltage while ADC1 outputs 0. These two signals are
subtracted using a differential amplifier, which creates the desired
bipolar triangle wave. 
"""

def complextriangle(period):

	period = period * 2

	#complex triangle wave
	def f1(t,period,slope):
	    t=t%period
	    if (t<=period/5 or t>=4*period/5):
		t=t%(period/15)
		if (t<=period/30):
		    output = slope * t
		else:
		    output = 1.0/3 - slope * (t-period/30)
	    elif (t<=2*period/5 or t>=3*period/5):
		t=t%(period/15)
		if(t<=period/30):
		    output = 2 * slope * t
		else:
		    output = (2.0/3) - 2* slope * (t-period/30)
	    else:
		t=t%(period/15)
		if(t<=period/30):
		    output = 3 * slope * t
		else:
		    output = 1 - 3 * slope * (t-period/30)
	    
	    return output


	t0=time.time()
	t=0
	out=0
	n=0
	i=0
	period=.5*period
	slope1 = (1.0/3)/(period/30) #calculated from the period

	#initialize DAC
	dac=ADCDACPi()
	#infinite loop
	print "Press ENTER to quit.\n"
	while(True):
	    #exit when user presses enter
	 if sys.stdin in select.select([sys.stdin],[],[],0)[0]:
	     line = raw_input()
	     break
	 #get time
	 t=time.time()-t0
	 #make signal bipolar
	 if ((t//period)%2)==1:
	     out=f1(t,period,slope1)
	     dac.set_dac_voltage(1,.55*out)
	 else:
     	     out=f1(t,period,slope1)
     	     dac.set_dac_voltage(2,.55*out)
