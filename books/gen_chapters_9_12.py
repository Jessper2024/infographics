#!/usr/bin/env python3
"""Generate infographic HTML files for chapters 9-12 of 杜甫的五城"""
import os

os.chdir(os.path.dirname(os.path.abspath(__file__)))

def zh_page(ch_num, ch_title, subtitle, overview, kpis, sections, takeaway, footer_title):
    kpi_html = ""
    colors = ['c01','c02','c03','c04']
    for i, (icon, val, label) in enumerate(kpis):
        kpi_html += f'  <div class="kpi-card {colors[i]}">\n    <div class="kpi-icon">{icon}</div>\n    <div class="kpi-value">{val}</div>\n    <div class="kpi-label">{label}</div>\n  </div>\n'

    sec_colors = ['c01','c02','c03','c04','c05']
    sec_html = ""
    for i, (sec_title, sec_body) in enumerate(sections):
        sec_html += f'<div class="section {sec_colors[i]}">\n  <div class="section-title"><span class="num">{i+1:02d}</span>{sec_title}</div>\n  <div class="section-body">{sec_body}</div>\n</div>\n'

    return f'''<!DOCTYPE html>
<html lang="zh-CN">
<head>
<meta charset="UTF-8">
<meta name="viewport" content="width=device-width,initial-scale=1.0">
<title>杜甫的五城 · 第{ch_num}章「{ch_title}」</title>
<style>
    *{{margin:0;padding:0;box-sizing:border-box}}
    @font-face{{font-family:'FZXPYZS';src:url('../方正屏显雅宋简体.TTF') format('truetype')}}
    body{{background:#f5f1eb;font-family:'FZXPYZS','PingFang SC','Noto Serif SC','STSong',Georgia,serif;color:#2d2d2d;line-height:1.8;display:flex;justify-content:center;align-items:flex-start;min-height:100vh;padding:40px 16px 60px}}
    .container{{max-width:880px;width:100%}}
    .back-catalog{{display:inline-block;font-size:13px;color:#4f46e5;text-decoration:none;margin-bottom:12px;transition:color .15s}}
    .back-catalog:hover{{color:#dc2626}}
    .lang-switch{{float:right;display:inline-block;font-size:13px;color:#4f46e5;text-decoration:none;border:1px solid #4f46e5;border-radius:6px;padding:4px 14px;transition:all .15s}}
    .lang-switch:hover{{background:#4f46e5;color:#fff}}
    h1{{font-family:'FZXPYZS','PingFang SC',serif;font-size:26px;color:#1a1a1a;margin-top:20px;margin-bottom:6px;letter-spacing:.03em;line-height:1.4}}
    .subtitle{{font-size:15px;color:#888;margin-bottom:20px;letter-spacing:.05em}}
    .divider{{width:60px;height:3px;background:linear-gradient(90deg,#dc2626,#ea580c,#ca8a04,#4f46e5,#db2777);border-radius:2px;margin:20px 0 28px}}
    .overview{{background:#eef2ff;border-left:4px solid #4f46e5;border-radius:10px;padding:20px 24px;margin-bottom:32px;font-size:15px;color:#444;line-height:1.9}}
    .kpi-row{{display:flex;flex-wrap:wrap;gap:12px;margin-bottom:36px}}
    .kpi-card{{flex:1;min-width:140px;background:#fff;border-radius:10px;padding:18px 16px;text-align:center;box-shadow:0 1px 4px rgba(0,0,0,.06)}}
    .kpi-card.c01{{border-top:3px solid #dc2626}}
    .kpi-card.c02{{border-top:3px solid #ea580c}}
    .kpi-card.c03{{border-top:3px solid #ca8a04}}
    .kpi-card.c04{{border-top:3px solid #4f46e5}}
    .kpi-icon{{font-size:28px;margin-bottom:6px}}
    .kpi-value{{font-size:18px;font-weight:700;color:#1a1a1a;margin-bottom:4px}}
    .kpi-label{{font-size:12px;color:#888;line-height:1.6}}
    .section{{counter-increment:sec;background:#fff;border-radius:12px;padding:24px 28px;margin-bottom:20px;box-shadow:0 1px 4px rgba(0,0,0,.05)}}
    .section.c01{{border-left:4px solid #dc2626}}
    .section.c02{{border-left:4px solid #ea580c}}
    .section.c03{{border-left:4px solid #ca8a04}}
    .section.c04{{border-left:4px solid #4f46e5}}
    .section.c05{{border-left:4px solid #db2777}}
    .section-title{{font-size:17px;font-weight:700;color:#1a1a1a;margin-bottom:10px;display:flex;align-items:center;gap:10px}}
    .section-title .num{{display:inline-flex;align-items:center;justify-content:center;width:28px;height:28px;border-radius:50%;color:#fff;font-size:13px;font-weight:700;flex-shrink:0}}
    .section.c01 .num{{background:#dc2626}}
    .section.c02 .num{{background:#ea580c}}
    .section.c03 .num{{background:#ca8a04}}
    .section.c04 .num{{background:#4f46e5}}
    .section.c05 .num{{background:#db2777}}
    .section-body{{font-size:14px;color:#555;line-height:1.9}}
    .takeaway{{background:#fff;border-left:4px solid #dc2626;border-radius:10px;padding:20px 24px;margin-top:32px;margin-bottom:36px;font-size:15px;color:#1a1a1a;font-weight:600;line-height:1.8}}
    .takeaway-label{{display:inline-block;background:#dc2626;color:#fff;font-size:11px;padding:3px 10px;border-radius:4px;margin-bottom:10px;letter-spacing:.05em}}
    .footer{{text-align:center;font-size:12px;color:#bbb;padding-top:20px;border-top:1px solid #e8e0d5;margin-top:12px}}
    .footer a{{color:#bbb;text-decoration:none}}
    @media(max-width:640px){{
      .container{{padding:0 12px}}
      h1{{font-size:22px}}
      .kpi-card{{min-width:120px}}
      .section{{padding:18px 20px}}
    }}
</style>
</head>
<body>
<div class="container">

<a class="back-catalog" href="杜甫的五城-catalog.html">← 返回章节目录</a>
<a class="lang-switch" target="_blank" href="杜甫的五城-ch{ch_num}-info-en.html">EN</a>

<h1>杜甫的五城 · 第{ch_num}章「{ch_title}」</h1>
<div class="subtitle">{subtitle}</div>
<div class="divider"></div>

<div class="overview">
  <p>{overview}</p>
</div>

<div class="kpi-row">
{kpi_html}</div>
{sec_html}
<div class="takeaway">
  <div class="takeaway-label">💡 核心启示</div>
  {takeaway}
</div>

<div class="footer">
  杜甫的五城 · 第{ch_num}章「{footer_title}」 | 赖瑞和 著 · 一位唐史学者的寻踪壮游
</div>

</div>
</body>
</html>'''

