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
		data = bytearray()
		data.append(0x11)
		data.append(0x00)
		data.append(0x00)
		data.append(0x11)

		ser.write(data)
		receive = ser.readline(4)

		high = ord(receive[1])
		high = int(high)
		high = high << 8

		low = ord(receive[2])
		low = int(low)

		temperature = (high + low) / 10
		print temperature

	except Exception as e:
		print e
		pass

	time.sleep(0.2)
