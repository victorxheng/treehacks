from openai import OpenAI
import sys

import shutil
import os

client = OpenAI(api_key = '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')

path_name = input("Type in directory of the .vly file to process without the extension\n")

file = open(path_name+".vly", "r")

if file is None:
    sys.exit("file empty, abort")

prompt = file.read()

# duplicates the starter code
shutil.copytree("stack", 'generated/'+path_name)

# make sure API key is set correctly
# agent starts by writing the database schema
response = client.chat.completions.create(
  model="gpt-4-0125-preview",
  messages=[
    {"role": "system", "content": "You are a helpful assistant."},
    {"role": "user", "content": prompt.split('[PAGES]')[0]},
  ]
)

# edit the db_model.py file from the path with the response


# replace and then start writing the stack

# initialize and deploy