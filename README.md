# RPi_Memristor
Raspberry Pi software to output voltages for use in testing a memristor. This voltage is output through the ADCDACPi hardware from abElectronics.com, and requires the use of any commercially available differential amplifier or subtractor circuit.

##Dependencies
This software is for use with the ADCDACPi Raspberry Pi expansion board from http://www.abelectronics.co.uk. It uses the AB Electronics UK ADCDAC Pi Python Library, which can be downloaded free of charge from https://github.com/abelectronicsuk/ABElectronics_Python_Libraries/tree/master/ADCDACPi. See the associated README and license for details on installation, use, and permissions for the AB Electronics UK ADCDAC Pi Python Library.

Before beginning, install the AB Electronics UK ADCDAC Pi Python Library according the the Install directions in their README file.

##Install
To download this software, connect your Raspberry Pi to the Internet and type in the command line
```
git clone https://github.com/jhart12/RPi_Memristor.git
```

Then add the location where you downloaded the library to the PYTHONPATH. For example, if you downloaded the library to the desktop, type in the command line
```
export PYTHONPATH=${PYTHONPATH}:~/Desktop/jhart12/RPi_Memristor/
```
Then to use any of the functions, simply import the RPi_Memristor library:

```
import RPi_memristor
RPi_memristor.simpletriangle(2) #see below for functions
```

##Functions:
```
simpletriangle(period)
```
Makes voltage signal with period T=period for measuring 
the pinched hysteresis curve of a memristor.
Each period consists of three positive voltage triangles of 
period t=T/6 each followed by three negative voltage triangles of
period t=T/6 each.
The wave will repeat until the user hits ENTER on the keyboard.

######EXPERIMENTAL SETUP:
Since the ADCDACPi can only output positive voltages, ADC1 outputs
a positive triangle voltage while ADC2 outputs 0, then ADC2 outputs a 
positive triangle voltage while ADC1 outputs 0. These two signals are
subtracted using a differential amplifier, which creates the desired
bipolar triangle wave. 

```
complextriangle(period)
```
Makes complex triangle wave with period T=period
for measuring how the resistance changes as a function
of the largest current to pass through the memristor.
 
Each period consists of series of three voltage triangles
of different amplitudes and polarities. The amplitudes are
(in order) positive small, medium, large, medium, small;
then negative small, medium, large, medium, small. The wave
then repeats indefinitely until the user hits ENTER on the keyboard.

######EXPERIMENTAL SETUP:
Since the ADCDACPi can only output positive voltages, ADC1 outputs
a positive voltage while ADC2 outputs 0, then ADC2 outputs a 
positive voltage while ADC1 outputs 0. These two signals are
subtracted using a differential amplifier, which creates the desired
bipolar triangle wave. 
