print ("Convert Temperature")
print ("-------------------")

def c_to_f (C):
    f_ans = str((1.8)*(C) + 32)
    print ("Temperature = " + f_ans + "℉")

def f_to_c (F):
    c_ans = str(((F)-32)/(1.8))
    print ("Temperature = " + c_ans + "℃")

using = True
while using == True:

    response = str(input("\nConvert to Celsius? [c] or to Fahrenheit? [f]\n"))
    if response=="f":
        C = float(input("\nTemperature in Celsius:\n"))
        c_to_f(C)
        pass
    elif response=="c":
        F = float(input("\nTemperature in Fahrenheit:\n"))
        f_to_c(F)
        pass
    else:
        print("Please enter a valid character [c]/[f]")
    
    again = input("\nTry again? (y to retry)\n")
    if again == "y":
        continue
    else:
        exit()
