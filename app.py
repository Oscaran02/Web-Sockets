import json
import time
import _thread
from itertools import count

import websocket


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


# Class to store the data block
class DataBlock:
    # set the initial values
    def __init__(self):
        self.__max_number = None  # Store the max number
        self.__min_number = None  # Store the min number
        self.__first_number = None  # Store the first number
        self.__last_number = None  # Store the last number
        self.__number_of_prime_numbers = 0  # Store the number of prime numbers
        self.__number_of_even_numbers = 0  # Store the number of even numbers
        self.__number_of_odd_numbers = 0  # Store the number of odd numbers

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

    # Method to get the max number
    def get_max_number(self):
        return self.__max_number

    # Method to get the min number
    def get_min_number(self):
        return self.__min_number

    # Method to get the first number
    def get_first_number(self):
        return self.__first_number

    # Method to get the last number
    def get_last_number(self):
        return self.__last_number

    # Method to get the number of prime numbers
    def get_number_of_prime_numbers(self):
        return self.__number_of_prime_numbers

    # Method to get the number of even numbers
    def get_number_of_even_numbers(self):
        return self.__number_of_even_numbers

    # Method to get the number of odd numbers
    def get_number_of_odd_numbers(self):
        return self.__number_of_odd_numbers

    # Print the data block
    def show_data(self):
        print("Max number: " + str(self.__max_number))
        print("Min number: " + str(self.__min_number))
        print("First number: " + str(self.__first_number))
        print("Last number: " + str(self.__last_number))
        print("Number of prime numbers: " + str(self.__number_of_prime_numbers))
        print("Number of even numbers: " + str(self.__number_of_even_numbers))
        print("Number of odd numbers: " + str(self.__number_of_odd_numbers))


class SocketClient:
    def __init__(self):
        # Activate this if you want to see the websocket messages
        websocket.enableTrace(False)
        self.ws = None
        self.data_blocks = []

    def start_socket(self):
        self.reset_data()
        # Connect to the websocket
        self.ws = websocket.WebSocketApp("ws://209.126.82.146:8080/",
                                         on_message=self.on_message,
                                         on_error=self.on_error)
        self.ws.on_open = self.on_open

        # Run the websocket
        self.ws.run_forever()

    # Default method to receive the data from the server
    def on_message(self, ws, message):
        data = json.loads(message)
        self.data_blocks[data["a"] - 1].update_data(data["b"])

    # Default method to print and catch errors
    def on_error(self, ws, error):
        print(error)

    # Method to manage the logic of the program when the connection starts
    def on_open(self, ws):
        def run():
            while True:
                time.sleep(60)  # Wait 60s to start the analysis
                counter = count(start=1, step=1)
                # Print the recollected data in 1m
                for block in self.data_blocks:
                    print(f"\n\n<<<Block #{next(counter)}>>>")
                    block.show_data()
                self.reset_data()

        # Start the thread to manage the logic of the program
        _thread.start_new_thread(run, ())

    # Method to reset and create a list of the data blocks
    def reset_data(self, size=100):
        self.data_blocks.clear()
        # init the list with 100 data blocks
        for i in range(size):
            self.data_blocks.append(DataBlock())


if __name__ == "__main__":
    socket = SocketClient()
    socket.start_socket()
