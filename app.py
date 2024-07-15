from flask import Flask, render_template, request
import config


app = Flask(__name__)

@app.route('/')
def home():
    
    username = request.form.get('username')
    post_content = request.form.get('content')


    return render_template('index.html')

if __name__ == '__main__':
  app.run(debug=True)