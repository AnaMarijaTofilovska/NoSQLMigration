import pyodbc  # Import the pyodbc module for connecting to SQL Server
from pymongo import MongoClient  # Import the MongoClient class from the pymongo module for connecting to MongoDB

# SQL Server connection details
server = 'MSI'  # Server name where SQL Server is hosted
database = 'UniversityEnrollmentDataBase'  # Name of the database within SQL Server
trusted_connection = 'yes'  # Indicates whether to use Windows authentication (yes or no)
driver = '{SQL Server}'  # ODBC driver to be used for the connection

# MongoDB connection details
mongo_client = MongoClient('mongodb://localhost:27017/')  # Connect to MongoDB server running on localhost at default port
mongo_db = mongo_client['university']  # Select the 'university' database within MongoDB

# Create the SQL Server connection
conn = pyodbc.connect(f'DRIVER={driver};SERVER={server};DATABASE={database};Trusted_Connection={trusted_connection}')  # Establish connection to SQL Server
cursor = conn.cursor()  # Create a cursor object to execute SQL commands

# Retrieve data from each table and insert it into MongoDB collections
tables = ['STUDENT', 'FACULTY', 'COURSE', 'INVOICE', 'PROFFESOR', 'ADMINISTRATOR', 'HAS']  # List of tables to migrate

for table in tables:  # Iterate through each table
    cursor.execute(f'SELECT * FROM {table}')  # Execute SQL query to select all columns from the current table
    rows = cursor.fetchall()  # Fetch all rows returned by the query
    collection = mongo_db[table.lower()]  # Select a MongoDB collection based on lowercase table name
    
    for row in rows:  # Iterate through each row
        data = {}  # Create an empty dictionary to store row data
        for idx, column in enumerate(cursor.description):  # Iterate through columns
            data[column[0]] = row[idx]  # Add key-value pair to data dictionary (column name: column value)
        collection.insert_one(data)  # Insert row data into MongoDB collection
    
    # Print a message indicating the number of records migrated and the corresponding MongoDB collection
    print(f'{len(rows)} records from {table} migrated to MongoDB collection {table.lower()}')

print('Migration completed!')  # Print a completion message
