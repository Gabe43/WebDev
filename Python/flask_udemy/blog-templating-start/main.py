from flask import Flask, render_template
from post import Post

app = Flask(__name__)

@app.route('/vlog')
def blog_post():
    pst = Post()
    data = pst.get_blog()
    return render_template('index.html',dat = data)

@app.route('/vlogid/<int:num>')
def get_vlog(num):
    pst = Post()
    id = pst.get_blog()
    nm = num
    return render_template('vlog.html',number=nm,vlg=id)
if __name__ == "__main__":
    app.run(debug=True)
