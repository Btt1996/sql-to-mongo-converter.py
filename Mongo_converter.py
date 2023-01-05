import pymongo

# Connect to the MongoDB server
client = pymongo.MongoClient('mongodb://localhost:27017/')

# Select the database and collection
db = client['mydatabase']
collection = db['mycollection']

# Define a function to convert an SQL SELECT statement to a MongoDB find() query
def convert_select(sql):
    # Split the SQL statement into words
    words = sql.split()

    # Check if the SELECT statement has a WHERE clause
    if 'WHERE' in words:
        # Extract the field and value to filter by
        field = words[words.index('WHERE')+1]
        value = words[words.index('WHERE')+3]

        # Execute the MongoDB find() query and return the results
        return list(collection.find({field: value}))
    else:
        # Execute the MongoDB find() query without a filter and return the results
        return list(collection.find())

# Define a function to convert an SQL INSERT statement to a MongoDB insert_one() query
def convert_insert(sql):
    # Split the SQL statement into words
    words = sql.split()

    # Extract the field names and values from the INSERT statement
    fields = words[1][1:-1].split(',')
    values = words[3][1:-1].split(',')

    # Create a document from the field names and values
    doc = {}
    for i in range(len(fields)):
        doc[fields[i]] = values[i]

    # Execute the MongoDB insert_one() query
    collection.insert_one(doc)
