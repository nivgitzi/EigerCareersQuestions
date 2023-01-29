
def sumOfAllDigits(num):    # The function Which sums the digits of a given number

    if (num // 10 == 0):    # condition can also be: if(num == 0), but it is an unnecessary call
        return num
    else:
        return (num % 10) + sumOfAllDigits(num // 10)



while True:    #keep reading input, until a valid integer is entered
    try:
        inputNum = int(input("Enter a number:"))
    except:
        print("please write a valid Integer")
    else:
        inputNum = abs(inputNum)     # in case num is negative
        print(sumOfAllDigits(inputNum))     # print the sum of digits
        break


