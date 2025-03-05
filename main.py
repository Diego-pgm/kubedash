import requests
from flask import Flask, render_template

app = Flask(__name__)

kube_url = 'https://192.168.0.44:6443/api/v1/namespaces/default/pods'
key = './certs/abed.key'
cert = './certs/abed.crt'
ca = './certs/ca.crt'

response = requests.get(kube_url, cert=(cert, key), verify=ca)

if response.status_code  == 200:
    pods_data = response.json()
    pods = [{'name': pod['metadata']['name'], 'status': pod['status']['phase']} for pod in pods_data['items']]
else:
    print(f'[-] Auth error: {response.status_code}')
    print(response.text)


