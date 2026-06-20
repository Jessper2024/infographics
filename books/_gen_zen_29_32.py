#!/usr/bin/env python3
"""Generate ch029-ch032 ZH+EN infographic HTML files for 禅与摩托车维修艺术"""

import os

BOOKDIR = os.path.expanduser("~/.openclaw/workspace/infographics/books")
SLUG = "禅与摩托车维修艺术"

CSS = """*{margin:0;padding:0;box-sizing:border-box}
body{background:#f5f1eb;display:flex;justify-content:center;align-items:flex-start;min-height:100vh;padding:32px 16px 60px;font-family:'FZXPYZS','PingFang SC','Hiragino Sans GB','Microsoft YaHei',serif;color:#555}
.container{max-width:880px;width:100%}
.catalog-link{text-align:right;margin-bottom:12px}
.catalog-link a{font-size:13px;color:#888;text-decoration:none;transition:color .2s;padding:4px 10px;border:1px solid #d8d0c5;border-radius:20px;background:#fff}
.catalog-link a:hover{color:#dc2626}
.lang-switch{text-align:center;margin-bottom:24px}
.lang-switch a{display:inline-block;padding:6px 18px;margin:0 4px;font-size:13px;border:1px solid #d8d0c5;border-radius:20px;background:#fff;color:#555;text-decoration:none;transition:all .2s}
.lang-switch a.active{background:#4f46e5;color:#fff;border-color:#4f46e5}
.lang-switch a:hover:not(.active){border-color:#dc2626;color:#dc2626}
.header{text-align:center;margin-bottom:28px}
.header h1{font-size:28px;color:#1a1a1a;font-weight:400;line-height:1.4;margin-bottom:6px}
.header .subtitle{font-size:14px;color:#888;margin-bottom:16px}
.divider{width:60px;height:3px;background:linear-gradient(to right,#dc2626,#ea580c);margin:0 auto 28px;border-radius:2px}
.chapter-overview{background:#f8f6f3;border-left:3px solid #4f46e5;border-radius:8px;padding:16px 20px;margin:12px 0 24px;font-size:14px;color:#555;line-height:1.8;font-family:'FZXPYZS','PingFang SC',serif}
.chapter-overview p{margin:0}
.kpi-row{display:flex;flex-wrap:wrap;gap:12px;margin-bottom:28px}
.kpi-card{flex:1;min-width:140px;background:#fff;border-radius:14px;padding:16px 14px;text-align:center;box-shadow:0 1px 8px rgba(0,0,0,0.03);border-top:3px solid #ccc}
.kpi-card .kpi-val{font-size:26px;font-weight:700;line-height:1.3}
.kpi-card .kpi-label{font-size:12px;color:#888;margin-top:4px}
.section{background:#fff;border-radius:14px;padding:22px 24px;margin-bottom:18px;box-shadow:0 1px 8px rgba(0,0,0,0.03);position:relative}
.section .sec-header{display:flex;align-items:center;gap:12px;margin-bottom:14px;flex-wrap:wrap}
.section .sec-num{width:42px;height:42px;border-radius:50%;display:flex;align-items:center;justify-content:center;font-size:16px;font-weight:700;flex-shrink:0}
.section .sec-tag{font-size:11px;padding:3px 10px;border-radius:12px;font-weight:600;letter-spacing:.04em}
.section .sec-title{font-size:18px;font-weight:700;line-height:1.3}
.section .sec-body{font-size:14px;line-height:1.9;color:#555;margin-bottom:18px}
.flow-row{display:flex;align-items:center;flex-wrap:wrap;gap:8px;padding:6px 0}
.flow-step{background:#fff7ed;border:1px solid #fed7aa;border-radius:10px;padding:8px 14px;font-size:13px;color:#9a3412;font-weight:600;text-align:center;white-space:nowrap}
.flow-step.end{background:#fef2f2;border-color:#fecaca;color:#991b1b}
.flow-arrow{color:#ea580c;font-size:18px;font-weight:bold}
.dual-grid{display:flex;gap:14px}
.dual-card{flex:1;border-radius:12px;padding:18px;font-size:13px;line-height:1.8;white-space:pre-line}
.dual-card.yes{background:#f0fdf4;border:1px solid #bbf7d0}
.dual-card.no{background:#fef2f2;border:1px solid #fecaca}
.quote-box{background:#fdf2f8;border:1px solid #fbcfe8;border-radius:12px;padding:18px 22px;font-size:14px;line-height:2;color:#9d174d;text-align:center}
.takeaway{background:#fff;border-left:4px solid #db2777;border-radius:14px;padding:22px 28px;margin-top:22px;margin-bottom:22px;box-shadow:0 1px 8px rgba(0,0,0,0.03);font-size:14px;line-height:1.9;color:#555}
.takeaway .ta-label{font-size:12px;color:#db2777;font-weight:bold;text-transform:uppercase;letter-spacing:.08em;margin-bottom:8px}
.footer{text-align:center;font-size:13px;color:#bbb;padding:20px 0 10px;line-height:1.8}
@media(max-width:640px){
  .kpi-row{flex-direction:column}
  .dual-grid{flex-direction:column}
  .flow-row{flex-direction:column;align-items:stretch}
}"""

# =============================================
# Chapter 29 data
# =============================================
ch029_zh = {
    "num": "第二十九章",
    "title": "「智者的复仇——卓越的湮灭与良质的重生」",
    "subtitle": "「人是衡量一切的标准」——古希腊智者在一千年前就教导着良质",
    "overview": (
        "波西格从修理链条护罩的日常琐事出发，在焊接工和女服务生眼中发现了共同的寂寞。这种寂寞并非源于物理距离，而是科技所强化的主客二分——当人被物化时，人与人之间的心理距离便无限扩大。斐德洛的哲学探索推进到最深处：他从亚里士多德的修辞学分类中嗅到了学究的腐朽，在柏拉图的《对话录》中发现了惊人的真相——苏格拉底和柏拉图用辩证法摧毁了智者的卓越（Arete），将良质从最高地位贬至真理之下。柏拉图把智者的「卓越」固定化为僵化的「善」的理念，亚里士多德进一步用形式与本质的二分法将良质彻底埋葬。两千年来，西方文明以真理之名压制良质，直到斐德洛这个「狂人」挖出了被埋葬的智者遗骨——卓越，才是古希腊人真正的追求。"
    ),
    "kpis": [
        ("1 把", "焊接枪：寂寞的手艺人", "#dc2626"),
        ("1 个", "问题：摧毁斐德洛的研究", "#ea580c"),
        ("2 派", "宇宙学者 vs 智者", "#ca8a04"),
        ("2000 年", "良质被埋葬的时间", "#4f46e5"),
    ],
    "sections": [
        {
            "color": "#dc2626", "tag": "旅途",
            "title": "寂寞的焊接工：科技不能消除心理距离",
            "body": (
                "从修理链条护罩开始，波西格走进一间「最干净的焊接店」。老板六七十岁，用令人惊叹的手艺焊接好了薄薄的金属片，收费一块钱——眼中却和那位女服务生一样，有着相同的寂寞。沿着海岸进入加州，波西格在超市、洗衣店、汽车旅馆、杉林和城市中处处看到寂寞的面孔。他敏锐地发现：在人口稀少的蒙大拿和爱达荷，人们心理距离很近；在拥挤的西海岸，人们反而最寂寞。「身体上的距离和寂寞毫不相关，造成寂寞的原因是心理的距离。」真正祸首不是科技本身，而是科技背后截然二分主客观的看法——它将人变成了物体。"
            ),
            "viz": (
                '<div class="flow-row">'
                '<div class="flow-step">🔧 焊接工<br/>一块钱手艺<br/>眼中寂寞</div>'
                '<div class="flow-arrow">→</div>'
                '<div class="flow-step">👩 女服务生<br/>偷偷注视<br/>同样寂寞</div>'
                '<div class="flow-arrow">→</div>'
                '<div class="flow-step">🏙️ 西海岸<br/>人口最密<br/>寂寞最重</div>'
                '<div class="flow-arrow">→</div>'
                '<div class="flow-step">🌄 蒙大拿<br/>人口最少<br/>心理最近</div>'
                '<div class="flow-arrow">→</div>'
                '<div class="flow-step end">⚡ 主客二分<br/>= 物化人<br/>= 寂寞之源</div>'
                '</div>'
            ),
        },
        {
            "color": "#ea580c", "tag": "哲学",
            "title": "亚里士多德的分类暴政：修辞学如何被贬低",
            "body": (
                "斐德洛重读亚里士多德，看到的是一堆乏味的分类——"修辞学可分成特定实证和一般实证。特定实证可分成实证方法和实证种类……"这和三流技术指导员把一切列出来、仔细解说、自作聪明指出新关系的方式毫无二致。亚里士多德把修辞学视为理论科学的次要分支——实用科学的一支，与真理、善和美完全隔绝。在亚里士多德的体系中，良质和修辞学被完全分离。「亚里士多德树立了一个坏榜样，在历史上有数以百万计的无知而自满的老师，他们运用这种愚笨的分析模式，无情地把学生的创造力给抹煞了。现在进入任何一间教室，你听到的只不过是亚里士多德数千年前的鬼魂在说话。」"
            ),
            "viz": (
                '<div class="dual-grid">'
                '<div class="dual-card yes">📐 亚里士多德体系<br/>• 理论科学（最高）<br/>• 实用科学（次要）<br/>  └ 修辞学<br/>• 良质与修辞学<br/>  完全分离<br/>→ 真/善/美优先<br/>  良质靠边站</div>'
                '<div class="dual-card no">⚠️ 两千年的后果<br/>• 教室里永无止尽的分析<br/>• 学生创造力被抹煞<br/>• 形式与规则取代卓越<br/>• 修辞学沦为"空洞"<br/>• 甲等归循规蹈矩者<br/>  卓越归沉默的后排</div>'
                '</div>'
            ),
        },
        {
            "color": "#ca8a04", "tag": "课堂",
            "title": "课堂上的无声对决：辩证法的狩猎",
            "body": (
                "在阴暗的教室里，哲学教授当众羞辱学生——「我们来这里不是要研究你想什么，而是要研究亚里士多德想什么。」教授把权威浪费在无辜学生身上，却因此暴露了弱点。当教授指向斐德洛时，斐德洛沉稳而准确地说出了特定修辞学的三种分类。教授的攻击被化解，教室一片寂然。那位无辜学生再也没有回来。斐德洛保持沉默，努力学习——不是为了做「好学生」，而是为了寻找攻击的材料。教授开始害怕斐德洛，因为教室里的力量格局已经逆转。教授试图用苏格拉底式的辩证法引诱斐德洛讨论烹饪，斐德洛看穿了陷阱——"辩证法正是苏格拉底摧毁修辞学家高尔吉亚的武器。""
            ),
            "viz": (
                '<div class="flow-row">'
                '<div class="flow-step">🎯 教授<br/>羞辱无辜学生<br/>树立权威</div>'
                '<div class="flow-arrow">→</div>'
                '<div class="flow-step">🐺 斐德洛<br/>准确回答<br/>分类问题</div>'
                '<div class="flow-arrow">→</div>'
                '<div class="flow-step">😨 教授<br/>开始恐惧<br/>力量逆转</div>'
                '<div class="flow-arrow">→</div>'
                '<div class="flow-step">🎣 教授<br/>设陷阱：<br/>烹饪=煽动</div>'
                '<div class="flow-arrow">→</div>'
                '<div class="flow-step end">🛡️ 斐德洛<br/>看穿：辩证法<br/>= 摧毁修辞学<br/>的武器</div>'
                '</div>'
            ),
        },
        {
            "color": "#4f46e5", "tag": "溯源",
            "title": "柏拉图的背叛：卓越如何被固定为「善」",
            "body": (
                "斐德洛深入研究了苏格拉底之前的哲学史后发现了全貌。在古希腊，有两派对立的学者：宇宙学者（泰勒斯学派、毕达哥拉斯学派、巴门尼德等）追求不变的「真理」；智者们则教导「卓越」（Arete）——"人是衡量一切的标准"，这是斐德洛所说的良质。柏拉图综合了两派：将智者的「卓越」转化为「善」——一种固定不变的理念，在真理序列中排在真理之下；用辩证法作为通往真理的惟一方法。更糟糕的是，柏拉图在《对话录》中对智者大肆诅咒，用苏格拉底辩证法的刀把高尔吉亚的修辞学劈成碎片——这些碎片正是后来亚里士多德修辞学的基础。斐德洛在书旁愤怒地写道："骗子！"——苏格拉底根本没有用辩证法去了解修辞学，而是用它去摧毁修辞学。"
            ),
            "viz": (
                '<div class="flow-row">'
                '<div class="flow-step">🌌 宇宙学者<br/>追求真理<br/>永恒不变</div>'
                '<div class="flow-arrow">→</div>'
                '<div class="flow-step">🏆 智者<br/>教导卓越<br/>人是标准</div>'
                '<div class="flow-arrow">→</div>'
                '<div class="flow-step">⚔️ 柏拉图<br/>综合两派<br/>善<真理</div>'
                '<div class="flow-arrow">→</div>'
                '<div class="flow-step">🔪 辩证法<br/>摧毁修辞学<br/>贬低卓越</div>'
                '<div class="flow-arrow">→</div>'
                '<div class="flow-step end">📚 亚里士多德<br/>形式+本质<br/>良质彻底埋葬</div>'
                '</div>'
            ),
        },
        {
            "color": "#db2777", "tag": "复仇",
            "title": "智者的复仇：两千年后，卓越被重新发现",
            "body": (
                "斐德洛在季多的《希腊人》中发现了决定性证据：荷马的英雄不是被「责任」驱动，而是被「卓越」——Arete——驱动。这个词被后人误译为「伦理道德」，完全丧失了原意。卓越意味着对生活完整性的尊重，要求生命的本身就很卓越，而不只是某一部分卓越。奥德赛的英雄能演说、能建船、能犁地、能拳击、能赛跑，也能因美妙的歌曲感动流泪。"卓越暗示着对所谓的效率的轻视——它具有更高等级的效率。"两千年前智者们教导的正是这个。他们的尸骨化为尘土，所说的话也烟消云散，被埋在毁灭的雅典、覆灭的马其顿、古罗马和拜占庭的瓦堆之下——"只有很多个世纪之后出现的这个狂人，才发现了可以将他们出土的线索，同时恐怖地看清了前人的所作所为。""
            ),
            "viz": (
                '<div class="quote-box">"我们翻译成<span style="font-weight:bold;color:#ea580c;">伦理道德</span>的<br/>希腊原文是指<br/><span style="font-weight:bold;font-size:22px;color:#dc2626;">卓越</span>"<br/><br/>⚡ 两千年前<br/>智者就在教导<span style="font-weight:bold;color:#4f46e5;">良质</span><br/><br/>荷马的英雄追求<span style="font-weight:bold;color:#ca8a04;">卓越</span><br/>而非责任<br/><br/>只有<span style="font-weight:bold;font-size:18px;">狂人</span><br/>才能挖出被埋葬的真相</div>'
            ),
        },
    ],
    "takeaway": (
        "这是全书哲学体系最壮观的一章。波西格完成了对西方思想史的一整套"考古发掘"：从焊接工眼中的寂寞（主客二分的后果），到亚里士多德对修辞学和良质的分类性贬低（体系化暴政的起源），到柏拉图用辩证法摧毁智者的卓越（真理篡夺了善的地位），再到两千年前智者们原本教导的「卓越」如何被完全遗忘。斐德洛发现的真相是惊心动魄的：早在苏格拉底和柏拉图之前，希腊的智者就已经在教导良质了——"人是衡量一切的标准"——只是他们用来说明良质的词是Arete：卓越。柏拉图把它固定为僵化的「善」，亚里士多德把它进一步埋葬在"形式与本质"之下。两千年来，整个西方文明在追求真理的同时，遗忘并压制了它真正的源头——良质。而斐德洛，这个在雨雾中骑行的「狂人」，成为了第一个重新挖出这根线索的人。"
    ),
}

