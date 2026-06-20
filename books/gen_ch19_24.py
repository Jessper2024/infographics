#!/usr/bin/env python3
"""Generate HTML infographics for 弹性生长 chapters 19-24 (zh + en)"""

OUT = "/Users/jessper/.openclaw/workspace/infographics/books"

def html_head(ch, zh_title, en_title, lang, subtitle_zh, subtitle_en):
    t = zh_title if lang == "zh" else en_title
    sub = subtitle_zh if lang == "zh" else subtitle_en
    lang_label = "中文版" if lang == "zh" else "English"
    lang_code = "zh-CN" if lang == "zh" else "en"
    return f'''<!DOCTYPE html>
<html lang="{lang_code}">
<head>
<meta charset="UTF-8">
<meta name="viewport" content="width=device-width, initial-scale=1.0">
<title>弹性生长 · 第{ch}章 – {t}</title>
<style>
@font-face {{ font-family:'FZXPYZS'; src:url('../方正屏显雅宋简体.TTF') format('truetype'); }}
* {{ margin:0; padding:0; box-sizing:border-box; }}
body {{ background:#e5e7eb; display:flex; justify-content:center; padding:30px 10px;
        font-family:'FZXPYZS','PingFang SC','Hiragino Sans GB','Microsoft YaHei',sans-serif; }}
.card {{ width:880px; max-width:100%; background:#f5f1eb; border-radius:20px;
         box-shadow:0 8px 40px rgba(0,0,0,.10); overflow:hidden; }}
.pad {{ padding:32px 40px; }}
@media(max-width:880px){{ .pad {{ padding:24px 20px; }} }}
</style>
</head>
<body>
<div class="card">

<div class="pad" style="padding-bottom:0;">
  <a href="弹性生长-catalog.html" style="font-size:13px; color:#9ca3af; text-decoration:none;">{'← 返回目录' if lang=='zh' else '← Catalog'}</a>
</div>

<div class="pad" style="padding-top:8px; padding-bottom:0; text-align:right;">
  <span style="display:inline-block; background:#e5e7eb; color:#6b7280; font-size:11px;
               padding:4px 10px; border-radius:20px; letter-spacing:.5px;">{lang_label}</span>
</div>

<div class="pad" style="padding-top:16px; padding-bottom:0;">
  <h1 style="font-size:28px; font-weight:900; color:#1f2937; line-height:1.3;">
    弹性生长 · 第{ch}章<br><span style="color:#dc2626;">「{zh_title}」</span>
  </h1>
</div>

<div class="pad" style="padding-top:8px; padding-bottom:0;">
  <p style="font-size:15px; color:#6b7280; line-height:1.6;">{sub}</p>
</div>

<div class="pad" style="padding-top:18px; padding-bottom:0;">
  <div style="height:4px; border-radius:2px;
              background:linear-gradient(90deg,#dc2626,#ea580c,#d97706,#4f46e5,#db2777);"></div>
</div>
'''

def overview_section(zh_overview, en_overview, lang):
    text = zh_overview if lang == "zh" else en_overview
    label = "📖 章节概述" if lang == "zh" else "📖 Chapter Overview"
    return f'''
<div class="pad" style="padding-top:22px; padding-bottom:0;">
  <div style="background:linear-gradient(135deg,#eef2ff,#e0e7ff); border-radius:14px;
              padding:20px 24px; border:1px solid #c7d2fe;">
    <div style="font-size:13px; color:#4f46e5; font-weight:700; margin-bottom:8px;
                letter-spacing:1px;">
      {label}
    </div>
    <p style="font-size:14px; color:#3730a3; line-height:1.8;">{text}</p>
  </div>
</div>
'''

def kpi_section(kpis_zh, kpis_en, lang):
    kpis = kpis_zh if lang == "zh" else kpis_en
    colors = ["#dc2626", "#ea580c", "#d97706", "#4f46e5"]
    label = "📊 核心指标" if lang == "zh" else "📊 Core Metrics"
    html = f'''
<div class="pad" style="padding-top:24px; padding-bottom:0;">
  <div style="font-size:13px; color:#4f46e5; font-weight:700; margin-bottom:12px;
              letter-spacing:1px;">
    {label}
  </div>
  <div style="display:flex; flex-wrap:wrap; gap:12px;">
'''
    for i, (k, v) in enumerate(kpis):
        c = colors[i % len(colors)]
        html += f'''
    <div style="background:#fff; border-radius:12px; padding:18px 16px; text-align:center;
                box-shadow:0 2px 8px rgba(0,0,0,.06); flex:1; min-width:180px;
                border-top:4px solid {c};">
      <div style="font-size:12px; color:#6b7280; margin-bottom:4px; letter-spacing:.5px;
                  text-transform:uppercase;">{k}</div>
      <div style="font-size:14px; color:#1f2937; line-height:1.5; font-weight:600;">{v}</div>
    </div>
'''
    html += '</div>\n</div>\n'
    return html

def sections_html(sections_zh, sections_en, lang):
    sections = sections_zh if lang == "zh" else sections_en
    colors = ["#dc2626", "#ea580c", "#d97706", "#4f46e5", "#db2777"]
    label = "🔍 深度解读" if lang == "zh" else "🔍 Deep Dive"
    html = f'''
<div class="pad" style="padding-top:28px; padding-bottom:0;">
  <div style="font-size:13px; color:#4f46e5; font-weight:700; margin-bottom:12px;
              letter-spacing:1px;">
    {label}
  </div>
'''
    for i, (title, content) in enumerate(sections):
        c = colors[i % len(colors)]
        html += f'''
    <div style="background:#fff; border-radius:12px; padding:20px 22px;
                box-shadow:0 2px 8px rgba(0,0,0,.05); margin-bottom:14px;
                border-left:5px solid {c};">
      <div style="font-size:16px; font-weight:700; color:{c}; margin-bottom:8px;">{title}</div>
      <div style="font-size:14px; color:#374151; line-height:1.75;">{content}</div>
    </div>
'''
    html += '</div>\n'
    return html

def takeaway_section(zh_takeaway, en_takeaway, lang):
    text = zh_takeaway if lang == "zh" else en_takeaway
    label = "💡 核心启示" if lang == "zh" else "💡 Key Takeaway"
    return f'''
<div class="pad" style="padding-top:28px; padding-bottom:0;">
  <div style="background:#fff; border-radius:14px; padding:22px 24px;
              border:2px solid #dc2626; position:relative;">
    <div style="position:absolute; top:-12px; left:24px; background:#dc2626; color:#fff;
                font-size:12px; font-weight:700; padding:4px 14px; border-radius:20px;
                letter-spacing:.5px;">
      {label}
    </div>
    <p style="font-size:15px; color:#1f2937; line-height:1.85; font-weight:500;
             padding-top:6px;">{text}</p>
  </div>
</div>
'''

def footer(lang):
    f_text = '《弹性生长》信息图 · 中文版 · 由AI生成' if lang == 'zh' else '《弹性生长 Resilience Growth》 Infographic · English · AI-Generated'
    return f'''
<div class="pad" style="padding-top:24px; text-align:center;">
  <div style="height:1px; background:#e5e7eb; margin-bottom:16px;"></div>
  <p style="font-size:12px; color:#9ca3af;">{f_text}</p>
</div>

</div>
</body>
</html>'''

# ============================================================
# CHAPTER 19
# ============================================================
ch19_zh = "为什么普通人比富二代更容易创业成功"
ch19_en = "Why Ordinary People Succeed More at Entrepreneurship Than the Rich Second Generation"
ch19_sub_zh = "真正的企业家永远在创业——中等家庭才是创业主力军"
ch19_sub_en = "True entrepreneurs are forever starting up — middle-class families are the real entrepreneurial force"

ch19_ov_zh = """我国上市公司的富二代继承人们资源充足、人脉广泛，为什么创业成功率却不高？从美国经验看，二代们大部分脱离了管理层，把企业交给职业经理人，富豪家族处于食利阶层。而排名靠前的上市公司CEO中，含着金钥匙出生的人非常少，贫困家庭出身的更少，大部分都是中产阶层家庭出身。问题的核心在于：企业经营本身非常不稳定，真正的企业家"永远在创业"；富二代不是创业者，周围都是马屁精，缺乏"基层视角"理解不了普通人需求。中等家庭子弟既有烟火气又懂社会，拥有相对多的资源接受教育，形成"接力赛"模式——每代人往前走一步。"""

