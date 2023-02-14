from flask import Flask, render_template, request
import openai
openai.api_key = ""

# Use the ChatGPT model to generate a response to the prompt
app = Flask(__name__)
@app.route("/chatbot")
def home():
    return render_template("index.html")

# Using a global variable to switch between models
models = ["text-davinci-003", "code-davinci-002"]
model = models[0]
@app.route("/get")
def get_bot_response():
    prompt = request.args.get('msg')
    if(prompt == "/switch"):
        # use a ternary operator to switch between models
        global model
        model = models[1] if model == models[0] else models[0]

        return "Switched to " + model
    if(model == 'code-davinci-002'):
        prompt += ". The output should be formatted in a way that can be rendered in HTML."
    response = openai.Completion.create(
        model=model,
        prompt=prompt,
        temperature=0.5,
        max_tokens=250,
        top_p=1,
        frequency_penalty=0,
        presence_penalty=0,
    )
    # convert response to html format and return it
    response_html = response["choices"][0]["text"]
    return response_html
app.run(debug = True)