"""Javanese Script Grapheme to IPA Equivalent Mapper"""
#
# Rewrite rules based on research by K. Dudas. 1976. “The phonology and morphology of modern Javanese. University Microfilms, Ann Arbor, Michigan.
#

import pynini
from pynini.lib import rewrite

from javanese_graphemes import (
    AKSARA_NGLEGENA,
    AKSARA_NGLEGENA_PASANGAN,
    AKSARA_MURDA,
    AKSARA_MURDA_PASANGAN,
    AKSARA_MAHAPRANA,
    AKSARA_MAHAPRANA_PASANGAN,
    AKSARA_REKAN,
    AKSARA_SWARA,
    PASANGAN,
    SANDHANGAN_PANYIGEGING_WANDA,
    SANDHANGAN_PANYIGEGING_WANDA_ORA_PANGKON,
    PANGKON,
    SANDHANGAN_SWARA,
    SANDHANGAN_WYANJANA,
    ANGKA,
    PADA,
    PEPADAN,
    LATIN,
    IPA,
    ARABIC_NUMERALS,
    CONSONANTS,
    VOWELS,
)

# AKSARAs except for SWARA (Pure Vowels)
AKSARA_ORA_SWARA = pynini.union(
    AKSARA_NGLEGENA, AKSARA_MURDA, AKSARA_MAHAPRANA, AKSARA_REKAN
)

SIGMA_STAR = (
    pynini.union(
        AKSARA_NGLEGENA,
        AKSARA_NGLEGENA_PASANGAN,
        AKSARA_MURDA,
        AKSARA_MURDA_PASANGAN,
        AKSARA_MAHAPRANA,
        AKSARA_MAHAPRANA_PASANGAN,
        AKSARA_REKAN,
        AKSARA_SWARA,
        SANDHANGAN_PANYIGEGING_WANDA,
        SANDHANGAN_SWARA,
        SANDHANGAN_WYANJANA,
        ANGKA,
        PADA,
        LATIN,
        IPA,
        ARABIC_NUMERALS,
    )
    .closure()
    .optimize()
)

# Javanese Numbers and Punctuation Rules
ANGKA_LAN_PADA = (
    # ANGKA
    pynini.cdrewrite(
        pynini.cross("꧐", "0"),
        pynini.union("꧈", "꧇"),
        pynini.union("꧈", "꧇"),
        SIGMA_STAR,
    )
    @ pynini.cdrewrite(
        pynini.cross("꧑", "1"),
        pynini.union("꧈", "꧇", ANGKA, ARABIC_NUMERALS),
        pynini.union("꧈", "꧇", ANGKA, ARABIC_NUMERALS),
        SIGMA_STAR,
    )
    @ pynini.cdrewrite(
        pynini.cross("꧒", "2"),
        pynini.union("꧈", "꧇"),
        pynini.union("꧈", "꧇"),
        SIGMA_STAR,
    )
    @ pynini.cdrewrite(
        pynini.cross("꧓", "3"),
        pynini.union("꧈", "꧇"),
        pynini.union("꧈", "꧇"),
        SIGMA_STAR,
    )
    @ pynini.cdrewrite(
        pynini.cross("꧔", "4"),
        pynini.union("꧈", "꧇"),
        pynini.union("꧈", "꧇"),
        SIGMA_STAR,
    )
    @ pynini.cdrewrite(
        pynini.cross("꧕", "5"),
        pynini.union("꧈", "꧇"),
        pynini.union("꧈", "꧇"),
        SIGMA_STAR,
    )
    @ pynini.cdrewrite(
        pynini.cross("꧖", "6"),
        pynini.union("꧈", "꧇"),
        pynini.union("꧈", "꧇"),
        SIGMA_STAR,
    )
    @ pynini.cdrewrite(
        pynini.cross("꧗", "7"),
        pynini.union("꧈", "꧇", ANGKA, ARABIC_NUMERALS),
        pynini.union("꧈", "꧇", ANGKA, ARABIC_NUMERALS),
        SIGMA_STAR,
    )
    @ pynini.cdrewrite(
        pynini.cross("꧘", "8"),
        pynini.union("꧈", "꧇"),
        pynini.union("꧈", "꧇"),
        SIGMA_STAR,
    )
    @ pynini.cdrewrite(
        pynini.cross("꧙", "9"),
        pynini.union("꧈", "꧇"),
        pynini.union("꧈", "꧇"),
        SIGMA_STAR,
    )
    # PADA
    @ pynini.cdrewrite(
        pynini.cross("꧋꧆꧋", "(neutral rank letter intro)"), "", "", SIGMA_STAR
    )
    @ pynini.cdrewrite(pynini.cross("꧉꧆꧉", "(letter closure)"), "", "", SIGMA_STAR)
    @ pynini.cdrewrite(pynini.cross("꧈", ","), "", "", SIGMA_STAR)
    @ pynini.cdrewrite(pynini.cross("꧉", "."), "", "", SIGMA_STAR)
    @ pynini.cdrewrite(pynini.cross("꧊", "(parenthesis)"), "", "", SIGMA_STAR)
    @ pynini.cdrewrite(pynini.cross("꧋", "(paragraph start)"), "", "", SIGMA_STAR)
    @ pynini.cdrewrite(pynini.cross("꧌", '"'), "", "", SIGMA_STAR)
    @ pynini.cdrewrite(pynini.cross("꧍", '"'), "", "", SIGMA_STAR)
    @ pynini.cdrewrite(pynini.cross("꧁", "(title enclosure left)"), "", "", SIGMA_STAR)
    @ pynini.cdrewrite(pynini.cross("꧂", "(title enclosure right)"), "", "", SIGMA_STAR)
    @ pynini.cdrewrite(pynini.cross("꧇", ":"), "", "", SIGMA_STAR)
    @ pynini.cdrewrite(pynini.cross("ꧏ", "(repeat twice)"), "", "", SIGMA_STAR)
    @ pynini.cdrewrite(
        pynini.cross("ꦧ꧀ꦖ", "(poem first canto)"),
        pynini.union("꧅"),
        pynini.union("꧅"),
        SIGMA_STAR,
    )
    @ pynini.cdrewrite(
        pynini.cross("ꦟ꧀ꦢꦿ", "(poem change canto)"),
        pynini.union("꧅"),
        pynini.union("꧅"),
        SIGMA_STAR,
    )
    @ pynini.cdrewrite(
        pynini.cross("ꦆ", "(poem final canto)"),
        pynini.union("꧅"),
        pynini.union("꧅"),
        SIGMA_STAR,
    )
    @ pynini.cdrewrite(
        pynini.cross("꧃", "(lower rank letter intro)"), "", "", SIGMA_STAR
    )
    @ pynini.cdrewrite(
        pynini.cross("꧄", "(same rank letter intro)"), "", "", SIGMA_STAR
    )
    @ pynini.cdrewrite(
        pynini.cross("꧅", "(higher rank letter intro)"), "", "", SIGMA_STAR
    )
    @ pynini.cdrewrite(pynini.cross("꧞", ""), "꧞", "꧞", SIGMA_STAR)
    @ pynini.cdrewrite(pynini.cross("꧟", ""), "꧟", "꧟", SIGMA_STAR)
    @ pynini.cdrewrite(pynini.cross("꧞", ""), "꧞", "", SIGMA_STAR)
    @ pynini.cdrewrite(pynini.cross("꧟", ""), "꧟", "", SIGMA_STAR)
    @ pynini.cdrewrite(
        pynini.cross("꧞", "(Yogyakarta correction mark)"), "", "", SIGMA_STAR
    )
    @ pynini.cdrewrite(
        pynini.cross("꧟", "(Surakarta correction mark)"), "", "", SIGMA_STAR
    )
)

