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

reciprocal_options = {
    "True": 0.1,
    "False": 0.9
}

mood_options = {
    "sbjv": 0.1,
    "imp": 0.05,
    "ind": 0.75,
    "cond": 0.05,
    "sit": 0.025,
    "cons": 0.025
}

test_roots = ['amka', 'andalia', 'bishana', 'bomoa', 'chambua', 'chefuka', 'chekecha', 'chukua', 'dhani', 'epa', 'fuata', 'funga', 'gomba', 'heshimu', 'hifadhi', 'hitaji', 'hutubia', 'jaza', 'karibia', 'keti', 'kubali', 'laki', 'legea', 'lemaa', 'nyunyizia', 'omboleza', 'ona', 'onyesha', 'ozesha', 'piga', 'pukuta', 'randa', 'samaheka', 'sikia', 'sikika', 'songa', 'stahili', 'tamani', 'tandaza', 'tangaza', 'teka', 'tetema', 'tomba', 'twika', 'uawa', 'uma', 'uvumbuzi', 'vuma', 'vunja', 'wika']
train_roots = ['abudu', 'acha', 'achia', 'adhibu', 'aga', 'agiza', 'agua', 'aibisha', 'ajiri', 'aka', 'alika', 'amba', 'ambua', 'amini', 'amsha', 'amua', 'amuka', 'amuru', 'andika', 'angalia', 'angamia', 'angaza', 'anguka', 'angusha', 'anika', 'anua', 'anza', 'apa', 'azima', 'azimu', 'babaika', 'babuka', 'badili', 'bahatisha', 'baki', 'bandika', 'banduka', 'banika', 'bariki', 'batili', 'beba', 'bembeleza', 'bidi', 'bingirika', 'burudisha', 'bwata', 'bweka', 'chacha', 'chafua', 'chafya', 'chagua', 'chana', 'changa', 'changamsha', 'changanya', 'changanyika', 'chanja', 'cheka', 'chekesha', 'chelewa', 'chemka', 'chemsha', 'cheza', 'chimba', 'chinja', 'chipuka', 'chochea', 'choka', 'chokonoa', 'choma', 'chomoa', 'chonga', 'chora', 'chota', 'chuchumaa', 'chuja', 'chukia', 'chukulia', 'chuma', 'chuna', 'chunga', 'chutama', 'dai', 'daka', 'danganya', 'elea', 'elimisha', 'enda', 'enea', 'erevuka', 'ezeka', 'faa', 'fagia', 'fahamisha', 'fahamu', 'faidia', 'fanana', 'fanya', 'faulu', 'ficha', 'fika', 'fikiri', 'finyanga', 'fufua', 'fuga', 'fukuta', 'fukuza', 'fuma', 'fumba', 'fumbua', 'fumua', 'fundisha', 'fungua', 'funguka', 'funguliwa', 'fungwa', 'funika', 'funua', 'funza', 'fupika', 'fura', 'furahi', 'futa', 'fyeka', 'ganda', 'gandamana', 'gawanya', 'geua', 'goma', 'gombana', 'gonga', 'gongana', 'guguna', 'gumia', 'guna', 'gundua', 'gusa', 'hadithia', 'haribu', 'hesabu', 'himiza', 'hitimu', 'hudhuria', 'hurumia', 'husu', 'huzunia', 'iba', 'iga', 'imarika', 'imba', 'inama', 'ingia', 'inua', 'ipo', 'isha', 'ishi', 'ita', 'iva', 'jaa', 'jamba', 'jaribu', 'jenga', 'jua', 'julikana', 'juta', 'kaa', 'kaanga', 'kaba', 'kagua', 'kamata', 'kana', 'kanda', 'kanyaga', 'kata', 'kataa', 'kataza', 'katika', 'kauka', 'kawia', 'kemea', 'kenua', 'kimbia', 'kinga', 'kingama', 'kiri', 'kodi', 'kohoa', 'kojoa', 'koma', 'komba', 'konda', 'konyeza', 'kopesha', 'koroga', 'koroma', 'kosa', 'kua', 'kwaa', 'kwama', 'lainisha', 'lala', 'lamba', 'lawama', 'laza', 'lazimu', 'lea', 'leta', 'letwa', 'levya', 'lewa', 'lia', 'lima', 'limwa', 'linda', 'lingana', 'lipa', 'lisha', 'lowa', 'maliza', 'menya', 'meremeta', 'meza', 'mimina', 'minya', 'momonyoka', 'mulika', 'mwaga', 'nawa', 'nenepa', "ng'aa", "ng'oa", "ng'oka", "ng'olewa", 'ngara', 'ngoja', 'nguruma', "ning'inia", 'noa', 'nuka', 'nukia', "nung'unika", 'nunua', 'nusa', 'nyakua', 'nyamaza', "nyang'anya", 'nyanyua', 'nyauka', 'nyemelea', 'nyesha', 'nyima', 'nyoa', 'nyonga', 'nyonya', 'nyooka', 'nyoosha', 'nywewa', 'oa', 'oga', 'ogopa', 'oka', 'okoa', 'okota', 'omba', 'ondoa', 'onea', 'ongea', 'ongeza', 'ongopa', 'ongoza', 'onwa', 'onya', 'osha', 'ota', 'oza', 'paa', 'paaza', 'pagawa', 'paka', 'pakia', 'pakua', 'palilia', 'pambanua', 'panda', 'panga', 'pangusa', 'papasa', 'parua', 'pasa', 'pasua', 'pata', 'patia', 'payuka', 'pekecha', 'peleka', 'peleleza', 'pembea', 'penda', 'penga', 'pepea', 'pepeta', 'pewa', 'pika', 'pikwa', 'pima', 'pinda', 'pindua', 'pinga', 'pita', 'poa', 'ponya', 'potea', 'pukuchua', 'puliza', 'pumua', 'pumzika', 'punga', 'ramba', 'refuka', 'rithi', 'roga', 'rudi', 'ruhusu', 'ruka', 'runda', 'rusha', 'sadiki', 'safiri', 'safisha', 'saga', 'sahau', 'saidia', 'sali', 'salimia', 'salimu', 'sambaa', 'samehe', 'sawazisha', 'sema', 'semezana', 'shambuliwa', 'shangaa', 'shangilia', 'shawishi', 'sherehekea', 'shiba', 'shika', 'shikamana', 'shinda', 'shindilia', 'shindwa', 'shirikiana', 'shona', 'shtaki', 'shtua', 'shtuka', 'shughulika', 'shuhudia', 'shuka', 'shukuru', 'shutumika', 'sifu', 'sihi', 'sikiliza', 'sikitika', 'sikiza', 'simama', 'simika', 'simulia', 'sindikiza', 'sinzia', 'sita', 'sitawi', 'sogea', 'sokota', 'soma', 'staajabu', 'subiri', 'sugua', 'suka', 'sukuma', 'sumbua', 'tafadhali', 'tafuna', 'tafuta', 'taga', 'tagaa', 'tajirika', 'taka', 'takata', 'takiwa', 'tambaa', 'tambua', 'tamka', 'tandika', 'tangulia', 'tanua', 'tapakaa', 'tapika', 'tata', 'tatanisha', 'tatua', 'tawala', 'tayarisha', 'tazama', 'tega', 'tegemea', 'tegua', 'teleza', 'tema', 'tembea', 'tenda', 'tenga', 'tengemaa', 'tengeneza', 'teseka', 'tetea', 'tetemeka', 'tia', 'tibu', 'tii', 'tikisa', 'timia', 'tiririka', 'tisha', 'toa', 'toba', 'toboa', 'toka', 'tolewa', 'tona', 'toroka', 'tota', 'tua', 'tubu', 'tukana', 'tukia', 'tukuka', 'tulia', 'tuma', 'tumaini', 'tundika', 'tunza', 'tupa', 'twanga', 'ua', 'udhika', 'ugua', 'uliza', 'umba', 'umuka', 'unga', 'uza', 'vaa', 'valisha', 'vimba', 'vua', 'vuja', 'vuka', 'vumilia', 'vuna', 'vundika', 'vuruga', 'vuta', 'vutia', 'wamba', 'weka', 'weza', 'wima', 'winda', 'yumba', 'zaa', 'zama', 'zeeka', 'ziba', 'zidi', 'zika', 'zima', 'zingira', 'zipo', 'zoea', 'zuia', 'zuka', 'zunguka', 'zungumza', 'zurura']

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
    "reciprocal": reciprocal_options,
    "applicative": applicative_options,
    "stative": stative_options,
    "mood": mood_options,
    "root": [*test_roots, *train_roots]
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


