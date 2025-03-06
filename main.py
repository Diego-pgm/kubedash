import os
import requests
from flask import Flask, render_template

app = Flask(__name__)

kube_url = os.environ['KUBEHOST']
key = './certs/user.key'
cert = './certs/user.crt'
ca = './certs/ca.crt'

def get_data():

    response = requests.get(kube_url, cert=(cert, key), verify=ca)

    if response.status_code  == 200:
        pods_data = response.json()
        return  [{'name': pod['metadata']['name'], 'status': pod['status']['phase']} for pod in pods_data['items']]
    else:
        print(f'[-] Auth error: {response.status_code}')
        print(response.text)
        return None
    
@app.route('/')
def dashboard():
    return render_template('index.html', pods=get_data())

if __name__ == '__main__':
    app.run('0.0.0.0', 5000, debug=True)







