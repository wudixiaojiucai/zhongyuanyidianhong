from flask_sqlalchemy import SQLAlchemy
from flask_restful import Resource, Api
from flask import Flask, request, jsonify

app = Flask(__name__)
api = Api(app)
app.config["SQLALCHEMY_DATABASE_URI"] = "mysql+pymysql://root:123456@127.0.0.1:3306/flask?charset=utf8mb4"
app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = True
db = SQLAlchemy(app)


class TestCase(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(80), unique=False, nullable=True)
    description = db.Column(db.String(80), unique=False, nullable=True)
    steps = db.Column(db.String(120), unique=False, nullable=True)

    def __repr__(self):
        return '<User %r>' % self.description

    def to_json(self):
        """返回对象转json"""
        return {"id": self.id,
                "name": self.name,
                "description": self.description,
                "steps": self.steps}
        # dict = self.__dict__
        # if "_sa_instance_state" in dict:
        #     del dict["_sa_instance_state"]
        # return dict


class TestCaseServer(Resource):

    def get(self):
        if "id" in request.args:
            if db.session.query(TestCase.id == int(request.args["id"])) is not None:
                get_id = db.session.query(TestCase).filter(TestCase.id == int(request.args["id"])).all()
                for content in get_id:
                    return jsonify(content.to_json())
            return None
        else:
            result = []
            contents = db.session.query(TestCase).all()
            for all_content in contents:
                result.append(all_content.to_json())
            return result

    def post(self):
        data = request.json
        if "id" in data:
            print(request.json)
            db.session.add(TestCase(id=data.get("id"), name=data.get("name"), description=data.get("description"),
                                    steps=data.get("steps")))
            db.session.commit()
            return {"msg": "ok", "errcode": "0"}
        return {"errormsg": "need id", "errcode": "404"}


api.add_resource(TestCaseServer, '/testcase')
# 创建所有表
# db.create_all()
# db.session.add(TestCase(id=1, name="heihei", description="嘿嘿", steps="{'dd':'123'}"))
# db.session.commit()

if __name__ == "__main__":
    app.run(debug=True, host="0.0.0.0")
