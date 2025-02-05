"""Entry points for the application."""

import json
import logging
from typing import Dict, Union

logger = logging.getLogger()
logger.setLevel(logging.INFO)

def process(message: str) -> str:
    """Process message. The application logic is impleted here.
    Nothing to implement for the assessment.
    """
    return f"The received message is: '{message}'"

JSON = Dict[str, Union[int, str, float, 'JSON']]
LambdaEvent = JSON
LambdaContext = object
LambdaOutput = JSON

def extract_body(event: LambdaEvent) -> Dict:
    """Extracts and validates the body from the event."""
    body = event.get('body')
    if not body:
        error_msg = "Missing 'body' in request"
        raise ValueError(error_msg)

    return json.loads(body) if isinstance(body, str) else body

def extract_message(body: Dict) -> str:
    """Extracts and validates the 'message' field from the body."""
    message = body.get('message')
    if not message:
        error_msg = "Missing 'message' field in request body"
        raise ValueError(error_msg)

    return message

def lambda_handler(event: LambdaEvent, context: LambdaContext) -> LambdaOutput:  # noqa: ARG001
    """Entry point for Lambda function."""
    try:
        #1. Extract and validate the body
        body_json = extract_body(event)

        #2. Extract and validate the message
        message = extract_message(body_json)

        #3. Call the process function
        result = process(message)

        #4. Return the response in API Gateway format
        return {
            'statusCode': 200,
            'body': json.dumps({'message': result}),
        }

    except ValueError as e:
        logger.exception('Bad Request: %s')
        return {
            'statusCode': 400,
            'body': json.dumps({'error': str(e)}),
        }

    except Exception:
        logger.exception('Internal Server Error')
        return {
            'statusCode': 500,
            'body': json.dumps({'error': 'Internal Server Error'}),
        }
