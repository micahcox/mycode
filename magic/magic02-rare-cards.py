
import mtgsdk as mtg

cards = mtg.Card.where(page=0).where(pageSize=10).where(rarity="Rare").all()
rare_cards = {}
"Dictionary of cards keyed by name"
for card in cards:
    rare_cards[card.name] = card.rarity

print(rare_cards)