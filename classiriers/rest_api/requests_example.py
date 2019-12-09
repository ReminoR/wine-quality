import requests
import json

def main():
    data = [7.9, 0.35, 0.46, 3.6, 0.078, 15, 37, 0.9973, 3.35, 0.86, 12.8]
    answer = get_requests(data)

    return json.loads(answer)

def get_requests(data):
    url = 'http://127.0.0.1:5000/rf_model/'
    headers = {'content-type': 'application/json', 'Accept-Charset': 'UTF-8'}

    r = requests.post(url, data=json.dumps(data), headers=headers)
    return r.text

if __name__ == '__main__':
    print(main())
