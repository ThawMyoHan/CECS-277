def main():

    num = int(input("Enter #(1-10): "))
    while num != 7:
        print(num, "is incorrect.")
        num = int(input("Enter #(1-10): "))
    print("Correct")

main()