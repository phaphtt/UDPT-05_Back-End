
from flask import Flask

app = Flask(__name__)
app.config['JSON_AS_ASCII'] = False
from src.Controllers import employee
from src.Controllers import login
from src.Controllers import department
