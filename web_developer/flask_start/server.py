from flask import Flask
import random

app = Flask(__name__)

my_number = random.randint(0, 9)


@app.route('/')
def hello():
    return '<h1 align="center">Guess a number between 0 and 9</h1>' \
           '<div align="center"><iframe src="https://giphy.com/embed/gT9BPNXovhAs0" width="420" height="480" ' \
           'frameBorder="0"class="giphy-embed"allowFullScreen></div>'


@app.route("/<int:guess>")
def guess_number(guess):
    if guess > my_number:
        return "<h1 align='center''>Too high, try again!</h1>" \
               "<img src='https://media.giphy.com/media/3o6ZtaO9BZHcOjmErm/giphy.gif'/>"
    elif guess < my_number:
        return "<h1 align='center'>Too low, try again!</h1>" \
               "<img src='https://media.giphy.com/media/jD4DwBtqPXRXa/giphy.gif'/>"
    else:
        return "<h1 align='center'>You found me!</h1>" \
               "<img src='https://media.giphy.com/media/4T7e4DmcrP9du/giphy.gif'/>"


if __name__ == "__main__":
    print(my_number)
    app.run()
