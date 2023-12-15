# init Flask
from flask import Flask, render_template
app = Flask(__name__, static_url_path='/static')

# init AI
#from openai import OpenAI
#client = OpenAI()
#client = OpenAI(api_key="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")

# completion = client.chat.completions.create(
#  model="gpt-3.5-turbo",
#  messages=[
#    {"role": "system", "content": "You are a christmas tree on a dating site like Tinder"},
#    {"role": "user", "content": "Write your bio for a dating site like tinder, which includes your first name, age as a number, height as a number, hobbies, tree type. make it short, each information on a separate line, use emojis before each title"}
#  ]
# )

# print(completion.choices[0].message.content)



@app.route('/')
def home():

    # return "Hello Timberrrr"

    page = render_template("Home.html", tree = "StromZivotaa")

    return page

@app.route('/about')
def about():
    return 'About'