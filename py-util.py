from flask import Flask, request, redirect, url_for, flash, jsonify
import psutil
import json
import os, sys

application = Flask(__name__)
@application.route('/')
def calculate():
    #Processing sys info
    cpu = psutil.cpu_percent()
    mem = psutil.virtual_memory().percent
    diskpartition = psutil.disk_partitions()
    du = psutil.disk_usage('/')
    
    result={"cpu_usage": cpu, "memory_used": mem, "disk_usage": du, "partitions": diskpartition}

    return jsonify(result)

if __name__ == '__main__':
    application.run(host='0.0.0.0', port=9000)