ch19_ov_en = """Why do the rich second-generation heirs of China's listed companies, with abundant resources and extensive connections, have such low entrepreneurial success rates? Looking at the US experience, most second-generation heirs have stepped away from management, handing companies to professional managers while the wealthy families live off dividends. Among top listed company CEOs, very few were born with silver spoons, even fewer from poverty — most come from middle-class families. The core issue: business operations are inherently unstable and true entrepreneurs are "forever starting up." Rich second-gen heirs aren't entrepreneurs — they're surrounded by sycophants and lack the "grassroots perspective" to understand ordinary people's needs. Middle-class children have both street smarts and social understanding, with relatively more resources for education, forming a "relay race" model where each generation advances one step further."""

ch19_kpis_zh = [
    ("中产主导", "排名靠前的上市公司CEO，大部分出身中等家庭，既非豪门也非寒门"),
    ("创业者DNA", "真正的企业家永远在创业——企业经营不稳定，只有创业者能带领公司往前走"),
    ("富二代短板", "周围马屁精多→缺乏警戒心；缺基层视角→不理解普通人需求；砸钱模式不可持续"),
    ("接力赛模式", "每一代人往前走一步，用一代人熬成中产，下一代人在此基础上再进一步"),
]
ch19_kpis_en = [
    ("Middle-Class Dominance", "Most top listed-company CEOs come from middle-class families — neither wealthy nor poor"),
    ("Entrepreneur DNA", "True entrepreneurs are perpetually starting up; only founders can drive companies forward"),
    ("Rich Kid Weaknesses", "Surrounded by yes-men → no vigilance; no grassroots view → can't understand consumer needs; money-burning models are unsustainable"),
    ("Relay Race Model", "Each generation advances one step — one generation becomes middle class, the next climbs higher"),
]

ch19_sec_zh = [
    ("中产阶层的统治力：高盛掌门的故事",
     "以高盛两代掌门为例——现任掌门贝兰克梵出身纽约中等偏下家庭，父亲是邮局员工，母亲是公司接待员，靠奖学金进入哈佛。前任掌门保尔森出身4000人小镇的中等农场家庭，达特茅斯+哈佛MBA。显卡双神黄仁勋和苏姿丰都出身台湾中产阶级家庭，而非富二代。社会已进入流动性变差的状态，像沥青越来越稠，但'接力赛'模式依然有效。"),
    ("富二代的三大致命缺陷",
     "①周围全是马屁精——说真话的少，富二代被吹捧产生错觉，该避的坑一个避不开，无关智商，人性使然。②缺乏基层视角——绝大部分商业模式是'平民模式'，产品要卖给普通人，不理解需求就卖不出去。王思聪曾质疑充电宝租用模式，理解不了没车年轻人的需求。③砸钱模式不可持续——创业最关键的是'成本-收益利润差'，疯狂压低成本才是核心能力。"),
    ("创业的九死一生本质",
     "创业本身成功率极低，富二代只是把成功率从千分之一拉到百分之一，看着上升一个数量级，实际依旧非常低。一个真正的创业者走的是周围人都不认可的路——如果都认可，红利期早就过了。创业者需要能在质疑中前进，看到别人只能看到困难、看不到前景的地方。"),
    ("机会下乡：释放中国的人才潜力",
     "几十万人才能支撑一座博物馆，一百万人才能支撑一座歌剧院。在中国基层还有无数黄仁勋和苏姿丰，只是潜力还没释放人生就没了选择。庞大人口库如果不能释放人才潜力，就只是增加养老负担；如果能充分释放，就是全世界最大资源库。国家层面的扶贫、城市化、教育公平，个人层面尽量在城市生活——这代人前进一小步，下代人就能跨一大步。"),
    ("线性积累，指数爆发",
     "很多事都是经过漫长积累后一飞冲天的。前期发展是线性的，后期发展是指数级的。中等家庭的接力赛模式，本质就是用一代人的线性积累，换取下一代人的指数爆发。承认自己的普通没什么不好，关键是选对正确的路，持续向前。"),
]
ch19_sec_en = [
    ("Middle-Class Dominance: The Goldman Sachs Story",
     "Take Goldman Sachs' two recent leaders: current CEO Blankfein was born to a NYC postal worker and receptionist, got into Harvard on scholarship. Predecessor Paulson came from a 4,000-person town's medium farm, Dartmouth + Harvard MBA. NVIDIA's Jensen Huang and AMD's Lisa Su both came from Taiwanese middle-class families, not wealth. Society has become less fluid, like thickening asphalt, but the relay race model still works."),
    ("Three Fatal Flaws of Rich Heirs",
     "① Surrounded by sycophants — few speak truth, inflated egos blind them to traps. This isn't about IQ, it's human nature. ② No grassroots perspective — most business models are 'mass-market models'; products must sell to ordinary people. Wang Sicong questioned power bank rentals because he couldn't understand carless young people's needs. ③ Money-burning is unsustainable — the key to entrepreneurship is the 'cost-revenue profit gap'; relentlessly cutting costs is the core capability."),
    ("The Near-Impossible Nature of Entrepreneurship",
     "The baseline success rate is extremely low. Rich heirs only raise it from 0.1% to 1% — looks like an order of magnitude but remains tiny. A true entrepreneur walks a path others don't approve of — if everyone approved, the golden window would have closed. Entrepreneurs must advance amid doubt, seeing prospects where others only see obstacles."),
    ("Bringing Opportunity to the Countryside: Unlocking China's Talent",
     "It takes hundreds of thousands to support a museum, a million for an opera house. In China's grassroots, countless potential Huang Renxuns and Su Zifengs exist but never got the chance. A huge population that can't unlock talent potential is just a pension burden; if unlocked, it's the world's greatest resource pool. National-level poverty alleviation, urbanization, education equity; personal-level: live in cities — one small step this generation enables a giant leap for the next."),
    ("Linear Accumulation, Exponential Takeoff",
     "Many things require long accumulation before rocketing upward. Early development is linear; later development is exponential. The middle-class relay race model essentially uses one generation's linear accumulation to fuel the next generation's exponential explosion. Admitting you're ordinary isn't bad — the key is choosing the right path and persisting forward."),
]

ch19_take_zh = """富二代继承人们资源逆天却成功率低，根本原因在于企业经营是"永远在创业"的状态，而富二代不是创业者。中等家庭子女既接地气又有教育资源，形成了最有效的"接力赛"上升模式。从国家层面，扶贫、城市化和教育公平是释放亿万人才潜力的关键；从个人层面，每代人往前走一小步，积累到某个节点就会指数级爆发。承认普通、选对路径、持续向前——这才是普通人最务实的成功之道。"""
ch19_take_en = """Rich second-gen heirs have incredible resources yet low success rates because business operations demand "perpetual entrepreneurship" — and heirs are not entrepreneurs. Middle-class children have both real-world grounding and educational resources, forming the most effective "relay race" upward mobility model. At the national level, poverty alleviation, urbanization, and educational equity are key to unlocking the potential of millions. At the personal level, each generation advancing one small step eventually reaches an exponential tipping point. Admit you're ordinary, choose the right path, persist forward — this is the most practical success formula for ordinary people."""

# ============================================================
# CHAPTER 20
# ============================================================
ch20_zh = "想摆脱低端内卷，唯有提升产品力"
ch20_en = "To Escape Low-End Cutthroat Competition, Only Product Excellence Works"
ch20_sub_zh = "从山寨到高端——德国日本都走了几十年，我们正在路上"
ch20_sub_en = "From copycat to premium — Germany and Japan took decades, we're on the way"

ch20_ov_zh = """作者以大学时听到的一个"毒鸡汤"故事开篇：软件公司为省排查代码成本，每隔六天主动重启服务器来规避内存泄露问题。后来才意识到，真正高级的做法是不惜代价解决问题、推广经验、避免重蹈覆辙。产品开发是"设计—开发—发现问题—解决问题"的迭代过程，在残次品基础上迭代迟早会变得不可收拾。三个阶段：责任心→流程驱动→大神系统设计。德国工业早期也是山寨起家，用了数十年才从山寨走向高端，前提是坚持质量理念。我国企业死得还不够多——廉价劳动力掩盖了质量和管理的缺陷，人口下降反而预示着更尊重劳动者的时代到来。"""

ch20_ov_en = """The author opens with a "toxic鸡汤" story from college: a software company saved debugging costs by proactively rebooting servers every six days to avoid a memory leak. He later realized the truly professional approach is to solve problems at any cost, spread learnings, and prevent recurrence. Product development is an iterative "design-build-find problems-fix problems" cycle; iterating on a defective foundation eventually becomes unmanageable. Three stages: responsibility → process-driven → expert system design. German industry also started as copycats, taking decades to reach premium status — the prerequisite was commitment to quality. China's companies haven't died enough yet — cheap labor masked quality and management flaws. Population decline paradoxically signals the dawn of an era that respects workers more."""

