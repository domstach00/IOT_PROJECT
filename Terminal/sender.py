import paho.mqtt.client as mqtt
from constants import *
import datetime
import terminalscreen

# The MQTT client.
client = mqtt.Client()


def send_log(card: str, activity: str, register_time: str = datetime.datetime.now().strftime("%d/%m/%Y %H:%M:%S")):
    test = datetime.datetime.now().strftime("%d/%m/%Y %H:%M:%S")
    client.connect(BROKER)
    client.publish(SUBSCRIBE, f"{card}.{activity}.{test}.{TERMINAL_ID}")
    print(f"Wysłano: {card} : {activity} : {register_time} : {TERMINAL_ID}")


def connect_to_broker():
    # Connect to the broker.
    client.connect(BROKER)


def disconnect_from_broker():
    # Disconnet the client.
    client.disconnect()


def main():
    connect_to_broker()
    terminalscreen.main()
    disconnect_from_broker()


if __name__ == '__main__':
    main()
