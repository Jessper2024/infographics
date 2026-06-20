#!/usr/bin/env python3
import os
base = os.path.expanduser("~/.openclaw/workspace/infographics/books")

def css():
    return '''  @font-face {
    font-family: 'FZXPYZS';
    src: url('../方正屏显雅宋简体.TTF') format('truetype');
    font-weight: normal; font-style: normal;
  }
  * { margin: 0; padding: 0; box-sizing: border-box; }
  body {
    background: #f5f1eb;
    font-family: 'FZXPYZS', 'PingFang SC', 'Noto Serif SC', 'STSong', Georgia, serif;
    display: flex; justify-content: center; align-items: flex-start;
    min-height: 100vh; padding: 40px 20px 60px;
  }
  .container { max-width: 880px; width: 100%; }

  .lang-switch { text-align: right; margin-bottom: 16px; }
  .lang-btn {
    display: inline-block; padding: 6px 16px; border-radius: 8px;
    font-size: 13px; text-decoration: none; letter-spacing: 0.03em;
    font-family: 'FZXPYZS', 'PingFang SC', 'Noto Serif SC', serif;
    background: #fef2f2; color: #dc2626; border: 1px solid #fecaca;
    transition: opacity 0.15s;
  }
  .lang-btn:hover { opacity: 0.75; }

  .back-catalog {
    text-align: left; margin-bottom: 8px;
  }
  .back-catalog a {
    font-size: 13px; color: #4f46e5; text-decoration: none;
    font-family: 'FZXPYZS', 'PingFang SC', 'Noto Serif SC', serif;
  }
  .back-catalog a:hover { text-decoration: underline; }

  h1 {
    font-family: 'FZXPYZS', 'PingFang SC', 'Noto Serif SC', serif;
    font-size: 36px; color: #1a1a1a; text-align: center;
    line-height: 1.4; margin-bottom: 8px; font-weight: normal;
    letter-spacing: 1.5px;
  }
  .subtitle {
    text-align: center; font-family: 'FZXPYZS', 'PingFang SC', 'Noto Serif SC', serif;
    font-size: 14px; color: #888; margin-bottom: 24px; line-height: 1.7;
    max-width: 640px; margin-left: auto; margin-right: auto;
  }
  .divider {
    width: 60px; height: 3px;
    background: linear-gradient(90deg, #dc2626, #ea580c);
    margin: 0 auto 28px; border-radius: 2px;
  }

  .splash {
    background: #ffffff; border: 1px solid #e8e0d5; border-radius: 14px;
    padding: 28px 32px; margin-bottom: 24px; color: #555;
    font-size: 15px; line-height: 2.0;
    box-shadow: 0 1px 3px rgba(0,0,0,0.04);
    border-left: 4px solid #4f46e5;
  }

  .kpi-row {
    display: grid; grid-template-columns: repeat(4, 1fr); gap: 12px;
    margin-bottom: 24px;
  }
  .kpi-card {
    background: #ffffff; border: 1px solid #e8e0d5; border-radius: 12px;
    padding: 16px 12px; text-align: center;
    box-shadow: 0 1px 3px rgba(0,0,0,0.04);
  }
  .kpi-label {
    font-size: 11px; color: #888; margin-bottom: 6px;
    font-family: 'FZXPYZS', 'PingFang SC', 'Noto Serif SC', serif;
    letter-spacing: 1px;
  }
  .kpi-value {
    font-size: 22px; color: #1a1a1a; font-weight: bold;
    font-family: 'FZXPYZS', 'PingFang SC', 'Noto Serif SC', serif;
  }

  .section {
    background: #ffffff; border-radius: 14px;
    margin-bottom: 18px; padding: 24px 28px;
    box-shadow: 0 1px 3px rgba(0,0,0,0.04);
    display: flex; gap: 20px; align-items: flex-start;
    border-left: 4px solid transparent;
  }
  .section-01 { border-left-color: #dc2626; }
  .section-02 { border-left-color: #ea580c; }
  .section-03 { border-left-color: #ca8a04; }
  .section-04 { border-left-color: #4f46e5; }
  .section-05 { border-left-color: #db2777; }

  .section-num {
    flex-shrink: 0; width: 42px; height: 42px; border-radius: 50%;
    display: flex; align-items: center; justify-content: center;
    font-size: 17px; font-weight: bold; margin-top: 2px;
    font-family: 'FZXPYZS', 'PingFang SC', 'Noto Serif SC', serif;
  }
  .num-01 { background: #fef2f2; color: #dc2626; }
  .num-02 { background: #fff7ed; color: #ea580c; }
  .num-03 { background: #fefce8; color: #ca8a04; }
  .num-04 { background: #eef2ff; color: #4f46e5; }
  .num-05 { background: #fdf2f8; color: #db2777; }

  .section-body { flex: 1; }
  .tag {
    display: inline-block; font-size: 11px; font-weight: bold;
    padding: 2px 10px; border-radius: 10px; margin-bottom: 8px;
    letter-spacing: 1px; font-family: 'FZXPYZS', 'PingFang SC', 'Noto Serif SC', serif;
  }
  .tag-01 { background: #fef2f2; color: #dc2626; }
  .tag-02 { background: #fff7ed; color: #ea580c; }
  .tag-03 { background: #fefce8; color: #ca8a04; }
  .tag-04 { background: #eef2ff; color: #4f46e5; }
  .tag-05 { background: #fdf2f8; color: #db2777; }

  .section-title {
    font-size: 18px; margin-bottom: 10px; font-weight: bold; line-height: 1.4;
    font-family: 'FZXPYZS', 'PingFang SC', 'Noto Serif SC', serif;
  }
  .t-01 { color: #dc2626; } .t-02 { color: #ea580c; }
  .t-03 { color: #ca8a04; } .t-04 { color: #4f46e5; }
  .t-05 { color: #db2777; }

  .section-desc {
    font-size: 14px; color: #555; line-height: 1.9; margin-bottom: 14px;
  }

  .dual-grid { display: grid; grid-template-columns: 1fr 1fr; gap: 16px; margin-top: 10px; }
  .dual-card {
    border-radius: 12px; padding: 18px 20px;
    display: flex; gap: 12px; align-items: flex-start;
  }
  .dual-card.yes { background: #f0fdf4; border: 1px solid #bbf7d0; }
  .dual-card.no { background: #fef2f2; border: 1px solid #fecaca; }
  .dual-icon { font-size: 24px; flex-shrink: 0; line-height: 1; }
  .dual-text h4 { font-size: 14px; color: #1a1a1a; margin-bottom: 4px; font-family: 'FZXPYZS', 'PingFang SC', 'Noto Serif SC', serif; }
  .dual-text p { font-size: 12px; color: #777; line-height: 1.6; }

  .flow-row {
    display: flex; align-items: center; gap: 8px; flex-wrap: wrap;
    margin-top: 6px;
  }
  .flow-step {
    background: #fff7ed; border: 1px solid #fed7aa; border-radius: 10px;
    padding: 10px 12px; text-align: center; min-width: 80px; flex: 1;
    font-size: 13px; color: #9a3412; line-height: 1.5; font-weight: bold;
  }
  .flow-arrow { font-size: 20px; color: #ea580c; flex-shrink: 0; font-weight: bold; }
  .flow-step.end { background: #fef2f2; border-color: #fecaca; color: #991b1b; }

  .risk-bars { margin-top: 10px; }
  .risk-row { display: flex; align-items: center; gap: 12px; margin-bottom: 10px; }
  .risk-label { font-size: 13px; color: #555; width: 130px; flex-shrink: 0; font-family: 'FZXPYZS', 'PingFang SC', 'Noto Serif SC', serif; }
  .risk-meter { flex: 1; height: 10px; background: #eef2ff; border-radius: 5px; overflow: hidden; }
  .risk-fill { height: 100%; border-radius: 5px; background: #4f46e5; }
  .risk-val { font-size: 13px; font-weight: bold; color: #4f46e5; width: 50px; text-align: right; flex-shrink: 0; }

  .data-row { display: grid; grid-template-columns: 1fr 1fr 1fr; gap: 12px; margin-top: 10px; }
  .data-card {
    border-radius: 12px; padding: 20px 16px; text-align: center;
    border: 1px solid #fce7f3;
  }
  .data-card.d1 { background: #fdf2f8; border-color: #f9a8d4; }
  .data-card.d2 { background: #fdf2f8; border-color: #f9a8d4; }
  .data-card.d3 { background: #fdf2f8; border-color: #f9a8d4; }
  .data-big { font-size: 28px; margin-bottom: 6px; }
  .data-name { font-size: 15px; font-weight: bold; color: #831843; margin-bottom: 6px; font-family: 'FZXPYZS', 'PingFang SC', 'Noto Serif SC', serif; }
  .data-sm { font-size: 12px; color: #9d174d; line-height: 1.6; }

  .takeaway {
    background: #ffffff; border: 1px solid #e8e0d5; border-radius: 14px;
    padding: 24px 32px; margin-bottom: 18px;
    box-shadow: 0 1px 3px rgba(0,0,0,0.04);
    border-left: 4px solid #dc2626;
  }
  .takeaway-label {
    font-family: 'FZXPYZS', 'PingFang SC', 'Noto Serif SC', serif;
    font-size: 12px; color: #dc2626; letter-spacing: 2px; margin-bottom: 6px;
    font-weight: bold;
  }
  .takeaway-text {
    font-size: 16px; color: #1a1a1a; line-height: 1.9;
    font-family: 'FZXPYZS', 'PingFang SC', 'Noto Serif SC', serif;
  }

  .footer {
    text-align: center; margin-top: 32px; padding-top: 20px;
    border-top: 1px solid #e8e0d5; color: #bbb; font-size: 13px; line-height: 1.8;
  }

  @media (max-width: 640px) {
    .section { flex-direction: column; align-items: center; text-align: center; border-left: none; border-top: 4px solid transparent; padding-top: 20px; }
    .section-01 { border-top-color: #dc2626; }
    .section-02 { border-top-color: #ea580c; }
    .section-03 { border-top-color: #ca8a04; }
    .section-04 { border-top-color: #4f46e5; }
    .section-05 { border-top-color: #db2777; }
    .section-body { text-align: center; }
    .dual-grid { grid-template-columns: 1fr; }
    .flow-row { flex-direction: column; }
    .flow-arrow { transform: rotate(90deg); }
    .kpi-row { grid-template-columns: repeat(2, 1fr); }
    .data-row { grid-template-columns: 1fr; }
  }'''