ch20_kpis_zh = [
    ("毒鸡汤文化", "把偷奸耍滑当本事——服务器内存泄露不修，改成每周定时重启，低级作坊的缺德操作"),
    ("三阶段进化", "责任心→流程驱动（闭环测试）→大神操盘（前瞻性系统设计）——层层递进的质量进化"),
    ("山寨到高端", "德国'Made in Germany'曾是工业垃圾代名词，日本车靠便宜+质量占领美国——都走了几十年"),
    ("人口下降倒逼质量", "充裕人力造成滥用；人力不足时才会通过复杂工具和流程控制成本——更健康的人才道路"),
]
ch20_kpis_en = [
    ("Toxic Culture", "Cutting corners as skill — instead of fixing a memory leak, rebooting servers weekly. The shameful shortcut of low-grade workshops"),
    ("Three-Stage Evolution", "Responsibility → Process-driven (closed-loop testing) → Expert system design (forward-looking architecture) — layered quality evolution"),
    ("Copycat to Premium", "Germany's 'Made in Germany' was once a mark of industrial trash; Japanese cars won America through cheap prices + quality — both took decades"),
    ("Population Decline Forces Quality", "Abundant labor enabled abuse; only when labor is scarce do people use complex tools and processes to control costs — a healthier talent path"),
]

ch20_sec_zh = [
    ("毒鸡汤的毒性：偷奸耍滑不是智慧",
     "作者大学时听到某软件公司负责人的演讲：服务器每周内存泄露崩一次，技术骨干的'妙招'是每六天凌晨主动重启一次。当时觉得是大神操作，后来才明白这有多恶劣。真正专业的做法是不惜代价解决问题、推广经验、杜绝复发。产品开发是迭代过程——在残次品基础上不断迭代，最初的问题迟早变得不可收拾。就像盖楼，第一层就不能有质量问题。这种把偷奸耍滑当智慧的文化，长期毒害了无数人。"),
    ("三个阶段：从责任心到流程驱动到大神操盘",
     "第一阶段：责任心固然重要，但工业生产时代最关键是流程。兢兢业业写代码也不能确保不出问题，需要专业测试和闭环流程追踪。第二阶段：流程可以保证即使技术人员懈怠了，产品质量依旧可靠——这就是流程驱动。第三阶段：真正关键的是经验丰富的大神对系统进行改进。就像建楼，初期只准备了五层冗余，后来要加一百层，只能推倒重构——这需要顶级大神操盘，能力强且经验丰富。"),
    ("德国神话的真相：山寨起家，数十年进化",
     "德国工业神话出现得非常晚，早期也靠山寨起家。所有后起国家都是如此：初期赚钱窍门是复制而非改进，功能达别人80%、价格只有30%就能卖出去。'Made in Germany'曾是工业垃圾代名词，如今成为品质保证。日本也是一样：丰田先用低价+好质量占领美国，积累资本后再用雷克萨斯突破高端。他们都用了几十年。中国所有打出品牌的实力公司走的都是同一条路：同一套流程标准，质量一样高，价格还更便宜。"),
    ("企业死得还不够多：廉价劳动力的诅咒",
     "我国企业之前过得太舒服：人力资源太便宜，打得国外低端产品市场毫无还手之力。大部分企业不在意质量和管理缺陷——出问题用廉价劳动力加班补偿就行。欧美学者断言：中国当年没工业革命就是因为人口太多，什么事砸人力就行，任何机械和新发明都会因无用武之地而消亡。人口下降虽有坏处，但也预示着更尊重劳动者的时代。企业不再比拼低端产品时，质量、品位、迭代性才会成为核心竞争力。"),
    ("用产品给用户洗脑：产品力的终极形态",
     "丰田霸道买了过几年还能加价卖出——变态的质量理念打造出来的产品对用户有洗脑作用。苹果、安卓各有粉丝，甚至锤子手机都有粉丝。只要产品质量过关、有自己的风格、坚持以市场为导向做下去，关于产品的神话就会随之而来。中国制造要成为高品质代名词，必须走两条路：修复被毒鸡汤毒害的心灵，把质量意识灌输进去；同时鼓励突破，给年轻人和梦想家机会。"),
]
ch20_sec_en = [
    ("The Toxicity of 'Clever' Shortcuts",
     "The author heard a software company executive's speech in college: a server crashed weekly from a memory leak, and the 'genius' solution was to proactively reboot at 6 AM every six days. Initially admired as brilliant, he later realized how shameful this was. The truly professional approach is solving problems at any cost, spreading learnings, and preventing recurrence. Product development is iterative — iterating on a defective foundation inevitably becomes unmanageable. Like building a tower, the first floor can't have quality issues. This culture of celebrating shortcuts has long poisoned countless minds."),
    ("Three Stages: From Responsibility to Process to Master Design",
     "Stage 1: Responsibility matters, but in industrial production, the key is process. Writing code diligently can't guarantee zero bugs — you need professional testing and closed-loop tracking. Stage 2: Even when engineers slack off, process ensures quality — this is process-driven development. Stage 3: What truly matters is experienced masters improving the system. Like building: you prepared for 5 more floors, but now need 100 — you must tear down and rebuild. This requires top-level masters with both ability and experience."),
    ("The Truth About German Excellence: Started as Copycats",
     "Germany's industrial myth emerged quite late; early on they also relied on copying. All latecomer nations follow this path: the initial profit trick is copying, not improving — 80% functionality at 30% price sells. 'Made in Germany' was once a mark of industrial trash; now it's a quality guarantee. Japan followed the same path: Toyota won America with low prices + good quality, then broke into premium with Lexus. Both took decades. China's branded successful companies walk the exact same path: same process standards, equally high quality, lower prices."),
    ("Not Enough Companies Have Died: The Curse of Cheap Labor",
     "Chinese companies were too comfortable: labor was so cheap that foreign low-end products had no chance. Most companies ignored quality and management flaws — any problem could be compensated with cheap overtime labor. European scholars assert: China missed the Industrial Revolution because of too many people — just throw humans at any problem, and any machine or invention would find no use. Population decline has downsides but signals a new era that respects workers more. When companies can't compete on low-end products anymore, quality, taste, and iterability will become core competitiveness."),
    ("Brainwashing Users with Product: The Ultimate Form of Product Power",
     "A Toyota Prado can sell for more after years of use — products built with obsessive quality have a brainwashing effect on users. Apple and Android each have fans; even Smartisan phones had fans. As long as product quality is solid, has its own style, and persists market-oriented, myths about the product will naturally follow. For 'Made in China' to become synonymous with quality, two paths are needed: heal minds poisoned by shortcut culture and instill quality consciousness; simultaneously encourage breakthroughs and give young people and dreamers opportunities."),
]

ch20_take_zh = """摆脱低端内卷只有一条路：提升产品力。德国和日本从山寨走到高端用了数十年，前提是坚持质量理念。中国企业的发展路径已经清晰：责任心→流程驱动→大神系统设计，层层递进。人口下降带来的劳动力紧缺，将倒逼企业从依赖廉价人力转向依赖流程和品质。用变态的质量理念打造产品，产品自己就会给用户洗脑。两条腿走路：修复毒鸡汤文化，灌输质量意识；同时鼓励突破创新。路径就在那里，扎扎实实走，总会出头。"""
ch20_take_en = """Only one path to escape low-end cutthroat competition: elevate product excellence. Germany and Japan took decades from copycat to premium, built on commitment to quality. China's path is clear: responsibility → process-driven → master system design, progressing layer by layer. Labor scarcity from population decline will force companies to shift from cheap labor dependence to process and quality reliance. Products built with obsessive quality will naturally brainwash users. Walk on two legs: heal shortcut culture and instill quality consciousness; simultaneously encourage breakthrough innovation. The path is there — walk it steadily, and you'll eventually break through."""

# ============================================================
# CHAPTER 21
# ============================================================
ch21_zh = "碳排放和我们普通人有什么关系"
ch21_en = "What Does Carbon Emission Have to Do With Ordinary People?"
ch21_sub_zh = "碳中和是接下来十年最重要的事——它将重塑每一个人的生活"
ch21_sub_en = "Carbon neutrality is the most important thing in the next decade — it will reshape everyone's life"

ch21_ov_zh = """"碳中和"指通过减排和植树造林等方式抵消碳排放，实现相对"零排放"。中国承诺2030年碳达峰、2060年碳中和。为什么以前不搞现在主动减排？因为中国已基本实现工业化，要开始转型了——而且高举环保大旗可以防止制造业回流西方。回顾历史，每次弯道超车的发达国家都是换赛道：荷兰→英国→美国，都是在对原有体系的继承上实现突破。碳排放曾经就是发展权，现在碳税不可避免——特斯拉2020年仅靠出售碳积分就赚了15.8亿美元。中国已形成新能源产业闭环：光伏生产能源、特高压运输、电动车消费。光伏和电动车已跨过"奇点"，实现市场化运营。"""

