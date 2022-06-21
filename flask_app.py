#from flask import Flask
from flask import Flask, jsonify, request
app=Flask(__name__)
data=[
    {
        'Contact':9987644456,
        'name':u'Raju',
        'done':False,
        'id':1
    },
    {
        'Contact':9876543222,
        'name':u'Rahul',
        'done':False,
        'id':2
    }
]
@app.route("/")
def hello_world():
    return "hello world"
@app.route("/add-data",methods=['POST'])

def add_task():
    if not request.json :
        return jsonify({'status':'error',
                        'message':'Please provide the data!'},400)
                        
    contact={
        'id':data[-1]['id']+1,
        'name':request.json['name'],
        'contact':request.json['contact'],
        'done':False
    }
    data.append(contact)
    return jsonify({'status':'success','data':contact})
@app.route("/get-data",methods=['GET'])

def get_data():
    return jsonify({'status':'success','data':data})
if(__name__=="__main__"):
    app.run(debug=True)
