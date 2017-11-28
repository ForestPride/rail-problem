def main():
    print ("This program just tests things")
    capacity = int(eval(input("Enter the max capacity of the station: ")))
    if type(capacity) == int:
        print("You just set the max capacity")
    else:
        print("Enter an integer")
    print(capacity)
main()
