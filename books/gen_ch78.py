#!/usr/bin/env python3
"""Generate ch007-ch008 infographic HTML for 杜甫的五城 (ZH + EN)"""
import os

BOOKDIR = os.path.expanduser("~/.openclaw/workspace/infographics/books")
SLUG = "杜甫的五城"

CSS = """*{margin:0;padding:0;box-sizing:border-box}
@font-face{font-family:'FZXPYZS';src:url('../方正屏显雅宋简体.TTF') format('truetype')}
body{background:#f5f1eb;font-family:'FZXPYZS','PingFang SC','Noto Serif SC','STSong',Georgia,serif;color:#2d2d2d;line-height:1.8;display:flex;justify-content:center;align-items:flex-start;min-height:100vh;padding:40px 16px 60px}
.container{max-width:880px;width:100%}
.back-catalog{display:inline-block;font-size:13px;color:#4f46e5;text-decoration:none;margin-bottom:12px;transition:color .15s}
.back-catalog:hover{color:#dc2626}
.lang-switch{float:right;display:inline-block;font-size:13px;color:#4f46e5;text-decoration:none;border:1px solid #4f46e5;border-radius:6px;padding:4px 14px;transition:all .15s}
.lang-switch:hover{background:#4f46e5;color:#fff}
h1{font-family:'FZXPYZS','PingFang SC',serif;font-size:26px;color:#1a1a1a;margin-top:20px;margin-bottom:6px;letter-spacing:.03em;line-height:1.4}
.subtitle{font-size:15px;color:#888;margin-bottom:20px;letter-spacing:.05em}
.divider{width:60px;height:3px;background:linear-gradient(90deg,#dc2626,#ea580c,#ca8a04,#4f46e5,#db2777);border-radius:2px;margin:20px 0 28px}
.overview{background:#eef2ff;border-left:4px solid #4f46e5;border-radius:10px;padding:20px 24px;margin-bottom:32px;font-size:15px;color:#444;line-height:1.9}
.kpi-row{display:flex;flex-wrap:wrap;gap:12px;margin-bottom:36px}
.kpi-card{flex:1;min-width:140px;background:#fff;border-radius:10px;padding:18px 16px;text-align:center;box-shadow:0 1px 4px rgba(0,0,0,.06)}
.kpi-card.c01{border-top:3px solid #dc2626}
.kpi-card.c02{border-top:3px solid #ea580c}
.kpi-card.c03{border-top:3px solid #ca8a04}
.kpi-card.c04{border-top:3px solid #4f46e5}
.kpi-icon{font-size:28px;margin-bottom:6px}
.kpi-value{font-size:18px;font-weight:700;color:#1a1a1a;margin-bottom:4px}
.kpi-label{font-size:12px;color:#888;line-height:1.6}
.section{counter-increment:sec;background:#fff;border-radius:12px;padding:24px 28px;margin-bottom:20px;box-shadow:0 1px 4px rgba(0,0,0,.05)}
.section.c01{border-left:4px solid #dc2626}
.section.c02{border-left:4px solid #ea580c}
.section.c03{border-left:4px solid #ca8a04}
.section.c04{border-left:4px solid #4f46e5}
.section.c05{border-left:4px solid #db2777}
.section-title{font-size:17px;font-weight:700;color:#1a1a1a;margin-bottom:10px;display:flex;align-items:center;gap:10px}
.section-title .num{display:inline-flex;align-items:center;justify-content:center;width:28px;height:28px;border-radius:50%;color:#fff;font-size:13px;font-weight:700;flex-shrink:0}
.section.c01 .num{background:#dc2626}
.section.c02 .num{background:#ea580c}
.section.c03 .num{background:#ca8a04}
.section.c04 .num{background:#4f46e5}
.section.c05 .num{background:#db2777}
.section-body{font-size:14px;color:#555;line-height:1.9}
.takeaway{background:#fff;border-left:4px solid #dc2626;border-radius:10px;padding:20px 24px;margin-top:32px;margin-bottom:36px;font-size:15px;color:#1a1a1a;font-weight:600;line-height:1.8}
.takeaway-label{display:inline-block;background:#dc2626;color:#fff;font-size:11px;padding:3px 10px;border-radius:4px;margin-bottom:10px;letter-spacing:.05em}
.footer{text-align:center;font-size:12px;color:#bbb;padding-top:20px;border-top:1px solid #e8e0d5;margin-top:12px}
.footer a{color:#bbb;text-decoration:none}
@media(max-width:640px){
  .container{padding:0 12px}
  h1{font-size:22px}
  .kpi-card{min-width:120px}
  .section{padding:18px 20px}
}"""

