from flask import Flask
from blueprints.basic_endpints import blueprint as basic_endpoints
import wa_chatbot as chat

app = Flask(__name__)
# app.register_blueprint(basic_endpoints)

@app.route('/wa_chatbot')
def wa_chatbot():
    chat.main()
    return 'chat'


if __name__ == "__main__":
    app.run()

