#!/usr/bin/env python3
"""Generate ch005-ch006 infographic HTML for 杜甫的五城 (ZH + EN)"""
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


# ═══ CHAPTER 5: 入西域记 ═══
OV5_ZH = """从西安出发，赖瑞和沿河西走廊一路西行，穿越戈壁荒漠，直抵西域边陲。在兰州第一次见到黄河与光秃的皋兰山，在酒泉品味塞外小城的洁净与安宁，在敦煌莫高窟第十七窟前感受伯希和幽灵般的历史阴影。他在柳园的小摊上尝到吐鲁番葡萄干，在吐鲁番的交河故城与高昌故城中梦回唐代，最终抵达乌鲁木齐——在天池边吃茶叶蛋度过中秋，虽遗失了毛衣，却以半只哈密瓜自慰。这是一场穿越汉唐古道的壮游，一次从长安到西域边陲的历史回溯。"""

OV5_EN = """Departing Xi'an, Lai Ruihe journeyed westward along the Hexi Corridor, crossing the Gobi Desert to the farthest reaches of the Western Regions. In Lanzhou he saw the Yellow River for the first time and the barren Gaolan Mountain; in Jiuquan he savored the cleanliness of a frontier town; at Mogao Cave 17 in Dunhuang he sensed the lingering ghost of Pelliot. He tasted Turpan raisins at a Liuyuan street stall, dreamed of Tang dynasty glory amid the ruins of Jiaohe and Gaochang, and finally reached Urumqi—spending Mid-Autumn Festival alone by Tianchi Lake with tea eggs, consoling himself with half a Hami melon after losing his sweater. A grand journey along Han-Tang ancient roads, a historical pilgrimage from Chang'an to the edge of the Western Regions."""

TAKE5_ZH = """从西安到西域边陲，五段铁路、两千公里戈壁、四座故城遗址——大唐不在书本中，在软卧车厢的「增收」插曲里，在伯希和幽灵不舍离去的石窟中，在天池边一人吃茶叶蛋的中秋午后。"""
TAKE5_EN = """Five rail segments, 2,000 km of Gobi, four ancient city ruins. The Tang dynasty lives not in texts but in a train attendant's sly smile, in Pelliot's lingering ghost at Cave 17, and in a solitary Mid-Autumn afternoon with tea eggs by Tianchi."""

# ═══ CHAPTER 6: 五城何迢迢 ═══
OV6_ZH = """杜甫诗云「五城何迢迢？迢迢隔河水。」赖瑞和从乌鲁木齐坐了两天两夜硬座火车返回兰州，再从兰州经银川、平罗、五原一路北上呼和浩特，亲身走完了杜甫笔下的「五城」全线。沿途穿越乌兰布和沙漠，黄土高坡荒凉悲壮，阴山在夕阳下如血般橘红。在呼市午夜投宿个体户「双莲旅社」，丢失的毛衣却换来一件内蒙古东胜山羊绒。最终抵达希日穆仁大草原，在蒙古包中听雨入眠——圆了十年追寻的「五城」之梦。"""

OV6_EN = """Du Fu wrote: 'How distant the Five Cities? Distant, separated by the river.' Lai Ruihe endured 48 hours on a hard-seat train from Urumqi back to Lanzhou, then traveled north through Yinchuan, Pingluo, and Wuyuan to Hohhot—personally completing Du Fu's entire 'Five Cities' route. Along the way he crossed the Ulan Buh Desert, witnessed the tragic desolation of the Loess Plateau, and watched the Yin Mountains turn blood-orange at sunset. In Hohhot, a midnight stay at the private 'Shuanglian Inn' led to replacing his lost sweater with Inner Mongolian cashmere. Finally reaching the Xirimu Grasslands, he fell asleep to the sound of rain in a Mongolian yurt—fulfilling a decade-long dream of tracing the Five Cities."""

