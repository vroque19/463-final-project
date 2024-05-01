import csv
import pyfirmata
import serial
import time

#Arduino setup (doesnt work after 3.11)
board = pyfirmata.Arduino('COM6')


#finding value in csv file
with open('C:\\Users\\austi\\Downloads\\example.csv','r') as file:
  csv_reader = csv.reader(file)

  for row in csv_reader:
    if row[0] == '121':
        print('Found 121')

#Arduino loop to blink LED
while True:
   board.digitl[7].write(1)
   time.sleep(1)
   board.digital[7].write(0)
   time.sleep(1)
