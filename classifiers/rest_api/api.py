from flask import Flask, request, redirect, url_for, flash, jsonify
import numpy as np
import pickle as p
import json


app = Flask(__name__)


@app.route('/rf_model/', methods=['POST'])
def makecalc():

    data = request.get_data(as_text=True)
    try:
        data = json.loads(data)
    except json.decoder.JSONDecodeError:
        return 'Error: incorrect of data'

    if len(data) != 11:
        return 'Error: The number of features must be equal 11'

    del data[0]
    del data[4]

    pred = np.array2string(model.predict([data])[0])
    pred_proba = np.array2string(np.max(np.around(model.predict_proba([data]), decimals=3)))
    result = jsonify(Class_wine=pred, Probability=pred_proba)

    return result

if __name__ == '__main__':
    model = p.load(open('../rf.pickle', 'rb'))
    app.run(host='127.0.0.1')