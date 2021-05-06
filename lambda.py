import requests

def handler(event, context):
    response = requests.get("https://jsonplaceholder.typicode.com/todos/1")
    res = {
        "event": event,
        "output": response.json(),
        "context": context
    }
    print(res)

    return None
