from transformers import PegasusForConditionalGeneration
from tokenizers_pegasus import PegasusTokenizer
import torch

if __name__ == "__main__":
    print(torch.__version__)

    device = torch.device('cuda' if torch.cuda.is_available() else 'cpu')
    print(f"Using device {device}")

    # model = torch.load("pytorch_model.bin")
    # model = PegasusForConditionalGeneration("config.json")
    # model.load_state_dict(torch.load("pytorch_model.bin"))
    tokenizer = PegasusTokenizer.from_pretrained("vocab.txt", use_fast=True)

    model = PegasusForConditionalGeneration.from_pretrained("IDEA-CCNL/Randeng-Pegasus-523M-Summary-Chinese")
    tokenizer = PegasusTokenizer.from_pretrained("IDEA-CCNL/Randeng-Pegasus-523M-Summary-Chinese", use_fast=True)


    text = "记者2月23日从教育部获悉，教育部近日公布了中小学人工智能教育基地名单，184所学校入选。本次中小学人工智能教育基地推荐旨在通过基地试点，" \
           "进一步探索人工智能教育的新理念、新模式和新方案，形成可推广的优秀案例和先进经验，推动中小学人工智能教育深入开展。教育部表示，将加强对基地工作的指导，" \
           "促进各基地更加重视人工智能教育，积极探索人工智能教育实施方式，以中小学信息科技、通用技术等课程为主要依托，进一步丰富教育教学资源，创新教与学支持服务方式，" \
           "开展师资培训指导，扩大人工智能教育覆盖面和受益面，在人工智能校本课程建设、学科融合、教学方式变革、数字教育资源共建共享、教师数字素养培育、" \
           "学生全面发展等方面发挥示范引领作用，带动区域人工智能教师专业化水平不断提升。教育部还将选取典型经验、优秀课例、优质资源在国家中小学智慧教育平台上线，" \
           "推动更多中小学校探索开展人工智能教育。（记者杨湛菲）"

    inputs = tokenizer(text, max_length=1024, return_tensors="pt")
    summary_ids = model.generate(inputs["input_ids"])
    sen = tokenizer.batch_decode(summary_ids, skip_special_tokens=True, clean_up_tokenization_spaces=False)[0]
    print(sen)

# pip install torch==1.10.0 torchvision==0.11.1 torchaudio==0.10.0+cu113 -f https://download.pytorch.org/whl/cu113/torch_stable.html
