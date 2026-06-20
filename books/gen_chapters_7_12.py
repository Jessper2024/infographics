#!/usr/bin/env python3
"""Generate infographic HTML files for 弹性生长 chapters 7-12 (zh + en)."""

import os

OUT = os.path.expanduser("~/.openclaw/workspace/infographics/books")
os.makedirs(OUT, exist_ok=True)

FONT_PATH = "../方正屏显雅宋简体.TTF"
BOOK_TITLE = "弹性生长"

# ── Chapter data ──────────────────────────────────────────────

chapters = [
    {
        "num": 7, "title": "普通人做自媒体能赚到钱吗",
        "en_title": "Can Ordinary People Make Money from Self-Media?",
        "subtitle_zh": "平台价值 vs 个人能力，以及「代码与媒体」这对不需要许可的杠杆",
        "subtitle_en": "Platform Value vs Individual Skill, and the Permissionless Leverage of Code and Media",
        "overview_zh": (
            "一位读者因工作难找想全职做自媒体，作者通过两个真实故事给出答案："
            "小王从知名工作室出走，发现离开平台后自己的能力并不值钱，最终回归；"
            "小张从电视台出走，单飞后心态变好、收入也能养活自己。"
            "关键差异：你在平台的收入靠的是平台的声望，还是你自己的积累？"
            "结论：业余做自媒体是世上最好的事之一——极低成本冒险，不断自我提升；"
            "但全职去做需要极低的生活预期和超级好的心态。"
        ),
        "overview_en": (
            "A reader struggles to find work and considers full-time self-media. The author "
            "answers through two real stories: Xiao Wang left a famous studio, only to realize "
            "his value came from the platform's reputation, not his skill—and returned. Xiao Zhang "
            "left traditional TV, finding satisfaction and self-sufficiency as a solo creator. "
            "The key difference: does your income come from the platform's prestige or your own accumulation? "
            "Conclusion: doing self-media as a side hustle is one of the best things in the world—"
            "low-cost adventure and continuous self-improvement; but going full-time "
            "demands extremely low life expectations and superb mental resilience."
        ),
        "kpis": [
            {"label_zh": "平台抽成真相", "label_en": "Platform Cut Reality",
             "val_zh": "15%在业内已是高比例——素人变现靠的是平台声望", "val_en": "15% is already high in the industry—amateurs monetize through platform prestige"},
            {"label_zh": "运气权重", "label_en": "Luck Weight",
             "val_zh": "自媒体成败与能力非强相关，运气占80%以上", "val_en": "Success in self-media is not strongly correlated with ability; luck accounts for 80%+"},
            {"label_zh": "业余优先", "label_en": "Side-Hustle First",
             "val_zh": "有正经工作的人才能豁达，专职者心态容易崩溃", "val_en": "Those with regular jobs stay philosophical; full-timers easily break down"},
            {"label_zh": "以年为单位", "label_en": "Think in Years",
             "val_zh": "所有大号都是从零积累，有的写十年，后两三年爆发", "val_en": "All big accounts built from zero; some wrote for 10 years, exploded in the last 2-3"},
        ],
        "sections": [
            {"border": "red", "title_zh": "小王出走的教训：你以为值钱的是自己",
             "title_en": "Xiao Wang's Lesson: You Think You're the Valuable One",
             "body_zh": "小王被知名工作室主编手把手培养，独当一面后却发现文章收入自己只分15%，心态崩溃后出走。自己开号做不起来，给别人投稿稿费还不如老东家。后来知道：主编和其他同事全是跑了又回来的——15%在业内已是高比例。小王能变现不是因为文章值钱，而是工作室声望高、影响力大。很多大厂人在三四十岁时才发现：离开平台，啥都不会做。",
             "body_en": "Xiao Wang was mentored by a famous studio editor, mastering the craft—then discovered he only got 15% of article revenue. His confidence shattered, he left. His own account failed; freelance pay was worse. He later learned: the editor and all colleagues had also left and returned. 15% was already high industry standard. Xiao Wang monetized through the studio's prestige, not his writing. Many Big Tech workers discover at 30-40: without the platform, they can do nothing."},
            {"border": "orange", "title_zh": "小张的突围：被看不上反而是起点",
             "title_en": "Xiao Zhang's Breakout: Being Underestimated Is the Starting Point",
             "body_zh": "小张是人大高才生，在电视台却被领导百般看不上——文章被毙、被改得面目全非。他业余开自媒体写了五六年，收入超过工资后果断出走。现在虽然没赚大钱，但心态极好：不用受气，有写作自主权，能养活自己。传统媒体的'稳定感'本就是幻觉——互联网冲击下迟早被裁，不如直面不确定。他正在走主编当年走过的路——用时间积累声望。",
             "body_en": "Xiao Zhang, a top university grad, was disdained by his TV station boss—articles killed, mangled beyond recognition. He started a self-media account on the side for 5-6 years. When income surpassed salary, he boldly left. Not rich now, but mentally free: no more office abuse, creative autonomy, self-sustaining. Traditional media's 'stability' was always an illusion—internet disruption meant eventual layoffs. Better to face uncertainty head-on. He's walking the editor's original path: building reputation over time."},
            {"border": "gold", "title_zh": "能力 vs 运气：怀才不遇几乎不存在",
             "title_en": "Skill vs. Luck: 'Unrecognized Talent' Hardly Exists",
             "body_zh": "年入千万的大博主并非能力比你强百倍——只是他们把能力通过时间置换成声望。同时太多人能力很强——聊美妆头头是道、说汽车停不下来——却一毛钱赚不到，这纯属实践和运气问题。怀才不遇几乎不存在：市场定价下，聪明脑袋是稀缺资源。但如果想大富大贵，运气占80%以上。冒险精神比智商重要得多——真正混得好的人往往不是最聪明的，而是敢于去干的人。",
             "body_en": "Million-dollar influencers aren't 100x more capable—they just converted skill into reputation over time. Meanwhile, countless knowledgeable people—beauty experts, car gurus—earn nothing. That's purely practice and luck. 'Unrecognized talent' barely exists: in market pricing, smart minds are scarce resources. But for great wealth, luck accounts for 80%+. Risk-taking spirit far outweighs IQ. Those who thrive aren't the smartest—they're the boldest."},
            {"border": "indigo", "title_zh": "为什么不要全职做自媒体",
             "title_en": "Why You Shouldn't Go Full-Time in Self-Media",
             "body_zh": "公务员是极度稳定的极端，自媒体是极度不稳定的另一个极端。业余写的时候心态轻松——不想写就停更；全职做后，越想讨好读者越被刁钻评论消耗殆尽。关键在于：没正经工作过，没顶着压力完成过项目，没爬过职场天梯——很多社会问题你理解不了，写出来的东西肤浅可笑。先去上班，哪怕拧螺丝，也能增加人生经验。决定做什么，都以年为衡量单位。",
             "body_en": "Civil service is extreme stability; self-media is extreme randomness. Side-hustling writers stay relaxed—stop when they want. Full-timers, desperate to please readers, get consumed by harsh comments. Key point: without real work experience, without completing projects under pressure, without climbing career ladders—you can't understand social issues. Your writing will be shallow and laughable. Get a job first, even factory work adds life experience. Everything worth doing is measured in years."},
            {"border": "pink", "title_zh": "代码与媒体：不需要许可的杠杆",
             "title_en": "Code & Media: Permissionless Leverage",
             "body_zh": "纳瓦尔说：代码和媒体就是不需要许可就能使用的杠杆。上架一个App可以在你睡觉时赚钱；写出来的文章可以在你睡着时有人看。这两个杠杆是新富背后的杠杆。同时写作本身就是最好的大脑训练——脑子里想得好好的却写不出来，说明逻辑混乱。持续写作就是在不断训练和整理自己的思维。世界上没有快速致富的捷径和教程——如果有，只能是帮卖教程的人快速致富。",
             "body_en": "Naval said: code and media are permissionless leverage. An app earns while you sleep; your writing gets read while you sleep. These two levers are behind the new rich. Writing itself is the best brain training—thinking clearly but writing poorly reveals logical chaos. Persistent writing trains and organizes your mind. There's no get-rich-quick shortcut or course—if there were, it only enriches the course sellers."},
        ],
        "takeaway_zh": "业余做自媒体绝对是世界上最好的几件事之一：极低成本冒险，不断提升自我，给生活增加可能性。但全职之前，请先确保你有极低的生活预期和超级好的心态。以年为衡量单位去坚持，长期优质的内容输出能力加上爆棚的运气，总有人能熬出头。最重要的是：先去社会里实实在在地生活，否则你写不出真正打动人的东西。",
        "takeaway_en": "Self-media as a side hustle is one of the best things in the world: ultra-low-cost adventure, continuous self-improvement, adding possibilities to life. But before going full-time, ensure extremely low life expectations and superb mental resilience. Measure in years. Consistent quality output plus explosive luck—some will eventually break through. Most importantly: live a real life in society first, or you'll never write anything that truly moves people.",
    },
    {
        "num": 8, "title": "房产税和房价有哪些关系",
        "en_title": "Property Tax and Housing Prices—What's the Relationship?",
        "subtitle_zh": "免征首套是个伪命题，高税率区域房价反而更高",
        "subtitle_en": "First-Home Exemption Is a False Problem; Higher-Tax Areas Actually See Higher Prices",
        "overview_zh": (
            "房产税是很多读者的关注热点。作者首先拆解一个常见误解：首套房不会免征——"
            "如果一个人有一套千万豪宅和一套普通住宅，该免征哪套？最可行的方案是全面开征然后退税。"
            "更反直觉的结论：征收房产税后，税率越高的区域房价反而越高、涨幅越大——"
            "因为好资源永远是稀缺的，有钱人会源源不断填充进来。"
            "但二、三线城市租金涨不动，普通人所在区域的房价则会与收入挂钩并有所下跌。"
        ),
        "overview_en": (
            "Property tax is a hot topic. The author first dismantles a common misunderstanding: "
            "first-home exemption won't work—if someone has a 20M yuan mansion and a 3M apartment, "
            "which gets exempted? The practical solution: tax all homes, then issue refunds. "
            "A counterintuitive finding: after property taxes are imposed, higher-tax areas see higher prices "
            "and bigger gains—because premium resources are always scarce, and the wealthy keep flowing in. "
            "But rents in second/third-tier cities won't rise; housing in ordinary areas will align with income and decline somewhat."
        ),
        "kpis": [
            {"label_zh": "首套免征不可能", "label_en": "First-Home Exemption: Impossible",
             "val_zh": "两套房价值悬殊→全面开征+退税才是可行方案", "val_en": "Two homes with vastly different values → universal tax + rebates is the only viable approach"},
            {"label_zh": "上海十年经验", "label_en": "Shanghai's Decade-Long Experiment",
             "val_zh": "首套免征+人均60㎡，年收200多亿但财政占比极低", "val_en": "First-home exempt + 60㎡ per capita; annual ~20B yuan but minimal fiscal share"},
            {"label_zh": "税率-房价悖论", "label_en": "Tax-Price Paradox",
             "val_zh": "房产税越高区域房价越高涨幅越大——好资源永远稀缺", "val_en": "Higher tax zones = higher prices and gains—premium resources are always scarce"},
            {"label_zh": "租金涨不动", "label_en": "Rent Stickiness",
             "val_zh": "除一线和强二线，租金由需求方决定，租客没钱就涨不了", "val_en": "Except tier-1 and strong tier-2, rent is demand-determined; broke tenants cap it"},
        ],
        "sections": [
            {"border": "red", "title_zh": "首套免征为什么是个伪命题",
             "title_en": "Why First-Home Exemption Is a False Problem",
             "body_zh": "假如你有两套房——一套两千万豪宅、一套天通苑三四百万普通住宅，政府该免征哪套？再假如在北京有别墅、在鹤岗也有一套——该免征哪套？这种税收成本高得无边无际。最可行的方案：全面开征，然后把房产信息录入系统，用计算机算出退税金额，直接打到你账户上。上海已征收十年：首套免征、人均60㎡以下免征、超出部分征税，但一年只收200多亿——对比卖地收入，杯水车薪。其他地方房价远低于上海，学这模式根本收不到钱。",
             "body_en": "If you have a 20M mansion and a 3M ordinary apartment—which gets exempted? A Beijing villa and a Hegang flat—which? The administrative cost is infinite. The practical solution: tax all, then compute rebates by algorithm and deposit directly. Shanghai has taxed for a decade: first-home exempt, 60㎡ per capita threshold applies, taxing only the excess. But annual collection is just ~20B—a drop compared to land sales. Other cities, with far lower prices, would collect almost nothing copying this model."},
            {"border": "orange", "title_zh": "为什么房租涨不动（除了一线）",
             "title_en": "Why Rents Won't Rise (Except in Tier-1)",
             "body_zh": "很多人以为房租是房东想涨就涨的。在北京当了多年租客又做了房东的作者告诉你：即便是北京，不少地方房租依然涨不动——附近租客没钱，怎么涨？二、三线城市更是供过于求，根本租不上价。这是经济学基本常识：价格由需求方决定，不是供给方。就像中国生产成本大增但出口消费品价格没变一样——如果成本可以随便转嫁给消费者，地球上就没有亏本买卖了。今后的趋势是：分化进一步加重。二、三线租金上不去+持有成本增加→房价可能下跌；一线热门地区房价和房租可能一起涨。",
             "body_en": "Many think landlords raise rent at will. The author, a former tenant and current landlord in Beijing, tells you: even in Beijing, many areas see stagnant rent—nearby tenants simply lack money. Second/third-tier cities are oversupplied, can't price up. Basic economics: price is set by demand, not supply. Like Chinese production costs surging but export consumer prices unchanged—if costs could freely transfer to consumers, no business would ever lose money. Future: divergence deepens. Tier-2/3: stagnant rents + rising holding costs → potential price drops. Tier-1 hotspots: prices and rents may rise together."},
            {"border": "gold", "title_zh": "高税率=高房价：反直觉的真相",
             "title_en": "Higher Tax = Higher Price: The Counterintuitive Truth",
             "body_zh": "那些开征房产税的国家最常见的情况是：税率越高的区域，房价越高，涨幅也越大。这让人大跌眼镜但逻辑很简单：好地方为什么房价高？因为有商场、有学校、有医院、房子新。开征房产税后低收入者搬离——但很快有别的有钱人填充进来。好资源永远是稀缺的、永远供给不足。只要经济持续发展、有钱人越来越有钱，这种区域的房价就会持续上涨。而大部分人所在的普通区域，因为大家现金流不足支撑高房价，房价会下跌，慢慢跟收入挂钩。",
             "body_en": "Countries that have imposed property taxes universally show: higher-tax zones = higher prices = bigger gains. This surprises but the logic is simple. Why are prices high in good areas? Shopping, schools, hospitals, new buildings. After taxation, low-income residents move out—but wealthy newcomers immediately fill in. Premium resources are always scarce, always undersupplied. As long as the economy grows and the rich get richer, prices in these areas keep rising. Ordinary areas, with residents lacking cash flow to support high prices, will see declines as prices gradually align with income."},
            {"border": "indigo", "title_zh": "美国模式：分化才是常态",
             "title_en": "The American Pattern: Divergence Is the Norm",
             "body_zh": "美国房产税税率从1%到3%不等，整体规律：税率越高区域条件越好、房价越高——富人永远有钱追逐好资源。几十年来看，美国房价整体上涨但集中在东西两海岸——如果去掉两海岸，中部区域在缓慢下跌。全世界趋势：房价越贵的地方抗跌能力越强，征收巨额房产税后依旧抗跌；房价越便宜的地方，房产税不高也涨不上去。坏处：出现明确的富人区与穷人区。好处：权利和义务对等——住高档社区多交税回馈社会，钱少住便宜社区，房价和房租都不高，政府还能提供生活保障。",
             "body_en": "US property tax rates range from 1% to 3%. The pattern: higher tax zones = better conditions = higher prices—the wealthy eternally chase premium resources. Over decades, US housing rose overall but concentrated on the two coasts; remove them and the Midwest slowly declined. Global trend: the priciest areas have the strongest price resilience, even under heavy taxation; the cheapest areas, with low taxes, still can't rise. Downside: clear rich/poor neighborhood segregation. Upside: rights match obligations—living in premium areas means higher taxes back to society; living cheaply means lower housing costs plus possible government support."},
            {"border": "pink", "title_zh": "强悍的人：乐观判断，当下按危机打理",
             "title_en": "The Strong: Optimistic Outlook, Crisis-Mode Present",
             "body_zh": "总结一句话送给读者：房产税或房地产税，第一要务是扩大财政收入，金额范围得跟之前卖地收入接近。按上海模式每人免征60㎡就收不上来钱。所以征是迟早的，但方式会更务实。对普通人来说，二、三线房产会失去投资属性慢慢回归居住属性。一线热门区域依然抗跌。最重要的是：强悍的人对未来都是乐观判断，但当下永远按危机时期来打理。控制现金流，准备过冬粮，小心谨慎走好每一步。",
             "body_en": "One sentence summary: property tax or real estate tax—the primary goal is expanding fiscal revenue to match prior land-sale income levels. Shanghai's per-capita 60㎡ exemption collects too little. So taxation is inevitable but will be pragmatic. For ordinary people: tier-2/3 real estate will lose investment attributes and return to residential function. Tier-1 hotspots remain resilient. Most importantly: the strong are always optimistic about the future but manage the present as if in crisis. Control cash flow, prepare winter provisions, walk every step with care."},
        ],
        "takeaway_zh": "房产税不是洪水猛兽——好资源永远稀缺，高税率区域房价不降反升。真正受影响的是二、三线城市，它们将回归居住属性而非投资属性，对老百姓来说未必是坏事。关键在于管理好自己的现金流：对未来的判断可以乐观，但对当下的打理永远按危机时期来。",
        "takeaway_en": "Property tax isn't a catastrophe—premium resources stay scarce, higher-tax areas see prices rise, not fall. The real impact hits tier-2/3 cities, which will return to residential rather than investment functions—not necessarily bad for ordinary people. The key: manage your cash flow well—be optimistic about the future but manage the present as if in crisis.",
    },
    {
        "num": 9, "title": "汇率、美债，对我们的生意和生活有哪些影响",
        "en_title": "Exchange Rates, US Debt—How They Affect Our Business and Life",
        "subtitle_zh": "美元加息周期下的全球困局与中国应对",
        "subtitle_en": "The Global Dilemma Under Dollar Rate Hikes and China's Response",
        "overview_zh": (
            "汇率本质是'被需要'的程度——一个国家能生产别人生产不了的东西，其货币就抢手。"
            "2022年美元暴力加息后，全球资金涌向美国吃利息，导致各国货币大幅贬值。"
            "各国的两难困局：加息保汇率→企业倒闭+房地产崩盘；降息保经济→外汇流出+汇率暴跌。"
            "人民币贬值并非灭顶之灾——出口略有受益但全球购买力恶化；真正的麻烦是美元债和汇率波动导致买卖无法做。"
            "长期来看，一切由先进生产力说了算——持续精进就能摆脱困局。"
        ),
        "overview_en": (
            "Exchange rates reflect 'being needed'—a country producing what others can't will see "
            "strong demand for its currency. After the US's aggressive 2022 rate hikes, global capital "
            "flooded into America for interest income, causing widespread currency depreciation. "
            "Every nation faces a dilemma: raise rates to defend currency → business failures + real estate "
            "collapse; cut rates to protect the economy → capital flight + currency crash. "
            "RMB depreciation isn't apocalyptic—exports benefit slightly but global purchasing power worsens; "
            "the real problem is dollar-denominated debt and exchange-rate volatility paralyzing trade. "
            "Long-term: advanced productivity decides everything—continuous improvement breaks the cycle."
        ),
        "kpis": [
            {"label_zh": "汇率=被需要", "label_en": "Exchange Rate = Being Needed",
             "val_zh": "能生产别人不能产的东西→货币抢手→汇率走高", "val_en": "Produce what others can't → currency in demand → rate rises"},
            {"label_zh": "美元霸权逻辑", "label_en": "Dollar Hegemony Logic",
             "val_zh": "全球认、随时花、随时换美债投资——其他货币做不到", "val_en": "Globally accepted, instantly spendable, freely convertible to bonds—others can't match"},
            {"label_zh": "加息两难困局", "label_en": "Rate Hike Dilemma",
             "val_zh": "加息保汇率→公司倒闭带崩房市；不加→外汇外流汇率暴跌", "val_en": "Hike to defend currency → firms collapse, housing crashes; don't hike → capital flight"},
            {"label_zh": "2023拐点", "label_en": "2023 Inflection Point",
             "val_zh": "加息不会一直持续，2023年大概率结束", "val_en": "Rate hikes won't continue indefinitely; likely ending in 2023"},
        ],
        "sections": [
            {"border": "red", "title_zh": "汇率就是'被需要'的程度",
             "title_en": "Exchange Rate = How Much You're Needed",
             "body_zh": "把汇率理解为一个交易价：中国需要美元买石油、芯片、铁矿，就得用人民币换美元；别人需要人民币买中国产品，就得用美元换人民币。来回交易形成价格。能生产别人都需要的产品，货币自然抢手、汇率上升。反之，只能种地、社会动乱的国家，货币没人需要，汇率自然低。有的小国干脆不用本国货币直接用美元——比如帕劳。港币本质上就是美元的'代金券'——上面印着'凭票即付'。美国货币坚挺的原因：全球需要美元买产品（包括石油），有钱人存美元避险；流通性极好，全世界都认。",
             "body_en": "Think of exchange rates as a transaction price: China needs dollars for oil, chips, iron ore—must exchange RMB. Others need RMB for Chinese goods—must exchange dollars. Back and forth creates a price. Producing what everyone needs → currency in demand → rate rises. Conversely, farming-only countries or chaotic societies → nobody needs their currency → rate stays low. Some small nations skip their own currency entirely—Palau uses dollars. The HK dollar is essentially a dollar 'voucher'—printed with 'payable on demand.' Dollar strength: global need for US products (including oil) + wealthy holding dollars as haven + unmatched liquidity."},
            {"border": "orange", "title_zh": "美元加息的全球冲击波",
             "title_en": "The Global Shockwave of Dollar Rate Hikes",
             "body_zh": "2022年美国10年期国债收益率达到4%。对普通人：10万元一年4000元利息，没什么感觉。对有钱人：这个利率高得吓人——他们买高利率理财产品需要冒赔掉本金的风险，但存美国银行或买美债基本无风险。全世界的钱涌向美国：做外贸的赚了100万美元，以前换成人民币消费投资，现在50万转去美国银行吃利息。这些钱还是你的，但抽走货币导致本地股市、房市下跌。最发达的国家的利息比发展中国家还高——资本当然跑向美国。",
             "body_en": "In 2022, US 10-year Treasury yield hit 4%. To ordinary people: 4,000 yuan interest on 100K—nothing. To the wealthy: terrifyingly high—their typical high-yield products risk principal loss, but US bank deposits or Treasuries are virtually risk-free. Global money floods America: an exporter earning $1M used to convert to RMB for consumption and investment; now $500K goes to US bank for interest. It's still your money, but draining currency crushes local stock and property markets. The most developed nation now offers higher interest than developing countries—capital inevitably flows to America."},
            {"border": "gold", "title_zh": "保汇率还是保房市：无解的两难",
             "title_en": "Defend Currency or Housing: The Unsolvable Dilemma",
             "body_zh": "美国之外的国家想遏制资本外逃？加息。美元利率4%，你给到8%，有钱人就不走了——但风险太大照样没人敢投。更致命的是：现代企业都是负债运营——老板给你发工资的钱是从银行贷的，进货、买机器也得靠贷款。银行加息，公司平白无故多出一笔开支，可能直接倒闭。每次大规模加息都倒掉一堆公司，这也是各国一般能不加息就不加息的原因。保汇率就拉高利率→房价波动；保房价就得降息→外汇流出、汇率下跌。美国自己加息公司也跟割麦子似的被割掉。20世纪80年代保罗·沃克一口气加息到19.1%，美国企业跟深秋蚂蚱一样成批倒下。",
             "body_en": "How do non-US nations curb capital flight? Raise rates. Dollar at 4%, you offer 8%, wealthy stay—but if risk is too high, still nobody dares invest. The killer: modern enterprises operate on debt—your salary is bank-loan funded, inventory and machinery too. Bank rate hikes mean sudden extra costs, potentially instant bankruptcy. Every major rate hike cycle kills batches of companies—why nations avoid hiking whenever possible. Defend currency → hike rates → housing wobbles. Protect housing → cut rates → capital flight + currency plunge. The US itself bleeds too: companies mowed down like wheat. In the 1980s, Paul Volcker hiked to 19.1%—US firms dropped like autumn locusts."},
            {"border": "indigo", "title_zh": "人民币贬值：没那么糟糕，也没那么好",
             "title_en": "RMB Depreciation: Not That Bad, Not That Good",
             "body_zh": "贬值后进口变贵——大豆（榨油+喂猪）涨价→肉价涨，能源原材料涨价→生活用品涨价、制造业成本上升。出口老板：原材料贵了、出口价格提不上去→赚得少了，可能裁员降工资。好处：产品便宜了利于出口——但美元加息导致全球老百姓都缺钱、消费欲望低。真正的大麻烦不是10%升贬，而是汇率波动太大导致买卖没法做：客户等着人民币再跌10%再下单，因为他们本有库存。汇率不稳定→双方买卖瘫痪。更严重的是美元债：借10亿美元本来还65亿人民币，汇率下跌后要还72亿——平白无故多了10%，很多企业一年利润才10%全搭进去了，还不上就破产，连带供应商和烂尾楼。",
             "body_en": "After depreciation: imports cost more—soybean (oil + pig feed) price rise → meat prices up; energy and raw materials up → daily goods up, manufacturing costs up. Exporters: raw materials pricier, export prices can't rise → thinner margins, potential layoffs or wage cuts. Benefit: cheaper products help exports—but dollar hikes mean global consumers are cash-strapped, demand weak. The real crisis isn't 10% moves—it's volatility making trade impossible: clients wait for another 10% RMB drop before ordering, relying on existing stock. Unstable rates paralyze trade. Worse: dollar-denominated debt. Borrowed $1B, originally 6.5B RMB to repay; after depreciation, 7.2B—a sudden 10% extra. Many firms have annual profits of just 10%—all gone to cover this gap. Default → bankruptcy → cascading supplier failures and unfinished buildings."},
            {"border": "pink", "title_zh": "人民币国际化与长期出路",
             "title_en": "RMB Internationalization and the Long-Term Path",
             "body_zh": "应对手段确实不多——不只中国不多，全世界都不多，只能任由美国折腾——谁让美元是世界货币。好消息是：加息是双刃剑，对发展中国家是割肉，对美国是刮骨，他们也疼。人民币将来大有前途，但现阶段占比不到3%，需要时间去积累信用，一点点渗透进世界人民的观念里，让大家慢慢接受人民币的信用——这种该走的路一步都少不了。从短期来看只能受美国影响，从长期来看一切是先进生产力说了算，我们只要不断精进，慢慢就可以摆脱这种困扰。",
             "body_en": "Response options are limited—not just for China, but globally. America calls the shots; the dollar is the world's currency. Good news: rate hikes cut both ways. For developing nations, they're flesh wounds; for America, they're bone-deep—they hurt too. RMB has great future potential but currently under 3% global share. It needs time to build credibility, gradually penetrating global consciousness, earning trust step by step—every step is necessary. Short-term: subject to US influence. Long-term: advanced productivity decides everything. Keep refining, and we'll gradually escape this predicament."},
        ],
        "takeaway_zh": "美元加息周期下，全球都在熬。汇率短期受美国影响不可避免，但长期由先进生产力决定。对于普通人：理解汇率波动背后的逻辑，不要被贬值恐慌绑架——10%的升贬对过日子影响没那么大。真正该关注的：控制个人杠杆，在加息周期别倒闭，现金流为王。",
        "takeaway_en": "Under the dollar rate-hike cycle, the whole world endures. Short-term, exchange rates inevitably follow US moves; long-term, advanced productivity dictates everything. For ordinary people: understand the logic behind volatility, don't be hijacked by depreciation panic—10% moves aren't life-changing. What truly matters: control personal leverage, survive the hiking cycle, cash flow is king.",
    },
    {
        "num": 10, "title": "房价波动的真正原因是什么",
        "en_title": "What Really Causes Housing Price Fluctuations?",
        "subtitle_zh": "房地产是实体经济，一线房价是通胀与观念的折现",
        "subtitle_en": "Real Estate Is Real Economy; Tier-1 Prices Are Discounted Inflation + Belief",
        "overview_zh": (
            "2022年央行声称'房地产是实体经济'，引发热议。作者从产业数据切入："
            "中国重工业25%以上挂钩房地产——城市化推动工业化，卖地收入支撑产业园建设。"
            "房价不是开发商控制的，本质是'黄金四十年'结束后的观念博弈。"
            "一线房价类似股票定价——是对未来价格的'折现'：有钱人相信30万/㎡，现在15万就划算。"
            "结论：除少数城市外，大部分城市房价将稳定甚至下跌——回归居住属性；"
            "一线城市房价会涨的共识可能依旧存在，取决于限购、首付、放水和'信仰'。"
        ),
        "overview_en": (
            "When the central bank declared 'real estate is the real economy' in 2022, it sparked debate. "
            "The author starts with hard data: 25%+ of China's heavy industry is tied to real estate—"
            "urbanization drove industrialization, land-sale revenue built industrial parks. "
            "Housing prices aren't developer-controlled; they're belief-battles after the 'Golden 40 Years.' "
            "Tier-1 prices resemble stock pricing—a 'discount' of future prices: the wealthy believe "
            "in 300K/㎡, so 150K today seems a bargain. Conclusion: except a few cities, most will "
            "see prices stabilize or fall—returning to residential function; tier-1 'it will rise' "
            "consensus may persist, depending on purchase limits, down payments, money printing, and 'faith.'"
        ),
        "kpis": [
            {"label_zh": "重工业25%+挂钩", "label_en": "25%+ Heavy Industry Tied",
             "val_zh": "钢筋水泥、化工机械四分之一以上服务房地产", "val_en": "Over a quarter of steel, cement, chemicals, machinery serves real estate"},
            {"label_zh": "黄金四十年结束", "label_en": "Golden 40 Years Ending",
             "val_zh": "技术红利+城市化+基建→各国均有40年高速期，结束后进入微增长", "val_en": "Tech dividend + urbanization + infrastructure → every nation's 40-year sprint, then micro-growth"},
            {"label_zh": "房价=未来折现", "label_en": "Price = Discounted Future",
             "val_zh": "一线房价类似DCF模型——相信2030年值30万/㎡，现在15万就划算", "val_en": "Tier-1 price like DCF—if you believe 300K/㎡ by 2030, 150K today is a bargain"},
            {"label_zh": "观念决定价格", "label_en": "Belief Determines Price",
             "val_zh": "大家都觉得未来差→不投资→未来真差；反之亦然——自我实现的预言", "val_en": "Everyone thinks future is bad → no investment → future really bad; the reverse also holds—self-fulfilling prophecy"},
        ],
        "sections": [
            {"border": "red", "title_zh": "房地产就是实体经济：产业真相",
             "title_en": "Real Estate IS the Real Economy: Industry Reality",
             "body_zh": "中国重工业有25%以上挂钩房地产——钢筋水泥、化工产品、机械设备四分之一服务房地产行业。房地产不景气，这些产能全部变成'过剩产能'。此外下游的家具、家电、装修设计、餐饮等产业也跟房地产业深度挂钩。我国是城市化推动了工业化，房地产居功至伟。基建的钱大头也由房地产出——卖地收入当首付，银行贷款或社会融资扩建基础设施，再卖地加收税还贷。老百姓贷款买房预支未来三十年收入，开发商拿小头，地方政府拿大头——然后改善市政、搞基建、建产业园。过去二十年城市面貌焕然一新，很大程度上是因为财政从房地产拿到了充足的钱投入其他领域。",
             "body_en": "China's heavy industry has 25%+ tied to real estate—a quarter of steel, cement, chemicals, machinery serves this sector. When real estate slumps, all becomes 'excess capacity.' Downstream: furniture, appliances, interior design, dining are all deeply linked. China's urbanization drove industrialization; real estate made seminal contributions. Infrastructure funding mostly came from real estate too—land-sale revenue as down payment, bank loans or social financing to expand facilities, then more land sales and taxes to repay. Citizens mortgaged 30 years of future income; developers got the small share, local governments the large—then upgraded cities, built infrastructure, created industrial parks. Two decades of urban transformation largely came from real-estate-funded fiscal capacity deployed elsewhere."},
            {"border": "orange", "title_zh": "黄金四十年与供给控制",
             "title_en": "Golden 40 Years and Supply Control",
             "body_zh": "美国、德国、日本、韩国在各自历史上都有长达四十年左右的快速发展期——技术铺开产生巨量红利，叠加人口进城加速城市化，国家主动投资基础设施，经济发展稳定，老百姓收入增长快。但'黄金四十年'结束后各国相继进入'微增长时代'。我国的很多城市房地产供应量一直被压着——最明显的就是深圳，商品房太少，稍有风吹草动有钱人就对赌'供低于求'加杠杆追高。如果深圳产业升级成功→房价超过香港；如果继续大放水→富人没处投资→继续买房；如果银行不给二套房放贷+限购→限制需求→房价长期横着，收益率还不如存款利息。",
             "body_en": "The US, Germany, Japan, South Korea each had roughly 40-year boom periods—technology diffusion creating massive dividends, urban migration accelerating cities, state infrastructure investment, stable growth, rising incomes. But after the 'Golden 40,' all entered 'micro-growth.' In China, many cities' housing supply has been deliberately constrained—most obviously Shenzhen, with far too few commercial units. Any slight trigger, the wealthy bet on 'undersupply' and leverage-chase prices. If Shenzhen upgrades its industry successfully → prices surpass Hong Kong. If money printing continues → the rich have nowhere else to invest → keep buying property. If banks restrict second-home loans + purchase limits → capped demand → prices flat for years, returns worse than bank interest."},
            {"border": "gold", "title_zh": "一线房价的折现模型",
             "title_en": "The Discounted-Future Model of Tier-1 Pricing",
             "body_zh": "炒股机构的'现金流折现法'：特斯拉股价高是因为木头姐计算2030年产能达2300万辆→一年赚的钱超捷克GDP→现在股价高怎么了？房价某种意义上也是未来价格在现在的'折现'。买房者凭直觉领悟：北、上、广未来房价会突破30万/㎡，现在15万买也划算。为什么觉得值30万？因为会一直放水、可能放开限购、北京成全球一线城市……其实万柳书院多年前开盘就十几万/㎡，根本是普通人任何时候都买不起的。2021年救市贷款从全国涌向深圳，甚至有人搞'证券化买房'。有钱人的观点就两个字：稀缺。土地不是无限供应的资源，一线城市控制人口→土地供应有限，每年能留下的都是能接盘房价的人群。",
             "body_en": "Investment firms use Discounted Cash Flow: Tesla's stock was sky-high because Cathie Wood calculated 23M vehicles by 2030—annual profit exceeding Czech GDP—so what if the stock price is high now? Housing prices, in a sense, are discounted future prices. Many buyers intuitively grasp: if Beijing/Shanghai/Guangzhou prices will break 300K/㎡, buying at 150K now is a deal. Why believe in 300K? Continuous money printing, potential removal of purchase limits, Beijing becoming a global tier-1 city… Actually, Wanshuyuan mansions sold at 100K+/㎡ years ago—forever unaffordable for ordinary people. 2021 relief loans poured nationwide into Shenzhen, some even 'securitized' house purchases. The wealthy's logic boils down to one word: scarcity. Land isn't infinite; tier-1 cities cap population → limited land supply. Every year only those who can bear the price remain."},
            {"border": "indigo", "title_zh": "通胀与观念：一切都是对赌",
             "title_en": "Inflation and Belief: Everything Is a Bet",
             "body_zh": "一线房产本质就两点：通胀和观念。对所有未来的预期本质上都是对赌。经济变差→大部分人没工作没收入，但另有大量人手里拿着几百上千万资金，实体产业萧条只能存入银行——如果实体一直不好转，可能转投房地产追高。2022年一季度居民存款新增7.82万亿元，是有记录以来最高值——90天平均每天800亿涌进银行。10%的人占90%的钱。但二、三线城市不同，大部分盘靠老百姓工资扛着。天津挨着北京，这两年房价跌得一塌糊涂——有钱人都拿钱去北京了。《人类简史》的核心洞见：人类先编出一个想象的东西，相信的人拿出资源去探索，说不定就成功了。编织伟大愿景的人，成功了是大神，失败了是骗子。未来房价是涨是跌，在很大程度取决于相信这些观念的人有多少。",
             "body_en": "Tier-1 real estate boils down to two things: inflation and belief. All future expectations are essentially bets. Economy worsens → most lose jobs and income, but many others sit on millions in cash. With real industry in depression, they park money in banks—if industry doesn't recover, they may pivot to real estate, chasing highs. Q1 2022: household deposits rose 7.82 trillion yuan—a record high—averaging 80 billion daily flowing into banks. 10% of people hold 90% of the money. But tier-2/3 cities differ: most housing is supported by ordinary wages. Tianjin, next to Beijing, saw prices collapse—the wealthy took their money to Beijing. Sapiens' core insight: humans first imagine something, believers commit resources to explore, and maybe it succeeds. Those who weave grand visions: gods if they succeed, frauds if they fail. Whether housing prices rise or fall largely depends on how many believe the story."},
            {"border": "pink", "title_zh": "五条判断：分化才是未来",
             "title_en": "Five Judgments: Divergence Is the Future",
             "body_zh": "除了少数城市，绝大部分城市房价会慢慢稳定下来，没什么投资价值，自然没什么房产泡沫——房价稳中向下，大家反而会过得轻松一些。一线城市房价会上涨的共识可能依旧存在——富人没什么可投资的，股市反复虐人，每次股市崩盘资金就跑到房地产。即便一线带头涨，缺钱地方的老百姓也不一定会跟进了。一线城市已不太需要卖地增加财政收入，其他城市需要但历史上房价都是一线带头先涨其他才会跟进。最关键的指标：看限购政策和首付比例会不会有变化。",
             "body_en": "Except a few cities, most will see prices stabilize—no investment value, thus no bubble. Prices trending gently downward, people actually live more easily. The tier-1 'will rise' consensus may persist—the wealthy have nowhere else to invest, stock markets repeatedly torture believers, each crash sends money to real estate. Even if tier-1 leads a price increase, cash-strapped regions' residents may not follow. Tier-1 cities barely need land-sale revenue anymore; others do, but historically prices only rise when tier-1 leads first. The most critical indicators: purchase limit policies and down payment ratio changes."},
        ],
        "takeaway_zh": "房价不是开发商可以操控的数字，而是亿万人用真金白银投票形成的观念共识。一线城市的房价本质是少数有钱人对未来的折现对赌——只要有足够多的人相信，这个游戏就能继续。但对于绝大多数城市，'黄金四十年'结束后房价将温和回归居住属性，这对老百姓而言也许反而是好事。",
        "takeaway_en": "Housing prices aren't numbers developers can manipulate—they are belief-consensus formed by millions voting with real money. Tier-1 prices are essentially a discounted-future bet by the wealthy minority—as long as enough believe, the game continues. But for the vast majority of cities, after the Golden 40 Years, prices will gently return to residential function—which may actually be good for ordinary people.",
    },
    {
        "num": 11, "title": "出生率下降后，房价会跌吗",
        "en_title": "Will Housing Prices Drop After Birth Rates Decline?",
        "subtitle_zh": "人口负增长的城镇化分层效应与一线城市为何不跌反涨",
        "subtitle_en": "Urbanization Layering Under Population Decline and Why Tier-1 Cities Rise, Not Fall",
        "overview_zh": (
            "人口下降会导致房价全面下跌吗？作者给出的答案出人意料："
            "人口不是均匀变少，而是分层流动——农村空心化→小城市人口流失→大城市持续膨胀。"
            "日本、韩国、美国的先例表明：老龄化越严重，首都圈房价反而越坚挺——"
            "因为货币超发通过信贷渠道优先流入富人手中，富人在危机时期疯狂抢购稀缺资产。"
            "结果：一线城市的超级都市圈越来越大，房价在房产税下继续上涨；"
            "而绝大多数城市失去投资属性后，房价温和回归——老百姓反而不焦虑了。"
        ),
        "overview_en": (
            "Will population decline cause across-the-board housing price drops? The author's answer "
            "is surprising: population doesn't shrink evenly—it flows in layers: rural hollowing out "
            "→ small-city population loss → megacities keep swelling. Japan, Korea, and the US show: "
            "the more severe the aging, the more resilient capital-city housing prices—because "
            "money printing flows through credit channels to the wealthy first, who frantically "
            "buy scarce assets during crises. Result: tier-1 megacity regions grow ever larger, "
            "prices rise even under property tax; while most cities lose investment attributes, "
            "prices gently stabilize—and ordinary people paradoxically stop feeling anxious."
        ),
        "kpis": [
            {"label_zh": "人口分层流动", "label_en": "Layered Population Flow",
             "val_zh": "一线吸全国人才→大城市吸小城富人→小城吸农村青年→农村消亡", "val_en": "Tier-1 absorbs national talent → big cities absorb small-city wealthy → small cities absorb rural youth → villages vanish"},
            {"label_zh": "首尔/东京先例", "label_en": "Seoul/Tokyo Precedent",
             "val_zh": "老龄化越严重首都圈房价越坚挺，'江南不败'的韩国传说", "val_en": "More aging = stronger capital-region housing; Korea's 'Gangnam Unbeatable' legend"},
            {"label_zh": "信贷渠道偏差", "label_en": "Credit Channel Bias",
             "val_zh": "超发货币通过抵押→富人先拿到→加杠杆→推高稀缺资产", "val_en": "Printed money flows through collateral → wealthy get first → leverage → push up scarce assets"},
            {"label_zh": "换仓马太效应", "label_en": "Portfolio Rebalancing Matthew Effect",
             "val_zh": "不景气地区富人去南方/一线换仓，让差的更差、好的更好", "val_en": "Stagnant-area wealthy rebalance to south/tier-1, worsening the worse and bettering the better"},
        ],
        "sections": [
            {"border": "red", "title_zh": "人口不是均匀地减少",
             "title_en": "Population Doesn't Shrink Evenly",
             "body_zh": "作者的老家乡镇经历了完整的'下沉'过程：他小时候一个班二三十人——那是中国最后一次婴儿潮的尾巴。如今乡镇学校撤销，剩下个位数学生划归县里，70%的房子空置卖不掉。人口流动的链条：乡镇孩子考上大学→去大城市发展→能力强去一线扎根；县城有钱人→去省城买房；村里年轻人→去县城买房（不买房可能娶不到媳妇）；村里老人留守→直至消亡。人口减少10%不是每个城市均匀减10%，而是自下而上把房子空出来——农村大量荒废，小城市人口锐减，但核心一线人口更多更密集。日本也一样：乡村彻底衰败只剩温泉村和度假村，东京圈半径50公里范围聚集4000万人——经济规模比俄罗斯都大。",
             "body_en": "The author's rural hometown experienced complete 'downward flow': his childhood class had 20-30 students—the tail of China's last baby boom. Now: township schools dissolved, remaining single-digit students merged into county schools, 70% of houses empty and unsellable. The chain: rural kids enter college → move to big cities → the capable root in tier-1; county wealthy → buy in provincial capitals; village youth → buy in county seats (no house = no marriage); elderly left in villages → until extinction. Population declining 10% doesn't mean every city shrinks 10%—houses empty from bottom up. Rural areas hollow out massively, small cities bleed population, but core tier-1 cities grow denser. Japan: countryside virtually died except hot-spring and resort villages; Tokyo's 50km-radius zone holds 40M people—economic output exceeding Russia's."},
            {"border": "orange", "title_zh": "日本、韩国的镜子",
             "title_en": "The Mirror of Japan and Korea",
             "body_zh": "日本头部城市人口越大的流入越多。东京圈现在已扩展到大阪的五六倍——以前说'东京大阪'，现在大阪已成东京的零头。首尔更极端：人口持续向首尔聚集，几乎所有拿得出手的企业也全聚集到首尔。江南区的房价从1997年开始一路飙升——经济好时小涨，经济不好时反而大涨，新冠疫情后更是超级涨。'江南不败'的传说：每次大危机政府放水，富人拿到钱没处投→优先抢购稀缺资产→全韩国最稀缺就是江南区房产→疯抢→涨得更离谱。文在寅上台主打'公平'和治理房价——可从经济规模看，大首尔区占韩国40%，第二名釜山只有首尔的十分之一。顶着房产税房价继续上涨——这个趋势在发达国家特别明显，美国、日本、德国都一样。",
             "body_en": "Japan's top cities: the bigger, the more inflow. Tokyo's metro area is now 5-6× Osaka's size—once 'Tokyo and Osaka,' now Osaka is a Tokyo footnote. Seoul is more extreme: population continuously concentrates in Seoul, nearly every notable company clusters there. Gangnam prices have soared since 1997: modest rises in good times, explosive rises in bad times, supercharged after COVID. The 'Gangnam Unbeatable' legend: every major crisis triggers government money printing; the wealthy, with nowhere to invest, rush to scarce assets—all of Korea's scarcest is Gangnam real estate → bidding wars → absurd appreciation. President Moon campaigned on 'fairness' and taming housing prices—but Greater Seoul accounts for 40% of Korea's economy, second-place Busan barely one-tenth of Seoul. Prices rise despite property tax—this pattern is stark across developed nations: the US, Japan, Germany, all the same."},
            {"border": "gold", "title_zh": "富人和穷人的信贷差别",
             "title_en": "The Credit Difference Between Rich and Poor",
             "body_zh": "货币超发是怎么往下走的？通过信贷——从银行借钱流入经济体。资产越值钱的人越能借到超发的钱。2021年12月央行降准释放1.2万亿——普通人能借出来吗？不能！银行要抵押，谁的房子值钱谁就能贷到更多的款。超发出来的钱大部分进入一线大城市→多多少少进入房市→推高房价。张三觉得钱会越印越多→抵押房子贷款再买一套→等政府放水升值后卖掉。这就是击鼓传花。美股也是一个逻辑——不是大家的真金白银推上去的，是美国放水→机构借钱买美股→股价涨→全世界借钱再买→循环推高。如果没有增量资金，就陷入半死不活。富人用银行的钱赚钱，普通人只能赚回自己的工资——赚钱速度天壤之别。当然破产速度也是天壤之别——我们常听说富人破产，却很少听说穷人破产——穷人向来穷得很稳定。",
             "body_en": "How does money printing propagate? Through credit—bank loans flowing into the economy. The more valuable your assets, the more printed money you can borrow. Dec 2021: PBOC cut reserve requirement, releasing 1.2 trillion yuan. Could ordinary people borrow it? No! Banks demand collateral—whose house is worth more gets bigger loans. Printed money flows mostly into tier-1 cities → more or less enters housing → pushes prices up. Zhang San believes money will keep printing → mortgages his house for another → waits for government easing to appreciate and sell. It's a hot-potato game. US stocks follow the same logic—not real money pushing them up, but US printing → institutions borrow to buy → prices rise → global borrowing to buy more → self-reinforcing cycle. Without fresh money, everything stagnates. The wealthy earn with bank money; ordinary people only earn their wages—earnings speeds are worlds apart. Bankruptcy speeds too: we often hear of rich bankruptcies, rarely poor ones—the poor are stably poor."},
            {"border": "indigo", "title_zh": "换仓效应：差的更差，好的更好",
             "title_en": "Portfolio Rebalancing: Worse Gets Worse, Better Gets Better",
             "body_zh": "为什么这两年环京房价腰斩、东北不怎么样、天津一塌糊涂？因为不景气地方的有钱人在抛盘去南方了。有人在东北有五套房但多年不涨——理智做法是卖掉换成升值前景更好的房子。毕业后到北京专门找能解决工作居住证的地方上班，工资低也没事——就是为了拿到房票后把老家房子'换仓'到一线。这两年房地产不景气加速了换仓进程——不景气地方有钱人抛盘去南方/一线→不景气地方惨上加惨。一线房子平均持有时间五年以上，换手率极低——一个东西想持续升值的重要原则就是大家都握在手里不抛。美股也是这样——换手率极低。什么时候股民买了股票像持房子一样不急于抛出，股市也会越来越好。",
             "body_en": "Why have Beijing-ring prices halved, the Northeast slumped, Tianjin collapsed in the last two years? Because wealthy people in stagnant areas are dumping property to move south. Someone in the Northeast with 5 houses that haven't appreciated—the rational move is to sell and buy properties with better upside. Graduates take low-paying Beijing jobs just for residency permits—to get a 'housing ticket' and rebalance hometown property into tier-1. The recent property downturn accelerated this rebalancing—stagnant areas' wealthy dumping for south/tier-1 → stagnant areas worsening further. Tier-1 average holding period exceeds 5 years, turnover is extremely low—a key principle for sustained appreciation is everyone holding tight. US stocks work the same—very low turnover. When stockholders hold as patiently as homeowners, stock markets will stabilize too."},
            {"border": "pink", "title_zh": "失去投资属性后：老百姓反而不焦虑了",
             "title_en": "After Losing Investment Status: People Paradoxically Relax",
             "body_zh": "一线城市的房子会贵得离谱，但其他地方因为失去投资属性，楼市变得越来越温和。如果买了房也不涨，大家就不会再囤房子了→房价走低→当地人不焦虑了。房子不涨→大家不着急买房→租房也无所谓。天津的现状：几个朋友租房住，买得起也不买，口头禅是'反正也会跌下去，着什么急'。看出来了吧：房子不涨，很多人就没有了'刚需'——不过这个去泡沫的过程很痛苦，因为目前我国大部分人都有房，房价下跌已经让很多地方的老百姓非常郁闷。个别城市全市只有少数几个地方还在涨——有房的朋友们非常痛苦，没房的反而幸灾乐祸，有钱也不买，等着看笑话。这就是成熟国家的状态：一线贵到离谱，其他地方温和，年轻人不慌——只要房子不跳涨，大家就不慌，慢慢一起耗着。",
             "body_en": "Tier-1 housing will be absurdly expensive, but elsewhere, losing investment attributes, markets grow gentle. If buying yields no appreciation, people stop hoarding → prices drift down → locals stop feeling anxious. No appreciation → no rush to buy → renting becomes fine. Tianjin's reality: several friends rent despite being able to buy, mantra: 'It'll just fall anyway, what's the rush?' See the pattern: without price hikes, many lose 'urgent demand'—but this de-bubbling process is painful, since most Chinese own homes and price declines have already made many miserable. In some cities only a few zones still rise—homeowners suffer, non-owners gloat, refusing to buy even with money, waiting to watch the show. This is mature-nation status: tier-1 absurdly expensive, elsewhere moderate, youth unworried—as long as prices don't spike, nobody panics, just slowly wait it out together."},
        ],
        "takeaway_zh": "人口下跌不会让一线房价崩盘——货币超发通过信贷渠道优先给富人加杠杆去抢稀缺资产，这个循环在各国都被反复验证。但绝大多数城市将失去投资属性，房价温和回归。对普通人来说这未必是坏事：房子不涨，刚需消失，焦虑也就消失了。等着人口下跌去一线捡漏？可能性不大。",
        "takeaway_en": "Population decline won't crash tier-1 housing—money printing flows through credit channels to the wealthy first, who leverage-buy scarce assets, a cycle repeatedly verified across nations. But most cities will lose investment attributes, prices gently normalizing. For ordinary people, this may not be bad: without price hikes, 'urgent demand' vanishes, and so does anxiety. Waiting for population decline to pick up tier-1 bargains? Unlikely.",
    },
    {
        "num": 12, "title": "未来城市，是「鹤岗化」还是「深圳化」",
        "en_title": "Future Cities: 'Hegang-ization' or 'Shenzhen-ization'?",
        "subtitle_zh": "低增长是常态，接受多元化，给每个人一个合适的生态位",
        "subtitle_en": "Low Growth Is the Norm; Embrace Pluralism, Give Everyone Their Niche",
        "overview_zh": (
            "作者老家的地级市领导同学提供了一个犀利视角：除了一、二线大城市，"
            "国内大部分地方都是鹤岗——没有好资源、没有增长性产业、人才持续外流。"
            "城市衰落的三要素形成恶性循环：没资源→没好产业→人才不回来→更没产业。"
            "但这不是绝望的：发展是异类，停滞或微增长才是人类历史的常态。"
            "未来城市将分层演化：少数'深圳化'（高收入高房价高压高淘汰），更多'鹤岗化'（低压低房价低消费）。"
            "好的国家应该给不同的人提供不同选择——承认自己普通，才能选对正确的路。"
        ),
        "overview_en": (
            "The author's classmate, now a city-level official in his hometown, offers a sharp perspective: "
            "except tier-1 and tier-2 mega-cities, most of China mirrors Hegang—no premium resources, "
            "no growth industries, persistent brain drain. The three factors form a vicious cycle: "
            "no resources → no good industries → talent never returns → even fewer industries. "
            "But this isn't despair: development is the anomaly; stagnation or micro-growth is humanity's norm. "
            "Future cities will stratify: a few 'Shenzhen-ized' (high income, high prices, high pressure, high elimination), "
            "many more 'Hegang-ized' (low pressure, low prices, low consumption). "
            "A good nation provides different choices for different people—only by accepting you're ordinary can you choose the right path."
        ),
        "kpis": [
            {"label_zh": "衰落三要素", "label_en": "Three Decline Factors",
             "val_zh": "没好资源→没增长产业→人才外流→恶性循环锁死", "val_en": "No premium resources → no growth industries → brain drain → vicious cycle lock-in"},
            {"label_zh": "双重城市化", "label_en": "Dual Urbanization Waves",
             "val_zh": "第一波农村进城→第二波小城向大城市，第二波持续更久", "val_en": "Wave 1: rural to urban → Wave 2: small cities to mega-cities, Wave 2 lasts longer"},
            {"label_zh": "静态文化", "label_en": "Static Culture",
             "val_zh": "人情是另一种货币，编制是最热门职业——低增长社会的必然", "val_en": "Relationships are another currency; civil service is the hottest career—inevitable in low-growth society"},
            {"label_zh": "多元生态位", "label_en": "Plural Niches",
             "val_zh": "热血青年去深圳，恋家的人建设家乡——好国家提供不同选择", "val_en": "Ambitious youth go to Shenzhen; hometown-lovers build their hometowns—good nations offer different choices"},
        ],
        "sections": [
            {"border": "red", "title_zh": "为什么大多数地方都是鹤岗",
             "title_en": "Why Most Places Are Hegang",
             "body_zh": "作者和老家市级领导同学的谈话揭示了城市衰落的三个原因：没有好资源（港口、特产等，或资源耗尽）；没有增长性特别好的产业；人才持续外流。这三者形成恶性循环——没有资源就发展不出产业，没有产业人才考大学走了就不回来（回来也找不到对口工作），人才不回来更没有新兴产业。老家几十年处于持续放血状态。而有资源的城市：先做资源买卖积累本钱，再赶在资源耗尽前转型——但资源型城市大多有依赖症，转型失败的也很多。鹤岗成了典型——资源耗尽后一切都锁死了。",
             "body_en": "The author's conversation with his city-official classmate revealed three reasons cities decline: no premium resources (ports, specialties, or depleted resources); no strongly growing industries; persistent brain drain. These form a vicious cycle—no resources means no industries, no industries means college-bound talent never returns (no matching jobs if they did), no talent means even fewer industries. The author's hometown bled continuously for decades. Cities with resources: first trade resources for capital, then transform before depletion—but resource cities mostly develop dependency syndromes; many fail at transition. Hegang became the poster child—everything locked down after resources ran out."},
            {"border": "orange", "title_zh": "静态文化：人情是货币，编制是信仰",
             "title_en": "Static Culture: Relationships as Currency, Civil Service as Religion",
             "body_zh": "在增长速度很慢的社会里，人情就是另一种货币——子女找工作、出门办事，不找点关系心里不踏实。'拼搏奋斗''出人头地'的想法会很淡薄，反而对'稳定'有独特需求。公务员是最热门的职业——考不上退而求其次去电厂等国营单位。不只山东这样，哪儿都差不多：民营企业不好的地方这种观念就越重，而这种观念又束缚民营企业——稍微有点能力的人都进了体制，民营企业自然发展不好，又反过来强化'唯有公差高'。古代'读书高'说的不是知识是生产力，而是读书可以考取功名——看着是说读书，其实说的是考编制。另一个魔幻现象：买房。低房价地方只有公务员能贷到款，其他人靠民间借贷——找亲戚朋友'融资'。县城有钱人也去小城市买房——所以县城同时流失年轻人和有钱中年人。",
             "body_en": "In slow-growth societies, relationships become another currency—finding jobs for children, getting anything done, without connections you feel insecure. Ideas like 'struggle hard' and 'rise above' fade; craving for 'stability' becomes unique. Civil service is the hottest career; if you can't pass, fall back to state-owned power plants. Not just Shandong—everywhere similar: the worse private enterprise develops, the stronger this belief, and this belief shackles private enterprise—anyone with some ability enters the system, private firms stagnate, reinforcing 'nothing beats officialdom.' Ancient 'scholarship is supreme' didn't mean knowledge is productivity—it meant exams lead to official posts. Another bizarre phenomenon: housing. In low-price areas, only civil servants get bank loans; everyone else relies on private lending—financing through relatives and friends. County wealthy also buy in small cities—so counties simultaneously lose young people and wealthy middle-aged."},
            {"border": "gold", "title_zh": "双重城市化：第一波已尽，第二波正酣",
             "title_en": "Dual Urbanization: Wave 1 Done, Wave 2 Underway",
             "body_zh": "每个发达国家历史上都有一段超级基建时期——全国大拆大建。但很快实行不下去——因为需要老百姓极大财力支持，基层储蓄耗尽就停了。然后无一例外出现'二次城市化'：第一波是农村人进城→城市大规模拆迁扩张，到了一定程度就停了。第二波是小城市向大城市再来一波→有才华的人选择去大城市打拼。东京、首尔、洛杉矶和旧金山都是这样。第一波和第二波有重合但第二波持续更久。结果：各国除了大城市，其他地方出现不同程度的停滞和倒退。美国小城市和旧金山画风完全不同；日本小地方和东京完全两个模样。中国今后也会慢慢呈现这种状态。房地产拉经济有根最后的红线——开发商开发出来的房子，当地老百姓不买了。如果买说明还有购买力；不买说明没钱了——开发商就不拿地了，低房价城市就这样形成。",
             "body_en": "Every developed nation had a super-infrastructure period—nationwide construction boom. Then it quickly became unsustainable—it required massive citizen financial support; once grassroots savings were exhausted, it stopped. Then came 'secondary urbanization' everywhere: Wave 1—rural people entering cities → massive urban demolition and expansion, stopping at a certain point. Wave 2—small cities to mega-cities → talented people choosing big cities to strive. Tokyo, Seoul, LA, San Francisco all followed this. Waves overlap but Wave 2 lasts longer. Result: everywhere except major cities experiences varying stagnation and decline. US small towns and San Francisco look like different countries; Japanese small places and Tokyo, two completely different worlds. China will gradually show the same pattern. Real estate's economic engine has a final red line: when locals stop buying the developments. If they buy, purchasing power remains; if they stop, money's gone—developers stop acquiring land, low-price cities form this way."},
            {"border": "indigo", "title_zh": "深圳化：高收入、高房价、高压、高淘汰",
             "title_en": "Shenzhen-ization: High Income, High Prices, High Pressure, High Elimination",
             "body_zh": "一个研究图形算法的博士，成果顶级但国内没有厂家用得着。导师说'去美国碰碰运气'，机票已订好时大厂技术负责人打来电话——向领导汇报后领导思路开放，拨钱资助继续研究。几年后出成果，他不再是当年的穷博士——有了实验室、团队，住进北京好小区。这种事以前只能在其他国家发生，现在在我们身边越来越多——几乎无一例外集中在一线城市。一线城市人更多，思路视野更开阔，人才和优秀想法更容易被识别→拿到投资→形成正反馈。发达国家科技研发也是这个逻辑——拥有强大的'技术市场'，有才华的人公开叫卖，投资方给有前途的方案打钱，慢慢美国就成了全世界的'一线城市'。中国不出意外也会形成少数城市'深圳化'：高收入、高房价、高压力、高淘汰。",
             "body_en": "A PhD in graphics algorithms, world-class results but no domestic manufacturer could use them. His advisor said 'try your luck in America.' Flights booked, then a Big Tech lead called—pitched to his boss, who was open-minded, allocated funding for continued research. Years later, results emerged. He's no longer that impoverished PhD—has a lab, team, lives in a nice Beijing neighborhood. Such stories, once only possible abroad, now increasingly happen here—almost without exception concentrated in tier-1 cities. Tier-1 has more people, broader vision, talent and ideas more easily recognized → receive investment → positive feedback loop. Developed-nation tech innovation follows the same logic—powerful 'technology markets' where talented people openly pitch, investors fund promising proposals, gradually making America the world's 'tier-1 city.' China will likely see a few cities 'Shenzhen-ize': high income, high prices, high pressure, high elimination."},
            {"border": "pink", "title_zh": "多元生态位：承认普通才能选对路",
             "title_en": "Plural Niches: Accept Being Ordinary to Choose the Right Path",
             "body_zh": "好的国家的多元化就是给各种不同的人提供不同选择：热血青年去深圳建功立业，也可以选择在老家建设家乡。有没有那种躺平了还可以很舒服的生活？现阶段受发展水平和人口基数限制不太可能——除非家里有矿有产业。国家思路是'底线思维'：努力给老弱托底，逐步落实劳动法，走出传统无限内卷模式。如果有手有脚头脑正常的人不工作就比辛苦工作的人过得更好，那就是一个畸形的社会。'鹤岗化'小城和'深圳化'大城的财富差距会越来越大，但生活质量差距不会太大——大城市用大品牌，小城市用质量可靠价格便宜无品牌的同质化产品。成熟社会就是这样：给每个人一个合适的生态位，让每个人都能找到自己的位置——只要心态调整好，每个人都能过得挺不错。承认自己普通吧，这没什么不好。当你承认自己普通的时候，才能够选对正确的路。",
             "body_en": "A good nation's pluralism means providing different choices for different people: ambitious youth go to Shenzhen to build careers; others can stay and build their hometowns. Is there a 'lie flat comfortably' life? At current development levels and population scale, unlikely—unless you have family mines or businesses. National thinking is 'bottom-line mindset': support the elderly and weak, gradually implement labor laws, escape the endless involution model. If able-bodied, clear-minded people live better not working than those working hard—that's a deformed society, not a healthy one. The wealth gap between 'Hegang-ized' small cities and 'Shenzhen-ized' megacities will widen, but quality-of-life gap won't be huge—big cities use brands, small cities use reliable, cheap, unbranded equivalent products. Mature societies work like this: give everyone a suitable niche, let everyone find their place—with the right mindset, everyone can live quite well. Accept being ordinary—there's nothing wrong with it. Only when you accept being ordinary can you choose the right path."},
        ],
        "takeaway_zh": "发展是异类，停滞才是常态——人类有文字记录的五千多年历史中，低速和停滞是绝对的主旋律。未来城市将分层演变：少数深圳化为创新引擎，多数鹤岗化但生活质量未必差。成熟社会的标志不是所有人都住豪宅，而是每个人都能找到自己的生态位。承认自己普通，然后选择适合自己的那条路。",
        "takeaway_en": "Development is the anomaly; stagnation is the norm—across 5,000+ years of recorded human history, low speed and stasis are the dominant melody. Future cities will stratify: a few Shenzhen-ize as innovation engines; most Hegang-ize but quality of life won't necessarily be worse. The mark of a mature society isn't everyone in mansions—it's everyone finding their niche. Accept being ordinary, then choose the path that fits you.",
    },
]


