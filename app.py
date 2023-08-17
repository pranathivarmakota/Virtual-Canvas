
from flask import Flask , request, render_template
from aircanva import air_canva
app = Flask(__name__)

@app.route('/',methods=['GET','POST'])
def index():
	return render_template('index.html')
@app.route('/input',methods = ['GET','POST'])
def indput():
	air_canva()
	return render_template('input-pagec.html')
if __name__ == '__main__':
    app.run(debug = False)