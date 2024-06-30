def convert_data_size(value, from_unit, to_unit):
    units = ["B", "KB", "MB", "GB", "TB", "PB", "EB", "ZB", "YB"]
    from_index = units.index(from_unit)
    to_index = units.index(to_unit)
    factor = 1024 ** (to_index - from_index)
    return value * factor

def convert_data_rate(value, from_unit, to_unit):
    units = ["bps", "Kbps", "Mbps", "Gbps", "Tbps"]
    from_index = units.index(from_unit)
    to_index = units.index(to_unit)
    factor = 1000 ** (to_index - from_index)
    return value * factor

def unit_converter():
    print("Network and Computer Unit Converter")
    print("1. Data Size (e.g., KB to MB)")
    print("2. Data Rate (e.g., Mbps to Gbps)")
    print("3. Exit")

    choice = input("Select an option: ")
    if choice == "1":
        value = float(input("Enter value: "))
        from_unit = input("Enter from unit (B, KB, MB, GB, TB, PB, EB, ZB, YB): ").strip().upper()
        to_unit = input("Enter to unit (B, KB, MB, GB, TB, PB, EB, ZB, YB): ").strip().upper()
        result = convert_data_size(value, from_unit, to_unit)
        print(f"{value} {from_unit} is {result:.2f} {to_unit}")
    elif choice == "2":
        value = float(input("Enter value: "))
        from_unit = input("Enter from unit (bps, Kbps, Mbps, Gbps, Tbps): ").strip()
        to_unit = input("Enter to unit (bps, Kbps, Mbps, Gbps, Tbps): ").strip()
        result = convert_data_rate(value, from_unit, to_unit)
        print(f"{value} {from_unit} is {result:.2f} {to_unit}")
    elif choice == "3":
        return
    else:
        print("Invalid option, please try again.")
