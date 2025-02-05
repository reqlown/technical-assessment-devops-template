import json

from lambda_app.app import lambda_handler


def test_lambda_handler_valid_event():
    """Test lambda_handler with a valid input."""
    event = {'body': json.dumps({'message': 'Hello, Lambda!'})}
    response = lambda_handler(event, None)

    assert response['statusCode'] == 200
    assert json.loads(response['body'])['message'] == "The received message is: 'Hello, Lambda!'"


def test_lambda_handler_missing_body():
    """Test lambda_handler when the event body is missing."""
    event = {}
    response = lambda_handler(event, None)

    assert response['statusCode'] == 400
    assert json.loads(response['body'])['error'] == "Missing 'body' in request"


def test_lambda_handler_invalid_json():
    """Test lambda_handler when the body is not valid JSON."""
    event = {'body': 'invalid_json'}
    response = lambda_handler(event, None)

    assert response['statusCode'] == 400
    assert 'error' in json.loads(response['body'])


def test_lambda_handler_missing_message():
    """Test lambda_handler when the 'message' key is missing."""
    event = {'body': json.dumps({})}
    response = lambda_handler(event, None)

    assert response['statusCode'] == 400
    assert json.loads(response['body'])['error'] == "Missing 'message' field in request body"