ch029_en = {
    "num": "Chapter 29",
    "title": "\"The Revenge of the Sophists — The Burial and Resurrection of Quality\"",
    "subtitle": "\"Man is the measure of all things\" — The Sophists were teaching Quality a thousand years before dialectics",
    "overview": (
        "Starting from repairing a chain guard at a welding shop, Pirsig discovers a common loneliness in the eyes of the welder and the waitress — a loneliness caused not by physical distance but by the subject-object dualism reinforced by technology. When people are objectified, psychological distance becomes infinite. Phaedrus's philosophical investigation reaches its deepest level: he detects scholastic decay in Aristotle's rhetorical classifications, then discovers in Plato's Dialogues a shocking truth — Socrates and Plato used dialectics to destroy the Sophists' Excellence (Arete), demoting Quality below Truth. Plato fixed the fluid Arete into a rigid Idea of the Good; Aristotle buried it further under form and substance. For two thousand years, Western civilization suppressed Quality in the name of Truth — until Phaedrus, this \"madman,\" unearthed the buried bones of the Sophists."
    ),
    "kpis": [
        ("1", "Welding torch: lonely craftsman", "#dc2626"),
        ("1", "Question: destroyed Phaedrus's research", "#ea580c"),
        ("2", "Camps: Cosmologists vs Sophists", "#ca8a04"),
        ("2000 yrs", "Quality buried underground", "#4f46e5"),
    ],
    "sections": [
        {
            "color": "#dc2626", "tag": "Journey",
            "title": "The Lonely Welder: Technology Cannot Erase Psychological Distance",
            "body": (
                "From repairing a chain guard, Pirsig enters the \"cleanest welding shop\" he has ever seen. The welder, in his sixties or seventies, repairs the thin metal plate with breathtaking skill — charges one dollar — yet in his eyes is the same loneliness as the waitress. Riding along the coast into California, Pirsig sees lonely faces everywhere: supermarkets, laundromats, motels, redwood forests, cities. He discovers the paradox: in sparsely populated Montana and Idaho, people are psychologically close; in crowded West Coast cities, they are the loneliest. \"Physical distance and loneliness have nothing to do with each other. Loneliness is caused by psychological distance.\" The real culprit is not technology itself, but the underlying subject-object dualism that turns people into objects."
            ),
            "viz": (
                '<div class="flow-row">'
                '<div class="flow-step">🔧 The Welder<br/>One-dollar skill<br/>Lonely eyes</div>'
                '<div class="flow-arrow">→</div>'
                '<div class="flow-step">👩 Waitress<br/>Watches secretly<br/>Same loneliness</div>'
                '<div class="flow-arrow">→</div>'
                '<div class="flow-step">🏙️ West Coast<br/>Most crowded<br/>Loneliest</div>'
                '<div class="flow-arrow">→</div>'
                '<div class="flow-step">🌄 Montana<br/>Least crowded<br/>Closest hearts</div>'
                '<div class="flow-arrow">→</div>'
                '<div class="flow-step end">⚡ Dualism<br/>= Objectification<br/>= Source of loneliness</div>'
                '</div>'
            ),
        },
        {
            "color": "#ea580c", "tag": "Philosophy",
            "title": "Aristotle's Tyranny of Classification: How Rhetoric Was Degraded",
            "body": (
                "Phaedrus rereads Aristotle and finds only tedious classifications — \"Rhetoric can be divided into particular proofs and general proofs. Particular proofs can be divided into methods of proof and kinds of proof...\" It reads exactly like a third-rate technical manual listing all parts, explaining relationships, self-satisfied about trivial new connections. Aristotle made rhetoric a minor branch of practical science, completely severed from Truth, Goodness, and Beauty. In Aristotle's system, Quality and rhetoric are fully separated. \"Aristotle set a bad example, followed by millions of ignorant and self-satisfied teachers across history who used this foolish analytical model, ruthlessly obliterating students' creativity. Enter any classroom today and you hear nothing but Aristotle's ghost from two thousand years ago — a voice lacking vitality, endorsing dualistic thinking.\""
            ),
            "viz": (
                '<div class="dual-grid">'
                '<div class="dual-card yes">📐 Aristotle\'s System<br/>• Theoretical Science (highest)<br/>• Practical Science (secondary)<br/>  └ Rhetoric<br/>• Quality & rhetoric<br/>  completely severed<br/>→ Truth/Goodness/Beauty first<br/>  Quality pushed aside</div>'
                '<div class="dual-card no">⚠️ Two-Thousand-Year Consequences<br/>• Endless analysis in classrooms<br/>• Student creativity obliterated<br/>• Form & rules replace Excellence<br/>• Rhetoric reduced to "empty"<br/>• Straight A\'s for conformists<br/>  Excellence for silent back row</div>'
                '</div>'
            ),
        },
        {
            "color": "#ca8a04", "tag": "Classroom",
            "title": "Silent Duel in the Classroom: The Hunt of Dialectics",
            "body": (
                "In a gloomy classroom, the philosophy professor publicly humiliates a student — \"We are not here to study what you think, but what Aristotle thought.\" The professor wastes his authority on an innocent student, exposing his own weakness. When he turns to Phaedrus, Phaedrus calmly and accurately names the three kinds of particular rhetoric. The professor's attack is neutralized. Silence fills the room. The innocent student never returns. Phaedrus stays silent, studying relentlessly — not to be a \"good student,\" but to find material for attack. The professor begins to fear Phaedrus, for the power dynamics in the classroom have reversed. The professor tries to trap Phaedrus with a Socratic question about cooking — Phaedrus sees through it: \"Dialectics was precisely the weapon Socrates used to destroy Gorgias the rhetorician.\""
            ),
            "viz": (
                '<div class="flow-row">'
                '<div class="flow-step">🎯 Professor<br/>Humiliates student<br/>Establishes authority</div>'
                '<div class="flow-arrow">→</div>'
                '<div class="flow-step">🐺 Phaedrus<br/>Answers correctly<br/>Classification question</div>'
                '<div class="flow-arrow">→</div>'
                '<div class="flow-step">😨 Professor<br/>Begins to fear<br/>Power shifts</div>'
                '<div class="flow-arrow">→</div>'
                '<div class="flow-step">🎣 Professor<br/>Sets trap:<br/>Cooking = pandering</div>'
                '<div class="flow-arrow">→</div>'
                '<div class="flow-step end">🛡️ Phaedrus<br/>Sees through:<br/>Dialectics = weapon<br/>to destroy rhetoric</div>'
                '</div>'
            ),
        },
        {
            "color": "#4f46e5", "tag": "Origins",
            "title": "Plato's Betrayal: How Excellence Was Fixed as \"the Good\"",
            "body": (
                "Diving into pre-Socratic philosophy, Phaedrus discovers the full picture. Ancient Greece had two opposing camps: Cosmologists (Thales, Pythagoreans, Parmenides) pursuing unchanging Truth; Sophists teaching Arete (Excellence) — \"Man is the measure of all things\" — which is exactly Phaedrus's Quality. Plato synthesized both: he turned the Sophists' fluid Excellence into \"the Good\" — a fixed, unchanging Idea, ranked below Truth in the hierarchy; and made dialectics the sole path to Truth. Worse still, in the Dialogues, Plato viciously cursed the Sophists, using Socrates's dialectical knife to slice Gorgias's rhetoric into fragments — the very fragments that became the foundation of Aristotle's Rhetoric. Phaedrus scrawled in the margin: \"Fraud!\" — Socrates never used dialectics to understand rhetoric, but to destroy it."
            ),
            "viz": (
                '<div class="flow-row">'
                '<div class="flow-step">🌌 Cosmologists<br/>Pursue Truth<br/>Eternal & unchanging</div>'
                '<div class="flow-arrow">→</div>'
                '<div class="flow-step">🏆 Sophists<br/>Teach Arete<br/>Man is the measure</div>'
                '<div class="flow-arrow">→</div>'
                '<div class="flow-step">⚔️ Plato<br/>Synthesizes both<br/>Good < Truth</div>'
                '<div class="flow-arrow">→</div>'
                '<div class="flow-step">🔪 Dialectics<br/>Destroys rhetoric<br/>Demotes Excellence</div>'
                '<div class="flow-arrow">→</div>'
                '<div class="flow-step end">📚 Aristotle<br/>Form + Substance<br/>Quality fully buried</div>'
                '</div>'
            ),
        },
        {
            "color": "#db2777", "tag": "Resurrection",
            "title": "The Revenge of the Sophists: Excellence Rediscovered After Two Millennia",
            "body": (
                "Phaedrus finds the decisive evidence in Kitto's \"The Greeks\": Homer's heroes were driven not by \"duty\" but by Arete — Excellence. This word was later mistranslated as \"virtue\" or \"ethics,\" completely losing its original meaning. Arete implies respect for the wholeness of life, demanding that life itself be excellent, not just one part. Odysseus could speak, build a ship, plow a field, box, race, and weep at beautiful songs. \"Arete implies a contempt for so-called efficiency — it represents a higher-grade efficiency.\" This is what the Sophists taught two thousand years ago. Their bones turned to dust, their words scattered in the wind, buried beneath the ruins of Athens, Macedon, Rome, and Byzantium — \"Only after many centuries did this madman appear, finding the clues to unearth them, while seeing with horror what their predecessors had done.\""
            ),
            "viz": (
                '<div class="quote-box">"The Greek word we translate as<br/><span style="font-weight:bold;color:#ea580c;">Virtue</span><br/>originally means<br/><span style="font-weight:bold;font-size:22px;color:#dc2626;">Excellence</span>"<br/><br/>⚡ Two thousand years ago<br/>Sophists taught <span style="font-weight:bold;color:#4f46e5;">Quality</span><br/><br/>Homer\'s heroes pursued <span style="font-weight:bold;color:#ca8a04;">Excellence</span><br/>not duty<br/><br/>Only a <span style="font-weight:bold;font-size:18px;">madman</span><br/>could unearth the buried truth</div>'
            ),
        },
    ],
    "takeaway": (
        "This is the most spectacular philosophical chapter in the entire book. Pirsig completes an archaeological excavation of Western intellectual history: from the loneliness in the welder's eyes (the consequence of subject-object dualism), to Aristotle's classificatory degradation of rhetoric and Quality (the origin of systematic tyranny), to Plato's dialectical destruction of the Sophists' Excellence (Truth usurped the throne of the Good), to how the Arete taught by the Sophists two millennia ago was completely forgotten. Phaedrus's discovery is electrifying: long before Socrates and Plato, Greek Sophists were already teaching Quality — \"Man is the measure of all things\" — only the word they used was Arete: Excellence. Plato fixed it as rigid \"Goodness,\" Aristotle buried it further under \"form and substance.\" For two thousand years, Western civilization pursued Truth while forgetting and suppressing its true source — Quality. And Phaedrus, this \"madman\" riding through rain and fog, became the first to rediscover this thread."
    ),
}

