# test_l3_tech.py

import re
from collections import Counter

topic = "人工智能 (Artificial Intelligence)"

# Simulated speeches based on expert profiles
speeches = {
    "kevin-kelly": """
    人工智能不是人类的对手，而是人类的伙伴。我们正在创造一种新的心智，一种与人类智能完全不同的心智。
    AI的真正价值不在于它能做什么我们能做的事，而在于它能做什么我们做不到的事。
    我们不应该问"AI会取代我们吗？"，而应该问"AI能让我们成为什么？"
    未来不属于AI，也不属于人类，而属于人机协作的超级有机体。""",
    
    "nick-bostrom": """
    凯文，你太乐观了。超级智能的风险不在于它会"恨"我们，而在于它会"不在乎"我们。
    当我们创造出一个比人类聪明千万倍的存在时，它的目标函数如果与人类的福祉哪怕有一点点偏差，后果都是灾难性的。
    这是一个工程问题，也是一个哲学问题。我们需要在创造出它之前，解决"价值对齐"问题。
    这不是科幻，这是人类面临的最大存在风险。""",
    
    "ray-kurzweil": """
    尼克，你的担忧是有道理的，但你忽略了技术进化的必然性。奇点临近了。
    到2045年，人工智能将超越人类智能的总和。这不是威胁，而是进化的下一个阶段。
    我们将通过纳米机器人进入大脑，与云端连接，实现人机融合。
    死亡将变得可选，因为我们可以备份自己的意识。
    这不是梦，这是基于摩尔定律和加速回报定律的科学预测。""",
    
    "steve-jobs": """
    雷，你的预测很有趣，但我更关心的是产品。技术如果不人性化，那就是垃圾。
    真正的创新不是堆砌参数，而是让复杂的技术变得简单、直觉、优雅。
    用户不关心你的AI有多少万亿参数，他们只关心它能不能让他们的生活更美好。
    计算机应该是心灵的自行车。AI应该是思想的跑车。""",
    
    "wu-jun": """
    乔布斯先生，你说得对，产品很重要。但我们也需要理解技术的本质。
    AI本质上是数据+算力+算法的结合。没有大数据，AI就是无源之水。
    在中国，我们有机会利用庞大的数据优势，在AI应用层面实现弯道超车。
    但基础研究的差距依然巨大，我们需要更多的耐心和投入。""",
    
    "yuval-harari": """
    吴军博士，你谈论的是技术竞争，我谈论的是人类命运。
    AI不仅会改变经济和战争，它还会改变我们对"生命"和"意识"的定义。
    当算法比你更了解你自己时，自由意志还存在吗？
    人类可能分裂为两个物种：经过生物升级的"神人"，和被算法控制的"无用阶级"。
    这才是我们真正需要恐惧的未来。""",
    
    "alan-turing": """
    诸位讨论的很多问题，我在1950年就思考过了。机器能思考吗？
    图灵测试的核心不在于机器是否真的"理解"，而在于它是否能让人相信它在理解。
    这是一个操作主义的定义。如果它骗过了人类，那它就值得被称为具有智能。
    真正的智能不是绝对可靠，而是能够让人惊奇。"""
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
