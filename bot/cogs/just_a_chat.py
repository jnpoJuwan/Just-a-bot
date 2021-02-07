import datetime

import discord
from discord.ext import commands
from pytz import timezone, utc

from ..utils import checks
from ..utils.constants import COLOUR


class JustAChat(commands.Cog, name='Just a chat...'):
    def __init__(self, bot):
        self.bot = bot

    # GLOSS: 'js' means 'Just some', not 'JavaScript'.

    @commands.command(aliases=['jsd', 'just_some_documents'])
    async def jsdocs(self, ctx):
        """Sends Just some documents...."""
        docs_values = {
            'Just a bot...': 'https://github.com/jnpoJuwan/Just-a-bot',
            'Just a map...': 'https://goo.gl/maps/Z3VDj5JkwpVrDUSd7',
            'Just some (fuck-able) ages...':
                'https://docs.google.com/document/d/1xeAlaHXVZ4PfFm_BrOuAxXrO-0SBZZZvZndCpI0rkDc/edit?usp=sharing',
            'Just some guidelines...':
                'https://docs.google.com/document/d/1NAH6GZNC0UNFHdBmAd0u9U5keGhAgnxY-vqiRaATL8c/edit?usp=sharing',
            'Just some penises...':
                'https://docs.google.com/document/d/1gUoTqg4uzdSG_0eqoERcbMBFBrWdIEw6IBy_L3OrRnQ/edit?usp=sharing',
            'Just some stories...':
                'https://docs.google.com/document/d/1EGwg2vBL6VHaXK0B0u1mEXGV8SE9w6Xr1axlN8rB-Ic/edit?usp=sharing',
            'Just some units of measurement...':
                'https://docs.google.com/document/d/1Zk1unIM76WaBvOh1ew04nEbSPxH1Gq54M3Tu4Znj05A/edit?usp=sharing',
            '(Extended) International Phonetic Alphabet':
                'https://docs.google.com/spreadsheets/d/1Rx8ui5eug2Qk__B9IQkxVxFkdZaxbDkgGI2xNicqbtM'
                '/edit?usp=sharing',
        }

        embed = discord.Embed(title='Just some documents...', colour=COLOUR)
        for k, v in docs_values.items():
            embed.add_field(name=k, value=v, inline=False)
        embed.set_footer(text=f'Requested by {ctx.author.display_name}', icon_url=ctx.author.avatar_url)
        await ctx.send(embed=embed)

    @commands.command(aliases=['jstz'])
    async def jstimezones(self, ctx):
        """Sends Just a chat... users' time zones."""
        message = await ctx.send('Calculating time zones...')

        # ctx.typing() is used, since this command takes an *extremely* long time.
        async with ctx.typing():
            dt = datetime.datetime.now(tz=utc)
            fmt = '%A, %B %d **%H:%M** UTC%z'
            tz_values = {
                ':flag_mx: Mexico (Pacific)': timezone('Mexico/BajaSur'),
                ':flag_um: US (Mountain)': timezone('US/Mountain'),
                ':flag_mx: Mexico (Central)': timezone('Mexico/General'),
                ':flag_us: US (Central)': timezone('US/Central'),
                ':flag_um: US (Eastern)': timezone('US/Eastern'),
                ':flag_py: Paraguay': timezone('America/Asuncion'),
                ':flag_br: Brazil (Brasília)': timezone('Brazil/East'),
                ':flag_eu: Europe (Western)': timezone('Europe/London'),
                ':flag_eu: Europe (Central)': timezone('Europe/Berlin'),
                ':flag_eu: Europe (Eastern)': timezone('Europe/Athens'),
                ':flag_ae: United Arab Emirates': timezone('Asia/Dubai'),
                ':flag_kr: South Korea': timezone('Asia/Seoul'),
            }

            embed = discord.Embed(title='Just some time zones...', colour=COLOUR)
            for k, v in tz_values.items():
                embed.add_field(name=k, value=str(dt.astimezone(v).strftime(fmt)))
            embed.set_footer(text=f'Requested by {ctx.author.display_name}', icon_url=ctx.author.avatar_url)
        await message.edit(embed=embed)

    @commands.command(aliases=['jsyt'])
    async def jsyoutube(self, ctx):
        """Send some Just a chat... user's YouTube channels."""
        channel_values = {
            'Aurora': 'https://www.youtube.com/channel/UCmDE7oQp2wzTLxd7lc4mA9A',
            'D\'ignoranza': 'https://www.youtube.com/channel/UCI4ZJ0QmSokr6ctUfURqm5A',
            'Dr. IPA': 'https://www.youtube.com/channel/UCfPYxsZHRBaW24q3pb9oOnA',
            'Dracheneks': 'https://www.youtube.com/channel/UCiaOA8yjnuZX5wUqmlRDUuA',
            'MAGNVS': 'https://www.youtube.com/channel/UC2AcuqQOPxH6pkbJs-xm_Qw',
            'PD6': 'https://www.youtube.com/channel/UCuAsPOh-qA7wakswF6ioo4g',
        }

        embed = discord.Embed(name='Just some channels...', colour=COLOUR)
        for k, v in channel_values.items():
            embed.add_field(name=k, value=v)
        embed.set_footer(text=f'Requested by {ctx.author.display_name}', icon_url=ctx.author.avatar_url)
        await ctx.send(embed=embed)

    # TODO: Add paginator
    @commands.command(aliases=['jsg'])
    @commands.cooldown(3, 60.0, commands.BucketType.user)
    @checks.is_mod()
    async def jsguidelines(self, ctx, paginator='off'):
        """Sends the Just a chat... guidelines from Amino."""
        # SEE: https://docs.google.com/document/d/1NAH6GZNC0UNFHdBmAd0u9U5keGhAgnxY-vqiRaATL8c/edit?usp=sharing
        if paginator not in ['on', 'off']:
            raise commands.BadArgument

        # FIXME: Use a text file for the page content.
        natlangs = discord.Embed(title='Just some guidelines...', colour=COLOUR)
        natlangs.add_field(name=':flag_gb::flag_us: English',
                           value='The Amino\'s guidelines apply here!\n'
                                 'Dark humor is tolerated, just don\'t offend anyone.\n'
                                 'Peace and love. Let\'s all be friends here! :D')
        # Mandarin Chinese (Simplified)
        natlangs.add_field(name=':flag_cn: 普通话',
                           value='「Amino」规则在这里适用！\n'
                                 '黑暗的幽默容忍在这里, 不要冒犯。\n'
                                 '安和爱。 让我们在这里成为朋友! :D')
        # Mandarin Chinese (Traditional)
        natlangs.add_field(name=':flag_tw: 國語',
                           value='「Amino」規則在這裡適用！\n'
                                 '黑暗的幽默容忍在這裡, 不要冒犯。\n'
                                 '安和愛。 讓我們在這裡成為朋友! :D')
        # Spanish
        natlangs.add_field(name=':flag_ea: Español',
                           value='¡Las reglas del Amino también se aplican aquí!\n'
                                 'Toleramos el humor negro, solo no ofendas a nadie.\n'
                                 'Paz y amor. ¡Seamos todos amigos! :D')
        # French
        natlangs.add_field(name=':flag_fr: Français',
                           value='Les règles de l\'Amino s\'appliquent ici !\n'
                                 'L\'humour noir est toléré, ne blessez juste pas les gens.\n'
                                 'Paix et amour. Soyons tous amis ici ! :D')
        # Portuguese
        natlangs.add_field(name=':flag_br::flag_pt: Português',
                           value='As regras do Amino também aplicam-se aqui!\n'
                                 'Toleramos humor negro, só não ofenda(s) os outros.\n'
                                 'Paz e amor. Vamos todos ser amigos aqui! :D')
        # Standard German
        natlangs.add_field(name=':flag_de: Deutsch',
                           value='Die Regeln von diesem Amino gelten auch hier!\n'
                                 'Schwarzer Humor ist erlaubt, solange keine Menschen verletzt werden.\n'
                                 'Friede und Liebe. Lasst uns hier alle Freunde sein! :D')
        # Japanese
        natlangs.add_field(name=':flag_jp: 日本語',
                           value='「Amino」ガイドラインがここに適用されます！\n'
                                 'ダークユーモアは許容されます、唯誰かを怒らせないで下さい。\n'
                                 '平和と愛。ここでみんな友達になりましょう！ :D')
        # Korean
        natlangs.add_field(name=':flag_kr: 한국말',
                           value='아미노의 지침이 여기에 적용됩니다!\n'
                                 '어두운 유머는 용인되며 누구에게 화를 내지는 마시고.\n'
                                 '평화와 사랑. 여기서 모두 친구 되자! :D')
        # Italian
        natlangs.add_field(name=':flag_it: Italiano',
                           value='Le regole del Amino si applicano anche qui!\n'
                                 'L\'umore nero è permesso, ma non offendere nessuno.\n'
                                 'Pace e amore. Siamo tutti amici! :D')
        # Filipino
        natlangs.add_field(name=':flag_ph: Wikang Filipino',
                           value='Dapat niyong sundin ang mga panuntunan ng Amino dito!\n'
                                 'Hindi bawal ang pagpapatawang itim, basta\'t walang asarin.\n'
                                 'Saya at ibig. Magkaibigan tayo dito! :D')
        # Polish
        natlangs.add_field(name=':flag_pl: Polski',
                           value='Zasady tego Amino obowiązują na tym czacie!\n'
                                 'Czarny humor jest tolerowany, tylko nikogo nie obrażaj.\n'
                                 'Pokój i miłość. Bądźmy tu kolegami! :D')
        # Dutch
        natlangs.add_field(name=':flag_nl: Nederlands',
                           value='De regels van de Amino zijn ook hier toegepast!\n'
                                 'Zwarte humor is toegestaan, maar kwetst niemand.\n'
                                 'Vrede en liefde. Laat ons vrienden zijn! :D')
        # Romanian
        natlangs.add_field(name=':flag_md::flag_ro: Limbă română',
                           value='Regulile Aminolui se aplică și aici!\n'
                                 'Umorul negru este permis, dar nu jigniți nimeni.\n'
                                 'Pace și dragoste. Fiți amici aici! :D')
        # Greek
        natlangs.add_field(name=':flag_gr: Ελληνικά',
                           value='Οι κανόνες αυτού του Άμινο ισχύουν σε αυτό το τσατ!\n'
                                 'Το κρύο χιούμορ υπομένεται, απλά μην προσβάλλετε κανέναν.\n'
                                 'Ειρήνη και αγάπη. Ας γίνουμε όλοι φίλοι εδώ! :D')
        # Catalan
        natlangs.add_field(name=':flag_ad: Català',
                           value='Les regles del Amino s\'apliquen aquí!\n'
                                 'L\'humor negre està permès, però no ofenguis ningú.\n'
                                 'Pau i amor. Siguem tots amics! :D')
        # Guaraní
        natlangs.add_field(name=':flag_py: Avañe\'ẽ',
                           value='Amíno tekorã ojeporu ko\'ápe avei!\n'
                                 'Ore rohechakuaáta tykue pytũ, anínte remoñemyrõi ambue tapicha.\n'
                                 'Py\'aguapy ha mborayhu. Javy\'ákena ko\'ápe! :D')
        # Lombard
        natlangs.add_field(name='Lombard',
                           value='I regol del Amino i se applichen anca chì!\n'
                                 'El humor negher a l’è permiss, ma offend minga nissun.\n'
                                 'Pas e amor. Siom tœcc amis chì! :D')
        # ???: (Saxon) German?
        natlangs.add_field(name='Sächssch',
                           value='De Räschln vom Amino gäldn a hior! Schworzer!\n'
                                 'Humor is erlabd, solang keene Mänschn vorledzd wärdn.\n'
                                 'Friede un Liebe. Lassd uns alle Freinde sein! :D')
        # Galician
        natlangs.add_field(name='Galego',
                           value='As regras do Amino tamén aplícanse aquí!\n'
                                 'O humor negro tolérase, mais non ofendades a ninguén.\n'
                                 'Paz e amor. Sexamos todos amigos! :D')
        # Irish
        natlangs.add_field(name=':flag_ie: Gaeilge',
                           value='Tá na rialacha an Amino i bhfeidhm anseo!\n'
                                 'Glactar le greann dubh, ach ná cuir múisiam ar dhuine ar bith.\n'
                                 'Suaimhneas agus grá. Lig dúinn go léir a bheith cairde anseo! :D󠁢')
        # Comorian
        natlangs.add_field(name=':flag_km::flag_yt: Shikomori',
                           value='Na amino shariyah woe appliquées ici!\n'
                                 'Humour noiri je autorisé, sha namntsi blessé personne.\n'
                                 'Amani na kuishi. Sisi marafiki! :D')
        # Basque
        natlangs.add_field(name='Euskara',
                           value='Aminoaren erregelak hemen ere aplikatuak dira!\n'
                                 'Umore beltza onartua da, baina ez ofenditu.\n'
                                 'Bake eta maite. Lagunak izan! :D')
        # Asturian
        natlangs.add_field(name='Asturianu',
                           value='¡Les regles del Amino tamién aplíquense equí!\n'
                                 'L\'humor negru está permitíu, pero non ofendáis a naide.\n'
                                 'Paz y amor. ¡Vamos ser toos amigos equí! :D')

        natlangs_ext = discord.Embed(title='Just some guidelines...', colour=COLOUR)
        # Picard
        natlangs_ext.add_field(name='Ch\'ti picard',
                               value='Chès règles del\'Amino è s\'applique ichi !\n'
                                     'Ch\'noir humour y\'est autorisé, faut juste pas faire d\'maux à chès gins.\n'
                                     'L\'paix et l\'amour ichi. Gu\'in sot amiteux tertous ! :D')
        # Icelandic
        natlangs_ext.add_field(name=':flag_is: Íslenska',
                               value='Reglur af Amino eiga við öllum í þessum chat!\n'
                                     'Svartur humour er þolað, bara ekki móðga neinn.\n'
                                     'Friður og ást. Skulum vera frændur hér! :D')
        # Occitan
        natlangs_ext.add_field(name='Occitan',
                               value='Las normas del\'Amino s\'aplicon aicí !\n'
                                     'L\'umor nièr es tolerat, just non bleçatz los gents.\n'
                                     'Patz e amor. Siam tot amics aicí ! :D')
        # Aragonese
        natlangs_ext.add_field(name='Aragonés',
                               value='As reglas d\'o Amino tamién s\'aplican astí!\n'
                                     'L\'humor negro se permite, maguer no ofendaz a dengún.\n'
                                     'Paz y aimor. Imos ser totz amicos astí! :D')
        # Spanglish
        natlangs_ext.add_field(name=':flag_pr: Spanglish',
                               value='Lah reglas del Amino aplayan aqi tambiem!\n'
                                     'He tolera humor negro, solo no ofend-a nadie.\n'
                                     'Paz y lof. Les ol bi frens! :D')
        # Latin
        natlangs_ext.add_field(name=':flag_va: Lingua Latīna',
                               value='Rēgulae Aminī hīc applicantur quoque!\n'
                                     'Hūmor obscūrus permittitur, sed ne laeserītis populum.\n'
                                     'Pax et amor. Este amīcī! :D')

        conlangs = discord.Embed(title='Just some guidelines...', colour=COLOUR)
        conlangs.add_field(name='Adennoghion',
                           value='Ze zodeoti Amino anei menotoledes!\n'
                                 'Mir\'adaetu critimobru dorvodes, sco ciniomenote meci\'so geigertico.\n'
                                 'Cimmorr o chomae. Chozenes anei essi! :D')
        conlangs.add_field(name='aUI',
                           value='jwYzn Ub aMINo fag tsYv-tvev!\n'
                                 'yim rOvU cEv o-dYvQ, YvYdrOrv Ymu.\n'
                                 'brU Ib brO. fnu fag drYv cEv bru! :D')
        conlangs.add_field(name='Baleñero',
                           value='O leyas de Amino se aplikan aki!\n'
                                 'E nero humor esa toleradi, to no offendan o otros.\n'
                                 'Pas y amor. Esamos todo lagunos aki! :D')
        conlangs.add_field(name='Búuku',
                           value='Búuku-wáá xumí txua paa’ú sákí xugá ‘áu háá!\n'
                                 'Gúi-gúi txua llúa xugá ‘áu xuwí. Tuña tidá gúmi ná biú.\n'
                                 'Suú muala xugá luwí-luwí. Suú ñúa’á xugá xumí ná nuxu! :D')
        conlangs.add_field(name='Hilten',
                           value='N̄on imsam Amino ecue iso fejjo ecue!\n'
                                 'Hakari moli tsiti ucuitsiti fahan̄, tsure on̄dui ato fahan̄ ejtsi moli.\n'
                                 'Sun̄n̄ura suan̄ moj maru. Rulejtsi mahu maru fejjo ecue! :D')
        conlangs.add_field(name='Hẇv̈',
                           value='ćq̃ c̈ńṅq d́q̈ d́sqć bỹ!\n'
                                 'ċqr̈s ḃv ʋ̌nć, q̃ŕ ćñ śqr̈ ỹsṁꞇ.\n'
                                 'd́q̈ pʋ́ ṅď̌. ř ỹq̌sḋ bỹ! :D')
        conlangs.add_field(name='Iqglic',
                           value='Rwlz ðu grwp prsn hixiq iz importent her!\n'
                                 'Dörk funynis iz okey, plyz köz nöt "sumbudy iz sad".\n'
                                 'Pys and luv. Plyz let "wy iz frenz" her! :D')
        conlangs.add_field(name='Kwilo',
                           value='Da pa o de Amino apik isi!\n'
                                 'Da shwas humo bi tolewans isi, jos no blese pipol.\n'
                                 'An e lib isi. Wi bi pwend beto! :D')
        conlangs.add_field(name='Lirin',
                           value='Libiim Aminoermet kamamt dare\n'
                                 'Imiem tashfem mhort nihdir, na n\'eblesh neam.\n'
                                 'Imildesh Fash ne hish, berostem! :D')
        conlangs.add_field(name='Ndu Biliva',
                           value='Bularu Vamimu mi rula lurawa bu ndu ba!\n'
                                 'Ndima munli ramba wuva ba. Wuva bularu li ba.\n'
                                 'Lamvi dida ridandi. Mimu bularu rami bu ba! :D')
        conlangs.add_field(name='Okodan',
                           value='Komeko Amino-Ikke keta hahā ef fika.\n'
                                 'Lakko bala ef teu, tayo imi(imy) mafa ach.\n'
                                 'Kemi teuta koni teu. Lalaik mam ach fika teu! :D')
        conlangs.add_field(name='Ommem',
                           value='’ꜛ3ꜛ1ꜜ2ꜛ4400  ꜜ50  ’ꜛ2ꜛ44ꜜ4ꜜ2ꜛ6ꜜ22  ꜜꜜ200！\n'
                                 'ꜛ3ꜜ1’0’ꜜ11  ꜜꜜ1’ꜛ2  ꜜ1ꜛ2ꜜ1’ꜛ1’  ’ꜛ3’  ꜜꜜ2ꜛ2  ꜛ66ꜜ50  ꜜ6  ꜜ2ꜛ550  ꜛ1ꜜ1ꜛ2ꜛ3’\n'
                                 'ꜛ44ꜜ11  0  ꜛ3ꜜ1’0’ .  ꜜꜜ2ꜛ2  ꜛ3ꜜ11ꜛ2  ꜜꜜ1 ꜜꜜ1 ꜜꜜ1ꜜ5ꜛ2ꜛ3’！:D')
        conlangs.add_field(name='Ommem',
                           value='Ŏfsmiitt irer Ŏmiimotss iisess!\n'
                                 'Ofm’em’oo lls’i salil’ ŏf’ iisi ottrer id ariit oroml’.\n'
                                 'Ossaa od ofm’em’. Iisi ofmmss iil iil iiloml’! :D')
        conlangs.add_field(name='Oskibæ',
                           value='Aminokoniqa bikamiwaan!\n'
                                 'Makadebaapiqa kaawaabam, inawisaki pemaadiw.\n'
                                 'Pankana o saakiqa. Waqndawbiqiikaanayaawaani! :D')
        conlangs.add_field(name='Shinkokugo',
                           value='Aminono famon kokoni fuitari!\n'
                                 'Suiwaraga kanyōreru, ikabasuyo jinwaku.\n'
                                 'Hyōka to ai. Ashisen tomo zeyo! :D')
        conlangs.add_field(name='Sulioqaasiip',
                           value='Aminolagatuq mannani lagatutoq!\n'
                                 'Qernerillarpuq mannami aaptut, inuiaatit naaanniaatkalargituusi!\n'
                                 'Pijairliuq aammaa asanninequq. Ikinngit agitugut! :D')
        conlangs.add_field(name='Taot',
                           value='Elwasnoo za Amino oolo rol phoon haok anna sewak.\n'
                                 'Seek woosthek rol tak, tas kheeyok so sees za.\n'
                                 'So pey loa toot. A rol sees zaaza noan! :D')
        conlangs.add_field(name='Temalyi',
                           value='Reeny, ddailyas aiwa teaminoddai bada!\n'
                                 'Masesami vosu hinyen, Churolyos tebeccha.\n'
                                 'Ameeplya chimee. Reeny malyalyas mechidi :D')
        conlangs.add_field(name='toki pona',
                           value='sitelen lawa pi tomo Amino li lon lon ni a!\n'
                                 'musi pakala li pona. taso o pakala toki ala tawa jan.\n'
                                 'pona en olin. o kama e jan pona a! :D')
        conlangs.add_field(name='Tsun-Raj',
                           value='Seuptsijlnok Baitsotew Xeaisas chutj taipnok!\n'
                                 'Nəptsak ruj kudan, temp ruk daib so-ap fesdpap.\n'
                                 'Bainr wər miŋ. Djeaix gemos wumk ŋaodj Cholas taipnok! :D')
        conlangs.add_field(name='Ūareo Travi',
                           value='Zhiyuneoda \'Amino\' do\'ohokoanei!\n'
                                 'Oraseisatodaneiweá\', neizhodan\'aīe!\n'
                                 'Haòyeao\'e\'ai\'oha. Yaikunako\'itoyeaokoanei! :D')
        conlangs.add_field(name='uo\'aXy\'an',
                           value='E huang tyung e Â.mi\'no ka" .a\'u!\n'
                                 'O s.ōng xyē\'na lē yai hua\'ua e yothle\'a okuaichyo\'a o myāl ku\'ya.\n'
                                 'E tue" sa\'a ka" .a\'u! :D')
        conlangs.add_field(name='Vinlandic',
                           value='Log Aminos atfald hér!\n'
                                 'Svartlætor er tolur, tó nej meid einver.\n'
                                 'Frid ok æst; all erm frændar hér! :D')
        conlangs.add_field(name='VötGil',
                           value='Löv​Zis​Vun​Ðyt​Prs​Grp​Viz​Vim​Cin​Ðis​Plw!\n'
                                 'Vöt​Wys​Fun​Nis​Viz​Key.​Nöt​Ply​Köz"​Cen​Prs​Viz​Vöt​Hap".\n'
                                 'Vöt​Wor​Van​Luv​Nis.Ply​Let​"Cöl​Nuy​Viz​Fen​Zis​"Cin​Ðis​Plw! :D')

        conlangs_ext = discord.Embed(title='Just some guidelines...', colour=COLOUR)
        conlangs_ext.add_field(name='ⲘOΡΑΒИ',
                               value='¡Ⲗαs ρиɣⲗαs Ⲇ̃ εⲗ Αⲙиⲛo S̃ απⲗиϧαⲛ ακи ταнεⲙ!\n'
                                     'Ⲙoz ταⲙиⲗαⲙos εⲗ uⲙoρ ⲇαϧκⲛo, soⲗo ⲛo ιραинεs ⲛατα.\n'
                                     'Sуⲗⲙα uε ⲙαuⲇα. ¡sεαⲙos τoⲇos αⲙεκos! :D')
        conlangs_ext.add_field(name='新国語',
                               value='「Amino」拥法文此処在振用前!\n'
                                     '酸笑者寛容愔、怒不命人或。\n'
                                     '平和及愛。我全友是命! :D')
        conlangs_ext.add_field(name='강서말',
                               value='아미노워 왕추미 죵댠!\n'
                                     '운엥 유민 햐샌디, 걍 단 인간 환다메 학 마드레 망세비.\n'
                                     '픙대아 앙. 울 믇 치가 디쟈! :D')
        conlangs_ext.set_footer(text=f'Requested by {ctx.author.display_name}', icon_url=ctx.author.avatar_url)

        if paginator == 'off':
            await ctx.send(embed=natlangs)
            await ctx.send(embed=natlangs_ext)
            await ctx.send(embed=conlangs)
            await ctx.send(embed=conlangs_ext)
        else:
            pass


def setup(bot):
    bot.add_cog(JustAChat(bot))
