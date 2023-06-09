from flask import Flask,redirect,url_for,render_template,request

app=Flask(__name__)





@app.route('/',methods=['GET','POST'])
def homepage():
   
    return render_template('homepage.html')

@app.route('/login',methods=['GET','POST'])
def login():
    if request.method=='POST':
        # Handle POST Request here
        return render_template('login.html')
    return render_template('login.html')

@app.route('/sigin',methods=['GET','POST'])
def sigin():
    if request.method=='POST':
        # Handle POST Request here
        return render_template('sigin.html')
    return render_template('sigin.html')



@app.route('/main',methods=['GET','POST'])
def main():
    if request.method=='POST':
        # Handle POST Request here
        return render_template('main.html')
    return render_template('main.html')

@app.route('/give',methods=['GET','POST'])
def give():
    if request.method=='POST':
        # Handle POST Request here
        return render_template('give.html')
    return render_template('give.html')

@app.route('/whoops',methods=['GET','POST'])
def whoops():
    if request.method=='POST':
        # Handle POST Request here
        return render_template('whoops.html')
    return render_template('whoops.html')




@app.route('/ministry',methods=['GET','POST'])
def ministry():
    if request.method=='POST':
        # Handle POST Request here
        return render_template('ministry.html')
    return render_template('ministry.html')

if __name__ == '__main__':
    #DEBUG is SET to TRUE. CHANGE FOR PROD
    app.run(host='0.0.0.0', port=5000,debug=True)