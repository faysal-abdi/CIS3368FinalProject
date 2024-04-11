from flask import Flask, request
from flask_restful import Api, Resource
from passlib.hash import pbkdf2_sha256 as sha256
from database import connection

app = Flask(__name__)
api = Api(app)


class FacilityResource(Resource):
    def get(self, facility_id):
        cursor = connection.cursor(dictionary=True)
        query = "SELECT * FROM Facility WHERE id = %s"
        cursor.execute(query, (facility_id,))
        facility = cursor.fetchone()

        if not facility:
            cursor.close()
            return {'message': 'Facility not found'}, 404

        cursor.close()
        return {'id': facility['id'], 'name': facility['name']}, 200


class ClassroomResource(Resource):
    def get(self, classroom_id):
        cursor = connection.cursor(dictionary=True)
        query = "SELECT * FROM Classroom WHERE id = %s"
        cursor.execute(query, (classroom_id,))
        classroom = cursor.fetchone()

        if not classroom:
            cursor.close()
            return {'message': 'Classroom not found'}, 404

        cursor.close()
        return {'id': classroom['id'], 'name': classroom['name']}, 200


class TeacherResource(Resource):
    def get(self, teacher_id):
        cursor = connection.cursor(dictionary=True)
        query = "SELECT * FROM Teacher WHERE id = %s"
        cursor.execute(query, (teacher_id,))
        teacher = cursor.fetchone()

        if not teacher:
            cursor.close()
            return {'message': 'Teacher not found'}, 404

        cursor.close()
        return {'id': teacher['id'], 'name': teacher['name']}, 200


class ChildResource(Resource):
    def get(self, child_id):
        cursor = connection.cursor(dictionary=True)
        query = "SELECT * FROM Child WHERE id = %s"
        cursor.execute(query, (child_id,))
        child = cursor.fetchone()

        if not child:
            cursor.close()
            return {'message': 'Child not found'}, 404

        cursor.close()
        return {'id': child['id'], 'name': child['name']}, 200


class LoginResource(Resource):
    def post(self):
        username = request.form['John']
        password = request.form['Smith']

        if username == 'John' and password == 'Smith':
            return {'message': 'Login successful'}, 200
        else:
            return {'message': 'Invalid credentials'}, 401


api.add_resource(FacilityResource, '/facilities/<int:facility_id>')
api.add_resource(ClassroomResource, '/classrooms/<int:classroom_id>')
api.add_resource(TeacherResource, '/teachers/<int:teacher_id>')
api.add_resource(ChildResource, '/children/<int:child_id>')
api.add_resource(LoginResource, '/login')

if __name__ == '__main__':
    app.run(debug=True)