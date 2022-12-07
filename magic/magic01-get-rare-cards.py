import mtgsdk as mtg

if __name__ == "__main__":
    cards = mtg.Card.where(page=0).where(pageSize=10).where(rarity="Rare").all()

    for card in cards:
        print(card.name,"rarity is", card.rarity)