zh_nums = {5:'五',6:'六',7:'七',8:'八'}
en_ord = {5:'Five',6:'Six',7:'Seven',8:'Eight'}

def gen_html(lang, chap_num, title_en, zh_title, subtitle, overview, kpis, sections, takeaway_text, footer_info):
    if lang == 'zh':
        h1 = f'楚汉双雄 · 第{zh_nums[chap_num]}章「{zh_title}」'
        en_file = f'楚汉双雄-ch{chap_num:03d}-info-en.html'
        lang_label = 'EN'
        catalog = '← 返回章节目录'
    else:
        h1 = f'The Chu-Han Contention · Chapter {en_ord[chap_num]}「{title_en}」'
        en_file = f'楚汉双雄-ch{chap_num:03d}-info-zh.html'
        lang_label = '中文'
        catalog = '← Back to Catalog'

    html_lang = 'zh-CN' if lang == 'zh' else 'en'

    sec_html = ''
    for i, s in enumerate(sections):
        n = i + 1
        tag = s.get('tag', '')
        title = s.get('title', '')
        desc = s.get('desc', '')
        extra = s.get('extra', '')
        sec_html += f'''    <!-- Section {n} / {n:02d} -->
    <div class="section section-{n:02d}">
      <div class="section-num num-{n:02d}">{n:02d}</div>
      <div class="section-body">
        <span class="tag tag-{n:02d}">{tag}</span>
        <div class="section-title t-{n:02d}">{title}</div>
        <div class="section-desc">{desc}</div>
{extra}
      </div>
    </div>
'''

    kpi_html = ''
    if kpis:
        kpi_html = '  <div class="kpi-row">\n'
        for k in kpis:
            kpi_html += f'''      <div class="kpi-card">
        <div class="kpi-label">{k[0]}</div>
        <div class="kpi-value">{k[1]}</div>
      </div>
'''
        kpi_html += '  </div>\n'

    return f'''<!DOCTYPE html>
<html lang="{html_lang}">
<head>
<meta charset="UTF-8">
<meta name="viewport" content="width=device-width, initial-scale=1.0">
<title>{h1}</title>
<style>
{css()}
</style>
</head>
<body>
<div class="container">

  <!-- Language Switch -->
  <div class="lang-switch">
    <a class="lang-btn" href="{en_file}" target="_blank">{lang_label}</a>
  </div>

  <!-- Back to Catalog -->
  <div class="back-catalog">
    <a href="楚汉双雄-catalog.html">{catalog}</a>
  </div>

  <!-- Chapter Title -->
  <h1>{h1}</h1>

  <!-- Subtitle -->
  <div class="subtitle">{subtitle}</div>

  <!-- Divider -->
  <div class="divider"></div>

  <!-- Overview -->
  <div class="splash">
    {overview}
  </div>

  <!-- KPI Row -->
{kpi_html}
  <!-- Content Sections -->
{sec_html}
  <!-- Key Takeaway -->
  <div class="takeaway">
    <div class="takeaway-label">{'📌 核心启示' if lang == 'zh' else '📌 KEY TAKEAWAY'}</div>
    <div class="takeaway-text">{takeaway_text}</div>
  </div>

  <!-- Footer -->
  <div class="footer">
{footer_info}
  </div>

</div>
</body>
</html>'''

# ── Chapter 5: 暗度陈仓 ──

ch5_title_zh = '暗度陈仓：月下追回来的"汉中对"'
ch5_title_en = 'Secretly Crossing Chencang: The "Hanzhong Strategy" Retrieved Under the Moon'

ch5_sub_zh = '从萧何月下追韩信到一个月平定三秦——刘邦集团的最强引擎是如何在汉中启动的'
ch5_sub_en = 'From Xiao He chasing Han Xin under the moon to pacifying the Three Qins in one month — how Liu Bang\'s faction ignited its most powerful engine in Hanzhong'

ch5_overview_zh = '<p>公元前206年，刘邦被项羽分封到偏远的巴蜀汉中。在这个"养老之地"，将士纷纷逃亡，连大管家萧何也"跑了"。但萧何并非逃跑，而是月下追回了一位能改变天下格局的天才——韩信。在萧何的力荐下，刘邦以空前隆重的仪式拜韩信为大将。随后，韩信献上"汉中对"，明确指出项羽的四大致命弱点，力主立即打回关中。仅用四个月整军备战，一个月内三路出击、四面开花，秦汉之际第二位"战神"正式登上历史舞台。</p>'
ch5_overview_en = '<p>In 206 BC, Liu Bang was assigned by Xiang Yu to the remote Ba-Shu-Hanzhong region. In this "retirement paradise," soldiers deserted in droves, and even chief steward Xiao He "ran away." But Xiao He wasn\'t fleeing — he was chasing back a genius who could reshape the world: Han Xin. Under Xiao He\'s forceful recommendation, Liu Bang appointed Han Xin as Grand General in an unprecedentedly grand ceremony. Han Xin then presented the "Hanzhong Strategy," identifying Xiang Yu\'s four fatal weaknesses and urging an immediate counterattack on Guanzhong. In just four months of preparation and one month of three-pronged attack, the second "God of War" of the Qin-Han era officially took the stage.</p>'

