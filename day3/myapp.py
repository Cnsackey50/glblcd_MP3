from flask import Flask, render_template
app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/whereami')
def whereami():
    return 'Ghana!'

@app.route('/thename/<name>')
def my_name(name):
    return render_template('myname.html', thename=name)

@app.route('/passion')
def hob():
    return render_template('passion.html')
      
@app.route('/song')
def favsong():
    return render_template('favsong.html')

if __name__ == '__main__':
    app.run(debug=True)