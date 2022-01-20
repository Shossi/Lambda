import json


def handler(event, context):
    number1 = event['num1']
    number2 = event['num2']
    return int(number1) + int(number2)

