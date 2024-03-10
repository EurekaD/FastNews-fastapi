from transformers import PegasusForConditionalGeneration
# Need to download tokenizers_pegasus.py and other Python script from Fengshenbang-LM github repo in advance,
# or you can download tokenizers_pegasus.py and data_utils.py in https://huggingface.co/IDEA-CCNL/Randeng_Pegasus_523M/tree/main
# Strongly recommend you git clone the Fengshenbang-LM repo:
# 1. git clone https://github.com/IDEA-CCNL/Fengshenbang-LM
# 2. cd Fengshenbang-LM/fengshen/examples/pegasus/
# and then you will see the tokenizers_pegasus.py and data_utils.py which are needed by pegasus model
from tokenizers_pegasus import PegasusTokenizer

PATH = r"IDEA-CCNL/Randeng-Pegasus-523M-Summary-Chinese"

model = PegasusForConditionalGeneration.from_pretrained(PATH)
tokenizer = PegasusTokenizer.from_pretrained(PATH, use_fast=True)

texts = [
    "据台湾联合新闻网3月6日报道，仅南投集集镇就在一周内发生两起军人轻生案。据台军方通报，陆军兵工发展整备中心（兵整中心）武化翻修厂的一名潘姓下士于5日晚8时许失联。家人与军方报案后，警方通过定位系统于6日早上在兵整中心附近一路口旁发现潘的摩托车，随后在河边草地上找到他的尸体，颈部有明显刀伤。检方检验后称，现场并无他杀、外力介入致死嫌疑，确认为轻生案件。另一名家住南投集集的赵姓军人，上周五疑似为情所困，在集集拦河堰旁上吊。",
    "联合新闻网7日称，台军8天内已发生5起自伤案。除了上述两起外，据台媒2月29日报道，台陆军第六军团指挥部所属542旅联兵一营战车第一连黄姓下士在家附近的车内轻生。接着，蔡英文办公室一名卫兵于3月1日晚间执勤时持枪自戕，震惊岛内。3月2日台陆军航空第602旅的赵姓下士离家后未返家，当天晚上被发现陈尸在树林中。",
    "台“国防部长”邱国正7日在“立法院”承认，台军自伤人员确实在增加，“有的人抗压性比较弱”，但军方不会去怪当事人，发生这种事总是很遗憾，对家庭、部队来说都会带来创伤。他以蔡英文办公室宪兵自戕案举例称，军方第一时间从官兵身心健康、职务派遣有无违反规定等方面展开调查。按规定卫兵执勤2小时要歇6小时，该单位并没有违规。但岛内普遍认为，自伤案增加与台军士兵任务过重、压力过大有关。国民党“立委”徐巧芯7日说，据传自戕士兵已3天3夜没睡觉，但台军方却说“都很好”。"
]


def sum_text(texts):
    for text in texts:
        inputs = tokenizer(text, max_length=1024, return_tensors="pt ")
        # Generate Summary
        summary_ids = model.generate(inputs["input_ids"])
        sen = tokenizer.batch_decode(summary_ids, skip_special_tokens=True, clean_up_tokenization_spaces=False)[0]
        print(sen)


sum_text(texts)