ch5_kpis_zh = [('韩信拜将', '从未带兵者'), ('还定三秦', '1个月'), ('汉军整编', '10万人'), ('出秦岭通道', '3路并行')]
ch5_kpis_en = [('Han Xin\'s Rise', 'From Nobody'), ('Pacifying 3 Qins', '1 Month'), ('Han Army Size', '100,000 Men'), ('Routes Out', '3 Axes')]

ch5_sections = [
    dict(tag='关键抉择', title='萧何月下追韩信：刘邦的识人之明',
         desc='刘邦被分封到汉中后，将士因看不到希望纷纷逃亡。一天，听说萧何也跑了，刘邦如遭晴天霹雳。但萧何并非逃跑，而是月下追回了韩信。萧何以"国士无双"四字力荐，并说服刘邦以最隆重的仪式拜韩信为大将。全军大惊——一个从未带过兵的人怎么就成了总司令？但刘邦赌的是萧何的眼光，而非韩信的才干。这一赌，赌出了大汉四百年江山。',
         extra='''        <div class="dual-grid">
          <div class="dual-card yes">
            <div class="dual-icon">✅</div>
            <div class="dual-text">
              <h4>刘邦的选择（高明）</h4>
              <p>信任萧何的判断力，以超规格拜将。用仪式感和权威压住老将们的质疑，为韩信创造施展空间。本质上赌的是对"人"的判断力——信的不是韩信，是萧何。</p>
            </div>
          </div>
          <div class="dual-card no">
            <div class="dual-icon">❌</div>
            <div class="dual-text">
              <h4>普通领导的反应（平庸）</h4>
              <p>看履历、看资历、看出身。一个管后勤的无名之辈凭什么当大将？按常理出牌就会错过顶级人才。项羽就是这样错过了韩信——让天才当执戟郎中。</p>
            </div>
          </div>
        </div>'''),
    dict(tag='战略蓝图', title='韩信的"汉中对"：刘邦版的隆中对',
         desc='韩信拜将后，为刘邦分析了项羽的致命弱点：匹夫之勇（不能放手用将）、妇人之仁（舍不得分封利益）、没有原则（任人唯亲定都彭城）、失去民心（坑杀降卒烧杀抢掠）。他明确指出：打回关中的窗口期稍纵即逝——此时关中民心向汉，三秦王民心不稳，一旦章邯巩固统治，再进关中难如登天。这篇"汉中对"让刘邦茅塞顿开，也确认了萧何为何死保韩信——"萧何抢档案，韩信承秦制，你俩是个组合！"',
         extra='''        <div class="risk-bars">
          <div class="risk-row">
            <div class="risk-label">关中民心向汉</div>
            <div class="risk-meter"><div class="risk-fill" style="width:100%"></div></div>
            <div class="risk-val">100%</div>
          </div>
          <div class="risk-row">
            <div class="risk-label">三秦王民心不稳</div>
            <div class="risk-meter"><div class="risk-fill" style="width:85%"></div></div>
            <div class="risk-val">85%</div>
          </div>
          <div class="risk-row">
            <div class="risk-label">项羽失信于天下</div>
            <div class="risk-meter"><div class="risk-fill" style="width:90%"></div></div>
            <div class="risk-val">90%</div>
          </div>
          <div class="risk-row">
            <div class="risk-label">章邯防御能力</div>
            <div class="risk-meter"><div class="risk-fill" style="width:30%"></div></div>
            <div class="risk-val">30%</div>
          </div>
        </div>'''),
    dict(tag='制度建设', title='"韩信申军法"：军事上的全面继承大秦',
         desc='韩信没有凭空创造一套新系统，而是相信一百多年来的正确选择——全面继承秦国的军事制度。这就是"因地制宜的拿来主义"。军功说话、有法可依，整个汉军被拧成一股绳。萧何在后方用"国家操作系统"（秦宫档案）动员战争力量，韩信在前方用秦制训练军队。仅仅四个月，汉中就从三万残兵扩张到十万大军，粮草辎重齐备——刘邦出汉中时已不是那个灰溜溜南下的败军之将了。',
         extra='''        <div class="flow-row">
            <div class="flow-step ">萧何抢秦宫档案</div>
            <div class="flow-arrow">→</div>
            <div class="flow-step ">建立后勤系统</div>
            <div class="flow-arrow">→</div>
            <div class="flow-step ">韩信承秦军制</div>
            <div class="flow-arrow">→</div>
            <div class="flow-step ">整军备战十万</div>
            <div class="flow-arrow">→</div>
            <div class="flow-step end">一个月定三秦</div>
          </div>'''),
    dict(tag='战术天才', title='四面烟雾三路出击：史上唯一成功出秦岭的战例',
         desc='韩信的总思路是"四面烟雾，三路出击"：派老弱病残修褒斜道放烟雾弹；曹参樊哙走祁山道佯攻陇西；灌婴走子午道牵制司马欣；自己率主力出陈仓道。章邯面对多路战报左右为难，只能平均布防。韩信充分发挥了"大有大的难处"的反向逻辑——用多路出击把章邯的兵力劣势放大到极致。一旦突破秦岭，各路迅速集中，永远在人多打人少。韩信出汉中攻关中，成为中国几千年历史中唯一一次成功的战例。此后诸葛亮六出祁山皆无功而返。',
         extra='''        <div class="flow-row">
            <div class="flow-step ">修褒斜道放烟幕</div>
            <div class="flow-arrow">→</div>
            <div class="flow-step ">曹参樊哙出祁山</div>
            <div class="flow-arrow">→</div>
            <div class="flow-step ">灌婴走子午牵制</div>
            <div class="flow-arrow">→</div>
            <div class="flow-step ">韩信主力出陈仓</div>
            <div class="flow-arrow">→</div>
            <div class="flow-step end">三秦大定</div>
          </div>'''),
    dict(tag='战神降临', title='一个月还定三秦：第二位"战神"的完美首秀',
         desc='章邯的老思路没问题：实力不济就收缩。但他面对的是一个永远在人多打人少的对手。韩信的所有调度都是：凉州闹完调回西路军、主力决战引出三秦全部力量、灌婴子午口出场、曹参打阻击引出残余力量后迅速支援。整个还定三秦过程，没有一战是纠结于攻城战的——全是调动出来以野战消灭有生力量。一个月内，除章邯死守废丘外，渭水河谷全部平定。司马欣投降，董翳投降，章邯最终自杀。秦末第二位"战神"正式就位。',
         extra='''        <div class="data-row">
            <div class="data-card d1">
              <div class="data-big">4个月</div>
              <div class="data-name">整军备战</div>
              <div class="data-sm">从三万残兵到十万大军的速度</div>
            </div>
            <div class="data-card d2">
              <div class="data-big">1个月</div>
              <div class="data-name">定三秦</div>
              <div class="data-sm">韩信平定雍、塞、翟三国的总时间</div>
            </div>
            <div class="data-card d3">
              <div class="data-big">唯一</div>
              <div class="data-name">成功纪录</div>
              <div class="data-sm">中国史上唯一一次成功从汉中攻入关中</div>
            </div>
          </div>'''),
]

