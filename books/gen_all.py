#!/usr/bin/env python3
# -*- coding: utf-8 -*-
import os

outdir = "/Users/jessper/.openclaw/workspace/infographics/books"

CH = {}

# ── ch001 ──
CH["001"] = {
    "zh_title": "第一章 大脑——一切问题的起源",
    "en_title": "The Brain — The Origin of All Problems",
    "zh_overview": '本章是全书的起点。作者从脑科学角度出发，揭示了三重大脑（本能脑、情绪脑、理智脑）的进化历程与力量对比。本能脑3.6亿年、情绪脑2亿年、理智脑仅250万年，这决定了人类天性中的目光短浅与即时满足。焦虑的根源是\u201c想同时做很多事，又想立即看到效果\u201d。而耐心的关键不在于毅力，在于长远目光\u2014\u2014看清复利曲线、舒适区边缘、成长权重对比等规律，才能真正拥有耐心。',
    "en_overview": "This chapter is the book's foundation. The author reveals the triune brain (instinctive brain, emotional brain, rational brain) from an evolutionary neuroscience perspective. The instinctive brain is 360 million years old, the emotional brain 200 million years, but the rational brain only 2.5 million years \u2014 which explains humanity's innate short-sightedness and craving for instant gratification. Anxiety stems from 'wanting to do many things at once while expecting immediate results.' The key to patience is not willpower but long-term vision \u2014 understanding the compound interest curve, the edge of the comfort zone, and the growth weight comparison.",
    "kpi": [
        ["3.6<span class=\"kpi-unit\">亿年</span>", "本能脑进化历史", "爬行动物时代的产物"],
        ["2<span class=\"kpi-unit\">亿年</span>", "情绪脑进化历史", "哺乳动物时代的产物"],
        ["250<span class=\"kpi-unit\">万年</span>", "理智脑进化历史", "仅前额叶皮层成形期"],
        ["860<span class=\"kpi-unit\">亿</span>", "大脑神经元总数", "本能脑+情绪脑占近八成"],
    ],
    "en_kpi": [
        ["360M<span class=\"kpi-unit\"> yrs</span>", "Instinctive Brain Age", "Product of the reptilian era"],
        ["200M<span class=\"kpi-unit\"> yrs</span>", "Emotional Brain Age", "Product of the mammalian era"],
        ["2.5M<span class=\"kpi-unit\"> yrs</span>", "Rational Brain Age", "Prefrontal cortex formation period"],
        ["86<span class=\"kpi-unit\"> billion</span>", "Total Brain Neurons", "Instinct+emotional \u2248 80%"],
    ],
    "sections": [
        {
            "num": "01", "color": "01", "tag_zh": "进化根源", "tag_en": "Evolutionary Root",
            "title_zh": "三重大脑：本能、情绪与理智的角力",
            "title_en": "The Triune Brain: Instinct, Emotion & Reason",
            "desc_zh": "<strong>人类由内到外有三重大脑：本能脑（3.6亿年）、情绪脑（2亿年）、理智脑（250万年）。</strong>本能脑和情绪脑掌管潜意识和生理系统，运行速度高达11,000,000次/秒；而理智脑最快仅40次/秒且极耗能。这种力量悬殊导致我们的大多数决策源于本能和情绪而非理智。理智脑就像一个不满1岁的宝宝，在两个成年人面前势单力薄\u2014\u2014<strong>这解释了我们为什么\u201c明明知道，但就是做不到\u201d。</strong>",
            "desc_en": "<strong>Humans have three brain layers: the instinctive brain (360M yrs), emotional brain (200M yrs), and rational brain (2.5M yrs).</strong> The instinctive and emotional brains control the subconscious and physiological systems at 11,000,000 operations/second; the rational brain maxes at 40/sec and is extremely energy-hungry. This power imbalance means most decisions come from instinct and emotion, not reason. The rational brain is like a baby under 1 year old facing two full-grown adults \u2014 <strong>this explains why we \u201cknow what's right but can't do it.\u201d</strong>",
            "viz": "flow", "viz_data": [
                "本能脑<br>3.6亿年·爬行动物", "", "情绪脑<br>2亿年·哺乳动物", "", "理智脑<br>250万年·人类独有"
            ]
        },
        {
            "num": "02", "color": "02", "tag_zh": "焦虑之源", "tag_en": "Root of Anxiety",
            "title_zh": "焦虑的根源：急于求成与避难趋易",
            "title_en": "The Root of Anxiety: Haste and Avoidance",
            "desc_zh": "<strong>焦虑的5种形式\u2014\u2014完成焦虑、定位焦虑、选择焦虑、环境焦虑、难度焦虑\u2014\u2014归根结底一句话：想同时做很多事，又想立即看到效果。</strong>焦虑是天性，是人类默认设置，与道德品质无关。更深层的原因是大脑的生理结构：本能脑和情绪脑的基因被生存压力塑造，天性就是目光短浅、即时满足。在现代社会，这表现为\u201c避难趋易\u201d和\u201c急于求成\u201d：只做简单舒适的事，凡事希望立即看到结果。",
            "desc_en": "<strong>The 5 forms of anxiety \u2014 completion anxiety, positioning anxiety, choice anxiety, environmental anxiety, difficulty anxiety \u2014 boil down to: wanting to do many things at once while expecting immediate results.</strong> Anxiety is human nature, the default setting, unrelated to moral character. The deeper cause is brain physiology: the instinctive and emotional brains were shaped by survival pressure, making short-sightedness and instant gratification our default. In modern society, this manifests as \u2018avoiding difficulty\u2019 and \u2018seeking quick results.\u2019",
            "viz": "dual", "viz_data": {
                "no_h": "5种焦虑形式",
                "no_p": "完成焦虑·定位焦虑·选择焦虑·环境焦虑·难度焦虑",
                "yes_h": "根源就两条",
                "yes_p": "\u2460想同时做很多事 \u2461又想立即看到效果 \u2192 欲望>能力+缺乏耐心"
            }
        },
        {
            "num": "03", "color": "03", "tag_zh": "增值曲线", "tag_en": "Growth Curve",
            "title_zh": "复利曲线：前期缓慢，拐点后飞速增长",
            "title_en": "The Compound Interest Curve: Slow Start, Explosive Growth",
            "desc_zh": "<strong>复利曲线揭示了价值积累的普遍规律：前期增长非常缓慢，但到达拐点后会飞速增长。</strong>学习、成长、财富都遵循这一规律。问题是大多数人看不清全局，用天性这把短视之尺衡量，在拐点到来前就放弃了。对于没有特殊资源的普通人来说，坚信并践行这一规律，早晚能有所成就。前提是选择正确的方向，并在舒适区边缘一点一点扩展能力范围。",
            "desc_en": "<strong>The compound interest curve reveals a universal law of value accumulation: early growth is extremely slow, but after reaching an inflection point, growth becomes explosive.</strong> Learning, growth, and wealth all follow this pattern. The problem is most people can't see the big picture, measure with the short-sighted ruler of instinct, and give up before the inflection point. For ordinary people without special resources, believing in and following this law will eventually lead to achievement \u2014 provided they choose the right direction and expand at the edge of comfort zone.",
            "viz": "flow", "viz_data": [
                "缓慢积累期<br>看似无变化", "", "拐点到来<br>加速增长", "", "飞速增长期<br>复利威力显现"
            ]
        },
        {
            "num": "04", "color": "04", "tag_zh": "成长法则", "tag_en": "Growth Law",
            "title_zh": "舒适区边缘：在拉伸区刻意练习进步最快",
            "title_en": "Edge of Comfort Zone: Deliberate Practice in the Stretch Zone",
            "desc_zh": "<strong>无论个体还是群体，能力都以\u201c舒适区\u2014拉伸区\u2014困难区\u201d的形式分布。</strong>在舒适区边缘（拉伸区）刻意练习，进步最快。但人类天性恰好相反：欲望上急于求成\u2192在困难区受挫；行动上避难趋易\u2192在舒适区停滞。复利曲线和舒适区边缘是一对好朋友：它们组合在一起，让普通人在宏观上看到保持耐心的力量。",
            "desc_en": "<strong>Whether individual or collective, abilities are distributed in 'comfort zone \u2192 stretch zone \u2192 difficulty zone.'</strong> Deliberate practice at the edge of the comfort zone (stretch zone) yields the fastest progress. But human nature works oppositely: in desire we rush \u2192 failing in the difficulty zone; in action we avoid \u2192 stagnating in the comfort zone. The compound interest curve and comfort zone edge are perfect partners: together they let ordinary people see the power of patience at a macro level.",
            "viz": "flow", "viz_data": [
                "舒适区<br>停滞不前", "", "拉伸区<br>进步最快", "", "困难区<br>容易受挫"
            ]
        },
        {
            "num": "05", "color": "05", "tag_zh": "耐心真谛", "tag_en": "True Patience",
            "title_zh": "得耐心者得天下：长远目光胜过意志力",
            "title_en": "Patience Wins: Vision Over Willpower",
            "desc_zh": "<strong>耐心不是毅力带来的，而是长远目光带来的。</strong>成长权重对比揭示：改变量 > 行动量 > 思考量 > 学习量。只盯表层学习量会陷入\u201c越学越焦虑\u201d的怪圈；盯住底层改变量才能跳出无效勤奋。另一个关键规律是学习的平台期：进步不是线性的，而是波浪式上升。在平台期坚持的人终将突破。培养耐心的最高级方法是：让本能脑和情绪脑从困难事物中感受到乐趣。",
            "desc_en": "<strong>Patience comes not from willpower but from long-term vision.</strong> Growth weight comparison reveals: Change > Action > Thinking > Learning. Focusing only on learning quantity traps you in the 'more learning, more anxiety' cycle; focusing on real change frees you from ineffective diligence. Another key pattern is the learning plateau: progress is not linear but wave-like. Those who persist through plateaus eventually break through. The ultimate patience hack: make your instinctive and emotional brains enjoy difficult things.",
            "viz": "data", "viz_data": [
                ["\u2460 学习量", "表层·最易见", "读了多少书、学了多少小时"],
                ["\u2461 思考量", "中层·需要烧脑", "有没有关联、有没有提问"],
                ["\u2462 改变量", "底层·最难发生", "真正改变了什么行为或认知"],
            ]
        },
    ]
}

