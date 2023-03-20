from flask import Flask,redirect,url_for,render_template,request

app=Flask(__name__)



@app.route('/',methods=['GET','POST'])
def home():
    if request.method=='POST':
        # Handle POST Request here
        return render_template('in.html')
    return render_template('index.html')


@app.route('/main',methods=['GET','POST'])
def main():
    if request.method=='POST':
        # Handle POST Request here
        return render_template('main.html')
    return render_template('main.html')

@app.route('/front',methods=['GET','POST'])
def front():
    if request.method=='POST':
        # Handle POST Request here
        return render_template('front.html')
    return render_template('front.html')

if __name__ == '__main__':
    #DEBUG is SET to TRUE. CHANGE FOR PROD
    app.run(port=5000,debug=True)