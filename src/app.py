from flask import Flask, jsonify, request, json

app = Flask(__name__)


todos = [{
    "label": "My first task", "done": False
}]




@app.route ("/todos", methods = ["GET"])
def get_todo():
    json_text = jsonify(todos)
    return json_text


@app.route ("/todos", methods= ["POST"])
def post_todo():
    request_body = request.data
    decoded_object = json.loads(request_body)
    todos.append(decoded_object)
    return jsonify(todos)


@app.route ("/todos/<int:position>", methods= ["DELETE"])
def delete_todo(position):
    todos.pop(position)
    return jsonify(todos)



if __name__ == "__main__":
    app.run (host="127.0.0.1", port=8000, debug = True)
