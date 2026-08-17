components = {
    "R1": {
        "type": "Resistor",
        "value": 220,
        "unit": "Ohm",
        "power": "0.25 W",
        "tolerance": "5%"
    },
    "R2": {
        "type": "Resistor",
        "value": 1000,
        "unit": "Ohm",
        "power": "0.5 W",
        "tolerance": "1%"
    },
    "C1": {
        "type": "Capacitor",
        "value": 100,
        "unit": "uF",
        "voltage": "25 V"
    },
    "L1": {
        "type": "Inductor",
        "value": 10,
        "unit": "mH",
        "current": "0.5 A"
    },
    "D1": {
        "type": "LED",
        "color": "Red",
        "forward_voltage": "2.0 V",
        "current": "20 mA"
    }
}

while True:
    print("\n|||||||||||||||||||||||||||||||||||||||||||||||||||||||||")
    print("Electrical Components Database")
    print("|||||||||||||||||||||||||||||||||||||||||||||||||||||||||")
    print("1. Show Components")
    print("2. Add Component")
    print("3. Delete Component")
    print("4. Exit")
    print("\n")
    
    try:
        choice = int(input("Choice: "))
    except ValueError:
        print("Invalid input! Please enter a number.")
        continue

    if choice == 1:
        for component_name, info in components.items():
            print(component_name)
            for key, value in info.items():
                print(f"{key}: {value}")
            print()

    elif choice == 2:
        component_name = input("Component name: ")

        if component_name in components:
            print("Component already exists!")
            continue

        component_type = input("Type: ")

        try:
            value = float(input("Value: "))
        except ValueError:
            print("Invalid input! Please enter a number.")
            continue

        unit = input("Unit: ")

        components[component_name] = {
            "type": component_type,
            "value": value,
            "unit": unit
        }

        print("Component added successfully!")

    elif choice == 3:
        component_name = input("Component name: ")

        if component_name in components:
            del components[component_name]
            print("Component deleted successfully!")
        else:
            print("Component not found!")

    elif choice == 4:
        print("Goodbye!")
        break

    else:
        print("Invalid choice")