def make_kpi_html(kpis):
    out = ""
    for i, k in enumerate(kpis):
        cls = f"c0{i+1}"
        out += f'  <div class="kpi-card {cls}">\n'
        out += f'    <div class="kpi-icon">{k["icon"]}</div>\n'
        out += f'    <div class="kpi-value">{k["value"]}</div>\n'
        out += f'    <div class="kpi-label">{k["label"]}</div>\n'
        out += '  </div>\n'
    return out

def make_sec_html(sections):
    out = ""
    for i, s in enumerate(sections):
        cls = f"c0{i+1}"
        out += f'<div class="section {cls}">\n'
        out += f'  <div class="section-title"><span class="num">{i+1:02d}</span>{s["title"]}</div>\n'
        out += f'  <div class="section-body">{s["body"]}</div>\n'
        out += '</div>\n'
    return out

def make_page_html(ch_num, ch_title, subtitle, overview, kpis, sections, takeaway, takeaway_label, footer_text, back_label, en_href, en_tab):
    return f"""<!DOCTYPE html>
<html lang="zh-CN">
<head>
<meta charset="UTF-8">
<meta name="viewport" content="width=device-width,initial-scale=1.0">
<title>杜甫的五城 · 第{ch_num}章「{ch_title}」</title>
<style>
{CSS}
</style>
</head>
<body>
<div class="container">

<a class="back-catalog" href="杜甫的五城-catalog.html">{back_label}</a>
<a class="lang-switch" target="_blank" href="{en_href}">{en_tab}</a>

<h1>杜甫的五城 · 第{ch_num}章「{ch_title}」</h1>
<div class="subtitle">{subtitle}</div>
<div class="divider"></div>

<div class="overview">
  <p>{overview}</p>
</div>

<div class="kpi-row">
{make_kpi_html(kpis)}</div>
{make_sec_html(sections)}
<div class="takeaway">
  <div class="takeaway-label">{takeaway_label}</div>
  {takeaway}
</div>

<div class="footer">
  {footer_text}
</div>

</div>
</body>
</html>"""


def build_ch(ch_num, title, subtitle, ov_zh, ov_en, kpi_zh, kpi_en, sec_zh, sec_en, take_zh, take_en):
    cn_num = int(ch_num)
    zh_path = os.path.join(BOOKDIR, f"{SLUG}-ch{ch_num}-info-zh.html")
    en_path = os.path.join(BOOKDIR, f"{SLUG}-ch{ch_num}-info-en.html")

    zh_html = make_page_html(
        ch_num=cn_num, ch_title=title, subtitle=subtitle,
        overview=ov_zh, kpis=kpi_zh, sections=sec_zh,
        takeaway=take_zh, takeaway_label="💡 核心启示",
        footer_text=f"杜甫的五城 · 第{cn_num}章「{title}」 | 赖瑞和 著 · 一位唐史学者的寻踪壮游",
        back_label="← 返回章节目录",
        en_href=f"{SLUG}-ch{ch_num}-info-en.html", en_tab="EN"
    )
    with open(zh_path, "w", encoding="utf-8") as f:
        f.write(zh_html)

    en_html = make_page_html(
        ch_num=cn_num, ch_title=title, subtitle=subtitle,
        overview=ov_en, kpis=kpi_en, sections=sec_en,
        takeaway=take_en, takeaway_label="💡 Key Insight",
        footer_text=f"Five Cities of Du Fu · Ch.{cn_num} 「{title}」 | Lai Ruihe · A Tang Historian's Grand Tour",
        back_label="← Back to Catalog",
        en_href=f"{SLUG}-ch{ch_num}-info-zh.html", en_tab="中文"
    )
    with open(en_path, "w", encoding="utf-8") as f:
        f.write(en_html)

    results = []
    for lang, path in [("ZH", zh_path), ("EN", en_path)]:
        with open(path) as fh:
            c = fh.read()
        opens = c.count("<div")
        closes = c.count("</div>")
        diff = opens - closes
        s = "✅" if diff == 0 else f"❌ diff={diff}"
        results.append(f"{s} {lang} ch{ch_num}: {os.path.basename(path)} div={opens}/{closes} diff={diff}")
    return results


