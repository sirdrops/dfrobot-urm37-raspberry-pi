import serial
import time

ser = serial.Serial(
	port='/dev/ttyS0',
	baudrate=9600,
	parity=serial.PARITY_NONE,
	stopbits=serial.STOPBITS_ONE,
	bytesize=serial.EIGHTBITS
)

while True:
	data = b'\x11\x00\x00\x11'
	ser.write(data)
	data = ser.readline(4)
	tempvalue = data[1] << 8
	tempvalue = int(tempvalue) + int(data[2])
	tempvalue = tempvalue / 10
	print(tempvalue)
	time.sleep(0.2)
