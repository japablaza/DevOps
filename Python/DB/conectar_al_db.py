#!/user/bin/env python

import mysql.connector
from mysql.connector import Error
import pandas as pd
import os 

server  = os.environ.get("DB_SERVER")
usuario = os.environ.get("DB_USER")
laclave = os.environ.get("DB.CLAVE")
 
def contect_a_db(server, usuario, laclave)