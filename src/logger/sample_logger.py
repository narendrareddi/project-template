from logger import logger

def some_function():
    logger.info("This is an info message from some_function")
    logger.error("This is an error message from some_function")

if __name__ == "__main__":
    some_function()
