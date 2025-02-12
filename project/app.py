from flask import Flask, request, render_template

app = Flask(__name__)

@app.route('/', methods=['GET', 'POST'])
def index():
    if request.method == 'POST':
        user_input = request.form['textfield']
        return f"You entered: {user_input}"
    return render_template('index.html')

if __name__ == '__main__':
    app.run(debug=True)
