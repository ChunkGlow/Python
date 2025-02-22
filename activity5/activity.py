def temperature():
    temp_input = int(input("Enter a Temperature : "))
    if temp_input < 0:
        print("Freezing")
    elif temp_input < 10:
        print("Very Cold")
    elif temp_input < 20:
        print("Cold")
    elif temp_input < 30:
        print("Warm")
    elif temp_input < 40:
        print("Hot")
    else:
        print("Very Hot")
temperature()
def main():
    temperature()

if __name__ == "__main__":
    main()
''''''
