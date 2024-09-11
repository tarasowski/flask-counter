from flask import Flask, render_template, redirect, url_for

app = Flask(__name__)

# Initialize counter
counter = {'value': 0}


@app.route('/')
def index():
    return render_template('index.html', counter=counter)


@app.route('/increment')
def increment():
    counter['value'] += 1
    return redirect(url_for('index'))

# decorators 👇
@app.route('/decrement')
def decrement():
    counter['value'] -= 1
    return redirect(url_for('index'))


if __name__ == '__main__':
    app.run(debug=True)