def en_page(ch_num, ch_title, subtitle, overview, kpis, sections, takeaway, footer_title):
    kpi_html = ""
    colors = ['c01','c02','c03','c04']
    for i, (icon, val, label) in enumerate(kpis):
        kpi_html += f'  <div class="kpi-card {colors[i]}">\n    <div class="kpi-icon">{icon}</div>\n    <div class="kpi-value">{val}</div>\n    <div class="kpi-label">{label}</div>\n  </div>\n'

    sec_colors = ['c01','c02','c03','c04','c05']
    sec_html = ""
    for i, (sec_title, sec_body) in enumerate(sections):
        sec_html += f'<div class="section {sec_colors[i]}">\n  <div class="section-title"><span class="num">{i+1:02d}</span>{sec_title}</div>\n  <div class="section-body">{sec_body}</div>\n</div>\n'

    return f'''<!DOCTYPE html>
<html lang="en">
<head>
<meta charset="UTF-8">
<meta name="viewport" content="width=device-width,initial-scale=1.0">
<title>杜甫的五城 · 第{ch_num}章「{ch_title}」</title>
<style>
    *{{margin:0;padding:0;box-sizing:border-box}}
    @font-face{{font-family:'FZXPYZS';src:url('../方正屏显雅宋简体.TTF') format('truetype')}}
    body{{background:#f5f1eb;font-family:'FZXPYZS','PingFang SC','Noto Serif SC','STSong',Georgia,serif;color:#2d2d2d;line-height:1.8;display:flex;justify-content:center;align-items:flex-start;min-height:100vh;padding:40px 16px 60px}}
    .container{{max-width:880px;width:100%}}
    .back-catalog{{display:inline-block;font-size:13px;color:#4f46e5;text-decoration:none;margin-bottom:12px;transition:color .15s}}
    .back-catalog:hover{{color:#dc2626}}
    .lang-switch{{float:right;display:inline-block;font-size:13px;color:#4f46e5;text-decoration:none;border:1px solid #4f46e5;border-radius:6px;padding:4px 14px;transition:all .15s}}
    .lang-switch:hover{{background:#4f46e5;color:#fff}}
    h1{{font-family:'FZXPYZS','PingFang SC',serif;font-size:26px;color:#1a1a1a;margin-top:20px;margin-bottom:6px;letter-spacing:.03em;line-height:1.4}}
    .subtitle{{font-size:15px;color:#888;margin-bottom:20px;letter-spacing:.05em}}
    .divider{{width:60px;height:3px;background:linear-gradient(90deg,#dc2626,#ea580c,#ca8a04,#4f46e5,#db2777);border-radius:2px;margin:20px 0 28px}}
    .overview{{background:#eef2ff;border-left:4px solid #4f46e5;border-radius:10px;padding:20px 24px;margin-bottom:32px;font-size:15px;color:#444;line-height:1.9}}
    .kpi-row{{display:flex;flex-wrap:wrap;gap:12px;margin-bottom:36px}}
    .kpi-card{{flex:1;min-width:140px;background:#fff;border-radius:10px;padding:18px 16px;text-align:center;box-shadow:0 1px 4px rgba(0,0,0,.06)}}
    .kpi-card.c01{{border-top:3px solid #dc2626}}
    .kpi-card.c02{{border-top:3px solid #ea580c}}
    .kpi-card.c03{{border-top:3px solid #ca8a04}}
    .kpi-card.c04{{border-top:3px solid #4f46e5}}
    .kpi-icon{{font-size:28px;margin-bottom:6px}}
    .kpi-value{{font-size:18px;font-weight:700;color:#1a1a1a;margin-bottom:4px}}
    .kpi-label{{font-size:12px;color:#888;line-height:1.6}}
    .section{{counter-increment:sec;background:#fff;border-radius:12px;padding:24px 28px;margin-bottom:20px;box-shadow:0 1px 4px rgba(0,0,0,.05)}}
    .section.c01{{border-left:4px solid #dc2626}}
    .section.c02{{border-left:4px solid #ea580c}}
    .section.c03{{border-left:4px solid #ca8a04}}
    .section.c04{{border-left:4px solid #4f46e5}}
    .section.c05{{border-left:4px solid #db2777}}
    .section-title{{font-size:17px;font-weight:700;color:#1a1a1a;margin-bottom:10px;display:flex;align-items:center;gap:10px}}
    .section-title .num{{display:inline-flex;align-items:center;justify-content:center;width:28px;height:28px;border-radius:50%;color:#fff;font-size:13px;font-weight:700;flex-shrink:0}}
    .section.c01 .num{{background:#dc2626}}
    .section.c02 .num{{background:#ea580c}}
    .section.c03 .num{{background:#ca8a04}}
    .section.c04 .num{{background:#4f46e5}}
    .section.c05 .num{{background:#db2777}}
    .section-body{{font-size:14px;color:#555;line-height:1.9}}
    .takeaway{{background:#fff;border-left:4px solid #dc2626;border-radius:10px;padding:20px 24px;margin-top:32px;margin-bottom:36px;font-size:15px;color:#1a1a1a;font-weight:600;line-height:1.8}}
    .takeaway-label{{display:inline-block;background:#dc2626;color:#fff;font-size:11px;padding:3px 10px;border-radius:4px;margin-bottom:10px;letter-spacing:.05em}}
    .footer{{text-align:center;font-size:12px;color:#bbb;padding-top:20px;border-top:1px solid #e8e0d5;margin-top:12px}}
    .footer a{{color:#bbb;text-decoration:none}}
    @media(max-width:640px){{
      .container{{padding:0 12px}}
      h1{{font-size:22px}}
      .kpi-card{{min-width:120px}}
      .section{{padding:18px 20px}}
    }}
</style>
</head>
<body>
<div class="container">

<a class="back-catalog" href="杜甫的五城-catalog.html">← Back to Chapter Catalog</a>
<a class="lang-switch" target="_blank" href="杜甫的五城-ch{ch_num}-info-zh.html">中文</a>

<h1>杜甫的五城 · 第{ch_num}章「{ch_title}」</h1>
<div class="subtitle">{subtitle}</div>
<div class="divider"></div>

<div class="overview">
  <p>{overview}</p>
</div>

<div class="kpi-row">
{kpi_html}</div>
{sec_html}
<div class="takeaway">
  <div class="takeaway-label">💡 KEY INSIGHT</div>
  {takeaway}
</div>

<div class="footer">
  杜甫的五城 · 第{ch_num}章「{footer_title}」 | By Lai Ruihe · A Tang Historian's Grand Tour
</div>

</div>
</body>
</html>'''


