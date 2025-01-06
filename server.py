from flask import Flask, request, render_template

app = Flask(__name__)

@app.route('/')
def home_page():
   return render_template('index.html', first_name='Ryan')

@app.route('/about')
def about_page():
   return render_template('about.html')

@app.route('/contact')
def contact_page():
   return render_template('contact.html')

@app.route('/form')
def form_page():
   return render_template('form-page.html')

@app.post('/create-account')
def create_account():
   return 'Successfully created account!'

if __name__ == '__main__':
   app.run(port=8000, debug=True)