TAKE6_ZH = """四十八小时硬座、五百五十公里沙漠、五座被黄沙掩埋的唐城、零下二度的草原雨夜——杜甫的「五城何迢迢」不再是诗句，而是车轮下的戈壁、黄河外的落日，和蒙古包中被窝里的雨声。"""
TAKE6_EN = """Forty-eight hours in a hard seat, 550 km of desert, five Tang fortresses buried under sand, a -2°C rainy night on the steppe. Du Fu's 'How Distant the Five Cities' ceased to be verse and became Gobi beneath the wheels, sunset beyond the Yellow River, and raindrops on a Mongolian yurt."""


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


# ──────────── CHAPTER 5 DATA ────────────
KPI5_ZH = [
    {"icon":"🚂","value":"5段铁路","label":"西安→兰州→酒泉<br>柳园→吐鲁番→乌市<br>横跨甘新两省区"},
    {"icon":"🏜️","value":"2,000+km","label":"河西走廊西行<br>戈壁·长城·祁连山<br>全程硬座与硬卧交替"},
    {"icon":"🏛️","value":"4处遗址","label":"莫高窟·交河故城<br>高昌故城·嘉峪关<br>汉唐军事要塞"},
    {"icon":"🍇","value":"中秋独旅","label":"吐鲁番葡萄·哈密瓜<br>天池茶叶蛋·白兰瓜<br>遗失毛衣得半瓜自慰"},
]
KPI5_EN = [
    {"icon":"🚂","value":"5 Rail Segments","label":"Xi'an→Lanzhou→Jiuquan<br>Liuyuan→Turpan→Ürümqi<br>Across Gansu & Xinjiang"},
    {"icon":"🏜️","value":"2,000+ km","label":"Hexi Corridor Westward<br>Gobi Desert · Great Wall<br>Hard seat & hard sleeper"},
    {"icon":"🏛️","value":"4 Historic Sites","label":"Mogao Caves · Jiaohe<br>Gaochang · Jiayuguan<br>Han-Tang military outposts"},
    {"icon":"🍇","value":"Solo Mid-Autumn","label":"Turpan grapes · Hami melon<br>Tea eggs by Tianchi Lake<br>Lost sweater, found solace"},
]

