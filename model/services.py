import re
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

    async def predict(self, text):
        inputs = self.tokenizer(text, max_length=1024, return_tensors="pt")
        summary_ids = self.model.generate(inputs["input_ids"])
        sen = self.tokenizer.batch_decode(summary_ids, skip_special_tokens=True, clean_up_tokenization_spaces=False)[0]
        print(sen)
        return sen

    # predict after paragraphing the news text
    async def predict_paragraphing(self, text):
        text_list = re.split("\n", text)
        result = []
        for paragraph in text_list:
            sen = await self.predict(paragraph)
            result.append(sen)
        return "\n".join(result)


def get_model() -> Summarization:
    return Summarization()

# if __name__ == "__main__":
#     # model_0 = get_model()
#     # model_1 = get_model()
#     # print(id(model_0))
#     # print(id(model_1))


