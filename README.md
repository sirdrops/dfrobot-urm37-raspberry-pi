# dfrobot-urm37-raspberry-pi
Reading values from dfrobot sensor urm37 v5 connected to raspberry pi with serial port. For python 2.7 and python 3.

Only requirement is to install pyserial. preferably with pip
```
sudo apt install python-pip python3-pip
pip install pyserial
pip3 install pyserial
```

You can change the time.sleep() for whatever delay you need.

During short testing the python3 code sometimes bugged out and had to be restarted. Still looking for the cause.

[Source arduino code and refference](https://wiki.dfrobot.com/URM37_V5.0_Ultrasonic_Sensor_SKU_SEN0001_)
