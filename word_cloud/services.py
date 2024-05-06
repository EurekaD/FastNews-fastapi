
import random
import matplotlib
from wordcloud import WordCloud
from collections import Counter
import jieba

matplotlib.use('TkAgg')

# font_path = "C:\Windows\Fonts\simsun.ttc"
font_path = r"FastNews-fastapi\res\simsun.ttc"


# 偏蓝色色系函数
def blue_color_func(word, font_size, position, orientation, random_state, **kwargs):
    blue_colors = ['#66c2ff', '#3399ff', '#0066cc', '#003366', '#99ccff']
    return random.choice(blue_colors)


class WordCloudService:

    @staticmethod
    def word_cloud(new_text):
        new_text = jieba.cut(new_text)

        # 初始化词频统计
        word_counts = Counter()

        word_counts.update([word for word in new_text if len(word) > 1])

        word_counts_filtered = {word: count for word, count in word_counts.items() if count >= 2}

        wordcloud_img = WordCloud(font_path=font_path, background_color='white', color_func=blue_color_func, scale=3, prefer_horizontal=1)\
            .generate_from_frequencies(word_counts_filtered)

        return wordcloud_img.to_image()

if __name__ == "__main__":
    text = "摘要指摘录文献内容的要点，提供内容梗概的。摘要有助于节省读者阅读时间，快速了解原文的主要内容。它是一篇完整的短文，重点在于原文的结论，不需要添加详细的解释。"  \
            "在当下这个信息爆炸的时代，文字，图片，视频等信息的载体多种多样，各种信息充斥着我们的生活。新闻依然是重要的一种信息载体，新闻摘要通过对新闻的要点、关键事件的简要概括，新闻摘要通常包含了新闻事件的背景、主要参与者、关键冲突或事件经过、以及可能的影响或后续发展。这样的摘要有助于读者迅速抓住新闻的要点，对于快速获取信息非常有用。" \
            "本课题的研究目标在于通过训练基于transformer架构的摘要模型，生成较高质量的摘要。目前，大多数面向中文的模型都沿用英文模型的分词嵌入方式，尤其是能够建模汉语这种特殊语言特性的模型，相比之下，较为缺乏。" \
            "本课题使用ChineseBERT 模型中提出的将中文字形和拼音信息融入模型的方法，以此增强模型对中文语料的建模能力。系统使用当前先进的技术架构 fastapi与vue3 完成前后端设计，数据库使用mysql。"
    image = WordCloudService.word_cloud(text)
    image.save('saved_image.png')