SEC5_ZH = [
    {"title":"软卧票上的「增收」插曲",
     "body":"西安站购票人龙永远那么长。作者买了硬座票上车再补软卧，清秀的女列车员收了他西安到兰州的全价，却只补了天水到兰州的票——差价入袋。被发现后，她羞涩地笑道：「这样我们的收入不就可以增加一些吗？」语调那般平静自然，仿佛在说柴米油盐。她那出奇的坦率和「奥妙」的字眼，让作者没有再追究。这正是80年代末内地铁路系统的一个微缩影。"},
    {"title":"黄河初遇与河西走廊的戈壁列车",
     "body":"兰州清晨6点多，皋兰山光秃秃如秃鹰盘踞——这不正是他想象中「终南山包围西安」的场景吗？站前十几个老妇人一字排开兜售洗脸水，「来啊，洗脸啊！」成了一道独特风景。从兰州乘143次列车西行，全车爆满，他站了三个多小时才补到硬卧上铺。深夜在走道小凳上看火车转大弯，车头大灯射向戈壁滩铁轨——「最动人的时刻」。半夜过张掖，一名军人主动让出下铺。"},
    {"title":"酒泉：塞外最洁净的小镇",
     "body":"酒泉出奇地干净——马路上无一片纸屑。易君左1947年就写道「整整齐齐干干净净」。作者在酒泉宾馆客房窗口望见祁连山，「仿佛被窗子框起来」。他补了三小时「早觉」，骑车绕小镇一周，逛遍东南西北四家商店补充旅行用品，笑称如花木兰「东市买骏马，西市买鞍鞯」。傍晚在宾馆餐厅十元包餐四菜一汤，「吃得我非常满意」。"},
    {"title":"敦煌第十七窟：伯希和的幽灵",
     "body":"从酒泉乘豪华空调旅游车经四百公里戈壁至敦煌。作者最想看的并非壁画，而是第十七窟——斯坦因与伯希和偷窃经文的地方。洞室很小、很低矮、不透光。他见过伯希和当年在里头点蜡烛工作几天几夜的照片。「一直到离开，我仿佛还可以见到，伯希和的幽灵，还点着蜡烛，在那洞窟里『工作』，依依不舍离去的样子。这意象恐怕也将永远玷在敦煌的历史上，洗不净了。」"},
    {"title":"天池中秋：遗失毛衣的慰藉",
     "body":"吐鲁番→乌鲁木齐段改乘长途汽车，半路天山雪峰「像浮在戈壁上」。到乌市发现毛衣被偷，垂头丧气时偶遇路边五毛钱半边哈密瓜——「又脆又甜又多汁，遗失毛衣弄坏的心情这才好转」。恰逢中秋，餐厅人手不足，他回客房吃瓜当晚饭。次日乘班车游天池，「坐在天池边，吃茶叶蛋，看了一整个下午的碧蓝湖水。」"},
]
SEC5_EN = [
    {"title":"The Soft-Sleeper 'Income Supplement'",
     "body":"At Xi'an station, the author bought a hard-seat ticket and boarded a soft-sleeper car, paying full fare Xi'an to Lanzhou. The demure female attendant gave him a ticket from Tianshui only, pocketing the difference. When discovered, she smiled shyly: 'This way our income can increase a little, right?' Her disarming frankness and calm tone, as if discussing household groceries, left him unable to pursue the matter. A microcosm of China's railway system in the late 1980s."},
    {"title":"First Sight of the Yellow River & Gobi Express",
     "body":"At 6 AM in Lanzhou, barren Gaolan Mountain loomed like a vulture, exactly his imagined scene of 'Zhongnan Mountains enclosing Xi'an.' Elderly women lined up selling wash water: 'Come, wash your face!' He boarded packed Train 143 westward, stood three hours before securing a top hard-sleeper berth. In the dead of night, watching the train round great bends, the headlight sweeping Gobi rails: 'the most moving moment.' Past Zhangye, a soldier quietly traded his lower berth."},
    {"title":"Jiuquan: The Cleanest Town Beyond the Wall",
     "body":"Jiuquan was astonishingly clean, not a scrap of litter. Yi Junzuo had noted in 1947 it was 'sparkling clean and tidy.' From his hotel window, Qilian Mountain 'seemed framed like a painting.' After a three-hour morning nap, he cycled around the tiny town, visiting shops north, south, east, and west for supplies, laughingly comparing himself to Hua Mulan. That evening, a 10-yuan set meal of four dishes and soup left him 'utterly satisfied.'"},
    {"title":"Cave 17 at Dunhuang: Pelliot's Ghost",
     "body":"Traveling 400 km of Gobi from Jiuquan, the author reached Dunhuang. What he most wanted to see was not the murals but Cave 17, where Stein and Pelliot plundered manuscripts. The chamber was tiny, low-ceilinged, lightless. He had seen the photo of Pelliot working inside by candlelight for days. As he left, he could still almost see Pelliot's ghost, candle in hand, still working in that cave, reluctant to depart. This image will forever stain Dunhuang's history, never to be cleansed."},
    {"title":"Mid-Autumn at Tianchi: Solace After Loss",
     "body":"He took a bus to Urumqi: Tianshan's snowy peaks 'floated on the Gobi.' Upon arrival, his sweater was stolen. Dejected, he stumbled upon half a Hami melon for 50 cents: 'so crisp, sweet, and juicy that my ruined mood finally lifted.' It was Mid-Autumn Festival; he ate melon for dinner alone. Next day, a bus to Tianchi: 'I sat by the lake, ate tea eggs, and watched the aquamarine waters for an entire afternoon.'"},
]

