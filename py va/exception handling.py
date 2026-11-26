# A.error and exception 
# 1.sytex error
# 2.logic error

# 3.why do we need exception handling 
# we want to exception handling for some sensitive cases 
# eg.while payment menthod and payment was alredy done but purchase of item 
# is not done so to refund money exception handligh is used



# 1.try 
# try:
# is which error could be happen those block of code is in try

# except:
# code that runs if exception occurs



# program 1:


# try:
#     a=10
#     b=0
#     result = a/b
#     print(result)

# except:
#     print("something went wrong")

# print("program complete")


#zerodivision error 
#vlaue error
#type error
#index error
#name error
#key error    

# value error vs type error

# try:
#     num = int(input("Enter a number: "))
#     result = 100 / num
# except ValueError:
#     print("Invalid input")
# except ZeroDivisionError:
#     print("Cannot divide by zero")
# else:
#     print("Result:", result)
#     print("Calculation successful")  #else get used if oonly try block runs without any error then only else block will run
# finally:    #finally is used to print the code is ended 

#     print("program is completed") 

    #finally program also runs only with try but will only run without error while running and will run finally
    #just it will terminate when error in try block 

age = 15
try:
    if age < 18:
        raise ValueError("you must enter a valid age to procced")
except ValueError as e:
    print("error:",e)
    
else:
    print("acess granted")