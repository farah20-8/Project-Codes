import time
import random
from azure.iot.device import IoTHubDeviceClient, Message


CONNECTION_STRING = "HostName=iotc-a8146a69-ae78-416d-b01b-5329377a7304.azure-devices.net;DeviceId=1kv0189oyez;SharedAccessKey=fSoxSU7Xdm8NeksgbhDcnfd+rnrSNhUhCQd4b4WHc+Y="


MESSAGE_TEMPLATE = '{{"airQuality": {}}}'


client = IoTHubDeviceClient.create_from_connection_string(CONNECTION_STRING)

def send_air_quality_data():
    """Simulate air quality data and send it to Azure IoT Hub."""
    while True:
        try:
            air_quality = random.randint(37, 54)  
            message = Message(MESSAGE_TEMPLATE.format(air_quality))
            print(f"Sending message: {message}")
            client.send_message(message)
            print("Message successfully sent to Azure IoT Hub.")
        except Exception as e:
            print("Error sending data:", e)

        time.sleep(5)  


try:
    print("Connecting to Azure IoT Hub...")
    client.connect()
    print("Connected successfully.")
    send_air_quality_data()
except Exception as e:
    print("Connection error:", e)
finally:
    client.shutdown()
