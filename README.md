# NoSQLMigration
This repository contains a Python script (migration.py) for migrating data from a relational database (SQL Server) to a NoSQL database (MongoDB) for a university enrollment system. The script retrieves data from tables in the SQL database and inserts it into corresponding collections in the MongoDB database.

# University Enrollment Data Migration

This script migrates data from a SQL database to MongoDB for a university enrollment system.

## Installation

To run this script, you'll need to install the following dependencies:

```bash
pip install pymongo
pip install pyodbc
```

## Usage

To migrate data, run the following command:

```bash
python migration.py
```

## Documentation

This script connects to a SQL Server database and a MongoDB instance to migrate data. It retrieves data from specified tables in the SQL database and inserts it into corresponding collections in MongoDB.

## Contributing

Contributions are welcome! Please submit bug reports, feature requests, or pull requests through GitHub.

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

## Acknowledgments

- Thanks to the contributors of the pyodbc and pymongo libraries.
