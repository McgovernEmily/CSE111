
# Added function get_adjective to complete the exceeded requirements.

import random

def main():
    # First sentence.
    quantity = 1
    tense = "past"
    print(f"{make_sentence(quantity, tense)}.")
    
    # Second sentence
    quantity = 1
    tense = "present"
    print(f"{make_sentence(quantity, tense)}.")

    # Third sentence.
    quantity = 1
    tense = "future"
    print(f"{make_sentence(quantity, tense)}.")

    # Fourth sentence.
    quantity = 2
    tense = "present"
    print(f"{make_sentence(quantity, tense)}.")

    # Five sentence.
    quantity = 2
    tense = "present"
    print(f"{make_sentence(quantity, tense)}.")   

    # Sixth sentence.
    quantity = 2
    tense = "future"
    print(f"{make_sentence(quantity, tense)}.") 


def get_determiner(quantity):
    """Return a randomly chosen determiner. A determiner is
    a word like "the", "a", "one", "some", "many".
    If quantity is 1, this function will return either "a",
    "one", or "the". Otherwise this function will return
    either "some", "many", or "the".

    Parameter
        quantity: an integer.
            If quantity is 1, this function will return a
            determiner for a single noun. Otherwise this
            function will return a determiner for a plural
            noun.
    Return: a randomly chosen determiner.
    """

    # Creating the list of words.
    if quantity == 1:
        words = ["a", "one", "the"]
    else:
        words = ["some", "many", "the"]

    # Randomly choose and return a determiner.
    word = random.choice(words)
    return word
    

def get_noun(quantity):
    """Return a randomly chosen noun.
    If quantity is 1, this function will
    return one of these ten single nouns:
        "bird", "boy", "car", "cat", "child",
        "dog", "girl", "man", "rabbit", "woman"
    Otherwise, this function will return one of
    these ten plural nouns:
        "birds", "boys", "cars", "cats", "children",
        "dogs", "girls", "men", "rabbits", "women"

    Parameter
        quantity: an integer that determines if
            the returned noun is single or plural.
    Return: a randomly chosen noun.
    """
    # List of both single and plural nouns.
    single_noun = [ "bird", "boy", "car", "cat", "child", "dog", 
        "girl", "man", "rabbit", "woman"]
    plural_noun = ["birds", "boys", "cars", "cats", "children", 
        "dogs", "girls", "men", "rabbits", "women"]

    # If statement determining if the quantity is 1 or higher.
    if quantity == 1:
        noun = random.choice(single_noun)
    else:
        noun = random.choice(plural_noun)

    return noun
 
    
def get_verb(quantity, tense):
    """Return a randomly chosen verb. If tense is "past",
    this function will return one of these ten verbs:
        "drank", "ate", "grew", "laughed", "thought",
        "ran", "slept", "talked", "walked", "wrote"
    If tense is "present" and quantity is 1, this
    function will return one of these ten verbs:
        "drinks", "eats", "grows", "laughs", "thinks",
        "runs", "sleeps", "talks", "walks", "writes"
    If tense is "present" and quantity is NOT 1,
    this function will return one of these ten verbs:
        "drink", "eat", "grow", "laugh", "think",
        "run", "sleep", "talk", "walk", "write"
    If tense is "future", this function will return one of
    these ten verbs:
        "will drink", "will eat", "will grow", "will laugh",
        "will think", "will run", "will sleep", "will talk",
        "will walk", "will write"

    Parameters
        quantity: an integer that determines if the
            returned verb is single or plural.
        tense: a string that determines the verb conjugation,
            either "past", "present" or "future".
    Return: a randomly chosen verb.
    """
    # List of all the verbs.
    verb_past = ["drank", "ate", "grew", "laughed", "thought", 
        "ran", "slept", "talked", "walked", "wrote"]
    verbs_one_quantity = ["drinks", "eats", "grows", "laughs", 
        "thinks", "runs", "sleeps", "talks", "walks", "writes"]
    verbs_no_quantity = ["drink", "eat", "grow", "laugh", "think", 
        "run", "sleep", "talk", "walk", "write"]
    verb_future = ["will drink", "will eat", "will grow", "will laugh",
        "will think", "will run", "will sleep", "will talk",
        "will walk", "will write"]

    # If statements showing past, present, and future.
    # Also randomizing the verbs.
    if tense == "past":
        verb = random.choice(verb_past)
        
    elif tense == "present" and quantity == 1:
        verb = random.choice(verbs_one_quantity)
        
    elif tense == "present" and quantity != 1:
        verb = random.choice(verbs_no_quantity)
        
    elif tense == "future":
        verb = random.choice(verb_future)
    
    return verb