# ── HTML Templates ──────────────────────────────────────────────

def kpi_card(label, value, color_class, idx):
    colors = {0: "#dc2626", 1: "#ea580c", 2: "#d97706", 3: "#4f46e5"}
    c = colors.get(idx, "#dc2626")
    return f"""
    <div style="background:#fff; border-radius:12px; padding:18px 16px; text-align:center;
                box-shadow:0 2px 8px rgba(0,0,0,.06); flex:1; min-width:180px;
                border-top:4px solid {c};">
      <div style="font-size:12px; color:#6b7280; margin-bottom:4px; letter-spacing:.5px;
                  text-transform:uppercase;">{label}</div>
      <div style="font-size:14px; color:#1f2937; line-height:1.5; font-weight:600;">{value}</div>
    </div>"""

def section_card(border_color, title, body):
    colors = {"red": "#dc2626", "orange": "#ea580c", "gold": "#d97706",
              "indigo": "#4f46e5", "pink": "#db2777"}
    c = colors.get(border_color, "#dc2626")
    return f"""
    <div style="background:#fff; border-radius:12px; padding:20px 22px;
                box-shadow:0 2px 8px rgba(0,0,0,.05); margin-bottom:14px;
                border-left:5px solid {c};">
      <div style="font-size:16px; font-weight:700; color:{c}; margin-bottom:8px;">{title}</div>
      <div style="font-size:14px; color:#374151; line-height:1.75;">{body}</div>
    </div>"""