# ──────────── CHAPTER 6 DATA ────────────
KPI6_ZH = [
    {"icon":"🚂","value":"48小时硬座","label":"乌市→兰州2,000km<br>昼夜不停·三次播音<br>推销卧铺无人问津"},
    {"icon":"🏯","value":"5座唐城","label":"丰安·定远·西/中/东<br>三受降城·韩公筑<br>今已尽掩黄沙下"},
    {"icon":"🐑","value":"零下2°C","label":"希日穆仁草原·中秋后<br>住蒙古包·手扒羊肉<br>山羊绒御寒"},
    {"icon":"🐪","value":"550km沙漠","label":"乌兰布和沙漠横穿<br>黄河大河套·阴山<br>「除了风和沙，什么都没有」"},
]
KPI6_EN = [
    {"icon":"🚂","value":"48-Hour Hard Seat","label":"Urumqi→Lanzhou 2,000 km<br>Two days two nights nonstop<br>Empty sleepers announced thrice"},
    {"icon":"🏯","value":"5 Tang Fortresses","label":"Feng'an · Dingyuan · Three<br>Shouxiang Forts by Han Gong<br>Now buried beneath the sands"},
    {"icon":"🐑","value":"-2°C on the Steppe","label":"Xirimu Grasslands<br>Mongolian yurt · hand-grabbed<br>mutton · cashmere warmth"},
    {"icon":"🐪","value":"550 km Desert","label":"Ulan Buh Desert crossing<br>Yellow River loop · Yin Mtns<br>'Nothing but wind and sand'"},
]

