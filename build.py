#!/usr/bin/env python3
# Generator voor bal-herenkleding.nl  -  output: ./site (deploybaar via Cloudflare Pages)
import os, re, datetime

SITE = "https://bal-herenkleding.nl"
OUT = os.path.join(os.path.dirname(__file__), "site")
TODAY = datetime.date(2026, 6, 24)

NAV = [
    ("home", "Home", "/"),
    ("over", "Over", "/over.html"),
    ("nieuws", "Nieuws", "/nieuws.html"),
    ("stijlgids", "Stijlgids", "/stijlgids.html"),
    ("partners", "Partners", "/partners.html"),
    ("contact", "Contact", "/contact.html"),
]

MENU_JS = (
    "<script>"
    "var b=document.querySelector('.menu-btn'),n=document.querySelector('.nav');"
    "if(b){b.addEventListener('click',function(){n.classList.toggle('open');"
    "b.setAttribute('aria-expanded',n.classList.contains('open'));});}"
    "</script>"
)


def nav_html(active):
    items = ""
    for key, label, href in NAV:
        cls = ' class="is-active"' if key == active else ""
        items += f'<a href="{href}"{cls}>{label}</a>'
    return items


def footer_html():
    return f"""<footer class="site-foot">
  <div class="wrap">
    <div class="foot-grid">
      <div class="brandblock">
        <div class="bf">Bal Herenkleding</div>
        <p>Een onafhankelijk magazine over herenkleding. Nuchtere stijladviezen, uitleg over pasvorm en materiaal, en aandacht voor kleding die lang meegaat.</p>
        <p>Reageren of een tip insturen kan via <a href="mailto:info@bal-herenkleding.nl">info@bal-herenkleding.nl</a>.</p>
      </div>
      <div>
        <h4>Lezen</h4>
        <ul class="foot-links">
          <li><a href="/nieuws.html">Nieuws</a></li>
          <li><a href="/stijlgids.html">Stijlgids</a></li>
          <li><a href="/over.html">Over het platform</a></li>
          <li><a href="/partners.html">Partners</a></li>
        </ul>
      </div>
      <div>
        <h4>Service</h4>
        <ul class="foot-links">
          <li><a href="/contact.html">Contact</a></li>
          <li><a href="/privacy.html">Privacybeleid</a></li>
          <li><a href="/cookies.html">Cookies</a></li>
        </ul>
      </div>
    </div>
    <div class="foot-bottom">
      <span>&copy; {TODAY.year} bal-herenkleding.nl</span>
      <span><a href="/privacy.html">Privacy</a> &nbsp; <a href="/cookies.html">Cookies</a></span>
    </div>
  </div>
</footer>"""


def base(title, description, body, active, canonical, og_type="website"):
    full_title = f"{title} | Bal Herenkleding"
    return f"""<!doctype html>
<html lang="nl">
<head>
<meta charset="utf-8">
<meta name="viewport" content="width=device-width, initial-scale=1">
<title>{full_title}</title>
<meta name="description" content="{description}">
<link rel="canonical" href="{canonical}">
<meta property="og:type" content="{og_type}">
<meta property="og:title" content="{title}">
<meta property="og:description" content="{description}">
<meta property="og:url" content="{canonical}">
<meta property="og:site_name" content="Bal Herenkleding">
<meta property="og:locale" content="nl_NL">
<meta name="theme-color" content="#2E3A30">
<link rel="icon" href="/favicon.svg" type="image/svg+xml">
<link rel="stylesheet" href="/style.css">
</head>
<body>
<header class="site-head">
  <div class="wrap">
    <a class="brand" href="/">Bal Herenkleding<small>Herenmode magazine</small></a>
    <button class="menu-btn" aria-label="Menu" aria-expanded="false">Menu</button>
    <nav class="nav" aria-label="Hoofdmenu">{nav_html(active)}</nav>
  </div>
</header>
<main>
{body}
</main>
{footer_html()}
{MENU_JS}
</body>
</html>"""


# ---------------------------------------------------------------------------
# Artikelen
# ---------------------------------------------------------------------------

