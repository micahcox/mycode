
#!/usr/bin/python3
"""Get Magic the Gathering rare cards"""
# An object of Flask class is our WSGI application
from flask import Flask
import mtgsdk as mtg

# Flask constructor takes the name of current
# module (__name__) as argument
app = Flask(__name__)

# route() function of the Flask class is a
# decorator, tells the application which URL
# should call the associated function
@app.route("/")
def mtk_rare_cards():
    cards = mtg.Card.where(page=0).where(pageSize=10).where(rarity="Rare").all()
    rare_cards = {}
    "Dictionary of cards keyed by name"
    for card in cards:
        rare_card[card.name] = card.rarity

    return rare_cards.card

if __name__ == "__main__":
   app.run(host="0.0.0.0", port=2224) # runs the application
   # app.run(host="0.0.0.0", port=2224, debug=True) # DEBUG MODE