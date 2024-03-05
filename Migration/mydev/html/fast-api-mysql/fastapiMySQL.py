import MySQLdb

# Database configuration
db_config = {
    'host': '127.0.0.1',
    'user': 'mysqluser',
    'passwd': 'password',
    'db': 'topicmatchdb',
}

# Create a connection to the database
conn = MySQLdb.connect(**db_config)