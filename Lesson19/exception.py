class JustNotCoolError(Exception):
    pass

x = 2

try: 
    raise JustNotCoolError("This isn't coool")
    # raise Exception("I'm a custom exception!")
    # print(x / 0)
    # if not type(x) is str:
    #     raise TypeError("Only strings are allowed")
    
except NameError:
    print('NameError = something is undefined')
except ZeroDivisionError:
    print('Do not divide by zero')
except Exception as error:
    print(error)
else:
    print('No Errors!!!!! :D')
finally:
    print("I'm going to print with or without an error.")
