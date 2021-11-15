from flask import Flask,render_template

app=Flask(__name__,static_folder='./templates/static/')


@app.route('/')
def index():
    return render_template('./index.html')


if __name__=='__main__':
    app.run(host='127.0.0.1',port=5001,debug=False)