ch21_ov_en = """'Carbon neutrality' means offsetting carbon emissions through emission reduction and afforestation to achieve relative 'zero emissions.' China has committed to peak carbon by 2030 and achieve neutrality by 2060. Why proactively reduce emissions now after resisting before? Because China has basically completed industrialization and needs to transform — and championing environmentalism can prevent manufacturing from returning to the West. Historically, every nation that overtook on the curve switched tracks: Netherlands → UK → US, each building breakthroughs on inherited systems. Carbon emissions were once development rights; now carbon taxes are inevitable — Tesla earned $1.58B from carbon credits alone in 2020. China has formed a new energy industry closed loop: solar generates energy, UHV transmits it, EVs consume it. Solar and EVs have crossed the 'singularity' point to market-driven operation."""

ch21_kpis_zh = [
    ("碳达峰·碳中和", "2030年碳达峰、2060年碳中和——新能源闭环：光伏（产）+特高压（运）+电动车（消）"),
    ("碳税绞索", "碳排放量大的企业若不整改，赚的钱还不够交碳税；特斯拉靠卖碳积分年赚15.8亿美元"),
    ("奇点思维", "技术发展像在迷雾中前行，过了某个节点突然醍醐灌顶——光伏和电动车已跨过奇点"),
    ("电力-人民币体系", "西北地区变'超级大油田'，特高压输电网络取代油轮，挑战石油美元霸权"),
]
ch21_kpis_en = [
    ("Carbon Peak & Neutrality", "2030 peak, 2060 neutral — new energy closed loop: Solar (produce) + UHV (transmit) + EVs (consume)"),
    ("Carbon Tax Stranglehold", "High-emission companies will pay more in carbon taxes than they earn; Tesla made $1.58B from carbon credit sales alone"),
    ("Singularity Thinking", "Tech development is like walking through fog — suddenly everything clicks at a tipping point. Solar and EVs have crossed the singularity"),
    ("Electricity-RMB System", "NW China becomes a 'super oil field,' UHV transmission replaces tankers, challenging the petrodollar hegemony"),
]

ch21_sec_zh = [
    ("弯道超车的密码：换赛道，定规则",
     "回顾大国交替：荷兰靠信用和压低成本→英国殖民地+第一次工业革命→美国德国换赛道（内燃机+电力）+第二次工业革命→美国押注核能+计算机+互联网彻底领先。每次弯道超车都是继承原有体系又实现突破。碳中和规则体系同理：早年碳排放就是发展权，若严格执行碳壁垒会锁死中国工业水平。如今中国工业化基本完成，主动转型，还要防止制造业回流西方。"),
    ("新能源三驾马车：光伏·特高压·电动车",
     "2008年次贷危机后中国集中火力研发光伏和电动车，2006年已开始特高压。三者形成闭环：光伏生产能源→特高压运输→电动车消费。光伏产业经历了无数质疑：早期骗补贴、成本居高不下。但政府清醒明智，两条腿走路——国家财政推动初始阶段，市场需求接管盈利阶段。光伏和电动车已跨过奇点：光伏不再需要补贴，电动车渗透率有望突破35%，续航突破1000公里。"),
    ("奇点思维：从迷雾到豁然开朗",
     "市场技术发展像学习新技能：一开始痛苦神秘，过了某个节点突然醍醐灌顶。iPhone4之前诺基亚研究了多年触屏但效果不好，iPhone4发布后智能手机爆发性突破。同样的逻辑：中国光伏已完全市场化，每年装机量暴涨。日本押注氢能源积累了无数专利，但中美欧选择了电动车——市场规模决定了赛道选择。氢能源不会放弃，但主攻重卡场景——高速路口修少量加氢站即可覆盖。"),
    ("碳税：催命绞索与新的财富密码",
     "碳排放量大的企业不整改，赚的钱还不够交碳税。特斯拉2020年碳积分赚了15.8亿美元，而净利润才7亿多美元——相当于对企业征收另一种碳税。碳壁垒可能绞死一些国家的低端制造业。定投碳积分可能是下一个投资商机。浙江已开设'碳账户'，按行为习惯充值，落实到政策扶持上——社保年限、碳账户数值都可能纳入购房摇号评估。"),
    ("从打工者到专利主：研发强国之路",
     "现在风电和光伏占社会用电量11%，2030年目标25%。未来电动车天地广阔，足以养活几百万研发人员，间接创造上千万岗位。过去制造业不赚钱因为研发和销售都不在国内，只赚代加工辛苦钱。碳中和就是要避开西方成熟专利，研发自己的科技专利——光伏和特高压国际标准已是中文翻译成英文。你看到的障碍，别人看到的是激发潜力的悬赏令。未来十年，碳中和会催生无数新技术新思想，重塑每一个人。"),
]
ch21_sec_en = [
    ("The Secret to Overtaking on the Curve: Switch Tracks, Set Rules",
     "Review great power transitions: Netherlands (credit + cost suppression) → UK (colonies + First Industrial Revolution) → US/Germany (switched to combustion engines + electricity, Second IR) → US (bet on nuclear + computing + internet, total dominance). Every overtaking involved inheriting old systems while achieving breakthrough. Carbon neutrality rules follow the same logic: earlier, carbon emissions were development rights — strict carbon barriers would have locked China's industrialization. Now that China has basically completed industrialization, proactively transforming also prevents manufacturing from returning to the West."),
    ("The New Energy Trinity: Solar · UHV · EVs",
     "After the 2008 subprime crisis, China focused firepower on solar and EVs, with UHV starting in 2006. The three form a closed loop: solar produces energy → UHV transmits → EVs consume. Solar faced countless criticisms: early subsidy scams, persistently high costs. But the government stayed lucid, walking on two legs — national finance pushed the initial phase, market demand took over the profitable phase. Solar and EVs have crossed the singularity: solar no longer needs subsidies, EV penetration may exceed 35%, range may break 1,000km."),
    ("Singularity Thinking: From Fog to Enlightenment",
     "Market-tech development is like learning a new skill: painful and mysterious at first, then suddenly everything clicks at a tipping point. Before iPhone 4, Nokia researched touchscreens for years with poor results; iPhone 4 triggered explosive smartphone breakthroughs. Same logic: China's solar is fully marketized now, with installations surging annually. Japan bet on hydrogen and accumulated countless patents, but China, US, and Europe chose EVs — market size determines track selection. Hydrogen won't be abandoned but will focus on heavy trucks — a few highway refueling stations can cover all needs."),
    ("Carbon Tax: Stranglehold and New Wealth Code",
     "High-emission companies that don't reform will pay more in carbon taxes than they earn. Tesla earned $1.58B from carbon credits in 2020, while net profit was only $700M+ — effectively another form of carbon tax on companies. Carbon barriers may strangle some nations' low-end manufacturing. Carbon credit investment could be the next opportunity. Zhejiang has already opened 'carbon accounts,' crediting behavior-based scores that feed into policy support — social security years and carbon account scores may factor into housing lottery evaluations."),
    ("From Laborers to Patent Holders: The R&D Power Path",
     "Wind and solar now account for 11% of electricity consumption, targeting 25% by 2030. The future EV industry is vast, capable of supporting millions of R&D personnel and indirectly creating tens of millions of jobs. Manufacturing was unprofitable because R&D and sales were overseas — China only earned meager processing fees. Carbon neutrality means bypassing mature Western patents and developing our own — solar and UHV international standards are already translated from Chinese to English. What you see as obstacles, others see as bounty posters unlocking potential. In the coming decade, carbon neutrality will spawn countless new technologies and ideas, reshaping everyone's life."),
]

ch21_take_zh = """碳中和不是遥远的环境议题，而是接下来十年最重要的事——没有之一。能源本身就是天大的事，与十年前的互联网科技没什么差别。中国已形成光伏+特高压+电动车的新能源闭环，且都跨过了市场化奇点。碳税将成为催命绞索，鞭策高排放企业转型，同时创造巨大的新财富机会。西北地区将变成"超级大油田"，特高压网络取代油轮，挑战石油美元体系。你看到的障碍，别人看到的是商机。这场变革将养活几百万研发人员、创造上千万岗位，重塑每一个普通人的生活。"""
ch21_take_en = """Carbon neutrality isn't a distant environmental topic — it's the single most important thing in the next decade. Energy itself is a monumental matter, no different from the internet revolution a decade ago. China has formed a new energy closed loop of solar + UHV + EVs, all having crossed the marketization singularity. Carbon taxes will be a tightening noose forcing high-emission companies to transform while creating massive new wealth opportunities. Northwest China will become a 'super oil field,' and UHV networks will replace tankers, challenging the petrodollar system. What you see as obstacles, others see as business opportunities. This transformation will support millions of R&D workers, create tens of millions of jobs, and reshape every ordinary person's life."""