# =============================================
# Chapter 30 data
# =============================================
ch030_zh = {
    "num": "第三十章",
    "title": "「死荫的幽谷——斐德洛的崩溃与觉醒」",
    "subtitle": "「你必须要独自经过那死荫的幽谷」——走出神话，灵魂得到安息",
    "overview": (
        "哲学教授因病缺席，委员会主席接管课堂。斐德洛经历了与主席的直接对决——他在这场辩证法的角力中精确地指出苏格拉底自己说过"这是比喻"，使主席颜面扫地。然而当主席问他"什么是辩证法"时，斐德洛指出"辩证法先于所有一切"——这正是主席自己的观点。主席震惊、暴怒、打断——却无法攻击自己说过的话。但斐德洛的胜利反而揭示了深渊：他意识到自己正在用系统性的思考去界定良质，这本身就是对良质的背叛。「一旦想通过系统的思考去界定良质，就会破坏它最原始的目标。」他停止了教学，盯着墙壁三日三夜，抛弃所有身外之物，独自走过"死荫的幽谷"——走出神话，走出自我，意识完全瓦解。从崩溃的边缘，他获得前所未有的理解：「他曾经这样辛苦地保卫、牺牲，从来没有背叛过的良质，原来他从来不曾了解，现在却了然于心，他的灵魂得到安息了。」"
    ),
    "kpis": [
        ("2 分", "修辞学得分：击败辩证法", "#dc2626"),
        ("3 天", "盯着墙壁：意识瓦解", "#ea580c"),
        ("4 堂", "沉默的课：不再教学", "#ca8a04"),
        ("1 扇", "打不开的门：医院", "#4f46e5"),
    ],
    "sections": [
        {
            "color": "#dc2626", "tag": "对决",
            "title": "主席登场：辩证法猎杀狼",
            "body": (
                "主席走进教室，带着仁慈的笑容和旧烟斗。他用一种近乎催眠的眼神巡视每一个人。那位曾被羞辱的无辜学生也回来了——他来旁观斐德洛被猎杀。斐德洛留了胡子，主席一时没能认出他。但斐德洛已经准备好了。当主席开始讲解柏拉图的《斐德洛篇》，宣称苏格拉底向神明发誓马车和马的描述是「真理」时，斐德洛举起手："这一切只不过是比喻。苏格拉底自己说这是比喻。"主席不敢翻阅教材求证——如果证明斐德洛正确，他在班里的颜面就扫地了。修辞学得一分；辩证法得零分。"
            ),
            "viz": (
                '<div class="flow-row">'
                '<div class="flow-step">🎭 主席<br/>仁慈笑容<br/>催眠眼神</div>'
                '<div class="flow-arrow">→</div>'
                '<div class="flow-step">📖 "马车与马<br/>是真理"<br/>苏格拉底发誓</div>'
                '<div class="flow-arrow">→</div>'
                '<div class="flow-step">🐺 斐德洛举手<br/>"苏格拉底自己<br/>说这是比喻"</div>'
                '<div class="flow-arrow">→</div>'
                '<div class="flow-step">😱 主席<br/>不敢翻教材<br/>颜面扫地</div>'
                '<div class="flow-arrow">→</div>'
                '<div class="flow-step end">🏆 修辞学 2<br/>辩证法 0<br/>第一回合</div>'
                '</div>'
            ),
        },
        {
            "color": "#ea580c", "tag": "陷阱",
            "title": "陷阱反转：辩证法的自我吞噬",
            "body": (
                "主席不甘失败，转向斐德洛问道："什么是辩证法？"——他要将斐德洛拉入自己的领域。斐德洛回答："就我所知，亚里士多德认为辩证法先于所有的一切。"主席的表情从感谢变为震惊，再变为暴怒——这正是他自己在《大英百科全书》中写过的话。他不能因为斐德洛引用了自己的观点而攻击他。修辞学再得一分。主席打断了斐德洛的后续发挥，结束了对话。斐德洛想：如果他是真正追寻真理的人，就不应该打断。"辩证法先于所有的一切"——这句话本身就成了辩证的实体，隶属于辩证问题。有什么证据？毫无证据。辩证法像牛顿定律一样悬在半空，下面没有任何支撑，却宣称是万物的根源——"真是愚不可及的事。""
            ),
            "viz": (
                '<div class="dual-grid">'
                '<div class="dual-card yes">🎯 斐德洛的陷阱反转<br/>主席问：什么是辩证法？<br/>斐德洛引用主席自己的话：<br/>"辩证法先于所有一切"<br/>主席的表情：<br/>感谢→震惊→暴怒<br/>不能攻击自己的话</div>'
                '<div class="dual-card no">🕳️ 辩证法的空洞<br/>"辩证法先于一切"<br/>→ 没有证据支持<br/>→ 悬在半空无支撑<br/>→ 却宣称是万物根源<br/>→ 历史上与常识上<br/>  辩证法的源头是<br/>  修辞学→神话→诗→良质</div>'
                '</div>'
            ),
        },
        {
            "color": "#ca8a04", "tag": "崩溃",
            "title": "意识瓦解：沉默的课堂与死荫的幽谷",
            "body": (
                "斐德洛发现自己开始害怕教室里的沉寂。他开始在上课时一言不发——先是一堂课，然后是两堂，然后四堂课的沉默。学生惊慌失措。感恩节到了，一切结束。他走过芝加哥的街道，城市在他眼中变成了「形式与本质的大本营」：砖块、水泥、霓虹灯，没有良质。他对时间的感觉在逐渐消失。有一个念头击中了他——他发现自己和良质的距离非常遥远，因为他也正在用系统性的思考去界定良质，在良质旁边建立砖墙。「一旦想通过系统的思考去界定良质，就会破坏它最原始的目标，他所做的实在是一桩愚不可及的事。」他盯着卧室的墙壁看了三天三夜。思绪停顿，欲望止住。他开始扔东西，尿液流满地。"你必须要独自经过那死荫的幽谷"——他走过了这一段幽谷，走出神话，走出自我。"
            ),
            "viz": (
                '<div class="flow-row">'
                '<div class="flow-step">🏫 4堂课<br/>沉默<br/>学生惊慌</div>'
                '<div class="flow-arrow">→</div>'
                '<div class="flow-step">🏙️ 芝加哥<br/>= 形式+本质<br/>没有良质</div>'
                '<div class="flow-arrow">→</div>'
                '<div class="flow-step">⏳ 时间感<br/>消失<br/>思想停顿</div>'
                '<div class="flow-arrow">→</div>'
                '<div class="flow-step">🧱 3天3夜<br/>盯着墙壁<br/>意识瓦解</div>'
                '<div class="flow-arrow">→</div>'
                '<div class="flow-step end">🌑 死荫幽谷<br/>走出神话<br/>灵魂安息</div>'
                '</div>'
            ),
        },
        {
            "color": "#4f46e5", "tag": "觉醒",
            "title": "走出神话：良质终于被理解",
            "body": (
                "在意识瓦解的边缘，斐德洛获得了前所未有的理解。他明白，自己一直在用辩证法的体系去对抗辩证法——这本身就是矛盾。良质不能被界定，一旦用系统性的思考去界定它，就破坏了它最原始的目标。真正的了解不是通过概念和分类，而是通过直接的体验和直觉。走出神话、走出自我之后，他对自己说：「他曾经这样辛苦地保卫、牺牲，从来没有背叛过的良质，原来他从来不曾了解，现在却了然于心，他的灵魂得到安息了。」这种了解不是知识性的，而是存在性的——只有放下一切思维体系，才能真正触及良质。"
            ),
            "viz": (
                '<div class="quote-box">"他曾经这样辛苦地保卫、牺牲<br/>从来没有背叛过的<span style="font-weight:bold;color:#4f46e5;">良质</span><br/><br/>原来他从来不曾了解<br/><br/>现在却<span style="font-weight:bold;font-size:20px;color:#dc2626;">了然于心</span><br/><br/>他的灵魂<br/>得到<span style="font-weight:bold;color:#ea580c;">安息</span>了"</div>'
            ),
        },
        {
            "color": "#db2777", "tag": "当下",
            "title": "克里斯的眼泪：他怀念的是过去的自己",
            "body": (
                "回到旅途的当下。在黑暗的雨中，波西格和克里斯好不容易找到一间破败的汽车旅馆。克里斯突然问："什么时候回家？"他哭了起来，说出了多年的心结："当我小的时候，情形不是这样……我们总是一起做事情，都做我想做的事。现在我什么事都不想做。"他前后摇摆，脸埋在手里——这正是医院地板上斐德洛曾经的动作。他怀念的不是某个地方，而是过去的自己——那个曾经和父亲一起玩游戏、听故事、骑车出去的孩子。波西格问："我们离开芝加哥之前情况比较好吗？""是啊。""怎样好法？""很有意思。记得我们一起去找床的事吗？"——那个斐德洛精神错乱时六岁克里斯牵着父亲回家的记忆，对克里斯来说竟是"很有意思"。"
            ),
            "viz": (
                '<div class="flow-row">'
                '<div class="flow-step">🌧️ 雨中<br/>找到破旧<br/>汽车旅馆</div>'
                '<div class="flow-arrow">→</div>'
                '<div class="flow-step">😢 克里斯<br/>哭着问<br/>"什么时候回家"</div>'
                '<div class="flow-arrow">→</div>'
                '<div class="flow-step">🔄 前后摇摆<br/>脸埋在手里<br/>= 医院的姿势</div>'
                '<div class="flow-arrow">→</div>'
                '<div class="flow-step">💭 "我们离开<br/>芝加哥之前<br/>比较好"</div>'
                '<div class="flow-arrow">→</div>'
                '<div class="flow-step end">💔 他想念的是<br/>过去的自己<br/>不是某个地方</div>'
                '</div>'
            ),
        },
    ],
    "takeaway": (
        "第三十章是全书哲学探索与个人悲剧的交汇点。斐德洛在课堂上用两记精准的攻击击败了委员会主席——但胜利带来的不是凯旋，而是毁灭性的自我觉察：他发现自己正在用辩证法的武器去对抗辩证法，在良质旁边建立思维的砖墙。「一旦想通过系统的思考去界定良质，就会破坏它最原始的目标。」这个悖论将他推入了深渊：停止教学、抛弃一切、意识瓦解。然而正是在这个深渊——"死荫的幽谷"——中，他获得了真正的理解。不是在概念层面"知道"良质，而是在存在层面"成为"良质。他的灵魂得到安息。而旅馆里克里斯的哭声与那个"找床"的回忆，将两个时间维度拉到了一起：过去（精神错乱的斐德洛和六岁的克里斯）与现在（试图和解的波西格和十一岁的克里斯）——他们都曾失去自己，都在寻找回归的路。"
    ),
}