# ═══ CHAPTER 7: 谁谓河广 ═══
OV7_ZH = """从呼和浩特南下大同，赖瑞和开启了穿越山西、北京的旅程。在大同访云冈石窟，考证「云冈」与「云岗」之辨；在北京西山意外走进曹雪芹晚年故居；乘389次列车穿越太行山井陉险道；搭583次普客——「简直就是一列浪漫的古董火车」——木造座椅、木造行李架，在雨中慢慢驶向运城。在运城亲眼见到《资治通鉴》中反复提及的盐池，「这『池』简直就是个大海啊！」最终渡黄河入洛阳，访龙门石窟与隋唐含嘉仓——读《资治通鉴》十年，不如来此一行。"""

OV7_EN = """From Hohhot south to Datong, Lai Ruihe began a journey through Shanxi and Beijing. At Datong he visited the Yungang Grottoes and verified the correct Chinese character for 'Yungang'; in Beijing's Western Hills he unexpectedly stumbled into Cao Xueqin's former residence; he took Train 389 through the treacherous Jingxing Pass of the Taihang Mountains; then boarded Train 583, a slow ordinary passenger train—'a genuinely romantic antique train'—with wooden seats and wooden luggage racks, creeping through rain toward Yuncheng. At Yuncheng he saw with his own eyes the salt pool repeatedly mentioned in Zizhi Tongjian: 'This pool is practically a sea!' Finally crossing the Yellow River by ferry to Luoyang, he visited Longmen Grottoes and the Sui-Tang Hanjiacang Granary—a decade reading Zizhi Tongjian could not match this single visit."""

TAKE7_ZH = """从北魏云冈到隋唐含嘉仓，从太行山古董列车到运城八十公里盐池——读《资治通鉴》十年，不如亲临盐池一行。而那包带回香港的运城陆盐，炒出的菜心带着泥土之味，正是中国大地最真实的滋味。"""
TAKE7_EN = """From Northern Wei Yungang to Sui-Tang Hanjiacang, from an antique train through the Taihang Mountains to Yuncheng's 80-km salt lake—a decade reading Zizhi Tongjian cannot match one visit to the salt pool. And that bag of Yuncheng land salt, stir-fried with choy sum, carried the taste of China's very soil."""

# ═══ CHAPTER 8: 南诏缘 ═══
OV8_ZH = """第三年中国内地行，赖瑞和从香港直飞昆明，开启为期两月的西南之旅。在昆明访西南联大旧址，在石林赏怪石，在大理苍山洱海间徜徉——但此行真正的目的，是寻访一通鲜为人知的唐代石碑：「南诏德化碑」。在大理太和村高坡上，他亲手触摸了这通一千二百多年前南诏国王阁逻凤竖立的建国纪念碑。更意外的是，在剑川县改乘手扶拖拉机颠簸六小时深入深山，竟发现了极为罕见的石钟山石窟——南诏王异牟寻与阁逻凤的精美雕像，至今保存完好。"""

OV8_EN = """On his third mainland China trip, Lai Ruihe flew from Hong Kong to Kunming, beginning a two-month journey through the southwest. He visited the site of Southwest Associated University in Kunming, marveled at the Stone Forest, and wandered between Cangshan Mountain and Erhai Lake in Dali—but his true purpose was to find a little-known Tang dynasty stele: the 'Nanzhao Dehua Stele.' On a high slope in Taihe Village near Dali, he touched with his own hands this founding monument erected by Nanzhao King Geluofeng over 1,200 years ago. Even more unexpectedly, taking a hand-tractor for six bone-jarring hours into the deep mountains near Jianchuan, he discovered the extraordinarily rare Shizhongshan Grottoes—exquisitely carved statues of Nanzhao kings Yimouxun and Geluofeng, perfectly preserved to this day."""

