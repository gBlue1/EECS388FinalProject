import serial
ser1=serial.Serial('/dev/ttyAMA1', 115200)
while(1):
speed = input("Enter Speed: ")
angle = input("Enter Angle: ")
speed = str(speed)
angle = str(angle)
ser1.write(bytes("speed: " + speed + "\n"))
ser1.write(bytes("angle: " + angle))

ser1.close()
