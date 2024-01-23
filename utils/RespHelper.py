from flask import jsonify


class RespHelper:

    def jsonResp(message, data, status):
        return jsonify({
            "status": status,
            "message": message,
            "data": data
        })