AKSARA_ROOT_CONSONANT_ONLY_NO_VOWELS = (
    pynini.cdrewrite(
        pynini.cross("ꦲ", "(h)"),
        "",
        pynini.union(SANDHANGAN_SWARA, SANDHANGAN_WYANJANA, PASANGAN, PANGKON),
        SIGMA_STAR,
    )
    @ pynini.cdrewrite(
        pynini.cross("ꦤ", "n"),
        "",
        pynini.union(SANDHANGAN_SWARA, SANDHANGAN_WYANJANA, PASANGAN, PANGKON),
        SIGMA_STAR,
    )
    @ pynini.cdrewrite(
        pynini.cross("ꦕ", "tʃ"),
        "",
        pynini.union(SANDHANGAN_SWARA, SANDHANGAN_WYANJANA, PASANGAN, PANGKON),
        SIGMA_STAR,
    )
    @ pynini.cdrewrite(
        pynini.cross("ꦫ", "r"),
        "",
        pynini.union(SANDHANGAN_SWARA, SANDHANGAN_WYANJANA, PASANGAN, PANGKON),
        SIGMA_STAR,
    )
    @ pynini.cdrewrite(
        pynini.cross("ꦏ", "k"),
        "",
        pynini.union(SANDHANGAN_SWARA, SANDHANGAN_WYANJANA, PASANGAN, PANGKON),
        SIGMA_STAR,
    )
    @ pynini.cdrewrite(
        pynini.cross("ꦢ", "d̪"),
        "",
        pynini.union(SANDHANGAN_SWARA, SANDHANGAN_WYANJANA, PASANGAN, PANGKON),
        SIGMA_STAR,
    )
    @ pynini.cdrewrite(
        pynini.cross("ꦠ", "t̪"),
        "",
        pynini.union(SANDHANGAN_SWARA, SANDHANGAN_WYANJANA, PASANGAN, PANGKON),
        SIGMA_STAR,
    )
    @ pynini.cdrewrite(
        pynini.cross("ꦱ", "s"),
        "",
        pynini.union(SANDHANGAN_SWARA, SANDHANGAN_WYANJANA, PASANGAN, PANGKON),
        SIGMA_STAR,
    )
    @ pynini.cdrewrite(
        pynini.cross("ꦮ", "w"),
        "",
        pynini.union(SANDHANGAN_SWARA, SANDHANGAN_WYANJANA, PASANGAN, PANGKON),
        SIGMA_STAR,
    )
    @ pynini.cdrewrite(
        pynini.cross("ꦭ", "l"),
        "",
        pynini.union(SANDHANGAN_SWARA, SANDHANGAN_WYANJANA, PASANGAN, PANGKON),
        SIGMA_STAR,
    )
    @ pynini.cdrewrite(
        pynini.cross("ꦥ", "p"),
        "",
        pynini.union(SANDHANGAN_SWARA, SANDHANGAN_WYANJANA, PASANGAN, PANGKON),
        SIGMA_STAR,
    )
    @ pynini.cdrewrite(
        pynini.cross("ꦝ", "ɖ"),
        "",
        pynini.union(SANDHANGAN_SWARA, SANDHANGAN_WYANJANA, PASANGAN, PANGKON),
        SIGMA_STAR,
    )
    @ pynini.cdrewrite(
        pynini.cross("ꦗ", "dʒ"),
        "",
        pynini.union(SANDHANGAN_SWARA, SANDHANGAN_WYANJANA, PASANGAN, PANGKON),
        SIGMA_STAR,
    )
    @ pynini.cdrewrite(
        pynini.cross("ꦪ", "j"),
        "",
        pynini.union(SANDHANGAN_SWARA, SANDHANGAN_WYANJANA, PASANGAN, PANGKON),
        SIGMA_STAR,
    )
    @ pynini.cdrewrite(
        pynini.cross("ꦚ", "ɲ"),
        "",
        pynini.union(SANDHANGAN_SWARA, SANDHANGAN_WYANJANA, PASANGAN, PANGKON),
        SIGMA_STAR,
    )
    @ pynini.cdrewrite(
        pynini.cross("ꦩ", "m"),
        "",
        pynini.union(SANDHANGAN_SWARA, SANDHANGAN_WYANJANA, PASANGAN, PANGKON),
        SIGMA_STAR,
    )
    @ pynini.cdrewrite(
        pynini.cross("ꦒ", "g"),
        "",
        pynini.union(SANDHANGAN_SWARA, SANDHANGAN_WYANJANA, PASANGAN, PANGKON),
        SIGMA_STAR,
    )
    @ pynini.cdrewrite(
        pynini.cross("ꦧ", "b"),
        "",
        pynini.union(SANDHANGAN_SWARA, SANDHANGAN_WYANJANA, PASANGAN, PANGKON),
        SIGMA_STAR,
    )
    @ pynini.cdrewrite(
        pynini.cross("ꦛ", "ʈ"),
        "",
        pynini.union(SANDHANGAN_SWARA, SANDHANGAN_WYANJANA, PASANGAN, PANGKON),
        SIGMA_STAR,
    )
    @ pynini.cdrewrite(
        pynini.cross("ꦔ", "ŋ"),
        "",
        pynini.union(SANDHANGAN_SWARA, SANDHANGAN_WYANJANA, PASANGAN, PANGKON),
        SIGMA_STAR,
    )
    @ pynini.cdrewrite(
        pynini.cross("ꦟ", "n"),
        "",
        pynini.union(SANDHANGAN_SWARA, SANDHANGAN_WYANJANA, PASANGAN, PANGKON),
        SIGMA_STAR,
    )
    @ pynini.cdrewrite(
        pynini.cross("ꦖ", "tʃ"),
        "",
        pynini.union(SANDHANGAN_SWARA, SANDHANGAN_WYANJANA, PASANGAN, PANGKON),
        SIGMA_STAR,
    )
    @ pynini.cdrewrite(
        pynini.cross("ꦬ", "r"),
        "",
        pynini.union(SANDHANGAN_SWARA, SANDHANGAN_WYANJANA, PASANGAN, PANGKON),
        SIGMA_STAR,
    )
    @ pynini.cdrewrite(
        pynini.cross("ꦑ", "k"),
        "",
        pynini.union(SANDHANGAN_SWARA, SANDHANGAN_WYANJANA, PASANGAN, PANGKON),
        SIGMA_STAR,
    )
    @ pynini.cdrewrite(
        pynini.cross("ꦡ", "t̪"),
        "",
        pynini.union(SANDHANGAN_SWARA, SANDHANGAN_WYANJANA, PASANGAN, PANGKON),
        SIGMA_STAR,
    )
    @ pynini.cdrewrite(
        pynini.cross("ꦯ", "s"),
        "",
        pynini.union(SANDHANGAN_SWARA, SANDHANGAN_WYANJANA, PASANGAN, PANGKON),
        SIGMA_STAR,
    )
    @ pynini.cdrewrite(
        pynini.cross("ꦦ", "p"),
        "",
        pynini.union(SANDHANGAN_SWARA, SANDHANGAN_WYANJANA, PASANGAN, PANGKON),
        SIGMA_STAR,
    )
    @ pynini.cdrewrite(
        pynini.cross("ꦘ", "ɲ"),
        "",
        pynini.union(SANDHANGAN_SWARA, SANDHANGAN_WYANJANA, PASANGAN, PANGKON),
        SIGMA_STAR,
    )
    @ pynini.cdrewrite(
        pynini.cross("ꦓ", "g"),
        "",
        pynini.union(SANDHANGAN_SWARA, SANDHANGAN_WYANJANA, PASANGAN, PANGKON),
        SIGMA_STAR,
    )
    @ pynini.cdrewrite(
        pynini.cross("ꦨ", "b"),
        "",
        pynini.union(SANDHANGAN_SWARA, SANDHANGAN_WYANJANA, PASANGAN, PANGKON),
        SIGMA_STAR,
    )
    @ pynini.cdrewrite(
        pynini.cross("ꦣ", "d"),
        "",
        pynini.union(SANDHANGAN_SWARA, SANDHANGAN_WYANJANA, PASANGAN, PANGKON),
        SIGMA_STAR,
    )
    @ pynini.cdrewrite(
        pynini.cross("ꦰ", "s"),
        "",
        pynini.union(SANDHANGAN_SWARA, SANDHANGAN_WYANJANA, PASANGAN, PANGKON),
        SIGMA_STAR,
    )
    @ pynini.cdrewrite(
        pynini.cross("ꦞ", "ɖ"),
        "",
        pynini.union(SANDHANGAN_SWARA, SANDHANGAN_WYANJANA, PASANGAN, PANGKON),
        SIGMA_STAR,
    )
    @ pynini.cdrewrite(
        pynini.cross("ꦙ", "dʒ"),
        "",
        pynini.union(SANDHANGAN_SWARA, SANDHANGAN_WYANJANA, PASANGAN, PANGKON),
        SIGMA_STAR,
    )
    @ pynini.cdrewrite(
        pynini.cross("ꦜ", "ʈ"),
        "",
        pynini.union(SANDHANGAN_SWARA, SANDHANGAN_WYANJANA, PASANGAN, PANGKON),
        SIGMA_STAR,
    )
    @ pynini.cdrewrite(
        pynini.cross("ꦲ꦳", "ħ"),
        "",
        pynini.union(SANDHANGAN_SWARA, SANDHANGAN_WYANJANA, PASANGAN, PANGKON),
        SIGMA_STAR,
    )
    @ pynini.cdrewrite(
        pynini.cross("ꦏ꦳", "x"),
        "",
        pynini.union(SANDHANGAN_SWARA, SANDHANGAN_WYANJANA, PASANGAN, PANGKON),
        SIGMA_STAR,
    )
    @ pynini.cdrewrite(
        pynini.cross("ꦐ", "q"),
        "",
        pynini.union(SANDHANGAN_SWARA, SANDHANGAN_WYANJANA, PASANGAN, PANGKON),
        SIGMA_STAR,
    )
    @ pynini.cdrewrite(
        pynini.cross("ꦢ꦳", "ð"),
        "",
        pynini.union(SANDHANGAN_SWARA, SANDHANGAN_WYANJANA, PASANGAN, PANGKON),
        SIGMA_STAR,
    )
    @ pynini.cdrewrite(
        pynini.cross("ꦱ꦳", "ʃ"),
        "",
        pynini.union(SANDHANGAN_SWARA, SANDHANGAN_WYANJANA, PASANGAN, PANGKON),
        SIGMA_STAR,
    )
    @ pynini.cdrewrite(
        pynini.cross("ꦥ꦳", "f/v"),
        "",
        pynini.union(SANDHANGAN_SWARA, SANDHANGAN_WYANJANA, PASANGAN, PANGKON),
        SIGMA_STAR,
    )
    @ pynini.cdrewrite(
        pynini.cross("ꦗ꦳", "z"),
        "",
        pynini.union(SANDHANGAN_SWARA, SANDHANGAN_WYANJANA, PASANGAN, PANGKON),
        SIGMA_STAR,
    )
    @ pynini.cdrewrite(
        pynini.cross("ꦒ꦳", "ɣ"),
        "",
        pynini.union(SANDHANGAN_SWARA, SANDHANGAN_WYANJANA, PASANGAN, PANGKON),
        SIGMA_STAR,
    )
    @ pynini.cdrewrite(
        pynini.cross("ꦔ꦳", "ʕ"),
        "",
        pynini.union(SANDHANGAN_SWARA, SANDHANGAN_WYANJANA, PASANGAN, PANGKON),
        SIGMA_STAR,
    )
)

