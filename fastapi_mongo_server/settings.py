import os


class MongoDBConfig:
    # TODO Add the database name and authentication details nicely
    username = os.environ.get('MONGO_USERNAME')
    password = os.environ.get('MONGO_PASSWORD')
    database_name = os.environ.get('MONGO_DATABASE', '<ADD_DB_HERE>')
    replica_set = os.environ.get('MONGODB_REPLICA_SET', 'rs0')
    host = os.environ.get('MONGODB_HOST', 'localhost')
    port = os.environ.get('MONGODB_PORT', 27017)