ARTICLES = [
    {
        "slug": "basisgarderobe-onderlagen-heren",
        "cat": "Garderobe",
        "title": "De onderlaag van een herengarderobe: t-shirts, ondergoed en pasvorm",
        "dek": "Wat onder het overhemd zit bepaalt de val van de bovenlaag sterker dan de meeste mannen denken.",
        "date": datetime.date(2026, 8, 19),
        "read": "5 min",
        "body": """
<p>Aan een garderobe wordt meestal van buiten naar binnen gewerkt: eerst het colbert, dan het overhemd, en pas als er iets knelt of doorschijnt komt de onderlaag ter sprake. Terwijl juist die laag bepaalt hoe de rest valt.</p>
<h2>Waarom de onderlaag meetelt</h2>
<p>Een t-shirt met een te wijde hals tekent zich af onder een overhemd met een open boord. Een shirt dat te kort is, kruipt boven de broekband uit en veroorzaakt de plooi die vervolgens in het overhemd zichtbaar wordt. Beide problemen zijn niet met een beter overhemd op te lossen.</p>
<p>Bij donkere overhemden speelt daarnaast de kleur van de onderlaag. Wit schijnt door, en dat blijft ook na wassen zo. Een huidkleurige of grijze variant is onder vrijwel elke bovenkleur de neutralere keuze.</p>
<h2>Waar op te letten bij een t-shirt</h2>
<ul>
  <li>De halsvorm: een diepe V verdwijnt onder een open boord, een ronde hals niet.</li>
  <li>De lengte: minstens tot over de broekband, ook met de armen omhoog.</li>
  <li>De naad op de schouder: die hoort op het schouderpunt te vallen, niet erboven of eronder.</li>
  <li>Het gewicht van het jersey: te dun geeft doorschijnen, te dik geeft volume onder een colbert.</li>
</ul>
<p>Een set van twee of drie in dezelfde uitvoering werkt praktischer dan losse aankopen. Ze slijten dan gelijkmatig en de kast blijft overzichtelijk. Het aanbod staat bij <a href="https://www.hemdvoorhem.nl/alan-red-t-shirts" rel="nofollow">Hemd voor Hem</a>.</p>
<h2>Materiaal</h2>
<p>Katoen blijft de standaard en is prettig zolang het niet warm wordt. Bij warmte of een lange dag is een vezel die vocht sneller afvoert comfortabeler. Bamboeviscose en modal voelen koeler aan en houden geur minder vast dan gewoon katoen.</p>
<p>Let bij die materialen wel op de wasvoorschriften. Ze verdragen doorgaans dertig graden en geen droger; wie ze op zestig meewast, houdt na een paar beurten een maat kleiner over. Het aanbod staat op <a href="https://www.hemdvoorhem.nl/bamboe-heren-ondergoed" rel="nofollow">hemdvoorhem.nl</a>.</p>
<h2>Vervangen op tijd</h2>
<p>Boorden die uitgerekt blijven, dunne plekken onder de armen en een grijze waas op wit zijn allemaal signalen dat een stuk uit de rotatie kan. Doorgaan tot iets echt kapot is, kost aan uitstraling meer dan de vervanging kost.</p>
<p>Een praktische aanpak is om twee keer per jaar de hele onderlaag na te lopen en alles wat twijfelachtig is in één keer te vervangen. Dat voorkomt de situatie waarin de helft van de la bruikbaar is en er elke ochtend gezocht moet worden.</p>
<h2>Sokken en de rest van de laag</h2>
<p>Sokken vallen onder dezelfde categorie en worden nog vaker vergeten. Een sok die op de kuit afzakt, is niet te verbergen zodra iemand gaat zitten, en dat is precies het moment waarop de sok zichtbaar wordt. Een langere uitvoering met een stevige boord lost dat op.</p>
<p>Kies daarbij liever een beperkt aantal kleuren in grotere aantallen dan telkens iets anders. Sokken raken kwijt, en een lade met vijf paar in dezelfde uitvoering blijft bruikbaar terwijl een lade met tien verschillende paren binnen een half jaar uit losse exemplaren bestaat.</p>
""",
    },
    {
        "slug": "capsule-garderobe-voor-mannen",
        "cat": "Garderobe",
        "title": "De capsule garderobe voor mannen",
        "dek": "Een kleine, doordachte basis levert meer combinaties op dan een volle kast vol losse aankopen.",
        "date": datetime.date(2026, 6, 18),
        "read": "6 min",
        "body": """
<p>Een capsule garderobe draait om een beperkt aantal kledingstukken die onderling goed combineren. Het idee is simpel: minder stuks, maar wel stuks die op elkaar zijn afgestemd in kleur, pasvorm en stijl. Het resultaat is een kast waarin vrijwel elke combinatie klopt, zonder dagelijks gepuzzel.</p>

<h2>Waarom minder vaak meer is</h2>
<p>Een volle kast geeft niet automatisch meer keuze. Vaak zit er juist veel in dat zelden wordt gedragen, omdat het nergens bij past of niet lekker zit. Een capsule keert dat om. Door te kiezen voor neutrale basiskleuren en betrouwbare modellen, sluit elk stuk aan op de rest. Wie tien goed gekozen stuks bezit, komt verder dan met dertig willekeurige aankopen.</p>

<h2>De basis van een herengarderobe</h2>
<p>Een werkbare capsule voor het hele jaar bestaat grofweg uit de volgende onderdelen:</p>
<ul>
  <li>Twee tot drie overhemden in effen, rustige kleuren zoals wit, lichtblauw en een zachte tint.</li>
  <li>Twee broeken: een chino in een neutrale kleur en een donkere jeans.</li>
  <li>Een trui met ronde of V-hals in wol of katoen.</li>
  <li>Een nette pantalon en een blazer voor formele momenten.</li>
  <li>Een paar witte sneakers en een paar nette leren schoenen.</li>
  <li>Effen T-shirts en kwalitatieve sokken als onderlaag.</li>
</ul>
<p>Deze lijst is geen wet, maar een vertrekpunt. Wie veel op kantoor is, voegt overhemden en pantalons toe. Wie vooral casual leeft, legt het accent op chino, trui en sneakers.</p>

<div class="callout"><p>Een capsule werkt het best wanneer minstens tachtig procent in dezelfde kleurfamilie valt. Daardoor passen bovenkleding en broek vrijwel altijd bij elkaar.</p></div>

<h2>Kleur als bindmiddel</h2>
<p>De kracht van een capsule zit in de kleurkeuze. Blauw, grijs, beige, wit en zwart vormen een rustige basis die onderling combineert. Eén of twee accentkleuren mogen daarbij, mits ze terugkomen in meerdere stuks. Een groene trui en een groene sok lopen zo netjes in elkaar over, terwijl een losse felle kleur al snel buiten de boot valt.</p>

<h2>Kwaliteit boven aantal</h2>
<p>Een kleinere garderobe rechtvaardigt een hogere uitgave per stuk. Een overhemd dat goed zit en netjes wast, gaat jaren mee en blijft in model. Datzelfde geldt voor schoenen en een blazer. De kosten per keer dragen liggen bij een goed stuk vaak lager dan bij een goedkoop alternatief dat na een seizoen vervangen moet worden.</p>

<table class="compare">
  <tr><th>Aanpak</th><th>Volle kast</th><th>Capsule</th></tr>
  <tr><td>Aantal stuks</td><td>Veel, vaak ongedragen</td><td>Beperkt, alles in gebruik</td></tr>
  <tr><td>Combineren</td><td>Kost moeite</td><td>Vrijwel altijd raak</td></tr>
  <tr><td>Kosten op termijn</td><td>Versnipperd</td><td>Gericht en lager</td></tr>
  <tr><td>Ochtendkeuze</td><td>Twijfel</td><td>Snel klaar</td></tr>
</table>

<h2>Onderhoud houdt het systeem overeind</h2>
<p>Een capsule blijft alleen werken bij goed onderhoud. Overhemden die op de juiste temperatuur worden gewassen en direct worden opgehangen, blijven langer mooi. Schoenen die af en toe worden gepoetst en op spanners staan, gaan jaren langer mee. Door versleten stuks tijdig te vervangen blijft het geheel kloppen.</p>

<h2>Tot slot</h2>
<p>Een capsule garderobe is geen modetrend maar een manier van organiseren. Minder, beter en op elkaar afgestemd levert meer rust op en meer bruikbare combinaties. Het vertrekpunt is altijd hetzelfde: kies neutrale basics, hou de kleuren bij elkaar en investeer in kwaliteit die meegaat.</p>
""",
    },
    {
        "slug": "overhemd-pasvorm-en-boordmaat",
        "cat": "Overhemden",
        "title": "Het overhemd: pasvorm en boordmaat uitgelegd",
        "dek": "Boordmaat alleen zegt weinig. De pasvorm van de rest van het overhemd bepaalt of het echt goed zit.",
        "date": datetime.date(2026, 6, 12),
        "read": "7 min",
        "body": """
<p>Het overhemd is voor veel mannen het lastigste kledingstuk om online te kiezen. De boordmaat lijkt het houvast, maar dat getal zegt alleen iets over de omvang van de kraag. De pasvorm van schouders, borst en taille bepaalt of een overhemd uiteindelijk lekker zit en er verzorgd uitziet.</p>

<h2>Wat boordmaat wel en niet zegt</h2>
<p>De boordmaat is het aantal centimeters van de halsomtrek. Een man met boordmaat 41 kan bij het ene merk perfect zitten en bij het andere juist te ruim of te strak. Dat komt doordat elk merk een eigen snit hanteert. Boordmaat is dus een startpunt, geen garantie.</p>

<div class="callout"><p>Wie de boordmaat niet kent, meet de halsomtrek met een centimeter net onder de adamsappel en telt daar ongeveer een centimeter speling bij op.</p></div>

<h2>De pasvormen op een rij</h2>
<p>Overhemden worden meestal aangeboden in een handvol pasvormen. De namen verschillen per merk, maar de hoofdlijnen komen overeen.</p>

<table class="compare">
  <tr><th>Pasvorm</th><th>Voor wie</th><th>Kenmerk</th></tr>
  <tr><td>Slim fit</td><td>Slanke bouw</td><td>Strak, getailleerd</td></tr>
  <tr><td>Modern of tailored fit</td><td>Gemiddelde bouw</td><td>Licht getailleerd, ruimte zonder bol te staan</td></tr>
  <tr><td>Regular fit</td><td>Stevige bouw of voorkeur voor ruimte</td><td>Rechte, ruime snit</td></tr>
  <tr><td>Comfort fit</td><td>Brede bouw</td><td>Extra ruim, valt recht</td></tr>
</table>

<h2>De punten die er echt toe doen</h2>
<p>Of een overhemd goed zit, valt af te lezen aan een paar vaste plekken:</p>
<ul>
  <li><strong>Schoudernaad.</strong> Die hoort precies op de rand van de schouder te vallen, niet erover en niet erboven.</li>
  <li><strong>Borst en taille.</strong> Het overhemd mag niet trekken bij de knopen en niet bol staan in de zij.</li>
  <li><strong>Mouwlengte.</strong> De manchet eindigt op de pols, zodat onder een colbert een randje zichtbaar blijft.</li>
  <li><strong>Lengte.</strong> Het pand reikt tot net over de bilnaad, zodat het in de broek blijft zitten.</li>
</ul>

<h2>Strijkvrij of niet</h2>
<p>Katoen ademt en voelt prettig, maar kreukt. Strijkvrije overhemden combineren het comfort van katoen met een behandeling die kreuk tegengaat. Voor wie strijken liever overslaat, is dat een praktische keuze. Webshops die gespecialiseerd zijn in herenmode, zoals <a href="https://www.hemdvoorhem.nl" rel="nofollow noopener" target="_blank">HemdVoorHem.nl</a>, bieden een ruime selectie strijkvrije modellen met heldere maattabellen per merk. Dat helpt bij het vergelijken van pasvormen voordat er besteld wordt.</p>

<h2>Extra lange mouwen</h2>
<p>Lange mannen lopen vaak tegen te korte mouwen aan. Sommige merken voeren daarom een mouwlengte 7, met mouwen die ongeveer vijf centimeter langer zijn dan standaard. Ook de totale lengte van het overhemd is dan iets ruimer, zodat het netjes in de broek blijft.</p>

<h2>Online kopen zonder misgrepen</h2>
<p>De maattabel is bij online kopen het belangrijkste hulpmiddel. Door de maten van een overhemd dat perfect past op te meten en die te vergelijken met de tabel, wordt de kans op een misser klein. Boordmaat, borstwijdte, schouderbreedte en mouwlengte samen geven een betrouwbaar beeld.</p>

<h2>Tot slot</h2>
<p>Een goed zittend overhemd begint niet bij de boordmaat maar bij de pasvorm die past bij de lichaamsbouw. Wie weet welke snit goed valt en de maattabel raadpleegt, kiest met vertrouwen, ook online. Daarna is het een kwestie van kleur en gelegenheid.</p>
""",
    },
    {
        "slug": "herenarmbanden-stijl-aan-de-pols",
        "cat": "Accessoires",
        "title": "Herenarmbanden: stijl aan de pols",
        "dek": "Een armband maakt een outfit persoonlijk. Het draait om materiaal, kleur en de juiste maat.",
        "date": datetime.date(2026, 6, 5),
        "read": "6 min",
        "body": """
<p>De herenarmband is de laatste jaren een vast onderdeel van het straatbeeld geworden. Waar het accessoire vroeger vooral opviel, is het nu een rustige manier om een outfit af te maken. Het verschil tussen smaakvol en opzichtig zit in materiaal, kleur en pasvorm.</p>

<h2>Leer of natuursteen</h2>
<p>Grofweg vallen herenarmbanden in twee groepen. Leren armbanden ogen ingetogen en passen bij vrijwel elke gelegenheid, van casual tot net. Gevlochten leer geeft wat meer textuur, glad leer oogt strakker. Kralenarmbanden van natuursteen, zoals onyx of tijgeroog, brengen kleur en reliëf en vallen sneller op.</p>

<table class="compare">
  <tr><th>Type</th><th>Uitstraling</th><th>Past bij</th></tr>
  <tr><td>Glad leer</td><td>Strak en ingetogen</td><td>Net en zakelijk casual</td></tr>
  <tr><td>Gevlochten leer</td><td>Wat ruiger, textuurrijk</td><td>Casual en weekend</td></tr>
  <tr><td>Natuursteen kralen</td><td>Opvallender, kleurrijk</td><td>Vrijetijd en zomer</td></tr>
  <tr><td>Leer en kralen gecombineerd</td><td>Veelzijdig</td><td>Bijna alles</td></tr>
</table>

<h2>De juiste maat is de helft van het werk</h2>
<p>Een armband die te los zit, draait weg en oogt slordig. Een armband die te strak zit, knelt. De ideale pasvorm laat ongeveer een vinger speling tussen band en pols. Polsmaten lopen flink uiteen, dus een armband op maat zit merkbaar beter dan een standaardlengte. Een Nederlandse maker als <a href="https://milezbracelets.nl" rel="nofollow noopener" target="_blank">Milez Bracelets</a> maakt herenarmbanden handgemaakt en voor iedere polsmaat, van smal tot breed, zonder meerprijs voor maatwerk. Dat scheelt het gepuzzel met een band die net niet past.</p>

<div class="callout"><p>Wie de polsmaat niet kent, wikkelt een stukje touw of een centimeter rond de pols, net onder het polsbeentje, en meet de lengte. Daar komt de gewenste speling bij.</p></div>

<h2>Combineren met de rest</h2>
<p>Een armband hoeft niet alleen te blijven. Twee of drie dunne banden samen, een stack, geven een rustig laagje, mits de kleuren bij elkaar passen. Een veelgebruikte richtlijn: hou het metaal in de armband gelijk aan dat van het horloge. Zilverkleurige details bij een zilverkleurig horloge oogt rustiger dan een mix van tinten.</p>

<h2>Kleur afstemmen op de outfit</h2>
<p>Bruin leer sluit aan bij warme kleuren en bruine schoenen. Zwart leer is neutraal en past overal bij. Een kralenarmband met een kleur die terugkomt in het overhemd of de trui, bindt de outfit samen. Het accessoire werkt het best als het meedoet met het geheel, niet als losse blikvanger.</p>

<h2>Een armband als cadeau</h2>
<p>Een herenarmband is een veelgekozen cadeau voor een verjaardag of jubileum. Handgemaakte kwaliteit en een passende maat maken het persoonlijk, en een neutraal model in leer is een veilige keuze wanneer de voorkeur onbekend is. Een graveren van een naam of datum maakt het extra persoonlijk.</p>

<h2>Tot slot</h2>
<p>De herenarmband is een klein accessoire met merkbaar effect. Materiaal en kleur bepalen de uitstraling, de juiste maat bepaalt het comfort. Wie kiest voor een band die past bij de outfit en lekker om de pols zit, voegt iets persoonlijks toe zonder dat het opdringt.</p>
""",
    },
    {
        "slug": "van-casual-naar-zakelijk",
        "cat": "Stijl",
        "title": "Van casual naar zakelijk met één basis",
        "dek": "Met een paar slimme keuzes verschuift dezelfde outfit moeiteloos van weekend naar werkdag.",
        "date": datetime.date(2026, 5, 28),
        "read": "5 min",
        "body": """
<p>Veel mannen denken in aparte garderobes: een set voor het werk en een set voor de vrije tijd. Dat is niet nodig. Met een doordachte basis schuift dezelfde kleding van casual naar zakelijk, door een enkel onderdeel te wisselen.</p>

<h2>De gemene deler</h2>
<p>De sleutel zit in stuks die in beide werelden thuishoren. Een donkere jeans of nette chino, een effen overhemd en een paar schoenen die zowel net als casual kunnen, vormen samen het hart. Daar omheen bepaalt één laag of het geheel ontspannen of zakelijk leest.</p>

<h2>De schakelaars</h2>
<p>Een paar onderdelen doen het meeste werk in de overgang:</p>
<ul>
  <li><strong>De blazer.</strong> Over een overhemd en chino oogt het meteen verzorgd. Eraf en het wordt casual.</li>
  <li><strong>Het schoeisel.</strong> Witte sneakers houden het luchtig, leren veterschoenen tillen het naar net.</li>
  <li><strong>De bovenlaag.</strong> Een trui maakt het ontspannen, een colbert maakt het formeel.</li>
</ul>

<div class="callout"><p>Een overhemd dat in de broek wordt gedragen oogt netter, uit de broek juist losser. Eén handeling, twee uitstralingen.</p></div>

<h2>Een voorbeeld door de dag heen</h2>
<p>Stel: een effen lichtblauw overhemd op een donkere chino. Met witte sneakers en losse panden is dat een prima outfit voor een ontspannen dag. Overhemd in de broek, leren schoenen eronder en een blazer erbij, en hetzelfde geheel past bij een afspraak op kantoor. De basis blijft gelijk, alleen de randen veranderen.</p>

<table class="compare">
  <tr><th>Onderdeel</th><th>Casual</th><th>Zakelijk</th></tr>
  <tr><td>Bovenlaag</td><td>Trui of geen</td><td>Blazer of colbert</td></tr>
  <tr><td>Overhemd</td><td>Uit de broek</td><td>In de broek</td></tr>
  <tr><td>Schoenen</td><td>Witte sneakers</td><td>Leren veterschoenen</td></tr>
  <tr><td>Accessoire</td><td>Leren armband</td><td>Horloge, ingetogen</td></tr>
</table>

<h2>Kleur houdt het rustig</h2>
<p>Een veelzijdige basis vraagt om neutrale kleuren. Blauw, grijs en beige laten zich in beide richtingen sturen. Felle prints of opvallende kleuren binden zich sneller aan één gelegenheid en beperken daarmee de bruikbaarheid.</p>

<h2>Tot slot</h2>
<p>Wie investeert in stuks die beide kanten op kunnen, heeft minder kleding nodig en meer flexibiliteit. De truc zit niet in twee garderobes maar in een paar onderdelen die de toon zetten. Een blazer, het juiste schoeisel en de keuze om een overhemd wel of niet in de broek te dragen, doen het meeste werk.</p>
""",
    },
    {
        "slug": "kleurencombinaties-die-werken",
        "cat": "Stijl",
        "title": "Kleurencombinaties die het altijd doen",
        "dek": "Met een handvol betrouwbare combinaties zit een outfit vrijwel altijd goed in elkaar.",
        "date": datetime.date(2026, 5, 20),
        "read": "5 min",
        "body": """
<p>Kleur kiezen voelt voor veel mannen als gokken. Dat hoeft niet. Een paar combinaties zitten vrijwel altijd goed, en wie die kent, bouwt met vertrouwen een outfit op. De basis is rust: neutrale kleuren als fundament, met hoogstens een of twee accenten.</p>

<h2>De neutrale basis</h2>
<p>Blauw, grijs, beige, wit en zwart vormen samen een palet waarin bijna alles met alles combineert. Een outfit die volledig uit deze kleuren bestaat, zit altijd goed. Het is de veilige kern waar de rest omheen wordt gebouwd.</p>

<h2>Combinaties die zich bewijzen</h2>
<ul>
  <li><strong>Blauw en bruin.</strong> Een blauw overhemd met een bruine broek of bruine schoenen is een klassieker die warm en verzorgd oogt.</li>
  <li><strong>Grijs en wit.</strong> Rustig, fris en moeilijk fout te doen.</li>
  <li><strong>Beige en marineblauw.</strong> Een lichte chino met een donkerblauwe trui oogt zomers en net tegelijk.</li>
  <li><strong>Wit en denim.</strong> Een wit overhemd op een blauwe jeans is tijdloos.</li>
</ul>

<div class="callout"><p>Een veelgebruikte richtlijn is om bij een outfit niet meer dan drie kleuren aan te houden. Daarboven wordt het geheel snel onrustig.</p></div>

<h2>Werken met een accent</h2>
<p>Wie kleur wil toevoegen, doet dat het best met een enkel accent op een neutrale basis. Een groene trui bij een grijze broek, of een bordeauxrode sok onder een blauwe outfit. Het accent valt op doordat de rest rustig blijft. Komt de accentkleur op twee plekken subtiel terug, dan oogt het doordacht in plaats van toevallig.</p>

<table class="compare">
  <tr><th>Basis</th><th>Accent dat werkt</th><th>Effect</th></tr>
  <tr><td>Grijs en wit</td><td>Marineblauw</td><td>Fris en zakelijk</td></tr>
  <tr><td>Beige en blauw</td><td>Wit</td><td>Licht en zomers</td></tr>
  <tr><td>Marineblauw</td><td>Bruin leer</td><td>Warm en verzorgd</td></tr>
  <tr><td>Zwart en grijs</td><td>Bordeaux</td><td>Ingetogen met diepte</td></tr>
</table>

<h2>Let op materiaal en tint</h2>
<p>Kleur staat niet los van materiaal. Eenzelfde blauw oogt anders in een ruwe wol dan in glad katoen. Ook tinten onderling vragen aandacht: een koel grijs botst soms met een warm beige. Bij twijfel helpt het om stuks in daglicht naast elkaar te leggen.</p>

<h2>Tot slot</h2>
<p>Kleur is geen kwestie van geluk maar van een paar vaste principes. Een neutrale basis, hoogstens drie kleuren en een enkel accent dat terugkomt, leveren samen een outfit die klopt. Wie deze lijnen volgt, hoeft nooit meer te twijfelen voor de spiegel.</p>
""",
    },
    {
        "slug": "accessoires-die-een-outfit-afmaken",
        "cat": "Accessoires",
        "title": "Accessoires die een outfit afmaken",
        "dek": "De details bepalen het verschil. Een paar goed gekozen accessoires tillen een eenvoudige outfit op.",
        "date": datetime.date(2026, 5, 12),
        "read": "6 min",
        "body": """
<p>Een outfit staat of valt met de details. Kleding vormt het fundament, maar accessoires geven het geheel persoonlijkheid en afwerking. Het draait niet om veel, maar om de juiste keuzes op de juiste plek.</p>

<h2>Het horloge</h2>
<p>Het horloge is voor veel mannen het belangrijkste accessoire. Een rustig model met een leren of stalen band past bij vrijwel elke gelegenheid. De richtlijn is eenvoudig: stem de toon van de band af op de schoenen en de riem. Een bruine leren band loopt zo netjes mee met bruine schoenen.</p>

<h2>De armband</h2>
<p>Een armband voegt iets persoonlijks toe zonder dat het hoeft op te vallen. Leer oogt ingetogen, natuursteen brengt kleur. Belangrijk is dat de maat klopt, zodat de band niet wegdraait. Handgemaakte armbanden van een maker als <a href="https://milezbracelets.nl" rel="nofollow noopener" target="_blank">Milez Bracelets</a> worden op polsmaat gemaakt, wat het comfort merkbaar verbetert ten opzichte van een standaardlengte. Wie metaal in de armband afstemt op het horloge, houdt het geheel rustig.</p>

<div class="callout"><p>Minder is vaak meer. Een horloge en een enkele armband zien er verzorgder uit dan een pols vol losse stuks.</p></div>

<h2>De riem</h2>
<p>De riem is functioneel en zichtbaar tegelijk. Een leren riem hoort qua kleur bij de schoenen, zwart bij zwart en bruin bij bruin. De gesp blijft het best ingetogen. Voor net gebruik werkt een smalle, gladde riem, voor casual mag die wat breder en ruwer.</p>

<h2>Sokken als stil detail</h2>
<p>Sokken zijn een onderschat onderdeel. Onder een nette broek geven effen sokken in de kleur van de broek een rustige lijn. Wie durft, gebruikt de sok als klein accent met een ingetogen kleur of patroon. Belangrijk is de kwaliteit: een sok die goed zit, zakt niet af en knelt niet.</p>

<table class="compare">
  <tr><th>Accessoire</th><th>Net</th><th>Casual</th></tr>
  <tr><td>Horloge</td><td>Leren band, rustige wijzerplaat</td><td>Stalen of sportief model</td></tr>
  <tr><td>Armband</td><td>Glad leer, ingetogen</td><td>Natuursteen of gevlochten leer</td></tr>
  <tr><td>Riem</td><td>Smal, glad, kleur bij schoen</td><td>Breder, ruwer leer</td></tr>
  <tr><td>Sokken</td><td>Effen, kleur van de broek</td><td>Accentkleur of patroon</td></tr>
</table>

<h2>Een overhemd als basis</h2>
<p>Accessoires werken het best op een rustige ondergrond. Een effen overhemd in een neutrale kleur laat de details het werk doen. Te veel druk in de kleding en de accessoires verdwijnen in het geheel. De afwerking begint dus bij een schone basis.</p>

<h2>Tot slot</h2>
<p>Accessoires maken het verschil tussen aangekleed en afgemaakt. Een goed horloge, een passende armband, een riem die meedoet en sokken die kloppen, vormen samen de laatste laag. De kunst zit in de afstemming: kleuren en materialen die elkaar versterken in plaats van met elkaar wedijveren.</p>
""",
    },
]

