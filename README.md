# Fuel Cost & Trip Budget Calculator

An engineering-grade, modular Python command-line utility engineered to model route fuel consumption, distribute travel expenses equitably among passengers, evaluate reverse budgets, and persist session history to structured CSV audit logs.

---

## Academic Project Details
* **Student Name:** Chirag G
* **Registration / Roll No:** 26BCE10925
* **Class / Division:** B11-CSE1021
* **Course:** Computer Science / Python Programming Practical
* **Institution:** VIT Bhopal
* **Supervisor / Mentor:** Devendra kumar vedi
* **Department:** Department of Computer Science
* **Date:** 29/09/2026

---

## Core Capabilities
* **Precision Cost Modeling:** Converts odometer measurements and vehicle fuel economies into exact volume and currency metrics.
* **Equitable Expense Allocation:** Distributes fiscal responsibility across passengers while guarding against zero-headcount edge cases.
* **Reverse Budget Synthesis:** Determines maximum travel distances and trip capacities from a fixed rupee allowance.
* **Data Persistence:** Preserves trip histories into structured CSV records for auditability and personal expense tracking.
* **Defensive Console Layer:** Safely validates inputs, catching invalid types or empty values to enable graceful session termination.

---

## Mathematical Formulations
* **Total Effective Distance:**  
  $$D_{effective} = D_{base} \times (2 \text{ if Round Trip else } 1)$$
* **Volume Consumption:**  
  $$V = \frac{D_{effective}}{\text{Mileage (km/L)}}$$
* **Aggregate Cost:**  
  $$C_{total} = V \times P_{per\_liter}$$
* **Passenger Allocation:**  
  $$C_{person} = \frac{C_{total}}{\max(1, N_{passengers})}$$
* **Reverse Budget Capacity:**  
  $$V_{purchased} = \frac{\text{Budget}}{P_{per\_liter}}, \quad D_{range} = V_{purchased} \times \text{Mileage}, \quad N_{trips} = \frac{D_{range}}{D_{effective}}$$

---

## Step-by-Step Setup & Execution (For Evaluators)

### Prerequisites
* You only need standard **Python 3** installed on your system (Python 3.6 or newer). No external third-party libraries (such as `pip install ...`) are required, as the project uses built-in Python modules.

### 1. Download the Project
* Click the green **Code** button at the top of this GitHub repository page and select **Download ZIP**.
* Extract the downloaded `.zip` folder to your preferred location (e.g., your Desktop or Documents).

### 2. Launch the Application
* **On Windows:**
  1. Open the extracted project folder.
  2. Click on the address bar at the top of the folder window, type `cmd` or `powershell`, and press **Enter**.
  3. Run the following command:
     ```bash
     python fuel_calculator.py
     ```
     *(Or double-click `fuel_calculator.py` directly).*
* **On macOS / Linux:**
  1. Open your Terminal and navigate to the project directory:
     ```bash
     cd /path/to/extracted/folder
     ```
  2. Run the script:
     ```bash
     python3 fuel_calculator.py
     ```

---

## Step-by-Step User Guide (How to Use)

When launched, the program guides the user interactively through sequentially validated prompts:

1. **Enter Distance:**
   * Enter the one-way route distance in kilometers (e.g., `145.50`).
2. **Select Trip Mode:**
   * Type `yes` for a round trip (this automatically doubles your base distance) or `no` for a single one-way trip.
3. **Enter Vehicle Fuel Economy (Mileage):**
   * Enter the fuel efficiency in km/L (e.g., `16.2`).
4. **Enter Fuel Price:**
   * Enter the current retail fuel price per liter in Rupees (e.g., `101.40`).
5. **Enter Passenger Count:**
   * Enter the number of people splitting the expense (e.g., `3`).
   * *Safety Note:* Entering `0` or `1` will safely allocate 100% of the cost to the single driver without causing any division errors.
6. **Review Summary Receipt:**
   * The terminal immediately outputs a neatly formatted receipt showing total distance, fuel required in liters, overall cost, and individual cost per person.
7. **Optional: Run Reverse Budget Forecast:**
   * Type `yes` when prompted to evaluate a fixed cash budget.
   * Enter a cash amount (e.g., `2500.00`).
   * The program calculates the purchasable liters, total possible driving distance, and total round trips achievable.
8. **Exit or Terminate Anytime:**
   * Pressing **Enter** on an empty input prompt safely exits the calculator without crashing.
9. **Automatic Audit Trail:**
   * All trip computations are automatically timestamped and appended into `trip_history.csv` in the root folder for record-keeping.

---

## Sample Test Run Walkthrough

```text
  FUEL Cost Calculator 
  (Press Enter without typing anything to exit )

Enter distance (in km): 145.50
Is this a round trip? (yes/no): yes
Enter mileage (km/L): 16.2
Enter petrol/diesel price per litre: 101.40
Enter number of people splitting the cost: 3

===================================
Original Distance: 145.50 km
Trip Type:         Round Trip
Total Distance (per trip):    291.00 km
Fuel Needed (per trip):       17.96 liters
Total Fuel Cost (per trip):   Rs.1821.43
Cost Per Person:   Rs.607.14
===================================

Do you want to check how many trips you can make with a fixed amount of money for fuel? (yes/no): yes
Enter amount of money for fuel : 2500.00

===================================
With Rs.2500.00 you can buy 24.65 liters of fuel.
You can travel approximately 399.41 km.
You can make approximately 1.37 Round Trips.
===================================
   ```bash
   python fuel_calculator.py