# ── ch002 ──
CH["002"] = {
    "zh_title": "第二章 潜意识——生命留给我们的彩蛋",
    "en_title": "The Subconscious \u2014 Life's Hidden Easter Egg",
    "zh_overview": '本章深入探讨潜意识。进化赋予人类意识分层\u2014\u2014潜意识负责生理系统，意识负责社会系统。但这也带来副作用：模糊。人生是一场消除模糊的比赛：认知模糊靠学习消除，情绪模糊靠正视化解，行动模糊靠清晰目标。更惊人的是，潜意识处理信息的速度是意识的275,000倍，顶级成长竟然是\u201c凭感觉\u201d\u2014\u2014让潜意识的感性帮你发现真正重要的事。',
    "en_overview": "This chapter dives into the subconscious. Evolution gave humans consciousness stratification \u2014 the subconscious handles physiology, consciousness handles social systems. But this brings a side effect: fuzziness. Life is a competition of eliminating fuzziness: cognitive fuzziness through learning, emotional fuzziness through confrontation, action fuzziness through clear goals. Even more striking: the subconscious processes information 275,000\u00d7 faster than consciousness. Top-level growth is 'going by feeling' \u2014 letting subconscious intuition help you discover what truly matters.",
    "kpi": [
        ["11,000,000<span class=\"kpi-unit\">次/秒</span>", "潜意识处理速度", "相当于最快个人计算机"],
        ["40<span class=\"kpi-unit\">次/秒</span>", "意识处理速度", "理性思考的运行上限"],
        ["275,000<span class=\"kpi-unit\">倍</span>", "潜意识vs意识差距", "火箭vs散步的速度对比"],
        ["3<span class=\"kpi-unit\">种模糊</span>", "需要消除的模糊", "认知·情绪·行动"],
    ],
    "en_kpi": [
        ["11M<span class=\"kpi-unit\"> ops/s</span>", "Subconscious Speed", "Equal to fastest computers"],
        ["40<span class=\"kpi-unit\"> ops/s</span>", "Conscious Speed", "Upper limit of rational thought"],
        ["275K<span class=\"kpi-unit\"> \u00d7</span>", "Speed Gap", "Rocket vs walking"],
        ["3<span class=\"kpi-unit\"> types</span>", "Fuzziness to Eliminate", "Cognitive\u00b7Emotional\u00b7Action"],
    ],
    "sections": [
        {
            "num": "01", "color": "01", "tag_zh": "人生本质", "tag_en": "Life's Essence",
            "title_zh": "模糊是困扰之源：人生是消除模糊的比赛",
            "title_en": "Fuzziness is the Root of Trouble: Life is a Race to Eliminate It",
            "desc_zh": "<strong>意识分层给人类带来巨大好处，但也带来了副作用\u2014\u2014模糊。</strong>潜意识能轻易左右意识，而意识很难介入潜意识。人们总是做着自己不理解的事：明明想去学习，转身却拿起手机。模糊让人心生迷茫和恐惧，继而影响人生的走向。谁的模糊越少，谁就越清醒；谁的模糊越严重，谁就越混沌。人生的比拼，本质上是消除模糊的速度和模式。",
            "desc_en": "<strong>Consciousness stratification brought huge benefits but also a side effect \u2014 fuzziness.</strong> The subconscious easily influences consciousness, but consciousness struggles to access the subconscious. People constantly do things they don't understand: wanting to study but reaching for the phone instead. Fuzziness breeds confusion and fear, which then shape life's trajectory. Those with less fuzziness live clearer; those with more live in chaos. Life's competition is essentially about the speed and pattern of eliminating fuzziness.",
            "viz": "flow", "viz_data": [
                "模糊严重<br>混沌迷茫", "", "主动消除模糊<br>认知·情绪·行动", "", "清晰明澈<br>人生自主"
            ]
        },
        {
            "num": "02", "color": "02", "tag_zh": "顶级能力", "tag_en": "Supreme Ability",
            "title_zh": "感性大于理性：潜意识的惊人力量",
            "title_en": "Intuition Over Reason: The Astonishing Power of Subconscious",
            "desc_zh": "<strong>潜意识处理信息速度11,000,000次/秒，意识仅40次/秒\u2014\u2014差距275,000倍。</strong>丘吉尔凭感觉换车门躲过炸弹、林肯凭感觉拒绝阁员，这都是潜意识捕捉到了意识无法察觉的信号。\u2018凭感觉\u2019之所以是顶级方法，是因为它能帮我们感知真正适合自己并需要的东西，让自己处于学习的\u2018拉伸区\u2019。感性在前选择，理性在后思考\u2014\u2014这才是高手的学习策略。",
            "desc_en": "<strong>Subconscious processes at 11,000,000 ops/s; consciousness at only 40 ops/s \u2014 a 275,000\u00d7 gap.</strong> Churchill changed car doors on instinct and dodged a bomb; Lincoln rejected a cabinet member on instinct. Both captured subconscious signals their conscious minds missed. 'Going by feeling' is the top method because it helps us sense what truly suits us, placing us in the stretch zone. Intuition selects first, reason analyzes second \u2014 that's the expert's learning strategy.",
            "viz": "dual", "viz_data": {
                "no_h": "\u274c 纯理性选择",
                "no_p": "向优等生看齐·选最难题目·追求完整框架·容易受挫放弃",
                "yes_h": "\u2705 凭感觉选择",
                "yes_p": "感知拉伸区·选略有难度·抓住触动点·最快进步见效"
            }
        },
        {
            "num": "03", "color": "03", "tag_zh": "学习方法", "tag_en": "Learning Method",
            "title_zh": "熔断读书法：不贪多，只取触动",
            "title_en": "Circuit-Breaker Reading: Don't Greed, Just Capture Sparks",
            "desc_zh": '<strong>成甲自创的\u201c熔断不读书法\u201d：读书时一旦看到有启发的内容，立刻停止。</strong>停下来做三件事：\u2460为什么刚才这个点让我有启发？\u2461我能够把这个启发点用在3个不同的事情上吗？\u2462这个启发点有没有其他类似的知识？好读书不如会读书。读完一本书只取最触动自己的那一个点，尽可能去实践、改变，收获比读完但停留在知道层面大得多。',
            "desc_en": "<strong>Cheng Jia's 'Circuit-Breaker Reading': when you encounter something inspiring, stop immediately.</strong> Then ask three questions: \u2460 Why did this point inspire me? \u2461 Can I apply this insight in 3 different contexts? \u2462 What similar knowledge connects to this? Being well-read is less important than reading well. Take just ONE most inspiring point from a book, practice and change \u2014 the yield far exceeds finishing the book while staying at the 'knowing' level.",
            "viz": "flow", "viz_data": [
                "读到启发点<br>立即停止", "", "问自己3个问题<br>为什么·用在哪·关联", "", "实践改变<br>真正内化"
            ]
        },
        {
            "num": "04", "color": "04", "tag_zh": "认知进化", "tag_en": "Cognitive Evolution",
            "title_zh": "消除认知模糊：学习的真正目的",
            "title_en": "Eliminating Cognitive Fuzziness: The True Purpose of Learning",
            "desc_zh": '<strong>学习知识的目的是消除模糊，获取知识的方法也是消除模糊\u2014\u2014目的与方法相统一。</strong>人类天生不喜欢学习和思考，因为耗能。但领域精英无不比其他人了解的更多，认知更清晰。\u201c学霸\u201d的秘诀在错题本上\u2014\u2014他们更愿意花时间明确错误、集中攻克。而普通学生重复已掌握的，对困难视而不见。差异不在勤奋程度，在努力模式：谁更愿意做高耗能的事\u2014\u2014消除模糊。',
            "desc_en": "<strong>The purpose of learning is to eliminate fuzziness, and the method to acquire knowledge is also to eliminate fuzziness \u2014 purpose and method are unified.</strong> Humans naturally dislike learning and thinking because they consume energy. Yet elites in every field simply know more and see more clearly. Top students' secret is their error notebook \u2014 they invest time clarifying mistakes and attacking them. Average students repeat what they already know, ignoring real difficulties. The difference isn't diligence but the pattern of effort: who's more willing to do high-energy tasks \u2014 eliminating fuzziness.",
            "viz": "dual", "viz_data": {
                "no_h": "\u274c 普通学习者",
                "no_p": "重复已掌握部分·对困难视而不见·模糊点越积越多·陷入低水平勤奋",
                "yes_h": "\u2705 高效学习者",
                "yes_p": "明确核心困难·集中精力攻克·消除模糊点·持续拓宽认知边界"
            }
        },
        {
            "num": "05", "color": "05", "tag_zh": "行动破局", "tag_en": "Action Breakthrough",
            "title_zh": "消除情绪与行动模糊：正视它，拆解它",
            "title_en": "Eliminate Emotional & Action Fuzziness: Face It, Break It Down",
            "desc_zh": '<strong>行动力不足的真正原因是选择模糊。</strong>当我们没有足够清晰的指令或目标时，就会本能选择享乐，放弃烧脑的选项。对策：把目标和过程细化、具体化，在诸多可能性中建立单行通道，让自己\u201c没得选\u201d。情绪模糊同样致命\u2014\u2014回避痛苦不会使其消失，反而使其转入潜意识，边界无限扩大。唯一的办法：正视它、看清它、拆解它、化解它。恐惧欺软怕硬，你正视它，它就原形毕露。',
            "desc_en": "<strong>The real cause of weak action is choice fuzziness.</strong> When we lack sufficiently clear instructions or goals, we instinctively choose pleasure over mentally demanding options. Solution: break goals and processes into concrete, specific steps \u2014 create a single-track path from many possibilities, leaving yourself 'no choice.' Emotional fuzziness is equally fatal \u2014 avoiding pain doesn't make it disappear; it pushes it into the subconscious where boundaries expand infinitely. The only way: face it, see it clearly, break it down, dissolve it. Fear bullies the timid; face it and it reveals its true form.",
            "viz": "flow", "viz_data": [
                "正视情绪<br>不回避不压抑", "", "拆解分析<br>向自己提问", "", "具体行动<br>建立单行通道"
            ]
        },
    ]
}

