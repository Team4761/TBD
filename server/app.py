#!/usr/bin/env
from flask import Flask
junaid = Flask(__name__)

from frontend import front
junaid.register_blueprint(front)

if __name__ == "__main__":
	junaid.run()
