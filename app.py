import json
import time
import _thread

import websocket


class Mensaje:
    def __init__(self, mensaje, index):
        self.index = index
        self.mensaje = mensaje


class Data_Block:
    def __init__(self):
        self.__max_number = None
        self.__min_number = None
        self.__first_number = None
        self.__last_number = None
        self.__number_of_prime_numbers = None
        self.__number_of_even_numbers = None
        self.__number_of_odd_numbers = None

    def get_max_number(self):
        return self.__max_number

    def get_min_number(self):
        return self.__min_number

    def get_first_number(self):
        return self.__first_number

    def get_last_number(self):
        return self.__last_number

    def get_number_of_prime_numbers(self):
        return self.__number_of_prime_numbers

    def get_number_of_even_numbers(self):
        return self.__number_of_even_numbers

    def get_number_of_odd_numbers(self):
        return self.__number_of_odd_numbers


def on_message(ws, message):
    print(json.loads(message))


def on_error(ws, error):
    print(error)


def on_open(ws):
    def run(*args):
        print("thread terminating...")
        ws.close()

    _thread.start_new_thread(run, ())


if __name__ == "__main__":
    # websocket.enableTrace(True)
    ws = websocket.WebSocketApp("ws://209.126.82.146:8080/",
                                on_message=on_message,
                                on_error=on_error)
    ws.on_open = on_open
    ws.run_forever()
