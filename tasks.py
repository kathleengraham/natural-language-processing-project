#----------------------------------------Background worker process----------------------------------------#
#
#--- Imports ---#
# Throughout this program we call the below imports for various actions
# failing to import one of these libraries, or importing the wrong one
# may be one reason for an app just failing mid-process

# All of these libraries need to be reflected in our requirements file
# which we upload as part of our app

import celery
from celery import Celery
app = celery.Celery('example')

import os

from flask import Flask, make_response, request

import oauth2client
from datetime import datetime, time, date, timedelta
from oauth2client.service_account import ServiceAccountCredentials
import json

import os.path
import sys

import requests

import re

try:
    import dialogflow
except ImportError:
    sys.path.append(
        os.path.join(os.path.dirname(os.path.realpath(__file__)), os.pardir))
    import dialogflow
from collections import Counter
import time

import tasks

import psycopg2
from flask.ext.sqlalchemy import SQLAlchemy
#Thanks to http://blog.y3xz.com/blog/2012/08/16/flask-and-postgresql-on-heroku

import urllib.parse
#Thanks to https://stackoverflow.com/questions/45133831/heroku-cant-launch-python-flask-app-attributeerror-function-object-has-no


#--- End of imports ---#
#

#--- Environment variables ---#

# Celery variables
# Thanks to (https://devcenter.heroku.com/articles/celery-heroku, for another good resource on celery and flask, but which had to be modified due to clash with database, go to https://blog.miguelgrinberg.com/post/using-celery-with-flask)
app.conf.update(BROKER_URL=os.environ['REDIS_URL'],
                CELERY_RESULT_BACKEND=os.environ['REDIS_URL'])


# Authentication for sending message to Dialogflow
api_bearer = os.environ["API_BEARER"]

#--- End of environment variables ---#
#
#--- w1 add - async task caled by main process, testing call working ---#

@app.task
def add(app_code,location_code,x, y):
    print (app_code,location_code,"begun")
    print (app_code,location_code,"answer is", x+y)
    return x + y

#--- End of test ---#

# Printing for debugging
json_key = json.load(open('agent.json'))
print (app_code,location_code,sublocation, "json key is: ", json_key)

  
