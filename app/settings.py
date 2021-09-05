import os


class MongoDBConfig:
    # TODO Add the database name
    db = os.environ.get('DATABASE', '<ADD DB HERE>')
    replicaSet = os.environ.get('REPLICA_SET', 'rs0')
    host = os.environ.get('HOST', 'localhost')
    port = os.environ.get('PORT', 27017)