TAKE8_ZH = """一通一千二百年唐碑、六小时拖拉机颠晃、十六座深山洞窟——南诏不只在《资治通鉴》的边陲战事中，更在太和村高坡上的巨石碑身中，在守碑人寂寞的烟卷里，在拖拉机虎口震痛的双手间。"""
TAKE8_EN = """A 1,200-year-old Tang stele, six hours of tractor jolting, sixteen mountain grottoes—Nanzhao exists not only in the border wars of Zizhi Tongjian, but in the massive stone at Taihe Village, in the lonely caretaker's cigarette smoke, and between aching hands gripping a tractor's iron bar."""


# ──────────── CHAPTER 7 DATA ────────────
KPI7_ZH = [
    {"icon":"🚂","value":"5段列车","label":"呼市→大同→北京<br>→太原→运城→洛阳<br>穿越山西·河北·河南"},
    {"icon":"🏛️","value":"3处石窟","label":"云冈·龙门·曹雪芹<br>西山故居·含嘉仓<br>井陉太行险道"},
    {"icon":"🧂","value":"80km盐池","label":"运城盐池·大地之母<br>宽2km·长80km<br>以陆盐炒菜心寄乡愁"},
    {"icon":"⛴️","value":"黄河古渡","label":"平陆茅津渡口<br>「谁谓河广？一苇杭之」<br>不足百米·钢铁平底船"},
]
KPI7_EN = [
    {"icon":"🚂","value":"5 Train Segments","label":"Hohhot→Datong→Beijing<br>→Taiyuan→Yuncheng→Luoyang<br>Across Shanxi · Hebei · Henan"},
    {"icon":"🏛️","value":"3 Grotto Sites","label":"Yungang · Longmen<br>Cao Xueqin's former home<br>Hanjiacang Granary · Jingxing"},
    {"icon":"🧂","value":"80 km Salt Lake","label":"Yuncheng Salt Pool<br>2 km wide · 80 km long<br>Cooked choy sum with land salt"},
    {"icon":"⛴️","value":"Yellow River Ferry","label":"Maodu Crossing at Pinglu<br>'Who says the river is wide?'<br>Under 100m · flat steel boat"},
]

