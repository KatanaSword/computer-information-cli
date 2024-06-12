import platform
import psutil

def get_size(bytes, suffix="B"):
    """
    Scaling bytes to its proper format- KB, MB, GB, TB and PB 
    """
    the_factor = 1024
    for the_unit in ["", "K", "M", "G", "T", "P"]:
        if bytes < the_factor:
            return f"{bytes:.2f} {the_unit}{suffix}"
        bytes /= the_factor

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

def memory_info():
    vm = psutil.virtual_memory()
    print(f"\n{"*"*30} Virtual Memory {"*"*30}")
    print(f"Total: {get_size(vm.total)}")
    print(f"Available: {get_size(vm.free)}")
    print(f"Used: {get_size(vm.used)}")
    print(f"Percentage: {vm.percent} %")

    swap = psutil.swap_memory()
    print(f"\n{"*"*30} SWAP Memory {"*"*30}")
    print(f"Total: {get_size(swap.total)}")
    print(f"Free: {get_size(swap.free)}")
    print(f"Used: {get_size(swap.used)}")
    print(f"Percentage: {swap.percent} %")

def main():
    while True:
        print("\n1. Know Computer System.")
        print("2. Know Computer CPU.")
        print("3. Know Computer Network.")
        print("4. Know Computer GPU.")
        print("5. Know About Virtual Memory.")
        print("6. Know About Storage.")
        print("0. Exit App")
        choose = input("\nEnter a number to learn more about computer: ")

        if choose == "1":
            system_info()
        elif choose == "2":
            cpu_info()
        elif choose == "3":
            network_info()
        elif choose == "4":
            gpu_info()
        elif choose == "5":
            memory_info()
        elif choose == "6":
            storage_info()
        elif choose == "0":
            break
        else:
            print("Invalid Number Try Again")

if __name__ == "__main__":
    main()