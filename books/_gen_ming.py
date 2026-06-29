#!/usr/bin/env python3
"""
Batch generate infographic HTML for 明朝那些事儿 chapters.
Reads _ming_data.json and generates zh+en HTML files.
"""
import os, json, re

BOOKS_DIR = os.path.dirname(os.path.abspath(__file__))
DATA_PATH = os.path.join(BOOKS_DIR, '_ming_data.json')

CSS = '''<style>
@font-face{font-family:'FZXPYZS';src:url('../方正屏显雅宋简体.TTF') format('truetype');font-weight:normal;font-style:normal;}
*{margin:0;padding:0;box-sizing:border-box;}
body{background:#f5f1eb;font-family:'FZXPYZS','PingFang SC','Noto Serif SC','STSong',Georgia,serif;display:flex;justify-content:center;align-items:flex-start;min-height:100vh;padding:40px 20px 60px;}
.container{max-width:880px;width:100%;}
.back-catalog{text-align:right;margin-bottom:4px;}
.back-catalog a{font-size:12px;color:#888;text-decoration:none;font-family:'FZXPYZS','PingFang SC',serif;}
.lang-switch{text-align:right;margin-bottom:12px;}
.lang-switch a.lang-btn{font-size:13px;color:#4f46e5;text-decoration:none;font-family:'FZXPYZS','PingFang SC',serif;}
h1{font-family:'FZXPYZS',serif;font-size:32px;font-weight:bold;color:#1a1a1a;margin-bottom:8px;line-height:1.3;}
.subtitle{font-size:14px;color:#888;margin-bottom:20px;line-height:1.6;}
.divider{height:3px;background:linear-gradient(90deg,#dc2626,#ea580c);margin:20px 0 28px;border-radius:2px;}
.chapter-overview{background:#fff;border-left:4px solid #4f46e5;border-radius:8px;padding:16px 20px;margin-bottom:24px;box-shadow:0 1px 3px rgba(0,0,0,0.04);}
.chapter-overview p{font-size:14px;color:#333;line-height:1.7;}
.kpi-row{display:grid;grid-template-columns:repeat(4,1fr);gap:12px;margin-bottom:24px;}
.kpi{background:#fff;border-radius:12px;padding:14px 10px;text-align:center;box-shadow:0 1px 3px rgba(0,0,0,0.04);}
.kpi-num{font-family:'FZXPYZS',serif;font-size:26px;font-weight:bold;}
.kpi-label{font-size:12px;color:#888;margin-top:2px;}
.kpi .c01{color:#dc2626;}.kpi .c02{color:#ea580c;}.kpi .c03{color:#ca8a04;}.kpi .c04{color:#4f46e5;}
.section-01,.section-02,.section-03,.section-04,.section-05{background:#fff;border-radius:12px;padding:20px 24px;margin-bottom:16px;box-shadow:0 1px 3px rgba(0,0,0,0.04);position:relative;overflow:hidden;}
.section-01{border-left:4px solid #dc2626;}.section-02{border-left:4px solid #ea580c;}.section-03{border-left:4px solid #ca8a04;}.section-04{border-left:4px solid #4f46e5;}.section-05{border-left:4px solid #db2777;}
.section-header{display:flex;align-items:center;gap:10px;margin-bottom:12px;}
.num-01,.num-02,.num-03,.num-04,.num-05{width:28px;height:28px;border-radius:50%;display:flex;align-items:center;justify-content:center;font-size:13px;font-weight:bold;color:#fff;flex-shrink:0;}
.num-01{background:#dc2626;}.num-02{background:#ea580c;}.num-03{background:#ca8a04;}.num-04{background:#4f46e5;}.num-05{background:#db2777;}
.section-title{font-size:17px;font-weight:bold;color:#1a1a1a;}
.section-body{font-size:14px;color:#333;line-height:1.75;}
.section-body .bluf{font-weight:bold;color:#1a1a1a;}
.flow-row{display:flex;align-items:center;gap:8px;margin:12px 0;flex-wrap:wrap;}
.flow-step{background:#fef3c7;border:1px solid #fcd34d;border-radius:8px;padding:8px 14px;font-size:13px;text-align:center;color:#92400e;flex:1;min-width:80px;}
.flow-arrow{color:#ca8a04;font-size:16px;}
.dual-grid{display:grid;grid-template-columns:1fr 1fr;gap:12px;margin:12px 0;}
.dual-card{background:#f8fafc;border-radius:8px;padding:12px 14px;}
.dual-card .label{font-size:11px;color:#888;margin-bottom:4px;}
.dual-card .value{font-size:15px;font-weight:bold;color:#1a1a1a;}
.dual-card.good{border-left:3px solid #16a34a;}
.dual-card.bad{border-left:3px solid #dc2626;}
.data-row{display:grid;grid-template-columns:repeat(3,1fr);gap:10px;margin:12px 0;}
.data-card{background:#fff;border:1px solid #e5e7eb;border-radius:8px;padding:12px;text-align:center;}
.data-card .num{font-family:'FZXPYZS',serif;font-size:22px;font-weight:bold;color:#dc2626;}
.data-card .tag{font-size:11px;color:#888;margin-top:2px;}
.takeaway{background:#fff;border-left:4px solid #dc2626;border-radius:8px;padding:18px 22px;margin-top:8px;box-shadow:0 1px 3px rgba(0,0,0,0.04);}
.takeaway-title{font-size:15px;font-weight:bold;color:#dc2626;margin-bottom:6px;}
.takeaway p{font-size:14px;color:#333;line-height:1.7;}
.footer{margin-top:28px;text-align:center;font-size:12px;color:#999;line-height:1.8;}
@media(max-width:768px){body{padding:20px 12px 40px;}.kpi-row{grid-template-columns:repeat(2,1fr);}.dual-grid,.data-row{grid-template-columns:1fr;}.flow-row{flex-direction:column;}.flow-arrow{transform:rotate(90deg);}}
</style>'''

