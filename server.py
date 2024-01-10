from flask import Flask, render_template, request, redirect
import csv

app = Flask(__name__)


@app.route("/")
def home():
    return render_template('index.html')


# @app.route("/index.html")
# def my_home():
#     return render_template('index.html')
#
#
# @app.route("/works.html")
# def my_work():
#     return render_template('works.html')
#
#
# @app.route("/about.html")
# def about_me():
#     return render_template('about.html')
#
#
# @app.route("/contact.html")
# def contact_me():
#     return render_template('contact.html')

# Instead of doing this repeatedly, we can do this dynamically:
@app.route("/<string:page_name>")
def html_page(page_name):
    return render_template(page_name)


# Plain text file:
# def write_to_file(data):
#     with open('database.txt', 'a') as database:
#         email = data['email']
#         subject = data['subject']
#         message = data['message']
#         file = database.write(f'\nEmail: {email}, Subject: {subject}, Message: {message}')


# Excel file:
def write_to_csv(data):
    with open('database.csv', 'a', newline='') as database2:
        email = data['email']
        subject = data['subject']
        message = data['message']
        csv_writer = csv.writer(database2, delimiter=',', quotechar='"', quoting=csv.QUOTE_MINIMAL)
        csv_writer.writerow([email, subject, message])


@app.route('/submit_form', methods=['POST', 'GET'])
def submit_form():
    if request.method == 'POST':
        try:
            data = request.form.to_dict()
            write_to_csv(data)
            return redirect('/thankyou.html')
        except:
            return 'Did not saved to database'
    else:
        return 'Oops! Something went wrong'