ch5_takeaway_zh = '韩信出汉中的真正秘密不在"明修栈道暗度陈仓"的戏剧性，而在于三点：出汉时限论（抓住民心窗口期立即行动）、申军法承秦制（不打无准备之仗）、四面出击法（用多路作战放大己方优势）。这三个战略层面的"庙算之胜"，比任何战术花招都重要。刘邦赌萧何的眼光，萧何识韩信的天才，韩信识大势的窗口——三层信任链环环相扣，才是刘邦集团真正启动的核心引擎。'
ch5_takeaway_en = 'The true secret of Han Xin\'s breakout from Hanzhong is not the dramatic "repairing the plank road while secretly crossing Chencang," but three strategic insights: the time-limit doctrine (seizing the window of popular support), military reform by inheriting Qin\'s system (preparing before fighting), and multi-axis assault (amplifying one\'s own advantages). These "temple calculations of victory" mattered far more than any tactical trick. Liu Bang bet on Xiao He\'s judgment, Xiao He recognized Han Xin\'s genius, and Han Xin read the strategic window — this three-layer chain of trust was the core engine that truly launched Liu Bang\'s faction.'

ch5_footer_zh = '渤海小吏 · 楚汉双雄 · 第五章 · 图书信息图<br>\n来源：楚汉双雄（渤海小吏 著，台海出版社，2020）'
ch5_footer_en = 'Bohai Xiaoli · The Chu-Han Contention · Chapter 5 · Book Infographic<br>\nSource: The Chu-Han Contention (by Bohai Xiaoli, Taihai Press, 2020)'

# ── Chapter 6: 彭城大屠杀 ──

ch6_title_zh = '彭城大屠杀："西楚霸王"的闪电战'
ch6_title_en = 'The Pengcheng Massacre: The "Hegemon-King of Western Chu\'s" Blitzkrieg'

ch6_sub_zh = '项羽三万铁骑如何用一次闪电奔袭击溃刘邦的五十六万诸侯联军——大胜与大败之间只隔了一夜'
ch6_sub_en = 'How Xiang Yu crushed Liu Bang\'s 560,000-strong coalition army with 30,000 cavalry in a single lightning raid — the thin line between total victory and catastrophic defeat'

ch6_overview_zh = '<p>公元前205年四月，刘邦趁项羽深陷齐国泥潭，率五十六万诸侯联军攻占了项羽的都城彭城。然而仅仅一个月后，项羽亲率三万精骑从齐国闪电回师，先击破樊哙北面防线，再走泗水线直插萧县，拂晓闪电突袭汉军侧翼。从清晨战至正午，汉军全线崩溃，被驱赶入泗水、睢水，溺死者不计其数，"睢水为之不流"。刘邦仅率数十骑在沙尘暴中侥幸逃脱。此后张良指明三大关键人物——英布、彭越、韩信——成为扭转战局的核心战略。</p>'
ch6_overview_en = '<p>In April 205 BC, Liu Bang exploited Xiang Yu\'s entanglement in Qi to capture the Chu capital Pengcheng with a 560,000-strong coalition army. Yet just one month later, Xiang Yu personally led 30,000 elite cavalry in a lightning return from Qi, breaking through Fan Kuai\'s northern defenses, racing down the Sishui line to Xiao County, and launching a dawn flank attack. By noon the Han army had completely collapsed, driven into the Si and Sui rivers with countless drowned — "the Sui River ceased to flow." Liu Bang escaped with only dozens of horsemen in a sandstorm. Zhang Liang then identified three pivotal figures — Ying Bu, Peng Yue, Han Xin — as the strategic key to reversing the war.</p>'

ch6_kpis_zh = [('联军号称', '56万'), ('项羽精骑', '3万'), ('汉军被歼', '10余万'), ('关键人物', '3人')]
ch6_kpis_en = [('Coalition Claimed', '560,000'), ('Xiang Yu\'s Cavalry', '30,000'), ('Han Losses', '100,000+'), ('Key Figures', '3 Named')]

ch6_sections = [
    dict(tag='战略灾难', title='项羽的齐国之困：战略目标达成后不知打住',
         desc='公元前206年四月项羽分封完诸侯，五月田荣就反了。项羽北伐灭齐，击溃田荣、斩杀田假，战略目标全部达成。但他没有收手——恼怒于齐人，尽烧房屋、劫掠妇女，一路屠到北海。"西楚霸王"变成了杀人恶魔。田横趁机收揽败军，齐国人民群起反抗，项羽陷入了与齐国人民作战的汪洋大海。拿破仑说过："胜利的时刻往往潜伏着最大的危险。"项羽缺乏自制力和大局观——他不知道何时该停止，这成为他最终失败的深层原因。',
         extra='''        <div class="dual-grid">
          <div class="dual-card yes">
            <div class="dual-icon">✅</div>
            <div class="dual-text">
              <h4>正确的做法</h4>
              <p>战略目标达成后及时收手。扶植傀儡政权、收取贡赋、撤军休整。省下来的时间、资源和机会可以用于更重要的方向。</p>
            </div>
          </div>
          <div class="dual-card no">
            <div class="dual-icon">❌</div>
            <div class="dual-text">
              <h4>项羽的做法</h4>
              <p>被情绪驱动，将战争变为无限报复。烧杀抢掠导致全民反抗，深陷泥潭无法脱身。百战百胜的最后，往往是数胜而亡。</p>
            </div>
          </div>
        </div>'''),
    dict(tag='闪电突袭', title='三万对五十六万：史上最惊人的以少胜多闪电战',
         desc='项羽面对号称五十六万的诸侯联军，做出了令人瞠目的决定：留下主力继续攻齐，自率三万精骑救楚。他的思路极其清晰——多国联军最大的弱点是指挥系统不协调。项羽先击破樊哙北面防线，不理纠缠马不停蹄走泗水线直扑萧县，拂晓由西向东闪击汉军侧翼。从清晨战至正午，汉军全线崩溃。项羽咬定刘邦中军穷追猛打，将汉军驱赶入泗水、睢水，"睢水为之不流"。此一战汉军被歼十余万，刘邦仅率数十骑在沙尘暴中逃脱。项羽又一次创下战争史上以少胜多的奇迹。',
         extra='''        <div class="flow-row">
            <div class="flow-step ">破樊哙北面防线</div>
            <div class="flow-arrow">→</div>
            <div class="flow-step ">走泗水线南下</div>
            <div class="flow-arrow">→</div>
            <div class="flow-step ">拂晓突袭萧县</div>
            <div class="flow-arrow">→</div>
            <div class="flow-step ">击溃汉军侧翼</div>
            <div class="flow-arrow">→</div>
            <div class="flow-step end">屠杀泗水睢水</div>
          </div>'''),
    dict(tag='战略眼光', title='张良的下邑画策：三根柱子撑住将倾的大厦',
         desc='刘邦逃到下邑后对张良说："关东的土地我不要了！都分了！"张良回答："分了就对了！指你一个人搞不定项羽。重要的只有三个人：英布（项羽头号战将，近期表现可疑，所处九江在西楚上游占据地利）、彭越（没有背景却越混越壮，一直跟项羽捣乱还没被打死）、韩信（不用争取，调回来就行）。只有这三个人全部站到你这边并发挥出全部力量，才有可能战胜项羽。"刘邦对张良言听计从，派随何争取英布，调韩信驰援荥阳，让彭越继续袭扰。这套三路牵制战略为整个楚汉战争定下了总框架。',
         extra='''        <div class="data-row">
            <div class="data-card d1">
              <div class="data-big">①</div>
              <div class="data-name">英布</div>
              <div class="data-sm">项羽头号战将，九江扼守西楚上游，争取他对刘邦至关重要</div>
            </div>
            <div class="data-card d2">
              <div class="data-big">②</div>
              <div class="data-name">彭越</div>
              <div class="data-sm">无背景无投资，靠游击越混越壮，处中原腹地一直骚扰项羽</div>
            </div>
            <div class="data-card d3">
              <div class="data-big">③</div>
              <div class="data-name">韩信</div>
              <div class="data-sm">唯一能独当一面率方面军执行战略任务的人，赶紧从围城调回来</div>
            </div>
          </div>'''),
    dict(tag='当机立断', title='随何说英布：就差几天改变历史的先手棋',
         desc='刘邦派随何前往九江争取英布。随何到后，英布三天不见。随何直接挑明——"项羽伐齐你只派几千人，刘邦攻彭城你按兵不动，你这么\'忠心\'让项羽怎么想？"一针见血击中英布最害怕的地方。英布虽同意归汉但仍想观望，再三叮嘱随何万不可走漏风声。恰好项羽的使者也来催促英布出兵，随何当机立断闯入王廷当众宣告"九江王已归汉"，逼英布上贼船。就差几天的工夫——如果楚使先到，英布就可能倒向项羽。刘邦的"当机立断"为自己争取了宝贵的半年战略窗口期。',
         extra='''        <div class="flow-row">
            <div class="flow-step ">刘邦派随何出使</div>
            <div class="flow-arrow">→</div>
            <div class="flow-step ">英布观望三天</div>
            <div class="flow-arrow">→</div>
            <div class="flow-step ">随何挑明利害</div>
            <div class="flow-arrow">→</div>
            <div class="flow-step ">项羽使者到来</div>
            <div class="flow-arrow">→</div>
            <div class="flow-step end">随何逼英布杀使归汉</div>
          </div>'''),
    dict(tag='成本意识', title='战争的成本与代价：为什么必须"化敌为友"',
         desc='项羽打完田荣后如果收手，齐国会进贡、战士可回家、百姓能生产、资源可建粮仓桥梁。但他选择了无限报复，结果深陷泥潭——刘邦趁机攻占彭城。但刘邦也犯了同样的错误：进彭城后日日置酒高会、尽享项羽财宝美人，没有挥师北上找项羽决战。一夜之间，五十六万大军灰飞烟灭。战争的核心原则：凡是能直接用钱解决的，代价最低；凡是能用嘴解决的，不要用拳头。每个领导人都应该满足于战略目标达成后的胜利——因为你的每次行动，都是有成本的。人生很长，没有战略方针和自制力的人，到达不了巅峰。',
         extra='''        <div class="risk-bars">
          <div class="risk-row">
            <div class="risk-label">化敌为友的成本</div>
            <div class="risk-meter"><div class="risk-fill" style="width:5%"></div></div>
            <div class="risk-val">5%</div>
          </div>
          <div class="risk-row">
            <div class="risk-label">战争直接成本</div>
            <div class="risk-meter"><div class="risk-fill" style="width:60%"></div></div>
            <div class="risk-val">60%</div>
          </div>
          <div class="risk-row">
            <div class="risk-label">战争机会成本</div>
            <div class="risk-meter"><div class="risk-fill" style="width:90%"></div></div>
            <div class="risk-val">90%</div>
          </div>
          <div class="risk-row">
            <div class="risk-label">无限战争反噬</div>
            <div class="risk-meter"><div class="risk-fill" style="width:100%"></div></div>
            <div class="risk-val">100%</div>
          </div>
        </div>'''),
]

