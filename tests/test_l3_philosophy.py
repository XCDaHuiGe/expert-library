# test_l3_philosophy.py

import re
from collections import Counter

topic = "孤独 (Solitude)"

# Simulated speeches based on expert profiles
speeches = {
    "albert-camus": """
    孤独？你把它看作一种疾病，一种需要治愈的状态。但我告诉你，世界本身就是荒诞的，人与人之间的隔阂是不可逾越的。
    西西弗斯推石上山，他孤独吗？他在那一刻是世界上最充实的人，因为他直面了自己的命运。
    不要试图逃避孤独，那是逃避你自己的存在。真正的反抗，是在孤独中保持清醒，在沉默中寻找自己的声音。
    你问我如何克服孤独？别克服它。拥抱它。就像拥抱一个不爱你的情人。""",
    
    "friedrich-nietzsche": """
    孤独是超人的试炼场！庸人害怕孤独，他们成群结队，像羊群一样寻求安全感。
    查拉图斯特拉下山，因为他太孤独了——他需要把他的智慧赠予人类，即使人类不配。
    你的孤独不是软弱，而是力量的积蓄。只有在孤独中，你才能听到自己内心的声音——那个被“道德”和“社会”压抑的声音。
    不要寻求同伴，要寻求对手！只有在与强者的交锋中，你才能超越自己。
    你说你孤独？好极了！这意味着你还没有被平庸同化。""",
    
    "arthur-schopenhauer": """
    孤独是人类注定的命运。欲望是痛苦的根源，而人与人之间的交往，不过是欲望的相互碰撞。
    你以为社交能带来快乐？那只是暂时的麻醉。钟摆摆动，从痛苦摆向无聊，而孤独，正是无聊的极致。
    但孤独也是智慧的起点。只有在孤独中，你才能摆脱意志的奴役，进入审美的静观。
    不要试图在人群中寻找解脱，那只会让你陷入更深的痛苦。学会独处，学会在艺术和哲学中寻找慰藉。
    记住，要么孤独，要么庸俗。""",
    
    "jean-paul-sartre": """
    你说你感到孤独？让我问你：你是在“感到”孤独，还是在“选择”孤独？
    你说你无法与人沟通，他人即地狱——但这不是逃避责任的借口。你选择用“孤独”来定义自己，这是一种自欺。
    存在先于本质。没有所谓的“孤独的本质”，只有你正在经历的存在。你不是“孤独的人”，你是“正在选择孤独的人”。
    他人不是地狱，他人是镜子。在与他人的对视中，你看到了自己的自由——以及自由的重负。
    不要躲在孤独的标签下。承认你的自由，承担你的责任。现在，你打算怎么做？"""
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
