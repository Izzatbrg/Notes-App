from flask import Flask, render_template, request
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
from flask import jsonify

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] =     """postgresql://postgres:n3w0bj{1}@localhost:5432/Notes"""
db = SQLAlchemy(app)
migrate = Migrate(app, db)

class Note(db.Model):
    __tablename__ = "Notes"
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(), nullable=False)
    text = db.Column(db.String(), nullable=False)

    def __init__(self, title, text):
        self.title = title
        self.text = text
    
    def __repr__(self):
        return f"<Note{self.title}>"


@app.route('/Notes', methods=['POST','GET'])
def handle_notes():
    if request.method == 'POST':
        try:
            data = request.get_json(force=True)
            new_notes = Note(title = data["title"], text = data["text"])
            db.session.add(new_notes)
            db.session.commit()
            return {"message": "a new notes has been created successfully"}, 201
        except :
            return {"error":"The inserted data is not in Json format"}, 400
    elif request.method == 'GET':
        Notes =  Note.query.all()
        results = [{
            "title": Note.title,
            "text" : Note.text
        } for Note in Notes]
        return {"count": len(results), "Notes": results}



if __name__ == '__main__':
    app.run(debug=True)