def gen_html(ch, lang):
    is_zh = (lang == "zh")
    title_str = ch["title"] if is_zh else ch["en_title"]
    subtitle = ch["subtitle_zh"] if is_zh else ch["subtitle_en"]
    overview = ch["overview_zh"] if is_zh else ch["overview_en"]
    takeaway = ch["takeaway_zh"] if is_zh else ch["takeaway_en"]
    lang_label = "中文版" if is_zh else "English"
    chapter_label = f"第{ch['num']}章" if is_zh else f"Ch.{ch['num']}"
    catalog_text = "← 返回目录" if is_zh else "← Catalog"
    footer_text = f"《弹性生长》信息图 · {lang_label} · 由AI生成" if is_zh else f"Elastic Growth Infographic · {lang_label} · AI-Generated"

    kpi_html = "\n".join(
        kpi_card(k["label_zh"] if is_zh else k["label_en"],
                 k["val_zh"] if is_zh else k["val_en"], "", i)
        for i, k in enumerate(ch["kpis"])
    )

    section_html = "\n".join(
        section_card(s["border"],
                     s["title_zh"] if is_zh else s["title_en"],
                     s["body_zh"] if is_zh else s["body_en"])
        for s in ch["sections"]
    )

    return f"""<!DOCTYPE html>
<html lang="{'zh-CN' if is_zh else 'en'}">
<head>
<meta charset="UTF-8">
<meta name="viewport" content="width=device-width, initial-scale=1.0">
<title>弹性生长 · 第{ch['num']}章 – {title_str}</title>
<style>
@font-face {{ font-family:'FZXPYZS'; src:url('{FONT_PATH}') format('truetype'); }}
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

<!-- 1. Catalog link -->
<div class="pad" style="padding-bottom:0;">
  <a href="弹性生长-catalog.html" style="font-size:13px; color:#9ca3af; text-decoration:none;">{catalog_text}</a>
</div>

<!-- 2. Language badge -->
<div class="pad" style="padding-top:8px; padding-bottom:0; text-align:right;">
  <span style="display:inline-block; background:#e5e7eb; color:#6b7280; font-size:11px;
               padding:4px 10px; border-radius:20px; letter-spacing:.5px;">{lang_label}</span>
</div>

<!-- 3. H1 -->
<div class="pad" style="padding-top:16px; padding-bottom:0;">
  <h1 style="font-size:28px; font-weight:900; color:#1f2937; line-height:1.3;">
    弹性生长 · {chapter_label}<br><span style="color:#dc2626;">「{title_str}」</span>
  </h1>
</div>

<!-- 4. Subtitle -->
<div class="pad" style="padding-top:8px; padding-bottom:0;">
  <p style="font-size:15px; color:#6b7280; line-height:1.6;">{subtitle}</p>
</div>

<!-- 5. Divider -->
<div class="pad" style="padding-top:18px; padding-bottom:0;">
  <div style="height:4px; border-radius:2px;
              background:linear-gradient(90deg,#dc2626,#ea580c,#d97706,#4f46e5,#db2777);"></div>
</div>

<!-- 6. Overview -->
<div class="pad" style="padding-top:22px; padding-bottom:0;">
  <div style="background:linear-gradient(135deg,#eef2ff,#e0e7ff); border-radius:14px;
              padding:20px 24px; border:1px solid #c7d2fe;">
    <div style="font-size:13px; color:#4f46e5; font-weight:700; margin-bottom:8px;
                letter-spacing:1px;">
      {'📖 章节概述' if is_zh else '📖 Chapter Overview'}
    </div>
    <p style="font-size:14px; color:#3730a3; line-height:1.8;">{overview}</p>
  </div>
</div>

<!-- 7. KPI cards -->
<div class="pad" style="padding-top:24px; padding-bottom:0;">
  <div style="font-size:13px; color:#4f46e5; font-weight:700; margin-bottom:12px;
              letter-spacing:1px;">
    {'📊 核心指标' if is_zh else '📊 Key Metrics'}
  </div>
  <div style="display:flex; flex-wrap:wrap; gap:12px;">{kpi_html}</div>
</div>

<!-- 8. Sections -->
<div class="pad" style="padding-top:28px; padding-bottom:0;">
  <div style="font-size:13px; color:#4f46e5; font-weight:700; margin-bottom:12px;
              letter-spacing:1px;">
    {'🔍 深度解读' if is_zh else '🔍 Deep Dive'}
  </div>
  {section_html}
</div>

<!-- 9. Takeaway -->
<div class="pad" style="padding-top:28px; padding-bottom:0;">
  <div style="background:#fff; border-radius:14px; padding:22px 24px;
              border:2px solid #dc2626; position:relative;">
    <div style="position:absolute; top:-12px; left:24px; background:#dc2626; color:#fff;
                font-size:12px; font-weight:700; padding:4px 14px; border-radius:20px;
                letter-spacing:.5px;">
      {'💡 核心启示' if is_zh else '💡 Key Takeaway'}
    </div>
    <p style="font-size:15px; color:#1f2937; line-height:1.85; font-weight:500;
             padding-top:6px;">{takeaway}</p>
  </div>
</div>

<!-- 10. Footer -->
<div class="pad" style="padding-top:24px; text-align:center;">
  <div style="height:1px; background:#e5e7eb; margin-bottom:16px;"></div>
  <p style="font-size:12px; color:#9ca3af;">{footer_text}</p>
</div>

</div>
</body>
</html>"""


