def fibonacci(startInt, length = 2):
    if not isinstance(startInt, int):
        raise TypeError("Starting point must be of type integer")
        
    series = []
    prevInt = startInt
    currentInt = startInt
    for i in range(length):
        # calculate the next fibonacci number
        nextInt = prevInt + currentInt
        series.append(nextInt)
        
        # update F_n-1 and F_n-2
        temp = currentInt
        currentInt = nextInt
        prevInt = temp
    return series
    
    
def main():    
    series = fibonacci(1, 9)
    file = open("fibonacci.txt", "w")
    
    for i in series:
        file.write(str(i) + " ")
    print("saved to fibonacci.txt")
    file.close()
    

main()




