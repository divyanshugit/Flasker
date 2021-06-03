from flask import Flask, render_template
app = Flask(__name__)

posts = [
    {
        'author': 'Divyanshu',
        'title': 'Blog Post 1',
        'content': 'First post content',
        'date_posted': 'March 14, 2021'
    },
    {
        'author': 'Dummy User',
        'title': 'Blog Post 2',
        'content': 'Second post content',
        'date_posted': 'March 15, 2021'
    }

]

@app.route('/')
@app.route('/home')
def home():
        return render_template('home.html')

if __name__ == "__main__":
    app.run(debug=True)
