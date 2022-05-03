import json
import time
import _thread
from itertools import count

import websocket

# init the list with 100 spaces
data_blocks = []


# Method to know if a number is prime
def is_prime(number):
    if number == 2:
        return True
    if number % 2 == 0 or number <= 1:
        return False

    sqr = int(number ** 0.5) + 1

    for divisor in range(3, sqr, 2):
        if number % divisor == 0:
            return False
    return True


# Method to know if a number is even
def is_even(number):
    if number % 2 == 0:
        return True
    return False


# Method to reset and create a list of the data blocks
def reset_data(size=100):
    global data_blocks
    data_blocks.clear()
    # init the list with 100 data blocks
    for i in range(size):
        data_blocks.append(Data_Block())


class Data_Block:
    # set the initial values
    def __init__(self):
        self.__max_number = None
        self.__min_number = None
        self.__first_number = None
        self.__last_number = None
        self.__number_of_prime_numbers = 0
        self.__number_of_even_numbers = 0
        self.__number_of_odd_numbers = 0

    # Method to add and analyze a number in the data block
    def update_data(self, number):
        # if the data block is empty (first value)
        if self.__max_number is None:
            self.__max_number = number
            self.__min_number = number
            self.__first_number = number
            self.__last_number = number
        else:
            if number > self.__max_number:
                self.__max_number = number
            if number < self.__min_number:
                self.__min_number = number
            self.__last_number = number
        if is_prime(number):
            self.__number_of_prime_numbers += 1
        if is_even(number):
            self.__number_of_even_numbers += 1
        else:
            self.__number_of_odd_numbers += 1

    # Print the data block
    def show_data(self):
        print("Max number: " + str(self.__max_number))
        print("Min number: " + str(self.__min_number))
        print("First number: " + str(self.__first_number))
        print("Last number: " + str(self.__last_number))
        print("Number of prime numbers: " + str(self.__number_of_prime_numbers))
        print("Number of even numbers: " + str(self.__number_of_even_numbers))
        print("Number of odd numbers: " + str(self.__number_of_odd_numbers))


def on_message(ws, message):
    data = json.loads(message)
    data_blocks[data["a"]-1].update_data(data["b"])


def on_error(ws, error):
    print(error)


def on_open(ws):
    def run():
        global data_blocks
        while True:
            time.sleep(10)
            counter = count(start=1, step=1)
            for block in data_blocks:
                print(f"\n\n<<<Bloque #{next(counter)}")
                block.show_data()
            reset_data()

    _thread.start_new_thread(run, ())


if __name__ == "__main__":
    # websocket.enableTrace(True)
    # list of data blocks
    reset_data()
    ws = websocket.WebSocketApp("ws://209.126.82.146:8080/",
                                on_message=on_message,
                                on_error=on_error)
    ws.on_open = on_open
    ws.run_forever()
