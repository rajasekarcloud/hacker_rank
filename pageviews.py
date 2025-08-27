def function_d(data):
    data.append("Inside function D")
    return data

def function_c(data):
    data.append("Inside function C")
    function_d(data)
    return data

def function_b(data):
    data.append("Inside function B")
    function_c(data)  # call function_c
    return data  # pass it back to whoever called function_b

def function_a(data):
    data.append("Inside function A")
    function_b(data)  # call function_b
    return data  # return all the way back

# Calling the first function
data=[]
final_result = function_a(data)
print("Final result returned to main:", final_result)