def get_preposition():
    """Return a randomly chosen preposition
    from this list of prepositions:
    "about", "above", "across", "after", "along",
    "around", "at", "before", "behind", "below",
    "beyond", "by", "despite", "except", "for",
    "from", "in", "into", "near", "of",
    "off", "on", "onto", "out", "over",
    "past", "to", "under", "with", "without"

    Return: a randomly chosen preposition.
    """

    # List of all the words for preposition.
    preposition = ["about", "above", "across", "after", "along",
    "around", "at", "before", "behind", "below",
    "beyond", "by", "despite", "except", "for",
    "from", "in", "into", "near", "of",
    "off", "on", "onto", "out", "over",
    "past", "to", "under", "with", "without"]

    # Randomly selecting one of the prepositions.
    preposition = random.choice(preposition)
    return preposition

def get_prepositional_phrase(quantity):
    """Build and return a prepositional phrase composed
    of three words: a preposition, a determiner, and a
    noun by calling the get_preposition, get_determiner,
    and get_noun functions.

    Parameter
        quantity: an integer that determines if the
            determiner and noun in the prepositional
            phrase returned from this function should
            be single or pluaral.
    Return: a prepositional phrase.
    """
    
    # Calling the preposition, determiner, and the noun.
    preposition = get_preposition()
    determiner = get_determiner(quantity)
    noun = get_noun(quantity)   

    # Constructing the words into the prepositional phrase.
    prepositional_phrase = f"{preposition} {determiner} {noun}"
    return prepositional_phrase

def get_adjective():
    """Return a randomly chosen adjective
    from this list of adjectives:
    "joyful", "mysterious", "bright", "courageous", "humble",
    "generous", "loyal", "adventurous", "graceful", "ambitious",
    "creative", "determined", "energetic", "fearless", "honest",
    "imaginative", "kind", "lively", "optimistic", "passionate"

    Return: a randomly chosen preposition.
    """

    # List of all the adjectives.
    adjectives = ["joyful", "mysterious", "bright", "courageous", "humble",
    "generous", "loyal", "adventurous", "graceful", "ambitious",
    "creative", "determined", "energetic", "fearless", "honest",
    "imaginative", "kind", "lively", "optimistic", "passionate"]

    # Randomly selecting the adjective.
    adjective = random.choice(adjectives)
    return adjective

def make_sentence(quantity, tense):
    """Build and return a sentence with three words:
    a determiner, a noun, and a verb. The grammatical
    quantity of the determiner and noun will match the
    number in the quantity parameter. The grammatical
    quantity and tense of the verb will match the number
    and tense in the quantity and tense parameters.
    """
    # Labeling calling the determiner, noun, and verb functions.
    determiner = get_determiner(quantity)
    noun = get_noun(quantity)
    verbs = get_verb(quantity, tense)
    first_prepositional_phrase = get_prepositional_phrase(quantity)
    second_preopositional_phrase = get_prepositional_phrase(quantity)
    adjective = get_adjective()

    # Structuring the sentences.
    full_sentence = f"{determiner.capitalize()} {adjective} {noun} {first_prepositional_phrase} {verbs} {second_preopositional_phrase}"
    return full_sentence
    
# Calling the main function.
main()