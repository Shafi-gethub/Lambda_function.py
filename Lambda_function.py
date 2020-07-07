import json

print('Loading function')
print('Besic lambda function')


def lambda_handler(event, context):
    #print("Received event: " + json.dumps(event, indent=2))
   return {" massage" : "Hello world " }
