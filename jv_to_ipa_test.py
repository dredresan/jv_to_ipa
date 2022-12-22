import unittest
from jv_to_ipa import map_jv_to_ipa


class TranslitTest(unittest.TestCase):
    def rewrites(self, string, expected_string):
        mapped_string = map_jv_to_ipa(string)
        self.assertEqual(mapped_string, expected_string)

    # Test Aksara Consonants
    def test_nglegena(self):
        self.rewrites("ꦲ", "(h)a")

    def test_murda(self):
        self.rewrites("ꦨ", "ba")

    def test_mahaprana(self):
        self.rewrites("ꦰ", "sa")

    def test_rekan(self):
        self.rewrites("ꦏ꦳", "xa")

    # Test Sandhangan Swara
    def test_inherent_a_vowel(self):
        self.rewrites("ꦲ", "(h)a")

    def test_i(self):
        self.rewrites("ꦲꦶꦲꦶꦲꦶ", "(h)i(h)i(h)i")

    def test_u(self):
        self.rewrites("ꦲꦸꦲꦸꦲꦸ", "(h)u(h)u(h)u")

    def test_o(self):
        self.rewrites("ꦲꦺꦴꦲꦺꦴꦲꦺꦴ", "(h)o(h)o(h)o")

    def test_e(self):
        self.rewrites("ꦲꦺ", "(h)e")

    def test_ə(self):
        self.rewrites("ꦲꦼ", "(h)ə")

    def test_a_panjang(self):
        self.rewrites("ꦲꦴ", "(h)aː")

    def test_i_panjang(self):
        self.rewrites("ꦲꦷ", "(h)iː")

    def test_u_panjang(self):
        self.rewrites("ꦲꦹ", "(h)uː")

    def test_aj(self):
        self.rewrites("ꦲꦻ", "(h)aj")

    def test_aw(self):
        self.rewrites("ꦲꦻꦴ", "(h)aw")

    def test_ɨ(self):
        self.rewrites("ꦲꦼꦴ", "(h)ɨ")

    # Test Sandhangan Panyigeging Wanda
    def test_syl_closure_m(self):
        self.rewrites("ꦲꦶꦀ", "(h)im")

    def test_syl_closure_ŋ(self):
        self.rewrites("ꦤꦁ", "naŋ")

    def test_syl_closure_r_1(self):
        self.rewrites("ꦏꦂ", "kar")

    def test_syl_closure_r_2(self):
        self.rewrites("ꦲꦶꦂ", "(h)ir")

    def test_syl_closure_h(self):
        self.rewrites("ꦏꦃ", "kah")

    def test_pangkon(self):
        self.rewrites(
            "ꦤ꧀", "n",
        )

    def test_kraton(self):
        self.rewrites("ꦏꦿꦠꦺꦴꦤ꧀", "krat̪on")

    def test_harta(self):
        self.rewrites("ꦲꦂꦠ", "(h)art̪a")

    # Test Sandhangan Wyanjana
    def test_sw_ja(self):
        self.rewrites("ꦲꦾ", "(h)ja")

    def test_hjar(self):
        self.rewrites("ꦲꦾꦂ", "(h)jar")

    def test_hjir(self):
        self.rewrites("ꦲꦾꦶꦂ", "(h)jir")

    # Test Aksara Pasangan
    def test_hna(self):
        self.rewrites("ꦲ꧀ꦤ", "(h)na")

    def test_hni(self):
        self.rewrites("ꦲ꧀ꦤꦶ", "(h)ni")

    def test_aksara_pasangan_combo_1(self):
        self.rewrites("ꦲꦽꦀꦲꦾꦶ", "(h)rəm(h)ji")

    def test_aksara_pasangan_combo_2(self):
        self.rewrites("ꦲ꧀ꦤꦀ", "(h)nam")

    # Test Aksara Swara
    def test_as_om(self):
        self.rewrites("ꦎ", "o")

    def test_om(self):
        self.rewrites("ꦎꦀ", "om")

    # Test Angka
    def test_angka_pangkat(self):
        self.rewrites("ꦠꦁꦒꦭ꧀꧇꧑꧗꧇ꦗꦸꦤꦶ", "t̪aŋgal:17:dʒuni")

    def test_angka_lingsa(self):
        self.rewrites("ꦠꦁꦒꦭ꧀꧈꧑꧗꧈ꦗꦸꦤꦶ", "t̪aŋgal,17,dʒuni")

    # Test Correction
    def test_correction_yogyakarta(self):
        self.rewrites("ꦥꦢꦲꦸ꧞꧞꧞ꦭꦸꦲꦸꦂ", "pad̪a(h)u(Yogyakarta correction mark)lu(h)ur")

    def test_correction_surakarta(self):
        self.rewrites("ꦥꦢꦲꦸ꧟꧟꧟ꦭꦸꦲꦸꦂ", "pad̪a(h)u(Surakarta correction mark)lu(h)ur")

    # Test on Javanese Text with native punctuations
    def test_hanacaraka_sequence(self):
        self.rewrites(
            "ꦲꦤꦕꦫꦏꦢꦠꦱꦮꦭꦥꦝꦗꦪꦚꦩꦒꦧꦛꦔ", "(h)anatʃarakad̪at̪asawalapaɖadʒajaɲamagabaʈaŋa",
        )

    def test_sentence_1(self):
        self.rewrites(
            "꧅ꦭꦩꦸꦤ꧀ꦱꦶꦫꦔꦶꦔꦸꦏꦸꦕꦶꦁ꧈", "(higher rank letter intro)lamunsiraŋiŋukutʃiŋ,",
        )

    def test_serat_katuranggan_kucing_pada_7(self):
        self.rewrites(
            "꧅ꦭꦩꦸꦤ꧀ꦱꦶꦫꦔꦶꦔꦸꦏꦸꦕꦶꦁ꧈ꦲꦮꦏ꧀ꦏꦺꦲꦶꦉꦁꦱꦢꦪ꧈ꦭꦩ꧀ꦧꦸꦁꦏꦶꦮꦠꦺꦩ꧀ꦧꦺꦴꦁꦥꦸꦠꦶꦃ꧈ꦊꦏ꧀ꦱꦤ꧀ꦤꦶꦫꦥꦿꦪꦺꦴꦒ꧈ꦲꦫꦤ꧀ꦮꦸꦭꦤ꧀ꦏꦿꦲꦶꦤꦤ꧀꧈ꦠꦶꦤꦼꦏꦤꦤ꧀ꦱꦱꦼꦢꦾꦤ꧀ꦤꦶꦥꦸꦤ꧀꧈ꦪꦺꦤ꧀ꦧꦸꦟ꧀ꦝꦼꦭ꧀ꦭꦁꦏꦸꦁꦲꦸꦠꦩ꧈",
            "(higher rank letter intro)lamunsiraŋiŋukutʃiŋ,(h)awakke(h)irəŋsad̪aja,lambuŋkiwat̪emboŋput̪ih,ləksanniraprajoga,(h)aranwulankra(h)inan,t̪inəkanansasəd̪jannipun,jenbunɖəllaŋkuŋ(h)ut̪ama,",
        )

    def test_serat_katuranggan_kucing_pada_8(self):
        self.rewrites(
            "꧅ꦲꦗꦱꦶꦫꦔꦶꦔꦸꦏꦸꦕꦶꦁ꧈ꦭꦸꦫꦶꦏ꧀ꦲꦶꦉꦁꦧꦸꦤ꧀ꦠꦸꦠ꧀ꦥꦚ꧀ꦗꦁ꧈ꦥꦸꦤꦶꦏꦲꦮꦺꦴꦤ꧀ꦭꦩꦠ꧀ꦠꦺ꧈ꦱꦼꦏꦼꦭꦤ꧀ꦱꦿꦶꦁꦠꦸꦏꦂꦫꦤ꧀꧈ꦲꦫꦤ꧀ꦝꦣꦁꦱꦸꦁꦏꦮ꧈ꦥꦤ꧀ꦲꦢꦺꦴꦃꦫꦶꦗꦼꦏꦶꦤꦶꦥꦸꦤ꧀꧈ꦪꦺꦤ꧀ꦧꦸꦟ꧀ꦝꦼꦭ꧀ꦤꦺꦴꦫꦔꦥꦲ꧈",
            "(higher rank letter intro)(h)adʒasiraŋiŋukutʃiŋ,lurik(h)irəŋbunt̪ut̪paɲdʒaŋ,punika(h)awonlamat̪t̪e,səkəlansriŋt̪ukarran,(h)aranɖadaŋsuŋkawa,pan(h)ad̪ohridʒəkinipun,jenbunɖəlnoraŋapa(h)a,",
        )

    def test_kakawin_ramayana_pada_XVI_31(self):
        self.rewrites(
            "꧅ꦗꦲ꧀ꦤꦷꦪꦴꦲ꧀ꦤꦶꦁꦠꦭꦒꦏꦢꦶꦭꦔꦶꦠ꧀꧈ꦩꦩ꧀ꦧꦁꦠꦁꦥꦴꦱ꧀ꦮꦸꦭꦤꦸꦥꦩꦤꦶꦏꦴ꧈ꦮꦶꦤ꧀ꦠꦁꦠꦸꦭꦾꦁꦏꦸꦱꦸꦩꦪꦱꦸꦩꦮꦸꦫ꧀꧈ꦭꦸꦩꦿꦴꦥ꧀ꦮꦺꦏꦁꦱꦫꦶꦏꦢꦶꦗꦭꦢ꧉",
            "(higher rank letter intro)dʒa(h)niːjaː(h)niŋt̪alagakad̪ilaŋit̪,mambaŋt̪aŋpaːswulanupamanikaː,wint̪aŋt̪uljaŋkusumajasumawur,lumraːpwekaŋsarikad̪idʒalad̪a.",
        )


if __name__ == "__main__":
    unittest.main()
