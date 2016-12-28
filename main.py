from flask import Flask, jsonify, render_template
from time import sleep
import json

app = Flask(__name__)


def get_courses(user_id):
	sleep(3)
	return [1, 2, 3]

def get_user(user_id):
	return { "name": "noah" }


@app.route('/courses/<user_id>')
def load_courses(user_id):
	return jsonify(get_courses(user_id))


@app.route('/user/<user_id>')
def load_user(user_id):
	return jsonify(get_user(user_id))


@app.route('/')
def get_home():
	return render_template('fast.html')


@app.route('/slow')
def nri_get_home():
	user = get_user(4)
	courses = get_courses(4)
	stuff = { "user": user,"courses": courses }
	return render_template('slow.html', stuff=json.dumps(stuff))

if __name__ == '__main__':
	app.run()