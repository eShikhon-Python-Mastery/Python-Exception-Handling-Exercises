try:
    num = int(input())
    if num < 0:
        raise ValueError("num should be positive")
except ValueError as ve:
    print("Caught an exception:", ve)
    # raise # re-raises the same exception