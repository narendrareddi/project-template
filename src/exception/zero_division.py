import sys
from exception import customexception

def divide(a, b):
    try:
        return a / b
    except Exception as e:
        raise customexception(e, sys)

if __name__ == "__main__":
    try:
        result = divide(10, 0)
        print("Result:", result)
    except customexception as ce:
        print(ce)