BACK_ZH = '<div class="back-catalog"><a class="back-catalog-btn" href="../books/目录.html">&larr; 返回图书目录</a></div>'
BACK_EN = '<div class="back-catalog"><a class="back-catalog-btn" href="../books/目录.html">&larr; Back to Book Index</a></div>'
LANG_SWITCH_ZH = '<div class="lang-switch"><a class="lang-btn" href="{fname_en}" target="_blank">中文 / English</a></div>'
LANG_SWITCH_EN = '<div class="lang-switch"><a class="lang-btn" href="{fname_zh}" target="_blank">中文 / English</a></div>'
FOOTER_ZH = '<div class="footer"><p>明朝那些事儿 · 当年明月</p><p>本信息图基于公开资料整理</p></div>'
FOOTER_EN = '<div class="footer"><p>Ming Dynasty Stories · Author: Mingyue Dang</p><p>This infographic is based on publicly available information</p></div>'


def truncate(text, max_len=120):
    if not text:
        return ''
    text = re.sub(r'\s+', ' ', text).strip()
    return text[:max_len] + '...' if len(text) > max_len else text

def extract_key_points(body, n=3):
    lines = [l.strip() for l in body.split('\n') if l.strip() and len(l.strip()) > 8]
    lines = [l for l in lines if not re.match(r'^[一二三四五六七八九十]+$', l)]
    return lines[:n] if lines else ['本章内容精彩，敬请阅读原著。']


def make_kpis(title, body):
    nums = re.findall(r'\d+[万亿]?[年月日人]|\d+\.\d+|\d+%', body)
    kpis = [
        (nums[0] if nums else '1章', '章节内容', '#dc2626'),
        (nums[1] if len(nums) > 1 else '多角色', '人物互动', '#ea580c'),
        (nums[2] if len(nums) > 2 else '关键转折', '历史节点', '#ca8a04'),
        (nums[3] if len(nums) > 3 else '深远影响', '历史意义', '#4f46e5'),
    ]
    return '<div class="kpi-row">\n' + '\n'.join(
        f'<div class="kpi"><div class="kpi-num" style="color:{c};">{n}</div><div class="kpi-label">{l}</div></div>'
        for n, l, c in kpis
    ) + '\n</div>'


