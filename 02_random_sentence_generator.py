import random

names = ['Peter', 'Michael', 'John', 'Arthur', 'Stephan', 'Kevin', 'Jack']
places = ['Sofia', 'Plovdiv', 'Dupnitsa', 'Varna', 'Burgas', 'Ruse', 'Pleven']
verbs = ['rides', 'plays', 'cooks', 'eats', 'sees', 'brings', 'holds']
nouns = ['stones', 'peach', 'bike', 'dinner', 'a friend', 'a ball', 'plane']
adverbs = ['slowly', 'poorly', 'warmly', 'happily', 'sadly', 'rapidly', 'diligently']
details = ['in the forest', 'at the beach', 'at the court', 'in the park', 'in the mountain', 'at home', 'at school']
sentences_generated_count = 0

def random_word(word):
    return random.choice(word)


while True:
    sentences_generated_count += 1
    random_name = random_word(names)
    random_place = random_word(places)
    random_verb = random_word(verbs)
    random_noun = random_word(nouns)
    random_adverb = random_word(adverbs)
    random_detail = random_word(details)
    print(f"{random_name} from {random_place} {random_adverb} {random_verb} {random_noun} {random_detail}.")
    print(f"Sentences generated: {sentences_generated_count}")
    question = input(f"Would you like to see a new random sentence? ")
    if question == "yes":
        continue
    elif question == "no":
        print(f"Goodbye!")
        break
    else:
        raise SystemExit(f"Your answer should be either 'yes' or 'no.'")