ch6_takeaway_zh = '彭城之战展示了两个极端：项羽三万骑兵击溃五十六万联军——军事天才的极致；但项羽的战略灾难——不知何时打住的无限报复——却让他从"霸王"变成"恶魔"，从此陷入四面楚歌。刘邦的大败则催生了张良的"下邑画策"，锁定英布、彭越、韩信三根战略支柱。从此楚汉战争变成了一场消耗战——不是比谁的拳头更硬，而是比谁的体系更能撑。项羽每一次胜利都在消耗自己，刘邦每一次失败都在学习成长。这才是最终结局的决定性差异。'
ch6_takeaway_en = 'The Battle of Pengcheng revealed two extremes: Xiang Yu\'s 30,000 cavalry routing a 560,000-strong coalition — military genius at its peak; but his strategic disaster — endless vengeful warfare without knowing when to stop — transformed him from "Hegemon-King" to "demon," plunging him into encirclement. Liu Bang\'s catastrophic defeat catalyzed Zhang Liang\'s "Xia Yi Plan," locking in Ying Bu, Peng Yue, and Han Xin as three strategic pillars. Henceforth the Chu-Han war became a war of attrition — not about who punched harder, but whose system could endure longer. Every Xiang Yu victory consumed his own strength; every Liu Bang defeat was a learning experience. This was the decisive difference in the final outcome.'

ch6_footer_zh = '渤海小吏 · 楚汉双雄 · 第六章 · 图书信息图<br>\n来源：楚汉双雄（渤海小吏 著，台海出版社，2020）'
ch6_footer_en = 'Bohai Xiaoli · The Chu-Han Contention · Chapter 6 · Book Infographic<br>\nSource: The Chu-Han Contention (by Bohai Xiaoli, Taihai Press, 2020)'

# ── Chapter 7: 背水一战 ──

ch7_title_zh = '背水一战："兵仙"的一路向北'
ch7_title_en = 'The Battle of Jingxing: The "God of War\'s" Northern Campaign'

ch7_sub_zh = '韩信如何在十个月内用五万人横扫北方四国——"背水一战"的七个关键环节比你想象的复杂一万倍'
ch7_sub_en = 'How Han Xin swept four northern kingdoms with 50,000 men in ten months — the seven critical links of the "Back-to-the-River Battle" are far more complex than you imagined'

ch7_overview_zh = '<p>彭城大败后，刘邦派韩信率两万偏师北上灭魏。韩信在一个月内用木罂渡黄河、声东击西擒魏豹，随后三万人灭代，五万人破赵。最著名的"背水一战"——井陉口韩信背水列阵诱出赵军全部主力，两千骑兵奇袭空营换红旗，两面夹击大破陈馀二十万大军。战后用李左车"不战而屈人之兵"之计招降燕国。十个月内，韩信仅用五万非嫡系部队完成了对整个中国北方的征服。但"背水一战"的真正秘密不是"退无可退、拼命一战"——那是七个精密环节环环相扣的结果。</p>'
ch7_overview_en = '<p>After the Pengcheng disaster, Liu Bang sent Han Xin north with only 20,000 men to destroy Wei. Within one month Han Xin used wooden floats to cross the Yellow River, feigned east and struck west to capture Wei Bao. Then 30,000 men destroyed Dai, and 50,000 crushed Zhao. The most famous "Back-to-the-River Battle" — at Jingxing Pass, Han Xin arrayed his army with the river behind, baited out Zhao\'s entire force, sent 2,000 cavalry to seize the empty camp and raise red banners, then attacked from both sides, routing Chen Yu\'s 200,000-strong army. Afterward he employed Li Zuoche\'s strategy of "subduing the enemy without fighting" to force Yan\'s surrender. In ten months, Han Xin conquered all of northern China with just 50,000 non-elite troops. But the true secret of the "Back-to-the-River" victory was not "no retreat, fight to the death" — it was the result of seven precisely interlocking steps.</p>'

ch7_kpis_zh = [('完成北伐', '10个月'), ('使用兵力', '5万人'), ('灭国数量', '4个'), ('背水关键', '7环节')]
ch7_kpis_en = [('Campaign Duration', '10 Months'), ('Troops Used', '50,000'), ('Kingdoms Destroyed', '4'), ('Victory Links', '7 Steps')]