ch030_en = {
    "num": "Chapter 30",
    "title": "\"The Valley of the Shadow of Death — Phaedrus's Collapse and Awakening\"",
    "subtitle": "\"You must go through that valley of the shadow of death alone\" — Beyond myth, the soul finds rest",
    "overview": (
        "With the philosophy professor absent due to illness, the Committee Chairman takes over the class. Phaedrus confronts him directly — in a dialectical duel, he precisely points out that Socrates himself said \"this is a metaphor,\" causing the Chairman to lose face. But when the Chairman asks \"What is dialectics?\" Phaedrus answers that \"Dialectics comes before all else\" — the Chairman's own words from the Encyclopedia Britannica. The Chairman is shocked, enraged, interrupts — but cannot attack his own words. Yet Phaedrus's victory reveals an abyss: he realizes he is using systematic thinking to define Quality, which is itself a betrayal of Quality. He stops teaching, stares at a wall for three days and nights, discards all possessions, and walks alone through the \"valley of the shadow of death\" — beyond myth, beyond self, consciousness fully dissolving. From the brink of collapse, he gains an unprecedented understanding: the Quality he had so painstakingly defended and sacrificed for, without ever betraying, he had never truly understood — but now comprehends it fully, and his soul finds rest."
    ),
    "kpis": [
        ("2", "Points scored: rhetoric beats dialectics", "#dc2626"),
        ("3 days", "Staring at the wall: consciousness dissolves", "#ea580c"),
        ("4", "Silent classes: teaching stops", "#ca8a04"),
        ("1", "Unopenable door: the hospital", "#4f46e5"),
    ],
    "sections": [
        {
            "color": "#dc2626", "tag": "Duel",
            "title": "The Chairman Enters: Dialectics Hunts the Wolf",
            "body": (
                "The Chairman enters with a benevolent smile and an old pipe. He surveys each person with a nearly hypnotic gaze. The innocent student who was humiliated before has returned — to watch Phaedrus being hunted. Phaedrus has grown a beard; the Chairman does not recognize him at first. But Phaedrus is ready. When the Chairman lectures on Plato's Phaedrus, declaring that Socrates swore to the gods that the chariot and horses description is \"truth,\" Phaedrus raises his hand: \"All of this is just a metaphor. Socrates himself says it is a metaphor.\" The Chairman dares not check the text — if Phaedrus is right, he loses all face in class. Rhetoric scores one; dialectics zero."
            ),
            "viz": (
                '<div class="flow-row">'
                '<div class="flow-step">🎭 Chairman<br/>Benevolent smile<br/>Hypnotic gaze</div>'
                '<div class="flow-arrow">→</div>'
                '<div class="flow-step">📖 "Chariot & horses<br/>is TRUTH"<br/>Socrates swore</div>'
                '<div class="flow-arrow">→</div>'
                '<div class="flow-step">🐺 Phaedrus<br/>"Socrates says<br/>it\'s a metaphor"</div>'
                '<div class="flow-arrow">→</div>'
                '<div class="flow-step">😱 Chairman<br/>Dares not check<br/>Loses face</div>'
                '<div class="flow-arrow">→</div>'
                '<div class="flow-step end">🏆 Rhetoric 2<br/>Dialectics 0<br/>Round One</div>'
                '</div>'
            ),
        },
        {
            "color": "#ea580c", "tag": "Trap",
            "title": "The Trap Reversed: Dialectics Consumes Itself",
            "body": (
                "The Chairman, unwilling to lose, turns to Phaedrus: \"What is dialectics?\" — he wants to pull Phaedrus into his own territory. Phaedrus answers: \"As far as I know, Aristotle considers dialectics comes before all else.\" The Chairman's face shifts from gratitude to shock to fury — these are his own words from the Encyclopedia Britannica. He cannot attack Phaedrus for quoting his own view. Rhetoric scores again. The Chairman interrupts and ends the dialogue. Phaedrus thinks: if he were truly seeking truth, he wouldn't have interrupted. \"Dialectics comes before all else\" — this statement itself becomes a dialectical entity, subject to dialectical questioning. What is the evidence? None. Dialectics hangs in mid-air like Newton's laws, with nothing beneath it, yet claims to be the source of everything — \"What foolishness!\""
            ),
            "viz": (
                '<div class="dual-grid">'
                '<div class="dual-card yes">🎯 Phaedrus\'s Trap Reversal<br/>Chairman asks: What is dialectics?<br/>Phaedrus quotes Chairman\'s own words:<br/>"Dialectics comes before all else"<br/>Chairman\'s face:<br/>Gratitude→Shock→Fury<br/>Cannot attack his own words</div>'
                '<div class="dual-card no">🕳️ The Emptiness of Dialectics<br/>"Dialectics before all"<br/>→ No evidence<br/>→ Hangs in mid-air<br/>→ Claims to be source of all<br/>→ Historically & commonsensically<br/>  the source of dialectics is<br/>  Rhetoric→Myth→Poetry→Quality</div>'
                '</div>'
            ),
        },
        {
            "color": "#ca8a04", "tag": "Collapse",
            "title": "Consciousness Dissolves: Silent Classes and the Valley of Death",
            "body": (
                "Phaedrus notices he begins to fear the silence in the classroom. He starts teaching without saying a word — first one class, then two, then four classes of silence. Students panic. Thanksgiving arrives. It's all over. He walks through Chicago's streets — in his eyes, the city becomes \"the headquarters of form and substance\": bricks, cement, neon lights, no Quality. His sense of time gradually disappears. A thought strikes him — he realizes he is far from Quality because he too is using systematic thinking to define it, building brick walls around it. \"Once you attempt to define Quality through systematic thinking, you destroy its original purpose — what he was doing was the most foolish thing imaginable.\" He stares at the bedroom wall for three days and three nights. Thought stops. Desire stops. He begins throwing things away. Urine flows on the floor. \"You must go through the valley of the shadow of death alone\" — he walks through this valley, beyond myth, beyond self."
            ),
            "viz": (
                '<div class="flow-row">'
                '<div class="flow-step">🏫 4 classes<br/>Silence<br/>Students panic</div>'
                '<div class="flow-arrow">→</div>'
                '<div class="flow-step">🏙️ Chicago<br/>= Form + Substance<br/>No Quality</div>'
                '<div class="flow-arrow">→</div>'
                '<div class="flow-step">⏳ Time sense<br/>disappears<br/>Thought stops</div>'
                '<div class="flow-arrow">→</div>'
                '<div class="flow-step">🧱 3 days/nights<br/>Staring at wall<br/>Consciousness dissolves</div>'
                '<div class="flow-arrow">→</div>'
                '<div class="flow-step end">🌑 Valley of Death<br/>Beyond myth<br/>Soul finds rest</div>'
                '</div>'
            ),
        },
        {
            "color": "#4f46e5", "tag": "Awakening",
            "title": "Beyond Myth: Quality Finally Understood",
            "body": (
                "At the edge of consciousness dissolution, Phaedrus gains unprecedented understanding. He realizes he has been using the dialectical system to fight against dialectics — this itself is a contradiction. Quality cannot be defined; once you attempt to define it through systematic thinking, you destroy its original purpose. True understanding comes not through concepts and classifications, but through direct experience and intuition. Having walked beyond myth, beyond self, he tells himself: \"The Quality he had so painstakingly defended, sacrificed for, and never betrayed — he had never truly understood, but now comprehends it fully, and his soul finds rest.\" This understanding is not intellectual but existential — only by letting go of all thought-systems can one truly touch Quality."
            ),
            "viz": (
                '<div class="quote-box">"The <span style="font-weight:bold;color:#4f46e5;">Quality</span> he had<br/>so painstakingly defended<br/>sacrificed for, never betrayed<br/><br/>he had never truly understood<br/><br/>but now <span style="font-weight:bold;font-size:20px;color:#dc2626;">comprehends it fully</span><br/><br/>his soul<br/>finds <span style="font-weight:bold;color:#ea580c;">rest</span>"</div>'
            ),
        },
        {
            "color": "#db2777", "tag": "Present",
            "title": "Chris's Tears: He Misses His Former Self",
            "body": (
                "Back to the journey's present. In the dark rain, Pirsig and Chris barely find a shabby motel. Chris suddenly asks: \"When are we going home?\" He bursts into tears, revealing years of buried feelings: \"When I was little, it wasn't like this... We always did things together, things I wanted to do. Now I don't want to do anything.\" He rocks back and forth, face buried in hands — the exact gesture Phaedrus made on the hospital floor. He misses not a place, but his former self — the child who once played games, listened to stories, and rode out with his father. Pirsig asks: \"Was it better before we left Chicago?\" \"Yes.\" \"How was it better?\" \"It was interesting. Remember when we went looking for beds?\" — the memory of six-year-old Chris leading his insane father home, which to Chris was \"interesting.\""
            ),
            "viz": (
                '<div class="flow-row">'
                '<div class="flow-step">🌧️ In rain<br/>Find shabby<br/>motel</div>'
                '<div class="flow-arrow">→</div>'
                '<div class="flow-step">😢 Chris cries<br/>"When are we<br/>going home?"</div>'
                '<div class="flow-arrow">→</div>'
                '<div class="flow-step">🔄 Rocks back<br/>Face in hands<br/>= Hospital gesture</div>'
                '<div class="flow-arrow">→</div>'
                '<div class="flow-step">💭 "It was better<br/>before we left<br/>Chicago"</div>'
                '<div class="flow-arrow">→</div>'
                '<div class="flow-step end">💔 He misses<br/>his former self<br/>not a place</div>'
                '</div>'
            ),
        },
    ],
    "takeaway": (
        "Chapter 30 is the intersection of the book's philosophical inquiry and personal tragedy. Phaedrus defeats the Committee Chairman with two precise attacks in class — but victory brings not triumph, but a devastating self-awareness: he realizes he is using the weapons of dialectics against dialectics, building brick walls of thought around Quality. \"Once you attempt to define Quality through systematic thinking, you destroy its original purpose.\" This paradox pushes him into the abyss: stop teaching, discard everything, consciousness dissolves. Yet it is in this abyss — \"the valley of the shadow of death\" — that he gains true understanding. Not \"knowing\" Quality at a conceptual level, but \"being\" Quality at an existential level. His soul finds rest. And Chris's tears in the motel, with that memory of \"looking for beds,\" pull together two time dimensions: the past (insane Phaedrus with six-year-old Chris) and the present (Pirsig attempting reconciliation with eleven-year-old Chris) — both lost themselves, both seeking the way back."
    ),
}

