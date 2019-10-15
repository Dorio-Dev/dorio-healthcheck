import subprocess
import yaml
from flask import Flask

app = Flask(__name__)


@app.route('/')
def hello_world():
    yml = open('config.yaml', 'r')
    #result = subprocess.check_output("ps -ef | grep bash", shell=True)
    ymlResult = yaml.load(yml)
    processes = ymlResult['processes']

    result = "test <br/>"
    for p in processes:
        result += "name : " +  p['name']
        str = subprocess.check_output("ps -ef | grep " + p['ps'] + "| grep -v grep | wc -l", shell=True)
        result += "<br/>ps count : " + str.decode('utf-8')
        result += "<br/>"




    #print(ymlResult['test'])
    #result = subprocess.check_output("ps -ef | grep " + processes['cmd'] + "| grep -v grep | wc -l", shell=True)

    return result


if __name__ == '__main__':
    app.run()
