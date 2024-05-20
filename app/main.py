from flask import Flask, request, jsonify
from app.models import add_entity, get_entity, get_all_entities

app = Flask(__name__)

@app.route('/entities/<entity_type>' , methods=['POST'])
def create_entity(entity_type):
    entity_data = request.get_json()
    entity_id = add_entity(entity_type, entity_data)
    response = {'id': entity_id}
    return jsonify(response), 201

@app.route('/entities/<entity_type>' , methods=['GET'])
def get_all_entities(entity_type):
    entities = get_all_entities(entity_type)
    response = {'entities': [entity for entity in entities]}
    return  jsonify(response), 200