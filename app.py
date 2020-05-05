from flask import Flask
from flask_cors import CORS

app = Flask('gating module')
CORS(app)

import api.users
import api.gate