# ── ch003 ──
CH["003"] = {
    "zh_title": "第三章 元认知——人类的终极能能力",
    "en_title": "Metacognition \u2014 Humanity's Ultimate Ability",
    "zh_overview": '本章揭示人类终极能力\u2014\u2014元认知，即对思考的思考、对认知的认知。1959年第一张地球全景照让人类拥有了\u201c上帝之眼\u201d；元认知则让你拥有了对自我的\u201c上帝视角\u201d。元认知分被动与主动，主动开启者才能真正觉醒。在每一个选择的节点（元时间），审视第一反应、明确第二主张、做出更好选择\u2014\u2014这就是成为思维舵手的路径。',
    "en_overview": "This chapter reveals humanity's ultimate ability \u2014 metacognition: thinking about thinking, cognition of cognition. In 1959, the first full photo of Earth gave humans 'God's eye'; metacognition gives you 'God's view' of yourself. Metacognition comes in passive and active forms; only those who activate it proactively truly awaken. At every choice node ('meta-time'), examine your first reaction, clarify your second proposition, make a better choice \u2014 this is the path to becoming the helmsman of your own mind.",
    "kpi": [
        ["1959<span class=\"kpi-unit\">年</span>", "第一张地球全景照", "人类从此有了上帝之眼"],
        ["6<span class=\"kpi-unit\">个等级</span>", "元认知层级", "被动\u2192主动是觉醒转折点"],
        ["250<span class=\"kpi-unit\">万年</span>", "前额叶皮层进化", "元认知能力的生理基础"],
        ["40<span class=\"kpi-unit\">次/秒</span>", "意识运行速度", "vs潜意识11,000,000次/秒"],
    ],
    "en_kpi": [
        ["1959<span class=\"kpi-unit\"></span>", "First Earth Panorama", "'God's Eye' for humanity"],
        ["6<span class=\"kpi-unit\"> levels</span>", "Metacognition Tiers", "Passive\u2192Active = awakening"],
        ["2.5M<span class=\"kpi-unit\"> yrs</span>", "Prefrontal Cortex Age", "Biological basis of metacognition"],
        ["40<span class=\"kpi-unit\"> ops/s</span>", "Consciousness Speed", "vs subconscious 11M ops/s"],
    ],
    "sections": [
        {
            "num": "01", "color": "01", "tag_zh": "终极能力", "tag_en": "Ultimate Ability",
            "title_zh": "元认知=上帝视角：对思考的思考",
            "title_en": "Metacognition = God's View: Thinking About Thinking",
            "desc_zh": '<strong>1959年第一张地球全景照让人类拥有了\u201c上帝之眼\u201d。元认知就是你对自身的\u201c上帝视角\u201d\u2014\u2014对思考过程的思考，对认知过程的认知。</strong>其他动物不具备这种能力，与人类基因最接近的大猩猩也无法从自我和情境中脱离，假想出\u201c另一个自己\u201d。元认知正是人类成为\u201c万物之灵\u201d的根源。高级元认知能时刻帮你从高处、深处、远处看待现在的自己，保持清醒、不迷失。',
            "desc_en": "<strong>In 1959, the first full-Earth photo gave humanity 'God's eye.' Metacognition is your 'God's view' of yourself \u2014 thinking about your thinking process, cognition of your cognition.</strong> No other animal has this ability; even chimpanzees, our closest genetic relatives, cannot detach from self and context to imagine 'another self.' Metacognition is the root of humanity's unique position. Advanced metacognition lets you see yourself from above, below, and far away \u2014 staying clear and never lost.",
            "viz": "flow", "viz_data": [
                "普通认知<br>对事物思考", "", "元认知<br>对思考过程思考", "", "高级元认知<br>随时反观自身"
            ]
        },
        {
            "num": "02", "color": "02", "tag_zh": "觉醒关键", "tag_en": "Key to Awakening",
            "title_zh": "成长慢是因为你不会\u201c飞\u201d",
            "title_en": "Slow Growth Means You Can't 'Fly'",
            "desc_zh": '<strong>元认知能力弱的人像在地上爬，强的人像在天上飞。</strong>普通人只在遭遇指责、批评时才被动启用反思；处于顺境时依旧顺着本性生活。从被动到主动是一个转折点\u2014\u2014当一个人能主动开启第三视角、开始持续反观自己的思维和行为时，他就真正开始了觉醒，有了快速成长的可能。提升元认知的四条路径：学习前人智慧、反思自身经历、启用灵魂伴侣监控自己、冥想锻炼。',
            "desc_en": "<strong>Those with weak metacognition crawl on the ground; those with strong metacognition fly in the sky.</strong> Ordinary people only activate reflection when criticized; in good times they follow instinct. Moving from passive to active is the turning point \u2014 when someone proactively opens a third perspective and continuously reflects on their thoughts and actions, true awakening begins, and rapid growth becomes possible. Four paths to enhance metacognition: learn from predecessors' wisdom, reflect on personal experience, activate your 'soul companion' monitor, and practice meditation.",
            "viz": "dual", "viz_data": {
                "no_h": "\u274c 被动元认知",
                "no_p": "只在遭遇批评时反思·顺境随本性生活·缺乏自我觉察·困在原地打转",
                "yes_h": "\u2705 主动元认知",
                "yes_p": "主动开启第三视角·持续反观思维行为·时刻自我监控·实现快速成长"
            }
        },
        {
            "num": "03", "color": "03", "tag_zh": "决策节点", "tag_en": "Decision Node",
            "title_zh": "元时间的抉择：在每个选择节点想清楚",
            "title_en": "Meta-Time Decisions: Think Clearly at Every Choice Node",
            "desc_zh": '<strong>元时间=每个选择的节点。</strong>一天24小时看似一样，实则权重不同。一件事的起始、一天的开始与结束、面对诱惑或困难之时\u2014\u2014这些都是\u201c元时间\u201d。在元时间上想清楚，就能在接下来很长一段时间里做对。大多数人输在\u201c想都没想\u201d就行动了，被本能和潜意识直接接管了方向盘。焦虑的人很少有元时间意识，他们习惯不动脑子、直接行动。',
            "desc_en": "<strong>Meta-time = every choice node.</strong> 24 hours a day seem equal, but their weights differ greatly. The start of a task, the beginning or end of a day, moments of temptation or difficulty \u2014 these are all 'meta-time.' Thinking clearly at meta-time lets you do right for a long stretch afterward. Most people lose by acting 'without thinking,' letting instinct and subconscious take the wheel. Anxious people rarely have meta-time awareness; they habitually act without reflection.",
            "viz": "flow", "viz_data": [
                "选择节点<br>元时间到来", "", "停留几秒<br>审视第一反应", "", "想清楚再做<br>选择最优路径"
            ]
        },
        {
            "num": "04", "color": "04", "tag_zh": "思维舵手", "tag_en": "Mind Helmsman",
            "title_zh": "成为思维舵手的三步法",
            "title_en": "Three Steps to Becoming the Mind's Helmsman",
            "desc_zh": '<strong>三步成为思维舵手：\u2460审视第一反应</strong>\u2014\u2014本能冲动是什么？脱口而出的话、不假思索的行动都属于第一反应。<strong>\u2461明确第二主张</strong>\u2014\u2014理性应该怎么做？那一两秒的停顿就是理智脑的启动窗口，给出清晰明确的主张。<strong>\u2462做出更好选择</strong>\u2014\u2014选择第二主张而不是第一反应。这个零点几秒的间隔，就是教育和经历赋予你的意义。重复锻炼，理智脑自控力越来越强。',
            "desc_en": "<strong>Three steps to become the mind's helmsman: \u2460 Examine your first reaction</strong> \u2014 What's the instinctive impulse? Words that slip out, unthinking actions are all first reactions. <strong>\u2461 Clarify your second proposition</strong> \u2014 What should reason do? That one-second pause is the rational brain's activation window; produce a clear proposition. <strong>\u2462 Make the better choice</strong> \u2014 choose the second proposition over the first reaction. That split-second gap is the meaning your education and experience give you. With repeated practice, your rational brain's self-control grows stronger.",
            "viz": "data", "viz_data": [
                ["\u2460 审视第一反应", "停顿几秒", "不假思索的冲动是什么？本能想要什么？"],
                ["\u2461 明确第二主张", "理性介入", "更优的选择是什么？我应该怎么做？"],
                ["\u2462 做出更好选择", "主动控制", "选择第二主张，而非屈从第一反应"],
            ]
        },
        {
            "num": "05", "color": "05", "tag_zh": "顶级能力", "tag_en": "Supreme Skill",
            "title_zh": "反观自身是顶级能力：掌控命运的舵",
            "title_en": "Self-Reflection is Supreme: Steering Your Own Fate",
            "desc_zh": '<strong>元认知能力=自我审视+主动控制。</strong>人生若没有元认知，就像船没有舵，随波逐流。有了它，才可以掌控自己的命运。元认知能力强的人对模糊零容忍：无论如何要找出最重要的那个选项，让自己在一个时间段里只有一条路。\u201c想清楚\u201d这件事比什么都重要\u2014\u2014无论是当下的注意力、当天的日程，还是长远的人生目标，都应想清楚意义、自我审视、主动控制。高尔基说：每一次克制自己，就意味着比以前更强大。',
            "desc_en": "<strong>Metacognition = self-examination + active control.</strong> A life without metacognition is like a rudderless ship, drifting with the waves. With it, you can steer your own fate. People with strong metacognition have zero tolerance for fuzziness: they will find the single most important option, leaving themselves only one path per time period. 'Thinking clearly' matters more than anything \u2014 whether for immediate attention, daily schedule, or long-term life goals, clarify the meaning, self-examine, and actively control. Gorky said: every time you restrain yourself, you become stronger than before.",
            "viz": "flow", "viz_data": [
                "当下注意力<br>保持觉知", "", "全天日程<br>时刻清醒", "", "长远目标<br>想清意义"
            ]
        },
    ]
}

