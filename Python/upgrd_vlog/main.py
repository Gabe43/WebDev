from flask import Flask, flash, render_template, request
import requests,smtplib
app = Flask(__name__)
app.secret_key = b'_5#y2L"F4Q8z\n\xec]/'

url = 'https://api.npoint.io/c790b4d5cab58020d391'
response = requests.get(url=url)
data = response.json()


@app.route('/')
def get_all_posts():
    return render_template("index.html", dat=data)


@app.route('/about')
def abt():
    return render_template('about.html')


@app.route('/contact')
def cntct():
    return render_template('contact.html')


@app.route('/post/<int:index>')
def post_root(index):
    post = None
    nm = index
    for itm in data:
        if itm['id'] == nm:
            post = itm
    return render_template('post.html', id=post)


@app.route('/contact', methods=['GET', 'POST'])
def receive_data():
    if request.method == 'POST':
        name = request.form['fname']
        email = request.form['fmail']
        number = request.form['fnum']
        messg = request.form['fmsg']
        mail = 'gabrieljesus7616@gmail.com'
        password = 'abcd@1234'
        with smtplib.SMTP('smtp.gmail.com') as connection:
            connection.starttls()
            connection.login(user=mail,password=password)
            connection.sendmail(from_addr=mail,to_addrs='saptarshiabhi21@gmail.com',msg=f'Subject : New Message\n\nName : {name}\nEmail : {email}\nContact No : {number}\nMessage : {messg}')
        return render_template('contact.html',msg_sent=True)

    return render_template('contact.html',msg_sent=False)


if __name__ == "__main__":
    app.run(debug=True)
