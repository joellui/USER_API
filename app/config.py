import os
MONGO_URI = os.environ.get('MONGO_URI', 'mongodb://localhost:27017') or 'mongodb://localhost:27017'