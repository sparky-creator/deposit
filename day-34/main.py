import requests
import pandas as pd


parameters ={
    "amount": 10,
    "type": "boolean"

}

question_response = requests.get(url="https://opentdb.com/api.php", params=parameters)
question_response.raise_for_status()

df = pd.DataFrame.from_dict(question_response.json())

data = question_response.json()
print(data["results"])

#question_data = [ value for value in data]

#print(question_data)

