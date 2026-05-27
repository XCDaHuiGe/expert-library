# test_l3_economics.py

import re
from collections import Counter

topic = "资产泡沫 (Asset Bubbles)"

# Simulated speeches based on expert profiles
speeches = {
    "adam-smith": """
    诸位讨论的是市场的"泡沫"，但请不要忘记市场的本质——看不见的手。泡沫的形成，往往是因为政府这只看得见的手伸得太长了。
    当货币供应过剩，或者人为压低利率，资本就会被错误地引导到本不该去的地方。
    市场确实会犯错，就像人会犯错一样。但市场的纠错能力远超任何监管者。那些试图通过监管来防止泡沫的人，往往正是制造泡沫的人。
    让市场自己运行吧，尽管会有阵痛，但那是恢复健康的唯一途径。""",
    
    "charlie-munger": """
    沃伦，你说得对，但我得补充几点。泡沫的本质是什么？是人类的贪婪与嫉妒。人们看到邻居在股市里赚了钱，就忍不住也要冲进去。
    这种心理机制，进化心理学讲得很清楚——我们就是无法容忍别人比自己过得好。
    格雷厄姆说市场先生是个疯子，但我告诉你，市场先生还是个瘾君子。他每隔几年就要吸一口"非理性繁荣"的大麻。
    应对泡沫？只有一个字：忍。你必须建立一个心理模型网格，把心理学、经济学、历史学结合起来看问题。
    这种简单的常识，为什么大多数人做不到？因为他们太想赚快钱了。""",
    
    "john-maynard-keynes": """
    查理，你的心理学分析很精彩，但你忽略了结构性问题。市场长期来看可能是对的，但凯恩斯告诉我们，长期来看我们都死了。
    泡沫之所以危险，不是因为价格偏离价值，而是因为它会导致真实的投资失灵和失业。
    当泡沫破裂时，动物精神会从极度乐观转向极度悲观，这种信心的崩溃会导致流动性陷阱。
    这时候，只有政府出手干预——通过财政政策扩大支出，才能填补有效需求的不足。
    不要指望市场自我修复，那需要的时间太长，代价太大。我们必须现在就行动。""",
    
    "nassim-taleb": """
    约翰，你说的"政府干预"正是问题的根源！政府的干预让系统变得越来越脆弱。
    你们讨论的这些泡沫——2000年互联网泡沫、2008年次贷危机——都是典型的黑天鹅事件。你们在事后找原因，那是自欺欺人。
    真正的风险不是你们能看见的，而是那些看不见的尾部风险。
    传统的经济学家喜欢用正态分布来建模，但现实世界是肥尾分布。在这个世界里，极端事件发生的概率远比你们想象的高。
    不要去预测泡沫，那是徒劳的。你要做的，是建立反脆弱性——利用波动，而不是被波动摧毁。
    比如，你可以持有大量的现金和看跌期权，当黑天鹅来临时，你就能暴富。""",
    
    "ray-dalio": """
    纳西姆，你的反脆弱理论很有启发性，但你不能只靠防御来管理巨额资本。桥水基金之所以成功，是因为我们理解了经济机器的运行规律。
    资产泡沫，不过是债务周期的一部分。短期债务周期（5-8年）和长期债务周期（50-75年）的叠加，决定了泡沫何时破裂。
    当债务增长率超过收入增长率时，泡沫就在积累。这时候，我们需要"漂亮去杠杆"——既要债务重组，又要货币紧缩，还要适度的通货再膨胀。
    这是一门艺术，不是科学。历史已经无数次证明了这一点。""",
    
    "robert-shiller": """
    雷，你的周期理论很有解释力，但我更关心的是"故事"。泡沫的核心驱动力，是流行叙事。
    "房价永远不会跌"、"这次不一样"——这些叙事像病毒一样在社会中传播，扭曲了投资者的理性判断。
    我们用CAPE比率可以测量估值的偏离程度，但真正让泡沫膨胀的，是人们脑子里的故事。
    当大家都在讲同一个致富故事时，泡沫就在指数级膨胀。
    要治理泡沫，光靠调节货币是不够的，我们需要改变叙事环境。""",
    
    "warren-buffett": """
    罗伯特，你的叙事理论很有意思，但我是个生意人，我不关心那些宏观的东西。
    泡沫对我意味着什么？意味着好公司的股价变得便宜了。
    别人贪婪时我恐惧，别人恐惧时我贪婪——这不仅仅是一句口号，这是价值投资的核心。
    当市场先生恐慌性抛售时，那些拥有强大护城河的企业，其内在价值并没有改变。
    这时候，你只需要做一件事：买入。然后长期持有，让复利为你工作。
    至于泡沫什么时候破裂？我不知道，我也不需要知道。我只需要知道这家企业值多少钱。"""
}

print(f"L3 Simulation Test: {topic}\n")
print("-" * 60)

for expert, speech in speeches.items():
    print(f"Expert: {expert}")
    print(f"Speech:\n{speech.strip()}\n")
    print("-" * 60)

# Orthogonality Assessment
def get_ngrams(text, n=2):
    tokens = re.findall(r'[\u4e00-\u9fa5]|[a-zA-Z0-9]+', text)
    ngrams = []
    for i in range(len(tokens) - n + 1):
        ngrams.append("".join(tokens[i:i+n]))
    return ngrams

def cosine_similarity(v1, v2):
    intersection = set(v1.keys()) & set(v2.keys())
    numerator = sum([v1[x] * v2[x] for x in intersection])
    
    sum1 = sum([x**2 for x in v1.values()])
    sum2 = sum([x**2 for x in v2.values()])
    denominator = (sum1 ** 0.5) * (sum2 ** 0.5)
    
    if not denominator:
        return 0.0
    return float(numerator) / denominator

def evaluate_orthogonality(names, texts):
    print("\nOrthogonality Assessment (Cosine Similarity)")
    print("-" * 60)
    
    ngram_counts = [Counter(get_ngrams(text)) for text in texts]
    
    scores = []
    for i in range(len(names)):
        for j in range(i + 1, len(names)):
            sim = cosine_similarity(ngram_counts[i], ngram_counts[j])
            scores.append((names[i], names[j], sim))
            print(f"{names[i]} vs {names[j]}: {sim:.4f}")
            
    avg_sim = sum([s[2] for s in scores]) / len(scores)
    print("-" * 60)
    print(f"Average Similarity: {avg_sim:.4f} (Lower is more orthogonal)")
    return scores

evaluate_orthogonality(list(speeches.keys()), list(speeches.values()))