# =============== CHAPTER 9: 入蜀下三峡 ===============
ch09_zh = zh_page("9", "入蜀下三峡",
    "丽江 · 重庆 · 长江三峡",
    "游过剑川石钟山石窟后，赖瑞和从丽江古城出发，开始了他「四入四川」计划中的第一次入蜀——从南面经攀枝花入川。在丽江，他见到「处处流水、处处杨柳」，女子在溪边浣衣，仿佛北宋山水画。从成都出发，品赖家汤圆、钟家水饺，看大足石刻，最终抵达重庆朝天门码头。在江轮上连续两天两夜顺长江而下，穿越瞿塘峡、巫峡、西陵峡，感受那「悲欣交集」的漂泊心境——如弘一大师遗墨般，最甜美的时刻又有心如刀割的痛楚。",
    [
        ("🌊", "4次入川", "东·南·西·北<br>四方向入蜀计划"),
        ("🚢", "2天2夜", "江渝号长江漂流<br>瞿塘·巫峡·西陵峡"),
        ("🏘️", "5座古城", "丽江·成都·重庆<br>乐山·大足石刻"),
        ("🍶", "泸州大曲", "船上独饮看山水<br>微醉中入抒情之境"),
    ],
    [
        ("丽江：时间中止的桃花源", "从剑川乘长途汽车到丽江，古城里「处处流水，处处杨柳依依，还有女子在溪边浣衣，令人几疑是北宋的一幅山水画摆在那儿」。连居民衣着似乎都停留在宋代，「外人走进去，仿佛走进了桃花源，时间都中止了」。离开丽江后经攀枝花入川，先到峨眉山和乐山大佛游玩两天。"),
        ("成都：八百年后的另一种入蜀", "八百多年前陆游从绍兴沿长江逆流而上，我走的却是另一条罕见的路线——四入四川。在成都品尝赖家汤圆和钟家水饺，游杜甫草堂和武侯祠，到青城山和都江堰，再去永川寻访大足石刻——北山石窟里独自待了一个下午。深夜抵达重庆，准备从朝天门下三峡。"),
        ("重庆朝天门：小李与码头生存术", "在重庆码头附近偶遇「小李」——一个斯文的年轻人，帮我找到换票处、传授乘船「要诀」：开闸时走左边小门而非右边大门，「不必跟他们挤，反而会比他们早一点登上二等舱」。次日清晨他如约来会仙楼接我，陪我吃一碗地道担担面后上船。这个在路边逗弄小女儿的年轻人，「看着那种做爸爸的满足样子」，让我想起自己的小女儿。"),
        ("江渝号：中国社会的横切面", "江轮不设一等舱（因有「高人一等」含义），最好的舱房谦卑地称「二等」。船上可见各阶层：高级干部有人服侍、旅人如我、三等四等大统舱、农人自带草席在走道上打地铺。外国游客坐「豪华游轮」如「隆中」「长城」号，我却庆幸上了这艘普通江轮，「要不然就见不到国内的众生相了」。"),
        ("悲欣交集：长江上的抒情漂泊", "一连两天两夜，搬椅子坐在舱房外走道上，看山看水，偶尔翻书却「总觉得不是看书的心情，不如看山看水」。酒兴发时打开泸州大曲，微微醉了才回房。仿佛进入一种十分抒情的状态，「好像听肖邦，很中国，很诗意，很悲伤，又很幸福。」像弘一大师遗墨「悲欣交集」——最难忘的便是这种奇特的心情。航行经神女峰，穿过三峡，第二天午夜抵达沙市（古代荆州）。"),
    ],
    "四入四川的宏大计划、丽江古城的桃花源时光、偶遇码头上的「小李」、江轮上的众生相、长江上两天两夜的抒情漂泊——旅程中最珍贵的不是三峡的壮丽，而是那种「仿佛天地间一个永恒的旅者，航经古典的、水绿色的中国内陆」的悠长感。",
    "入蜀下三峡")

ch09_en = en_page("9", "Entering Shu, Down the Three Gorges",
    "Lijiang · Chongqing · Yangtze Three Gorges",
    "After visiting the Shizhongshan Grottoes in Jianchuan, Lai set out from Lijiang's ancient town to begin his 'Four-Entry-Into-Shu' plan—first entering Sichuan from the south via Panzhihua. In Lijiang, he found 'flowing water and willows everywhere,' women washing clothes by streams, a Northern Song landscape painting come to life. From Chengdu, he tasted Lai-family rice balls and Zhong-family dumplings, visited Dazu rock carvings, and finally reached Chaotianmen Wharf in Chongqing. For two days and two nights aboard the 'Jiangyu,' he drifted down the Yangtze through Qutang, Wu, and Xiling gorges, immersed in a state of 'sorrow and joy mingled'—like Master Hongyi's final calligraphy: the sweetest moments laced with heart-piercing pain.",
    [
        ("🌊", "4 Entries into Shu", "East·South·West·North<br>Grand Shu traversal plan"),
        ("🚢", "2 Days 2 Nights", "Aboard the Jiangyu<br>Qutang·Wu·Xiling Gorges"),
        ("🏘️", "5 Ancient Towns", "Lijiang·Chengdu·Chongqing<br>Leshan·Dazu Rock Carvings"),
        ("🍶", "Luzhou Daqu", "Drinking alone on deck<br>Drifting into lyrical reverie"),
    ],
    [
        ("Lijiang: A Peach-Blossom Spring Where Time Stops", "From Jianchuan by long-distance bus to Lijiang, the ancient town had 'flowing water and willows everywhere, and women washing clothes by streams—you would almost believe a Northern Song landscape painting was placed right there.' Even residents' clothing seemed stuck in the Song dynasty. 'Walking in, it was like entering the Peach-Blossom Spring; time had come to a halt.' Leaving Lijiang, he entered Sichuan via Panzhihua, first visiting Mount Emei and the Leshan Giant Buddha."),
        ("Chengdu: Another Way into Shu, 800 Years Later", "Eight centuries ago, Lu You traveled up the Yangtze from Shaoxing. Lai chose a different, rarer route: entering Shu from four directions. In Chengdu: Lai-family rice balls, Zhong-family dumplings, Du Fu's Thatched Cottage, the Wuhou Shrine, Mount Qingcheng, Dujiangyan. Then to Yongchuan for the Dazu rock carvings—spending an entire afternoon alone at the Beishan grottoes. Arriving in Chongqing late at night, ready to descend the Three Gorges from Chaotianmen."),
        ("Chaotianmen Wharf: Xiao Li and the Art of Riverboat Boarding", "Near Chongqing's wharf, he met 'Xiao Li'—a bookish young man who helped him find the ticket exchange office and taught riverboat strategy: when the gates open, take the left small door, not the right main entrance. 'Don't squeeze with them; you'll actually board the second-class cabin before they do.' Next morning Xiao Li arrived as promised, accompanied him through Chongqing's stepped streets, shared a bowl of authentic dandan noodles, then boarded. Watching Xiao Li play with his little daughter by the roadside, 'seeing that satisfied look of a father,' Lai recalled his own daughter."),
        ("The Jiangyu: A Cross-Section of Chinese Society", "No first-class cabins (too 'superior' in implication); the best cabins were humbly called 'second class.' Every social stratum aboard: senior cadres with attendants, travelers like Lai, third- and fourth-class berths, farmers sleeping on straw mats in corridors. Foreign tourists took 'luxury cruisers' like 'Longzhong' or 'Great Wall,' but Lai was glad he chose this ordinary vessel: 'otherwise I would never have seen the full panorama of life in China.'"),
        ("Sorrow and Joy Mingled: Lyrical Drifting on the Yangtze", "For two days and two nights, he placed a chair in the corridor outside his cabin, watching mountains and water, occasionally leafing through a book but 'never in the mood for reading—better to watch mountains, watch water.' When the wine mood struck, he opened his bottle of Luzhou Daqu, returning to the cabin only when slightly drunk. He entered a profoundly lyrical state: 'like listening to Chopin—very Chinese, very poetic, very sad, and very happy.' Like Master Hongyi's final calligraphy 'Sorrow and Joy Mingled'—this strange mood was the journey's most unforgettable gift. Passing Shennü Peak, through the Three Gorges, arriving at Shashi (ancient Jingzhou) the second midnight."),
    ],
    "A grand four-direction plan to enter Shu, a Peach-Blossom Spring in Lijiang, a chance encounter with Xiao Li at the wharf, the full spectrum of Chinese society aboard one riverboat, and two days and nights of lyrical drifting down the Yangtze—the journey's greatest treasure was not the grandeur of the Three Gorges, but the sensation of being 'an eternal traveler between heaven and earth, sailing through a classical, water-green interior China.'",
    "Entering Shu, Down the Three Gorges")