# ── ch004 ──
CH["004"] = {
    "zh_title": "第四章 专注力——情绪和智慧的交叉地带",
    "en_title": "Focus \u2014 Where Emotion and Intelligence Intersect",
    "zh_overview": '本章探讨专注力\u2014\u2014情绪和智慧的交叉地带。\u201c做A想B\u201d的身心分离模式是烦恼和无能的根源。一招提振注意力：让感受回归行动，吃饭就感受食物味道，走路就感受脚下触感。深度沉浸（心流）是进化双刃剑的安全剑柄\u2014\u2014天才=正确的方法+大量练习。正确方法四要素：明确目标、极度专注、有效反馈、在拉伸区练习。',
    "en_overview": "This chapter explores focus \u2014 the intersection of emotion and intelligence. The mind-body separation pattern of 'doing A while thinking B' is the root of anxiety and incompetence. One trick to boost attention: return feeling to action \u2014 taste food when eating, feel the ground when walking. Deep immersion (flow) is the safe handle of evolution's double-edged sword \u2014 genius = the right method + massive practice. The right method has four elements: clear goals, extreme focus, effective feedback, and practice in the stretch zone.",
    "kpi": [
        ["100<span class=\"kpi-unit\">%</span>", "极度专注的力量", "短时100% > 长时70%"],
        ["4<span class=\"kpi-unit\">要素</span>", "正确方法构成", "目标·专注·反馈·拉伸区"],
        ["2<span class=\"kpi-unit\">种模式</span>", "大脑工作模式", "意识专注+潜意识发散"],
        ["1<span class=\"kpi-unit\">个心法</span>", "提升注意力秘诀", "让感受回归行动"],
    ],
    "en_kpi": [
        ["100<span class=\"kpi-unit\">%</span>", "Extreme Focus Power", "Short 100% > Long 70%"],
        ["4<span class=\"kpi-unit\"> elements</span>", "Right Method", "Goal\u00b7Focus\u00b7Feedback\u00b7Stretch"],
        ["2<span class=\"kpi-unit\"> modes</span>", "Brain Work Modes", "Conscious focus + Subconscious diffuse"],
        ["1<span class=\"kpi-unit\"> trick</span>", "Attention Boost", "Return feeling to action"],
    ],
    "sections": [
        {
            "num": "01", "color": "01", "tag_zh": "烦恼之源", "tag_en": "Root of Distress",
            "title_zh": "\u201c做A想B\u201d：烦恼和无能的根源",
            "title_en": "'Doing A Thinking B': The Root of Anxiety and Incompetence",
            "desc_zh": '<strong>跑步时想工作、吃饭时想关系、睡觉时思绪如瀑\u2014\u2014\u201c做A想B\u201d是身心分离的典型表现。</strong>注意力分为\u201c集中在行动上的\u201d和\u201c集中在感受上的\u201d两部分。起初两者是统一的，但行动熟练后感受逐渐缺失，分心代替专注。缺少感受的行动如失去灵魂的躯壳，对情绪状态和能力提升产生持续负面影响。身心合一的片段组成幸福专注的高质量人生。',
            "desc_en": "<strong>Running while thinking about work, eating while worrying about relationships, sleeping while mind races like a waterfall \u2014 'doing A thinking B' is the classic sign of mind-body separation.</strong> Attention splits into 'action-focused' and 'feeling-focused' parts. Initially they're unified, but as actions become automatic, feeling fades \u2014 distraction replaces focus. Action without feeling is a soulless shell, continuously undermining emotional state and skill growth. Mind-body unity creates a high-quality life of happiness and focus.",
            "viz": "dual", "viz_data": {
                "no_h": "\u274c 身心分离（做A想B）",
                "no_p": "行动麻木·感受缺失·情绪焦虑·能力停滞·生命质量差",
                "yes_h": "\u2705 身心合一（做A即A）",
                "yes_p": "全情投入·感受敏锐·情绪平和·能力精进·幸福感强"
            }
        },
        {
            "num": "02", "color": "02", "tag_zh": "正念心法", "tag_en": "Mindfulness Hack",
            "title_zh": "一招提振注意力：让感受回归行动",
            "title_en": "One Trick to Boost Attention: Return Feeling to Action",
            "desc_zh": '<strong>吃饭就感受食物的味道，走路就感受脚下的触感\u2014\u2014把\u201c身体做着A脑子想着B\u201d变成\u201c身脑合一做A\u201d。</strong>身体感受是进入当下状态的最好媒介，感受事物消失的过程更是极好的专注力训练。得道前砍柴想挑水、挑水想做饭；得道后砍柴即砍柴、挑水即挑水、做饭即做饭。身心合一的要领不仅是专注于当下，更是享受当下。改变这个习惯等于改变底层行为模式。',
            "desc_en": "<strong>Taste food when eating, feel the ground when walking \u2014 transform 'body doing A, mind thinking B' into 'body and mind united doing A.'</strong> Physical sensation is the best medium to enter the present moment; feeling things fade is excellent focus training. Before enlightenment: chopping wood thinking of water, carrying water thinking of cooking. After: chopping wood is chopping wood, carrying water is carrying water, cooking is cooking. Mind-body unity isn't just about focusing on the present \u2014 it's about enjoying the present. Changing this habit changes your fundamental behavioral pattern.",
            "viz": "flow", "viz_data": [
                "吃饭<br>感受每一口味道", "", "走路<br>感受脚下每一步", "", "睡觉<br>感受身体松与紧"
            ]
        },
        {
            "num": "03", "color": "03", "tag_zh": "心流密码", "tag_en": "Flow Code",
            "title_zh": "深度沉浸=心流：进化双刃剑的安全剑柄",
            "title_en": "Deep Immersion = Flow: The Safe Handle of Evolution's Sword",
            "desc_zh": '<strong>深度沉浸（心流）是进化的双刃剑\u2014\u2014沉浸学习则强，沉浸享乐则废。</strong>能否进入深度沉浸是高手和普通人的最大区别。能力弱者极易分心，必须理想环境才能学习；能力强者能主动屏蔽干扰，在嘈杂处也能沉浸。前者处于被支配层，后者处于支配层。从人群中脱颖而出的金钥匙，就是刻意磨炼深度沉浸的品质。掌握它不一定靠热情，更是一项有方法论的\u201c技术\u201d。',
            "desc_en": "<strong>Deep immersion (flow) is evolution's double-edged sword \u2014 immerse in learning and you rise; immerse in pleasure and you fall.</strong> The ability to enter deep immersion is the biggest difference between experts and ordinary people. The weak are easily distracted, needing ideal environments to learn; the strong actively block interference, immersing even in noisy places. The former are in the dominated class; the latter in the dominating class. The golden key to standing out is deliberately honing deep immersion \u2014 not just through passion, but through a technical methodology.",
            "viz": "dual", "viz_data": {
                "no_h": "\u274c 沉浸能力弱者",
                "no_p": "极易分心·依赖理想环境·被风吹草动影响·处于被支配层",
                "yes_h": "\u2705 沉浸能力强者",
                "yes_p": "主动屏蔽干扰·任何环境可专注·主动选择信息·处于支配层"
            }
        },
        {
            "num": "04", "color": "04", "tag_zh": "天才公式", "tag_en": "Genius Formula",
            "title_zh": "天才=正确方法+大量练习",
            "title_en": "Genius = Right Method + Massive Practice",
            "desc_zh": '<strong>心理学家安德斯·艾利克森指出：天才的本质是\u201c正确的方法\u201d加上\u201c大量的练习\u201d。正确方法四要素：\u2460明确目标\u2014\u2014\u201c连续三次不犯错弹完\u201d而非\u201c练琴半小时\u201d；\u2461极度专注\u2014\u2014短时间100%精力>长时间70%；\u2462有效反馈\u2014\u2014教练指导、他人交流或自我反思，闭门造车必低效；\u2463在拉伸区练习\u2014\u2014太难受挫、太易停滞。缺一不可。</strong>',
            "desc_en": "<strong>Psychologist Anders Ericsson found: the essence of genius is 'the right method' plus 'massive practice.' The right method has four elements: \u2460 Clear goals \u2014 'play three times without error' not 'practice for 30 min'; \u2461 Extreme focus \u2014 short 100% > long 70%; \u2462 Effective feedback \u2014 coaching, peer exchange, or self-reflection; working in isolation guarantees inefficiency; \u2463 Stretch zone practice \u2014 too hard frustrates, too easy stagnates. All four are indispensable.</strong>",
            "viz": "data", "viz_data": [
                ["\u2460 明确目标", "定义越精确越好", "\u201c连续三次不出错\u201d vs \u201c练半小时\u201d"],
                ["\u2461 极度专注", "短时100%投入", "精力越集中感知越细微"],
                ["\u2462 有效反馈", "及时准确识别不足", "教练、交流或自我反思"],
            ]
        },
        {
            "num": "05", "color": "05", "tag_zh": "交叉地带", "tag_en": "Intersection Zone",
            "title_zh": "专注力=情绪+智慧的交叉地带",
            "title_en": "Focus = The Intersection of Emotion and Intelligence",
            "desc_zh": '<strong>专注力既是情绪问题（焦虑让人分心），也是智慧问题（方法不对则无效）。</strong>解决专注力，要从情绪和智慧两手抓。情绪端：让感受回归行动，身心合一；智慧端：掌握正确方法四要素，建立主动沉浸的行为模式。两脑协作的秘密：先极度专注（意识模式），再完全放下（潜意识发散模式），灵感自会浮现。阿基米德在澡盆里发现浮力定律\u2014\u2014正是专注后放松的结果。',
            "desc_en": "<strong>Focus is both an emotional issue (anxiety causes distraction) and an intellectual one (wrong methods are ineffective).</strong> Tackle focus from both ends. Emotion: return feeling to action, unite mind and body. Intelligence: master the four elements of the right method, establish active immersion patterns. The secret of two-brain collaboration: first extreme focus (conscious mode), then complete release (subconscious diffuse mode) \u2014 inspiration will surface. Archimedes discovered buoyancy in the bath \u2014 the result of relaxing after intense focus.",
            "viz": "flow", "viz_data": [
                "情绪端<br>感受回归·身心合一", "", "智慧端<br>四要素·正确方法", "", "深度沉浸<br>心流·灵感涌现"
            ]
        },
    ]
}

