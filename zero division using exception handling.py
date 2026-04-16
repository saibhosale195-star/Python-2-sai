num1 = int(input("Enter numerator: "))
num2 = int(input("Enter denominator: "))

try:
    if num2 == 0:
        print("Cannot divide by zero (checked using if).")
    else:
        result = num1 / num2
        print("Result:", result)

except Exception as e:
    print("An error occurred:", e)

else:
    print("Division performed successfully.")

finally:
    print("Program execution completed.")