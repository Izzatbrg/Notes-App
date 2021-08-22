from flask import Flask,jsonify
from flask_restful import Api, request, Resource, abort 
import json
from DB import DB

app = Flask(__name__)
api = Api(app)
class Notes(Resource):
    def __init__(self):
        self.__tablename = 'notes'
        self.db = DB()

    def post(self):
        # get request data as Jason
        title = request.form.get('title')
        text = request.form.get('text')
        resp = self.db.insert_note(self.__tablename,title, text)
        if resp == 400:
            abort(400, message="A problem acquired")
        else: return resp
    
    def get(self):
        resp = self.db.get_all_notes()
        if resp == 400:
            abort(400, message="A problem acquired")
        else: return resp
        

api.add_resource(Notes, '/notes')


if __name__ == '__main__':
    app.run(debug=False)
