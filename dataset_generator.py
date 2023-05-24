import json
import random
from verb_generator import generate_verb

finite_options = {
    "True": 0.95,
    "False": 0.05
}

negation_options = {
    "True": 0.25,
    "False": 0.75
}

subject_options = {
    "1sg": 0.1,
    "2sg": 0.1,
    "1pl": 0.1,
    "2pl": 0.1,
    "cl1": 0.125,
    "cl2": 0.125,
    "cl3": 0.025,
    "cl4": 0.025,
    "cl5": 0.025,
    "cl6": 0.025,
    "cl7": 0.025,
    "cl8": 0.025,
    "cl9": 0.025,
    "cl10": 0.025,
    "cl11": 0.025,
    "cl14": 0.025,
    "cl15": 0.025,
    "cl16": 0.025,
    "cl17": 0.025,
    "cl18": 0.025
}

tense_options = {
    "prs": 0.4,
    "pst": 0.2,
    "pst.prf": 0.15,
    "fut": 0.15,
    "hab": 0.1
}

anterior_options = {
    "True": 0.03,
    "False": 0.97
}

relative_options = {
    "None": 0.5,
    "cl1": 0.0625,
    "cl2": 0.0625,
    "cl3": 0.0125,
    "cl4": 0.0125,
    "cl5": 0.0125,
    "cl6": 0.0125,
    "cl7": 0.1125,
    "cl8": 0.0125,
    "cl9": 0.1125,
    "cl10": 0.0125,
    "cl11": 0.0125,
    "cl14": 0.0125,
    "cl15": 0.0125,
    "cl16": 0.0125,
    "cl17": 0.0125,
    "cl18": 0.0125
}

object_options = {
    "None": 0.5,
    "1sg": 0.05,
    "2sg": 0.05,
    "1pl": 0.05,
    "2pl": 0.05,
    "cl1": 0.0625,
    "cl2": 0.0625,
    "cl3": 0.0125,
    "cl4": 0.0125,
    "cl5": 0.0125,
    "cl6": 0.0125,
    "cl7": 0.0125,
    "cl8": 0.0125,
    "cl9": 0.0125,
    "cl10": 0.0125,
    "cl11": 0.0125,
    "cl14": 0.0125,
    "cl15": 0.0125,
    "cl16": 0.0125,
    "cl17": 0.0125,
    "cl18": 0.0125
}

causative_options = {
    "True": 0.15,
    "False": 0.85
}

passive_options = {
    "True": 0.10,
    "False": 0.90
}

applicative_options = {
    "True": 0.20,
    "False": 0.80
}

stative_options = {
    "True": 0.05,
    "False": 0.95
}

mood_options = {
    "sbjv": 0.1,
    "imp": 0.05,
    "ind": 0.75,
    "cond": 0.05,
    "sit": 0.025,
    "cons": 0.025
}

root = [
    "abudu",
    "acha",
    "achana",
    "achia",
    "adhibu",
    "aga",
    "agana",
    "agiza",
    "agua",
    "aibisha",
    "ajiri",
    "aka",
    "alika",
    "amba",
    "ambiana",
    "ambua",
    "amini",
    "amka",
    "amsha",
    "amua",
    "amuka",
    "amuru",
    "andalia",
    "andamana",
    "andika",
    "angalia",
    "angamia",
    "angaza",
    "anguka",
    "angusha",
    "anika",
    "anua",
    "anza",
    "apa",
    "azima",
    "azimu",
    "babaika",
    "babuka",
    "badili",
    "bahatisha",
    "baki",
    "bandika",
    "banduka",
    "banika",
    "bariki",
    "batili",
    "beba",
    "bembeleza",
    "bidi",
    "bingirika",
    "bishana",
    "bomoa",
    "burudisha",
    "bwata",
    "bweka",
    "chacha",
    "chafua",
    "chafya",
    "chagua",
    "chambua",
    "chana",
    "changa",
    "changamsha",
    "changanya",
    "changanyika",
    "chanja",
    "chefuka",
    "cheka",
    "chekecha",
    "chekesha",
    "chelewa",
    "chemka",
    "chemsha",
    "cheza",
    "chimba",
    "chinja",
    "chipuka",
    "chochea",
    "choka",
    "chokonoa",
    "choma",
    "chomoa",
    "chonga",
    "chora",
    "chota",
    "chuchumaa",
    "chuja",
    "chukia",
    "chukua",
    "chukulia",
    "chuma",
    "chuna",
    "chunga",
    "chutama",
    "dai",
    "daka",
    "danganya",
    "dhani",
    "elea",
    "elimisha",
    "enda",
    "enea",
    "epa",
    "erevuka",
    "ezeka",
    "faa",
    "fagia",
    "fahamisha",
    "fahamu",
    "faidia",
    "fanana",
    "fanya",
    "faulu",
    "ficha",
    "fichwa",
    "fika",
    "fikiri",
    "fikisha",
    "finyanga",
    "fuata",
    "fuatana",
    "fufua",
    "fuga",
    "fukuta",
    "fukuza",
    "fuma",
    "fumba",
    "fumbua",
    "fumua",
    "fundisha",
    "funga"
] # INCOMPLETE

parameters = {
    "finite": finite_options,
    "negation": negation_options,
    "subject": subject_options,
    "tense": tense_options,
    "anterior": anterior_options,
    "relative": relative_options,
    "object": object_options,
    "causative": causative_options,
    "passive": passive_options,
    "applicative": applicative_options,
    "stative": stative_options,
    "mood": mood_options,
    "root": root
}


def find_random(distribution, weighted_randomness):
    if not weighted_randomness:
        return random.sample(distribution.keys(), 1)[0]

    keys = list(distribution.keys() )
    probabilities = list(distribution.values() )
    choice = random.choices(keys, probabilities)[0]

    if choice == "True":
        return True
    elif choice == "False":
        return False
    elif choice == "None":
        return None
    else:
        return choice


def make_verb(weighted_randomness):
    return generate_verb(
        root=random.sample(root, 1)[0],
        finite=find_random(finite_options, weighted_randomness),
        negation=find_random(negation_options, weighted_randomness),
        subject=find_random(subject_options, weighted_randomness),
        tense=find_random(tense_options, weighted_randomness),
        anterior=find_random(anterior_options, weighted_randomness),
        relative=find_random(relative_options, weighted_randomness),
        object=find_random(object_options, weighted_randomness),
        causative=find_random(causative_options, weighted_randomness),
        passive=find_random(passive_options, weighted_randomness),
        applicative=find_random(applicative_options, weighted_randomness),
        stative=find_random(stative_options, weighted_randomness),
        mood=find_random(mood_options, weighted_randomness)
    )


def make_dataset(size, file_name, weighted_randomness=True):
    data = []
    for i in range(size):
        try:
            data.append(make_verb(weighted_randomness))
        except Exception:
            pass
        if i % 1000 == 1:
            print(f"{i / size} complete")
    # Write to the file
    with open("datasets/" + file_name, "w") as file:
        json.dump(data, file)


if __name__ == '__main__':
    num_verbs = 1000
    make_dataset(num_verbs, f"test{str(num_verbs)}verbs.json")

