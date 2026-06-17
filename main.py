from .health import Health
from .data import save_json, load_json, get_statistics


while True:
    print("1. Add Health Record")
    print("2. View All Records")
    print("3. View Statistics")
    print("4. Save & Quit")

    choice = input("Enter choice: ")
    if choice == "1":
        name = input("Enter name: ")
        if name == "":
            print("Name cannot be empty.")
            raise ValueError
        weight = input("Enter weight in kg: ")
        try:
            weight = float(weight)
        except ValueError:
                print("invalid weight")
        if weight <= 0:
            print("Weight must be positive.")
            raise ValueError
        else:
            height = input("Enter height in m: ")
            try:
                height = float(height)
                if height <= 0:
                    print("Height must be positive.")
            except ValueError:
                print("Invalid height. Enter a number.")

        print(f"Name: {name}, Weight: {weight}kg, Height: {height}m")

        b = barbie = Health(name, weight, height)
        save_json([b])

        print(
        f"Added {barbie.name}: BMI {barbie.bmi} ({barbie.get_category()}) | "
        f"Ideal: {barbie.get_ideal_weight()}kg | Advice: {barbie.get_health_advice()}"
        )


    elif choice == "2":
        data = load_json()
        print(data)
        if len(data) == 0:
                print("No records found.")
        for person in data:
            print(f"{person.name} - {person.weight_kg}kg, {person.height_m}m, BMI {person.bmi:.2f} ({person.get_category()})")
        

    elif choice == "3":
        stats = get_statistics()
        print("Statistics:", stats)

    elif choice == "4":
        print("Saving and quitting...")
        break

    else:
        print("Invalid choice.")