ARTICLES_BY_DATE = sorted(ARTICLES, key=lambda a: a["date"], reverse=True)


def nl_date(d):
    months = ["januari", "februari", "maart", "april", "mei", "juni",
              "juli", "augustus", "september", "oktober", "november", "december"]
    return f"{d.day} {months[d.month-1]} {d.year}"


def article_jsonld(a, url):
    return f"""<script type="application/ld+json">
{{"@context":"https://schema.org","@type":"BlogPosting","headline":{a['title']!r},"description":{a['dek']!r},"datePublished":"{a['date'].isoformat()}","dateModified":"{a['date'].isoformat()}","author":{{"@type":"Organization","name":"Bal Herenkleding"}},"publisher":{{"@type":"Organization","name":"Bal Herenkleding"}},"mainEntityOfPage":{url!r},"articleSection":{a['cat']!r}}}
</script>"""


def render_article(a):
    url = f"{SITE}/nieuws/{a['slug']}.html"
    body = f"""<article class="article">
  <div class="wrap">
    <a class="backlink" href="/nieuws.html">&larr; Terug naar nieuws</a>
    <div class="head">
      <span class="tag">{a['cat']}</span>
      <h1>{a['title']}</h1>
      <p class="dek">{a['dek']}</p>
      <div class="meta"><span>{nl_date(a['date'])}</span><span>&middot;</span><span>{a['read']} lezen</span></div>
    </div>
    <div class="prose">{a['body']}</div>
  </div>
</article>
{article_jsonld(a, url)}"""
    return base(a["title"], a["dek"], body, "nieuws", url, og_type="article")