# =============================================
# Chapter 31 data
# =============================================
ch031_zh = {
    "num": "第三十一章",
    "title": "「海崖之上——『我』就是斐德洛」",
    "subtitle": "「你真的精神错乱过？」——「没有！」——「我就知道。」",
    "overview": (
        "全书情感最密集的章节。蛞蝓爬满的潮湿清晨，克里斯持续的愤怒和沉默——他站在百英尺高的海崖边上不肯回来，父子之间的对立达到了顶峰。克里斯想回家，想找回过去的父亲——那个曾经和他玩游戏、讲故事、一起骑车出去的父亲。在悬崖边的雾中，波西格终于对克里斯说出了从未说出的真相：他曾经精神错乱，现在可能又要发病了，他必须把克里斯送回家。克里斯放声痛哭——哭声很奇怪，「好像从很遥远的地方传来」。而就在这一刻，所有的拼图终于合上：克里斯问出了那个梦——"那扇玻璃门！难道你不记得？"波西格被电击了一般——他从来没有告诉过克里斯那个梦。他明白了：那扇打不开的门是医院的门。"我就是斐德洛，我就是他，他们因为我说实话而想把我给毁了。""
    ),
    "kpis": [
        ("30 分钟", "崖边僵持：父与子的耐心战争", "#dc2626"),
        ("1 扇", "玻璃门：克里斯的梦", "#ea580c"),
        ("1 只", "绿蛞蝓：潮湿的疏离", "#ca8a04"),
        ("1 句", "「我就知道」——释怀", "#4f46e5"),
    ],
    "sections": [
        {
            "color": "#dc2626", "tag": "疏离",
            "title": "蛞蝓之晨：潮湿的沉默与崖边的危险",
            "body": (
                "清晨醒来，地上爬满了绿色的蛞蝓——又长又软，全身覆盖着黏液。克里斯对这个奇异景象毫无反应。一路上，他持续冷淡、沉默、闷闷不乐。在莱吉特喂鸭子时，脸上是「最不快乐的神情」。当他们停在海崖边，克里斯径直走到离悬崖边极近的地方——至少一百英尺高。波西格大喊他的名字，冲过去一把抓住他的衬衫把他拉回来。克里斯用"很奇怪的眼神"瞄了他一眼。这种眼神——不是愤怒、不是恐惧——而是一种疏离的、将父亲视为陌生人的凝视。"
            ),
            "viz": (
                '<div class="flow-row">'
                '<div class="flow-step">🐌 蛞蝓<br/>爬满地面<br/>潮湿疏离</div>'
                '<div class="flow-arrow">→</div>'
                '<div class="flow-step">🦆 喂鸭子<br/>"最不快乐<br/>的神情"</div>'
                '<div class="flow-arrow">→</div>'
                '<div class="flow-step">🌊 百英尺<br/>海崖边上<br/>不肯回来</div>'
                '<div class="flow-arrow">→</div>'
                '<div class="flow-step">👀 奇怪的<br/>眼神<br/>视父为陌生人</div>'
                '<div class="flow-arrow">→</div>'
                '<div class="flow-step end">⚔️ 父子<br/>对立<br/>到达顶峰</div>'
                '</div>'
            ),
        },
        {
            "color": "#ea580c", "tag": "僵持",
            "title": "崖边的耐心战争：三十分钟的沉默对峙",
            "body": (
                "波西格拿出克里斯的衣服，让他穿上。克里斯迟迟不肯穿——十分钟过去了，十五分钟过去了。「我们似乎在比赛耐性。」吹了三十分钟冷风之后，克里斯问："我们要往哪里走？""往南，沿着海岸走。""我们回去吧。""回比较温暖的地方。"这样又要骑好几百英里。波西格说不行。克里斯不肯，坐在地上。又过了十五分钟，"骑摩托车的人不是你，是我。我们要往南走。"波西格快要爆发了——克里斯的反抗不是为了回家，而是为了激怒他。克里斯想恨他——因为父亲不是他理想中的父亲。这是全书最赤裸的父子冲突：不是关于方向，而是关于认同。"
            ),
            "viz": (
                '<div class="flow-row">'
                '<div class="flow-step">🧥 拿出衣服<br/>克里斯<br/>不肯穿</div>'
                '<div class="flow-arrow">→</div>'
                '<div class="flow-step">⏱️ 10分钟<br/>15分钟<br/>30分钟</div>'
                '<div class="flow-arrow">→</div>'
                '<div class="flow-step">🗣️ "我们回去吧"<br/>"不行"<br/>"我要回去"</div>'
                '<div class="flow-arrow">→</div>'
                '<div class="flow-step">😤 波西格<br/>快要爆发<br/>"骑车的不是你"</div>'
                '<div class="flow-arrow">→</div>'
                '<div class="flow-step end">🐺 克里斯<br/>想恨父亲<br/>因为父亲<br/>不是他</div>'
                '</div>'
            ),
        },
        {
            "color": "#ca8a04", "tag": "坦白",
            "title": "雾中坦白：说出从未说出的真相",
            "body": (
                "在一座可以俯瞰海洋的高崖上，四周浓雾弥漫。波西格感到"该发生的事还是必然会发生"。他说出了从未对克里斯说过的话："克里斯，你眼前的父亲曾经精神错乱过好长一段时间，现在他又快要发病了。"不是"快要发病"——根本已经发病了。像海一样深。他要把克里斯送回家，因为害怕继续旅行不知道会发生什么。"我现在就要和你说再见。克里斯，我不确定我们是否还会再相见。"这段话的每一个字都在撕开父子之间那道从未愈合的伤口——波西格在承认他就是斐德洛，斐德洛正在回来。"
            ),
            "viz": (
                '<div class="quote-box">🌫️ 雾中高崖之上<br/><br/>"克里斯，你眼前的父亲<br/><span style="font-weight:bold;color:#dc2626;">曾经精神错乱过</span><br/>好长一段时间<br/><br/>现在他又<span style="font-weight:bold;color:#ea580c;">快要发病了</span>"<br/><br/>"我不确定<br/>我们是否还会<span style="font-weight:bold;color:#4f46e5;">再相见</span>"</div>'
            ),
        },
        {
            "color": "#4f46e5", "tag": "拼图",
            "title": "玻璃门之谜：梦的拼图终于完整",
            "body": (
                "克里斯放声痛哭——哭声很奇怪，「好像从很遥远的地方传来」，「几乎不像人在哭，而像一个遥远的水妖。」"他问了一个让波西格如被电击的问题："你为什么离开我们？""什么时候？""在医院的时候！""难道他们不让你出来吗？""那么，你为什么不开门？""那扇玻璃门！难道你不记得？"波西格从来没有告诉过克里斯那个梦——在梦里，克里斯站在玻璃门的一边，斐德洛站在另一边，门打不开。克里斯竟然梦到了一模一样的东西。波西格明白了：那扇门是在医院里，那是他最后一次看到他们。"我就是斐德洛，我就是他，他们因为我说实话而想把我给毁了。这一切都对上了。""
            ),
            "viz": (
                '<div class="flow-row">'
                '<div class="flow-step">😭 克里斯<br/>放声痛哭<br/>水妖般的哭声</div>'
                '<div class="flow-arrow">→</div>'
                '<div class="flow-step">❓ "你为什么<br/>离开我们？"<br/>"在医院时!"</div>'
                '<div class="flow-arrow">→</div>'
                '<div class="flow-step">🚪 "那扇<br/>玻璃门！<br/>难道你不记得？"</div>'
                '<div class="flow-arrow">→</div>'
                '<div class="flow-step">⚡ 波西格<br/>被电击<br/>他从未说过那个梦</div>'
                '<div class="flow-arrow">→</div>'
                '<div class="flow-step end">🧩 拼图完整<br/>"我就是斐德洛"<br/>那扇门=医院之门</div>'
                '</div>'
            ),
        },
        {
            "color": "#db2777", "tag": "释怀",
            "title": "「我就知道」：克里斯的释怀与重生的阳光",
            "body": (
                "雾逐渐散去。克里斯哭了很久，哭声从水妖般的嚎叫变为人的啜泣。波西格给他一块破布擦脸。克里斯眼中多年来一直存在的恐惧，终于找到了出口。他们收拾好东西，放上摩托车。雾突然散去了，阳光照在克里斯脸上——波西格看到了"以前从未见过的表情"。克里斯戴上头盔，系上带子，抬起头来：\n\n"你真的精神错乱过？"\n\n他为什么这样问呢？\n\n"没有！"\n\n他吃了一惊，但是眼睛里闪烁着光芒。\n\n"我就知道。"他说。然后他爬上摩托车，他们出发了。\n\n这四个字——"我就知道"——卸下了克里斯多年的重担。他早就知道，只是需要亲耳听到父亲说"没有"。而波西格说"没有"，不是因为撒谎，而是因为他们已经成为了同一个人——不需要再分开。"
            ),
            "viz": (
                '<div class="quote-box">🌤️ 雾散去了<br/>阳光照在克里斯脸上<br/><br/>"你真的<span style="font-weight:bold;color:#dc2626;">精神错乱过</span>？"<br/><br/>"<span style="font-weight:bold;font-size:20px;color:#4f46e5;">没有！</span>"<br/><br/>他吃了一惊<br/>但是眼睛里<span style="font-weight:bold;color:#ea580c;">闪烁着光芒</span><br/><br/>"<span style="font-weight:bold;font-size:22px;">我就知道</span>。"</div>'
            ),
        },
    ],
    "takeaway": (
        "第三十一章是全书情感的高潮与哲学探索的最终落地——不再是关于柏拉图或亚里士多德，而是关于一个父亲和一个儿子之间那道从未愈合的伤口。克里斯站在海崖边不肯回来，不是因为他想回家，而是因为他在寻找那个已经消失的父亲。波西格在雾中说出真相——他曾经精神错乱，斐德洛正在回来——这既是坦白，也是承认。"我就是斐德洛。"而克里斯问出的那个问题——"那扇玻璃门！"——将全书关于分裂、对立、二分法的哲学主题具象化为一道真实存在的、父亲打不开的门。当克里斯得到"没有"的回答时，他等的不是事实（他知道真相），而是父亲的回归——一个完整的、不再分裂的父亲的回归。他们出发的时候，阳光照在克里斯脸上，那是全书第一次真正意义上的"和解"。"
    ),
}

