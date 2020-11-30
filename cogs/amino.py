import discord
from discord.ext import commands

from just_a_bot.utils import checks


class Amino(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.Cog.listener()
    async def on_ready(self):
        print(f"INFO: {__name__} is ready.")

    # NOTE: "js" is the abbreviation "Just some", not "JavaScript".

    @commands.command(aliases=["jg", "jsg", "amino_guidelines", "ag"])
    @checks.is_admin()
    # @commands.cooldown(3, 60.0, commands.BucketType.user)
    @checks.is_jsguilds()
    async def jsguidelines(self, ctx):
        """Send an embed with (Amino) Just a chat... guidelines."""
        async with ctx.typing():
            natlangs = discord.Embed(title="Just some guidelines... (1/3)", colour=discord.Colour(0x8b0000))
            natlangs.add_field(name=":flag_gb::flag_us: English",
                               value="The Amino's Guidelines apply here!\n"
                                     "Dark humor is tolerated, just don't offend anyone.\n"
                                     "Peace and love. Let's all be friends here! :D")
            # Mandarin Chinese (Simplified)
            natlangs.add_field(name=":flag_cn: 普通话",
                               value="「Amino」规则在这里适用！\n"
                                     "黑暗的幽默容忍在这里, 不要冒犯。\n"
                                     "安和爱。 让我们在这里成为朋友! :D")
            # Mandarin Chinese (Traditional)
            natlangs.add_field(name=":flag_tw: 國語",
                               value="「Amino」規則在這裡適用！\n"
                                     "黑暗的幽默容忍在這裡, 不要冒犯。\n"
                                     "安和愛。 讓我們在這裡成為朋友! :D")
            # Spanish
            natlangs.add_field(name=":flag_ea: Español",
                               value="¡Las reglas del Amino también se aplican aquí!\n"
                                     "Toleramos el humor negro, solo no ofendas a nadie.\n"
                                     "Paz y amor. ¡Seamos todos amigos! :D")
            # French
            natlangs.add_field(name=":flag_fr: Français",
                               value="Les règles de l'Amino s'appliquent ici !\n"
                                     "L'humour noir est toléré, ne blessez juste pas les gens.\n"
                                     "Paix et amour. Soyons tous amis ici ! :D")
            # Portuguese
            natlangs.add_field(name=":flag_br::flag_pt: Português",
                               value="As regras do Amino também aplicam-se aqui!\n"
                                     "Toleramos humor negro, só não ofenda(s) os outros.\n"
                                     "Paz e amor. Vamos todos ser amigos aqui! :D")
            # Standard German
            natlangs.add_field(name=":flag_de: Deutsch",
                               value="Die Regeln von diesem Amino gelten auch hier!\n"
                                     "Schwarzer Humor ist erlaubt, solange keine Menschen verletzt werden.\n"
                                     "Friede und Liebe. Lasst uns hier alle Freunde sein! :D")
            # Swahili
            # NOTE: The Swahili translator's has a Comorian dialect,
            # so the translation may not be entirely accurate in Standard Swahili.
            natlangs.add_field(name=":flag_tz::flag_km: Kiswahili",
                               value="Na amino shariyah woe appliquées ici!\n"
                                     "Humour noiri je autorisé, sha namntsi blessé personne.\n"
                                     "Amani na kuishi. Sisi marafiki! :D")
            # Korean
            natlangs.add_field(name=":flag_kr: 한국말",
                               value="아미노의 지침이 여기에 적용됩니다!\n"
                                     "어두운 유머는 용인되며 누구에게도 화를 내지 마시요.\n"
                                     "평화와 사랑. 여기서 모두 친구가되자! :D")
            # Italian
            natlangs.add_field(name=":flag_it: Italiano",
                               value="Le regole del Amino si applicano anche qui!\n"
                                     "L'umore nero è permesso, ma non offendere nessuno.\n"
                                     "Pace e amore. Siamo tutti amici! :D")
            # Filipino
            natlangs.add_field(name=":flag_ph: Wikang Filipino",
                               value="Dapat niyong sundin ang mga panuntunan ng Amino dito!\n"
                                     "Hindi bawal ang pagpapatawang itim, basta't walang asarin.\n"
                                     "Saya at ibig. Magkaibigan tayo dito! :D")
            # Polish
            natlangs.add_field(name=":flag_pl: Polski",
                               value="Zasady tego Amino obowiązują na tym czacie!\n"
                                     "Czarny humor jest tolerowany, tylko nikogo nie obrażaj.\n"
                                     "Pokój i miłość. Bądźmy tu kolegami! :D")
            # Dutch
            natlangs.add_field(name=":flag_nl: Nederlands",
                               value="De regels van de Amino zijn ook hier toegepast!\n"
                                     "Zwarte humor is toegestaan, maar kwetst niemand.\n"
                                     "Vrede en liefde. Laat ons vrienden zijn! :D")
            # Romanian
            natlangs.add_field(name=":flag_md::flag_ro: Limbă română",
                               value="Regulile Aminolui se aplică și aici!\n"
                                     "Umorul negru este permis, dar nu jigniți nimeni.\n"
                                     "Pace și dragoste. Fiți amici aici! :D")
            # Greek
            natlangs.add_field(name=":flag_gr: Ελληνικά",
                               value="Οι κανόνες αυτού του Άμινο ισχύουν σε αυτό το τσατ!\n"
                                     "Το κρύο χιούμορ υπομένεται, απλά μην προσβάλλετε κανέναν.\n"
                                     "Ειρήνη και αγάπη. Ας γίνουμε όλοι φίλοι εδώ! :D")
            # Swedish
            # NOTE: The translator has said their translation isn't great,
            # so it'll stay as a comment until a better translation is made.
            # natlangs.add_field(name=":flag_fi::flag_se: Svenska",
            #                    value="Amino reglerna gäller här!\n"
            #                          "Svart humor tolereras, bara stör ingen.\n"
            #                          "Fred ock kärlek. Låt oss vara vänner har! :D")
            # Catalan
            natlangs.add_field(name=":flag_ad: Català",
                               value="Les regles del Amino s'apliquen aquí!\n"
                                     "L'humor negre està permès, però no ofenguis ningú.\n"
                                     "Pau i amor. Siguem tots amics! :D")
            # Guaraní
            natlangs.add_field(name=":flag_py: Avañe'ẽ",
                               value="Amíno tekorã ojeporu ko'ápe avei!\n"
                                     "Ore rohechakuaáta tykue pytũ, anínte remoñemyrõi ambue tapicha.\n"
                                     "Py'aguapy ha mborayhu. Javy'ákena ko'ápe! :D")
            # Lombard
            natlangs.add_field(name="Lombaard",
                               value="I regol del Amino i se applichen anca chì!\n"
                                     "El humor negher a l’è permiss, ma offend minga nissun.\n"
                                     "Pas e amor. Siom tœcc amis chì! :D")
            # ???: (Saxon) German?
            natlangs.add_field(name="Sächssch",
                               value="De Räschln vom Amino gäldn a hior! Schworzer!\n"
                                     "Humor is erlabd, solang keene Mänschn vorledzd wärdn.\n"
                                     "Friede un Liebe. Lassd uns alle Freinde sein! :D")
            # Galician
            natlangs.add_field(name="Galego",
                               value="As regras do Amino tamén aplícanse aquí!\n"
                                     "O humor negro tolérase, mais non ofendades a ninguén.\n"
                                     "Paz e amor. Sexamos todos amigos! :D")
            # Irish
            natlangs.add_field(name=":flag_ie: Gaeilge",
                               value="Tá na rialacha an Amino i bhfeidhm anseo!\n"
                                     "Glactar le greann dubh, ach ná cuir múisiam ar dhuine ar bith.\n"
                                     "Suaimhneas agus grá. Lig dúinn go léir a bheith cairde anseo! :D󠁢󠁥󠁮󠁧󠁿")
            # Basque
            natlangs.add_field(name="Euskara",
                               value="Aminoaren erregelak hemen ere aplikatuak dira!\n"
                                     "Umore beltza onartua da, baina ez ofenditu.\n"
                                     "Bake eta maite. Lagunak izan! :D")
            # Asturian
            natlangs.add_field(name="Asturianu",
                               value="Les regles del Amino tamién aplíquense equí!\n"
                                     "L'humor negru está permitíu, pero non ofendáis a naide.\n"
                                     "Paz y amor. Vamos ser toos amigos equí! :D")
            # Picard
            natlangs.add_field(name="Ch'ti Picard",
                               value="Chès règles del'Amino è s'applique ichi !\n"
                                     "Ch'noir humour y'est autorisé, faut juste pas faire d'maux à chès gins.\n"
                                     "L'paix et l'amour ichi. Gu'in sot amiteux tertous ! :D")

            natlangs_ext = discord.Embed(title="Just some guidelines... (2/3)", colour=discord.Colour(0x8b0000))
            # Icelandic
            natlangs_ext.add_field(name=":flag_is: Íslenska",
                                   value="Reglur af Amino eiga við öllum í þessum chat!\n"
                                         "Svartur humour er þolað, bara ekki móðga neinn.\n"
                                         "Friður og ást. Skulum vera frændur hér! :D")
            # Occitan
            natlangs_ext.add_field(name="Occitan",
                                   value="Las normas del'Amino s'aplicon aicí !\n"
                                         "L'umor nièr es tolerat, just non bleçatz los gents.\n"
                                         "Patz e amor. Siam tot amics aicí ! :D")
            # Aragonese
            natlangs_ext.add_field(name="Aragonés",
                                   value="As reglas d'o Amino tamién s'aplican astí!\n"
                                         "L'humor negro se permite, maguer no ofendaz a dengún.\n"
                                         "Paz y aimor. Imos ser totz amicos astí! :D")
            # Spanglish
            natlangs_ext.add_field(name=":flag_pr: Spanglish",
                                   value="Lah reglas del Amino aplayan aqi tambiem!\n"
                                         "He tolera humor negro, solo no ofend-a nadie.\n"
                                         "Paz y lof. Les ol bi frens! :D")
            # Latin
            natlangs_ext.add_field(name=":flag_va: Lingua Latīna",
                                   value="Rēgulae Aminī hīc applicantur quoque!\n"
                                         "Hūmor obscūrus permittitur, sed ne laeserītis populum.\n"
                                         "Pax et amor. Este amīcī! :D")

            conlangs = discord.Embed(title="Just some guidelines... (3/3)", colour=discord.Colour(0x8b0000))
            conlangs.add_field(name="Adennoghion",
                               value="Ze zodeoti Amino anei menotoledes!\n"
                                     "Mir'adaetu critimobru dorvodes, sco ciniomenote meci'so geigertico.\n"
                                     "Cimmorr o chomae. Chozenes anei essi! :D")
            conlangs.add_field(name="Baleñero",
                               value="O leyas de Amino se aplikan aki!\n"
                                     "E nero humor esa toleradi, to no offendan o otros.\n"
                                     "Pas y amor. Esamos todo lagunos aki! :D")
            conlangs.add_field(name="Búuku",
                               value="Búuku-wáá xumí txua paa’ú sákí xugá ‘áu háá!\n"
                                     "Gúi-gúi txua llúa xugá ‘áu xuwí. Tuña tidá gúmi ná biú.\n"
                                     "Suú muala xugá luwí-luwí. Suú ñúa’á xugá xumí ná nuxu!")
            conlangs.add_field(name="Hẇv̈",
                               value="ćq̃ c̈ńṅq d́q̈ d́sqć bỹ!\n"
                                     "ċqr̈s ḃv ʋ̌nć, q̃ŕ ćñ śqr̈ ỹsṁꞇ.\n"
                                     "d́q̈ pʋ́ ṅď̌. ř ỹq̌sḋ bỹ! :D")
            conlangs.add_field(name="Iqglic",
                               value='Rwlz ðu grwp prsn hixiq iz importent her!\n'
                                     'Dörk funynis iz okey, plyz köz nöt "sumbudy iz sad". \n'
                                     'Pys and luv. Plyz let "wy iz frenz" her! :D')
            conlangs.add_field(name="Kwilo",
                               value="Da pa o de Amino apik isi!\n"
                                     "Da shwas humo bi tolewans isi, jos no blese pipol.\n"
                                     "An e lib isi. Wi bi pwend beto! :D")
            conlangs.add_field(name="Ndu Biliva",
                               value="Bularu Vamimu mi rula lurawa bu ndu ba!\n"
                                     "Ndima munli ramba wuva ba. Wuva bularu li ba.\n"
                                     "Lamvi dida ridandi. Mimu bularu rami bu ba! :D")
            conlangs.add_field(name="Okodan",
                               value="Komeko Amino-Ikke keta hahā ef fika.\n"
                                     "Lakko bala ef teu, tayo imi(imy) mafa ach.\n"
                                     "Kemi teuta koni teu. Lalaik mam ach fika teu! :D")
            conlangs.add_field(name="Ommem",
                               value="’ꜛ3ꜛ1ꜜ2ꜛ4400  ꜜ50  ’ꜛ2ꜛ44ꜜ4ꜜ2ꜛ6ꜜ22  ꜜꜜ200！\n"
                                     "ꜛ3ꜜ1’0’ꜜ11  ꜜꜜ1’ꜛ2  ꜜ1ꜛ2ꜜ1’ꜛ1’  ’ꜛ3’  ꜜꜜ2ꜛ2  ꜛ66ꜜ50  ꜜ6  ꜜ2ꜛ550  ꜛ1ꜜ1ꜛ2ꜛ3’\n"
                                     "ꜛ44ꜜ11  0  ꜛ3ꜜ1’0’ .  ꜜꜜ2ꜛ2  ꜛ3ꜜ11ꜛ2  ꜜꜜ1 ꜜꜜ1 ꜜꜜ1ꜜ5ꜛ2ꜛ3’！:D\n\n")
            conlangs.add_field(name="Ommem",
                               value="Ŏfsmiitt irer Ŏmiimotss iisess!\n"
                                     "Ofm’em’oo lls’i salil’ ŏf’ iisi ottrer id ariit oroml’.\n"
                                     "Ossaa od ofm’em’. Iisi ofmmss iil iil iiloml’! :D")
            conlangs.add_field(name="Oskibæ",
                               value="Aminokoniqa bikamiwaan!\n"
                                     "Makadebaapiqa kaawaabam, inawisaki pemaadiw.\n"
                                     "Pankana o saakiqa. Waqndawbiqiikaanayaawaani! :D")
            conlangs.add_field(name="Shinkokugo",
                               value="Aminono famon kokoni fuitari!\n"
                                     "Suiwaraga kanyōreru, ikabasuyo jinwaku.\n"
                                     "Hyōka to ai. Ashisen tomo zeyo! :D")
            conlangs.add_field(name="Sulioqaasiip",
                               value="Aminolagatuq mannani lagatutoq!\n"
                                     "Qernerillarpuq mannami aaptut, inuiaatit naaanniaatkalargituusi!\n"
                                     "Pijairliuq aammaa asanninequq. Ikinngit agitugut! :D")
            conlangs.add_field(name="Taot",
                               value="Elwasnoo za Amino oolo rol phoon haok anna sewak.\n"
                                     "Seek woosthek rol tak, tas kheeyok so sees za.\n"
                                     "So pey loa toot. A rol sees zaaza noan! :D")
            conlangs.add_field(name="Temalyi",
                               value="Reeny, ddailyas aiwa teaminoddai bada!\n"
                                     "Masesami vosu hinyen, Churolyos tebeccha.\n"
                                     "Ameeplya chimee. Reeny malyalyas mechidi :D")
            conlangs.add_field(name="toki pona",
                               value="sitelen lawa pi tomo Amino li lon lon ni a!\n"
                                     "musi pakala li pona. taso o pakala toki ala tawa jan.\n"
                                     "pona en olin. o kama e jan pona a! :D")
            conlangs.add_field(name="Tsun-Raj",
                               value="Seuptsijlnok Baitsotew Xeaisas chutj taipnok!\n"
                                     "Nəptsak ruj kudan, temp ruk daib so-ap fesdpap.\n"
                                     "Bainr wər miŋ. Djeaix gemos wumk ŋaodj Cholas taipnok! :D")
            conlangs.add_field(name="Ūareo Travi",
                               value="Zhiyuneoda \"Amino\" do'ohokoanei!\n"
                                     "Oraseisatodaneiweá', neizhodan'aīe!\n"
                                     "Haòyeao'e'ai'oha, Yaikunako'itoyeaokoanei! :D")
            conlangs.add_field(name="Vinlandic",
                               value="De lága Aminoar framr he!\n"
                                     "Svártlátr em beþólet, þó ney miska fólk.\n"
                                     "Fríðr ok ástr. Ale erm frændr he! :D")
            conlangs.add_field(name="VötGil",
                               value='Löv​Zis​Vun​Ðyt​Prs​Grp​Viz​Vim​Cin​Ðis​Plw!\n'
                                     'Vöt​Wys​Fun​Nis​Viz​Key.​Nöt​Ply​Köz"​Cen​Prs​Viz​Vöt​Hap".\n'
                                     'Vöt​Wor​Van​Luv​Nis.Ply​Let​"Cöl​Nuy​Viz​Fen​Zis​"Cin​Ðis​Plw! :D')
            conlangs.add_field(name="ⲘOΡΑΒИ",
                               value="¡Ⲗαs ρиɣⲗαs Ⲇ̃ εⲗ Αⲙиⲛo S̃ απⲗиϧαⲛ ακи ταнεⲙ!\n"
                                     "Ⲙoz ταⲙиⲗαⲙos εⲗ uⲙoρ ⲇαϧκⲛo, soⲗo ⲛo ιραинεs ⲛατα.\n"
                                     "Sуⲗⲙα uε ⲙαuⲇα. ¡sεαⲙos τoⲇos αⲙεκos! :D")
            conlangs.add_field(name="新国語",
                               value="「Amino」拥法文此処在振用前!\n"
                                     "酸笑者寛容愔、怒不命人或。\n"
                                     "平和及愛。我全友是命! :D")
            conlangs.add_field(name="강서말",
                               value="아미노워 왕추미 죵댠!\n"
                                     "운엥 유민 햐샌디, 걍 단 인간 환다메 학 마드레 망세비.\n"
                                     "픙대아 앙. 울 믇 치가 디쟈! :D")
            conlangs.set_footer(text=f"Requested by {ctx.author.name}", icon_url=ctx.author.avatar_url)
            await ctx.send(embed=natlangs)
            await ctx.send(embed=natlangs_ext)
            await ctx.send(embed=conlangs)


def setup(bot):
    bot.add_cog(Amino(bot))