def make_verb(weighted_randomness, training):
    return generate_verb(
        root=random.sample(train_roots if training else test_roots, 1)[0],
        finite=find_random(finite_options, weighted_randomness),
        negation=find_random(negation_options, weighted_randomness),
        subject=find_random(subject_options, weighted_randomness),
        tense=find_random(tense_options, weighted_randomness),
        anterior=find_random(anterior_options, weighted_randomness),
        relative=find_random(relative_options, weighted_randomness),
        object=find_random(object_options, weighted_randomness),
        causative=find_random(causative_options, weighted_randomness),
        reciprocal=find_random(reciprocal_options, weighted_randomness),
        passive=find_random(passive_options, weighted_randomness),
        applicative=find_random(applicative_options, weighted_randomness),
        stative=find_random(stative_options, weighted_randomness),
        mood=find_random(mood_options, weighted_randomness)
    )


def make_dataset(size, file_name, weighted_randomness=True, training=True, spaced=True, stripped=True):
    data = []
    while len(data) < size:
        try:
            verb = make_verb(weighted_randomness, training)
            if stripped:
                morphemes = "".join([(morpheme + " " if morpheme != "" else "") for morpheme in verb["morphemes"] ]).strip() if spaced else verb['morphemes']
                verb_data = {
                    'surface_form': verb['surface_form'],
                    'morphemes': morphemes
                }
                data.append(verb_data)
            else:
                if spaced:
                    verb["parsed"] = "".join([(morpheme + " " if morpheme != "" else "") for morpheme in verb["morphemes"] ]).strip()
                data.append(verb)
        except Exception:
            pass
        if len(data) % 10000 == 0:
            print(f"{len(data) / size} complete")
    # Write to the file
    with open("datasets/" + file_name, "w") as file:
        json.dump(data, file)


if __name__ == '__main__':
    is_training = True
    weighted = True
    spaced = True
    quantity = 1000000
    stripped = True
    make_dataset(quantity,
                 f"{quantity}_{'training' if is_training else 'testing'}{'_stripped' if stripped else ''}_{'not_' if not weighted else ''}weighted_{'not_' if not spaced else ''}spaced.json",
                 weighted_randomness=weighted,
                 training=is_training,
                 spaced=spaced,
                 stripped=stripped)