def make_sections_zh(title, key_points):
    s1 = f'''<div class="section-01">
<div class="section-header"><div class="num-01">01</div><div class="section-title">历史背景与局势</div></div>
<div class="section-body">
<p class="bluf">本章「{title}」讲述的历史背景与各方势力博弈格局。</p>
<div class="dual-grid">
<div class="dual-card good"><div class="label">关键态势</div><div class="value">{key_points[0][:60] if key_points else title[:60]}</div></div>
<div class="dual-card bad"><div class="label">潜在风险</div><div class="value">权力斗争中各方利益交织，一步错满盘皆落空</div></div>
</div>
<p>{key_points[0][:200] if key_points else ''}</p>
</div>
</div>'''
    
    s2 = f'''<div class="section-02">
<div class="section-header"><div class="num-02">02</div><div class="section-title">核心冲突与博弈</div></div>
<div class="section-body">
<p class="bluf">权力、利益、生存——三重博弈同时进行。</p>
<div class="flow-row">
<div class="flow-step">利益博弈</div><span class="flow-arrow">→</span>
<div class="flow-step">权力争夺</div><span class="flow-arrow">→</span>
<div class="flow-step">生存抉择</div><span class="flow-arrow">→</span>
<div class="flow-step">历史走向</div>
</div>
<div class="data-row">
<div class="data-card"><div class="num">博弈</div><div class="tag">多方利益交织</div></div>
<div class="data-card"><div class="num">抉择</div><div class="tag">历史转折点</div></div>
<div class="data-card"><div class="num">代价</div><div class="tag">成败皆付出一代</div></div>
</div>
<p>{key_points[1][:200] if len(key_points) > 1 else key_points[0][:200] if key_points else ''}</p>
</div>
</div>'''
    
    s3 = f'''<div class="section-03">
<div class="section-header"><div class="num-03">03</div><div class="section-title">关键人物与抉择</div></div>
<div class="section-body">
<p class="bluf">每一个重大历史节点，背后都是人物的性格与选择。</p>
<div class="dual-grid">
<div class="dual-card good"><div class="label">明智之举</div><div class="value">审时度势，顺势而为</div></div>
<div class="dual-card bad"><div class="label">致命失误</div><div class="value">刚愎自用，逆势而行</div></div>
</div>
<p>{key_points[2][:200] if len(key_points) > 2 else key_points[0][:200] if key_points else ''}</p>
</div>
</div>'''
    
    s4 = '''<div class="section-04">
<div class="section-header"><div class="num-04">04</div><div class="section-title">历史影响与连锁反应</div></div>
<div class="section-body">
<p class="bluf">一件小事，可能改变整个帝国的走向。</p>
<div class="flow-row">
<div class="flow-step">直接后果</div><span class="flow-arrow">→</span>
<div class="flow-step">连锁反应</div><span class="flow-arrow">→</span>
<div class="flow-step">长期影响</div><span class="flow-arrow">→</span>
<div class="flow-step">历史定论</div>
</div>
<div class="data-row">
<div class="data-card"><div class="num">短期</div><div class="tag">直接后果</div></div>
<div class="data-card"><div class="num">中期</div><div class="tag">连锁反应</div></div>
<div class="data-card"><div class="num">长期</div><div class="tag">历史定论</div></div>
</div>
<p>历史从不孤立地发生事件，每一个决策都像投入湖中的石子，涟漪扩散至整个帝国。</p>
</div>
</div>'''
    
    s5 = '''<div class="section-05">
<div class="section-header"><div class="num-05">05</div><div class="section-title">历史教训与启示</div></div>
<div class="section-body">
<p class="bluf">读史使人明智，但真正的智慧在于从历史中看见自己。</p>
<div class="comparison-table">
<table>
<tr><th>维度</th><th>正面启示</th><th>反面教训</th></tr>
<tr><td>决策</td><td style="color:#16a34a;">集思广益，兼听则明</td><td style="color:#dc2626;">独断专行，刚愎自用</td></tr>
<tr><td>用人</td><td style="color:#16a34a;">知人善任，人尽其才</td><td style="color:#dc2626;">嫉贤妒能，亲小人远君子</td></tr>
<tr><td>治国</td><td style="color:#16a34a;">宽严相济，以民为本</td><td style="color:#dc2626;">暴政虐民，众叛亲离</td></tr>
</table>
</div>
<p>历史的车轮滚滚向前，但人性的规律从未改变。读懂这些，才算真正读懂了明朝。</p>
</div>
</div>'''
    
    return s1 + s2 + s3 + s4 + s5


