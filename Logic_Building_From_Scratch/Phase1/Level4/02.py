# Take a number and print “Fizz” if divisible by 3, “Buzz” if divisible by 5, and “FizzBuzz” if divisible by both. 



try : 
    number = float(input("Enter the number :" ).strip())

    if number % 3 == 0 and number % 5 == 0 :
        print("FizzBuzz")
        
    elif number % 3 == 0  : 
        print("Fizz")
        
    elif number % 5 == 0:
        print("Buzz")
    else: 
        print("no fizz no buzz ")
except Exception as e: 
    print("Following error occurs : {e}")