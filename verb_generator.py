subject_prefixes = {
    "1sg.pos.sbj": "ni",
    "2sg.sbj": "u",
    "1pl.sbj": "tu",
    "2pl.sbj": "m",
    "1sg.neg.sbj": "si",
    "cl1.sbj": "a",
    "cl2.sbj": "wa",
    "cl3.sbj": "u",
    "cl4.sbj": "i",
    "cl5.sbj": "li",
    "cl6.sbj": "ya",
    "cl7.sbj": "ki",
    "cl8.sbj": "vi",
    "cl9.sbj": "i",
    "cl10.sbj": "zi",
    "cl11.sbj": "u",
    "cl14.sbj": "u",
    "cl15.sbj": "ku",
    "cl16.sbj": "pa",
    "cl17.sbj": "ku",
    "cl18.sbj": "mu"
}

tense_prefixes = {
    "prs.pos": "na",
    "pst.pos": "li",
    "pst.prf.pos": "me",
    "pst.neg": "ku",
    "pst.prf.neg": "ja",
    "fut": "ta",
    "hab.pos": "hu"
}  

relative_prefixes = {
    "cl1.rel": "ye",
    "cl2.rel": "o",
    "cl3.rel": "o",
    "cl4.rel": "yo",
    "cl5.rel": "lo",
    "cl6.rel": "yo",
    "cl7.rel": "cho",
    "cl8.rel": "vyo",
    "cl9.rel": "yo",
    "cl10.rel": "zo",
    "cl11.rel": "o",
    "cl14.rel": "o",
    "cl15.rel": "ko",
    "cl16.rel": "po",
    "cl17.rel": "ko",
    "cl18.rel": "mo"
}

object_prefixes = {
    "1sg.obj": "ni",
    "2sg.obj": "ku",
    "1pl.obj": "tu",
    "2pl.obj": "ma",  # cl1.obj are handled separately
    "cl2.obj": "wa",
    "cl3.obj": "u",
    "cl4.obj": "i",
    "cl5.obj": "li",
    "cl6.obj": "ya",
    "cl7.obj": "ki",
    "cl8.obj": "vi",
    "cl9.obj": "i",
    "cl10.obj": "zi",
    "cl11.obj": "u",
    "cl14.obj": "u",
    "cl15.obj": "ku",
    "cl16.obj": "pa",
    "cl17.obj": "ku",
    "cl18.obj": "mu"
}


# Finds the harmony class (i/u/a, e/o) of a given stem
def find_harmony_class(stem):
    high_harmony = "aiu"
    mid_harmony = "eo"
    for char in reversed(stem):
        if char in high_harmony:
            return "high"
        elif char in mid_harmony:
            return "mid"
    raise Exception("No harmony class for stem", stem)