# =============== CHAPTER 10: 湘西行 ===============
ch010_zh = zh_page("10", "湘西行",
    "常德 · 桃源 · 张家界 · 王村 · 凤凰",
    "十三岁时在南方小城的图书馆偶然发现沈从文，从此日夜沉迷于《边城》《长河》《从文自传》。多年后赖瑞和从长江沙市下船，经常德、桃源，穿越湘西，一路追寻沈从文的足迹。在桃源欲乘湘船逆沅江漂流未果，转道张家界在细雨中登山，乘船穿酉江抵王村（芙蓉镇），游猛洞河感受「翡冷翠」般的绿意，最后抵达凤凰——终于坐在沈从文故居的书房窗前，走到沱江边看妇女捣衣，听小学生朗朗读书声。",
    [
        ("📚", "13岁初识沈从文", "边城·长河·从文自传<br>日夜不分地阅读"),
        ("🏞️", "6处湘西地标", "常德·桃源·张家界<br>王村·猛洞河·凤凰"),
        ("🚢", "3种水路交通", "沅江湘船·酉江小船<br>猛洞河游船"),
        ("🌿", "翡翠世界", "碧绿酉江水<br>「翠翠」般的湘西山水"),
    ],
    [
        ("常德与桃源：追寻沈从文的「长河」", "在沙市下船后游荆州古城，随即乘车到湖南常德——沈从文常说的「我在常德」之地。黄昏时分独自走到沅江边，「站立了良久良久，直到天黑了」。第二天到桃源，走到沅江边小码头打听好湘船，准备「逆沅江而上，一直漂流到湘西的辰溪」。可惜连日豪雨致水位暴涨，所有船只停航——「是命也夫？是命也夫？」——与沈从文的「长河」只能远望。"),
        ("桃花源与雨中的张家界", "桃花源幽深沉静，竹林、桃花树、小桥流水，管理员说「明年四月春天花开的时候再来」。在细雨中登张家界，土家族导游淳朴忠厚，「没有感染到汉族导游常有的那种诈」，两人相处极为愉快。下山后导游目送他上了去大庸北火车站的班车才离去。"),
        ("罗依溪与王村：碧绿酉江上的芙蓉镇", "从大庸北乘火车到「罗依溪」——「这地名真别致，像译音的外国地名，但又有一种中国的格调」。站台极短，旅客跨过铁轨径直走到对面小码头。船行酉江上，「江水之碧绿，绿得叫人有点晕眩」。黄昏到王村（芙蓉镇），青石板路从码头盘伸到村后，古老民居「散发着残旧的年岁余光」。"),
        ("猛洞河：写给「翠翠」的绿色情书", "乘船游猛洞河——「碧绿的水，苍翠的山，真是个翡翠的世界，完全没有工业的污染」。想起「翡冷翠」这个地名，仿佛也能描述这里的山水。终于明白为什么沈从文把女主角唤作「翠翠」——「因为她显然便活在一个全然绿色的世间啊。湘西的山和水，原来就是那么'翠翠'的。」还见到了全国重点文物溪州铜柱——北宋楚王和湘西土司罢兵休战的盟约，刻在铜上而非石碑，珍贵无比。"),
        ("凤凰：沈从文故居的寂静时光", "从吉首乘老旧长途汽车穿越尘土飞扬的阡陌，苗族妇女背着竹箩列队赶集。抵达凤凰后先吃了一碗绿色的面条——「我跑遍中国大地，也只在凤凰见过这么一次」。寻访沈从文故居：小庭院、四厢房、采光极好的书房——「然而沈老生前，好像从来没有一天是坐在那个明亮美丽的窗前写作的」。走到沱江边看妇女用棒槌捣衣，听小学生朗读，「那时，湘西就将远了」。"),
    ],
    "十三岁邂逅沈从文的文字，多年后亲自走入他笔下的湘西——沅江边久立至天黑、桃花源里的安静午后、碧绿酉江上的晕眩、猛洞河「翠翠」般的翡翠世界、凤凰故居窗前的沉默。年少时的痴迷化作了真实的脚步，文字里的湘西最终变成了脚下走过的每一寸山水。",
    "湘西行")