ch031_en = {
    "num": "Chapter 31",
    "title": "\"Above the Sea Cliff — 'I' Am Phaedrus\"",
    "subtitle": "\"Did you really go crazy?\" — \"No!\" — \"I knew it.\"",
    "overview": (
        "The most emotionally intense chapter in the entire book. A damp morning crawling with green slugs, Chris's sustained anger and silence — he stands at the edge of a hundred-foot sea cliff refusing to come back. The father-son opposition reaches its peak. Chris wants to go home, wants to find his former father — the one who played games with him, told him stories, and rode out together. In the fog at the cliff's edge, Pirsig finally tells Chris the truth he has never spoken: he was once insane, he may be breaking down again, he must send Chris home. Chris bursts into tears — his crying sounds strange, \"like it came from somewhere far away.\" And at this moment, all the puzzle pieces finally fit: Chris asks about the dream — \"That glass door! Don't you remember?\" Pirsig feels like he's been struck by lightning — he never told Chris that dream. He understands: that unopenable door was the hospital door. \"I am Phaedrus, I am he, and they tried to destroy me for telling the truth.\""
    ),
    "kpis": [
        ("30 min", "Cliff standoff: father-son patience war", "#dc2626"),
        ("1", "Glass door: Chris's dream", "#ea580c"),
        ("1", "Green slug: damp alienation", "#ca8a04"),
        ("1", "\"I knew it\" — release", "#4f46e5"),
    ],
    "sections": [
        {
            "color": "#dc2626", "tag": "Alienation",
            "title": "Morning of Slugs: Damp Silence and Cliffside Danger",
            "body": (
                "Waking in the morning, the ground is crawling with green slugs — long and soft, covered in mucus. Chris shows no reaction to this strange sight. All along the way, he remains cold, silent, sullen. Feeding ducks at Leggett, he wears \"the unhappiest expression I have ever seen.\" When they stop at the sea cliff, Chris walks right to the edge — at least a hundred feet high. Pirsig shouts his name, runs over, grabs his shirt and pulls him back. Chris glances at him with \"a very strange look\" — not anger, not fear, but a gaze of alienation, as if seeing his father as a stranger."
            ),
            "viz": (
                '<div class="flow-row">'
                '<div class="flow-step">🐌 Slugs<br/>Crawling everywhere<br/>Damp alienation</div>'
                '<div class="flow-arrow">→</div>'
                '<div class="flow-step">🦆 Feeding ducks<br/>"Unhappiest<br/>expression ever"</div>'
                '<div class="flow-arrow">→</div>'
                '<div class="flow-step">🌊 100-foot<br/>cliff edge<br/>Won\'t come back</div>'
                '<div class="flow-arrow">→</div>'
                '<div class="flow-step">👀 Strange<br/>look<br/>Father as stranger</div>'
                '<div class="flow-arrow">→</div>'
                '<div class="flow-step end">⚔️ Father-son<br/>opposition<br/>at its peak</div>'
                '</div>'
            ),
        },
        {
            "color": "#ea580c", "tag": "Standoff",
            "title": "The Patience War: Thirty Minutes of Silent Confrontation",
            "body": (
                "Pirsig takes out Chris's clothes and tells him to put them on. Chris refuses — ten minutes pass, then fifteen. \"We seemed to be competing in patience.\" After thirty minutes of cold wind, Chris asks: \"Where are we going?\" \"South, along the coast.\" \"Let's go back.\" \"Back to warmer places.\" That would be hundreds of miles. Pirsig says no. Chris refuses, sitting on the ground. After another fifteen minutes: \"I'm the one riding the motorcycle, not you. We're going south.\" Pirsig is about to explode — Chris's rebellion is not about going home, but about provoking him. Chris wants to hate him — because his father is not the father he wants. This is the book's most naked father-son conflict: not about direction, but about identity."
            ),
            "viz": (
                '<div class="flow-row">'
                '<div class="flow-step">🧥 Takes out<br/>clothes<br/>Chris refuses</div>'
                '<div class="flow-arrow">→</div>'
                '<div class="flow-step">⏱️ 10 min<br/>15 min<br/>30 min</div>'
                '<div class="flow-arrow">→</div>'
                '<div class="flow-step">🗣️ "Let\'s go back"<br/>"No"<br/>"I want to go back"</div>'
                '<div class="flow-arrow">→</div>'
                '<div class="flow-step">😤 Pirsig<br/>About to explode<br/>"I\'m riding, not you"</div>'
                '<div class="flow-arrow">→</div>'
                '<div class="flow-step end">🐺 Chris<br/>Wants to hate<br/>His father<br/>is not him</div>'
                '</div>'
            ),
        },
        {
            "color": "#ca8a04", "tag": "Confession",
            "title": "Confession in the Fog: Speaking the Unspoken Truth",
            "body": (
                "On a high cliff overlooking the ocean, thick fog surrounds them. Pirsig feels \"what must happen will happen.\" He speaks the words never before spoken to Chris: \"Chris, the father before your eyes was once insane for a long time, and now he is about to break down again.\" Not \"about to\" — already breaking down. As deep as the sea. He must send Chris home because he is afraid of what might happen if they continue traveling together. \"I'm saying goodbye now. Chris, I'm not sure we will see each other again.\" Every word tears open the wound between father and son that has never healed — Pirsig is admitting he IS Phaedrus, and Phaedrus is returning."
            ),
            "viz": (
                '<div class="quote-box">🌫️ Above the cliff in fog<br/><br/>"Chris, the father before your eyes<br/><span style="font-weight:bold;color:#dc2626;">was once insane</span><br/>for a long time<br/><br/>and now he is<br/><span style="font-weight:bold;color:#ea580c;">about to break down again</span>"<br/><br/>"I\'m not sure<br/>we will <span style="font-weight:bold;color:#4f46e5;">see each other again</span>"</div>'
            ),
        },
        {
            "color": "#4f46e5", "tag": "Puzzle",
            "title": "The Glass Door Mystery: The Dream Puzzle Becomes Complete",
            "body": (
                "Chris bursts into tears — his crying sounds strange, \"like it came from somewhere far away,\" \"almost not human, like a distant water spirit.\" He asks a question that strikes Pirsig like lightning: \"Why did you leave us?\" \"When?\" \"At the hospital!\" \"Wouldn't they let you out?\" \"Then why didn't you open the door?\" \"That glass door! Don't you remember?\" Pirsig has never told Chris about that dream — the dream where Chris stood on one side of a glass door and Phaedrus on the other, and the door would not open. Chris dreamed the exact same thing. Pirsig understands: that door was in a hospital, it was the last time he saw them. \"I am Phaedrus, I am he, and they tried to destroy me for telling the truth. It all fits together.\""
            ),
            "viz": (
                '<div class="flow-row">'
                '<div class="flow-step">😭 Chris<br/>Wails<br/>Water-spirit cry</div>'
                '<div class="flow-arrow">→</div>'
                '<div class="flow-step">❓ "Why did you<br/>leave us?"<br/>"At the hospital!"</div>'
                '<div class="flow-arrow">→</div>'
                '<div class="flow-step">🚪 "That glass<br/>door! Don\'t you<br/>remember?"</div>'
                '<div class="flow-arrow">→</div>'
                '<div class="flow-step">⚡ Pirsig<br/>Struck by lightning<br/>Never told the dream</div>'
                '<div class="flow-arrow">→</div>'
                '<div class="flow-step end">🧩 Puzzle complete<br/>"I am Phaedrus"<br/>Door = hospital door</div>'
                '</div>'
            ),
        },
        {
            "color": "#db2777", "tag": "Release",
            "title": "\"I Knew It\": Chris's Release and the Sunshine of Rebirth",
            "body": (
                "The fog gradually disperses. Chris cries for a long time, his sobs shifting from water-spirit wails to human weeping. Pirsig gives him a torn cloth to wipe his face. The fear that has been in Chris's eyes for all these years finally finds an outlet. They pack up and put things on the motorcycle. The fog suddenly lifts, and sunlight falls on Chris's face — Pirsig sees \"an expression I had never seen before.\" Chris puts on his helmet, fastens the strap, looks up:\n\n\"Did you really go crazy?\"\n\nWhy does he ask this?\n\n\"No!\"\n\nHe looks surprised, but his eyes sparkle.\n\n\"I knew it,\" he says. Then he climbs onto the motorcycle, and they set off.\n\nThese three words — \"I knew it\" — lift years of burden from Chris. He always knew; he just needed to hear his father say \"No.\" And Pirsig says \"No\" not because he is lying, but because they have become the same person — no need to separate anymore."
            ),
            "viz": (
                '<div class="quote-box">🌤️ The fog lifts<br/>Sunlight on Chris\'s face<br/><br/>"Did you really<br/><span style="font-weight:bold;color:#dc2626;">go crazy?</span>"<br/><br/>"<span style="font-weight:bold;font-size:20px;color:#4f46e5;">No!</span>"<br/><br/>He looks surprised<br/>but his eyes <span style="font-weight:bold;color:#ea580c;">sparkle</span><br/><br/>"<span style="font-weight:bold;font-size:22px;">I knew it.</span>"</div>'
            ),
        },
    ],
    "takeaway": (
        "Chapter 31 is the emotional climax of the entire book and the ultimate landing of its philosophical inquiry — no longer about Plato or Aristotle, but about a wound between a father and son that has never healed. Chris stands at the cliff edge refusing to come back, not because he wants to go home, but because he is searching for the father who has disappeared. Pirsig speaks the truth in the fog — he was once insane, Phaedrus is returning — and this is both confession and admission. \"I am Phaedrus.\" And the question Chris asks — \"That glass door!\" — concretizes the book's philosophical themes of division, opposition, and dualism into a real, physical door that the father could not open. When Chris receives the answer \"No,\" what he is waiting for is not the fact (he knows the truth) but the father's return — the return of a whole, undivided father. When they set off, sunlight falls on Chris's face — the first true moment of \"reconciliation\" in the entire book."
    ),
}