# ============================================================
# CHAPTER 22
# ============================================================
ch22_zh = "马斯克和SpaceX凭啥能成事"
ch22_en = "How Did Musk and SpaceX Pull It Off?"
ch22_sub_zh = "以大学生攒电脑的方式攒火箭——美国成熟的太空零件市场是核心土壤"
ch22_sub_en = "Building rockets like college students build PCs — America's mature space parts market is the core soil"

ch22_ov_zh = """作者拜访航天院高级工程师同事，发现他13岁的儿子用淘宝和二手平台攒齐了火箭模型的所有零件——涡轮机、燃料罐、燃烧室、矢量喷口等一应俱全，可编程可遥控。同事感慨：马斯克做的事跟这差不多——美国火箭零件和材料随处可买，成熟、便宜且故障率极低。SpaceX的历程：马斯克2001年参加火星社团，去俄罗斯买火箭未果，回程发现火箭原材料只要售价的3%。找到火箭天才汤姆·穆勒后，两人于2002年创立SpaceX，以"太空电驴"定位专接小卫星发射订单。2006-2008年连炸三次，第四次成功，NASA送来16亿美元大单救了公司。SpaceX把火箭计算机系统从1000万美元降到1万美元，通过多发动机并联和火箭回收技术，成为火箭领域的"价格屠夫"。"""

ch22_ov_en = """The author visited a senior engineer colleague at the space academy and discovered his 13-year-old son had assembled all rocket model parts — turbine, fuel tank, combustion chamber, vector nozzle, etc. — from Taobao and second-hand platforms, programmable and remote-controlled. The colleague remarked: Musk is doing essentially the same thing — in America, rocket parts and materials are readily available, mature, cheap, and extremely reliable. SpaceX's journey: Musk joined a Mars society in 2001, failed to buy rockets from Russia, realized on the return flight that rocket raw materials cost only 3% of the price. After finding rocket genius Tom Mueller, they founded SpaceX in 2002, positioned as a 'space electric scooter' for small satellite launches. 2006-2008: three consecutive explosions, fourth succeeded. NASA's $1.6B contract saved the company. SpaceX slashed the rocket computer system from $10M to $10K, mastered multi-engine parallel and rocket recovery, becoming the 'price butcher' of rocketry."""

ch22_kpis_zh = [
    ("太空电驴", "马斯克的洞见：巨头火箭运力过剩，开发便宜小火箭专接被筛掉的小卫星订单"),
    ("攒火箭模式", "美国成熟的太空零件市场→大学生攒电脑一样攒发动机→60%零件自给，不锈钢替代太空金属"),
    ("1/1000成本", "火箭计算机系统从1000万美元降到1万美元，通过NASA验收；单次发射6200万美元vs同行1.5-3.5亿"),
    ("三次炸出的成功", "2006-2008三次发射全炸，资金只够最后一次——2008年9月28日成功，NASA随后送来16亿美元大单"),
]
ch22_kpis_en = [
    ("Space Electric Scooter", "Musk's insight: giant rockets have excess capacity; build cheap small rockets for filtered-out small satellite orders"),
    ("PC-Building Model", "America's mature space parts market → assemble engines like college students building PCs → 60% self-made parts, stainless steel replacing space-grade metals"),
    ("1/1000th Cost", "Rocket computer system slashed from $10M to $10K, NASA-certified; $62M per launch vs competitors' $150M-$350M"),
    ("Success After Three Explosions", "2006-2008: three launches all exploded, funds only for one more attempt — September 28, 2008 succeeded, NASA followed with $1.6B contract"),
]

ch22_sec_zh = [
    ("土壤决定一切：美国的太空零件市场",
     "同事用某宝和二手平台攒齐火箭模型全部零件——不是给火箭用的但逻辑一样。真正火箭的复杂控制系统软件在美国随处可买，太空材料在其他国家极难获取，在美国很容易。SpaceX以大学生攒电脑的方式攒了火箭发动机——先买零件，壮大后不断优化自给，现已60%自给。马斯克的观点：相同零件，车上用的比火箭上的更稳定可靠，因为前者经历过无数消费者测试，后者只在极少数火箭上测试过——所以才堆叠大量冗余，导致价格高得离谱。"),
    ("太空电驴：被巨头忽略的市场",
     "马斯克在公司内部演讲：超级公司火箭运力极度过剩。很多大学、传媒公司、公益机构都想发卫星——便宜的卫星只要五六万美元，但火箭非常贵。就像想点麻辣烫，但外卖小哥都开卡车送10吨以上的外卖，你只能付卡车运费。如果有一种小而廉价的'太空电驴'，灵活多次配送，你只需付半个烧饼钱的运费就能发卫星。恰好在美国，成熟的太空零件市场让这个想法有了实现的可能。"),
    ("连炸三次：创业者的决心与官僚的恐惧",
     "2006年3月第一次发射——25秒后坠落。2007年第二次——上升很好，然后又炸了。第三次——缓缓升空，又炸了。资金只够最后一次。2008年9月28日第四次——成功。SpaceX炸三次要崩溃了，再炸一次就倒闭。在官僚化组织里，炸三次领导就别干了——所以巨头坚决不研发新型发动机，整个航天业进入老年状态。SpaceX的做法：加了大量检测芯片和复杂算法，一旦检测到发动机故障就停了它——测试几次后技术成熟。"),
    ("价格屠夫：多发动机并联+火箭回收",
     "马斯克两个大胆假设：能攒一台发动机就能攒九台；九台并联装一枚火箭。发动机并联是世界级难题——苏联N1火箭测试四次全炸。SpaceX加检测芯片+算法解决。火箭回收：涉及导航、姿态控制、热防护、推力调整、高空横向推进等技术难点。从2012年验证，四年摔了六次终于成功。单次发射成本6200万美元（还赚30%），同行要1.5-3.5亿美元，且重复发射费用更低。SpaceX不仅吸收美国经验，还广泛吸收全世界经验，包括苏联的栅格翼技术。"),
    ("中国的SpaceX之路：开放民营，两条腿走路",
     "很多人争论民营航天该不该搞——完全没有争论的必要。如果亿万富翁有航天梦，花自己的钱招募牛人研发，做成了成果是社会的，做不成自己倒闭，有啥道理不支持？开放民营就是让民间大神用自己的方法去试试，国家只需要把需要的东西卖给他。2014年中国已开放商业航天准入门槛，已有民企开始搞。不用整天担心SpaceX比我们强，SpaceX试过的路径我们也可以走。宇宙很大，不至于SpaceX进去了我们就没机会。不一定用最漂亮的方式解决问题，哪怕用最笨的方式解决了，也比没解决强。"),
]
ch22_sec_en = [
    ("Soil Determines Everything: America's Space Parts Market",
     "The colleague assembled all rocket model parts from Taobao and second-hand platforms — not for actual rockets but logically identical. Real rocket control system software is readily available in America; space-grade materials extremely hard to get elsewhere but easy in the US. SpaceX built rocket engines like college students building PCs — initially bought parts, then optimized and self-manufactured, now 60% self-made. Musk's insight: identical parts, those in cars are more stable and reliable than those in rockets — the former tested by countless consumers, the latter only by a few rockets, hence excessive redundancy and absurdly high prices."),
    ("Space Electric Scooter: The Market Giants Ignored",
     "Musk's internal speech: giant companies have severely excessive rocket capacity. Many universities, media companies, and nonprofits want to launch satellites — cheap satellites cost only $50-60K, but rockets are incredibly expensive. Like wanting to order hotpot delivery, but all delivery drivers use trucks carrying 10 tons — you pay truck freight for one serving. If there were a small cheap 'space electric scooter,' flexible and reusable, you'd only pay half a pancake's worth of freight to launch your satellite. In America, the mature space parts market made this vision possible."),
    ("Three Explosions: Entrepreneurial Grit vs Bureaucratic Fear",
     "March 2006 first launch — fell after 25 seconds. 2007 second launch — climbed well, then exploded again. Third launch — slowly ascended, exploded again. Funds only for one last attempt. September 28, 2008, fourth launch — success. SpaceX was crumbling after three explosions; one more would mean bankruptcy. In a bureaucratic organization, three explosions would end leadership careers — so giants stubbornly refused to develop new engines; the entire space industry entered geriatric mode. SpaceX's approach: added numerous detection chips and complex algorithms — upon detecting an engine fault, shut it down. After several tests, the technology matured."),
    ("Price Butcher: Multi-Engine Parallel + Rocket Recovery",
     "Musk's two bold assumptions: if you can build one engine, you can build nine; connect nine engines in parallel on one rocket. Engine parallelization is a world-class challenge — Soviet N1 rocket tested four times, all exploded. SpaceX solved it with detection chips + algorithms. Rocket recovery involves navigation, attitude control, thermal protection, thrust adjustment, and high-altitude lateral propulsion — extreme difficulty. Verified from 2012, crashed six times over four years before success. Single launch cost $62M (still 30% profit) vs competitors' $150M-$350M, and costs drop further with reuse. SpaceX absorbed not just American experience but worldwide experience, including Soviet grid fin technology."),
    ("China's SpaceX Path: Open Private Sector, Walk on Two Legs",
     "Many debate whether private space ventures should be allowed — there's no argument against it. If a billionaire has a space dream, spends their own money recruiting talent for R&D, success benefits society, failure costs themselves — why not support it? Opening private space means letting civilian geniuses try their own methods; the state just needs to sell them what they need. China opened commercial space access in 2014, and private companies have already started. No need to constantly worry about SpaceX being ahead — we can walk the path SpaceX tested. Space is vast; SpaceX entering doesn't mean we have no opportunity. You don't need the prettiest solution — even the dumbest solution beats no solution at all."),
]

