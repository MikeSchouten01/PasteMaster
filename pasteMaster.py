from flask import Flask, render_template
app = Flask(__name__)

@app.route('/')
def home():
   return render_template('index.html')
if __name__ == '__main__':
   app.run()

@app.route('/start.html', methods=['GET'])
def start():
   return render_template('start.html')