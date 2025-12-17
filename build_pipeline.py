def build_pipeline(operation_names):
    
    result = None
    
    def operations(name_of_operation, number):
        
        if name_of_operation == "double":
            return 2 * number
        elif name_of_operation == "triple":
            return 3 * number
        elif name_of_operation == "square":
            return number * number
        else:
            return None
            
    def operations_seq(value):
        nonlocal operation_names
        nonlocal result
        
        result = value
        
        for i in range(len(operation_names)):                
            result = operations(operation_names[i], result)
            
        return result
    
    for i in range(len(operation_names)):
        if operations(operation_names[i], 1) is None:
            raise KeyError
    
    return operations_seq