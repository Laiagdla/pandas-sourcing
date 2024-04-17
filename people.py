#### Import and global variables
import pandas as pd
from fastapi import FastAPI
api = FastAPI()
 
#### Main block
def load_csv():
    people_df = pd.read_csv('data/people.csv', index_col='Id')
    return people_df 

@api.get("/")
def hello():
    return "Hi 😊"

@api.get("/search")
def search_people(name):
    people_df = load_csv()
    return people_df[people_df['FirstName'] == name]

@api.get("/searchlastname")
def search_people(name):
    people_df = load_csv()
    return people_df[people_df['LastName'] == name]
    
#### Entry point:
if __name__ == "__main__":
    print(hello())
    name = input('▶️ choose name:')
    print(search_people(name))