SEC7_ZH = [
    {"title":"云冈石窟：考证一个「冈」字",
     "body":"大同就是北魏迁都洛阳前的都城平城。作者第二天便去寻访云冈石窟——那几座大佛「已经将近一千五百年了，永远那么慈悲地笑着，石头雕成的笑」。返港后宾馆收据成了重要考证依据：台湾和香港旅行文学几乎无一例外写成「云岗」——「这其实是错的」。宾馆收据上清楚印着「云冈」。「《辞海》等辞典只收『云冈』，没有『云岗』。」一个字的考证，折射出学者游历的独特视角。"},
    {"title":"北京西山：偶然走进曹雪芹故居",
     "body":"在北京，「除了出了个乱唐的安禄山之外，就没有什么唐或唐以前的遗物了」。作者在西山植物园闲走时，无意中见到「曹雪芹纪念馆」路牌——走过小桥，一排深褐色木造平房便是雪芹晚年故居。屋后竖立六七通清代古碑，碑额完美无缺。「雪芹晚年在这一片清幽的风景中写作，还有一名仆人服侍，虽说『潦倒』，恐怕还是远胜许多现代作家的。」"},
    {"title":"583次普客：浪漫的古董火车",
     "body":"从太原到运城，作者选了583次普通旅客列车——「上了『5』字头，便是十分缓慢的慢车」。车厢古色古香：木造座椅、木造行李架、木造窗子。「如果把这列车好好保养，把木质的纹路都擦得晶亮，简直就是一列浪漫的古董火车啊。」细雨在窗外下着，给深褐色泽更添寒意中的温馨。全程四百一十二公里，走了十一个小时——「我不赶路，十一个小时就十一个小时吧。」"},
    {"title":"运城盐池：读《通鉴》十年不如一行",
     "body":"当年读《资治通鉴》，以为河中节度使争夺的盐池不过是「像养鱼的池塘那样大小」。第二天站到盐池边一看，才知道自己大错特错——「这『池』简直就是个大海啊。」宽两公里，长八十公里。老盐工林师傅开了十七年盐车，「盐池的几乎每一个角落，他都到过」。作者买了一小包运城精盐带回香港，炒了一碟菜心：「吃着吃着，我才惊觉，这陆盐不就是中国泥土的一部分吗？」"},
    {"title":"茅津渡河与洛阳含嘉仓",
     "body":"从平陆茅津渡口乘钢铁平底船过黄河，「它顺着河水东流的冲击力，一会儿就漂啊漂到斜对岸」。这里黄河不到百米宽——「谁谓河广？一苇杭之」。在洛阳寻访隋唐含嘉仓，管理员「平静的语气中好像隐藏着一种辛酸」：「当年我也参加发掘工作，以后就一直在这儿，十多年了。」四百多个地窖「最大的十八米直径」，储藏江南租税粮——武则天和那几位「逐粮天子」所吃的粮，恐怕都来自此仓。"},
]
SEC7_EN = [
    {"title":"Yungang Grottoes: Verifying a Single Character",
     "body":"Datong was Pingcheng, capital of the Northern Wei before moving to Luoyang. The author visited Yungang the next day: those giant Buddhas have sat here for nearly 1,500 years, smiling forever with compassion, smiles carved from stone. Back in Hong Kong, the hotel receipt became crucial evidence: Taiwan and Hong Kong travel writing almost uniformly wrote the wrong character. The receipt clearly printed the correct one. Dictionaries like Cihai only list the correct form. A single character's verification revealed the scholar-traveler's unique lens."},
    {"title":"Western Hills: Stumbling into Cao Xueqin's Home",
     "body":"In Beijing, apart from An Lushan who plunged the Tang into chaos, there is nothing Tang or pre-Tang. Wandering in the Beijing Botanical Garden, he spotted a sign for the Cao Xueqin Memorial. Across a small bridge, a row of dark-brown wooden bungalows: the author of Dream of the Red Chamber spent his final years here. Behind them stood six or seven Qing stone steles with pristine tops. Though destitute, with a servant attending him and this serene landscape, Xueqin's life was likely far better than many modern writers."},
    {"title":"Train 583: A Romantic Antique on Rails",
     "body":"Taiyuan to Yuncheng, he chose the 583 ordinary passenger train, the slowest classification. The carriage was antique: wooden seats, wooden luggage racks, wooden windows. If properly maintained, wood grain polished to a gleam, this would be a genuinely romantic antique train. Drizzle outside added warmth to the dark-brown interior. 412 km, eleven hours: he was not in a hurry. Eleven hours it would be."},
    {"title":"Yuncheng Salt Pool: Decade of Reading vs. One Visit",
     "body":"Reading Zizhi Tongjian, he had imagined the salt pool fought over by regional governors as a mere pond for raising fish. Standing at its edge the next morning, he realized his colossal error: this pool is practically a sea! Two km wide, eighty km long. Veteran salt-truck driver Master Lin, seventeen years on the road, had been to nearly every corner. The author bought a small bag of Yuncheng salt, brought it to Hong Kong, and stir-fried choy sum: As he ate, it struck him: is not this land salt a part of China's very soil?"},
    {"title":"Maojin Ferry & Luoyang's Hanjiacang Granary",
     "body":"Crossing the Yellow River at Maojin Ferry on a flat steel boat: it drifted with the river's eastward current, soon landing on the opposite bank. Here the river was under 100 meters wide: Who says the river is wide? One reed could cross it. In Luoyang, seeking the Sui-Tang Hanjiacang Granary, the caretaker spoke with a calm tone that seemed to hide bitterness: he had taken part in the excavation himself and had been there ever since, over ten years. Over 400 pits, the largest 18 meters in diameter, stored grain-tax from Jiangnan: the very grain that fed Empress Wu and those grain-chasing emperors."},
]

