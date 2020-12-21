import discord
from discord.ext import commands

from ..configs.constants import COLOUR
from ..utils import checks


class Amino(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.Cog.listener()
    async def on_ready(self):
        print(f"INFO: {__name__} is ready.")

    # GLOSS: "js" means "Just some", not "JavaScript".

    @commands.command(aliases=["jg", "jsg", "amino_guidelines", "ag"])
    @checks.is_jsguilds()
    @checks.is_mod()
    # @commands.cooldown(3, 60.0, commands.BucketType.user)
    async def jsguidelines(self, ctx):
        """Send an embed with (Amino) Just a chat... guidelines."""
        async with ctx.typing():
            natlangs = discord.Embed(title="Just some guidelines... (1/4)", colour=COLOUR)
            natlangs.add_field(name=":flag_gb::flag_us: English",
                               value="""The Amino's Guidelines apply here!
                                     Dark humor is tolerated, just don't offend anyone.
                                     Peace and love. Let's all be friends here! :D""")
            # Mandarin Chinese (Simplified)
            natlangs.add_field(name=":flag_cn: 普通话",
                               value="""「Amino」规则在这里适用！
                                     黑暗的幽默容忍在这里, 不要冒犯。
                                     安和爱。 让我们在这里成为朋友! :D""")
            # Mandarin Chinese (Traditional)
            natlangs.add_field(name=":flag_tw: 國語",
                               value="""「Amino」規則在這裡適用！
                                     黑暗的幽默容忍在這裡, 不要冒犯。
                                     安和愛。 讓我們在這裡成為朋友! :D""")
            # Spanish
            natlangs.add_field(name=":flag_ea: Español",
                               value="""¡Las reglas del Amino también se aplican aquí!
                                     Toleramos el humor negro, solo no ofendas a nadie.
                                     Paz y amor. ¡Seamos todos amigos! :D""")
            # French
            natlangs.add_field(name=":flag_fr: Français",
                               value="""Les règles de l'Amino s'appliquent ici !
                                     L'humour noir est toléré, ne blessez juste pas les gens.
                                     Paix et amour. Soyons tous amis ici ! :D""")
            # Portuguese
            natlangs.add_field(name=":flag_br::flag_pt: Português",
                               value="""As regras do Amino também aplicam-se aqui!
                                     Toleramos humor negro, só não ofenda(s) os outros.
                                     Paz e amor. Vamos todos ser amigos aqui! :D""")
            # Standard German
            natlangs.add_field(name=":flag_de: Deutsch",
                               value="""Die Regeln von diesem Amino gelten auch hier!
                                     Schwarzer Humor ist erlaubt, solange keine Menschen verletzt werden.
                                     Friede und Liebe. Lasst uns hier alle Freunde sein! :D""")
            # Japanese
            natlangs.add_field(name=":flag_jp: 日本語",
                               value="""「Amino」ガイドラインがここに適用されます！
                                     ダークユーモアは許容されます、唯誰かを怒らせないで下さい。
                                     平和と愛。ここでみんな友達になりましょう！ :D""")
            # Korean
            natlangs.add_field(name=":flag_kr: 한국말",
                               value="""아미노의 지침이 여기에 적용됩니다!
                                     어두운 유머는 용인되며 누구에게 화를 내지는 마시고.
                                     평화와 사랑. 여기서 모두 친구 되자! :D""")
            # Italian
            natlangs.add_field(name=":flag_it: Italiano",
                               value="""Le regole del Amino si applicano anche qui!
                                     L'umore nero è permesso, ma non offendere nessuno.
                                     Pace e amore. Siamo tutti amici! :D""")
            # Filipino
            natlangs.add_field(name=":flag_ph: Wikang Filipino",
                               value="""Dapat niyong sundin ang mga panuntunan ng Amino dito!
                                     Hindi bawal ang pagpapatawang itim, basta't walang asarin.
                                     Saya at ibig. Magkaibigan tayo dito! :D""")
            # Polish
            natlangs.add_field(name=":flag_pl: Polski",
                               value="""Zasady tego Amino obowiązują na tym czacie!
                                     Czarny humor jest tolerowany, tylko nikogo nie obrażaj.
                                     Pokój i miłość. Bądźmy tu kolegami! :D""")
            # Dutch
            natlangs.add_field(name=":flag_nl: Nederlands",
                               value="""De regels van de Amino zijn ook hier toegepast!
                                     Zwarte humor is toegestaan, maar kwetst niemand.
                                     Vrede en liefde. Laat ons vrienden zijn! :D""")
            # Romanian
            natlangs.add_field(name=":flag_md::flag_ro: Limbă română",
                               value="""Regulile Aminolui se aplică și aici!
                                     Umorul negru este permis, dar nu jigniți nimeni.
                                     Pace și dragoste. Fiți amici aici! :D""")
            # Greek
            natlangs.add_field(name=":flag_gr: Ελληνικά",
                               value="""Οι κανόνες αυτού του Άμινο ισχύουν σε αυτό το τσατ!
                                     Το κρύο χιούμορ υπομένεται, απλά μην προσβάλλετε κανέναν.
                                     Ειρήνη και αγάπη. Ας γίνουμε όλοι φίλοι εδώ! :D""")
            # Swedish
            # NOTE: The translator has said their translation isn't great,
            # so it'll stay as a comment until a better translation is made.
            # natlangs.add_field(name=":flag_fi::flag_se: Svenska",
            #                    value="""Amino reglerna gäller här!
            #                          Svart humor tolereras, bara stör ingen.
            #                          Fred ock kärlek. Låt oss vara vänner har! :D""")
            # Catalan
            natlangs.add_field(name=":flag_ad: Català",
                               value="""Les regles del Amino s'apliquen aquí!
                                     L'humor negre està permès, però no ofenguis ningú.
                                     Pau i amor. Siguem tots amics! :D""")
            # Guaraní
            natlangs.add_field(name=":flag_py: Avañe'ẽ",
                               value="""Amíno tekorã ojeporu ko'ápe avei!
                                     Ore rohechakuaáta tykue pytũ, anínte remoñemyrõi ambue tapicha.
                                     Py'aguapy ha mborayhu. Javy'ákena ko'ápe! :D""")
            # Lombard
            natlangs.add_field(name="Lombaard",
                               value="""I regol del Amino i se applichen anca chì!
                                     El humor negher a l’è permiss, ma offend minga nissun.
                                     Pas e amor. Siom tœcc amis chì! :D""")
            # ???: (Saxon) German?
            natlangs.add_field(name="Sächssch",
                               value="""De Räschln vom Amino gäldn a hior! Schworzer!
                                     Humor is erlabd, solang keene Mänschn vorledzd wärdn.
                                     Friede un Liebe. Lassd uns alle Freinde sein! :D""")
            # Galician
            natlangs.add_field(name="Galego",
                               value="""As regras do Amino tamén aplícanse aquí!
                                     O humor negro tolérase, mais non ofendades a ninguén.
                                     Paz e amor. Sexamos todos amigos! :D""")
            # Irish
            natlangs.add_field(name=":flag_ie: Gaeilge",
                               value="""Tá na rialacha an Amino i bhfeidhm anseo!
                                     Glactar le greann dubh, ach ná cuir múisiam ar dhuine ar bith.
                                     Suaimhneas agus grá. Lig dúinn go léir a bheith cairde anseo! :D󠁢""")
            # Comorian
            # NOTE: The Swahili translator's has a Comorian dialect,
            # so the translation may not be entirely accurate in Standard Swahili.
            natlangs.add_field(name=":flag_km::flag_yt: Shikomori",
                               value="""Na amino shariyah woe appliquées ici!
                                     Humour noiri je autorisé, sha namntsi blessé personne.
                                     Amani na kuishi. Sisi marafiki! :D""")
            # Basque
            natlangs.add_field(name="Euskara",
                               value="""Aminoaren erregelak hemen ere aplikatuak dira!
                                     Umore beltza onartua da, baina ez ofenditu.
                                     Bake eta maite. Lagunak izan! :D""")
            # Asturian
            natlangs.add_field(name="Asturianu",
                               value="""¡Les regles del Amino tamién aplíquense equí!
                                     L'humor negru está permitíu, pero non ofendáis a naide.
                                     Paz y amor. ¡Vamos ser toos amigos equí! :D""")

            natlangs_ext = discord.Embed(title="Just some guidelines... (2/4)", colour=COLOUR)
            # Picard
            natlangs_ext.add_field(name="Ch'ti Picard",
                                   value="""Chès règles del'Amino è s'applique ichi !
                                         Ch'noir humour y'est autorisé, faut juste pas faire d'maux à chès gins.
                                         L'paix et l'amour ichi. Gu'in sot amiteux tertous ! :D""")
            # Icelandic
            natlangs_ext.add_field(name=":flag_is: Íslenska",
                                   value="""Reglur af Amino eiga við öllum í þessum chat!
                                         Svartur humour er þolað, bara ekki móðga neinn.
                                         Friður og ást. Skulum vera frændur hér! :D""")
            # Occitan
            natlangs_ext.add_field(name="Occitan",
                                   value="""Las normas del'Amino s'aplicon aicí !
                                         L'umor nièr es tolerat, just non bleçatz los gents.
                                         Patz e amor. Siam tot amics aicí ! :D""")
            # Aragonese
            natlangs_ext.add_field(name="Aragonés",
                                   value="""As reglas d'o Amino tamién s'aplican astí!
                                         L'humor negro se permite, maguer no ofendaz a dengún.
                                         Paz y aimor. Imos ser totz amicos astí! :D""")
            # Spanglish
            natlangs_ext.add_field(name=":flag_pr: Spanglish",
                                   value="""Lah reglas del Amino aplayan aqi tambiem!
                                         He tolera humor negro, solo no ofend-a nadie.
                                         Paz y lof. Les ol bi frens! :D""")
            # Latin
            natlangs_ext.add_field(name=":flag_va: Lingua Latīna",
                                   value="""Rēgulae Aminī hīc applicantur quoque!
                                         Hūmor obscūrus permittitur, sed ne laeserītis populum.
                                         Pax et amor. Este amīcī! :D""")

            conlangs = discord.Embed(title="Just some guidelines... (3/4)", colour=COLOUR)
            conlangs.add_field(name="Adennoghion",
                               value="""Ze zodeoti Amino anei menotoledes!
                                     Mir'adaetu critimobru dorvodes, sco ciniomenote meci'so geigertico.
                                     Cimmorr o chomae. Chozenes anei essi! :D""")
            conlangs.add_field(name="Baleñero",
                               value="""O leyas de Amino se aplikan aki!
                                     E nero humor esa toleradi, to no offendan o otros.
                                     Pas y amor. Esamos todo lagunos aki! :D""")
            conlangs.add_field(name="Búuku",
                               value="""Búuku-wáá xumí txua paa’ú sákí xugá ‘áu háá!
                                     Gúi-gúi txua llúa xugá ‘áu xuwí. Tuña tidá gúmi ná biú.
                                     Suú muala xugá luwí-luwí. Suú ñúa’á xugá xumí ná nuxu! :D""")
            conlangs.add_field(name="Hilten",
                               value="""N̄on imsam Amino ecue iso fejjo ecue!
                                     Hakari moli tsiti ucuitsiti fahan̄, tsure on̄dui ato fahan̄ ejtsi moli.
                                     Sun̄n̄ura suan̄ moj maru. Rulejtsi mahu maru fejjo ecue! :D""")
            conlangs.add_field(name="Hẇv̈",
                               value="""ćq̃ c̈ńṅq d́q̈ d́sqć bỹ!
                                     ċqr̈s ḃv ʋ̌nć, q̃ŕ ćñ śqr̈ ỹsṁꞇ.
                                     d́q̈ pʋ́ ṅď̌. ř ỹq̌sḋ bỹ! :D""")
            conlangs.add_field(name="Iqglic",
                               value="""Rwlz ðu grwp prsn hixiq iz importent her!
                                     Dörk funynis iz okey, plyz köz nöt "sumbudy iz sad".
                                     Pys and luv. Plyz let "wy iz frenz" her! :D""")
            conlangs.add_field(name="Kwilo",
                               value="""Da pa o de Amino apik isi!
                                     Da shwas humo bi tolewans isi, jos no blese pipol.
                                     An e lib isi. Wi bi pwend beto! :D""")
            conlangs.add_field(name="Ndu Biliva",
                               value="""Bularu Vamimu mi rula lurawa bu ndu ba!
                                     Ndima munli ramba wuva ba. Wuva bularu li ba.
                                     Lamvi dida ridandi. Mimu bularu rami bu ba! :D""")
            conlangs.add_field(name="Okodan",
                               value="""Komeko Amino-Ikke keta hahā ef fika.
                                     Lakko bala ef teu, tayo imi(imy) mafa ach.
                                     Kemi teuta koni teu. Lalaik mam ach fika teu! :D""")
            conlangs.add_field(name="Ommem",
                               value="""’ꜛ3ꜛ1ꜜ2ꜛ4400  ꜜ50  ’ꜛ2ꜛ44ꜜ4ꜜ2ꜛ6ꜜ22  ꜜꜜ200！
                                     ꜛ3ꜜ1’0’ꜜ11  ꜜꜜ1’ꜛ2  ꜜ1ꜛ2ꜜ1’ꜛ1’  ’ꜛ3’  ꜜꜜ2ꜛ2  ꜛ66ꜜ50  ꜜ6  ꜜ2ꜛ550  ꜛ1ꜜ1ꜛ2ꜛ3’
                                     ꜛ44ꜜ11  0  ꜛ3ꜜ1’0’ .  ꜜꜜ2ꜛ2  ꜛ3ꜜ11ꜛ2  ꜜꜜ1 ꜜꜜ1 ꜜꜜ1ꜜ5ꜛ2ꜛ3’！:D""")
            conlangs.add_field(name="Ommem",
                               value="""Ŏfsmiitt irer Ŏmiimotss iisess!
                                     Ofm’em’oo lls’i salil’ ŏf’ iisi ottrer id ariit oroml’.
                                     Ossaa od ofm’em’. Iisi ofmmss iil iil iiloml’! :D""")
            conlangs.add_field(name="Oskibæ",
                               value="""Aminokoniqa bikamiwaan!
                                     Makadebaapiqa kaawaabam, inawisaki pemaadiw.
                                     Pankana o saakiqa. Waqndawbiqiikaanayaawaani! :D""")
            conlangs.add_field(name="Shinkokugo",
                               value="""Aminono famon kokoni fuitari!
                                     Suiwaraga kanyōreru, ikabasuyo jinwaku.
                                     Hyōka to ai. Ashisen tomo zeyo! :D""")
            conlangs.add_field(name="Sulioqaasiip",
                               value="""Aminolagatuq mannani lagatutoq!
                                     Qernerillarpuq mannami aaptut, inuiaatit naaanniaatkalargituusi!
                                     Pijairliuq aammaa asanninequq. Ikinngit agitugut! :D""")
            conlangs.add_field(name="Taot",
                               value="""Elwasnoo za Amino oolo rol phoon haok anna sewak.
                                     Seek woosthek rol tak, tas kheeyok so sees za.
                                     So pey loa toot. A rol sees zaaza noan! :D""")
            conlangs.add_field(name="Temalyi",
                               value="""Reeny, ddailyas aiwa teaminoddai bada!
                                     Masesami vosu hinyen, Churolyos tebeccha.
                                     Ameeplya chimee. Reeny malyalyas mechidi :D""")
            conlangs.add_field(name="toki pona",
                               value="""sitelen lawa pi tomo Amino li lon lon ni a!
                                     musi pakala li pona. taso o pakala toki ala tawa jan.
                                     pona en olin. o kama e jan pona a! :D""")
            conlangs.add_field(name="Tsun-Raj",
                               value="""Seuptsijlnok Baitsotew Xeaisas chutj taipnok!
                                     Nəptsak ruj kudan, temp ruk daib so-ap fesdpap.
                                     Bainr wər miŋ. Djeaix gemos wumk ŋaodj Cholas taipnok! :D""")
            conlangs.add_field(name="Ūareo Travi",
                               value="""Zhiyuneoda "Amino" do'ohokoanei!
                                     Oraseisatodaneiweá', neizhodan'aīe!
                                     Haòyeao'e'ai'oha, Yaikunako'itoyeaokoanei! :D""")
            conlangs.add_field(name="Vinlandic",
                               value="""De lága Aminoar framr he!
                                     Svártlátr em beþólet, þó ney miska fólk.
                                     Fríðr ok ástr. Ale erm frændr he! :D""")
            conlangs.add_field(name="VötGil",
                               value="""Löv​Zis​Vun​Ðyt​Prs​Grp​Viz​Vim​Cin​Ðis​Plw!
                                     Vöt​Wys​Fun​Nis​Viz​Key.​Nöt​Ply​Köz"​Cen​Prs​Viz​Vöt​Hap".
                                     Vöt​Wor​Van​Luv​Nis.Ply​Let​"Cöl​Nuy​Viz​Fen​Zis​"Cin​Ðis​Plw! :D""")
            conlangs.add_field(name="ⲘOΡΑΒИ",
                               value="""¡Ⲗαs ρиɣⲗαs Ⲇ̃ εⲗ Αⲙиⲛo S̃ απⲗиϧαⲛ ακи ταнεⲙ!
                                     Ⲙoz ταⲙиⲗαⲙos εⲗ uⲙoρ ⲇαϧκⲛo, soⲗo ⲛo ιραинεs ⲛατα.
                                     Sуⲗⲙα uε ⲙαuⲇα. ¡sεαⲙos τoⲇos αⲙεκos! :D""")
            conlangs.add_field(name="新国語",
                               value="""「Amino」拥法文此処在振用前!
                                     酸笑者寛容愔、怒不命人或。
                                     平和及愛。我全友是命! :D""")
            conlangs.add_field(name="강서말",
                               value="""아미노워 왕추미 죵댠!\n"
                                     운엥 유민 햐샌디, 걍 단 인간 환다메 학 마드레 망세비.
                                     픙대아 앙. 울 믇 치가 디쟈! :D""")
            conlangs.set_footer(text=f"Requested by {ctx.author.name}", icon_url=ctx.author.avatar_url)
            await ctx.send(embed=natlangs)
            await ctx.send(embed=natlangs_ext)
            await ctx.send(embed=conlangs)


def setup(bot):
    bot.add_cog(Amino(bot))