ch22_take_zh = """马斯克和SpaceX的成功不是魔法——是美国几十年航天工业土壤的厚积薄发。成熟的太空零件市场让"大学生攒电脑式"造火箭成为可能。真正的厉害之处不是理论或想法，而是敢选中一个方案、承担风险、一直走下去。三次炸掉火箭，资金只够最后一次——这种孤注一掷在任何官僚组织里都是不可能的。中国已开放商业航天，两条腿走路。不必焦虑，SpaceX走过的路我们也可以走。宇宙够大，机会够多。不一定用最漂亮的方式，哪怕用最笨的方式解决了问题，也比没解决强。"""
ch22_take_en = """Musk and SpaceX's success isn't magic — it's the culmination of decades of American aerospace industrial soil. The mature space parts market made 'PC-building-style' rocket construction possible. True greatness isn't about theories or ideas — it's about daring to pick a plan, bearing the risk, and persisting all the way. Three rockets exploded, funds only for one last attempt — such all-in commitment is impossible in any bureaucratic organization. China has opened commercial space, walking on two legs. Don't be anxious — we can walk the path SpaceX tested. The universe is vast enough, opportunities abound. You don't need the prettiest solution — even the dumbest solution beats no solution at all."""

# ============================================================
# CHAPTER 23
# ============================================================
ch23_zh = "被ChatGPT淘汰的人，其实早就被淘汰了"
ch23_en = "People 'Eliminated' by ChatGPT Were Already Eliminated"
ch23_sub_zh = "工具的绝对平等与使用者的绝对不平等——复杂工具从不属于所有人"
ch23_sub_en = "Absolute equality of tools meets absolute inequality of users — complex tools never belonged to everyone"

ch23_ov_zh = """作者观察到：随手可搜到的东西，绝大部分人却疯狂传谣——人们害怕搜出来的结果跟自己想的不一样。这个问题同样移植到了ChatGPT上：需要精确描述自己想要什么，但大部分人做不到。生活像一个竞技场，里面摆着从木棍到机枪的各种武器，绝大部分人选择的是操作简单的菜刀。搜索引擎作为一种彻底公开的工具，对多数人无感，只成了极少数人的利器。ChatGPT本质依旧是搜索引擎做了二次加工——不管什么工具，最后还是依赖操作它的人。同样的工具在不同人手里效果差距远超木棍和核武器的差别。没必神化工具也不要小看工具。保持开放拥抱进化——如果改变不了趋势，就尽量站在趋势那一边。"""

ch23_ov_en = """The author observes: things easily searchable are wildly misrepresented by most people — they fear search results that contradict their beliefs. The same issue transfers to ChatGPT: you need to precisely describe what you want, but most can't. Life is like an arena with weapons from sticks to machine guns — most choose the easy-to-use cleaver. Search engines, as thoroughly public tools, are imperceptible to the majority and became weapons for only a tiny minority. ChatGPT is essentially a search engine with secondary processing — regardless of the tool, it ultimately depends on the person operating it. The same tool in different hands yields gaps far exceeding the difference between a stick and a nuke. Don't deify tools nor underestimate them. Stay open, embrace evolution — if you can't change the trend, stand on its side."""

ch23_kpis_zh = [
    ("工具不平等", "生活竞技场里武器从木棍到机枪应有尽有，绝大部分人选择菜刀——使用者的不平等远超工具的平等"),
    ("描述能力", "搜索引擎和ChatGPT都需要精确描述自己想要什么——这是一个稀缺技能，多数人根本做不到"),
    ("信息流vs思想流", "信息流工作（抄新闻+评论）迟早被AI取代；思想流工作（主观+创意+未知需求）短时间无法取代"),
    ("进化模式", "美国的分散试错模式=允许犯错→形成选择池→应对未知——一旦进入无人区，没有比进化更好的办法"),
]
ch23_kpis_en = [
    ("Tool Inequality", "Life's arena offers weapons from sticks to machine guns — most choose the cleaver. User inequality far exceeds tool equality"),
    ("Description Ability", "Both search engines and ChatGPT require precisely describing what you want — a rare skill most people simply don't possess"),
    ("Information Flow vs Thought Flow", "Information flow jobs (copying news + commentary) will eventually be replaced by AI; thought flow jobs (subjective + creative + unknown needs) won't be replaced soon"),
    ("Evolution Model", "America's distributed trial-and-error = allowing mistakes → forming a selection pool → confronting the unknown. Once in uncharted territory, nothing beats evolution"),
]

ch23_sec_zh = [
    ("搜索引擎的预言：公开工具的残酷真相",
     "随手可搜到的东西，绝大部分人疯狂传谣。不是大家懒得打开搜索引擎——是害怕搜出来的结果跟自己想的不一样，干脆坚决不去用。更重要的是'目标描述'能力：用几个关键词让搜索引擎知道自己想要什么，是个稀缺技能。搜索引擎作为一种彻底公开的工具，对多数人无感，只成了极少数人的利器。一位医学专业出身的技术大牛靠着谷歌混成了技术大牛——不同的人运用同样的工具，结果天差地别。"),
    ("生活竞技场：菜刀vs机枪",
     "生活像一个竞技场，里面木棍到机枪应有尽有。绝大部分人选择的却是操作简单容易上手的菜刀，而不是有一定学习成本的机枪。最后看似公平的竞赛，因为工具差别变成了一方单方面的挨打。'技术的公共性'和'使用者的不平等性'——论文库、各种教程都是封建社会要派重兵把守的'国家机密'，如今无差别展示给普通人，绝大部分人硬是视而不见。"),
    ("ChatGPT的真相：它不会大规模改变什么",
     "如果之前的搜索引擎没有改变大部分人的生活，ChatGPT又能改变什么呢？大概率喧闹过后人们恢复平静，ChatGPT变成少数人天天用的工具，大部分人非必要不会去碰。ChatGPT本质依旧是搜索引擎做了二次加工——它的信息源是网络，已经有多次发现它的东西也不对。确认信息真实性仍然需要交叉对比、上溯原始出处、看有没有论文支持。不管什么工具，最后依赖的还是操作它的人。"),
    ("信息流vs思想流：你的工作安全吗？",
     "财经小编把网上新闻汇编加几句评论推送出来——典型的'信息流'，迟早被AI取代，因为AI比你快、准，老板不用上社保。但如果面对的东西主观性很强，客户自己都不知道自己想要什么，或需要大量的想法——这种'思想流'工作短时间内AI不太能胜任，反而会成为你的帮手。Excel出现时大家惊呼要改变职场，结果只是让工作更琐碎。'琐碎'是自动化的大敌——做服装的小老板上了机械臂，还得配几个人专门伺候它。大公司里绝大部分人都是围绕几个关键核心在转。"),
    ("拥抱进化：站在趋势那一边",
     "技术最难的是'可行性研究'——不知道哪条路能走通。一旦路线被证实可行，后发国家堆资源就能赶上。但一旦进入无人区，没有比进化模式更好的办法——美国的分散试错就是用企业家的试错成本来建立选择池。允许犯错是进化必不可少的前提：当下的错误可能是未来的优势，如今的皇冠可能是下一个时代的累赘。如果改变不了趋势，就尽量让自己站在趋势那一边。唯一能做的，就是平时主动用这些工具，不断提升使用技巧。"),
]
ch23_sec_en = [
    ("Search Engines' Prophecy: The Harsh Truth of Public Tools",
     "Things easily searchable are wildly misrepresented. It's not laziness — people fear search results that contradict their beliefs, so they refuse to use search engines at all. More crucially, 'target description' ability: using keywords to make search engines understand what you want is a rare skill. As a thoroughly public tool, search engines are imperceptible to most and became weapons for only a tiny minority. A medical-school dropout became a tech expert purely through Google — same tools, wildly different outcomes."),
    ("Life's Arena: Cleaver vs Machine Gun",
     "Life is an arena stocked with everything from sticks to machine guns. Yet most choose the easy-to-use cleaver over the machine gun with a learning curve. A seemingly fair competition becomes one-sided slaughter due to tool disparity. 'Technology's public nature' vs 'user inequality' — academic databases, countless tutorials, all would have been 'state secrets' guarded by armies in feudal times, now displayed indiscriminately to everyone, yet most people are simply blind to them."),
    ("The Truth About ChatGPT: It Won't Massively Change Anything",
     "If previous search engines didn't change most people's lives, what can ChatGPT change? Most likely, after the noise dies down, people return to normal — ChatGPT becomes a tool a few use daily, most won't touch unless necessary. ChatGPT is essentially a search engine with secondary processing — its sources are online, and it has already been found wrong multiple times. Verifying information still requires cross-referencing, tracing original sources, checking for academic paper support. No matter the tool, it ultimately depends on the person operating it."),
    ("Information Flow vs Thought Flow: Is Your Job Safe?",
     "Financial news editors who compile online news and add bland commentary — classic 'information flow,' eventually replaced by AI because AI is faster, more accurate, and needs no social insurance. But if you face highly subjective matters, clients who don't know what they want, or situations requiring massive ideation — such 'thought flow' work won't be replaced by AI soon and may become your assistant. When Excel appeared, people predicted it would transform the workplace; it just made work more tedious. 'Tedium' is automation's enemy — a garment shop owner added a robotic arm but then hired people just to serve it. In big companies, most people orbit around a few key cores."),
    ("Embrace Evolution: Stand on the Side of Trends",
     "Technology's hardest part is 'feasibility research' — not knowing which path works. Once a path is proven viable, latecomer nations can pour resources and catch up. But in uncharted territory, nothing beats the evolution model — America's distributed trial-and-error uses entrepreneurs' failure costs to build a selection pool. Allowing mistakes is an essential prerequisite for evolution: today's errors may be tomorrow's advantages; today's crown may be the next era's burden. If you can't change the trend, stand on its side. The only thing you can do: proactively use these tools daily and continuously improve your skills."),
]

