
subject_prefixes = {
    "1sg.pos.sbj": "ni",
    "2sg.sbj": "u",
    "3sg.sbj": "a",
    "1pl.sbj": "tu",
    "2pl.sbj": "m",
    "3pl.sbj": "wa",
    "1sg.neg.sbj": "si"
}

tense_prefixes = {
    "prs.pos": "na",
    "pst.pos": "li",
    "pst.prf.pos": "me",
    "pst.neg": "ku",
    "pst.prf.neg": "ji",  # Double check this one I don't remember it
    "fut": "ta"
}


# Generates the surface form of a verb given its morphemes
def generate_surface_form(verb):
    morphemes = []

    # Generate the subject and subject negation morphemes
    subject_negation_morpheme = ""
    if verb["negation"] == "pos":
        subject_morpheme = subject_prefixes[verb["subject"] + (".pos" if verb["subject"] == "1sg" else "") + ".sbj"]
    elif verb["negation"] == "neg":
        if verb["subject"] == "1sg":
            subject_morpheme = subject_prefixes[verb["subject"] + ".neg.sbj"]
        elif verb["subject"] == "2sg" or verb["subject"] == "3sg":
            subject_negation_morpheme = "h"
            subject_morpheme = subject_prefixes[verb["subject"] + ".sbj"]
        else:
            subject_negation_morpheme = "ha"
            subject_morpheme = subject_prefixes[verb["subject"] + ".sbj"]
    else:
        raise Exception("Negation must be 'pos' or 'neg'")
    morphemes.append(subject_negation_morpheme)
    morphemes.append(subject_morpheme)

    # Generate the tense morpheme
    tense_morpheme = ""
    if verb["tense"] == "fut":
        tense_morpheme = tense_prefixes["tense"]
    else:
        if verb["negation"] == "pos":
            tense_morpheme = tense_prefixes[verb["tense"] + ".pos"]
        else:  # We already checked for valid negation slot
            if verb["tense"] != "prs":
                tense_morpheme = tense_prefixes[verb["tense"] + ".neg"]
    morphemes.append(tense_morpheme)

    # TODO Generate the relative pronoun morpheme
    # TODO Generate the object pronoun morpheme

    # Add the verb root
    verb_root_morpheme = verb["root"]
    morphemes.append(verb_root_morpheme)

    # TODO Append the derivational affixes to the verb root

    # Return the surface form as a combination of its morphemes
    return morphemes, "".join(morphemes)


# Creates a verb dictionary from its attributes
def generate_verb(root=None, negation="pos", subject="1sg", tense="prs"):
    # Make sure the root is non-null
    if root is None:
        raise Exception("Null root")

    # Create the verb's attributes
    verb = {
        "negation": negation,
        "subject": subject,
        "tense": tense,
        "root": root
    }

    # Generate the surface form of the verb
    morphemes, surface_form = generate_surface_form(verb)
    verb["morphemes"] = morphemes
    verb["surface_form"] = surface_form

    # Return the verb
    return verb


if __name__ == '__main__':
    sample_verb = generate_verb(root="penda")
    print(sample_verb["surface_form"])