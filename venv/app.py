from flask import Flask, render_template
import random

app = Flask(__name__)

fun_facts = [
    "The unicorn is the national animal of Scotland.",
    "Bananas are berries, but strawberries aren't.",
    "A group of flamingos is called a 'flamboyance'.",
    "A group of pandas is called an 'embarrassment'.",
    "The Great Wall Of China is not visible from space with the naked eye.",
    "Honeybees can recognize human faces.",
    "The world's oldest known recipe is for beer.",
    "The longest time between two twins being born is 87 days.",
    "There are more possible iterations of a game of chess than there are atoms in the known universe.",
    "Cows have best friends and can become stressed when they are separated.",
    "Astronauts cannot burp in space due to the lack of gravity.",
    "The shortest war in history was between Britain and Zanzibar on August 27, 1896. Zanzibar surrendered after 38 minutes.",
]

@app.route('/')
def index():
    fact = random.choice(fun_facts)
    return render_template('index.html', fact=fact)

if __name__ == '__main__':
    app.run(debug=True)