ch23_take_zh = """被ChatGPT淘汰的人，其实早就被搜索引擎淘汰了。工具的绝对平等掩盖了使用者的绝对不平等——生活竞技场里武器应有尽有，大部分人却选了菜刀。ChatGPT不会大规模改变世界，就像Google没有改变大多数人的生活一样。关键区别在于你的工作是"信息流"还是"思想流"：前者迟早被AI取代，后者反而能借助AI如虎添翼。中国在跟踪成熟路径上优势明显，但一旦进入无人区，美国的进化模式——允许犯错、分散试错——是最有效的应对。不要神化工具，也不要抗拒工具。如果改变不了趋势，就尽量站到趋势那一边。"""
ch23_take_en = """People 'eliminated' by ChatGPT were already eliminated by search engines. Absolute tool equality masks absolute user inequality — life's arena has every weapon imaginable, yet most choose the cleaver. ChatGPT won't massively change the world, just as Google didn't change most people's lives. The key distinction is whether your work is 'information flow' or 'thought flow': the former will eventually be replaced by AI; the latter can use AI as a force multiplier. China excels at following proven paths, but in uncharted territory, America's evolution model — allowing mistakes, distributed trial-and-error — is most effective. Don't deify tools nor resist them. If you can't change the trend, stand on its side."""

# ============================================================
# CHAPTER 24
# ============================================================
ch24_zh = "技术革新痛点太多，但我们必须主动拥抱"
ch24_en = "Tech Innovation Has Many Pain Points, But We Must Actively Embrace It"
ch24_sub_zh = "机器人大规模替代人力已是必然——唯一不变的就是变化本身"
ch24_sub_en = "Massive robotic replacement of human labor is inevitable — the only constant is change itself"

ch24_ov_zh = """2014年AI科学家说了一个反直觉的事实：中国加入WTO后，几亿农民进城以西方工人零头的工资接收产能，一度封死了西方机器人产业。富士康出事后开始思考用机器人替代人工，但进展不顺——手机组装部分烦琐无技术含量，用机器人成本比人工高。但随着用工成本持续上升，工业机器人已成共识：2022年中国装备30万台（全球一半），1台顶3个工人，每年替代约100万劳动力。回顾科技史：技术进步从来不只带来好处——英国工业革命后少量资本家更富、大部分人更穷，引发了工人运动。上一时代的王冠是下一时代的累赘：国企编制、一铺养三代，都曾被新技术颠覆。但变化无法避免——只能持续学习，不断适应。"""

ch24_ov_en = """An AI scientist shared a counterintuitive fact in 2014: China's WTO entry brought hundreds of millions of farmers-turned-workers into cities at a fraction of Western wages, temporarily killing the Western robot industry. After the Foxconn incidents, thoughts turned to robotic replacement, but progress was poor — phone assembly is tedious but low-skill, and robots cost more than humans. But as labor costs keep rising, industrial robots are now consensus: China deployed 300,000 in 2022 (half the global total), 1 robot replaces 3 workers, replacing ~1M workers annually. Looking at tech history: advances never just bring benefits — post-Industrial Revolution Britain saw a few capitalists get richer while most got poorer, sparking worker movements. The previous era's crown is the next era's burden: state-owned jobs, 'one shop feeds three generations' — all disrupted by new technology. But change is unavoidable — only continuous learning and adaptation remain."""

ch24_kpis_zh = [
    ("机器人替代加速", "2022年中国装备30万台工业机器人（全球50%），1台顶3个工人，年均替代100万劳动力，10年后替代几千万"),
    ("技术的历史代价", "英国工业革命后工匠失业、童工盛行——新技术大幅提升效率的同时让大部分人利益受损"),
    ("皇冠变累赘", "国企编制、一铺养三代……上一时代的王冠往往是下一时代的累赘——大家现在珍视的很多东西将面临重新估值"),
    ("购买力危机", "机器人不领工资→大规模失业→购买力下降→产能过剩危机→需要利益转移和社会保障托底"),
]
ch24_kpis_en = [
    ("Robot Replacement Accelerating", "China deployed 300K industrial robots in 2022 (50% global), 1 robot=3 workers, replacing ~1M/year, tens of millions in a decade"),
    ("Technology's Historical Cost", "Post-Industrial Revolution Britain: artisans unemployed, child labor rampant — new tech dramatically raises efficiency while harming most people's interests"),
    ("Crown Becomes Burden", "State-owned jobs, 'one shop feeds three generations' — the previous era's crown is often the next era's burden. Many things we cherish now face revaluation"),
    ("Purchasing Power Crisis", "Robots earn no wages → mass unemployment → purchasing power decline → overcapacity crisis → need wealth redistribution and social safety nets"),
]

