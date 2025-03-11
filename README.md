# Inventory Management

This Python script sets up a SQLite database (`inventory.db`) and creates a table named `Products` to store brand names and their corresponding product codes. It also inserts a predefined list of products from various brands into the database.

## Code Structure

The code includes the following sections:

- **SQLite Connection**: Establishes a connection to a SQLite database (`inventory.db`).
- **Table Creation**: Creates a table called `Products` with two columns:
  - `marca` (TEXT): The brand of the product.
  - `codigo` (TEXT): The code of the product.
  
- **Predefined Products**: A dictionary of predefined products from four brands:
  - **galvanotek**: ['GA90', 'G695', 'G697']
  - **niagara**: ['MUD1', 'MUD2', 'MUD3']
  - **hiperpack**: ['H742', 'H10', 'H20']
  - **goldpack**: ['3L', '5L', '7L', '12L', 'PESC15', '17L', '28L']

- **Data Insertion**: Iterates over the predefined products and inserts each brand and its corresponding codes into the `Products` table.

## Requirements

To run this project, you will need to have Python and SQLite3 installed on your system.

## How to Run

1. **Clone this repository**:
   ```bash
   git clone https://github.com/lucasfelipecastro/inventory-management.git
   cd inventory-management

2. **Run the script**:
   ```bash
   python inventory-management.py
This will create an inventory.db SQLite database file and insert the predefined product data into the Products table.

## Features

Automatic Table Creation: If the Products table does not exist, the script will automatically create it.

Predefined Product Insertion: The script inserts predefined product data for four brands into the database.

SQLite Error Handling: Handles potential SQLite errors and prints them.

## Example

After running the script, you can inspect the database and see the inserted products with an SQLite viewer or by querying the database:
```bash
  SELECT * FROM Products;
```

## License

This project is licensed under the MIT License - see the [LICENSE](./LICENSE) file for details.