ch7_sections = [
    dict(tag='情报先行', title='灭魏：每次作战前用间谍摸清所有底牌',
         desc='韩信每次战前必派大量间谍刺探敌情，汇总所有消息后才下达作战部署。灭魏时，他得知魏豹将主力全部集结在蒲津渡封锁黄河，龙门渡却无人设防——这是一个致命漏洞。韩信用灌婴骑兵和舟船在蒲津渡大张旗鼓佯攻，吸引魏军全部注意力；同时派曹参率主力在上游夏阳用木罂偷渡黄河，直插安邑切断魏军退路。两面夹击下魏军大败，魏豹被俘。山西高原一战而定。韩信为何成功？因为他不相信任何侥幸——"兵者，国之大事，生死之地，不可不察也。"',
         extra='''        <div class="dual-grid">
          <div class="dual-card yes">
            <div class="dual-icon">✅</div>
            <div class="dual-text">
              <h4>韩信做法（情报驱动）</h4>
              <p>先派间谍摸清敌情。发现魏豹赌在蒲津渡，龙门渡空虚。用自己的"虚"（旌旗舟船）牵制对方"实"，用自己的"实"（主力偷渡）打击对方"虚"。</p>
            </div>
          </div>
          <div class="dual-card no">
            <div class="dual-icon">❌</div>
            <div class="dual-text">
              <h4>魏豹做法（盲目下注）</h4>
              <p>兵力有限就孤注一掷堵蒲津渡，认为韩信没船就过不了河。但韩信根本不用船——用木罂搭浮桥偷渡。不撒胡椒面的结果是被一锅端。</p>
            </div>
          </div>
        </div>'''),
    dict(tag='恩怨驱动', title='陈馀放韩信进井陉：私仇如何毁掉一个国家',
         desc='陈馀部下李左车提出完美方案：给我三万骑兵断汉军粮道，您深沟高垒不战，不出十天韩信张耳人头送到。方案有分析有论据无风险。但陈馀拒绝了，理由冠冕堂皇——"我们是仁义之师，不以诡计取胜"。真实原因只有一个：张耳。陈馀无法忍受当着张耳的面不是碾压而是偷袭——他要让张耳亲眼看到，"没有我，你什么也不是"。这种将个人恩怨凌驾于国家利益的决策，为背水一战这场千古名局搭好了舞台。也是"对人不对事"的经典反面教材。',
         extra='''        <div class="flow-row">
            <div class="flow-step ">张耳陈馀生死之交</div>
            <div class="flow-arrow">→</div>
            <div class="flow-step ">巨鹿之战产生裂痕</div>
            <div class="flow-arrow">→</div>
            <div class="flow-step ">陈馀弃印张耳取之</div>
            <div class="flow-arrow">→</div>
            <div class="flow-step ">由爱生恨势同水火</div>
            <div class="flow-arrow">→</div>
            <div class="flow-step end">陈馀为私仇弃良策</div>
          </div>'''),
    dict(tag='七环紧扣', title='背水一战：七个环节缺一不可的精密工程',
         desc='流传两千年的"背水一战"故事极其简化——退无可退，奋勇上前。但这是完全的误导。实际情况是七个环节环环相扣：①提前用间谍探明井陉道无伏兵；②半夜派两千骑兵秘密出发至埋伏点；③先派一万兵背水列阵骄兵兼做缓冲；④自己殿后确保全军过河；⑤亲自做诱饵主力且战且退丢旗弃鼓；⑥背水阵成建制一万兵截住追兵让韩信喊出"退无可退"；⑦两千骑兵夺空营换红旗两面夹击。七个环节少了任何一个，韩信都赢不了。古往今来只成功过一次，是因为只有韩信做全了这七个步骤。',
         extra='''        <div class="risk-bars">
          <div class="risk-row">
            <div class="risk-label">①间谍探路</div>
            <div class="risk-meter"><div class="risk-fill" style="width:100%"></div></div>
            <div class="risk-val">致命</div>
          </div>
          <div class="risk-row">
            <div class="risk-label">②半夜伏兵</div>
            <div class="risk-meter"><div class="risk-fill" style="width:100%"></div></div>
            <div class="risk-val">致命</div>
          </div>
          <div class="risk-row">
            <div class="risk-label">③背水缓冲阵</div>
            <div class="risk-meter"><div class="risk-fill" style="width:100%"></div></div>
            <div class="risk-val">致命</div>
          </div>
          <div class="risk-row">
            <div class="risk-label">④⑦夺营红旗</div>
            <div class="risk-meter"><div class="risk-fill" style="width:100%"></div></div>
            <div class="risk-val">致胜</div>
          </div>
        </div>'''),
    dict(tag='被忽略的真相', title='韩信成功的深层原因：时代红利与国运窗口',
         desc='韩信北伐之所以十个月横扫北方，不仅因为军事天才，更因为三个时代红利：①对手虚弱——魏代赵燕都是"空降干部"，户口钱粮民心啥也没有；②项羽的顶层设计造成这种虚弱——他把各国故地重新洗牌，新封的国王全无根基；③刘邦在关中的民心优势和萧何的动员能力持续输血。还有一个被忽视的因素：韩信出汉中时有水路运粮（西汉水和嘉陵江），而四百年后诸葛亮北伐时武都大地震改变了河道，大泽消失，运粮成为噩梦。国运在时万事俱备，国运不在，再遇"国士无双"也无法逆天改命。',
         extra='''        <div class="data-row">
            <div class="data-card d1">
              <div class="data-big">🕐</div>
              <div class="data-name">对手虚弱</div>
              <div class="data-sm">四国皆为刚"空降"的政权，无户口钱粮无民心基础</div>
            </div>
            <div class="data-card d2">
              <div class="data-big">🌊</div>
              <div class="data-name">水运便利</div>
              <div class="data-sm">西汉水嘉陵江贯通汉中至关中，船运解决粮草问题</div>
            </div>
            <div class="data-card d3">
              <div class="data-big">⚙️</div>
              <div class="data-name">后方造血</div>
              <div class="data-sm">萧何用秦宫档案持续动员关中巴蜀人力物力</div>
            </div>
          </div>'''),
    dict(tag='以智代力', title='不战而屈人之兵：燕国一招降服的智慧',
         desc='破赵后韩信悬赏千金活捉李左车，以师长之礼虚心求教。李左车分析：将军连灭三国，威震天下是优势；但士卒疲惫、深入敌境是劣势。此时远征燕国坚城之下，势必久战不下，齐国就会固守边境——燕齐不下则天下胜负未分。建议：按兵不动休整士卒，摆出攻燕架势，然后派辩士游说——燕国必降。燕降后齐必跟风。韩信完全采纳，以"不战而屈人之兵"降燕。他懂得"凡动作必有成本"，能用嘴解决的就绝不动拳头。这恰恰是项羽一辈子没学会的——也是"化敌为友"比消灭敌人更高明的地方。',
         extra='''        <div class="flow-row">
            <div class="flow-step ">破赵立威</div>
            <div class="flow-arrow">→</div>
            <div class="flow-step ">悬赏千金求李左车</div>
            <div class="flow-arrow">→</div>
            <div class="flow-step ">休整摆出攻燕架势</div>
            <div class="flow-arrow">→</div>
            <div class="flow-step ">辩士游说燕国</div>
            <div class="flow-arrow">→</div>
            <div class="flow-step end">燕不战而降</div>
          </div>'''),
]

