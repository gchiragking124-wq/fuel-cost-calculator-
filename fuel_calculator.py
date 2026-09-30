
def calculate_fuel_cost():
    print("  FUEL Cost Calculator ")
    print("  (Press Enter without typing anything to exit )")

    # Helper function to get input with exit option
    def get_input_or_exit(prompt, type_func=str):
        while True:
            user_input = input(prompt).strip()
            if not user_input:
                print("Exiting fuel cost calculator.")
                return None
            try:
                return type_func(user_input)
            except ValueError:
                print("Invalid input. Please try again.")

    # Get user inputs
    distance = get_input_or_exit("Enter distance (in km): ", float)
    if distance is None: return

    round_trip_choice = get_input_or_exit("Is this a round trip? (yes/no): ", str)
    if round_trip_choice is None: return
    round_trip_choice = round_trip_choice.lower()

    mileage = get_input_or_exit("Enter mileage (km/L): ", float)
    if mileage is None: return

    fuel_price = get_input_or_exit("Enter petrol/diesel price per litre: ", float)
    if fuel_price is None: return

    passengers = get_input_or_exit("Enter number of people splitting the cost: ", int)
    if passengers is None: return

    # Calculations for a single trip
    if round_trip_choice == 'yes':
        total_distance_per_trip = distance * 2
        trip_type = "Round Trip"
    else:
        total_distance_per_trip = distance
        trip_type = "One-Way"

    fuel_needed_per_trip = total_distance_per_trip / mileage
    total_cost_per_trip = fuel_needed_per_trip * fuel_price
    cost_per_person = total_cost_per_trip / passengers if passengers > 0 else total_cost_per_trip

    # Results for a single trip
    print("\n" + "="*35)
    print(f"Original Distance: {distance:.2f} km")
    print(f"Trip Type:         {trip_type}")
    print(f"Total Distance (per trip):    {total_distance_per_trip:.2f} km")
    print(f"Fuel Needed (per trip):       {fuel_needed_per_trip:.2f} liters")
    print(f"Total Fuel Cost (per trip):   Rs.{total_cost_per_trip:.2f}")
    print(f"Cost Per Person:   Rs.{cost_per_person:.2f}")
    print("="*35)

    # Option to calculate trips for a fixed amount of fuel
    check_fixed_fuel = get_input_or_exit("\nDo you want to check how many trips you can make with a fixed amount of money for fuel? (yes/no): ", str)
    if check_fixed_fuel is None: return
    check_fixed_fuel = check_fixed_fuel.lower()

    if check_fixed_fuel == 'yes':
        money_for_fuel = get_input_or_exit("Enter amount of money for fuel : ", float)
        if money_for_fuel is None: return

        if fuel_price > 0 and total_distance_per_trip > 0:
            liters_bought = money_for_fuel / fuel_price
            distance_possible = liters_bought * mileage
            trips_possible = distance_possible / total_distance_per_trip

            print("\n" + "="*35)
            print(f"With Rs.{money_for_fuel:.2f} you can buy {liters_bought:.2f} liters of fuel.")
            print(f"You can travel approximately {distance_possible:.2f} km.")
            print(f"You can make approximately {trips_possible:.2f} {trip_type}s.")
            print("="*35)
        else:
            print("Cannot calculate trips with fixed fuel amount. Fuel price or trip distance is zero.")

# Run the calculator
calculate_fuel_cost()
input("\nPress Enter to exit...") # This ensures the script pauses before closing the window.