ch010_en = en_page("10", "Journey to West Hunan",
    "Changde · Taoyuan · Zhangjiajie · Wangcun · Fenghuang",
    "At thirteen, in a small southern-town library, Lai accidentally discovered Shen Congwen and became obsessed with 'Border Town,' 'Long River,' and 'Congwen's Autobiography'—reading day and night. Years later, disembarking at Shashi on the Yangtze, he traveled through Changde and Taoyuan, tracing Shen's footsteps across West Hunan. He hoped to drift upstream on the Yuan River aboard a Xiang boat but rains foiled his plans. He detoured to Zhangjiajie in drizzle, crossed the emerald You River to Wangcun (Hibiscus Town), cruised the Mengdong River through a jade-green world, and finally reached Fenghuang—sitting before the study window of Shen Congwen's former residence, watching women pound laundry by the Tuo River, listening to schoolchildren's recitations.",
    [
        ("📚", "Age 13 Discovery", "Border Town · Long River<br>Shen Congwen's writings"),
        ("🏞️", "6 West Hunan Sites", "Changde·Taoyuan·Zhangjiajie<br>Wangcun·Mengdong·Fenghuang"),
        ("🚢", "3 Water Routes", "Yuan River·You River<br>Mengdong River cruise"),
        ("🌿", "Emerald World", "Green You River waters<br>'Cuicui'-like Hunan landscape"),
    ],
    [
        ("Changde & Taoyuan: Searching for Shen's 'Long River'", "After disembarking at Shashi and touring ancient Jingzhou, Lai took a bus to Changde—the place Shen often mentioned: 'When I was in Changde...' He walked alone at dusk to the Yuan River shore, 'standing there a long, long time until it grew dark.' Next day in Taoyuan, he found a small dock and made inquiries about Xiang boats to drift upstream 'all the way to Chenxi in West Hunan.' But days of heavy rain had swollen the river; all boats were suspended—'Is this fate? Is this fate?'—Shen's 'Long River' could only be admired from afar."),
        ("Peach-Blossom Spring and Zhangjiajie in the Rain", "The Peach-Blossom Spring was deep and quiet, with bamboo groves, peach trees, small bridges, and flowing water. The caretaker said: 'Come back next April, when the spring flowers bloom.' Climbing Zhangjiajie in fine rain, a Tujia guide—still honest and simple, 'not yet infected by the slyness common among Han guides'—accompanied him agreeably. After descending, the guide watched him board the bus to Dayong North station before leaving."),
        ("Luoyixi & Wangcun: Hibiscus Town on Emerald Waters", "From Dayong North, a train to 'Luoyixi'—'what a distinctive name, like a transliterated foreign place-name yet with a Chinese cadence.' The platform was so short, travelers simply crossed the rails to a small dock opposite. Sailing the You River, 'the water was so green it made one dizzy.' At dusk, Wangcun (famous from the film 'Hibiscus Town'): a bluestone path winding from wharf to village rear, old wooden houses 'radiating the afterglow of worn years.'"),
        ("Mengdong River: A Green Love Letter to 'Cuicui'", "Cruising the Mengdong River: 'emerald water, verdant mountains—truly a jade world, entirely free of industrial pollution.' The Italian name 'Firenze' (Florence) felt apt for these landscapes, carrying 'a kind of cool greenness.' He finally understood why Shen Congwen named his heroine 'Cuicui' (Green-Green)—'because she clearly lived in an entirely green world. The mountains and waters of West Hunan are just that: green-green.' He also saw the Xizhou Bronze Pillar, a nationally protected relic: an 11th-century peace treaty between the Chu king and West Hunan tribal leaders, carved on bronze rather than stone—priceless."),
        ("Fenghuang: Silent Moments at Shen Congwen's Home", "From Jishou by decrepit long-distance bus through dusty field paths, Miao women in ethnic dress carrying bamboo baskets marching to market. In Fenghuang, he first ate a bowl of green noodles—'In all my travels across China, I have only seen this once, in Fenghuang.' Finding Shen's former residence: small courtyard, four wings, a study with lovely light—'yet in his lifetime, Shen probably never once sat writing before that bright, beautiful window.' Walking to the Tuo River watching women pound laundry with wooden clubs, hearing schoolchildren's recitations: 'By then, West Hunan was about to grow distant.'"),
    ],
    "Discovered Shen Congwen's prose at thirteen; walked into his West Hunan decades later—standing by the Yuan River until darkness, a quiet afternoon in the Peach-Blossom Spring, the dizzying green of the You River, a jade world on the Mengdong, and silence before Shen Congwen's study window. A teenage obsession transformed into real footsteps; the West Hunan of the page became the West Hunan beneath his feet.",
    "Journey to West Hunan")

# =============== CHAPTER 11: 便下襄阳向洛阳 ===============
ch011_zh = zh_page("11", "便下襄阳向洛阳",
    "贵阳 · 襄阳 · 宝丰 · 铁门",
    "游过湘西后，赖瑞和效仿杜甫「便下襄阳向洛阳」。先到贵阳目睹发大水的黄果树瀑布——「比起世界最大的尼亚加拉瀑布，真是一点也不逊色」。乘火车穿越川东二度入川，再经安康抵达襄阳。但此行真正的目的地，是襄阳以北二百多公里的河南宝丰县——寻找一通影响了他整个人生轨迹的宋代石碑。七十年代在台大偶然发现《大悲菩萨传》碑后半段，凭此获得普林斯顿大学博士入学资格；十多年后终在宝丰香山寺塔底券洞中找到石碑前半段——「我仿佛和一位失散已久的故人，偶然在天涯某一角重逢」。随后往铁门千唐志斋，面对一千多通唐代墓志，感受「一部刻在石头上的唐史」。",
    [
        ("💧", "黄果树大瀑布", "发大水后十倍壮观<br>「不逊尼亚加拉」"),
        ("📜", "1通宋碑", "《大悲菩萨传》碑<br>追寻十多年终得全貌"),
        ("🗿", "1000+唐墓志", "千唐志斋藏品<br>刻在石头上的唐史"),
        ("🚂", "4省穿行", "贵州·四川·陕西·河南<br>杜诗路线实地重走"),
    ],
    [
        ("黄果树：发大水的奇迹", "从怀化乘直快车到贵阳，正巧前几日刚下过豪雨，水位高涨，「黄果树瀑布突然变得比平时壮观十倍」。车子远远就听见万马奔腾的水声——大水夹着黄泥，如决堤般勇往下冲，激起几十丈水花和大片水雾。「这种声势，比起我见过的世界最大的尼亚加拉瀑布，真是一点也不逊色。」后来见到旅游照片上只有几条小水柱干巴巴挂着，才意识到自己遇到的是何等难得的机缘。"),
        ("效仿杜甫「下襄阳」", "从贵阳乘夜班火车二度入川，清晨抵重庆后马上转车穿越川东到陕南安康。安康火车站旅馆服务员说：「你是我们开业以来的第一位外宾。」第二天搭慢车「下襄阳」——早上十点到晚上八点，才走完三百六十八公里。杜甫当年下襄阳讲求「快」，诗节奏明快，一副猴急回家的样子；我坐在慢车上，「心情变得急躁起来了」。晚上抵襄阳，住卧龙饭店；次日游古隆中——诸葛亮耕读十年的地方。"),
        ("宝丰：万里寻碑记", "七十年代在台大外文系大四时，无意中找到北宋《大悲菩萨传》碑后半段——它是关于妙善菩萨传说最早的历史文献，却长期失踪，连专门研究的专家都未见过。凭此被推荐到普林斯顿大学读博士。「当年要不是找到这篇碑文，我的生命历程可能很不一样。」十多年来在海外漂泊，始终对前半段念念不忘。到宝丰后一出火车站就遇贵人——三轮车司机告知宋碑仍存。第二天冒大雨赶到香山寺塔底券洞——「洞里光线太暗，先伸出手去触摸碑身，凉凉的。等到瞳孔慢慢习惯微弱的光线后，才发现这正是我寻找了十多年的那通石碑。」在寂静的券洞中抄录下前半段二十几行碑文。"),
        ("铁门千唐志斋：刻在石头上的唐史", "千唐志斋收藏一千余通唐代墓志，许多墓主在正史中并无列传。这里是前国民党将领张钫的园林「蛰庐」，他将洛阳周围收集的历代碑石运来安放。十多个窑洞式收藏室和三个天井院，墙壁上密密麻麻镶嵌着墓志石碑。那天早上他是唯一的访客，「像幽灵一样从一个窑洞飘游到另一个窑洞」——「这些刻在石头上原始的墓志，真给人一种淡淡的、幽幽的、幽灵式的恐惧感，仿佛死者又重回阳间一样。」"),
        ("又一个唐代的幽灵重返阳间", "每一块墓志原本都应深埋在地下墓室里，目的不是给阳间俗人读的，而是向阴间宣扬死者功业。然而如今它们被高高镶嵌在墙上展示——「每一次见到这些墓志，我总不免在想：又一座古人的墓被盗了。又一个唐代的幽灵重返阳间了。」这些墓志既有历史文献价值，更让人直面死亡与记忆的沉重——刻在石头上的文字比纸上文章更持久，但也更令人不安。"),
    ],
    "一瀑布（黄果树发大水）、一诗（杜甫下襄阳）、一碑（《大悲菩萨传》宋碑）、一斋（千唐志斋）——这一程将自然奇观、诗歌地理、个人命运和千年石刻编织在一起。那通宋代石碑改变了他的生命轨迹，而一千多通唐代墓志则让他直面历史深处幽灵般的回响。",
    "便下襄阳向洛阳")