# ── Takeaways ──
takeaway_zh = {
    "001": '大脑的三重结构决定了人类天性中的目光短浅与即时满足。焦虑源于\u201c想同时做很多事，又想立即看到效果\u201d。真正的耐心不是靠意志力硬扛，而是通过认知复利曲线、舒适区边缘、成长权重对比等规律，用长远目光替代短视冲动。改变量>行动量>思考量>学习量\u2014\u2014盯着改变，才能跳出无效勤奋。',
    "002": '潜意识处理信息速度是意识的275,000倍。人生是一场消除模糊的比赛：认知模糊靠学习，情绪模糊靠正视，行动模糊靠清晰目标。\u201c凭感觉\u201d不是迷信，是让潜意识帮你发现真正重要的事。熔断读书法：读到一个有启发就停下来追问自己，只取一个触动点去实践。',
    "003": '元认知=对思考的思考，是人类终极能力。它让你有了对自我的\u201c上帝视角\u201d。在每个选择节点（元时间）想清楚：审视第一反应\u2192明确第二主张\u2192做出更好选择。成为思维舵手的三步法，本质上就是让理智脑在千钧一发之际掌握方向盘。',
    "004": '\u201c做A想B\u201d的身心分离是烦恼和无能的根源。一招提振注意力：让感受回归行动。深度沉浸（心流）是进化的安全剑柄\u2014\u2014天才=正确方法+大量练习。正确方法四要素：明确目标、极度专注、有效反馈、在拉伸区练习。专注力是情绪和智慧的交叉地带，两手都要抓。',
}