ch7_takeaway_zh = '"背水一战"不是"退无可退奋勇上前"的励志鸡汤，而是七个精密环节环环相扣的系统工程。两千年来无数人想复制韩信的奇迹，从马谡到各种"自断后路"的豪赌者，几乎全部失败——因为他们只看到了"背水列阵"的表象，却不知道韩信做了多少前期的间谍侦察、半夜部署、伏兵安排、骄兵诱敌。真正值得学习的是韩信每次战前的"庙算"——把所有信息汇总后才下决策，把每一个环节都做足准备。即便如此，以弱搏强仍不建议作为首选——因为环节越多，出纰漏的可能性就越大。气沉丹田，踏踏实实过好每一天，今天比昨天好，明天比今天好，足以。'
ch7_takeaway_en = '"Back-to-the-River Battle" is not an inspirational cliché of "no retreat, fight to the death" — it was a systems engineering feat of seven precisely interlocking steps. For two millennia countless imitators tried to replicate Han Xin\'s miracle, from Ma Su to various "burn your bridges" gamblers — nearly all failed. Because they only saw the surface image of "arrayed with the river behind" without knowing Han Xin\'s extensive pre-battle espionage, midnight deployments, ambush arrangements, and bait tactics. What\'s truly worth learning is Han Xin\'s pre-battle "temple calculation" — aggregating all intelligence before deciding, preparing every link thoroughly. Even so, fighting the strong with the weak is never recommended as a first choice — because the more steps, the higher the chance of failure. Ground yourself, live each day steadily, better today than yesterday, better tomorrow than today — that is enough.'

ch7_footer_zh = '渤海小吏 · 楚汉双雄 · 第七章 · 图书信息图<br>\n来源：楚汉双雄（渤海小吏 著，台海出版社，2020）'
ch7_footer_en = 'Bohai Xiaoli · The Chu-Han Contention · Chapter 7 · Book Infographic<br>\nSource: The Chu-Han Contention (by Bohai Xiaoli, Taihai Press, 2020)'

# ── Chapter 8: 拉锯荥阳 ──

ch8_title_zh = '拉锯荥阳：东奔西走的"霸王"'
ch8_title_en = 'The Xingyang Stalemate: The Exhausted "Hegemon-King"'

ch8_sub_zh = '情报战线的"成本革命"、两千名妇女的性掩护、打不完的"地鼠"——楚汉相持阶段的全维度消耗战'
ch8_sub_en = 'The "cost revolution" of intelligence warfare, 2,000 women as sexual cover, endless "whack-a-mole" — the all-dimensional war of attrition in the Chu-Han stalemate'

ch8_overview_zh = '<p>公元前204年起，楚汉在荥阳一线进入长达两年多的相持阶段。陈平以四万两黄金展开间谍战，离间项羽与范增、钟离昧等异姓将领；范增被驱逐后发背疮而死。荥阳危急时陈平用两千名妇女作性掩护，以纪信假扮刘邦诈降，助刘邦逃脱。此后项羽陷入"打地鼠"困境——刘邦正面牵制、彭越后方袭扰、英布南面牵制，项羽每扑灭一处火另一处又起。最终韩信潍水之战斩龙且定齐，刘邦荥阳战线起死回生。项羽第一次低下高贵的头颅，派人劝韩信三分天下——楚汉争霸走向终章。</p>'
ch8_overview_en = '<p>From 204 BC, the Chu and Han armies entered a two-year stalemate along the Xingyang line. Chen Ping launched a spy war with 40,000 taels of gold, sowing discord between Xiang Yu and his non-clan generals like Fan Zeng and Zhongli Mei; Fan Zeng was driven out and died of an ulcerated back. When Xingyang became critical, Chen Ping used 2,000 women as sexual cover, with Ji Xin impersonating Liu Bang in a fake surrender to enable Liu Bang\'s escape. Thereafter Xiang Yu fell into a "whack-a-mole" trap — Liu Bang pinned him frontally, Peng Yue raided his rear, Ying Bu harassed from the south. Every fire Xiang Yu extinguished, another ignited elsewhere. Finally Han Xin beheaded Long Ju at the Battle of the Wei River and pacified Qi, reviving Liu Bang\'s Xingyang front. For the first time, Xiang Yu lowered his proud head and sent envoys to persuade Han Xin to divide the empire into three — the Chu-Han contest moved toward its finale.</p>'

ch8_kpis_zh = [('陈平用金', '4万两'), ('对妇女', '2000名'), ('拉锯时间', '2年+'), ('范增之死', '被离间')]
ch8_kpis_en = [('Chen Ping\'s Gold', '40,000 Taels'), ('Women Used', '2,000'), ('Stalemate', '2+ Years'), ('Fan Zeng\'s Fate', 'Alienated')]

ch8_sections = [
    dict(tag='人性洞察', title='先抑后扬：刘邦用"洗脚接见"拿下英布',
         desc='英布为刘邦牵制项羽半年多后拼光了老本，投奔刘邦。刘邦倚着床、洗着脚接见他——英布虎目含泪当场就想自杀。但当他被引领到居处时，发现一切规格与汉王府一模一样。这种巨大的落差瞬间拿下英布："刘邦那叫随性、不做作！越看越可爱，还当我面洗脚，多皮啊！不是自己人能这样吗？"这是典型的"先辱后赏、先抑后扬"——刘邦对人性的精准把控对比项羽强了好几个档次，正如项羽在军事上对比他的巨大优势一样。英布争取来的半年时间，让韩信完成了整个北方征服。',
         extra='''        <div class="dual-grid">
          <div class="dual-card yes">
            <div class="dual-icon">✅</div>
            <div class="dual-text">
              <h4>刘邦 · 先抑后扬</h4>
              <p>洗脚接见制造巨大落差，然后以最高规格款待。利用人们憎恨失去的心理弱点——冷一点之后再热烈，才会让人感到春天般的温暖。</p>
            </div>
          </div>
          <div class="dual-card no">
            <div class="dual-icon">❌</div>
            <div class="dual-text">
              <h4>项羽 · 有恃无恐</h4>
              <p>一直对英布喜爱有加、裂土封王。但越偏爱越有恃无恐。项羽用人时英布派几千人打发——被偏爱的永远有恃无恐。</p>
            </div>
          </div>
        </div>'''),
    dict(tag='情报革命', title='陈平登场：四万两黄金的间谍战与成本哲学',
         desc='陈平来自项羽阵营，深知楚国内部项氏家族与异姓将领的矛盾。他向刘邦提出："给我四万两黄金，让我反间项羽君臣。"刘邦二话没说就拨了钱，连具体计划都不问。陈平用这些黄金在楚军中收买内线、散布谣言，目标精准锁定范增——项羽最不可替代的智囊。最终范增被猜忌驱逐，发背疮而死。刘邦的高明在于算清了一笔账：四万两黄金不过十万大军一个月的耗费，仗打了一年多，还在乎这点钱？"凡动作必有成本"——能用钱直接解决的，代价最低。间谍投入产出比永远最高。',
         extra='''        <div class="risk-bars">
          <div class="risk-row">
            <div class="risk-label">间谍成本(月)</div>
            <div class="risk-meter"><div class="risk-fill" style="width:5%"></div></div>
            <div class="risk-val">5%</div>
          </div>
          <div class="risk-row">
            <div class="risk-label">大军开支(月)</div>
            <div class="risk-meter"><div class="risk-fill" style="width:100%"></div></div>
            <div class="risk-val">100%</div>
          </div>
          <div class="risk-row">
            <div class="risk-label">范增价值</div>
            <div class="risk-meter"><div class="risk-fill" style="width:500%"></div></div>
            <div class="risk-val">&infin;</div>
          </div>
          <div class="risk-row">
            <div class="risk-label">投入产出比</div>
            <div class="risk-meter"><div class="risk-fill" style="width:10%"></div></div>
            <div class="risk-val">1:10</div>
          </div>
        </div>'''),
    dict(tag='暗黑手段', title='两千名妇女与纪信替死：被史书轻描淡写的代价',
         desc='范增死后荥阳仍然危在旦夕。陈平的脱身之计：让身形相貌酷似刘邦的纪信假扮汉王向项羽诈降，然后让两千名妇女化装成汉军出城。"两千名妇女假扮士兵"——这不是木兰从军，而是极其下作的"性掩护"。这两千名妇女让围城的饥渴楚军松懈下来，刘邦趁夜色从西门逃脱。忠勇的纪信被项羽活活烧死，两千名妇女的下场史书一字未提。陈平的手段极其冷酷高效——但代价是一批被史书抹去名字的人。情报工作永远走不到台前，这是其本质决定的。',
         extra='''        <div class="flow-row">
            <div class="flow-step ">纪信假扮刘邦</div>
            <div class="flow-arrow">&rarr;</div>
            <div class="flow-step ">2000妇女伪装出城</div>
            <div class="flow-arrow">&rarr;</div>
            <div class="flow-step ">楚军松懈围观</div>
            <div class="flow-arrow">&rarr;</div>
            <div class="flow-step ">刘邦西门逃脱</div>
            <div class="flow-arrow">&rarr;</div>
            <div class="flow-step end">纪信被项羽烧死</div>
          </div>'''),
    dict(tag='战略困境', title='"打地鼠"的项羽：为什么百战百胜却越来越被动',
         desc='项羽的军事才能无可匹敌——刘邦在正面战场从没赢过他。但问题在于他对人不对事：谁闹得欢就去灭谁，却没有制定过固定的战略分工。他手下有钟离昧、龙且等百战名将，却因陈平的离间而始终不放心放权。结果刘邦正面牵制、彭越后方袭扰、英布南面牵制——项羽在三个战场间疲于奔命。刘邦则越来越清楚自己的定位：他就是一根牵制的大旗，靠耗下去从别的方向慢慢耗死项羽。刘邦"对事不对人"，错了就改、对了就做；项羽"对人不对事"，被情绪和猜忌驱动——这正是两人最根本的差距。',
         extra='''        <div class="data-row">
            <div class="data-card d1">
              <div class="data-big">&#x1F3AF;</div>
              <div class="data-name">刘邦牵制</div>
              <div class="data-sm">荥阳正面顶住项羽主力，靠萧何后方持续输血</div>
            </div>
            <div class="data-card d2">
              <div class="data-big">&#x1F400;</div>
              <div class="data-name">彭越袭扰</div>
              <div class="data-sm">在楚国后方断粮道、攻城邑，项羽一走就大肆活动</div>
            </div>
            <div class="data-card d3">
              <div class="data-big">&#x2694;&#xFE0F;</div>
              <div class="data-name">韩信北伐</div>
              <div class="data-sm">开辟北方战场，最终从东面包抄楚国</div>
            </div>
          </div>'''),
    dict(tag='终章前奏', title='潍水之战斩龙且：楚汉天平彻底倾斜',
         desc='项羽派龙且率五万楚军救齐。龙且不屑韩信——"一个吃软饭、爬裤裆的货。"但韩信再次上演水战魔法：在潍水上游用上万沙袋筑坝蓄水，亲自引军过河诱敌，龙且率全军追击过河时，韩信下令破坝放水——突然暴涨的河水将楚军分割成两段。过河的楚军瞬间成为"背水孤军"，军心大乱，龙且被杀。潍水之战后韩信闪电平定齐国七十余城。项羽第一次感到空前的危险——西有刘邦、北有张耳、东有韩信、后方有彭越，四面楚歌。他放下了高傲，派人劝韩信三分天下。楚汉争霸走向终章。',
         extra='''        <div class="flow-row">
            <div class="flow-step ">上游沙袋筑坝</div>
            <div class="flow-arrow">&rarr;</div>
            <div class="flow-step ">韩信过河诱敌</div>
            <div class="flow-arrow">&rarr;</div>
            <div class="flow-step ">龙且全军追击</div>
            <div class="flow-arrow">&rarr;</div>
            <div class="flow-step ">破坝放水断后路</div>
            <div class="flow-arrow">&rarr;</div>
            <div class="flow-step end">龙且阵亡齐地平定</div>
          </div>'''),
]

