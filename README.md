# sql-to-mongo-converter.py
SQL to MongoDB Converter

This Python program converts basic SQL commands (SELECT, INSERT) to equivalent MongoDB commands. It consists of three files:

mongo_converter.py: Contains functions to convert SQL SELECT and INSERT statements to MongoDB find() and insert_one() queries, respectively.
file_writer.py: Contains a function to write the results of a MongoDB query to a file.
main.py: Contains a function to convert an SQL statement to a MongoDB command and write the results to a file, if applicable.
Requirements

Python 3
pymongo
Usage

To use the program, run the main.py file and pass an SQL statement and a filename as arguments to the convert_sql() function. The program will convert the SQL statement to a MongoDB command and write the results to the specified file, if applicable.

For example:
import main

main.convert_sql('SELECT * FROM mycollection WHERE field1 = value1', 'results.txt')
main.convert_sql('INSERT INTO mycollection (field1, field2) VALUES (value1, value2)', 'results.txt')


The program currently supports SELECT and INSERT statements only. Attempting to convert other types of SQL statements (e.g. UPDATE, DELETE) will result in an error message.

License

This project is licensed under the MIT License. See the LICENSE file for details.