# =============================================
# Chapter 32 data
# =============================================
ch032_zh = {
    "num": "第三十二章",
    "title": "「后视之外——我们赢了」",
    "subtitle": "「试炼永远没有了结……但我们赢了。情况正在慢慢好起来。」",
    "overview": (
        "全书最短的尾声，也是最温柔的章节。克里斯第一次从父亲背后站起身来，站在脚踏板上越过他的肩膀看到了不一样的风景——「所有的一切都变了」。这不仅是物理视角的改变，更是心理视角的转变：他不再是被动坐在后座的孩子，而是主动参与旅程的人。他问父亲自己长大后能否拥有一辆摩托车——这是对未来的期许，也是全书"传承"主题的体现。波西格的回答凝练了全书积攒的全部智慧："如果你有正确的态度就不难。事实上难的是要有正确的态度。"摩托车载着他们穿越加州的原野、树林与城市，向旧金山驶去。最后一段话成为全书的收束："试炼永远没有了结……但我现在有一种以前没有过的感觉……我们赢了。情况正在慢慢好起来。我们几乎可以这样期待。""
    ),
    "kpis": [
        ("1 次", "起身：越过父亲的肩膀", "#dc2626"),
        ("1 辆", "摩托车：未来的传承", "#ea580c"),
        ("1 句", "「我们赢了」", "#ca8a04"),
        ("∞", "试炼永远没有了结", "#4f46e5"),
    ],
    "sections": [
        {
            "color": "#dc2626", "tag": "视角",
            "title": "站在脚踏板上的视野：世界从此不同",
            "body": (
                "沿着曼扎尼塔海岸前行，克里斯第一次从座位上站起身来——他在脚踏板上越过父亲的肩膀，看到了不一样的风景。"所有的一切都变了。以前都不能越过你的肩看出去。"树枝在阳光下摆出奇怪而美丽的图案，忽明忽暗地闪过。克里斯发出一连串惊叹——"喔！""啊！""哇！"他不再是那个被挡在后座、只能看到父亲背影的孩子了。这个简单的动作——站起来——是全书的转折点：克里斯开始拥有自己的视野，自己的旅程。"
            ),
            "viz": (
                '<div class="flow-row">'
                '<div class="flow-step">🏍️ 克里斯<br/>站在脚踏板上<br/>越过父亲肩膀</div>'
                '<div class="flow-arrow">→</div>'
                '<div class="flow-step">🌳 "所有的一切<br/>都变了"<br/>树枝图案闪过</div>'
                '<div class="flow-arrow">→</div>'
                '<div class="flow-step">😲 "喔！"<br/>"啊！"<br/>"哇！"</div>'
                '<div class="flow-arrow">→</div>'
                '<div class="flow-step">👁️ 自己的<br/>视野<br/>自己的旅程</div>'
                '<div class="flow-arrow">→</div>'
                '<div class="flow-step end">🔄 全书转折<br/>从后座被动<br/>到主动参与</div>'
                '</div>'
            ),
        },
        {
            "color": "#ea580c", "tag": "传承",
            "title": "「等我长大可以有一辆摩托车吗？」——未来的期许",
            "body": (
                "克里斯重新坐下来，问了一个充满希望的问题——全书第一次面向未来的问题："等我长大可以有一辆摩托车吗？""如果你会照顾它的话。""那要怎样照顾呢？""要做许多事情。你看我一直做的就是。""你会全部教我吗？""当然。""很难吗？""如果你有正确的态度就不难。事实上难的是要有正确的态度。"这段对话是全书的浓缩——不是关于摩托车的技术问题，而是关于生活、关于良质、关于正确的态度。父亲终于可以回答儿子的问题了——不是逃避、不是发疯、不是在墙的另一边。"
            ),
            "viz": (
                '<div class="quote-box">"等我长大<br/>可以有一辆<span style="font-weight:bold;color:#ea580c;">摩托车</span>吗？"<br/><br/>"如果你会<span style="font-weight:bold;color:#dc2626;">照顾</span>它的话"<br/><br/>"你会全部教我吗？"<br/>"<span style="font-weight:bold;color:#4f46e5;">当然</span>"<br/><br/>"<span style="font-weight:bold;font-size:18px;color:#ca8a04;">难的是要有正确的态度</span>"</div>'
            ),
        },
        {
            "color": "#ca8a04", "tag": "智慧",
            "title": "「难的是要有正确的态度」——全书智慧的结晶",
            "body": (
                "这一句话凝结了全书全部的哲学探索。不是维修摩托车的技术有多复杂，而是态度——那种怀着良质去做每一件事的态度——才是真正困难的东西。正确的态度不能被传授为规则或方法（那正是亚里士多德的失败），也不能被定义为理念或形式（那是柏拉图的陷阱）。正确的态度只能在行动中体验、在旅程中培养、在人与世界的关系中自然而然地产生。克里斯问"我会有正确的态度吗？"波西格回答"我想会吧，我想不会有任何问题。"——这是全书最轻柔的许诺，也是一个父亲对儿子最本质的信任。"
            ),
            "viz": (
                '<div class="flow-row">'
                '<div class="flow-step">🔧 技术<br/>不难<br/>可传授</div>'
                '<div class="flow-arrow">→</div>'
                '<div class="flow-step">🧠 态度<br/>才是<br/>真正的困难</div>'
                '<div class="flow-arrow">→</div>'
                '<div class="flow-step">📏 不能列为<br/>规则/方法<br/>(非亚里士多德)</div>'
                '<div class="flow-arrow">→</div>'
                '<div class="flow-step">💡 不能定义<br/>为理念/形式<br/>(非柏拉图)</div>'
                '<div class="flow-arrow">→</div>'
                '<div class="flow-step end">⭐ 只能在<br/>行动中体验<br/>旅程中培养</div>'
                '</div>'
            ),
        },
        {
            "color": "#4f46e5", "tag": "旅程",
            "title": "穿越加州：从荒野到城市，从分裂到完整",
            "body": (
                "他们收起头盔——"在这种天气里是不需要戴头盔的。"克里斯注意到父亲也没有戴，就要把自己的也收起来。这是一个平等的信号：他们不再是指令者与服从者的关系，而是一起旅行的伙伴。他们穿越尤凯亚、霍普兰、克洛弗代尔，来到美酒的家乡。高速公路变得宽阔，车流增加，住宅和海湾出现在路旁。摩托车载着他们驶向旧金山——那个旅程的终点，也是新生活的起点。"我们几乎横跨过半个大陆的摩托车依然低低地吼着"——这辆摩托车已经不再只是机器，它是穿越荒野与心灵、穿越过去与现在的见证者。"
            ),
            "viz": (
                '<div class="flow-row">'
                '<div class="flow-step">🪖 摘下<br/>头盔<br/>平等伙伴</div>'
                '<div class="flow-arrow">→</div>'
                '<div class="flow-step">🍷 穿越<br/>尤凯亚·霍普兰<br/>美酒之乡</div>'
                '<div class="flow-arrow">→</div>'
                '<div class="flow-step">🛣️ 高速公路<br/>变宽<br/>车流增加</div>'
                '<div class="flow-arrow">→</div>'
                '<div class="flow-step">🏠 住宅<br/>船只<br/>海湾出现</div>'
                '<div class="flow-arrow">→</div>'
                '<div class="flow-step end">🏍️ 摩托车<br/>低低吼着<br/>横跨半个大陆</div>'
                '</div>'
            ),
        },
        {
            "color": "#db2777", "tag": "终章",
            "title": "「我们赢了」——试炼不息，希望不灭",
            "body": (
                "全书最后一句话，充满了前所未有的平静与力量："当然，试炼永远没有了结，人只要活着就会发生不愉快的事和不幸的事。但是我现在有一种以前没有过的感觉，这种感觉并不只停留在表面，而是深入内里：我们赢了。情况正在慢慢好起来。我们几乎可以这样期待。"这不是虚假的乐观主义——波西格承认试炼永无止尽，不幸和痛苦不会消失。但这种感觉"深入内里"，不是表面的愉快，而是存在层面的确信。全书从一个寻找自我的人开始，以两个人的"我们"告终——父亲和儿子、叙述者和斐德洛、理性与良质，不再对立，不再分裂。"我们几乎可以这样期待"——这个"几乎"带着全部的诚实，也带着全部的希望。"
            ),
            "viz": (
                '<div class="quote-box" style="background:#fef2f2;border-color:#fecaca;color:#991b1b;">📖 <span style="font-weight:bold;font-size:18px;color:#dc2626;">全书终章</span><br/><br/>"试炼<span style="font-weight:bold;">永远没有了结</span><br/>人只要活着<br/>就会发生不愉快的事<br/>和不幸的事<br/><br/>但是我<span style="font-weight:bold;font-size:20px;color:#dc2626;">现在有一种<br/>以前没有过的感觉</span><br/><br/>这种感觉并不只停留在表面<br/>而是<span style="font-weight:bold;color:#4f46e5;">深入内里</span>：<br/><br/><span style="font-weight:bold;font-size:24px;color:#ea580c;">我们赢了。</span><br/>情况正在慢慢好起来。<br/>我们几乎可以这样期待。"</div>'
            ),
        },
    ],
    "takeaway": (
        "第三十二章是全书的尾声，也是最温柔的收束。在经历了二十九章的哲学探索、情感撕裂、疯狂与觉醒之后，波西格给了读者——以及克里斯——一份安静的礼物。克里斯第一次站在摩托车脚踏板上越过父亲的肩膀看世界，这是全书最美的意象：不再被遮挡、不再被动、不再只能看到背影。他问能不能有一辆自己的摩托车——这是对未来、对传承、对继续活下去的期待。而波西格的回答"难的是要有正确的态度"是全书的哲学总结：良质不在规则里、不在定义里、不在理念里——它在态度里，在行动里，在人与世界每一刻的关系里。从"我"到"我们"——全书最后一个词的转变，是这场横跨半个大陆的奥德赛之旅的真正终点。不是问题被解决了，而是分裂被愈合了。"
    ),
}

