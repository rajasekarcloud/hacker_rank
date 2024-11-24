# If the number is a multiple of 3 and 5 print "FizzBuzz"
# If its only multiple of 3 and not 5 print "Fizz"
# If its only multiple of 5 and not 3 print "Buzz"
# else print the number
def fizzBuzz(n):
    for i in range(1,n+1):
        if i%3==0 and i%5==0:
            print("FizzBuzz");
        elif i%3==0 and i%5!=0:
            print("Fizz");
        elif i%5==0 and i%3!=0:
            print("Buzz");
        else:
            print(i)
if __name__ == '__main__':
    n = int(input().strip())
    fizzBuzz(n)
