"""Graphemes used in the Javanese language"""

import pynini

################################################################################################
# AKSARA WYANJANA - consonant letters with an inherent vowel /a/ (or /ɔ/ depending on dialect) #
# This is divided into three groups:                                                           #
#     * NGLEGENA - Modern Javanese consonants                                                  #
#     * MURDA - Honorific purpose consonants such as names of legendary heros, sultans, etc.   #
#     * MAHAPRANA - Obsolete consonants except in Sanskrit and Kawi texts                      #
################################################################################################
AKSARA_NGLEGENA = pynini.union(
    "ꦲ",
    "ꦤ",
    "ꦕ",
    "ꦫ",
    "ꦏ",
    "ꦢ",
    "ꦠ",
    "ꦱ",
    "ꦮ",
    "ꦭ",
    "ꦥ",
    "ꦝ",
    "ꦗ",
    "ꦪ",
    "ꦚ",
    "ꦩ",
    "ꦒ",
    "ꦧ",
    "ꦛ",
    "ꦔ",
)

AKSARA_MURDA = pynini.union("ꦟ", "ꦖ", "ꦬ", "ꦑ", "ꦡ", "ꦯ", "ꦦ", "ꦘ", "ꦓ", "ꦨ")

AKSARA_MAHAPRANA = pynini.union("ꦣ", "ꦰ", "ꦞ", "ꦙ", "ꦜ")

##################################################################
# AKSARA_REKAN - additional letters used to write foreign sounds #
# such as loanwords from Arabic, Dutch, etc.                     #
##################################################################
AKSARA_REKAN = pynini.union("ꦲ꦳", "ꦏ꦳", "ꦐ", "ꦢ꦳", "ꦱ꦳", "ꦥ꦳", "ꦗ꦳", "ꦒ꦳", "ꦔ꦳")

###################################################################################################################
# PASANGAN - each consonant has a conjuct to supress the inherent vowel when in the middle of a word or sentence. #
###################################################################################################################
AKSARA_NGLEGENA_PASANGAN = pynini.union(
    "꧀ꦲ",
    "꧀ꦤ",
    "꧀ꦕ",
    "꧀ꦫ",
    "꧀ꦏ",
    "꧀ꦢ",
    "꧀ꦠ",
    "꧀ꦱ",
    "꧀ꦮ",
    "꧀ꦭ",
    "꧀ꦥ",
    "꧀ꦝ",
    "꧀ꦗ",
    "꧀ꦪ",
    "꧀ꦚ",
    "꧀ꦩ",
    "꧀ꦒ",
    "꧀ꦧ",
    "꧀ꦛ",
    "꧀ꦔ",
)

AKSARA_MURDA_PASANGAN = pynini.union(
    "꧀ꦟ", "꧀ꦖ", "꧀ꦬ", "꧀ꦑ", "꧀ꦡ", "꧀ꦯ", "꧀ꦦ", "꧀ꦘ", "꧀ꦓ", "꧀ꦨ"
)

AKSARA_MAHAPRANA_PASANGAN = pynini.union("꧀ꦣ", "꧀ꦰ", "꧀ꦞ", "꧀ꦙ", "꧀ꦜ")

PASANGAN = pynini.union(
    AKSARA_NGLEGENA_PASANGAN, AKSARA_MURDA_PASANGAN, AKSARA_MAHAPRANA_PASANGAN
)

# AKSARA_SWARA - letters that represent pure vowels
AKSARA_SWARA = pynini.union(
    "ꦄ", "ꦆ", "ꦈ", "ꦉ", "ꦊ", "ꦌ", "ꦎ", "ꦄꦴ", "ꦇ", "ꦈꦴ", "ꦉꦴ", "ꦋ", "ꦍ", "ꦎꦴ"
)

##############################################################################
# SANDHANGAN - diacritics used to modify default vowel of a consonant letter #
##############################################################################

# SANDHANGAN_SWARA - diacritics that are used to change the inherent /a/ into different vowels
SANDHANGAN_SWARA = pynini.union(
    "ꦶ", "ꦸ", "ꦺ", "ꦺꦴ", "ꦼ", "ꦴ", "ꦷ", "ꦹ", "ꦻ", "ꦻꦴ", "ꦼꦴ"
)