ch011_en = en_page("11", "Down to Xiangyang, On to Luoyang",
    "Guiyang · Xiangyang · Baofeng · Tiemen",
    "After West Hunan, Lai traced Du Fu's route 'down to Xiangyang, on to Luoyang.' First to Guiyang, where he witnessed the Huangguoshu Waterfall swollen tenfold by recent torrential rain—'no less magnificent than Niagara.' By train through eastern Sichuan (his second entry into Shu), via Ankang to Xiangyang. But the true destination lay 200 km north: Baofeng County, Henan—to find a Song-dynasty stele that had changed his entire life. In the 1970s at National Taiwan University, he had accidentally discovered the second half of the 'Biography of the Great Compassion Bodhisattva' stele, earning him admission to Princeton's doctoral program. Over a decade later, he found the first half in a vault beneath Baofeng's Xiangshan Temple pagoda—'as if reunited with a long-lost friend at the edge of the world.' Then to Tiemen's 'Hall of a Thousand Tang Epitaphs,' facing over a thousand Tang tomb inscriptions—'a Tang history carved in stone.'",
    [
        ("💧", "Huangguoshu Falls", "Swollen 10x by rain<br>'No less than Niagara'"),
        ("📜", "1 Song Stele", "Great Compassion Bodhisattva<br>Found after 10+ years"),
        ("🗿", "1000+ Epitaphs", "Thousand Tang Epitaphs Hall<br>Tang history in stone"),
        ("🚂", "4 Provinces", "Guizhou·Sichuan·Shaanxi·Henan<br>Retracing Du Fu's route"),
    ],
    [
        ("Huangguoshu: A Flood-Created Miracle", "From Huaihua by express train to Guiyang; a few days of torrential rain had swelled the river, 'Huangguoshu Waterfall suddenly became ten times more spectacular than usual.' From afar the roar of galloping horses—yellow-muddy water plunging like a breached dam, exploding into towering spray and vast mist. 'In momentum, it was no less than the world's largest Niagara Falls I had seen.' Later, seeing tourist photos of a few pitiful dry trickles, he understood what a rare moment fate had granted him."),
        ("Following Du Fu 'Down to Xiangyang'", "From Guiyang by night train—second entry into Sichuan. At dawn in Chongqing, immediately transferred, crossing eastern Sichuan to Ankang in southern Shaanxi. The Ankang station hotel clerk said: 'You are our first foreign guest since we opened.' Next day, a slow train 'down to Xiangyang'—10 a.m. to 8 p.m., covering just 368 km. Du Fu's poem was all about speed, racing home. Sitting on the slow train, 'my mood grew restless.' Arriving in Xiangyang at night: Wolong Hotel. Next morning: Ancient Longzhong—where Zhuge Liang studied and farmed for ten years."),
        ("Baofeng: The 10,000-Li Search for a Stele", "In 1979, a fourth-year student at NTU's Foreign Languages department, Lai accidentally found the latter half of the Northern Song 'Biography of the Great Compassion Bodhisattva' stele—the earliest historical document on the Miaoshan legend, long missing and unseen even by specialists. This discovery earned him a Princeton PhD recommendation. 'Had I not found that inscription, my life's course would have been entirely different.' For over a decade abroad, he never forgot the missing first half. In Baofeng, stepping off the train he immediately met a benefactor—a three-wheel taxi driver who said the Song stele still stood. Next morning in heavy rain, he rushed to the Xiangshan Temple pagoda vault—'too dark inside; I reached out first to touch the stele, cold. When my pupils adjusted to the faint light, I saw it was the very stele I had sought for over ten years.' In the silent vault, he copied the first half's twenty-odd lines."),
        ("The Hall of a Thousand Tang Epitaphs: Tang History in Stone", "The 'Hall of a Thousand Tang Epitaphs' housed over a thousand Tang tomb inscriptions, many of whose subjects had no biographies in the official histories. The site was the 'Zhelu' garden of former Nationalist general Zhang Fang, who gathered epitaphs from around Luoyang. Over ten cave-dwelling-style chambers and three courtyard wells, walls densely inlaid with square stone epitaphs. That morning, Lai was the sole visitor, 'drifting like a ghost from one cave-chamber to another'—'these original epitaphs carved in stone give one a faint, ghostly, spectral sense of dread, as if the dead had returned to the world of the living.'"),
        ("Another Tang Ghost Returns to the Sunlit World", "Every epitaph was meant to lie deep in an underground tomb chamber, their purpose not for the living to read but to proclaim the deceased's accomplishments to the underworld. Yet now they hung displayed on walls—'Every time I see these epitaphs, I cannot help thinking: Another ancient tomb has been robbed. Another Tang ghost has returned to the sunlit world.' These inscriptions are both invaluable historical documents and a confrontation with the weight of death and memory—words carved in stone outlast paper, but also unsettle more deeply."),
    ],
    "One waterfall (Huangguoshu in flood), one poem (Du Fu's 'Down to Xiangyang'), one stele (the Great Compassion Bodhisattva inscription), one hall (the Thousand Tang Epitaphs)—this journey wove together natural spectacle, poetic geography, personal destiny, and millennium-old stone carvings. That Song stele altered his life's trajectory, and over a thousand Tang epitaphs made him face the ghostly echoes from history's depths.",
    "Down to Xiangyang, On to Luoyang")