# ---------------------------------------------------------------------------
# Homepage
# ---------------------------------------------------------------------------

def render_home():
    cards = ""
    for a in ARTICLES_BY_DATE[:3]:
        cards += f"""<a class="card" href="/nieuws/{a['slug']}.html">
  <span class="cat">{a['cat']}</span>
  <h3>{a['title']}</h3>
  <p>{a['dek']}</p>
  <span class="m">{nl_date(a['date'])} &middot; {a['read']}</span>
</a>"""

    body = f"""<section class="hero">
  <div class="wrap">
    <div class="lead">
      <p class="eyebrow">Herenmode magazine</p>
      <h1>Goed gekleed gaan is een kwestie van een paar vaste principes.</h1>
      <p class="dek">Bal Herenkleding verzamelt nuchtere stijladviezen over pasvorm, materiaal en combineren. Geen modegril, wel kleding die klopt en lang meegaat.</p>
    </div>
    <dl class="spec" style="margin-top:46px">
      <div><dt>Onderwerp</dt><dd>Herenkleding</dd></div>
      <div><dt>Insteek</dt><dd>Praktisch en helder</dd></div>
      <div><dt>Voor</dt><dd>De man die het netjes wil</dd></div>
    </dl>
  </div>
</section>

<section class="block">
  <div class="wrap">
    <div class="sec-head">
      <h2>Recent op het platform</h2>
      <a class="link" href="/nieuws.html">Alle artikelen</a>
    </div>
    <div class="cards">{cards}</div>
  </div>
</section>

<section class="block">
  <div class="wrap">
    <div class="sec-head">
      <h2>Uitgelicht</h2>
    </div>
    <div class="feature">
      <div class="feat-card">
        <p class="eyebrow">Accessoires</p>
        <h3>Handgemaakte herenarmbanden</h3>
        <p>Milez Bracelets maakt leren en natuurstenen armbanden voor heren, handgemaakt in Nederland en op iedere polsmaat. Een ingetogen manier om een outfit persoonlijk te maken.</p>
        <a class="out" href="https://milezbracelets.nl" rel="nofollow noopener" target="_blank">Bekijk Milez Bracelets</a>
      </div>
      <div class="feat-card">
        <p class="eyebrow">Overhemden</p>
        <h3>Strijkvrije herenmode</h3>
        <p>HemdVoorHem.nl is gespecialiseerd in strijkvrije overhemden en aanverwante herenmode, met heldere maattabellen per merk. Handig bij het vergelijken van pasvormen.</p>
        <a class="out" href="https://www.hemdvoorhem.nl" rel="nofollow noopener" target="_blank">Bekijk HemdVoorHem.nl</a>
      </div>
    </div>
  </div>
</section>

<section class="block">
  <div class="wrap">
    <div class="sec-head"><h2>Beginnen bij de basis</h2><a class="link" href="/stijlgids.html">Naar de stijlgids</a></div>
    <p style="max-width:680px;color:var(--muted);font-size:1.05rem">De stijlgids bundelt de vaste principes uit de artikelen: van het opbouwen van een capsule garderobe tot het kiezen van de juiste pasvorm en betrouwbare kleurencombinaties. Een vertrekpunt voor wie structuur in de garderobe wil aanbrengen.</p>
  </div>
</section>"""
    org_jsonld = f"""<script type="application/ld+json">
{{"@context":"https://schema.org","@type":"WebSite","name":"Bal Herenkleding","url":"{SITE}/","description":"Onafhankelijk magazine over herenkleding met praktische stijladviezen."}}
</script>"""
    return base("Herenmode magazine",
                "Bal Herenkleding is een onafhankelijk magazine over herenkleding: praktische adviezen over pasvorm, materiaal, kleur en combineren.",
                body + "\n" + org_jsonld, "home", f"{SITE}/")