ch24_sec_zh = [
    ("WTO与机器人的悖论：廉价劳动力封死了创新",
     "20世纪欧美劳动力太贵，资本家大规模研发机械臂。中国加入WTO后，几亿农民进城以西方工人零头的工资接收产能。机器人的公司顿时没了订单，大规模倒闭。富士康出事后开始思考用机器人替代人工——但手机组装烦琐无技术含量，机器人成本比人工高得多。直到中国用工成本持续上升，开发机器人才重新成为整个工业界的共识。2022年中国装备了30万台工业机器人——全世界一半卖到了中国——而且机器人不休息，一台顶三个工人。"),
    ("技术从来不只是技术：工业革命的黑暗面",
     "英国工业革命后国力迅速增长，但建立在毁灭性破坏基础上。早期制造业靠一技之长的工匠进入中产，工业革命后机器替代手艺，工人只需做几个机械动作。作坊倒闭，工厂雇用童工——孩子把父母的工作抢了。少量资本家更富，绝大部分人更穷——引发风起云涌的工人运动，直到一战后工人才重新好起来。技术在提升全社效率的同时让大部分人利益受损→人起来闹→社会制度变革→达到新平衡。这就是技术附带的社会学属性。"),
    ("皇冠变累赘：被新科技颠覆的旧资产",
     "上一次时代的王冠往往是下一次时代的累赘。曾经最看重的国企编制，面对新技术新管理冲击，陈旧低效的国企成了累赘，于是有了下岗潮。曾经'一铺养三代'，移动互联网崛起后店铺受前所未有的冲击，大量贷款买店铺的人成了超级韭菜。大家现在珍视的很多东西，再过一些年将面临重新估值。制造业将经受'重塑'级别变革，低级白领也会受AI冲击——财经小编被取代跟玩似的。"),
    ("购买力危机：机器人不领工资的后果",
     "工业革命后产能一直是过剩的，稀缺的从来就是购买力。机器人大规模替代人力→工人失业→购买力下降→商品卖不出去→企业倒闭。美国某总统候选人提出加税补贴百姓——大公司雇很少人生很多商品赚很多钱，长期有害。欧洲福利社会、日本僵尸企业，本质都是养闲人。机器人革命让少数公司变富可敌国，只能由它们出钱养没工作的人，维持凑合活下去的标准。想过得好，还是得自己想办法。"),
    ("拥抱变革：唯一不变的就是变化本身",
     "日本三十年没进展的关键原因：老百姓极度反感变革，对稳定有近乎变态的渴望——每次混不下去了才咬牙变革一次，然后精雕细琢形成极度稳定状态。英国因保守被美德内燃机和电力革命超越。中国加入WTO发展快是因为起点低，往哪走都是进步，改革阻力小。如今进入深水区是因为形成了大量既得利益阶层。但新技术的应用让国力迅速提升，产业工人只能去服务业。智能革命不可避免——只能持续学习、不断适应。毕竟，这世界唯一不变的，可能就是变化本身了。"),
]
ch24_sec_en = [
    ("WTO and the Robot Paradox: Cheap Labor Killed Innovation",
     "In the 20th century, expensive Western labor drove massive robotic arm R&D. After China joined WTO, hundreds of millions of farmers-turned-workers accepted production capacity at a fraction of Western wages. Robot companies instantly lost orders and went bankrupt en masse. After Foxconn incidents, thoughts turned to robotic replacement — but phone assembly is tedious and low-skill, and robots cost far more than humans. Only as China's labor costs kept rising did robot development become industry consensus again. In 2022, China deployed 300K industrial robots — half the world's total — and robots don't rest, one equals three workers."),
    ("Technology Is Never Just Technology: The Dark Side of Industrial Revolution",
     "Post-Industrial Revolution Britain's national power surged, but built on destructive foundations. Early manufacturing relied on skilled artisans who entered the middle class; after the revolution, machines replaced craftsmanship, workers only needed a few mechanical motions. Workshops closed, factories hired child labor — children stole their parents' jobs. A few capitalists got richer, most got poorer — triggering surging worker movements; only after WWI did workers' conditions improve. Technology dramatically raises social efficiency while harming most → people rise up → social systems change → new equilibrium. This is technology's sociological dimension."),
    ("Crown Becomes Burden: Old Assets Disrupted by New Tech",
     "The previous era's crown is often the next era's burden. Once-prized state-owned job positions, facing new tech and management, became burdens as obsolete, inefficient SOEs — leading to mass layoffs. Once 'one shop feeds three generations' — mobile internet's rise devastated storefronts; heavily leveraged shop buyers became ultimate bag-holders. Many things we cherish now face revaluation in coming years. Manufacturing will undergo 'remaking'-level transformation; low-level white-collar jobs will also be hit by AI — financial editors replaced as easily as playing games."),
    ("Purchasing Power Crisis: The Consequence of Robots Earning No Wages",
     "Since the Industrial Revolution, capacity has always been excessive — what's scarce is purchasing power. Massive robotic labor replacement → worker unemployment → purchasing power decline → goods can't sell → companies fail. A US presidential candidate proposed taxing big companies to subsidize ordinary people — companies employing few people, producing many goods, making huge profits is harmful long-term. Europe's welfare society, Japan's zombie companies — all essentially supporting idle populations. The robot revolution makes a few companies unimaginably wealthy; they'll have to fund those without work, maintaining a bare survival standard. To live well, you must find your own way."),
    ("Embrace Change: The Only Constant Is Change Itself",
     "Japan's 30-year stagnation has a key rarely mentioned cause: citizens extremely resent change, with an almost pathological craving for stability — only changing when cornered, then meticulously polishing into extreme stasis. Britain was overtaken by US and Germany's combustion engine and electricity revolution because of conservatism. China developed fast after WTO because the starting point was low — any direction was progress, reform faced little resistance. Now in 'deep water' because massive vested interest layers have formed. But new technology applications dramatically boost national power; industrial workers can only go to services. The intelligent revolution is unavoidable — only continuous learning and adaptation remain. After all, the only constant in this world may be change itself."),
]

ch24_take_zh = """技术革新带来阵痛，但我们必须主动拥抱。从英国工业革命到当代机器人革命，技术总是在大幅提升效率的同时让大部分人利益受损——然后社会制度变革达到新平衡。上一时代的王冠往往是下一时代的累赘：国企编制、一铺养三代，都曾被新科技颠覆。机器人革命不可逆——中国已占全球一半的工业机器人装机量。购买力危机会倒逼利益转移和社会保障完善。日本停滞三十年的教训就是抗拒变革。唯一不变的就是变化本身——持续学习、不断适应，是每个人在变革时代的生存之道。"""
ch24_take_en = """Tech innovation brings pain, but we must actively embrace it. From Britain's Industrial Revolution to today's robot revolution, technology dramatically raises efficiency while harming most people's interests — then social systems change to reach new equilibrium. The previous era's crown is often the next era's burden: state-owned jobs, 'one shop feeds three generations' — all disrupted by new tech. The robot revolution is irreversible — China already accounts for half the world's industrial robot installations. The purchasing power crisis will force wealth redistribution and social safety net improvements. Japan's 30-year stagnation lesson is resistance to change. The only constant is change itself — continuous learning and adaptation are everyone's survival strategy in transformational times."""


# ============================================================
# GENERATE ALL FILES
# ============================================================
chapters = [
    (19, ch19_zh, ch19_en, ch19_sub_zh, ch19_sub_en, ch19_ov_zh, ch19_ov_en,
     ch19_kpis_zh, ch19_kpis_en, ch19_sec_zh, ch19_sec_en, ch19_take_zh, ch19_take_en),
    (20, ch20_zh, ch20_en, ch20_sub_zh, ch20_sub_en, ch20_ov_zh, ch20_ov_en,
     ch20_kpis_zh, ch20_kpis_en, ch20_sec_zh, ch20_sec_en, ch20_take_zh, ch20_take_en),
    (21, ch21_zh, ch21_en, ch21_sub_zh, ch21_sub_en, ch21_ov_zh, ch21_ov_en,
     ch21_kpis_zh, ch21_kpis_en, ch21_sec_zh, ch21_sec_en, ch21_take_zh, ch21_take_en),
    (22, ch22_zh, ch22_en, ch22_sub_zh, ch22_sub_en, ch22_ov_zh, ch22_ov_en,
     ch22_kpis_zh, ch22_kpis_en, ch22_sec_zh, ch22_sec_en, ch22_take_zh, ch22_take_en),
    (23, ch23_zh, ch23_en, ch23_sub_zh, ch23_sub_en, ch23_ov_zh, ch23_ov_en,
     ch23_kpis_zh, ch23_kpis_en, ch23_sec_zh, ch23_sec_en, ch23_take_zh, ch23_take_en),
    (24, ch24_zh, ch24_en, ch24_sub_zh, ch24_sub_en, ch24_ov_zh, ch24_ov_en,
     ch24_kpis_zh, ch24_kpis_en, ch24_sec_zh, ch24_sec_en, ch24_take_zh, ch24_take_en),
]

import os

for ch_num, zh_t, en_t, zh_sub, en_sub, zh_ov, en_ov, zh_k, en_k, zh_s, en_s, zh_tk, en_tk in chapters:
    for lang in ("zh", "en"):
        head = html_head(ch_num, zh_t, en_t, lang, zh_sub, en_sub)
        ov = overview_section(zh_ov, en_ov, lang)
        kpi = kpi_section(zh_k, en_k, lang)
        sec = sections_html(zh_s, en_s, lang)
        tk = takeaway_section(zh_tk, en_tk, lang)
        ft = footer(lang)
        html = head + ov + kpi + sec + tk + ft
        lang_suffix = "zh" if lang == "zh" else "en"
        fname = f"弹性生长-ch{ch_num:03d}-info-{lang_suffix}.html"
        path = os.path.join(OUT, fname)
        with open(path, "w", encoding="utf-8") as f:
            f.write(html)
        size = len(html)
        print(f"✅ {fname}  ({size:,} bytes)")

print("\n🎉 All 12 files generated!")