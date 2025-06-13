# Using Python in AWS Lambda: Web APIs and HTTP Calls

AWS Lambda is a serverless compute service that lets you run Python code in response to events, including HTTP requests via API Gateway. This lecture covers how to write Lambda functions in Python, handle web calls, and best practices for deployment.

## Basic Lambda Function

A minimal Lambda handler receives `event` and `context` arguments:

```python
def lambda_handler(event, context):
    return {
        'statusCode': 200,
        'body': 'Hello from Lambda!'
    }
```

## Deploying with AWS Console

1. Go to AWS Lambda > Create function > Author from scratch.
2. Choose Python 3.x runtime.
3. Paste your code and click Deploy.

## Integrating with API Gateway (HTTP Trigger)

- Create an API Gateway REST API or HTTP API.
- Connect it to your Lambda function.
- API Gateway will pass HTTP request data in the `event` parameter.

## Handling Query and Path Parameters

```python
def lambda_handler(event, context):
    # For API Gateway REST API
    name = event['queryStringParameters'].get('name', 'World')
    return {
        'statusCode': 200,
        'body': f'Hello, {name}!'
    }
```

## Handling JSON Request Body (POST)

```python
import json
def lambda_handler(event, context):
    body = json.loads(event['body'])
    value = body.get('value')
    return {
        'statusCode': 200,
        'body': json.dumps({'received': value})
    }
```

## Returning Custom Headers

```python
def lambda_handler(event, context):
    return {
        'statusCode': 200,
        'headers': {'X-Custom-Header': 'Value'},
        'body': 'Headers set!'
    }
```

## Making Outbound HTTP Calls

Use `requests` or `httpx` (must be included in your deployment package):

```python
import requests
def lambda_handler(event, context):
    r = requests.get('https://api.github.com')
    return {
        'statusCode': 200,
        'body': r.text
    }
```

## Packaging Dependencies

- For external libraries, zip your code and `site-packages` folder, or use AWS Lambda Layers.
- Example with pip:
  ```cmd
  pip install requests -t ./package
  cd package
  zip -r ../lambda.zip .
  cd ..
  zip -g lambda.zip lambda_function.py
  ```

## Best Practices

- Keep handler functions fast (short timeouts)
- Use environment variables for config
- Log with `print()` or `logging`
- Use AWS IAM roles for secure access to AWS resources

## Example: Full Lambda for API Gateway

```python
import json
def lambda_handler(event, context):
    method = event['httpMethod']
    if method == 'GET':
        return {'statusCode': 200, 'body': json.dumps({'msg': 'GET received'})}
    elif method == 'POST':
        data = json.loads(event['body'])
        return {'statusCode': 200, 'body': json.dumps({'received': data})}
    else:
        return {'statusCode': 405, 'body': 'Method Not Allowed'}
```

See AWS docs for more: https://docs.aws.amazon.com/lambda/latest/dg/lambda-python.html