# ──────────── CHAPTER 8 DATA ────────────
KPI8_ZH = [
    {"icon":"🗿","value":"1,200年唐碑","label":"南诏德化碑·公元766年<br>阁逻凤建国纪念碑<br>3,800字今剩数百"},
    {"icon":"🚜","value":"6小时拖拉机","label":"剑川→石钟山石窟<br>手扶拖拉机·深山颠晃<br>双臂晒黑虎口震痛"},
    {"icon":"🛕","value":"3处南诏瑰宝","label":"德化碑·石钟山石窟<br>太和城遗址<br>大理苍山洱海"},
    {"icon":"🏫","value":"两个月旅程","label":"第三次内地行<br>昆明→大理→剑川→丽江<br>西南联大旧址寻访"},
]
KPI8_EN = [
    {"icon":"🗿","value":"1,200-Yr Tang Stele","label":"Nanzhao Dehua Stele · 766 CE<br>King Geluofeng's founding<br>monument · 3,800 to few hundred chars"},
    {"icon":"🚜","value":"6-Hour Tractor Ride","label":"Jianchuan to Shizhongshan<br>Hand-tractor · deep mountains<br>Sunburned arms · aching hands"},
    {"icon":"🛕","value":"3 Nanzhao Treasures","label":"Dehua Stele · Shizhongshan<br>Taihe City ruins<br>Cangshan & Erhai, Dali"},
    {"icon":"🏫","value":"2-Month Journey","label":"Third mainland trip<br>Kunming→Dali→Jianchuan→Lijiang<br>SW Associated University site"},
]