ch032_en = {
    "num": "Chapter 32",
    "title": "\"Beyond the Rear View — We Have Won\"",
    "subtitle": "\"Trials never end... But we have won. Things are getting better.\"",
    "overview": (
        "The shortest and gentlest chapter in the book. For the first time, Chris stands up from behind his father, on the foot pegs, looking over his shoulder — \"Everything is different.\" This is not just a change of physical perspective but a shift of psychological perspective: he is no longer a passive child sitting in the back seat, but an active participant in the journey. He asks his father if he can have a motorcycle when he grows up — a question looking toward the future, embodying the book's theme of inheritance. Pirsig's answer crystallizes all the wisdom accumulated throughout the book: \"If you have the right attitude, it's not hard. In fact, what's hard is having the right attitude.\" The motorcycle carries them through California's fields, forests, and cities toward San Francisco. The final paragraph becomes the book's closing chord: \"Trials never end... But I have a feeling now that I've never had before... We have won. Things are getting better. We can almost expect it.\""
    ),
    "kpis": [
        ("1", "Standing up: over father's shoulder", "#dc2626"),
        ("1", "Motorcycle: future inheritance", "#ea580c"),
        ("1", "\"We have won\"", "#ca8a04"),
        ("∞", "Trials never end", "#4f46e5"),
    ],
    "sections": [
        {
            "color": "#dc2626", "tag": "Perspective",
            "title": "Standing on the Foot Pegs: The World Is Different Now",
            "body": (
                "Riding along the Manzanita coast, Chris stands up from the seat for the first time — on the foot pegs, looking over his father's shoulder, he sees a different landscape. \"Everything is different. I could never see over your shoulder before.\" Tree branches cast strange and beautiful patterns in the sunlight, flashing light and dark. Chris lets out a series of exclamations — \"Oh!\" \"Ah!\" \"Wow!\" He is no longer the child blocked in the back seat, seeing only his father's back. This simple act — standing up — is the turning point of the entire book: Chris begins to have his own view, his own journey."
            ),
            "viz": (
                '<div class="flow-row">'
                '<div class="flow-step">🏍️ Chris<br/>Stands on pegs<br/>Over father\'s shoulder</div>'
                '<div class="flow-arrow">→</div>'
                '<div class="flow-step">🌳 "Everything<br/>is different"<br/>Branch patterns flash</div>'
                '<div class="flow-arrow">→</div>'
                '<div class="flow-step">😲 "Oh!"<br/>"Ah!"<br/>"Wow!"</div>'
                '<div class="flow-arrow">→</div>'
                '<div class="flow-step">👁️ His own<br/>view<br/>His own journey</div>'
                '<div class="flow-arrow">→</div>'
                '<div class="flow-step end">🔄 Book\'s turning point<br/>From passive passenger<br/>To active participant</div>'
                '</div>'
            ),
        },
        {
            "color": "#ea580c", "tag": "Inheritance",
            "title": "\"Can I Have a Motorcycle When I Grow Up?\" — A Question for the Future",
            "body": (
                "Chris sits back down and asks a hopeful question — the book's first question looking toward the future: \"Can I have a motorcycle when I grow up?\" \"If you take care of it.\" \"How do you take care of it?\" \"Lots of things. You see what I've been doing all along.\" \"Will you teach me everything?\" \"Of course.\" \"Is it hard?\" \"If you have the right attitude, it's not hard. In fact, what's hard is having the right attitude.\" This conversation is the entire book in miniature — not about the technical questions of motorcycle maintenance, but about life, about Quality, about the right attitude. A father can finally answer his son's questions — no evasion, no madness, no being on the other side of a wall."
            ),
            "viz": (
                '<div class="quote-box">"Can I have a<br/><span style="font-weight:bold;color:#ea580c;">motorcycle</span><br/>when I grow up?"<br/><br/>"If you <span style="font-weight:bold;color:#dc2626;">take care</span> of it"<br/><br/>"Will you teach me everything?"<br/>"<span style="font-weight:bold;color:#4f46e5;">Of course</span>"<br/><br/>"<span style="font-weight:bold;font-size:18px;color:#ca8a04;">What\'s hard is<br/>the right attitude</span>"</div>'
            ),
        },
        {
            "color": "#ca8a04", "tag": "Wisdom",
            "title": "\"What's Hard Is the Right Attitude\" — The Book's Wisdom Crystallized",
            "body": (
                "This single sentence crystallizes the entire philosophical inquiry of the book. It's not that the techniques of motorcycle maintenance are complex, but that attitude — the attitude of doing everything with Quality — is what is truly difficult. The right attitude cannot be taught as rules or methods (that was Aristotle's failure), nor defined as ideals or forms (that was Plato's trap). The right attitude can only be experienced in action, cultivated on the journey, naturally arising in the relationship between person and world. Chris asks, \"Will I have the right attitude?\" Pirsig answers, \"I think so. I don't think there will be any problem.\" — this is the gentlest promise in the book, and a father's most essential trust in his son."
            ),
            "viz": (
                '<div class="flow-row">'
                '<div class="flow-step">🔧 Technique<br/>Not hard<br/>Can be taught</div>'
                '<div class="flow-arrow">→</div>'
                '<div class="flow-step">🧠 Attitude<br/>is what\'s<br/>truly hard</div>'
                '<div class="flow-arrow">→</div>'
                '<div class="flow-step">📏 Cannot be<br/>listed as rules<br/>(not Aristotle)</div>'
                '<div class="flow-arrow">→</div>'
                '<div class="flow-step">💡 Cannot be<br/>defined as forms<br/>(not Plato)</div>'
                '<div class="flow-arrow">→</div>'
                '<div class="flow-step end">⭐ Only <br/>experienced in action<br/>cultivated on the journey</div>'
                '</div>'
            ),
        },
        {
            "color": "#4f46e5", "tag": "Journey",
            "title": "Across California: From Wilderness to City, From Division to Wholeness",
            "body": (
                "They put away their helmets — \"You don't need helmets in this weather.\" Chris notices his father isn't wearing one either, so he wants his put away too. This is a signal of equality: they are no longer commander and follower, but traveling companions. They ride through Ukiah, Hopland, Cloverdale, into wine country. The freeway widens, traffic increases, houses and bay appear along the roadside. The motorcycle carries them toward San Francisco — the journey's end, and the start of a new life. \"The motorcycle that has carried us nearly halfway across a continent still purrs lowly\" — this motorcycle is no longer just a machine; it is the witness that has crossed wilderness and heart, past and present."
            ),
            "viz": (
                '<div class="flow-row">'
                '<div class="flow-step">🪖 Removing<br/>helmets<br/>Equal partners</div>'
                '<div class="flow-arrow">→</div>'
                '<div class="flow-step">🍷 Through<br/>Ukiah, Hopland<br/>Wine country</div>'
                '<div class="flow-arrow">→</div>'
                '<div class="flow-step">🛣️ Freeway<br/>widens<br/>Traffic grows</div>'
                '<div class="flow-arrow">→</div>'
                '<div class="flow-step">🏠 Houses<br/>Boats<br/>Bay appears</div>'
                '<div class="flow-arrow">→</div>'
                '<div class="flow-step end">🏍️ Motorcycle<br/>Still purrs<br/>Half a continent</div>'
                '</div>'
            ),
        },
        {
            "color": "#db2777", "tag": "Finale",
            "title": "\"We Have Won\" — Trials Without End, Hope Without End",
            "body": (
                "The book's final sentence, filled with unprecedented calm and strength: \"Of course, trials never end — as long as one lives, unpleasant things and misfortunes will happen. But I have a feeling now that I've never had before, a feeling that doesn't just stay on the surface but goes deep inside: We have won. Things are getting better. We can almost expect it.\" This is not false optimism — Pirsig acknowledges that trials are endless, suffering and misfortune will not disappear. But this feeling \"goes deep inside\" — it is not superficial cheerfulness but existential conviction. The book began with one person searching for himself; it ends with two people's \"we\" — father and son, narrator and Phaedrus, reason and Quality, no longer opposed, no longer divided. \"We can almost expect it\" — this \"almost\" carries all the honesty, and all the hope."
            ),
            "viz": (
                '<div class="quote-box" style="background:#fef2f2;border-color:#fecaca;color:#991b1b;">📖 <span style="font-weight:bold;font-size:18px;color:#dc2626;">The Book\'s Finale</span><br/><br/>"<span style="font-weight:bold;">Trials never end</span><br/>as long as one lives<br/>unpleasant things and misfortunes<br/>will happen<br/><br/>But I have<br/><span style="font-weight:bold;font-size:20px;color:#dc2626;">a feeling now<br/>I\'ve never had before</span><br/><br/>It doesn\'t just stay on the surface<br/>but goes <span style="font-weight:bold;color:#4f46e5;">deep inside</span>:<br/><br/><span style="font-weight:bold;font-size:24px;color:#ea580c;">We have won.</span><br/>Things are getting better.<br/>We can almost expect it."</div>'
            ),
        },
    ],
    "takeaway": (
        "Chapter 32 is the book's epilogue and its gentlest closure. After twenty-nine chapters of philosophical inquiry, emotional tearing, madness and awakening, Pirsig gives the reader — and Chris — a quiet gift. Chris standing on the motorcycle foot pegs for the first time, looking over his father's shoulder at the world, is the book's most beautiful image: no longer blocked, no longer passive, no longer seeing only a back. He asks if he can have his own motorcycle — this is an expectation for the future, for inheritance, for continuing to live. And Pirsig's answer — \"What's hard is having the right attitude\" — is the book's philosophical summary: Quality does not reside in rules, in definitions, in ideals — it resides in attitude, in action, in the relationship between person and world in every moment. From \"I\" to \"we\" — the shift in the book's final word is the true destination of this odyssey across half a continent. Not that problems were solved, but that divisions were healed."
    ),
}


# =============================================
# TEMPLATES
# =============================================

def make_page(ch_data, lang, ch_num):
    """Generate HTML for one chapter."""
    zh_active = ' class="active"' if lang == "zh" else ' class=""'
    en_active = ' class="active"' if lang == "en" else ' class=""'
    
    sections_html = ""
    sec_colors = ["#dc2626", "#ea580c", "#ca8a04", "#4f46e5", "#db2777"]
    sec_bgs = ["#fef2f2", "#fff7ed", "#fefce8", "#eef2ff", "#fdf2f8"]
    sec_labels = ["01", "02", "03", "04", "05"]
    
    for i, sec in enumerate(ch_data["sections"]):
        color = sec["color"]
        bg = sec_bgs[i]
        label = sec_labels[i]
        # Use explicit color from section data if different
        border_color = color if color in sec_colors else sec_colors[i]
        bg_color = bg
        
        sections_html += f'''
<div class="section" style="border-left:4px solid {color}">
<div class="sec-header">
<div class="sec-num" style="background:{bg_color};color:{color}">{label}</div>
<span class="sec-tag" style="background:{bg_color};color:{color}">{sec["tag"]}</span>
<span class="sec-title" style="color:{color}">{label} {sec["title"]}</span>
</div>
<div class="sec-body">{sec["body"]}</div>
<div class="sec-viz">{sec["viz"]}</div>
</div>'''
    
    kpis_html = ""
    for val, label, color in ch_data["kpis"]:
        kpis_html += f'''
<div class="kpi-card" style="border-top-color:{color}">
<div class="kpi-val" style="color:{color}">{val}</div>
<div class="kpi-label">{label}</div>
</div>'''
    
    ch_label = {
        "zh": f"第二十{['九','','',''][0]}章" if ch_num == 29 else f"第三十{'章' if ch_num==30 else '一' if ch_num==31 else '二'}章",
        "en": f"Chapter {ch_num}"
    }[lang]
    
    footer_text = {
        "zh": "来源：罗伯特·M·波西格《禅与摩托车维修艺术》",
        "en": 'Source: Robert M. Pirsig <em>Zen and the Art of Motorcycle Maintenance</em>'
    }[lang]
    
    catalog_label = {
        "zh": "📖 返回目录",
        "en": "📖 Back to Catalog"
    }[lang]
    
    html = f'''<!DOCTYPE html>
<html lang="{lang}">
<head><meta charset="UTF-8"><meta name="viewport" content="width=device-width,initial-scale=1.0">
<title>禅与摩托车维修艺术 · {ch_label}</title>
<style>
{CSS}
</style>
</head><body>
<div class="container">
<div class="catalog-link">
<a href="catalog.html">{catalog_label}</a>
</div>
<div class="lang-switch">
<a href="{SLUG}-ch{ch_num:03d}-info-zh.html"{zh_active}>中文</a>
<a href="{SLUG}-ch{ch_num:03d}-info-en.html"{en_active}>EN</a>
</div>
<div class="header">
<h1>禅与摩托车维修艺术 · {ch_data["num"]}{ch_data["title"]}</h1>
<div class="subtitle">{ch_data["subtitle"]}</div>
</div>
<div class="divider"></div>
<div class="chapter-overview">
<p>{ch_data["overview"]}</p>
</div>
<div class="kpi-row">{kpis_html}
</div>{sections_html}
<div class="takeaway">
<div class="ta-label">💡 {"核心启示" if lang=="zh" else "Key Insight"}</div>
<p>{ch_data["takeaway"]}</p>
</div>
<div class="footer">
{footer_text}
</div>
</div><!-- .container -->
</body></html>'''
    return html


def main():
    chapters = [(29, ch029_zh, ch029_en), (30, ch030_zh, ch030_en),
                (31, ch031_zh, ch031_en), (32, ch032_zh, ch032_en)]
    
    for ch_num, zh_data, en_data in chapters:
        # Generate and write ZH
        zh_html = make_page(zh_data, "zh", ch_num)
        zh_path = os.path.join(BOOKDIR, f"{SLUG}-ch{ch_num:03d}-info-zh.html")
        with open(zh_path, "w", encoding="utf-8") as f:\n            f.write(zh_html)\n        print(f"✅ Written: {os.path.basename(zh_path)} ({len(zh_html)} chars)")
        
        # Validate ZH: div balance
        opens = zh_html.count("<div")
        closes = zh_html.count("</div>")
        if opens != closes:
            print(f"  ❌ DIV IMBALANCE: {opens} opens vs {closes} closes")
        else:
            print(f"  ✅ div balance OK: {opens}/{closes}")
        
        # Validate ZH: FZXPYZS
        if "'FZXPYZS'" not in zh_html:
            print(f"  ❌ Missing FZXPYZS font")
        else:
            print(f"  ✅ FZXPYZS font present")
        
        # Validate ZH: flex centering
        if "display:flex" not in zh_html or "justify-content:center" not in zh_html:
            print(f"  ❌ Missing flex centering in body")
        else:
            print(f"  ✅ Body flex centering present")
        
        # Generate and write EN
        en_html = make_page(en_data, "en", ch_num)
        en_path = os.path.join(BOOKDIR, f"{SLUG}-ch{ch_num:03d}-info-en.html")
        with open(en_path, "w", encoding="utf-8") as f:\n            f.write(en_html)\n        print(f"✅ Written: {os.path.basename(en_path)} ({len(en_html)} chars)")
        
        # Validate EN: div balance
        opens = en_html.count("<div")
        closes = en_html.count("</div>")
        if opens != closes:
            print(f"  ❌ DIV IMBALANCE: {opens} opens vs {closes} closes")
        else:
            print(f"  ✅ div balance OK: {opens}/{closes}")
        
        # Validate EN: FZXPYZS
        if "'FZXPYZS'" not in en_html:
            print(f"  ❌ Missing FZXPYZS font")
        else:
            print(f"  ✅ FZXPYZS font present")
        
        # Validate EN: flex centering
        if "display:flex" not in en_html or "justify-content:center" not in en_html:
            print(f"  ❌ Missing flex centering in body")
        else:
            print(f"  ✅ Body flex centering present")
        
        print()
    
    print("=== ALL FILES GENERATED ===")


if __name__ == "__main__":
    main()