def make_sections_en(title, key_points):
    s1 = f'''<div class="section-01">
<div class="section-header"><div class="num-01">01</div><div class="section-title">Historical Context</div></div>
<div class="section-body">
<p class="bluf">Chapter "{title}" — the historical backdrop and power dynamics.</p>
<div class="dual-grid">
<div class="dual-card good"><div class="label">Key Situation</div><div class="value">{key_points[0][:60] if key_points else title[:60]}</div></div>
<div class="dual-card bad"><div class="label">Hidden Risks</div><div class="value">Intertwined interests — one wrong move, total collapse</div></div>
</div>
<p>{key_points[0][:200] if key_points else ''}</p>
</div>
</div>'''
    
    s2 = f'''<div class="section-02">
<div class="section-header"><div class="num-02">02</div><div class="section-title">Core Conflicts</div></div>
<div class="section-body">
<p class="bluf">Power, interest, survival — three simultaneous games.</p>
<div class="flow-row">
<div class="flow-step">Interest博弈</div><span class="flow-arrow">&rarr;</span>
<div class="flow-step">Power Struggle</div><span class="flow-arrow">&rarr;</span>
<div class="flow-step">Survival Choice</div><span class="flow-arrow">&rarr;</span>
<div class="flow-step">History's Path</div>
</div>
<div class="data-row">
<div class="data-card"><div class="num">博弈</div><div class="tag">Multiple interests</div></div>
<div class="data-card"><div class="num">抉择</div><div class="tag">Turning point</div></div>
<div class="data-card"><div class="num">代价</div><div class="tag">A generation pays</div></div>
</div>
<p>{key_points[1][:200] if len(key_points) > 1 else key_points[0][:200] if key_points else ''}</p>
</div>
</div>'''
    
    s3 = f'''<div class="section-03">
<div class="section-header"><div class="num-03">03</div><div class="section-title">Key Figures & Choices</div></div>
<div class="section-body">
<p class="bluf">Behind every turning point lies character and choice.</p>
<div class="dual-grid">
<div class="dual-card good"><div class="label">Wise Moves</div><div class="value">Read the moment, follow the tide</div></div>
<div class="dual-card bad"><div class="label">Fatal Errors</div><div class="value">Dogmatic, going against the current</div></div>
</div>
<p>{key_points[2][:200] if len(key_points) > 2 else key_points[0][:200] if key_points else ''}</p>
</div>
</div>'''
    
    s4 = '''<div class="section-04">
<div class="section-header"><div class="num-04">04</div><div class="section-title">Historical Impact</div></div>
<div class="section-body">
<p class="bluf">Small events can redirect an entire empire.</p>
<div class="flow-row">
<div class="flow-step">Immediate</div><span class="flow-arrow">&rarr;</span>
<div class="flow-step">Cascade</div><span class="flow-arrow">&rarr;</span>
<div class="flow-step">Long-term</div><span class="flow-arrow">&rarr;</span>
<div class="flow-step">Verdict</div>
</div>
<div class="data-row">
<div class="data-card"><div class="num">短期</div><div class="tag">Direct consequences</div></div>
<div class="data-card"><div class="num">中期</div><div class="tag">Cascade effects</div></div>
<div class="data-card"><div class="num">长期</div><div class="tag">Historical verdict</div></div>
</div>
<p>History never happens in isolation. Every decision sends ripples across the empire.</p>
</div>
</div>'''
    
    s5 = '''<div class="section-05">
<div class="section-header"><div class="num-05">05</div><div class="section-title">Lessons from History</div></div>
<div class="section-body">
<p class="bluf">History teaches wisdom — real insight comes from seeing yourself in it.</p>
<div class="comparison-table">
<table>
<tr><th>Dimension</th><th>Positive Lesson</th><th>Negative Warning</th></tr>
<tr><td>Decision</td><td style="color:#16a34a;">Seek counsel, listen widely</td><td style="color:#dc2626;">Dictatorial, stubborn</td></tr>
<tr><td>Talent</td><td style="color:#16a34a;">Right person, right role</td><td style="color:#dc2626;">Jealous of ability, trust flatterers</td></tr>
<tr><td>Governance</td><td style="color:#16a34a;">Balance firmness with mercy</td><td style="color:#dc2626;">Tyrannical, alienating the people</td></tr>
</table>
</div>
<p>The wheel of history turns forward, but human nature never changes. Understanding these is understanding the Ming Dynasty.</p>
</div>
</div>'''
    
    return s1 + s2 + s3 + s4 + s5


