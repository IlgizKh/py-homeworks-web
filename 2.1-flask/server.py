import flask
from flask import jsonify, request
from flask.views import MethodView
from sqlalchemy.exc import IntegrityError

from models import Session, Adv

app = flask.Flask("app")

class HttpError(Exception):
    def __init__(self, status_code, message):
        self.status_code = status_code
        self.message = message



class AdvView(MethodView):

    def get(self, adv_id: int):
        adv = request.session.query(Adv).get(adv_id)
        if adv is None:
            raise HttpError(status_code=404, message="adv doesn't exist")
        return user

    def post(self):
        adv_data = request.json
        with Session() as session:
          adv = Adv(name=adv_data["name"], owner=adv_data["owner"], description=adv_data["description"])
          session.add(adv)
          session.commit()
          return jsonify(adv.dict)

        pass

    def delete(self, adv_id: int):
        adv = request.session.query(Adv).get(adv_id)
        request.session.delete(adv)
        request.session.commit()
        return jsonify({"status": "deleted"})


adv_view = AdvView.as_view("adv")
app.add_url_rule("/adv/", methods=["POST"], view_func=adv_view)
app.add_url_rule(
    "/adv/<int:adv_id>/", methods=["GET", "DELETE"], view_func=adv_view
)

app.run(port=8080)