# ---------------------------------------------------------------------------
# Over
# ---------------------------------------------------------------------------

def render_over():
    body = """<section class="page">
  <div class="wrap">
    <span class="eyebrow">Over het platform</span>
    <h1>Wat Bal Herenkleding doet</h1>
    <div class="prose">
      <p>Bal Herenkleding is een onafhankelijk online magazine over herenkleding. Het platform verzamelt praktische adviezen over kleden, met aandacht voor pasvorm, materiaal, kleur en het combineren van stuks. Geen vluchtige trends, maar uitleg die ook over een paar jaar nog klopt.</p>

      <h2>De insteek</h2>
      <p>Veel mannen willen er verzorgd uitzien zonder er veel tijd aan te besteden. Dat is het uitgangspunt van dit platform. De artikelen leggen in heldere taal uit hoe kleding werkt: waarom een pasvorm belangrijker is dan een maatlabel, hoe een kleine garderobe meer combinaties oplevert, en welke kleuren het altijd doen.</p>

      <h2>Onafhankelijk en nuchter</h2>
      <p>De adviezen op Bal Herenkleding zijn praktisch en zonder opsmuk. Het platform verkoopt zelf geen kleding. Waar een merk of webshop wordt genoemd, gebeurt dat omdat het past bij het onderwerp, niet omdat het de teksten stuurt. Aanbevelingen blijven daardoor bruikbaar voor de lezer.</p>

      <h2>Voor wie</h2>
      <p>Het platform richt zich op mannen die het netjes willen hebben, of dat nu zakelijk, casual of ergens daartussenin is. Beginnen bij de basis, kiezen voor kwaliteit die meegaat en leren combineren staan centraal. Wie structuur in de garderobe wil aanbrengen, vindt hier een vertrekpunt.</p>

      <h2>Reageren of bijdragen</h2>
      <p>Tips, vragen of reacties zijn welkom via <a href="mailto:info@bal-herenkleding.nl">info@bal-herenkleding.nl</a>. Suggesties voor onderwerpen worden meegenomen in de planning van nieuwe artikelen.</p>
    </div>
  </div>
</section>"""
    return base("Over", "Bal Herenkleding is een onafhankelijk magazine over herenkleding met praktische, nuchtere stijladviezen over pasvorm, materiaal en combineren.",
                body, "over", f"{SITE}/over.html")


