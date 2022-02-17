import serial


ser = serial.Serial("COM4", 9600)
while True:
    input_value = input('Enter 1-4: ')
    ser.write(input_value.encode())