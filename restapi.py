from flask import Flask, request, jsonify
from flask_restful import Api, Resource
from passlib.hash import pbkdf2_sha256 as sha256
from database import connection

app = Flask(__name__)
api = Api(app)

# Dummy data for testing
facilities = []
classrooms = []
teachers = []
children = []

# Login API
@app.route('/login', methods=['POST'])
def login():
    username = request.json['username']
    password = request.json['password']
    
    # Perform authentication logic here
    # You can compare the provided username and password with pre-configured values
    
    # Return a response indicating successful login
    return jsonify({'message': 'Logged in successfully'})

# Facilities API
@app.route('/facilities', methods=['GET'])
def get_facilities():
    return jsonify(facilities)

@app.route('/facilities', methods=['POST'])
def create_facility():
    data = request.json
    facility = {
        'id': len(facilities) + 1,
        'name': data['name']
    }
    facilities.append(facility)
    return jsonify(facility), 201

@app.route('/facilities/<int:facility_id>', methods=['PUT'])
def update_facility(facility_id):
    data = request.json
    facility = next((f for f in facilities if f['id'] == facility_id), None)
    if facility:
        facility['name'] = data['name']
        return jsonify(facility)
    else:
        return jsonify({'message': 'Facility not found'}), 404

@app.route('/facilities/<int:facility_id>', methods=['DELETE'])
def delete_facility(facility_id):
    facility = next((f for f in facilities if f['id'] == facility_id), None)
    if facility:
        facilities.remove(facility)
        return jsonify({'message': 'Facility deleted'})
    else:
        return jsonify({'message': 'Facility not found'}), 404

# Classrooms API
@app.route('/classrooms', methods=['GET'])
def get_classrooms():
    return jsonify(classrooms)

@app.route('/classrooms', methods=['POST'])
def create_classroom():
    data = request.json
    classroom = {
        'id': len(classrooms) + 1,
        'name': data['name'],
        'capacity': data['capacity'],
        'facility': data['facility']
    }
    classrooms.append(classroom)
    return jsonify(classroom), 201

@app.route('/classrooms/<int:classroom_id>', methods=['PUT'])
def update_classroom(classroom_id):
    data = request.json
    classroom = next((c for c in classrooms if c['id'] == classroom_id), None)
    if classroom:
        classroom['name'] = data['name']
        classroom['capacity'] = data['capacity']
        classroom['facility'] = data['facility']
        return jsonify(classroom)
    else:
        return jsonify({'message': 'Classroom not found'}), 404

@app.route('/classrooms/<int:classroom_id>', methods=['DELETE'])
def delete_classroom(classroom_id):
    classroom = next((c for c in classrooms if c['id'] == classroom_id), None)
    if classroom:
        classrooms.remove(classroom)
        return jsonify({'message': 'Classroom deleted'})
    else:
        return jsonify({'message': 'Classroom not found'}), 404

# Teachers API
@app.route('/teachers', methods=['GET'])
def get_teachers():
    return jsonify(teachers)

@app.route('/teachers', methods=['POST'])
def create_teacher():
    data = request.json
    teacher = {
        'id': len(teachers) + 1,
        'firstname': data['firstname'],
        'lastname': data['lastname'],
        'room': data['room']
    }
    teachers.append(teacher)
    return jsonify(teacher), 201

@app.route('/teachers/<int:teacher_id>', methods=['PUT'])
def update_teacher(teacher_id):
    data = request.json
    teacher = next((t for t in teachers if t['id'] == teacher_id), None)
    if teacher:
        teacher['firstname'] = data['firstname']
        teacher['lastname'] = data['lastname']
        teacher['room'] = data['room']
        return jsonify(teacher)
    else:
        return jsonify({'message': 'Teacher not found'}), 404

@app.route('/teachers/<int:teacher_id>', methods=['DELETE'])
def delete_teacher(teacher_id):
    teacher = next((t for t in teachers if t['id'] == teacher_id), None)
    if teacher:
        teachers.remove(teacher)
        return jsonify({'message': 'Teacher deleted'})
    else:
        return jsonify({'message': 'Teacher not found'}), 404


@app.route('/children', methods=['GET'])
def get_children():
    return jsonify(children)

@app.route('/children', methods=['POST'])
def create_child():
    data = request.json
    child = {
        'id': len(children) + 1,
        'firstname': data['firstname'],
        'lastname': data['lastname'],
        'age': data['age'],
        'classroom': data['classroom']
    }
    children.append(child)
    return jsonify(child), 201

@app.route('/children/<int:child_id>', methods=['PUT'])
def update_child(child_id):
    data = request.json
    child = next((c for c in children if c['id'] == child_id), None)
    if child:
        child['firstname'] = data['firstname']
        child['lastname'] = data['lastname']
        child['age'] = data['age']
        child['classroom'] = data['classroom']
        return jsonify(child)
    else:
        return jsonify({'message': 'Child not found'}), 404

@app.route('/children/<int:child_id>', methods=['DELETE'])
def delete_child(child_id):
    child = next((c for c in children if c['id'] == child_id), None)
    if child:
        children.remove(child)
        return jsonify({'message': 'Child deleted'})
    else:
        return jsonify({'message': 'Child not found'}), 404

if __name__ == '__main__':
    app.run(debug=True)
