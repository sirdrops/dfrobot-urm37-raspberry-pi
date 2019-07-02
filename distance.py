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
	try:
		data = b'\x22\x00\x00\x22'
		ser.write(data)
		data = ser.readline(4)
		distvalue = data[1] << 8
		distvalue = int(distvalue) + int(data[2])
		print(distvalue)
	except Exception as e:
		print(e)
		pass
	time.sleep(0.2)
