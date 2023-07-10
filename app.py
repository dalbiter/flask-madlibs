from flask import Flask, render_template
from flask_debugtoolbar import DebugToolbarExtension
from stories import Story

app = Flask(__name__)
app.config['SECRET_KEY'] = "oh-so-secret"
debug = DebugToolbarExtension(app)

@app.route('/')
def show_home():
    """Shows the home page"""
    return render_template('home.html')


@app.route('/form')
def show_story_form():
    """Shows story form"""
    return render_template('story_form.html')

@app.route('/story')
def show_story():
    """takes answers from story-form and renders the story"""
    return render_template('story.html')