# =============== CHAPTER 12: 细雨骑驴入剑门 ===============
ch012_zh = zh_page("12", "细雨骑驴入剑门",
    "华山 · 秦岭 · 汉中 · 广元 · 昭化",
    "探访千唐志斋后，赖瑞和从铁门上火车，黄昏抵华山脚下小镇。次日爬到五里关时被清风和宋人山水画般的山色留住，竟再也无心登顶——「不如坐在山坡上享受这一阵清风，这一幅山水，和这一种难遇的心情吧」。随即翻越秦岭：凌晨三点起床、五点发车，走子午旧道，在秦岭上穿行一整个上午，经过喂子坪、林场和城镇，看西安大学生捕蝶「让我猛然回想起我的大学时代」。过汉中访石门汉魏摩崖（虽已被迁入博物馆），买汉中黑米。三度入川抵广元，乘班车「入剑门」——七十二峰如「恐龙巨牙」倒竖天边。被困昭化一天，却意外吃到一尾两公斤的嘉陵江大鲤鱼——「我在中国内地吃到的最好一尾鲤鱼，不是在黄河边上盛产鲤鱼的郑州，而是在寂寂无闻的昭化。」",
    [
        ("⛰️", "5大名胜", "华山·秦岭·汉中<br>广元剑门·昭化"),
        ("🌧️", "陆游诗意路线", "细雨骑驴入剑门<br>重走子午旧道"),
        ("🚌", "凌晨3点起程", "翻越秦岭·子午道<br>一整个上午山中穿行"),
        ("🐟", "2kg嘉陵江鲤鱼", "昭化意外美食<br>滑熘鱼片仅10元"),
    ],
    [
        ("华山脚下：不如不爬", "黄昏抵华山脚下，住西岳饭店。客房窗正对华山——「面对一座高山的窗子，总是让人感觉到一种难言的温馨」。夜里，每隔几分钟就有一列火车从华山脚下开过，「一个个小窗子都亮着灯火，幽灵般地往前移动」。次日爬到五里关坐下休息，清风、灰黑山水、松树从崖缝中探向天边，「这一切真像北宋范宽和巨然的山水画」。陶醉中竟再也无心爬山，一直坐到快中午才下山——「将来有一天，等我的两个女儿都长大了，我可以带她们来，再一齐爬华山去。」"),
        ("翻越秦岭：喂子坪与捕蝶的大学生", "半夜三点起床退房，四点赶到朱雀门对面小站，五点半天未亮发车。走子午旧道——曲折上山路，「弯了一个大弯，又弯下一个大弯」。天亮后经过喂子坪，司机停车让乘客吃早饭。对面旅社里，六七名西安大学生正在收拾捕蝶网——「那几位秀丽的女大学生，衣着简朴，头戴鸭舌帽，很有一种帅气」。这场面猛然让他回想起十多年前的台大时光，「我突然感觉到自己不再年轻，心情像胡适所说的'微近中年'了」。好羡慕这些能在秦岭上捕蝶的年轻人——「我这一生，只怕不可能会有这种机缘了。」"),
        ("汉中：石门摩崖与黑米", "从石泉乘夜班火车到汉中，深夜一点抵达。铁路局招待所以「国家规定」拒绝接待——「好比在阴沟里翻了船那么委屈」。次日访汉中博物馆，石门汉魏十三品摩崖石刻虽已被迁来保护，但「摩崖石刻一离开它的天然环境，就不成其为摩崖了，好比动物园里头的狮子，气势立刻大减」。买两斤汉中名产黑米——回到香港后用高压气锅煮半小时，「芳香扑鼻，加点白糖，淋上泰国椰乳汁，就成了风味绝佳的一道甜品」。"),
        ("入剑门：恐龙巨牙般的七十二峰", "从广元乘班车入剑门。一个多小时后，「右边窗子上开始出现那剑门七十二峰了，一个紧接着一个，像恐龙的巨牙般，倒竖在天边白云之际」。抵达剑门关时不小心错过，心想「不如干脆先跑完这一段古蜀道」。中午在剑阁吃过饭，下午细雨蒙蒙中返回——「我虽不能骑驴入剑门，但倒可以在细雨中出剑门了」。从北上方向看剑门，「那道高高的、巨大的剑门山，就在马路右方不远处，仿佛立在天边，替天行道的那种气势」。坐在亭中默默望着雨中的剑门，下午四点才乘下一班车回广元。"),
        ("昭化：被困一天与意外美食", "赶到昭化时已错过每天唯一一班开往南坪的车，被困在这个偏荒小镇一整天——「又无端端捡到逍遥的一天」。无聊地走到嘉陵江边看漂浮树桐。想把一路购买的书报寄回香港，却因小县邮局不寄香港而作罢——「倒也没有什么失望。看来寄书的机缘，仍未到。」晚饭时开玩笑地问「有没有鱼？」，没想到厨师竟「抱」出一条两公斤的大鲤鱼——「他那个姿态，很像天津杨柳青年画中小孩儿抱鲤鱼那种吉祥图」。「我在中国内地吃到的最好一尾鲤鱼，不是黄河边上盛产鲤鱼的郑州，而是在寂寂无闻的昭化。」"),
    ],
    "华山脚下不爬山的闲散、秦岭子午道上捕蝶大学生的青春气息、汉中博物馆里失了气势的石门摩崖、剑门七十二峰如恐龙巨牙般的壮观、昭化小镇那尾意外鲜美的大鲤鱼——这一程教会他：最好的旅行不是征服所有的目的地，而是在不经意间收获了那些计划之外的风景、美食和心情。",
    "细雨骑驴入剑门")

