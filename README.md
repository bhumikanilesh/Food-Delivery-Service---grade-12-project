
# **Food Delivery Service System**

## **Overview**
This project is a Python-based food delivery service system that integrates with MySQL for backend operations. It allows users to browse cuisines, select restaurants, place orders, calculate bills (including discounts), and save user and order details in a MySQL database.

---

## **Features**
- **User Registration**:
  - Collects user details like name, phone number, and location.

- **Cuisine and Restaurant Browsing**:
  - Displays available cuisines: `Indian`, `Arabic`, `Chinese`, and `Fast Food`.
  - Lists restaurants offering the selected cuisine with their details (name, location, phone number).

- **Menu Display**:
  - Shows menu items for the selected restaurant with prices.

- **Order Placement**:
  - Allows users to select food items and calculates the total price.
  - Supports applying discounts based on order value.

- **Discount System**:
  - Discounts are applied as follows:
    - Orders below **50 AED**: No discount.
    - Orders between **50 AED and 70 AED**: 10% discount.
    - Orders between **70 AED and 100 AED**: 15% discount.
    - Orders above **100 AED**: 25% discount.

- **Database Integration**:
  - Stores user information, restaurant selection, and order details in the MySQL database.

---

## **Prerequisites**
1. Python 3.x installed on your system.
2. MySQL server installed and running.
3. Required Python libraries:
   - `mysql.connector`
   - `tabulate`

Install the libraries using:
```bash
pip install mysql-connector-python tabulate
```

---

## **Setup and Installation**
1. Clone the repository:
   ```bash
   git clone https://github.com/your-username/food-delivery-service.git
   ```
2. Navigate to the project directory:
   ```bash
   cd food-delivery-service
   ```
3. Set up the MySQL database:
   - Create a database named `project`.
   - Import the required schema and data. Run the SQL commands in the project script or execute `schema.sql` (if provided).
4. Update the database credentials in the Python script:
   ```python
   mycon = ms.connect(host="localhost", user="root", passwd="your-password", database="project")
   ```
5. Run the script:
   ```bash
   python food_delivery_service.py
   ```

---

## **Usage**
1. Register by entering your name, phone number, and location.
2. Browse available cuisines.
3. Select a restaurant and view its menu.
4. Place an order by selecting food items.
5. View the total price, discounts (if applicable), and the final bill.
6. Order details are saved to the database.

---

## **Project Structure**
```
food-delivery-service/
├── food_delivery_service.py   # Main Python script
├── README.md                  # Project documentation
└── schema.sql                 # SQL script to set up database (if applicable)
```

---

## **Technologies Used**
- **Programming Language**: Python
- **Database**: MySQL
- **Libraries**: `mysql.connector`, `tabulate`

---

## **Future Enhancements**
- Add a graphical user interface (GUI) for better user experience.
- Implement online payment integration.
- Enable multi-user support with login functionality.

---
