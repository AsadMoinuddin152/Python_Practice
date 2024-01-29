def divide(n1, n2):
    try:
        print(n1 / n2)
    except ZeroDivisionError:
        print("You can't divide by zero!")
        
    except ValueError:
        print("You must enter a number!")
    
    except: 
        print("Something went wrong!")
    return ("Program is executed successfully")
    
    
print(divide(int(input()), int(input())))