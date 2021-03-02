from application import app
from flask import request, jsonify
from logic import HTMLTarget, SMSTarget

@app.route("/")
@app.route("/index")
@app.route("/home")
def index():
    return 'test'


@app.route("/api", methods=['POST'])
def message_handler():
    if request.is_json:
        receivers = request.json['recievers']
        message = request.json['message']
        wrong_receivers = []
        errors = []
        for receiver in receivers:
            rec_name = receiver.get('name')
            if rec_name == 'HTML':
                rec = HTMLTarget(message, receiver.get('params'))
            elif rec_name == 'SMS':
                rec = SMSTarget(message, receiver.get('params'))
            else:
                wrong_receivers.append(rec_name)
            result = rec.process_message()
            if result:
                errors.append(result)
        if not errors and not wrong_receivers:
            return jsonify(message='Success'), 200
        return jsonify(message='Something went wrong', wrong_receivers=wrong_receivers,
                       errors=errors), 405

    return jsonify(message='Wrong method'), 405


