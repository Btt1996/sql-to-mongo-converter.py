import mongo_converter
import file_writer

# Define a function to convert an SQL statement to a MongoDB command
def convert_sql(sql, filename):
    # Split the SQL statement into words
    words = sql.split()

    # Check the first word to determine the type of SQL statement
    if words[0] == 'SELECT':
        # Convert the SELECT statement to a MongoDB find() query
        results = mongo_converter.convert_select(sql)
    elif words[0] == 'INSERT':
        # Convert the INSERT statement to a MongoDB insert_one() query
        mongo_converter.convert_insert(sql)
        results = None
    else:
        # Return an error message for unsupported SQL statements
        results = 'Error: Unsupported SQL statement'

    # Write the results to a file, if applicable
    if results is not None:
        file_writer.write_to_file(results, filename)

# Test the convert_sql() function with various SQL statements
convert_sql('SELECT * FROM mycollection WHERE field1 = value1', 'results.txt')
convert_sql('INSERT INTO mycollection (field1, field2) VALUES (value1, value2)', 'results.txt')
convert_sql('UPDATE mycollection SET field1 = value1 WHERE field2 = value2', 'results.txt')
