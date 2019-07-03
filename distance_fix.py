import serial
import time

ser = serial.Serial(
	port='/dev/ttyS0',
	baudrate=9600,
	parity=serial.PARITY_NONE,
	stopbits=serial.STOPBITS_ONE,
	bytesize=serial.EIGHTBITS
)

def read_dist(bit1,bit2):
	try:
		data = b'\x22\x00\x00\x22'
		ser.write(data)
		data = ser.readline(4)
		print(data[0],data[1],data[2],data[3])
		distvalue = data[bit1] << 8
		distvalue = int(distvalue) + int(data[bit2])
		print(distvalue)
	except Exception as e:
		print(e)
		print("error, bit move one right all")
		ser.close()
		ser.open()


while True:
	time.sleep(0.2)

	read_dist(1,2)

