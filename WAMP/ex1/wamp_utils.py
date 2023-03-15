import random  # Import the random module for generating random numbers

def random_temperature():  # Define a function called random_temperature
    return round(random.uniform(20, 30), 2)  # Generate a random floating-point number between 20 and 30 (inclusive) using the uniform method of the random module, round it to 2 decimal places using the round function, and return the result
