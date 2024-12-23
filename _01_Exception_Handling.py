try:
    num1 = int(input())
    num2 = int(input())
    result = num1 / num2
except ValueError:
    print("Error: num1, and num2 must be integer")
except ZeroDivisionError:
    print("Error: Division by Zero.")
except:
    print("Error: Something went wrong!")
else:
    # If No Exception - Execute
    print(f"Final Result:", result)
finally:
    # Always Executed
    print("Execution done!")


