import json
import random

quotes = [
  "Cloud computing is the future, and you are building it!",
  "Every 'Access Denied' is just a step closer to '200 OK'.",
  "Your code is like a cloud: floating, powerful, and slightly mysterious.",
  "Don't worry if it doesn't work; if it did, you'd be out of a job!"
]

def lambda_handler(event, context):    
    
  message = random.choice(quotes)
    
  return {
    'statusCode': 200,
    'body': json.dumps({'quote': message})
  }