takeaway_en = {
    "001": "The brain's triune structure predisposes humans to short-sightedness and instant gratification. Anxiety comes from 'wanting to do everything at once while expecting immediate results.' True patience isn't willpower \u2014 it's long-term vision powered by understanding the compound interest curve, the edge of the comfort zone, and growth weight comparison. Change > Action > Thinking > Learning \u2014 focus on real change to escape ineffective diligence.",
    "002": "The subconscious processes information 275,000\u00d7 faster than consciousness. Life is a competition of eliminating fuzziness: cognitive through learning, emotional through confrontation, action through clear goals. 'Going by feeling' isn't superstition \u2014 it's letting your subconscious help you discover what truly matters. Circuit-breaker reading: pause at every spark and ask yourself questions; take just one insight to practice.",
    "003": "Metacognition = thinking about thinking \u2014 humanity's ultimate ability. It gives you a 'God's view' of yourself. At every choice node (meta-time), think clearly: examine first reaction \u2192 clarify second proposition \u2192 make better choice. The three-step helmsman method essentially lets your rational brain grab the steering wheel in critical moments.",
    "004": "'Doing A while thinking B' \u2014 mind-body separation \u2014 is the root of anxiety and incompetence. One trick to boost attention: return feeling to action. Deep immersion (flow) is evolution's safe handle \u2014 genius = right method + massive practice. The right method has four elements: clear goals, extreme focus, effective feedback, stretch-zone practice. Focus sits at the intersection of emotion and intelligence \u2014 tackle both ends.",
}


