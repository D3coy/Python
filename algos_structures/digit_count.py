def count(num):
    delim = 10

    while (num % delim < num):
        delim *= 10

    print(f"\nNumber of digits -> {len(str(delim)[1:])}")
        

def main():
    number = int(input("Enter a number >> \n"))
    count(number)

main()