# ---------------------------------------------------------------------------
# Nieuws (index)
# ---------------------------------------------------------------------------

def render_nieuws():
    rows = ""
    for a in ARTICLES_BY_DATE:
        rows += f"""<a class="post-row" href="/nieuws/{a['slug']}.html">
  <div class="side"><span class="c">{a['cat']}</span>{nl_date(a['date'])}<br>{a['read']}</div>
  <div><h3>{a['title']}</h3><p>{a['dek']}</p></div>
</a>"""
    body = f"""<section class="page">
  <div class="wrap">
    <span class="eyebrow">Nieuws</span>
    <h1>Artikelen</h1>
    <div class="prose" style="max-width:680px"><p>Praktische stukken over herenkleding: pasvorm, materiaal, kleur en het combineren van een garderobe. De nieuwste artikelen staan bovenaan.</p></div>
    <div class="post-list" style="margin-top:34px">{rows}</div>
  </div>
</section>"""
    return base("Nieuws", "Alle artikelen van Bal Herenkleding over herenkleding: pasvorm, materiaal, kleur en het combineren van een garderobe.",
                body, "nieuws", f"{SITE}/nieuws.html")


# ---------------------------------------------------------------------------
# Stijlgids
# ---------------------------------------------------------------------------

def render_stijlgids():
    cards = ""
    for a in ARTICLES_BY_DATE:
        cards += f"""<a class="card" href="/nieuws/{a['slug']}.html">
  <span class="cat">{a['cat']}</span>
  <h3>{a['title']}</h3>
  <p>{a['dek']}</p>
  <span class="m">{a['read']}</span>
</a>"""
    body = f"""<section class="page">
  <div class="wrap">
    <span class="eyebrow">Stijlgids</span>
    <h1>De basis van goed kleden</h1>
    <div class="prose" style="max-width:720px">
      <p>Deze gids bundelt de vaste principes die in de artikelen terugkomen. Samen vormen ze een rode draad voor wie de garderobe wil opbouwen rond kleding die klopt en lang meegaat.</p>

      <h2>1. Begin bij een capsule</h2>
      <p>Een beperkt aantal goed gekozen stuks levert meer bruikbare combinaties op dan een volle kast. Neutrale kleuren en betrouwbare modellen vormen het fundament.</p>

      <h2>2. Let op pasvorm, niet alleen op maat</h2>
      <p>Een maatlabel zegt weinig over hoe een kledingstuk valt. Schoudernaad, taille en mouwlengte bepalen of iets echt goed zit.</p>

      <h2>3. Hou de kleuren rustig</h2>
      <p>Een neutrale basis met hoogstens een of twee accenten zit vrijwel altijd goed. Niet meer dan drie kleuren per outfit.</p>

      <h2>4. Maak het af met details</h2>
      <p>Een passend horloge, een ingetogen armband en sokken die kloppen vormen de laatste laag. Afstemming van kleur en materiaal doet het werk.</p>
    </div>
  </div>
</section>

<section class="block" style="border-top:1px solid var(--line)">
  <div class="wrap">
    <div class="sec-head"><h2>Lees verder</h2><a class="link" href="/nieuws.html">Alle artikelen</a></div>
    <div class="cards">{cards}</div>
  </div>
</section>"""
    return base("Stijlgids", "De stijlgids van Bal Herenkleding bundelt de basisprincipes van goed kleden: capsule garderobe, pasvorm, kleur en details.",
                body, "stijlgids", f"{SITE}/stijlgids.html")


