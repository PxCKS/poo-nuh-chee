import mysql.connector
from flask import Flask, render_template, request, url_for, redirect
from config import config

app = Flask(__name__)


@app.route('/', methods=['GET', 'POST'])
def home():

    content = request.form.get('content')

    if content:
        conn = mysql.connector.connect(**config)

        cursor = conn.cursor()

        query = "INSERT INTO POSTS (post_content) VALUES (%s)"

        cursor.execute(query, (content,))

        conn.commit()
        conn.close()

        return redirect(url_for('home'))

    return render_template('index.html')


if __name__ == '__main__':
    app.run(debug=True)
