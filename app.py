from flask import Flask, render_template, request, jsonify
from graph import setup_graph
import uuid

app = Flask(__name__)
graph = setup_graph()
thread_id = str(uuid.uuid4())
config = {
    "configurable": {
        "thread_id": thread_id,
    }
}


# Serve the chatbot UI
@app.route('/')
def index():
    return render_template('index.html')


# Chatbot API route to handle queries
@app.route('/chat', methods=['POST'])
def chat():
    user_query = request.json.get('query')

    # Process the query through the graph
    result = graph.invoke({"messages": ("user", user_query)}, config)
    response = result['messages'][-1].content
    return jsonify({"response": response})


if __name__ == '__main__':
    app.run(debug=True)