# ---------------------------------------------------------------------------
# Partners
# ---------------------------------------------------------------------------

def render_partners():
    body = """<section class="page">
  <div class="wrap">
    <span class="eyebrow">Partners</span>
    <h1>Partners en uitgelichte merken</h1>
    <div class="prose" style="max-width:720px">
      <p>Bal Herenkleding werkt samen met merken en webshops die passen bij het onderwerp van het platform. Op deze pagina staan de partners die op dit moment worden uitgelicht. De selectie blijft beperkt en relevant, zodat aanbevelingen bruikbaar blijven voor de lezer.</p>
    </div>

    <div class="partner-grid" style="margin-top:34px">
      <div class="partner">
        <p class="role">Herenarmbanden</p>
        <h3>Milez Bracelets</h3>
        <p>Handgemaakte leren en natuurstenen armbanden voor heren, gemaakt in Nederland en op iedere polsmaat. Een ingetogen accessoire dat past bij vrijwel elke outfit.</p>
        <a class="out" href="https://milezbracelets.nl" rel="nofollow noopener" target="_blank">Naar milezbracelets.nl</a>
      </div>
      <div class="partner">
        <p class="role">Herenmode en overhemden</p>
        <h3>HemdVoorHem.nl</h3>
        <p>Specialist in strijkvrije overhemden en aanverwante herenmode, met een ruim aanbod aan merken en heldere maattabellen. Handig bij het vergelijken van pasvormen.</p>
        <a class="out" href="https://www.hemdvoorhem.nl" rel="nofollow noopener" target="_blank">Naar hemdvoorhem.nl</a>
  
      <div class="partner">
        <p class="role">Smartshop</p>
        <h3>Tatanka</h3>
        <p>Tatanka is een Nederlandse smartshop met paddo growkits en smartshopproducten, met uitleg per soort en een overzicht van het aanbod.</p>
        <a class="out" href="https://www.tatanka.nl/nl/thai-magic-mushroom-paddo-grow-kit/" rel="nofollow noopener" target="_blank">Thai magic mushroom growkit</a>
      </div>
      <div class="partner">
        <p class="role">Smartshop</p>
        <h3>Smartific</h3>
        <p>Smartific is een Nederlandse smartshop met magic truffels, growkits en smartshopproducten, inclusief productinformatie per artikel.</p>
        <a class="out" href="https://smartific.nl/dragons-dynamite-magic-truffels/" rel="nofollow noopener" target="_blank">Dragons Dynamite Truffels</a>
      </div>
      <div class="partner">
        <p class="role">Headshop</p>
        <h3>The Headshop</h3>
        <p>The Headshop is een Nederlandse headshop met kratom en smartshopproducten, met een uitgebreid overzicht per soort en sterkte.</p>
        <a class="out" href="https://www.headshop.nl/nl/" rel="nofollow noopener" target="_blank">Headshop</a>
      </div>
      <div class="partner">
        <p class="role">Paddo growkits</p>
        <h3>Paddo.shop</h3>
        <p>Paddo.shop is een Nederlandse webshop gespecialiseerd in paddo growkits, met uitleg per kweekset en kweekinstructies.</p>
        <a class="out" href="https://www.paddo.shop/ecuadorian-paddo-growkit/" rel="nofollow noopener" target="_blank">Ecuadorian paddo</a>
      </div>
      <div class="partner">
        <p class="role">Magic truffels</p>
        <h3>Magictruffels.shop</h3>
        <p>Magictruffels.shop is een Nederlandse webshop voor magic truffels, met een overzicht per soort en de werking ervan.</p>
        <a class="out" href="https://www.magictruffels.shop/atlantis/" rel="nofollow noopener" target="_blank">atlantis truffels</a>
      </div>
    </div>

    <p class="partner-note">Interesse in een vermelding of samenwerking? Voorstellen kunnen worden gestuurd naar <a href="mailto:info@bal-herenkleding.nl">info@bal-herenkleding.nl</a>. Partners worden alleen opgenomen wanneer ze aansluiten bij het onderwerp van het platform.</p>
  </div>
</section>"""
    return base("Partners", "De partners en uitgelichte merken van Bal Herenkleding: Milez Bracelets en HemdVoorHem.nl.",
                body, "partners", f"{SITE}/partners.html")


# ---------------------------------------------------------------------------
# Contact
# ---------------------------------------------------------------------------

def render_contact():
    body = """<section class="page">
  <div class="wrap">
    <span class="eyebrow">Contact</span>
    <h1>Contact opnemen</h1>
    <div class="prose" style="max-width:680px">
      <p>Vragen, tips, reacties of een voorstel voor samenwerking zijn welkom. Contact verloopt per e-mail.</p>
      <p style="margin:30px 0"><a class="contact-mail" href="mailto:info@bal-herenkleding.nl">info@bal-herenkleding.nl</a></p>
      <p>Berichten worden doorgaans binnen enkele werkdagen beantwoord. Suggesties voor onderwerpen worden meegenomen in de planning van nieuwe artikelen.</p>
    </div>
  </div>
</section>"""
    return base("Contact", "Neem contact op met Bal Herenkleding via info@bal-herenkleding.nl voor vragen, tips of samenwerking.",
                body, "contact", f"{SITE}/contact.html")


# ---------------------------------------------------------------------------
# Privacy
# ---------------------------------------------------------------------------

def render_privacy():
    body = f"""<section class="page">
  <div class="wrap">
    <span class="eyebrow">Juridisch</span>
    <h1>Privacybeleid</h1>
    <div class="prose">
      <p>Dit privacybeleid beschrijft hoe bal-herenkleding.nl omgaat met persoonsgegevens. Het platform verwerkt zo min mogelijk gegevens en houdt zich aan de Algemene verordening gegevensbescherming (AVG).</p>

      <h2>Welke gegevens worden verwerkt</h2>
      <p>De website is een informatief magazine zonder accounts, bestelproces of contactformulier. Er worden geen persoonsgegevens gevraagd of opgeslagen tijdens een bezoek. Wie per e-mail contact opneemt, deelt daarbij een e-mailadres en de inhoud van het bericht. Die gegevens worden uitsluitend gebruikt om het bericht te beantwoorden.</p>

      <h2>E-mailcontact</h2>
      <p>E-mails die worden gestuurd naar info@bal-herenkleding.nl worden bewaard zolang dat nodig is om de vraag of het verzoek af te handelen. Berichten worden niet gebruikt voor andere doeleinden en niet gedeeld met derden, tenzij een wettelijke verplichting daartoe verplicht.</p>

      <h2>Hosting</h2>
      <p>De website wordt gehost via Cloudflare Pages. De hostingpartij kan technische gegevens zoals een IP-adres kortstondig verwerken voor de levering en beveiliging van de website. Dit gebeurt op grond van een gerechtvaardigd belang in het veilig en betrouwbaar aanbieden van de site.</p>

      <h2>Externe links</h2>
      <p>De website bevat links naar externe websites van partners en andere partijen. Op die websites geldt het privacybeleid van de betreffende partij. Bal-herenkleding.nl is niet verantwoordelijk voor de verwerking van gegevens op externe websites.</p>

      <h2>Rechten</h2>
      <p>Wie via e-mail gegevens heeft gedeeld, heeft het recht op inzage, correctie of verwijdering van die gegevens. Een verzoek daartoe kan worden gestuurd naar info@bal-herenkleding.nl. Daarnaast bestaat het recht om een klacht in te dienen bij de Autoriteit Persoonsgegevens.</p>

      <h2>Wijzigingen</h2>
      <p>Dit privacybeleid kan worden aangepast wanneer de werkwijze van de website verandert. De meest actuele versie staat altijd op deze pagina.</p>

      <p style="color:var(--muted);font-size:14px;margin-top:30px">Laatst bijgewerkt: {nl_date(TODAY)}.</p>
    </div>
  </div>
</section>"""
    return base("Privacybeleid", "Het privacybeleid van bal-herenkleding.nl: welke gegevens worden verwerkt en hoe daarmee wordt omgegaan.",
                body, "", f"{SITE}/privacy.html")


