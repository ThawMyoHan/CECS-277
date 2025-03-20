def main():

    print("Sum and Avg: Enter values or Q to quit")
    count = 0
    sum = 0
    val = 0
    while val != "Q":
        val = input("Enter number " + str(count) + " (or Q to quit): ")
        if val != "Q":
            sum += int(val)
            count += 1
        else:
            print("Sum  = " + str(sum))
            print("Average = " + str(sum / (count+1)))

main()
