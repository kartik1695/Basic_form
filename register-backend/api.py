from flask import * 
from flask_cors import CORS, cross_origin
import json
import datetime

from functools import update_wrapper




app = Flask(__name__)
app.config["DEBUG"] = True
CORS(app, support_credentials=True)


@app.route('/get-data', methods=['GET'])
@cross_origin(supports_credentials=True)
def home():
    with open('data.json','r+') as file:
          # First we load existing data into a dict.
        file_data = json.load(file)
        
        return file_data

@app.route('/post-data' , methods=['POST'])
@cross_origin(supports_credentials=True)
def post_data():
    print(request.data)
    data = (request.data).decode("utf-8")
    json_data = json.loads(data)
    print("dasdas")
    print(json_data)
    created_at = datetime.datetime.now().strftime("%d-%m_%Y %H:%M")
    json_data['created_at'] = created_at
    write_json(json_data)
    response = jsonify(data)
    response.headers.add("Access-Control-Allow-Origin", "*")
    return (response)

def write_json(new_data, filename='data.json'):
    with open(filename,'r+') as file:
          # First we load existing data into a dict.
        file_data = json.load(file)
        print("file data")
        print(file_data)
        # Join new_dat3a with file_data
        file_data['data'].append(new_data)
        # file_data.update(new_data)
        # Sets file's current position at offset.
        file.seek(0)
        # convert back to json.
        json.dump(file_data, file, indent = 4)

app.run()

