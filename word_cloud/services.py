
import random
import matplotlib
from wordcloud import WordCloud
from collections import Counter
import jieba
from utils.image_encoder import pil_to_bytes

matplotlib.use('TkAgg')

# font_path = "C:\Windows\Fonts\simsun.ttc"
font_path = r"FastNews-fastapi\res\simsun.ttc"


# 偏蓝色色系函数
def blue_color_func(word, font_size, position, orientation, random_state, **kwargs):
    blue_colors = ['#66c2ff', '#3399ff', '#0066cc', '#003366', '#99ccff']
    return random.choice(blue_colors)


class WordCloudService:

    @staticmethod
    async def word_cloud(new_text):
        new_text = jieba.cut(new_text)

        # 初始化词频统计
        word_counts = Counter()

        word_counts.update([word for word in new_text if len(word) > 1])

        word_counts_filtered = {word: count for word, count in word_counts.items() if count >= 2}

        wordcloud_img = WordCloud(font_path=font_path, background_color='white', color_func=blue_color_func, scale=3, prefer_horizontal=1)\
            .generate_from_frequencies(word_counts_filtered)

        image = wordcloud_img.to_image()

        image.save("test.png")

        return pil_to_bytes(image)

if __name__ == "__main__":
    text = "摘要指摘录文献内容的要点，提供内容梗概的。摘要有助于节省读者阅读时间，快速了解原文的主要内容。它是一篇完整的短文，重点在于原文的结论，不需要添加详细的解释。"  \
            "在当下这个信息爆炸的时代，文字，图片，视频等信息的载体多种多样，各种信息充斥着我们的生活。新闻依然是重要的一种信息载体，新闻摘要通过对新闻的要点、关键事件的简要概括，新闻摘要通常包含了新闻事件的背景、主要参与者、关键冲突或事件经过、以及可能的影响或后续发展。这样的摘要有助于读者迅速抓住新闻的要点，对于快速获取信息非常有用。" \
            "本课题的研究目标在于通过训练基于transformer架构的摘要模型，生成较高质量的摘要。目前，大多数面向中文的模型都沿用英文模型的分词嵌入方式，尤其是能够建模汉语这种特殊语言特性的模型，相比之下，较为缺乏。" \
            "本课题使用ChineseBERT 模型中提出的将中文字形和拼音信息融入模型的方法，以此增强模型对中文语料的建模能力。系统使用当前先进的技术架构 fastapi与vue3 完成前后端设计，数据库使用mysql。"
    text1 = "山煤国际主要有煤炭生产和煤炭贸易两大类业务，报告期内，公司自产煤的产量为3898.37万吨，销量为3485.99万吨，库存量为34.28万吨。分产品来看，山煤国际的动力煤实现营业收入13.52亿元，同比下滑16.28%，毛利率同比减少4.5个百分点；冶金煤的收入为10.27亿元，同比下降27.13%，毛利率大幅下降12.12个百分点。 年报显示，山煤国际拟向全体股东派发每股现金股利0.65元（含税），合计拟派发现金红利12.89亿元（含税），占2023年归母净利润的30.25%，以3月29日股价计算，股息率3.79%，股息率与分红总额均为近三年最低。据公司《2024年-2026年股东回报规划》，规划期内各年度以现金方式分配的利润不少于当年实现的可供分配利润的60%。 止损光伏项目后，业绩全看煤炭产销 光伏高速发展的当下，早在2019年山煤国际提出要做光伏电池。2020年8月，公司对外设立合资公司拟开展HJT电池产业化一期3GW项目，当年9月合资公司注册成立，并完成了项目单位建设环评工作，以及一号车间及动力、仓储等配套设施的桩基处理等阶段性工作，但项目主体未进行大规模投入。 近三年光伏产业发展节奏或许出乎山煤国际的预料，一方面硅料价格呈“过山车”走势，对产业链利润格局形成重大影响，另一方面，电池的技术路径百花齐放，TOPCon技术一马当先，成为当前较主流的电池技术路径，头部厂商均在积极扩产，而光电转换效率最高的HJT受制于成本问题，迟迟无法大规模上量。 山煤国际在年报中表示，光伏电池项目立项后，受全球公共卫生事件、所在区域光伏产业链条不完备、光伏产业迭代更新速度快、技术人才支撑不足等多重因素影响，基于光伏行业环境变化，综合考虑各方面因素后，公司认为继续推进该项目将会面临较大投资风险，决定终止实施HJT电池产业化一期3GW项目。 光伏项目及时止损后，山煤国际的煤炭产销恢复情况，决定了公司业绩表现。供给层面来看，2023年国内原煤产量47.1亿吨，同比增长3.4%，煤炭进口4.7亿吨，创历史新高，同比增长61.8%，进口规模增长主要系海内外煤炭价格差扩大、进口煤零关税政策延续、蒙古国煤炭进口通关恢复以及澳大利亚煤炭进口等多重因素。"
    image = WordCloudService.word_cloud(text1)
    image.save('saved_image.png')
