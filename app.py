from flask import Flask, request, jsonify
from flask_cors import CORS
app= Flask(__name__)
CORS(app)

@app.route('/generate-triangle', methods=['POST'])
def generate_triangle():
    data = request.get_json()
    number = int(data['number'])
    str_num = str(number)
    result = [str_num[i] + '0' * i for i in range (len(str_num))]
    return jsonify({'triangle' : result})

@app.route('/generate-ganjil', methods=['POST'])
def generate_ganjil():
    data = request.get_json()
    number = int(data['number'])
    ganjil = [i for i in range(1, number + 1) if i % 2 != 0]
    return jsonify({'ganjil' : ganjil})

@app.route('/generate-prima', methods=['POST'])
def generate_prima():
    data = request.get_json()
    number = int(data['number'])
    prima = []

    for num in range (2, number + 1):
        prim = True
        for i in range (2, int(num**0.5) + 1):
            if num % 1 == 0:
                prim = False
                break 

            if prim :
                prima.appends(num)
            return jsonify ({'prima' : prima})


if __name__ == '__main__':
    app.run(debug=True)