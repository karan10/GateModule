from flask import Flask
from flask_cors import CORS

app = Flask('dextr-docker')
CORS(app)

import api.users
import api.gate