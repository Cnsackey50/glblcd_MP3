from flask import Flask, render_template
app = Flask(__name__)

@app.route('/')
def index():
    return "My is Christopher Nii Sackey, I was born on 22nd october,2000 . Reading is something I love doing."

@app.route('/whereami')
def whereami():
    return 'Ghana!'


@app.route('/g')
def indexg():
    return render_template('index.html')

@app.route('/thename/<name>')
def my_name(name):
    return render_template('myname.html', thename=name)

@app.route('/passion')
def hob():
    return render_template('passion.html')

if __name__ == '__main__':
    app.run(debug=True)