def generate_chapter(ch, emperor):
    """Generate zh+en HTML files for one chapter."""
    title = ch['title']
    body = ch.get('body_full', ch.get('body', ''))
    info_num = ch['info_num']
    key_points = extract_key_points(body, 3)
    
    # Chinese
    zh = f'''<!DOCTYPE html>
<html lang="zh-CN">
<head>
<meta charset="UTF-8">
<meta name="viewport" content="width=device-width, initial-scale=1.0">
<title>明朝那些事儿 · {emperor} · {title}</title>
{CSS}
</head>
<body>
<div class="container">
{BACK_ZH}
{LANG_SWITCH_ZH.format(fname_en=f"明朝那些事儿-{emperor}-{info_num}-info-en.html")}
<h1>明朝那些事儿 · {emperor} · {title}</h1>
<div class="subtitle">当年明月 · 明朝那些事儿</div>
<div class="divider"></div>
<div class="chapter-overview">
<p><strong>SCQA解读：</strong>本章「{title}」讲述{truncate(key_points[0] if key_points else title, 80)}。通过具体历史事件和人物抉择，展现明朝政治、军事、文化的复杂博弈。</p>
</div>
{make_kpis(title, body)}
{make_sections_zh(title, key_points)}
<div class="takeaway">
<div class="takeaway-title">📌 核心结论</div>
<p>「{title}」这一章节展现了明朝历史的一个侧面：权力斗争、人性抉择、历史走向，三者交织构成波澜壮阔的历史画卷。读懂这一章，便多了一份对那个时代的理解。</p>
</div>
{FOOTER_ZH}
</div>
</body>
</html>'''
    
    # English
    en = f'''<!DOCTYPE html>
<html lang="en">
<head>
<meta charset="UTF-8">
<meta name="viewport" content="width=device-width, initial-scale=1.0">
<title>Ming Dynasty Stories · {emperor} · {title}</title>
{CSS}
</head>
<body>
<div class="container">
{BACK_EN}
{LANG_SWITCH_EN.format(fname_zh=f"明朝那些事儿-{emperor}-{info_num}-info-zh.html")}
<h1>Ming Dynasty Stories · {emperor} · {title}</h1>
<div class="subtitle">Author: Mingyue Dang · Ming Dynasty Stories</div>
<div class="divider"></div>
<div class="chapter-overview">
<p><strong>SCQA:</strong> Chapter "{title}" covers {truncate(key_points[0] if key_points else title, 80)}. Through specific historical events and character choices, it reveals the complex political, military, and cultural dynamics of the Ming Dynasty.</p>
</div>
{make_kpis(title, body)}
{make_sections_en(title, key_points)}
<div class="takeaway">
<div class="takeaway-title">📌 Key Takeaway</div>
<p>Chapter "{title}" reveals one facet of Ming Dynasty history: power struggles, human choices, and historical trajectories intertwined into a magnificent historical tapestry. Understanding this chapter means understanding that era a little better.</p>
</div>
{FOOTER_EN}
</div>
</body>
</html>'''
    
    return zh, en


def main():
    with open(DATA_PATH, 'r', encoding='utf-8') as f:
        data = json.load(f)
    
    total = 0
    skipped = 0
    
    for section in data['sections']:
        emperor = section['emperor']
        chapters = section['chapters']
        
        for ch in chapters:
            info_num = ch['info_num']
            zh_path = os.path.join(BOOKS_DIR, f'明朝那些事儿-{emperor}-{info_num}-info-zh.html')
            en_path = os.path.join(BOOKS_DIR, f'明朝那些事儿-{emperor}-{info_num}-info-en.html')
            
            # Skip if both exist
            if os.path.exists(zh_path) and os.path.exists(en_path):
                skipped += 1
                continue
            
            zh_html, en_html = generate_chapter(ch, emperor)
            
            if not os.path.exists(zh_path):
                with open(zh_path, 'w', encoding='utf-8') as f:
                    f.write(zh_html)
                total += 1
            
            if not os.path.exists(en_path):
                with open(en_path, 'w', encoding='utf-8') as f:
                    f.write(en_html)
                total += 1
    
    print(f'Generated {total} files ({skipped} skipped)')


if __name__ == '__main__':
    main()
