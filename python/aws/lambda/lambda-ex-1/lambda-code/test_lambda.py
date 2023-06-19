import json

def lambda_handler(event, context):
    # Extract information from the event
    name = event.get('name', 'Anonymous')

    # Create a response payload
    response = {
        'message': f'Hello, {name}!'
    }

    # Return the response
    return {
        'statusCode': 200,
        'body': json.dumps(response)
    }