# SANDHANGAN_PANYIGEGING_WANDA - diacritics used to write closed syllables
SANDHANGAN_PANYIGEGING_WANDA_ORA_PANGKON = pynini.union("ꦀ", "ꦁ", "ꦂ", "ꦃ")

PANGKON = pynini.union("꧀")

SANDHANGAN_PANYIGEGING_WANDA = pynini.union(
    SANDHANGAN_PANYIGEGING_WANDA_ORA_PANGKON, PANGKON
)

# SANDHANGAN_WYANJANA - diacritics used to write consonant clusters with semivowels that occur in a single syllable
SANDHANGAN_WYANJANA = pynini.union("ꦽ", "ꦾ", "ꦿ", "꧀ꦭ", "꧀ꦮ")

#####################################################################################################################################################
# ANGKA - Javanese numerals which can share glyphs with some Javanese consonants. This can be disambiguiated in writing using certain punctuations. #
#####################################################################################################################################################
ANGKA = pynini.union("꧐", "꧑", "꧒", "꧓", "꧔", "꧕", "꧖", "꧗", "꧘", "꧙")

###########################################################
# PEPADAN - Javanese script ornate verse marks for poetry #
###########################################################
PEPADAN = pynini.union("꧃", "꧄", "꧅", "ꦟ꧀ꦢꦿ", "ꦧ꧀ꦖ", "ꦆ",)

################################
# PADA - Javanese punctuations #
################################
PADA = pynini.union(
    "꧈",
    "꧉",
    "꧊",
    "꧋",
    "꧌",
    "꧍",
    "꧁",
    "꧂",
    "꧇",
    "ꧏ",
    "꧋",
    "꧉",
    "꧞",
    "꧟",
    "꧆",
    # Modern Javanese
    ":",
    ",",
    ".",
    '"',
    ")",
    "(",
    # For non-scriptio continua Javanese that uses spaces between words
    " ",
    PEPADAN,
)


#########################################################################################
# LATIN - Latin script used in modern Javanese (may include IPA characters in Javanese) #
#########################################################################################
LATIN = pynini.union(
    "A",
    "B",
    "C",
    "D",
    "E",
    "F",
    "G",
    "H",
    "I",
    "J",
    "K",
    "L",
    "M",
    "N",
    "O",
    "P",
    "Q",
    "R",
    "S",
    "T",
    "U",
    "V",
    "W",
    "X",
    "Y",
    "Z",
    "a",
    "ā",
    "b",
    "c",
    "d",
    "e",
    "é",
    "f",
    "g",
    "h",
    "i",
    "ī",
    "j",
    "k",
    "l",
    "m",
    "n",
    "o",
    "p",
    "q",
    "r",
    "s",
    "t",
    "u",
    "ū",
    "v",
    "w",
    "x",
    "y",
    "z",
)

#############################################################################
# IPA - IPA symbols not represented in Javanese Latin script                #
#############################################################################
IPA = pynini.union(
    "ə", "ʃ", "d̪", "t̪", "ɲ", "ɖ", "ʒ", "ŋ", "ʈ", "ð", "ɣ", "ʕ", "ː", "ɨ"
)

CONSONANTS = pynini.union(
    "ʃ",
    "d̪",
    "t̪",
    "ɲ",
    "ɖ",
    "ʒ",
    "ŋ",
    "ʈ",
    "ð",
    "ɣ",
    "ʕ",
    "B",
    "C",
    "D",
    "F",
    "G",
    "H",
    "J",
    "K",
    "L",
    "M",
    "N",
    "P",
    "Q",
    "R",
    "S",
    "T",
    "V",
    "W",
    "X",
    "Y",
    "Z",
    "b",
    "c",
    "d",
    "f",
    "g",
    "h",
    "j",
    "k",
    "l",
    "m",
    "n",
    "p",
    "q",
    "r",
    "s",
    "t",
    "v",
    "w",
    "x",
    "y",
    "z",
)

VOWELS = pynini.union(
    "A", "I", "E", "O", "U", "a", "i", "e", "o", "u", "ə", "ɨ", "ū", "ī", "ā", "é",
)

############################################################
# ARABIC_NUMERALS - Arabic numbers used in modern Javanese #
############################################################
ARABIC_NUMERALS = pynini.union("0", "1", "2", "3", "4", "5", "6", "7", "8", "9")