def make_file(ch_num, lang, ch_data):
    is_zh = (lang == "zh")

    if is_zh:
        h1 = f'\u8ba4\u77e5\u89c9\u9192 \u00b7 \u7b2c{int(ch_num)}\u7ae0\u300c{ch_data["zh_title"]}\u300d'
        subtitle_text = ch_data["zh_overview"]
        overview_text = ch_data["zh_overview"]
        back_text = "\u2190 \u8fd4\u56de\u7ae0\u8282\u76ee\u5f55"
        lang_btn_text = "\u4e2d\u6587 / English"
        catalog_href = "\u8ba4\u77e5\u89c9\u9192-catalog.html"
        other_href = f'\u8ba4\u77e5\u89c9\u9192-ch{ch_num}-info-en.html'
        footer_book = "\u300a\u8ba4\u77e5\u89c9\u9192\uff1a\u5f00\u542f\u81ea\u6211\u6539\u53d8\u7684\u539f\u52a8\u529b\u300b"
        kpi_data = ch_data["kpi"]
        subtitle_extra = '<span style="display:block;margin-bottom:6px;font-weight:bold;color:#dc2626;font-size:12px;letter-spacing:1px;">SCQA \u00b7 \u60c5\u5883 \u2192 \u51b2\u7a81 \u2192 \u95ee\u9898 \u2192 \u56de\u7b54</span>'
    else:
        h1 = f'Cognitive Awakening \u00b7 Ch.{int(ch_num)} "{ch_data["en_title"]}"'
        subtitle_text = ch_data["en_overview"]
        overview_text = ch_data["en_overview"]
        back_text = "\u2190 Back to Catalog"
        lang_btn_text = "English / \u4e2d\u6587"
        catalog_href = "\u8ba4\u77e5\u89c9\u9192-catalog.html"
        other_href = f'\u8ba4\u77e5\u89c9\u9192-ch{ch_num}-info-zh.html'
        footer_book = "Cognitive Awakening: The Driving Force of Self-Change"
        kpi_data = ch_data["en_kpi"]
        subtitle_extra = '<span style="display:block;margin-bottom:6px;font-weight:bold;color:#dc2626;font-size:12px;letter-spacing:1px;">SCQA \u00b7 Situation \u2192 Conflict \u2192 Question \u2192 Answer</span>'

    # Sections
    sections_html = ""
    for s in ch_data["sections"]:
        n = s["num"]
        c = s["color"]
        tag_text = s["tag_zh"] if is_zh else s["tag_en"]
        title_text = s["title_zh"] if is_zh else s["title_en"]
        desc_text = s["desc_zh"] if is_zh else s["desc_en"]
        viz_type = s["viz"]

        section_html = f'<!-- {n}: {title_text} -->\n'
        section_html += f'<div class="section section-{c}">\n'
        section_html += f'  <div class="section-num num-{c}">{n}</div>\n'
        section_html += f'  <div class="section-body">\n'
        section_html += f'    <div class="tag tag-{c}">{tag_text}</div>\n'
        section_html += f'    <div class="section-title t-{c}">{title_text}</div>\n'
        section_html += f'    <div class="section-desc">{desc_text}</div>\n'

        if viz_type == "flow":
            steps = s["viz_data"]
            section_html += '    <div class="flow-row">\n'
            for i, step in enumerate(steps):
                if step == "":
                    section_html += '      <div class="flow-arrow">\u2192</div>\n'
                elif i == len(steps) - 1:
                    section_html += f'      <div class="flow-step end">{step}</div>\n'
                else:
                    section_html += f'      <div class="flow-step">{step}</div>\n'
            section_html += '    </div>\n'

        elif viz_type == "dual":
            d = s["viz_data"]
            section_html += '    <div class="dual-grid">\n'
            section_html += f'      <div class="dual-card no">\n        <div class="dual-icon">\u26a0\ufe0f</div>\n        <div class="dual-text">\n          <h4>{d["no_h"]}</h4>\n          <p>{d["no_p"]}</p>\n        </div>\n      </div>\n'
            section_html += f'      <div class="dual-card yes">\n        <div class="dual-icon">\U0001f3c6</div>\n        <div class="dual-text">\n          <h4>{d["yes_h"]}</h4>\n          <p>{d["yes_p"]}</p>\n        </div>\n      </div>\n'
            section_html += '    </div>\n'

        elif viz_type == "data":
            items = s["viz_data"]
            section_html += '    <div class="data-row">\n'
            for i, item in enumerate(items):
                section_html += f'      <div class="data-card d{i+1}">\n        <div class="data-big">{item[0]}</div>\n        <div class="data-name">{item[1]}</div>\n        <div class="data-sm">{item[2]}</div>\n      </div>\n'
            section_html += '    </div>\n'

        section_html += '  </div>\n</div>\n'
        sections_html += section_html

    # KPI row
    kpi_html = ""
    for i, k in enumerate(kpi_data):
        ci = i + 1
        kpi_html += f'  <div class="kpi-card c0{ci}">\n'
        kpi_html += f'    <div class="kpi-value">{k[0]}</div>\n'
        kpi_html += f'    <div class="kpi-label">{k[1]}</div>\n'
        kpi_html += f'    <div class="kpi-note">{k[2]}</div>\n'
        kpi_html += '  </div>\n'

    tk = takeaway_zh[ch_num] if is_zh else takeaway_en[ch_num]
    tk_label = "\U0001f511 \u6838\u5fc3\u7ed3\u8bba" if is_zh else "\U0001f511 Key Takeaway"

    if is_zh:
        footer_text = f'{footer_book}\u7b2c{int(ch_num)}\u7ae0\u4fe1\u606f\u56fe \u00b7 \u57fa\u4e8e\u7b2c{int(ch_num)}\u7ae0\u5185\u5bb9\u63d0\u70bc \u00b7 \u4ec5\u4f9b\u5b66\u4e60\u53c2\u8003'
    else:
        footer_text = f'{footer_book} Ch.{int(ch_num)} Infographic \u00b7 Based on Chapter {int(ch_num)} \u00b7 For Learning Reference Only'

    html = f'''<!DOCTYPE html>
<html lang="{'zh-CN' if is_zh else 'en'}">
<head>
<meta charset="UTF-8">
<meta name="viewport" content="width=device-width, initial-scale=1.0">
<title>{h1}</title>
<style>
  @font-face {{
    font-family: 'FZXPYZS';
    src: url('../方正屏显雅宋简体.TTF') format('truetype');
    font-weight: normal; font-style: normal;
  }}
  * {{ margin: 0; padding: 0; box-sizing: border-box; }}
  body {{
    background: #f5f1eb;
    font-family: 'FZXPYZS', 'PingFang SC', 'Noto Serif SC', 'STSong', Georgia, serif;
    display: flex; justify-content: center; align-items: flex-start;
    min-height: 100vh; padding: 40px 20px 60px;
  }}
  .container {{ max-width: 880px; width: 100%; padding: 40px 32px 60px; }}

h1 {{
    font-family: 'FZXPYZS', 'PingFang SC', 'Noto Serif SC', serif;
    font-size: 36px; color: #1a1a1a; text-align: center;
    line-height: 1.4; margin-bottom: 8px; font-weight: normal;
    letter-spacing: 1.5px;
  }}
  .subtitle {{
    text-align: center; font-family: 'FZXPYZS', 'PingFang SC', 'Noto Serif SC', serif;
    font-size: 14px; color: #888; margin-bottom: 24px; line-height: 1.7;
    max-width: 640px; margin-left: auto; margin-right: auto;
  }}
  .divider {{
    width: 60px; height: 3px;
    background: linear-gradient(90deg, #dc2626, #ea580c);
    margin: 0 auto 28px; border-radius: 2px;
  }}

  .chapter-overview {{
    background: #f8f6f3; border-left: 3px solid #4f46e5; border-radius: 8px;
    padding: 16px 20px; margin: 12px 0 24px; font-size: 14px; color: #555;
    line-height: 1.8; font-family: 'FZXPYZS', 'PingFang SC', serif;
  }}
  .chapter-overview p {{ margin: 0; }}

  .section {{
    background: #ffffff; border-radius: 14px;
    margin-bottom: 18px; padding: 24px 28px;
    box-shadow: 0 1px 3px rgba(0,0,0,0.04);
    display: flex; gap: 20px; align-items: flex-start;
    border-left: 4px solid transparent;
  }}
  .section-01 {{ border-left-color: #dc2626; }}
  .section-02 {{ border-left-color: #ea580c; }}
  .section-03 {{ border-left-color: #ca8a04; }}
  .section-04 {{ border-left-color: #4f46e5; }}
  .section-05 {{ border-left-color: #db2777; }}

  .section-num {{
    flex-shrink: 0; width: 42px; height: 42px; border-radius: 50%;
    display: flex; align-items: center; justify-content: center;
    font-size: 17px; font-weight: bold; margin-top: 2px;
    font-family: 'FZXPYZS', 'PingFang SC', 'Noto Serif SC', serif;
  }}
  .num-01 {{ background: #fef2f2; color: #dc2626; }}
  .num-02 {{ background: #fff7ed; color: #ea580c; }}
  .num-03 {{ background: #fefce8; color: #ca8a04; }}
  .num-04 {{ background: #eef2ff; color: #4f46e5; }}
  .num-05 {{ background: #fdf2f8; color: #db2777; }}

  .section-body {{ flex: 1; }}
  .tag {{
    display: inline-block; font-size: 11px; font-weight: bold;
    padding: 2px 10px; border-radius: 10px; margin-bottom: 8px;
    letter-spacing: 1px; font-family: 'FZXPYZS', 'PingFang SC', 'Noto Serif SC', serif;
  }}
  .tag-01 {{ background: #fef2f2; color: #dc2626; }}
  .tag-02 {{ background: #fff7ed; color: #ea580c; }}
  .tag-03 {{ background: #fefce8; color: #ca8a04; }}
  .tag-04 {{ background: #eef2ff; color: #4f46e5; }}
  .tag-05 {{ background: #fdf2f8; color: #db2777; }}

  .section-title {{
    font-size: 18px; margin-bottom: 10px; font-weight: bold; line-height: 1.4;
    font-family: 'FZXPYZS', 'PingFang SC', 'Noto Serif SC', serif;
  }}
  .t-01 {{ color: #dc2626; }} .t-02 {{ color: #ea580c; }}
  .t-03 {{ color: #ca8a04; }} .t-04 {{ color: #4f46e5; }}
  .t-05 {{ color: #db2777; }}

  .section-desc {{
    font-size: 14px; color: #555; line-height: 1.9; margin-bottom: 14px;
  }}

  /* KPI */
  .kpi-row {{ display: grid; gap: 14px; margin: 0 0 18px; }}
  .kpi-row.cols-4 {{ grid-template-columns: repeat(4, 1fr); }}
  .kpi-row.cols-5 {{ grid-template-columns: repeat(5, 1fr); }}
  .kpi-card {{ border-radius: 12px; padding: 16px 14px; text-align: center; border: 1px solid; }}
  .kpi-card.c01 {{ background: #fef2f2; border-color: #fecaca; }}
  .kpi-card.c02 {{ background: #fff7ed; border-color: #fed7aa; }}
  .kpi-card.c03 {{ background: #fefce8; border-color: #fde68a; }}
  .kpi-card.c04 {{ background: #eef2ff; border-color: #c7d2fe; }}
  .kpi-card.c05 {{ background: #fdf2f8; border-color: #fbcfe8; }}
  .kpi-value {{ font-size: 34px; font-weight: bold; font-family: 'FZXPYZS', 'PingFang SC', 'Noto Serif SC', serif; color: #1a1a1a; line-height: 1.2; }}
  .kpi-unit {{ font-size: 13px; color: #888; font-weight: normal; }}
  .kpi-label {{ font-size: 12px; color: #666; margin-top: 6px; line-height: 1.4; font-family: 'FZXPYZS', 'PingFang SC', serif; }}
  .kpi-note {{ font-size: 11px; color: #aaa; margin-top: 3px; line-height: 1.4; }}

  /* Flow */
  .flow-row {{ display: flex; align-items: center; gap: 8px; flex-wrap: wrap; margin-top: 6px; }}
  .flow-step {{ background: #fff7ed; border: 1px solid #fed7aa; border-radius: 10px; padding: 10px 12px; text-align: center; min-width: 80px; flex: 1; font-size: 13px; color: #9a3412; line-height: 1.5; font-weight: bold; }}
  .flow-arrow {{ font-size: 20px; color: #ea580c; flex-shrink: 0; font-weight: bold; }}
  .flow-step.end {{ background: #fef2f2; border-color: #fecaca; color: #991b1b; }}

  /* Data row */
  .data-row {{ display: grid; grid-template-columns: 1fr 1fr 1fr; gap: 12px; margin-top: 10px; }}
  .data-card {{ border-radius: 12px; padding: 18px 16px; text-align: center; border: 1px solid #fce7f3; }}
  .data-card.d1 {{ background: #fdf2f8; border-color: #f9a8d4; }}
  .data-card.d2 {{ background: #fdf2f8; border-color: #f9a8d4; }}
  .data-card.d3 {{ background: #fdf2f8; border-color: #f9a8d4; }}
  .data-big {{ font-size: 26px; margin-bottom: 6px; }}
  .data-name {{ font-size: 15px; font-weight: bold; color: #831843; margin-bottom: 6px; font-family: 'FZXPYZS', 'PingFang SC', 'Noto Serif SC', serif; }}
  .data-sm {{ font-size: 12px; color: #9d174d; line-height: 1.6; }}

  /* Dual grid */
  .dual-grid {{ display: grid; grid-template-columns: 1fr 1fr; gap: 16px; margin-top: 10px; }}
  .dual-card {{ border-radius: 12px; padding: 18px 20px; display: flex; gap: 12px; align-items: flex-start; }}
  .dual-card.yes {{ background: #fef2f2; border: 1px solid #fecaca; }}
  .dual-card.no  {{ background: #f0fdf4; border: 1px solid #bbf7d0; }}
  .dual-icon {{ font-size: 24px; flex-shrink: 0; line-height: 1; }}
  .dual-text h4 {{ font-size: 14px; color: #1a1a1a; margin-bottom: 4px; font-family: 'FZXPYZS', 'PingFang SC', 'Noto Serif SC', serif; }}
  .dual-text p {{ font-size: 12px; color: #777; line-height: 1.6; }}

  /* Takeaway */
  .takeaway {{
    background: #ffffff; border: 1px solid #e8e0d5; border-radius: 14px;
    padding: 24px 32px; margin-bottom: 18px;
    box-shadow: 0 1px 3px rgba(0,0,0,0.04);
    border-left: 4px solid #dc2626;
  }}
  .takeaway-label {{ font-family: 'FZXPYZS', 'PingFang SC', 'Noto Serif SC', serif; font-size: 12px; color: #dc2626; letter-spacing: 2px; margin-bottom: 6px; font-weight: bold; }}
  .takeaway-text {{ font-size: 16px; color: #1a1a1a; line-height: 1.9; font-family: 'FZXPYZS', 'PingFang SC', 'Noto Serif SC', serif; }}

  /* Footer */
  .footer {{ text-align: center; margin-top: 32px; padding-top: 20px; border-top: 1px solid #e8e0d5; color: #bbb; font-size: 13px; line-height: 1.8; }}

  /* Lang */
  .lang-switch {{ text-align: right; margin-bottom: 16px; }}
  .lang-btn {{ display: inline-block; padding: 6px 16px; border-radius: 8px; font-size: 13px; text-decoration: none; letter-spacing: 0.03em; font-family: 'FZXPYZS', 'PingFang SC', 'Noto Serif SC', serif; background: #fef2f2; color: #dc2626; border: 1px solid #fecaca; transition: opacity 0.15s; }}
  .lang-btn:hover {{ opacity: 0.75; }}

  .back-catalog {{ text-align: right; margin-bottom: 4px; }}
  .back-catalog-btn {{ display: inline-block; padding: 5px 14px; border-radius: 8px; font-size: 12px; text-decoration: none; letter-spacing: .02em; background: #eef2ff; color: #4f46e5; border: 1px solid #c7d2fe; transition: opacity .15s; }}
  .back-catalog-btn:hover {{ opacity: .75; }}

  @media (max-width: 640px) {{
    .section {{ flex-direction: column; align-items: center; text-align: center; border-left: none; border-top: 4px solid transparent; padding-top: 20px; }}
    .section-01 {{ border-top-color: #dc2626; }} .section-02 {{ border-top-color: #ea580c; }}
    .section-03 {{ border-top-color: #ca8a04; }} .section-04 {{ border-top-color: #4f46e5; }}
    .section-05 {{ border-top-color: #db2777; }}
    .dual-grid, .data-row {{ grid-template-columns: 1fr; }}
    .flow-row {{ flex-direction: column; }}
    .flow-arrow {{ transform: rotate(90deg); }}
    .container {{ padding: 0 8px; }}
    h1 {{ font-size: 26px; }}
    .kpi-row.cols-4, .kpi-row.cols-5 {{ grid-template-columns: repeat(2, 1fr); }}
    .kpi-value {{ font-size: 34px; }}
  }}
  @media (max-width: 400px) {{
    .kpi-row.cols-4, .kpi-row.cols-5 {{ grid-template-columns: 1fr; }}
  }}
</style>
</head>
<body>
<div class="container">
<div class="back-catalog"><a class="back-catalog-btn" href="{catalog_href}">{back_text}</a></div>
<div class="lang-switch">
  <a class="lang-btn" target="_blank" href="{other_href}">{lang_btn_text}</a>
</div>

<h1>{h1}</h1>
<p class="subtitle">
  {subtitle_extra}
  {subtitle_text}
</p>
<div class="divider"></div>
<div class="chapter-overview">
  <p>{overview_text}</p>
</div>

<!-- KPI -->
<div class="kpi-row cols-4">
{kpi_html}</div>

{sections_html}
<div class="takeaway">
  <div class="takeaway-label">{tk_label}</div>
  <div class="takeaway-text">{tk}</div>
</div>

<div class="footer">
  {footer_text}
</div>
</div>
</body>
</html>'''
    return html


# Generate all 8 files
for ch in ["001", "002", "003", "004"]:
    for lang in ["zh", "en"]:
        filename = f"\u8ba4\u77e5\u89c9\u9192-ch{ch}-info-{lang}.html"
        filepath = os.path.join(outdir, filename)
        content = make_file(ch, lang, CH[ch])
        with open(filepath, 'w', encoding='utf-8') as f:
            f.write(content)
        size = os.path.getsize(filepath)
        print(f"\u2705 {filename} ({size:,} bytes)")

print("\nDone! All 8 files generated.")
