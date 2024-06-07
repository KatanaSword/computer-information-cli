def os():
    pass

def processor():
    pass

def ram():
    pass

def system_type():
    pass

def wifi():
    pass

def storage():
    pass

def battery():
    pass

def main():
    while True:
        print("\n1. Know Computer Oprating System.")
        print("2. Know Computer Processor.")
        print("3. Know Computer RAM.")
        print("4. Know Computer System Type.")
        print("5. Know About Computer WiFi.")
        print("6. Know Computer Storage.")
        print("7. Know Computer Battery.")
        print("0. Exit App")
        choose = input("Enter a number to learn more about your computer: ")

        if choose == 1:
            os()
        elif choose == 2:
            processor()
        elif choose == 3:
            ram()
        elif choose == 4:
            system_type()
        elif choose == 5:
            wifi()
        elif choose == 6:
            storage()
        elif choose == 7:
            battery()
        elif choose == 8:
            break
        else:
            print("Invalid Number Try Again")

if __name__ == "__main__":
    main()