SEC8_ZH = [
    {"title":"昆明：西南联大的角落",
     "body":"在昆明，作者「不免随俗」去了西山龙门、滇池、石林。但真正打动他的是云南师范大学校园内西南联大的旧址——「那一排低矮简陋的小教室，默默立在校园内一个不起眼的角落。真难想象，当年那么多知名的学者、诗人、小说家和物理学家，曾经在那里待过长长的八年抗战时光。」闻一多的雕像也竖立在校园内。路过蒙自——「小说家沈从文当年住过的地方」——历史和文学的厚重感一路伴随。"},
    {"title":"南诏德化碑：触摸一千二百年的历史",
     "body":"在大理，他最想看的是鲜有人知的「南诏德化碑」——一通南诏国王阁逻凤在公元766年竖立的建国纪念碑。「黑压压的巨石，发出一种无比威严的光彩。」碑身严重风化，原本三千八百多字，如今只剩几百字。「我绕着石碑走了一圈，再用手轻轻触摸它的碑身，觉得自己仿佛在触摸南诏和唐代的历史，那么具体而真实。」守碑人寂寞地守在荒凉碑亭旁，「似乎这里很少有访客，连这位守碑人都感到寂寞无比」。"},
    {"title":"石钟山石窟：拖拉机上的南诏因缘",
     "body":"从大理赴丽江途中，地图上偶然读到石钟山石窟的介绍——「第二窟为《阁逻凤出行图》」。这位阁逻凤，正是德化碑的竖立者！作者立刻改变行程，在剑川下车。坐上拖拉机深入山区，「我站在车斗上，双手紧紧握着车斗前头的一根横铁条……上石钟山去了。」二十五公里走了三个多小时，中途休息数次。石窟「静悄悄地藏在深山中，没有什么游客，幽静极了。」"},
    {"title":"南诏王雕像：世间罕见的精美石窟",
     "body":"石钟寺八窟中，第一窟《南诏王异牟寻朝议图》和第二窟《阁逻凤出行图》「雕刻得极为华美精致，而且居然保存得那么完美」。第八窟刻着巨大的女性生殖器——白族的「阿央白」崇拜，是母系社会的遗迹。遗憾的是「这些石窟连照片也不多见」，管理员也不容许拍照。作者感慨：「难怪外界几乎不知道云南有这么一个精彩的石窟。」临走时买了守碑人代售的碑文译注本，作为稀罕纪念。"},
    {"title":"大山深处的寂寞与坚守",
     "body":"售票的年轻人在读《法学概论》准备考大学，「能够在这么安静的环境中读书，我还真有点羡慕他的福气」。但他每月只能下山一次，「菜得自己种，肉每星期才能吃一次」。往返六小时拖拉机，双臂晒黑，虎口酸痛。但作者认为「这真是一段难忘的旅程，也让我多结了一段南诏缘」。回到香港后，他还查阅了文物专家宋伯胤1957年的文章，对「阿央白」雕刻提出质疑——学者的好奇心永不满足。"},
]
SEC8_EN = [
    {"title":"Kunming: A Corner of SW Associated University",
     "body":"In Kunming, the author followed custom to West Hills, Dianchi Lake, and Stone Forest. But what truly moved him was the site of Southwest Associated University inside Yunnan Normal University: a row of low, crude classrooms quietly occupying an inconspicuous corner of the campus. Hard to imagine so many renowned scholars, poets, novelists, and physicists spent eight long wartime years there. A statue of Wen Yiduo also stood on campus. Passing Mengzi, where novelist Shen Congwen once lived, the weight of history and literature accompanied him throughout."},
    {"title":"The Nanzhao Dehua Stele: Touching 1,200 Years",
     "body":"In Dali, his chief aim was the little-known Nanzhao Dehua Stele, a founding monument erected by King Geluofeng in 766 CE. The dark, massive stone emanated an incomparably solemn radiance. Heavily weathered, of 3,800 original characters only a few hundred remained. He walked around the stele, then gently touched its surface with his hand: he felt as if he were touching the very history of Nanzhao and Tang China, so concrete and real. The lonely caretaker stood by the desolate pavilion: so few visitors came that even the guardian seemed profoundly lonely."},
    {"title":"Shizhongshan Grottoes: A Nanzhao Adventure by Tractor",
     "body":"En route from Dali to Lijiang, he read on a map about Shizhongshan Grottoes: Cave 2 depicts King Geluofeng's Procession. This was the very king who erected the Dehua Stele! He immediately changed plans, alighting at Jianchuan. Boarding a hand-tractor into the mountains, he stood on the trailer, gripping the iron bar ahead with both hands, heading up to Shizhongshan. Twenty-five kilometers took over three hours with rest stops. The grottoes hid silently in deep mountains, no tourists, extraordinarily serene."},
    {"title":"Nanzhao King Sculptures: Rare, Exquisite Masterpieces",
     "body":"Of eight caves at Shizhong Temple, Cave 1, King Yimouxun's Court Assembly, and Cave 2, King Geluofeng's Procession, were carved with astonishing refinement and preserved so perfectly. Cave 8 featured a giant female reproductive organ: the Bai people's Ayangbai fertility worship, a matriarchal vestige. Sadly, photos of these caves are rare, and photography was forbidden. No wonder the outside world barely knows Yunnan has such splendid grottoes. He bought annotated stele texts from the caretaker as a rare souvenir."},
    {"title":"Solitude & Devotion in the Deep Mountains",
     "body":"The young ticket-seller was studying Introduction to Law, preparing for university exams: he rather envied his good fortune, being able to study in such quiet surroundings. But he could descend the mountain only once a month, growing his own vegetables, eating meat once a week. Six hours of tractor riding left arms sunburned and hands aching. Yet this was truly an unforgettable journey, adding another strand to his Nanzhao connection. Back in Hong Kong, he even consulted antiquities expert Song Boyin's 1957 article questioning the Ayangbai carving: a scholar's curiosity never rests."},
]


all_results = []
all_results += build_ch("007", "谁谓河广", "大同·北京·太原·运城·盐池·洛阳",
    OV7_ZH, OV7_EN, KPI7_ZH, KPI7_EN, SEC7_ZH, SEC7_EN, TAKE7_ZH, TAKE7_EN)
all_results += build_ch("008", "南诏缘", "昆明·剑川·大理",
    OV8_ZH, OV8_EN, KPI8_ZH, KPI8_EN, SEC8_ZH, SEC8_EN, TAKE8_ZH, TAKE8_EN)

for r in all_results:
    print(r)
print(f"\nTotal: {len(all_results)} files")