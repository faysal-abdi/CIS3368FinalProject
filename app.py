from flask import Flask, render_template, request, jsonify

app = Flask(__name__)

facilities = []
classrooms = []
teachers = []
children = []

# Login page
@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        username = request.form['username']
        password = request.form['password']

        return jsonify({'message': 'Logged in successfully'})
    
    return render_template('login.html')

# Facilities page
@app.route('/facilities', methods=['GET', 'POST'])
def facilities_page():
    if request.method == 'POST':
        data = request.form
        facility = {
            'id': len(facilities) + 1,
            'name': data['name']
        }
        facilities.append(facility)
        return jsonify(facility), 201
    
    return render_template('facilities.html', facilities=facilities)

@app.route('/facilities/<int:facility_id>', methods=['PUT', 'DELETE'])
def facility_details(facility_id):
    facility = next((f for f in facilities if f['id'] == facility_id), None)
    if facility:
        if request.method == 'PUT':
            data = request.form
            facility['name'] = data['name']
            return jsonify(facility)
        elif request.method == 'DELETE':
            facilities.remove(facility)
            return jsonify({'message': 'Facility deleted'})
    else:
        return jsonify({'message': 'Facility not found'}), 404

# Classrooms page
@app.route('/classrooms', methods=['GET', 'POST'])
def classrooms_page():
    if request.method == 'POST':
        data = request.form
        classroom = {
            'id': len(classrooms) + 1,
            'name': data['name'],
            'capacity': data['capacity'],
            'facility': data['facility']
        }
        classrooms.append(classroom)
        return jsonify(classroom), 201
    
    return render_template('classrooms.html', classrooms=classrooms)

@app.route('/classrooms/<int:classroom_id>', methods=['PUT', 'DELETE'])
def classroom_details(classroom_id):
    classroom = next((c for c in classrooms if c['id'] == classroom_id), None)
    if classroom:
        if request.method == 'PUT':
            data = request.form
            classroom['name'] = data['name']
            classroom['capacity'] = data['capacity']
            classroom['facility'] = data['facility']
            return jsonify(classroom)
        elif request.method == 'DELETE':
            classrooms.remove(classroom)
            return jsonify({'message': 'Classroom deleted'})
    else:
        return jsonify({'message': 'Classroom not found'}), 404

# Teachers page
@app.route('/teachers', methods=['GET', 'POST'])
def teachers_page():
    if request.method == 'POST':
        data = request.form
        teacher = {
            'id': len(teachers) + 1,
            'firstname': data['firstname'],
            'lastname': data['lastname'],
            'room': data['room']
        }
        teachers.append(teacher)
        return jsonify(teacher), 201
    
    return render_template('teachers.html', teachers=teachers)

@app.route('/teachers/<int:teacher_id>', methods=['PUT', 'DELETE'])
def teacher_details(teacher_id):
    teacher = next((t for t in teachers if t['id'] == teacher_id), None)
    if teacher:
        if request.method == 'PUT':
            data = request.form
            teacher['firstname'] = data['firstname']
            teacher['lastname'] = data['lastname']
            teacher['room'] = data['room']
            return jsonify(teacher)
        elif request.method == 'DELETE':
            teachers.remove(teacher)
            return jsonify({'message': 'Teacher deleted'})
    else:
       return jsonify({'message': 'Teacher not found'}), 404

# Children page
@app.route('/children', methods=['GET', 'POST'])
def children_page():
    if request.method == 'POST':
        data = request.form
        child = {
            'id': len(children) + 1,
            'firstname': data['firstname'],
            'lastname': data['lastname'],
            'age': data['age'],
            'classroom': data['classroom']
        }
        children.append(child)
        return jsonify(child), 201
    
    return render_template('children.html', children=children)

@app.route('/children/<int:child_id>', methods=['PUT', 'DELETE'])
def child_details(child_id):
    child = next((c for c in children if c['id'] == child_id), None)
    if child:
        if request.method == 'PUT':
            data = request.form
            child['firstname'] = data['firstname']
            child['lastname'] = data['lastname']
            child['age'] = data['age']
            child['classroom'] = data['classroom']
            return jsonify(child)
        elif request.method == 'DELETE':
            children.remove(child)
            return jsonify({'message': 'Child deleted'})
    else:
        return jsonify({'message': 'Child not found'}), 404

if __name__ == '__main__':
    app.run(debug=True)