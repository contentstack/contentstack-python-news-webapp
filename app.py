from flask import Flask, render_template, url_for
import contentstack

app = Flask(__name__)


@app.route('/')
@app.route('/news')
def news():
    stack = contentstack.Stack('blt920bb7e90248f607', 'blt0c4300391e033d4a59eb2857', 'production')
    query = stack.content_type('news').query()
    headlines = query.find()
    return render_template('home.html', news=headlines, title="home")


@app.route('/about')
def about():
    return render_template('about.html', title="about")


if __name__ == "__main__":
    app.run(debug=True)
