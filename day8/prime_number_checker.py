def checkPrimeNumber(num):
    for i in range(2, num):
        if num%i == 0:
            return False
    return True


if "__main__" == __name__:
    num = int(input("Enter a number: "))
    flag = checkPrimeNumber(num)
    if flag:
        print("Number is Prime")
    else:
        print("Non Prime Number")