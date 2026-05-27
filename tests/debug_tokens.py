import re
from collections import Counter

text1 = """
    人工智能不是人类的对手，而是人类的伙伴。我们正在创造一种新的心智，一种与人类智能完全不同的心智。
    AI的真正价值不在于它能做什么我们能做的事，而在于它能做什么我们做不到的事。  
    我们不应该问"AI会取代我们吗？"，而应该问"AI能让我们成为什么？"
    未来不属于AI，也不属于人类，而属于人机协作的超级有机体。
"""

text2 = """
    凯文，你太乐观了。超级智能的风险不在于它会"恨"我们，而在于它会"不在乎"我们。    
    当我们创造出一个比人类聪明千万倍的存在时，它的目标函数如果与人类的福祉哪怕有一点点偏差，后果都是灾难性的。
    这是一个工程问题，也是一个哲学问题。我们需要在创造出它之前，解决"价值对齐"问题。
    这不是科幻，这是人类面临的最大存在风险。
"""

def get_ngrams(text, n=2):
    # Simple character n-gram for Chinese, word for English
    tokens = re.findall(r'[\u4e00-\u9fa5]|[a-zA-Z0-9]+', text)
    ngrams = []
    for i in range(len(tokens) - n + 1):
        ngrams.append("".join(tokens[i:i+n]))
    return ngrams

ngrams1 = get_ngrams(text1)
ngrams2 = get_ngrams(text2)

print("Ngrams 1:", ngrams1[:10])
print("Ngrams 2:", ngrams2[:10])

c1 = Counter(ngrams1)
c2 = Counter(ngrams2)

intersection = set(c1.keys()) & set(c2.keys())
print("Intersection:", intersection)