# ── Generate & Validate ─────────────────────────────────────────

generated = []
for ch in chapters:
    num = ch["num"]
    for lang, suffix in [("zh", "zh"), ("en", "en")]:
        fname = f"弹性生长-ch{num:03d}-info-{suffix}.html"
        path = os.path.join(OUT, fname)
        html = gen_html(ch, lang)
        with open(path, "w", encoding="utf-8") as f:
            f.write(html)
        # Validate
        size = os.path.getsize(path)
        with open(path, "r", encoding="utf-8") as f:
            content = f.read()
        checks = {
            "FZXPYZS": "FZXPYZS" in content,
            "#f5f1eb": "#f5f1eb" in content,
            "880px": "880px" in content,
            "flex-center": "flex" in content and "center" in content,
            "title": (ch["title"] if lang == "zh" else ch["en_title"])[:30] in content,
            "divider-gradient": "#dc2626" in content and "#ea580c" in content,
            "overview": "#4f46e5" in content,
            "takeaway": "#dc2626" in content,
            "footer": "弹性生长" in content if lang == "zh" else "Elastic Growth" in content,
        }
        all_ok = all(checks.values())
        status = "✅" if all_ok else "❌"
        print(f"{status} {fname}  {size:,}B  {checks}")
        generated.append((path, size, all_ok))

print(f"\n🎉 Total: {len(generated)} files generated")
print(f"   All passed: {all(g[2] for g in generated)}")
print(f"   Location: {OUT}")
PYEOF