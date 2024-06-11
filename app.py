import platform
import psutil

def system_info():
    sys  = platform.uname()
    print(f"\n{"*"*30} System Information {"*"*30}")
    print(f"System: {sys.system}")
    print(f"Node name: {sys.node}")
    print(f"Release: {sys.release}")
    print(f"Version: {sys.version}")
    print(f"Machine: {sys.machine}")
    print(f"Processor: {sys.processor}")
    print(f"Physical core: ", psutil.cpu_count(logical=False))
    print(f"Total core: ", psutil.cpu_count(logical=True))

    cup_freq = psutil.cpu_freq()
    print(f"\n{"*"*30} CPU Frequencies {"*"*30}")
    print(f"Max frequency: {cup_freq.max:.2f}Mhz")
    print(f"Min frequency: {cup_freq.min:.2f}Mhz")
    print(f"Current frequency: {cup_freq.current:.2f}Mhz")

def main():
    while True:
        print("\n1. Know Computer System.")
        print("2. Know Computer CPU.")
        print("3. Know Computer Network.")
        print("4. Know Computer GPU.")
        print("5. Know About Virtual Memory.")
        print("0. Exit App")
        choose = input("Enter a number to learn more about computer: ")

        if choose == "1":
            system_info()
        elif choose == "2":
            cpu_info()
        elif choose == "3":
            network_info()
        elif choose == "4":
            gpu_info()
        elif choose == "5":
            virtual_memory_info()
        elif choose == "0":
            break
        else:
            print("Invalid Number Try Again")

if __name__ == "__main__":
    main()