ch012_en = en_page("12", "Riding a Donkey into Jianmen in Drizzle",
    "Mount Hua · Qinling · Hanzhong · Guangyuan · Zhaohua",
    "After visiting the Hall of a Thousand Tang Epitaphs, Lai boarded a train from Tiemen and reached the foot of Mount Hua by dusk. The next morning, climbing to Wuliguan, he was so captivated by the breeze and the landscape reminiscent of Northern Song ink paintings that he lost all desire to reach the summit—'better to sit on this hillside, enjoying this breeze, this landscape, and this rare mood.' Then over the Qinling Mountains: waking at 3 a.m., departing at 5:30, following the ancient Ziwu Road through an entire morning of mountain travel, passing the hamlet of Weiziping, forest farms and towns, watching university students catching butterflies—'it suddenly brought me back to my college days.' Through Hanzhong to see the Shimen Han-Wei cliff carvings (now relocated to a museum) and buy Hanzhong black rice. Third entry into Sichuan to Guangyuan, taking a bus 'into Jianmen'—seventy-two peaks rising 'like dinosaur fangs against the white clouds.' Stranded a full day in remote Zhaohua, yet unexpectedly ate a two-kilogram Jialing River carp—'the best carp I ever tasted in mainland China, not from carp-famous Zhengzhou on the Yellow River, but from obscure, unheard-of Zhaohua.'",
    [
        ("⛰️", "5 Landmarks", "Mount Hua·Qinling·Hanzhong<br>Jianmen Pass·Zhaohua"),
        ("🌧️", "Lu You's Poetic Path", "Riding donkey into Jianmen<br>Retracing ancient Ziwu Road"),
        ("🚌", "3 AM Departure", "Crossing Qinling·Ziwu Road<br>A full morning in mountains"),
        ("🐟", "2kg Jialing Carp", "Zhaohua surprise feast<br>Sautéed fillets: only ¥10"),
    ],
    [
        ("At Mount Hua's Foot: Better Not to Climb", "Arriving at Mount Hua's base at dusk, staying at the West Peak Hotel. His room window faced Mount Hua directly—'a window facing a tall mountain always brings an ineffable warmth.' At night, every few minutes a train passed below, 'each small window lit, ghostly lights moving forward.' The next morning he climbed to Wuliguan and sat to rest. A fresh breeze, grey-black mountains like ink-wash, pines jutting from cliff crevices toward the sky—'all this truly resembled the landscapes of Northern Song masters Fan Kuan and Juran.' Captivated, he lost all desire to continue climbing, sitting until nearly noon before descending. 'One day, when my two daughters are grown, I can bring them here to climb Mount Hua together.'"),
        ("Crossing the Qinling: Weiziping and Butterfly-Hunting Students", "Waking at 3 a.m., checking out, arriving at the small station across from Zhuquemen by 4 a.m. Departure at 5:30, before dawn. Taking the ancient Ziwu Road—a winding mountain ascent, 'rounding one great bend, rounding down another.' At daybreak, passing Weiziping, the driver stopped for breakfast. In the inn across the way, six or seven Xi'an university students were packing butterfly nets—'those graceful female students, in simple clothes with baseball caps, had a wonderful spirited air.' The scene abruptly recalled his NTU days over a decade past: 'I suddenly felt I was no longer young, my mood what Hu Shi called approaching middle age.' He envied those young students catching butterflies on Qinling—'in this lifetime, I shall probably never have such a chance.'"),
        ("Hanzhong: Shimen Cliff Carvings and Black Rice", "From Shiquan by night train to Hanzhong, arriving at 1 a.m. The railway guesthouse refused him citing 'state regulations'—'like capsizing in a ditch, so aggrieved.' Next day at the Hanzhong Museum, the Shimen Han-Wei thirteen cliff carvings had been relocated for protection, but 'once removed from their natural setting, they cease to be cliff carvings—like lions in a zoo, their majesty instantly diminished.' He bought two jin of Hanzhong's famed black rice—back in Hong Kong, pressure-cooked for half an hour, 'fragrance wafting, add sugar, drizzle Thai coconut milk, a dessert of exquisite flavor.'"),
        ("Entering Jianmen: Seventy-Two Peaks Like Dinosaur Fangs", "From Guangyuan by bus toward Jianmen. After an hour, 'on the right window, the seventy-two peaks of Jianmen began to appear, one after another, like dinosaur fangs, inverted against the edge of sky and white clouds.' He missed the stop at Jianmen Pass, decided 'might as well first traverse this entire stretch of the ancient Shu Road.' After lunch in Jiange, returning in the afternoon drizzle—'though I could not ride a donkey into Jianmen, I could at least exit Jianmen in drizzling rain.' From the northward direction, 'that towering, colossal Jianmen Mountain, just to the right of the road, seemed to stand at heaven's edge, enforcing heaven's mandate.' He sat in a pavilion, silently watching rain-soaked Jianmen until the 4 p.m. bus carried him back to Guangyuan."),
        ("Zhaohua: Stranded a Day, an Unexpected Feast", "Arriving in Zhaohua after the day's only bus to Nanping had left, stranded in this remote hamlet for a full day—'picking up yet another carefree day for no reason.' He wandered idly to the Jialing River, watching floating logs. Trying to mail home his growing pile of purchased books met defeat at the county post office—'not much disappointment. The karma for mailing books had not yet arrived.' At dinner, half-jokingly asked: 'Any fish?' The cook emerged cradling a two-kilogram carp in his arms—'his posture was exactly like the auspicious New Year's print of a child embracing a carp from Tianjin's Yangliuqing.' 'The best carp I ever tasted in mainland China was not on the Yellow River in carp-famous Zhengzhou, but in obscure, unheard-of Zhaohua.'"),
    ],
    "Choosing not to climb Mount Hua, the youthful energy of butterfly-hunting students on the Qinling Ziwu Road, the diminished majesty of Shimen cliff carvings in a museum, Jianmen's seventy-two peaks like dinosaur fangs, and a two-kilogram carp feast in forgotten Zhaohua—this journey taught him that the best travel isn't conquering every destination, but discovering the unplanned landscapes, flavors, and moods along the way.",
    "Riding a Donkey into Jianmen in Drizzle")

# Write all 8 files
files = [
    ("杜甫的五城-ch009-info-zh.html", ch09_zh),
    ("杜甫的五城-ch009-info-en.html", ch09_en),
    ("杜甫的五城-ch010-info-zh.html", ch010_zh),
    ("杜甫的五城-ch010-info-en.html", ch010_en),
    ("杜甫的五城-ch011-info-zh.html", ch011_zh),
    ("杜甫的五城-ch011-info-en.html", ch011_en),
    ("杜甫的五城-ch012-info-zh.html", ch012_zh),
    ("杜甫的五城-ch012-info-en.html", ch012_en),
]

for fname, content in files:
    with open(fname, 'w') as f:
        f.write(content)
    print(f"✅ Written: {fname} ({len(content)} bytes)")

print("\nDone! All 8 files generated.")