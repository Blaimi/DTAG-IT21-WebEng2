import json

from flask import Response


def create_response(data_dict, status=200):
    response_body = json.dumps(
        data_dict,
        indent=4,
        separators=(',', ': ')
    )
    return Response(response_body, status=status, mimetype="application/json")


def error_response(message, more_info, status=400):
    code = {
        400: "bad_request",
        401: "unauthorized",
        404: "not_found"
    }

    response_body = {

        "errors": [
            {
                "code": code[status],
                "message": message,
                "more_info": more_info
            }
        ]
    }
    return create_response(response_body, status=status)
