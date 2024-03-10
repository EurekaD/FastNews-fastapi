from utils.decorators import singleton
from transformers import PegasusForConditionalGeneration

from model.pegasus.tokenizers_pegasus import PegasusTokenizer


PATH = r"E:\workspace\graduation-project\FastNews-fastapi\model\pegasus\IDEA-CCNL\Randeng-Pegasus-523M-Summary-Chinese"


# 单例模式的 摘要服务 依赖
@singleton
class Summarization:
    def __init__(self):
        self.model = PegasusForConditionalGeneration.from_pretrained(PATH)
        self.tokenizer = PegasusTokenizer.from_pretrained(PATH, use_fast=True)

    def predict(self, text):
        inputs = self.tokenizer(text, max_length=1024, return_tensors="pt")
        summary_ids = self.model.generate(inputs["input_ids"])
        sen = self.tokenizer.batch_decode(summary_ids, skip_special_tokens=True, clean_up_tokenization_spaces=False)[0]
        return sen


def get_model() -> Summarization:
    return Summarization()