SEC6_ZH = [
    {"title":"两千公里硬座极限挑战",
     "body":"从乌鲁木齐回兰州，软卧硬卧全无。作者决心学邻座初中毕业的少年们——「就在硬座上度过两天两夜」。少年们打开草席铺在硬座底下，钻入睡觉，「连座位底下这么小的空间都能充分利用」。夜里列车播音员一再推销空卧铺，他一点也不动心。第二夜「更能耐了」，甚至睡得也更少——「经过这一回两千公里长途奔驰后，我想以后再也没有什么更艰苦的火车旅程，可以难倒我了。」"},
    {"title":"黄土高坡：悲壮的荒凉",
     "body":"44次列车从兰州开出，不到半小时，「一座座的黄土高坡就在窗外隆起，像变形的黄色怪兽」。一头驴子被绑在窑洞前木柱上暴晒，「一动也不动，在一大片黄泥色的背景下，沉默地站着，仿佛一座雕像，站在那里已经有一千多年了」。隔了许久许久，每当想起黄土高坡，作者都会不期然想起这头驴子，「在那年秋天的太阳底下暴晒」。这是他见过最悲壮的黄土地。"},
    {"title":"从丰安到东受降城：杜诗中的五城",
     "body":"下午3点列车到中卫——杜甫「五城」的起点。唐初五千军马在此筑丰安军城，遗址今已掩埋黄沙中。平罗是定远军城，韩公张仁愿趁突厥西征，「乘虚夺取漠南之地，于河北筑三受降城」——西城（五原北）、中城（包头北）、东城（呼市北），各距四百里，六十日内建成。从此突厥再不能越过阴山放牧。但如今，三城「早已被黄沙掩埋了，连遗址都找不到了。」"},
    {"title":"双莲旅社与内蒙古山羊绒",
     "body":"午夜到呼市，年轻女子提蜡烛领路至小巷深处的个体户「双莲旅社」——民居客房三张铁床、墙上明星海报。丢失毛衣后，中旅社女同志推荐内蒙古山羊绒：「茄士咩」。一摸料子柔柔软软，「无限温暖，我舍不得脱下了」。四百六十七元——比玩一趟草原还贵，但「却得到了一件内蒙古产的山羊绒毛衣」。后来伴他度过好几个香港寒冬。"},
    {"title":"草原落日与雨夜蒙古包",
     "body":"通往草原的路就是当年昭君出塞的路。大青山像「一个一个的大馒头堆在那里」。九月中草原冷冷清清，一人独享六人蒙古包。吃手扒羊肉喝宁城老窖，牧民家尝奶皮子「甘甘的，风味绝佳」。草原落日是「一大片罕见的橘红色，像什么人把浓浓的油彩打翻了」。夜里零下二度，穿山羊绒入眠。半夜下起雨，他「静静地躺在温暖的被窝里，听了一会儿雨声和风声，又沉沉地睡去了，睡在祖国的大地上。」"},
]
SEC6_EN = [
    {"title":"2,000 km Hard Seat: The Ultimate Test",
     "body":"Returning Urumqi to Lanzhou, no sleepers available. Determined to emulate the young schoolboys beside him, he resolved to spend two days and two nights in a hard seat. The boys spread straw mats beneath the seats and crawled in to sleep, making full use of every inch of space. When the announcer repeatedly advertised empty sleepers, he felt no temptation. By the second night he was even tougher. After this 2,000 km marathon, he thought nothing could ever intimidate him on a train again."},
    {"title":"Loess Plateau: Tragic Grandeur",
     "body":"Within half an hour from Lanzhou, loess plateaus rose outside the window like deformed yellow monsters. A donkey, tethered to a pole before a cave dwelling, stood motionless under blazing sun: against the yellow earth, silent as a statue, as if it had stood there for over a thousand years. Long afterward, whenever he recalled the loess plateau, he would think of that donkey baking in that autumn sun. The most majestic desolation he had ever seen."},
    {"title":"Du Fu's Five Fortresses: From Feng'an Eastward",
     "body":"The train reached Zhongwei at 3 PM, the starting point of Du Fu's Five Fortresses. In early Tang, 5,000 cavalry built Feng'an Fort here, now buried under sand. At Pingluo stood Dingyuan Fort. General Han Gong Zhang Renyuan, seizing the moment while the Turks campaigned westward, took the desert south of the Yellow River and built Three Shouxiang Forts, west, center, east, each 400 li apart, completed in sixty days. The Turks could no longer cross the Yin Mountains to graze. But today, all three have long been buried by sand, their ruins untraceable."},
    {"title":"Shuanglian Inn & Inner Mongolian Cashmere",
     "body":"Arriving in Hohhot at midnight, a young woman led him by candlelight through dark alleys to the privately run Shuanglian Inn: a converted home with three iron beds and celebrity posters on the wall. After losing his sweater, a CITS lady recommended Inner Mongolian cashmere. Feeling the fabric: infinitely warm, he could not bear to take it off. 467 yuan, more than the grassland trip itself, but he had gained a cashmere sweater from Inner Mongolia that warmed him through many Hong Kong winters."},
    {"title":"Sunset on the Steppe & A Rainy Night in the Yurt",
     "body":"The road to the grasslands was the very path Wang Zhaojun took into exile. Daqing Mountain looked like giant steamed buns piled together. In mid-September the steppe was deserted: he had a six-person yurt to himself. Ate hand-grabbed mutton with Ningcheng liquor, tasted milk skin at a herder's home, sweet and exquisitely flavored. The sunset was a rare expanse of orange-red, as if someone had overturned thick oil paints. At minus 2 degrees Celsius that night, wrapped in cashmere, rain pattered on the yurt: he lay quietly in his warm bed, listened to rain and wind, then sank into deep sleep, sleeping upon the earth of the motherland."},
]


all_results = []
all_results += build_ch("005", "入西域记", "兰州·酒泉·敦煌·柳园·吐鲁番·乌鲁木齐",
    OV5_ZH, OV5_EN, KPI5_ZH, KPI5_EN, SEC5_ZH, SEC5_EN, TAKE5_ZH, TAKE5_EN)
all_results += build_ch("006", "五城何迢迢", "银川·平罗·五原·呼和浩特·武川·希日穆仁",
    OV6_ZH, OV6_EN, KPI6_ZH, KPI6_EN, SEC6_ZH, SEC6_EN, TAKE6_ZH, TAKE6_EN)

for r in all_results:
    print(r)
print(f"\nTotal: {len(all_results)} files")