# Generates the surface form of a verb given its morphemes
def generate_surface_form(verb):
    morphemes = []

    # Generate the subject and subject negation morphemes
    subject_negation_morpheme = ""
    subject_morpheme = ""
    if not verb["finite"]:
        if verb["negation"]:
            subject_morpheme = "kuto"
        else:
            subject_morpheme = "ku"
    elif verb["mood"] != "imp" and verb["tense"] != "hab":
        if not verb["negation"] or verb["mood"] == "cond":
            if verb["subject"] == "1sg":
                subject_morpheme = subject_prefixes["1sg.pos.sbj"]
            else:
                subject_morpheme = subject_prefixes[verb["subject"] + ".sbj"]
        else:
            if verb["subject"] == "1sg":
                subject_morpheme = subject_prefixes[verb["subject"] + ".neg.sbj"]
            elif verb["subject"] == "2sg" or verb["subject"] == "cl1":
                subject_negation_morpheme = "h"
                subject_morpheme = subject_prefixes[verb["subject"] + ".sbj"]
            else:
                subject_negation_morpheme = "ha"
                subject_morpheme = subject_prefixes[verb["subject"] + ".sbj"]
    morphemes.append(subject_negation_morpheme)
    morphemes.append(subject_morpheme)

    # Generate the tense morpheme
    tense_morpheme = ""
    if verb["finite"] and verb["mood"] != "imp":
        # Verbs with relative pronouns take "si" iff negative
        if verb["mood"] == "sbjv" or (verb["relative"] is not None and verb["negation"]):
            if verb["negation"]:
                tense_morpheme = "si"
        elif verb["mood"] == "cond":
            if verb["tense"] == "fut" or verb["tense"] == "hab":
                raise Exception(f"Conditional {verb['tense']} does not exist.")
            elif verb["tense"] == "prs":
                tense_morpheme = "nge"
            elif verb["tense"] == "pst" or verb["tense"] == "pst.prf":
                tense_morpheme = "ngeli"
            # If negative, add the negative si
            if verb["negation"]:
                tense_morpheme = "si" + tense_morpheme
        # Sit = situational, cons = consecutive
        elif verb["mood"] == "sit" or verb["mood"] == "cons":
            if verb["negation"]:
                raise Exception(f"{verb['mood']} verbs can't be negated.")
            if verb["mood"] == "sit":
                tense_morpheme = "ki"
            elif verb["mood"] == "cons":
                tense_morpheme = "ka"
        elif verb["relative"] is not None:
            if verb["tense"] == "fut":
                tense_morpheme = "taka"
            elif verb["tense"] == "pst.prf":
                tense_morpheme = "li"
            elif verb["tense"] == "hab":
                tense_morpheme = "na"
            else:
                tense_morpheme = tense_prefixes[verb["tense"] + ".pos"]
        else:
            if verb["tense"] == "fut":
                tense_morpheme = tense_prefixes["tense"]
            else:
                if not verb["negation"]:
                    tense_morpheme = tense_prefixes[verb["tense"] + ".pos"]
                else:  # We already checked for valid negation slot
                    if verb["tense"] != "prs" and verb["tense"] != "hab":
                        tense_morpheme = tense_prefixes[verb["tense"] + ".neg"]
    morphemes.append(tense_morpheme)

    # Generate the anterior morpheme
    anterior_morpheme = ""
    if verb["finite"] and verb["anterior"]:
        anterior_morpheme = "sha"
    morphemes.append(anterior_morpheme)

    # Generate the relative morpheme
    # Tenseless positive relative templates are not handled
    relative_morpheme = ""
    if verb["finite"] and verb["mood"] != "imp":
        if verb["relative"] is not None:
            relative_morpheme = relative_prefixes[verb["relative"] + ".rel"]
    morphemes.append(relative_morpheme)

    # Generate the object morpheme
    object_morpheme = ""
    if verb["object"] is not None:
        if verb["subject"] == verb["object"]:
            object_morpheme = "ji"
        else:
            if verb["object"] == "cl1":
                if verb["root"][1] in "aeiou":
                    object_morpheme = "mw"
                else:
                    object_morpheme = "m"
            else:
                object_morpheme = object_prefixes[verb["object"] + ".obj"]
    morphemes.append(object_morpheme)

    # Find verb information
    verb_is_irregular = False  # TODO handle irregular verbs
    verb_class = verb["root"][-1]

    # Add the verb root
    verb_root_morpheme = verb["root"][:-1]
    morphemes.append(verb_root_morpheme)

    # Add the causative suffix
    causative_morpheme = ""
    if verb["causative"]:  # TODO Handle other, consider irregular verbs
        if morphemes[-1][-1] in "aeiou":
            causative_morpheme = "z"
        else:
            if find_harmony_class(morphemes[-1]) == "high":
                causative_morpheme = "ish"
            else:
                causative_morpheme = "esh"
        verb_class = "a"
    morphemes.append(causative_morpheme)

    # Add the passive morpheme
    passive_morpheme = ""
    if verb["passive"]:
        if verb_class == "a":
            if morphemes[-1][-1] in "aeiou":
                if find_harmony_class(morphemes[-1]) == "high":
                    passive_morpheme = "liw"
                else:
                    passive_morpheme = "lew"
            else:
                passive_morpheme = "w"
        elif verb_class == "e":
            passive_morpheme = "w"
        elif verb_class == "i":
            passive_morpheme = "iw"
        elif verb_class == "u":
            if verb["root"][-1] == "a":
                passive_morpheme = "liw"
            else:
                passive_morpheme = "iw"
        verb_class = "a"
    morphemes.append(passive_morpheme)

    # Add applicative morpheme
    applicative_morpheme = ""
    if verb["applicative"]:
        if verb_class == "a":
            if morphemes[-1][-1] in "aeiou":
                if find_harmony_class(morphemes[-1]) == "high":
                    applicative_morpheme = "li"
                else:
                    applicative_morpheme = "le"
            else:
                applicative_morpheme = "e"
        elif verb_class == "e" or verb_class == "i":
            applicative_morpheme = ""
        elif verb_class == "u":
            if verb["root"][-1] == "a":
                applicative_morpheme = "li"
            else:
                applicative_morpheme = "i"
        verb_class = "a"
    morphemes.append(applicative_morpheme)

    # Add stative morpheme
    stative_morpheme = ""
    if verb["applicative"]:
        if verb_class == "a":
            if morphemes[-1][-1] in "aeiou":
                if find_harmony_class(morphemes[-1]) == "high":
                    stative_morpheme = "ik"
                else:
                    stative_morpheme = "ek"
            else:
                if find_harmony_class(morphemes[-1]) == "high":
                    stative_morpheme = "lik"
                else:
                    stative_morpheme = "lek"
        elif verb_class == "i":
            stative_morpheme = "ik"
        elif verb_class == "e":
            stative_morpheme = "ek"
        elif verb_class == "u":
            if verb["root"][-1] == "a":
                stative_morpheme = "lik"
            else:
                stative_morpheme = "ik"
        verb_class = "a"
    morphemes.append(stative_morpheme)

    # Add the final vowel
    final_vowel_morpheme = ""
    imperative_morpheme = ""
    if verb["finite"]:
        if verb["mood"] == "sbjv":
            if verb_class == "a":
                final_vowel_morpheme = "e"
        elif verb["mood"] == "imp":
            if verb["subject"] == "2sg":
                if verb["object"] is not None:
                    if verb_class == "a":
                        final_vowel_morpheme = "e"
            elif verb["subject"] == "2pl":
                if verb_class == "a":
                    final_vowel_morpheme = "e"
                    imperative_morpheme = "ni"
            else:
                raise Exception("Imperative must take '2sg' or '2pl' subject")
        elif verb["mood"] == "ind":
            if verb["negation"] and verb["tense"] == "prs" and verb_class == "a":
                final_vowel_morpheme = "i"
            else:
                final_vowel_morpheme = "a"
        else:
            raise Exception("Mood must be 'sbjv', 'imp', 'ind', 'cond', 'sit'")
    morphemes.append(final_vowel_morpheme)
    morphemes.append(imperative_morpheme)

    # Return the surface form as a combination of its morphemes
    return morphemes, "".join(morphemes)


# Creates a verb dictionary from its attributes
def generate_verb(root=None, finite=True, negation=True, subject="1sg", tense="prs", anterior=False,
                  relative=None, object=None, causative=False, passive=False, applicative=False, stative=False,
                  mood="ind"):
    # Make sure the root is non-null
    if root is None:
        raise Exception("Null root")

    # Create the verb's attributes
    verb = {
        "finite": finite,
        "negation": negation,
        "subject": subject,
        "tense": tense,
        "anterior": anterior,
        "relative": relative,
        "object": object,
        "causative": causative,
        "passive": passive,
        "applicative": applicative,
        "stative": stative,
        "mood": mood,
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
