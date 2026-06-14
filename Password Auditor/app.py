from flask import Flask, render_template, request
from modules.strength import check_strength
from modules.entropy import calculate_entropy
from modules.dictionary_check import dictionary_check

app = Flask(__name__)

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/analyze', methods=['POST'])
def analyze():
    password = request.form['password']

    strength = check_strength(password)
    entropy = calculate_entropy(password)
    dictionary = dictionary_check(password)

    return render_template(
        'result.html',
        password=password,
        strength=strength,
        entropy=entropy,
        dictionary=dictionary
    )

if __name__ == '__main__':
    app.run(debug=True)