# Javanese Consonant and Vowel Rules
AKSARA_2_IPA = (
    AKSARA_ROOT_CONSONANT_ONLY_NO_VOWELS
    # SANDHANGAN_WYANJANA
    @ pynini.cdrewrite(pynini.cross("ꦽ", "rə"), "", "", SIGMA_STAR,)
    @ pynini.cdrewrite(
        pynini.cross("ꦾ", "ja"),
        "",
        pynini.union(
            AKSARA_ORA_SWARA,
            SANDHANGAN_PANYIGEGING_WANDA_ORA_PANGKON,
            PADA,
            PEPADAN,
            CONSONANTS,
            "[EOS]",
        ),
        SIGMA_STAR,
    )
    @ pynini.cdrewrite(
        pynini.cross("ꦿ", "ra"),
        "",
        pynini.union(
            AKSARA_ORA_SWARA,
            SANDHANGAN_PANYIGEGING_WANDA_ORA_PANGKON,
            PADA,
            PEPADAN,
            CONSONANTS,
            "[EOS]",
        ),
        SIGMA_STAR,
    )
    @ pynini.cdrewrite(
        pynini.cross("꧀ꦭ", "la"),
        "",
        pynini.union(
            AKSARA_ORA_SWARA,
            SANDHANGAN_PANYIGEGING_WANDA_ORA_PANGKON,
            PADA,
            PEPADAN,
            CONSONANTS,
            "[EOS]",
        ),
        SIGMA_STAR,
    )
    @ pynini.cdrewrite(
        pynini.cross("꧀ꦮ", "wa"),
        "",
        pynini.union(
            AKSARA_ORA_SWARA,
            SANDHANGAN_PANYIGEGING_WANDA_ORA_PANGKON,
            PADA,
            PEPADAN,
            CONSONANTS,
            "[EOS]",
        ),
        SIGMA_STAR,
    )
    # AKSARA_PASANGAN
    @ pynini.cdrewrite(
        pynini.cross("꧀ꦲ", "(h)a"),
        "",
        pynini.union(
            AKSARA_ORA_SWARA,
            SANDHANGAN_PANYIGEGING_WANDA_ORA_PANGKON,
            PADA,
            PEPADAN,
            CONSONANTS,
            "[EOS]",
        ),
        SIGMA_STAR,
    )
    @ pynini.cdrewrite(
        pynini.cross("꧀ꦤ", "na"),
        "",
        pynini.union(
            AKSARA_ORA_SWARA,
            SANDHANGAN_PANYIGEGING_WANDA_ORA_PANGKON,
            PADA,
            PEPADAN,
            CONSONANTS,
            "[EOS]",
        ),
        SIGMA_STAR,
    )
    @ pynini.cdrewrite(
        pynini.cross("꧀ꦕ", "tʃa"),
        "",
        pynini.union(
            AKSARA_ORA_SWARA,
            SANDHANGAN_PANYIGEGING_WANDA_ORA_PANGKON,
            PADA,
            PEPADAN,
            CONSONANTS,
            "[EOS]",
        ),
        SIGMA_STAR,
    )
    @ pynini.cdrewrite(
        pynini.cross("꧀ꦫ", "ra"),
        "",
        pynini.union(
            AKSARA_ORA_SWARA,
            SANDHANGAN_PANYIGEGING_WANDA_ORA_PANGKON,
            PADA,
            PEPADAN,
            CONSONANTS,
            "[EOS]",
        ),
        SIGMA_STAR,
    )
    @ pynini.cdrewrite(
        pynini.cross("꧀ꦏ", "ka"),
        "",
        pynini.union(
            AKSARA_ORA_SWARA,
            SANDHANGAN_PANYIGEGING_WANDA_ORA_PANGKON,
            PADA,
            PEPADAN,
            CONSONANTS,
            "[EOS]",
        ),
        SIGMA_STAR,
    )
    @ pynini.cdrewrite(
        pynini.cross("꧀ꦢ", "d̪a"),
        "",
        pynini.union(
            AKSARA_ORA_SWARA,
            SANDHANGAN_PANYIGEGING_WANDA_ORA_PANGKON,
            PADA,
            PEPADAN,
            CONSONANTS,
            "[EOS]",
        ),
        SIGMA_STAR,
    )
    @ pynini.cdrewrite(
        pynini.cross("꧀ꦠ", "t̪a"),
        "",
        pynini.union(
            AKSARA_ORA_SWARA,
            SANDHANGAN_PANYIGEGING_WANDA_ORA_PANGKON,
            PADA,
            PEPADAN,
            CONSONANTS,
            "[EOS]",
        ),
        SIGMA_STAR,
    )
    @ pynini.cdrewrite(
        pynini.cross("꧀ꦱ", "sa"),
        "",
        pynini.union(
            AKSARA_ORA_SWARA,
            SANDHANGAN_PANYIGEGING_WANDA_ORA_PANGKON,
            PADA,
            PEPADAN,
            CONSONANTS,
            CONSONANTS,
            "[EOS]",
        ),
        SIGMA_STAR,
    )
    @ pynini.cdrewrite(
        pynini.cross("꧀ꦮ", "wa"),
        "",
        pynini.union(
            AKSARA_ORA_SWARA,
            SANDHANGAN_PANYIGEGING_WANDA_ORA_PANGKON,
            PADA,
            PEPADAN,
            CONSONANTS,
            "[EOS]",
        ),
        SIGMA_STAR,
    )
    @ pynini.cdrewrite(
        pynini.cross("꧀ꦭ", "la"),
        "",
        pynini.union(
            AKSARA_ORA_SWARA,
            SANDHANGAN_PANYIGEGING_WANDA_ORA_PANGKON,
            PADA,
            PEPADAN,
            CONSONANTS,
            "[EOS]",
        ),
        SIGMA_STAR,
    )
    @ pynini.cdrewrite(
        pynini.cross("꧀ꦥ", "pa"),
        "",
        pynini.union(
            AKSARA_ORA_SWARA,
            SANDHANGAN_PANYIGEGING_WANDA_ORA_PANGKON,
            PADA,
            PEPADAN,
            CONSONANTS,
            "[EOS]",
        ),
        SIGMA_STAR,
    )
    @ pynini.cdrewrite(
        pynini.cross("꧀ꦝ", "ɖa"),
        "",
        pynini.union(
            AKSARA_ORA_SWARA,
            SANDHANGAN_PANYIGEGING_WANDA_ORA_PANGKON,
            PADA,
            PEPADAN,
            CONSONANTS,
            "[EOS]",
        ),
        SIGMA_STAR,
    )
    @ pynini.cdrewrite(
        pynini.cross("꧀ꦗ", "dʒa"),
        "",
        pynini.union(
            AKSARA_ORA_SWARA,
            SANDHANGAN_PANYIGEGING_WANDA_ORA_PANGKON,
            PADA,
            PEPADAN,
            CONSONANTS,
            "[EOS]",
        ),
        SIGMA_STAR,
    )
    @ pynini.cdrewrite(
        pynini.cross("꧀ꦪ", "ja"),
        "",
        pynini.union(
            AKSARA_ORA_SWARA,
            SANDHANGAN_PANYIGEGING_WANDA_ORA_PANGKON,
            PADA,
            PEPADAN,
            CONSONANTS,
            "[EOS]",
        ),
        SIGMA_STAR,
    )
    @ pynini.cdrewrite(
        pynini.cross("꧀ꦚ", "ɲa"),
        "",
        pynini.union(
            AKSARA_ORA_SWARA,
            SANDHANGAN_PANYIGEGING_WANDA_ORA_PANGKON,
            PADA,
            PEPADAN,
            CONSONANTS,
            "[EOS]",
        ),
        SIGMA_STAR,
    )
    @ pynini.cdrewrite(
        pynini.cross("꧀ꦩ", "ma"),
        "",
        pynini.union(
            AKSARA_ORA_SWARA,
            SANDHANGAN_PANYIGEGING_WANDA_ORA_PANGKON,
            PADA,
            PEPADAN,
            CONSONANTS,
            "[EOS]",
        ),
        SIGMA_STAR,
    )
    @ pynini.cdrewrite(
        pynini.cross("꧀ꦒ", "ga"),
        "",
        pynini.union(
            AKSARA_ORA_SWARA,
            SANDHANGAN_PANYIGEGING_WANDA_ORA_PANGKON,
            PADA,
            PEPADAN,
            CONSONANTS,
            "[EOS]",
        ),
        SIGMA_STAR,
    )
    @ pynini.cdrewrite(
        pynini.cross("꧀ꦧ", "ba"),
        "",
        pynini.union(
            AKSARA_ORA_SWARA,
            SANDHANGAN_PANYIGEGING_WANDA_ORA_PANGKON,
            PADA,
            PEPADAN,
            CONSONANTS,
            "[EOS]",
        ),
        SIGMA_STAR,
    )
    @ pynini.cdrewrite(
        pynini.cross("꧀ꦛ", "ʈa"),
        "",
        pynini.union(
            AKSARA_ORA_SWARA,
            SANDHANGAN_PANYIGEGING_WANDA_ORA_PANGKON,
            PADA,
            PEPADAN,
            CONSONANTS,
            "[EOS]",
        ),
        SIGMA_STAR,
    )
    @ pynini.cdrewrite(
        pynini.cross("꧀ꦔ", "ŋa"),
        "",
        pynini.union(
            AKSARA_ORA_SWARA,
            SANDHANGAN_PANYIGEGING_WANDA_ORA_PANGKON,
            PADA,
            PEPADAN,
            CONSONANTS,
            "[EOS]",
        ),
        SIGMA_STAR,
    )
    @ pynini.cdrewrite(
        pynini.cross("꧀ꦟ", "na"),
        "",
        pynini.union(
            AKSARA_ORA_SWARA,
            SANDHANGAN_PANYIGEGING_WANDA_ORA_PANGKON,
            PADA,
            PEPADAN,
            CONSONANTS,
            "[EOS]",
        ),
        SIGMA_STAR,
    )
    @ pynini.cdrewrite(
        pynini.cross("꧀ꦖ", "tʃa"),
        "",
        pynini.union(
            AKSARA_ORA_SWARA,
            SANDHANGAN_PANYIGEGING_WANDA_ORA_PANGKON,
            PADA,
            PEPADAN,
            CONSONANTS,
            "[EOS]",
        ),
        SIGMA_STAR,
    )
    @ pynini.cdrewrite(
        pynini.cross("꧀ꦬ", "ra"),
        "",
        pynini.union(
            AKSARA_ORA_SWARA,
            SANDHANGAN_PANYIGEGING_WANDA_ORA_PANGKON,
            PADA,
            PEPADAN,
            CONSONANTS,
            "[EOS]",
        ),
        SIGMA_STAR,
    )
    @ pynini.cdrewrite(
        pynini.cross("꧀ꦑ", "ka"),
        "",
        pynini.union(
            AKSARA_ORA_SWARA,
            SANDHANGAN_PANYIGEGING_WANDA_ORA_PANGKON,
            PADA,
            PEPADAN,
            CONSONANTS,
            "[EOS]",
        ),
        SIGMA_STAR,
    )
    @ pynini.cdrewrite(
        pynini.cross("꧀ꦡ", "t̪a"),
        "",
        pynini.union(
            AKSARA_ORA_SWARA,
            SANDHANGAN_PANYIGEGING_WANDA_ORA_PANGKON,
            PADA,
            PEPADAN,
            CONSONANTS,
            "[EOS]",
        ),
        SIGMA_STAR,
    )
    @ pynini.cdrewrite(
        pynini.cross("꧀ꦯ", "sa"),
        "",
        pynini.union(
            AKSARA_ORA_SWARA,
            SANDHANGAN_PANYIGEGING_WANDA_ORA_PANGKON,
            PADA,
            PEPADAN,
            CONSONANTS,
            "[EOS]",
        ),
        SIGMA_STAR,
    )
    @ pynini.cdrewrite(
        pynini.cross("꧀ꦦ", "pa"),
        "",
        pynini.union(
            AKSARA_ORA_SWARA,
            SANDHANGAN_PANYIGEGING_WANDA_ORA_PANGKON,
            PADA,
            PEPADAN,
            CONSONANTS,
            "[EOS]",
        ),
        SIGMA_STAR,
    )
    @ pynini.cdrewrite(
        pynini.cross("꧀ꦘ", "ɲa"),
        "",
        pynini.union(
            AKSARA_ORA_SWARA,
            SANDHANGAN_PANYIGEGING_WANDA_ORA_PANGKON,
            PADA,
            PEPADAN,
            CONSONANTS,
            "[EOS]",
        ),
        SIGMA_STAR,
    )
    @ pynini.cdrewrite(
        pynini.cross("꧀ꦓ", "ga"),
        "",
        pynini.union(
            AKSARA_ORA_SWARA,
            SANDHANGAN_PANYIGEGING_WANDA_ORA_PANGKON,
            PADA,
            PEPADAN,
            CONSONANTS,
            "[EOS]",
        ),
        SIGMA_STAR,
    )
    @ pynini.cdrewrite(
        pynini.cross("꧀ꦨ", "ba"),
        "",
        pynini.union(
            AKSARA_ORA_SWARA,
            SANDHANGAN_PANYIGEGING_WANDA_ORA_PANGKON,
            PADA,
            PEPADAN,
            CONSONANTS,
            "[EOS]",
        ),
        SIGMA_STAR,
    )
    @ pynini.cdrewrite(
        pynini.cross("꧀ꦣ", "da"),
        "",
        pynini.union(
            AKSARA_ORA_SWARA,
            SANDHANGAN_PANYIGEGING_WANDA_ORA_PANGKON,
            PADA,
            PEPADAN,
            CONSONANTS,
            "[EOS]",
        ),
        SIGMA_STAR,
    )
    @ pynini.cdrewrite(
        pynini.cross("꧀ꦰ", "sa"),
        "",
        pynini.union(
            AKSARA_ORA_SWARA,
            SANDHANGAN_PANYIGEGING_WANDA_ORA_PANGKON,
            PADA,
            PEPADAN,
            CONSONANTS,
            "[EOS]",
        ),
        SIGMA_STAR,
    )
    @ pynini.cdrewrite(
        pynini.cross("꧀ꦞ", "ɖa"),
        "",
        pynini.union(
            AKSARA_ORA_SWARA,
            SANDHANGAN_PANYIGEGING_WANDA_ORA_PANGKON,
            PADA,
            PEPADAN,
            CONSONANTS,
            "[EOS]",
        ),
        SIGMA_STAR,
    )
    @ pynini.cdrewrite(
        pynini.cross("꧀ꦙ", "dʒa"),
        "",
        pynini.union(
            AKSARA_ORA_SWARA,
            SANDHANGAN_PANYIGEGING_WANDA_ORA_PANGKON,
            PADA,
            PEPADAN,
            CONSONANTS,
            "[EOS]",
        ),
        SIGMA_STAR,
    )
    @ pynini.cdrewrite(
        pynini.cross("꧀ꦜ", "ʈa"),
        "",
        pynini.union(
            AKSARA_ORA_SWARA,
            SANDHANGAN_PANYIGEGING_WANDA_ORA_PANGKON,
            PADA,
            PEPADAN,
            CONSONANTS,
            "[EOS]",
        ),
        SIGMA_STAR,
    )
    @ pynini.cdrewrite(
        pynini.cross("꧀ꦲ꦳", "ħa"),
        "",
        pynini.union(
            AKSARA_ORA_SWARA,
            SANDHANGAN_PANYIGEGING_WANDA_ORA_PANGKON,
            PADA,
            PEPADAN,
            CONSONANTS,
            "[EOS]",
        ),
        SIGMA_STAR,
    )
    @ pynini.cdrewrite(
        pynini.cross("꧀ꦏ꦳", "xa"),
        "",
        pynini.union(
            AKSARA_ORA_SWARA,
            SANDHANGAN_PANYIGEGING_WANDA_ORA_PANGKON,
            PADA,
            PEPADAN,
            CONSONANTS,
            "[EOS]",
        ),
        SIGMA_STAR,
    )
    @ pynini.cdrewrite(
        pynini.cross("꧀ꦐ", "qa"),
        "",
        pynini.union(
            AKSARA_ORA_SWARA,
            SANDHANGAN_PANYIGEGING_WANDA_ORA_PANGKON,
            PADA,
            PEPADAN,
            CONSONANTS,
            "[EOS]",
        ),
        SIGMA_STAR,
    )
    @ pynini.cdrewrite(
        pynini.cross("꧀ꦢ꦳", "ða"),
        "",
        pynini.union(
            AKSARA_ORA_SWARA,
            SANDHANGAN_PANYIGEGING_WANDA_ORA_PANGKON,
            PADA,
            PEPADAN,
            CONSONANTS,
            "[EOS]",
        ),
        SIGMA_STAR,
    )
    @ pynini.cdrewrite(
        pynini.cross("꧀ꦱ꦳", "ʃa"),
        "",
        pynini.union(
            AKSARA_ORA_SWARA,
            SANDHANGAN_PANYIGEGING_WANDA_ORA_PANGKON,
            PADA,
            PEPADAN,
            CONSONANTS,
            "[EOS]",
        ),
        SIGMA_STAR,
    )
    @ pynini.cdrewrite(
        pynini.cross("꧀ꦥ꦳", "f/va"),
        "",
        pynini.union(
            AKSARA_ORA_SWARA,
            SANDHANGAN_PANYIGEGING_WANDA_ORA_PANGKON,
            PADA,
            PEPADAN,
            CONSONANTS,
            "[EOS]",
        ),
        SIGMA_STAR,
    )
    @ pynini.cdrewrite(
        pynini.cross("꧀ꦗ꦳", "za"),
        "",
        pynini.union(
            AKSARA_ORA_SWARA,
            SANDHANGAN_PANYIGEGING_WANDA_ORA_PANGKON,
            PADA,
            PEPADAN,
            CONSONANTS,
            "[EOS]",
        ),
        SIGMA_STAR,
    )
    @ pynini.cdrewrite(
        pynini.cross("꧀ꦒ꦳", "ɣa"),
        "",
        pynini.union(
            AKSARA_ORA_SWARA,
            SANDHANGAN_PANYIGEGING_WANDA_ORA_PANGKON,
            PADA,
            PEPADAN,
            CONSONANTS,
            "[EOS]",
        ),
        SIGMA_STAR,
    )
    @ pynini.cdrewrite(
        pynini.cross("꧀ꦔ꦳", "ʕa"),
        "",
        pynini.union(
            AKSARA_ORA_SWARA,
            SANDHANGAN_PANYIGEGING_WANDA_ORA_PANGKON,
            PADA,
            PEPADAN,
            CONSONANTS,
            "[EOS]",
        ),
        SIGMA_STAR,
    )
    @ pynini.cdrewrite(pynini.cross("ꦾ", "j"), "", "", SIGMA_STAR,)
    @ pynini.cdrewrite(pynini.cross("ꦿ", "r"), "", "", SIGMA_STAR)
    @ pynini.cdrewrite(pynini.cross("꧀ꦭ", "l"), "", "", SIGMA_STAR)
    @ pynini.cdrewrite(pynini.cross("꧀ꦮ", "w"), "", "", SIGMA_STAR)
    @ pynini.cdrewrite(pynini.cross("꧀ꦲ", "(h)"), "", "", SIGMA_STAR)
    @ pynini.cdrewrite(pynini.cross("꧀ꦤ", "n"), "", "", SIGMA_STAR)
    @ pynini.cdrewrite(pynini.cross("꧀ꦕ", "tʃ"), "", "", SIGMA_STAR)
    @ pynini.cdrewrite(pynini.cross("꧀ꦫ", "r"), "", "", SIGMA_STAR)
    @ pynini.cdrewrite(pynini.cross("꧀ꦏ", "k"), "", "", SIGMA_STAR)
    @ pynini.cdrewrite(pynini.cross("꧀ꦢ", "d̪"), "", "", SIGMA_STAR)
    @ pynini.cdrewrite(pynini.cross("꧀ꦠ", "t̪"), "", "", SIGMA_STAR)
    @ pynini.cdrewrite(pynini.cross("꧀ꦱ", "s"), "", "", SIGMA_STAR)
    @ pynini.cdrewrite(pynini.cross("꧀ꦮ", "w"), "", "", SIGMA_STAR)
    @ pynini.cdrewrite(pynini.cross("꧀ꦭ", "l"), "", "", SIGMA_STAR)
    @ pynini.cdrewrite(pynini.cross("꧀ꦥ", "p"), "", "", SIGMA_STAR)
    @ pynini.cdrewrite(pynini.cross("꧀ꦝ", "ɖ"), "", "", SIGMA_STAR)
    @ pynini.cdrewrite(pynini.cross("꧀ꦗ", "dʒ"), "", "", SIGMA_STAR)
    @ pynini.cdrewrite(pynini.cross("꧀ꦪ", "j"), "", "", SIGMA_STAR)
    @ pynini.cdrewrite(pynini.cross("꧀ꦚ", "ɲ"), "", "", SIGMA_STAR)
    @ pynini.cdrewrite(pynini.cross("꧀ꦩ", "m"), "", "", SIGMA_STAR)
    @ pynini.cdrewrite(pynini.cross("꧀ꦒ", "g"), "", "", SIGMA_STAR)
    @ pynini.cdrewrite(pynini.cross("꧀ꦧ", "b"), "", "", SIGMA_STAR)
    @ pynini.cdrewrite(pynini.cross("꧀ꦛ", "ʈ"), "", "", SIGMA_STAR)
    @ pynini.cdrewrite(pynini.cross("꧀ꦔ", "ŋ"), "", "", SIGMA_STAR)
    @ pynini.cdrewrite(pynini.cross("꧀ꦟ", "n"), "", "", SIGMA_STAR)
    @ pynini.cdrewrite(pynini.cross("꧀ꦖ", "tʃ"), "", "", SIGMA_STAR)
    @ pynini.cdrewrite(pynini.cross("꧀ꦬ", "r"), "", "", SIGMA_STAR)
    @ pynini.cdrewrite(pynini.cross("꧀ꦑ", "k"), "", "", SIGMA_STAR)
    @ pynini.cdrewrite(pynini.cross("꧀ꦡ", "t̪"), "", "", SIGMA_STAR)
    @ pynini.cdrewrite(pynini.cross("꧀ꦯ", "s"), "", "", SIGMA_STAR)
    @ pynini.cdrewrite(pynini.cross("꧀ꦦ", "p"), "", "", SIGMA_STAR)
    @ pynini.cdrewrite(pynini.cross("꧀ꦘ", "ɲ"), "", "", SIGMA_STAR)
    @ pynini.cdrewrite(pynini.cross("꧀ꦓ", "g"), "", "", SIGMA_STAR)
    @ pynini.cdrewrite(pynini.cross("꧀ꦨ", "b"), "", "", SIGMA_STAR)
    @ pynini.cdrewrite(pynini.cross("꧀ꦣ", "d"), "", "", SIGMA_STAR)
    @ pynini.cdrewrite(pynini.cross("꧀ꦰ", "s"), "", "", SIGMA_STAR)
    @ pynini.cdrewrite(pynini.cross("꧀ꦞ", "ɖ"), "", "", SIGMA_STAR)
    @ pynini.cdrewrite(pynini.cross("꧀ꦙ", "dʒ"), "", "", SIGMA_STAR)
    @ pynini.cdrewrite(pynini.cross("꧀ꦜ", "ʈ"), "", "", SIGMA_STAR)
    @ pynini.cdrewrite(pynini.cross("꧀ꦲ꦳", "ħ"), "", "", SIGMA_STAR)
    @ pynini.cdrewrite(pynini.cross("꧀ꦏ꦳", "x"), "", "", SIGMA_STAR)
    @ pynini.cdrewrite(pynini.cross("꧀ꦐ", "q"), "", "", SIGMA_STAR)
    @ pynini.cdrewrite(pynini.cross("꧀ꦢ꦳", "ð"), "", "", SIGMA_STAR)
    @ pynini.cdrewrite(pynini.cross("꧀ꦱ꦳", "ʃ"), "", "", SIGMA_STAR)
    @ pynini.cdrewrite(pynini.cross("꧀ꦥ꦳", "f/v"), "", "", SIGMA_STAR)
    @ pynini.cdrewrite(pynini.cross("꧀ꦗ꦳", "z"), "", "", SIGMA_STAR)
    @ pynini.cdrewrite(pynini.cross("꧀ꦒ꦳", "ɣ"), "", "", SIGMA_STAR)
    @ pynini.cdrewrite(pynini.cross("꧀ꦔ꦳", "ʕ"), "", "", SIGMA_STAR)
    # SANDHANGAN_PANYIGEGING_WANDA
    @ pynini.cdrewrite(pynini.cross("ꦀ", "m"), "", "", SIGMA_STAR,)
    @ pynini.cdrewrite(pynini.cross("ꦁ", "ŋ"), "", "", SIGMA_STAR)
    @ pynini.cdrewrite(pynini.cross("ꦂ", "r"), "", "", SIGMA_STAR)
    @ pynini.cdrewrite(pynini.cross("ꦃ", "h"), "", "", SIGMA_STAR)
    # SANDHANGAN_SWARA
    @ pynini.cdrewrite(pynini.cross("ꦶ", "i"), "", "", SIGMA_STAR)
    @ pynini.cdrewrite(pynini.cross("ꦸ", "u"), "", "", SIGMA_STAR)
    @ pynini.cdrewrite(pynini.cross("ꦺꦴ", "o"), "", "", SIGMA_STAR)
    @ pynini.cdrewrite(pynini.cross("ꦻꦴ", "aw"), "", "", SIGMA_STAR)
    @ pynini.cdrewrite(pynini.cross("ꦺ", "e"), "", "", SIGMA_STAR)
    @ pynini.cdrewrite(pynini.cross("ꦼꦴ", "ɨ"), "", "", SIGMA_STAR)
    @ pynini.cdrewrite(pynini.cross("ꦼ", "ə"), "", "", SIGMA_STAR)
    @ pynini.cdrewrite(pynini.cross("ꦴ", "aː"), "", "", SIGMA_STAR)
    @ pynini.cdrewrite(pynini.cross("ꦷ", "iː"), "", "", SIGMA_STAR)
    @ pynini.cdrewrite(pynini.cross("ꦹ", "uː"), "", "", SIGMA_STAR)
    @ pynini.cdrewrite(pynini.cross("ꦻ", "aj"), "", "", SIGMA_STAR)
    # AKSARA CONSONANT + VOWEL
    @ pynini.cdrewrite(
        pynini.cross("ꦲ", "(h)a"),
        "",
        pynini.union(
            AKSARA_ORA_SWARA,
            SANDHANGAN_PANYIGEGING_WANDA_ORA_PANGKON,
            PADA,
            PEPADAN,
            "[EOS]",
        ),
        SIGMA_STAR,
    )
    @ pynini.cdrewrite(
        pynini.cross("ꦤ", "na"),
        "",
        pynini.union(
            AKSARA_ORA_SWARA,
            SANDHANGAN_PANYIGEGING_WANDA_ORA_PANGKON,
            PADA,
            PEPADAN,
            "[EOS]",
        ),
        SIGMA_STAR,
    )
    @ pynini.cdrewrite(
        pynini.cross("ꦕ", "tʃa"),
        "",
        pynini.union(
            AKSARA_ORA_SWARA,
            SANDHANGAN_PANYIGEGING_WANDA_ORA_PANGKON,
            PADA,
            PEPADAN,
            "[EOS]",
        ),
        SIGMA_STAR,
    )
    @ pynini.cdrewrite(
        pynini.cross("ꦫ", "ra"),
        "",
        pynini.union(
            AKSARA_ORA_SWARA,
            SANDHANGAN_PANYIGEGING_WANDA_ORA_PANGKON,
            PADA,
            PEPADAN,
            "[EOS]",
        ),
        SIGMA_STAR,
    )
    @ pynini.cdrewrite(
        pynini.cross("ꦏ", "ka"),
        "",
        pynini.union(
            AKSARA_ORA_SWARA,
            SANDHANGAN_PANYIGEGING_WANDA_ORA_PANGKON,
            PADA,
            PEPADAN,
            "[EOS]",
        ),
        SIGMA_STAR,
    )
    @ pynini.cdrewrite(
        pynini.cross("ꦢ", "d̪a"),
        "",
        pynini.union(
            AKSARA_ORA_SWARA,
            SANDHANGAN_PANYIGEGING_WANDA_ORA_PANGKON,
            PADA,
            PEPADAN,
            "[EOS]",
        ),
        SIGMA_STAR,
    )
    @ pynini.cdrewrite(
        pynini.cross("ꦠ", "t̪a"),
        "",
        pynini.union(
            AKSARA_ORA_SWARA,
            SANDHANGAN_PANYIGEGING_WANDA_ORA_PANGKON,
            PADA,
            PEPADAN,
            "[EOS]",
        ),
        SIGMA_STAR,
    )
    @ pynini.cdrewrite(
        pynini.cross("ꦱ", "sa"),
        "",
        pynini.union(
            AKSARA_ORA_SWARA,
            SANDHANGAN_PANYIGEGING_WANDA_ORA_PANGKON,
            PADA,
            PEPADAN,
            "[EOS]",
        ),
        SIGMA_STAR,
    )
    @ pynini.cdrewrite(
        pynini.cross("ꦮ", "wa"),
        "",
        pynini.union(
            AKSARA_ORA_SWARA,
            SANDHANGAN_PANYIGEGING_WANDA_ORA_PANGKON,
            PADA,
            PEPADAN,
            "[EOS]",
        ),
        SIGMA_STAR,
    )
    @ pynini.cdrewrite(
        pynini.cross("ꦭ", "la"),
        "",
        pynini.union(
            AKSARA_ORA_SWARA,
            SANDHANGAN_PANYIGEGING_WANDA_ORA_PANGKON,
            PADA,
            PEPADAN,
            "[EOS]",
        ),
        SIGMA_STAR,
    )
    @ pynini.cdrewrite(
        pynini.cross("ꦥ", "pa"),
        "",
        pynini.union(
            AKSARA_ORA_SWARA,
            SANDHANGAN_PANYIGEGING_WANDA_ORA_PANGKON,
            PADA,
            PEPADAN,
            "[EOS]",
        ),
        SIGMA_STAR,
    )
    @ pynini.cdrewrite(
        pynini.cross("ꦝ", "ɖa"),
        "",
        pynini.union(
            AKSARA_ORA_SWARA,
            SANDHANGAN_PANYIGEGING_WANDA_ORA_PANGKON,
            PADA,
            PEPADAN,
            "[EOS]",
        ),
        SIGMA_STAR,
    )
    @ pynini.cdrewrite(
        pynini.cross("ꦗ", "dʒa"),
        "",
        pynini.union(
            AKSARA_ORA_SWARA,
            SANDHANGAN_PANYIGEGING_WANDA_ORA_PANGKON,
            PADA,
            PEPADAN,
            "[EOS]",
        ),
        SIGMA_STAR,
    )
    @ pynini.cdrewrite(
        pynini.cross("ꦪ", "ja"),
        "",
        pynini.union(
            AKSARA_ORA_SWARA,
            SANDHANGAN_PANYIGEGING_WANDA_ORA_PANGKON,
            PADA,
            PEPADAN,
            "[EOS]",
        ),
        SIGMA_STAR,
    )
    @ pynini.cdrewrite(
        pynini.cross("ꦚ", "ɲa"),
        "",
        pynini.union(
            AKSARA_ORA_SWARA,
            SANDHANGAN_PANYIGEGING_WANDA_ORA_PANGKON,
            PADA,
            PEPADAN,
            "[EOS]",
        ),
        SIGMA_STAR,
    )
    @ pynini.cdrewrite(
        pynini.cross("ꦩ", "ma"),
        "",
        pynini.union(
            AKSARA_ORA_SWARA,
            SANDHANGAN_PANYIGEGING_WANDA_ORA_PANGKON,
            PADA,
            PEPADAN,
            "[EOS]",
        ),
        SIGMA_STAR,
    )
    @ pynini.cdrewrite(
        pynini.cross("ꦒ", "ga"),
        "",
        pynini.union(
            AKSARA_ORA_SWARA,
            SANDHANGAN_PANYIGEGING_WANDA_ORA_PANGKON,
            PADA,
            PEPADAN,
            "[EOS]",
        ),
        SIGMA_STAR,
    )
    @ pynini.cdrewrite(
        pynini.cross("ꦧ", "ba"),
        "",
        pynini.union(
            AKSARA_ORA_SWARA,
            SANDHANGAN_PANYIGEGING_WANDA_ORA_PANGKON,
            PADA,
            PEPADAN,
            "[EOS]",
        ),
        SIGMA_STAR,
    )
    @ pynini.cdrewrite(
        pynini.cross("ꦛ", "ʈa"),
        "",
        pynini.union(
            AKSARA_ORA_SWARA,
            SANDHANGAN_PANYIGEGING_WANDA_ORA_PANGKON,
            PADA,
            PEPADAN,
            "[EOS]",
        ),
        SIGMA_STAR,
    )
    @ pynini.cdrewrite(
        pynini.cross("ꦔ", "ŋa"),
        "",
        pynini.union(
            AKSARA_ORA_SWARA,
            SANDHANGAN_PANYIGEGING_WANDA_ORA_PANGKON,
            PADA,
            PEPADAN,
            "[EOS]",
        ),
        SIGMA_STAR,
    )
    @ pynini.cdrewrite(
        pynini.cross("ꦟ", "na"),
        "",
        pynini.union(
            AKSARA_ORA_SWARA,
            SANDHANGAN_PANYIGEGING_WANDA_ORA_PANGKON,
            PADA,
            PEPADAN,
            "[EOS]",
        ),
        SIGMA_STAR,
    )
    @ pynini.cdrewrite(
        pynini.cross("ꦖ", "tʃa"),
        "",
        pynini.union(
            AKSARA_ORA_SWARA,
            SANDHANGAN_PANYIGEGING_WANDA_ORA_PANGKON,
            PADA,
            PEPADAN,
            "[EOS]",
        ),
        SIGMA_STAR,
    )
    @ pynini.cdrewrite(
        pynini.cross("ꦬ", "ra"),
        "",
        pynini.union(
            AKSARA_ORA_SWARA,
            SANDHANGAN_PANYIGEGING_WANDA_ORA_PANGKON,
            PADA,
            PEPADAN,
            "[EOS]",
        ),
        SIGMA_STAR,
    )
    @ pynini.cdrewrite(
        pynini.cross("ꦑ", "ka"),
        "",
        pynini.union(
            AKSARA_ORA_SWARA,
            SANDHANGAN_PANYIGEGING_WANDA_ORA_PANGKON,
            PADA,
            PEPADAN,
            "[EOS]",
        ),
        SIGMA_STAR,
    )
    @ pynini.cdrewrite(
        pynini.cross("ꦡ", "t̪a"),
        "",
        pynini.union(
            AKSARA_ORA_SWARA,
            SANDHANGAN_PANYIGEGING_WANDA_ORA_PANGKON,
            PADA,
            PEPADAN,
            "[EOS]",
        ),
        SIGMA_STAR,
    )
    @ pynini.cdrewrite(
        pynini.cross("ꦯ", "sa"),
        "",
        pynini.union(
            AKSARA_ORA_SWARA,
            SANDHANGAN_PANYIGEGING_WANDA_ORA_PANGKON,
            PADA,
            PEPADAN,
            "[EOS]",
        ),
        SIGMA_STAR,
    )
    @ pynini.cdrewrite(
        pynini.cross("ꦦ", "pa"),
        "",
        pynini.union(
            AKSARA_ORA_SWARA,
            SANDHANGAN_PANYIGEGING_WANDA_ORA_PANGKON,
            PADA,
            PEPADAN,
            "[EOS]",
        ),
        SIGMA_STAR,
    )
    @ pynini.cdrewrite(
        pynini.cross("ꦘ", "ɲa"),
        "",
        pynini.union(
            AKSARA_ORA_SWARA,
            SANDHANGAN_PANYIGEGING_WANDA_ORA_PANGKON,
            PADA,
            PEPADAN,
            "[EOS]",
        ),
        SIGMA_STAR,
    )
    @ pynini.cdrewrite(
        pynini.cross("ꦓ", "ga"),
        "",
        pynini.union(
            AKSARA_ORA_SWARA,
            SANDHANGAN_PANYIGEGING_WANDA_ORA_PANGKON,
            PADA,
            PEPADAN,
            "[EOS]",
        ),
        SIGMA_STAR,
    )
    @ pynini.cdrewrite(
        pynini.cross("ꦨ", "ba"),
        "",
        pynini.union(
            AKSARA_ORA_SWARA,
            SANDHANGAN_PANYIGEGING_WANDA_ORA_PANGKON,
            PADA,
            PEPADAN,
            "[EOS]",
        ),
        SIGMA_STAR,
    )
    @ pynini.cdrewrite(
        pynini.cross("ꦣ", "da"),
        "",
        pynini.union(
            AKSARA_ORA_SWARA,
            SANDHANGAN_PANYIGEGING_WANDA_ORA_PANGKON,
            PADA,
            PEPADAN,
            "[EOS]",
        ),
        SIGMA_STAR,
    )
    @ pynini.cdrewrite(
        pynini.cross("ꦰ", "sa"),
        "",
        pynini.union(
            AKSARA_ORA_SWARA,
            SANDHANGAN_PANYIGEGING_WANDA_ORA_PANGKON,
            PADA,
            PEPADAN,
            "[EOS]",
        ),
        SIGMA_STAR,
    )
    @ pynini.cdrewrite(
        pynini.cross("ꦞ", "ɖa"),
        "",
        pynini.union(
            AKSARA_ORA_SWARA,
            SANDHANGAN_PANYIGEGING_WANDA_ORA_PANGKON,
            PADA,
            PEPADAN,
            "[EOS]",
        ),
        SIGMA_STAR,
    )
    @ pynini.cdrewrite(
        pynini.cross("ꦙ", "dʒa"),
        "",
        pynini.union(
            AKSARA_ORA_SWARA,
            SANDHANGAN_PANYIGEGING_WANDA_ORA_PANGKON,
            PADA,
            PEPADAN,
            "[EOS]",
        ),
        SIGMA_STAR,
    )
    @ pynini.cdrewrite(
        pynini.cross("ꦜ", "ʈa"),
        "",
        pynini.union(
            AKSARA_ORA_SWARA,
            SANDHANGAN_PANYIGEGING_WANDA_ORA_PANGKON,
            PADA,
            PEPADAN,
            "[EOS]",
        ),
        SIGMA_STAR,
    )
    @ pynini.cdrewrite(
        pynini.cross("ꦲ꦳", "ħa"),
        "",
        pynini.union(
            AKSARA_ORA_SWARA,
            SANDHANGAN_PANYIGEGING_WANDA_ORA_PANGKON,
            PADA,
            PEPADAN,
            "[EOS]",
        ),
        SIGMA_STAR,
    )
    @ pynini.cdrewrite(
        pynini.cross("ꦏ꦳", "xa"),
        "",
        pynini.union(
            AKSARA_ORA_SWARA,
            SANDHANGAN_PANYIGEGING_WANDA_ORA_PANGKON,
            PADA,
            PEPADAN,
            "[EOS]",
        ),
        SIGMA_STAR,
    )
    @ pynini.cdrewrite(
        pynini.cross("ꦐ", "qa"),
        "",
        pynini.union(
            AKSARA_ORA_SWARA,
            SANDHANGAN_PANYIGEGING_WANDA_ORA_PANGKON,
            PADA,
            PEPADAN,
            "[EOS]",
        ),
        SIGMA_STAR,
    )
    @ pynini.cdrewrite(
        pynini.cross("ꦢ꦳", "ða"),
        "",
        pynini.union(
            AKSARA_ORA_SWARA,
            SANDHANGAN_PANYIGEGING_WANDA_ORA_PANGKON,
            PADA,
            PEPADAN,
            "[EOS]",
        ),
        SIGMA_STAR,
    )
    @ pynini.cdrewrite(
        pynini.cross("ꦱ꦳", "ʃa"),
        "",
        pynini.union(
            AKSARA_ORA_SWARA,
            SANDHANGAN_PANYIGEGING_WANDA_ORA_PANGKON,
            PADA,
            PEPADAN,
            "[EOS]",
        ),
        SIGMA_STAR,
    )
    @ pynini.cdrewrite(
        pynini.cross("ꦥ꦳", "f/va"),
        "",
        pynini.union(
            AKSARA_ORA_SWARA,
            SANDHANGAN_PANYIGEGING_WANDA_ORA_PANGKON,
            PADA,
            PEPADAN,
            "[EOS]",
        ),
        SIGMA_STAR,
    )
    @ pynini.cdrewrite(
        pynini.cross("ꦗ꦳", "za"),
        "",
        pynini.union(
            AKSARA_ORA_SWARA,
            SANDHANGAN_PANYIGEGING_WANDA_ORA_PANGKON,
            PADA,
            PEPADAN,
            "[EOS]",
        ),
        SIGMA_STAR,
    )
    @ pynini.cdrewrite(
        pynini.cross("ꦒ꦳", "ɣa"),
        "",
        pynini.union(
            AKSARA_ORA_SWARA,
            SANDHANGAN_PANYIGEGING_WANDA_ORA_PANGKON,
            PADA,
            PEPADAN,
            "[EOS]",
        ),
        SIGMA_STAR,
    )
    @ pynini.cdrewrite(
        pynini.cross("ꦔ꦳", "ʕa"),
        "",
        pynini.union(
            AKSARA_ORA_SWARA,
            SANDHANGAN_PANYIGEGING_WANDA_ORA_PANGKON,
            PADA,
            PEPADAN,
            "[EOS]",
        ),
        SIGMA_STAR,
    )
    # PANGKON
    @ pynini.cdrewrite(pynini.cross("꧀", ""), "", "", SIGMA_STAR)
    # AKSARA SWARA
    @ pynini.cdrewrite(pynini.cross("ꦄ", "a"), "", "", SIGMA_STAR)
    @ pynini.cdrewrite(pynini.cross("ꦆ", "i"), "", "", SIGMA_STAR)
    @ pynini.cdrewrite(pynini.cross("ꦈ", "u"), "", "", SIGMA_STAR)
    @ pynini.cdrewrite(pynini.cross("ꦉ", "rə"), "", "", SIGMA_STAR)
    @ pynini.cdrewrite(pynini.cross("ꦊ", "lə"), "", "", SIGMA_STAR)
    @ pynini.cdrewrite(pynini.cross("ꦌ", "e"), "", "", SIGMA_STAR)
    @ pynini.cdrewrite(pynini.cross("ꦎ", "o"), "", "", SIGMA_STAR)
    @ pynini.cdrewrite(pynini.cross("ꦄꦴ", "aː"), "", "", SIGMA_STAR)
    @ pynini.cdrewrite(pynini.cross("ꦇ", "iː"), "", "", SIGMA_STAR)
    @ pynini.cdrewrite(pynini.cross("ꦈꦴ", "uː"), "", "", SIGMA_STAR)
    @ pynini.cdrewrite(pynini.cross("ꦉꦴ", "ɻ̩ː"), "", "", SIGMA_STAR)
    @ pynini.cdrewrite(pynini.cross("ꦋ", "l̩ː"), "", "", SIGMA_STAR)
    @ pynini.cdrewrite(pynini.cross("ꦍ", "aj"), "", "", SIGMA_STAR)
    @ pynini.cdrewrite(pynini.cross("ꦎꦴ", "aw"), "", "", SIGMA_STAR)
    # AKSARA ROOT CONSONANT SANS VOWEL
    @ pynini.cdrewrite(pynini.cross("ꦲ", "(h)a"), "", "", SIGMA_STAR)
    @ pynini.cdrewrite(pynini.cross("ꦤ", "na"), "", "", SIGMA_STAR)
    @ pynini.cdrewrite(pynini.cross("ꦕ", "tʃa"), "", "", SIGMA_STAR)
    @ pynini.cdrewrite(pynini.cross("ꦫ", "ra"), "", "", SIGMA_STAR)
    @ pynini.cdrewrite(pynini.cross("ꦏ", "ka"), "", "", SIGMA_STAR)
    @ pynini.cdrewrite(pynini.cross("ꦢ", "d̪a"), "", "", SIGMA_STAR)
    @ pynini.cdrewrite(pynini.cross("ꦠ", "t̪a"), "", "", SIGMA_STAR)
    @ pynini.cdrewrite(pynini.cross("ꦱ", "sa"), "", "", SIGMA_STAR)
    @ pynini.cdrewrite(pynini.cross("ꦮ", "wa"), "", "", SIGMA_STAR)
    @ pynini.cdrewrite(pynini.cross("ꦭ", "la"), "", "", SIGMA_STAR)
    @ pynini.cdrewrite(pynini.cross("ꦥ", "pa"), "", "", SIGMA_STAR)
    @ pynini.cdrewrite(pynini.cross("ꦝ", "ɖa"), "", "", SIGMA_STAR)
    @ pynini.cdrewrite(pynini.cross("ꦗ", "dʒa"), "", "", SIGMA_STAR)
    @ pynini.cdrewrite(pynini.cross("ꦪ", "ja"), "", "", SIGMA_STAR)
    @ pynini.cdrewrite(pynini.cross("ꦚ", "ɲa"), "", "", SIGMA_STAR)
    @ pynini.cdrewrite(pynini.cross("ꦩ", "ma"), "", "", SIGMA_STAR)
    @ pynini.cdrewrite(pynini.cross("ꦒ", "ga"), "", "", SIGMA_STAR)
    @ pynini.cdrewrite(pynini.cross("ꦧ", "ba"), "", "", SIGMA_STAR)
    @ pynini.cdrewrite(pynini.cross("ꦛ", "ʈa"), "", "", SIGMA_STAR)
    @ pynini.cdrewrite(pynini.cross("ꦔ", "ŋa"), "", "", SIGMA_STAR)
    @ pynini.cdrewrite(pynini.cross("ꦟ", "na"), "", "", SIGMA_STAR)
    @ pynini.cdrewrite(pynini.cross("ꦖ", "tʃa"), "", "", SIGMA_STAR)
    @ pynini.cdrewrite(pynini.cross("ꦬ", "ra"), "", "", SIGMA_STAR)
    @ pynini.cdrewrite(pynini.cross("ꦑ", "ka"), "", "", SIGMA_STAR)
    @ pynini.cdrewrite(pynini.cross("ꦡ", "t̪a"), "", "", SIGMA_STAR)
    @ pynini.cdrewrite(pynini.cross("ꦯ", "sa"), "", "", SIGMA_STAR)
    @ pynini.cdrewrite(pynini.cross("ꦦ", "pa"), "", "", SIGMA_STAR)
    @ pynini.cdrewrite(pynini.cross("ꦘ", "ɲa"), "", "", SIGMA_STAR)
    @ pynini.cdrewrite(pynini.cross("ꦓ", "ga"), "", "", SIGMA_STAR)
    @ pynini.cdrewrite(pynini.cross("ꦨ", "ba"), "", "", SIGMA_STAR)
    @ pynini.cdrewrite(pynini.cross("ꦣ", "da"), "", "", SIGMA_STAR)
    @ pynini.cdrewrite(pynini.cross("ꦰ", "sa"), "", "", SIGMA_STAR)
    @ pynini.cdrewrite(pynini.cross("ꦞ", "ɖa"), "", "", SIGMA_STAR)
    @ pynini.cdrewrite(pynini.cross("ꦙ", "dʒa"), "", "", SIGMA_STAR)
    @ pynini.cdrewrite(pynini.cross("ꦜ", "ʈa"), "", "", SIGMA_STAR)
    @ pynini.cdrewrite(pynini.cross("ꦲ꦳", "ħa"), "", "", SIGMA_STAR)
    @ pynini.cdrewrite(pynini.cross("ꦏ꦳", "xa"), "", "", SIGMA_STAR)
    @ pynini.cdrewrite(pynini.cross("ꦐ", "qa"), "", "", SIGMA_STAR)
    @ pynini.cdrewrite(pynini.cross("ꦢ꦳", "ða"), "", "", SIGMA_STAR)
    @ pynini.cdrewrite(pynini.cross("ꦱ꦳", "ʃa"), "", "", SIGMA_STAR)
    @ pynini.cdrewrite(pynini.cross("ꦥ꦳", "f/va"), "", "", SIGMA_STAR)
    @ pynini.cdrewrite(pynini.cross("ꦗ꦳", "za"), "", "", SIGMA_STAR)
    @ pynini.cdrewrite(pynini.cross("ꦒ꦳", "ɣa"), "", "", SIGMA_STAR)
    @ pynini.cdrewrite(pynini.cross("ꦔ꦳", "ʕa"), "", "", SIGMA_STAR)
).optimize()


def map_jv_to_ipa(istring: str) -> str:
    """Applies the Javanese script to IPA equivalent mapping rules.

    Args:
      istring: the Javanese script graphemic input string.

    Returns:
      The Javanese script's IPA output string.

    Raises.
      rewrite.Error: composition failure.
    """
    return rewrite.one_top_rewrite(istring, ANGKA_LAN_PADA @ AKSARA_2_IPA)