# ---------------------------------------------------------------------------
# Cookies
# ---------------------------------------------------------------------------

def render_cookies():
    body = f"""<section class="page">
  <div class="wrap">
    <span class="eyebrow">Juridisch</span>
    <h1>Cookiebeleid</h1>
    <div class="prose">
      <p>Dit cookiebeleid legt uit welke cookies bal-herenkleding.nl gebruikt. Een cookie is een klein bestand dat een website op een apparaat kan plaatsen om informatie op te slaan.</p>

      <h2>Cookies op deze website</h2>
      <p>Bal-herenkleding.nl is een statische informatieve website zonder accounts, winkelwagen of trackingsystemen. De website plaatst zelf geen analytische of marketingcookies en volgt het surfgedrag van bezoekers niet. Er is daarom geen cookiemelding met toestemmingskeuze nodig voor het gebruik van de site.</p>

      <h2>Technische werking</h2>
      <p>De hostingpartij Cloudflare kan voor de beveiliging en goede werking van de website technisch noodzakelijke gegevens verwerken. Deze gegevens zijn niet bedoeld om bezoekers te identificeren of te volgen en worden uitsluitend gebruikt om de website veilig en betrouwbaar aan te bieden.</p>

      <h2>Externe websites</h2>
      <p>De website bevat links naar externe websites van partners en andere partijen. Zodra een bezoeker doorklikt naar zo'n website, gelden de cookies en het beleid van die partij. Bal-herenkleding.nl heeft daar geen invloed op. Het is raadzaam het cookiebeleid van de betreffende website te raadplegen.</p>

      <h2>Wijzigingen</h2>
      <p>Wanneer de werkwijze van de website verandert, bijvoorbeeld door de toevoeging van statistieken, wordt dit cookiebeleid aangepast en wordt waar nodig vooraf om toestemming gevraagd.</p>

      <p style="color:var(--muted);font-size:14px;margin-top:30px">Laatst bijgewerkt: {nl_date(TODAY)}.</p>
    </div>
  </div>
</section>"""
    return base("Cookiebeleid", "Het cookiebeleid van bal-herenkleding.nl. De website plaatst geen tracking- of marketingcookies.",
                body, "", f"{SITE}/cookies.html")


# ---------------------------------------------------------------------------
# Statische bestanden
# ---------------------------------------------------------------------------

FAVICON = """<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 64 64">
<rect width="64" height="64" rx="10" fill="#2E3A30"/>
<text x="32" y="44" font-family="Georgia, serif" font-size="34" font-weight="600" fill="#F3F2EE" text-anchor="middle">B</text>
</svg>"""

HEADERS = """/*
  X-Content-Type-Options: nosniff
  X-Frame-Options: SAMEORIGIN
  Referrer-Policy: strict-origin-when-cross-origin
  Permissions-Policy: geolocation=(), microphone=(), camera=()

/style.css
  Cache-Control: public, max-age=86400

/favicon.svg
  Cache-Control: public, max-age=604800
"""

ROBOTS = f"""User-agent: *
Allow: /

Sitemap: {SITE}/sitemap.xml
"""

README = """# bal-herenkleding.nl

Statische site, deploybaar via GitHub + Cloudflare Pages.

## Structuur
- `site/` bevat de volledige, deploybare website
- `build.py` genereert de site opnieuw vanuit content in het script

## Opnieuw bouwen
    python3 build.py

## Deploy via Cloudflare Pages
1. Push de repository naar GitHub.
2. Maak in Cloudflare een nieuw Pages-project en koppel de repo.
3. Build command: leeg laten (of `python3 build.py`).
4. Build output directory: `site`
5. Koppel het domein bal-herenkleding.nl aan het project.

Een nieuw artikel toevoegen: voeg een blok toe aan de lijst ARTICLES in build.py en draai het script opnieuw.
"""


def sitemap():
    urls = [
        (f"{SITE}/", "1.0"),
        (f"{SITE}/over.html", "0.6"),
        (f"{SITE}/nieuws.html", "0.9"),
        (f"{SITE}/stijlgids.html", "0.8"),
        (f"{SITE}/partners.html", "0.6"),
        (f"{SITE}/contact.html", "0.5"),
        (f"{SITE}/privacy.html", "0.3"),
        (f"{SITE}/cookies.html", "0.3"),
    ]
    for a in ARTICLES:
        urls.append((f"{SITE}/nieuws/{a['slug']}.html", "0.7"))
    lastmod = TODAY.isoformat()
    body = '<?xml version="1.0" encoding="UTF-8"?>\n<urlset xmlns="http://www.sitemaps.org/schemas/sitemap/0.9">\n'
    for loc, prio in urls:
        body += f"  <url><loc>{loc}</loc><lastmod>{lastmod}</lastmod><priority>{prio}</priority></url>\n"
    body += "</urlset>\n"
    return body


# ---------------------------------------------------------------------------
# Schrijven
# ---------------------------------------------------------------------------

def write(path, content):
    full = os.path.join(OUT, path)
    os.makedirs(os.path.dirname(full), exist_ok=True)
    with open(full, "w", encoding="utf-8") as f:
        f.write(content)
    print("  ", path)


def main():
    os.makedirs(os.path.join(OUT, "nieuws"), exist_ok=True)
    print("Genereren:")
    write("index.html", render_home())
    write("over.html", render_over())
    write("nieuws.html", render_nieuws())
    write("stijlgids.html", render_stijlgids())
    write("partners.html", render_partners())
    write("contact.html", render_contact())
    write("privacy.html", render_privacy())
    write("cookies.html", render_cookies())
    for a in ARTICLES:
        write(f"nieuws/{a['slug']}.html", render_article(a))
    write("favicon.svg", FAVICON)
    write("robots.txt", ROBOTS)
    write("sitemap.xml", sitemap())
    write("_headers", HEADERS)
    with open(os.path.join(os.path.dirname(__file__), "README.md"), "w", encoding="utf-8") as f:
        f.write(README)
    print("Klaar.")


if __name__ == "__main__":
    main()
