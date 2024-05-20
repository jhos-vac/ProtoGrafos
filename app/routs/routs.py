from flask import Flask, request, jsonify
from app.models.models import  Neo4jModel

app = Flask(__name__)
model = Neo4jModel()

@app.route('/entities/<entity_type>' , methods=['POST'])
def create_entity(entity_type):
    entity_data = request.get_json()
    entity_id = model.add_entity(entity_type, entity_data)
    response = {'id': entity_id}
    return jsonify(response), 201

@app.route('/entities/<entity_type>' , methods=['GET'])
def get_all_entities(entity_type):
    entities = model.get_all_entities(entity_type)
    response = {'entities': [entity for entity in entities]}
    return  jsonify(response), 200

@app.route('/entities/<entity_type>/<entity_id>' , methods=['GET'])
def get_entity(entity_type, entity_id):
    entity = model.get_entity(entity_type, entity_id)
    if entity:
        return jsonify(entity), 200
    else:
        return jsonify({'error': 'Entity not found'}), 404
