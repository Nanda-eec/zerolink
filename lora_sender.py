import serial
import time

# Configure the serial port for LoRa module
lora = serial.Serial('/dev/ttyS0', baudrate=9600, timeout=1)

def send_message(message):
    try:
        lora.write(message.encode('utf-8'))
        print(f"Message sent: {message}")
    except Exception as e:
        print(f"Error sending message: {e}")

if __name__ == "__main__":
    while True:
        message = input("Enter a message to send: ")
        send_message(message)
        time.sleep(2)