ch8_takeaway_zh = '荥阳拉锯战揭示了楚汉争霸最深刻的胜负密码：项羽百战百胜却越来越被动，刘邦屡战屡败却越来越强大。根本原因在于两人对"系统"的理解——刘邦建立了萧何后勤、张良战略、韩信军事、陈平情报的四大系统，而项羽只靠自己的军事天才单打独斗。陈平的四万两黄金间谍战展示了"凡动作必有成本"的冷酷真理：能用钱解决的代价最低。项羽舍不得封赏、不放权、不信任，最终被系统性消耗拖垮。荥阳的两年不是军事对决，是两种组织模式的对决。'
ch8_takeaway_en = 'The Xingyang stalemate reveals the deepest code of victory in the Chu-Han contest: Xiang Yu won every battle yet grew increasingly passive; Liu Bang lost repeatedly yet grew ever stronger. The root cause lay in their understanding of "systems" — Liu Bang built four systems (Xiao He\'s logistics, Zhang Liang\'s strategy, Han Xin\'s military, Chen Ping\'s intelligence), while Xiang Yu relied solely on his own military genius. Chen Ping\'s 40,000-tael gold spy operation demonstrated the cold truth that "every action has a cost" — what can be solved with money costs the least. Xiang Yu begrudged rewards, wouldn\'t delegate, wouldn\'t trust, and was ultimately worn down by systemic attrition. The two years at Xingyang were not a military duel but a duel between two organizational models.'

ch8_footer_zh = '渤海小吏 · 楚汉双雄 · 第八章 · 图书信息图<br>\n来源：楚汉双雄（渤海小吏 著，台海出版社，2020）'
ch8_footer_en = 'Bohai Xiaoli · The Chu-Han Contention · Chapter 8 · Book Infographic<br>\nSource: The Chu-Han Contention (by Bohai Xiaoli, Taihai Press, 2020)'


# ============================================================
# GENERATE ALL FILES
# ============================================================
chapters = [
    (5, ch5_title_zh, ch5_title_en, ch5_sub_zh, ch5_sub_en, ch5_overview_zh, ch5_overview_en, ch5_kpis_zh, ch5_kpis_en, ch5_sections, ch5_takeaway_zh, ch5_takeaway_en, ch5_footer_zh, ch5_footer_en),
    (6, ch6_title_zh, ch6_title_en, ch6_sub_zh, ch6_sub_en, ch6_overview_zh, ch6_overview_en, ch6_kpis_zh, ch6_kpis_en, ch6_sections, ch6_takeaway_zh, ch6_takeaway_en, ch6_footer_zh, ch6_footer_en),
    (7, ch7_title_zh, ch7_title_en, ch7_sub_zh, ch7_sub_en, ch7_overview_zh, ch7_overview_en, ch7_kpis_zh, ch7_kpis_en, ch7_sections, ch7_takeaway_zh, ch7_takeaway_en, ch7_footer_zh, ch7_footer_en),
    (8, ch8_title_zh, ch8_title_en, ch8_sub_zh, ch8_sub_en, ch8_overview_zh, ch8_overview_en, ch8_kpis_zh, ch8_kpis_en, ch8_sections, ch8_takeaway_zh, ch8_takeaway_en, ch8_footer_zh, ch8_footer_en),
]

for ch in chapters:
    (n, tzh, ten, szh, sen, ozh, oen, kzh, ken, sec, ttz, tte, fzh, fen) = ch

    zh_path = os.path.join(base, f'楚汉双雄-ch{n:03d}-info-zh.html')
    with open(zh_path, 'w') as f:
        f.write(gen_html('zh', n, ten, tzh, szh, ozh, kzh, sec, ttz, fzh))

    en_path = os.path.join(base, f'楚汉双雄-ch{n:03d}-info-en.html')
    with open(en_path, 'w') as f:
        f.write(gen_html('en', n, ten, tzh, sen, oen, ken, sec, tte, fen))

    print(f"✅ 楚汉双雄-ch{n:03d}-info-zh.html + en.html")

print("\n🎉 All 8 files generated successfully!")