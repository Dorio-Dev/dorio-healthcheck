import subprocess
import yaml
from flask_api import status
from flask import Flask

app = Flask(__name__)


@app.route('/HealthCheck')
def healthCheck():
    yml = open('config.yaml', 'r')
    ymlResult = yaml.load(yml)
    processes = ymlResult['processes']

    result = "Process Monitoring <br/>"
    for p in processes:
        result += "name : " +  p['name']
        str = subprocess.check_output("ps -ef | grep " + p['ps'] + "| grep -v grep | wc -l", shell=True)
        result += "<br/>ps count : " + str.decode('utf-8')
        result += "<br/>"
        if int(str) < 1 :
                return result, status.HTTP_503_SERVICE_UNAVAILABLE

    return result


if __name__ == '__main__':
    app.run(host='0.0.0.0',port='8000')
