from flask import Flask, jsonify, request
app = Flask(__name__)

todos = [
    { "label": "Walk dog", "done": False },
]

@app.route('/todos', methods=['GET'])
def hello_world():
    json_text = jsonify(todos)
    return json_text

@app.route('/todos', methods=['POST'])
def add_new_todo():
    request_body = request.json 
    if request_body is None:
        return "Please send valid todo", 400
    print("Incoming request with the following body", request_body) 
    todos.append(request_body)
    return jsonify(todos)


@app.route('/todos/<int:index>', methods=['DELETE'])
def delete_todo(index):
    request_body = request.json 
    if request_body is None:
        return "Please send valid todo", 400
    counter=0
    for todo in todos: 
        if counter == index:
            todos.remove(todo)
        counter=counter+1
    print("Incoming request with the following body", request_body) 

    return jsonify(todos)

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=3245, debug=True)