from app import app, json, Response
def user_dto(status, data, message=False):
    body = {"data": data}
    if message:
        body["message"] = message

    return Response(json.dumps(body), status=status, mimetype="application/json")
