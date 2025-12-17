def safe_call(func, a, b):
    
    success = False
    result = None
    name_of_exception = None
    
    try:
        result = func(a, b)
        success = True
    except ZeroDivisionError:
        name_of_exception = "ZeroDivisionError"
        print(f"Error: {name_of_exception}")
    except TypeError:
        name_of_exception = "TypeError"
        print(f"Error: {name_of_exception}")
    except ValueError:
        name_of_exception = "ValueError"
        print(f"Error: {name_of_exception}")
    except IndexError:
        name_of_exception = "IndexError"
        print(f"Error: {name_of_exception}")
    except KeyError:
        name_of_exception = "KeyError"
        print(f"Error: {name_of_exception}")
        
    return success, result, name_of_exception
    
