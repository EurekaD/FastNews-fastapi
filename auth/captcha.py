
# 验证码流程如下：
# 1. 前端发送get请求来获取验证码图片。需要前端生成uuid并把uuid的值传到后端；
# 2. 后端收到前端的生成验证码请求，生成验证码图片和验证码内容。然后将前端传递过来的uuid值作为键，验证码内容作为值，形成一对键值对，存储在Redis中。同时根据需求设置验证码的有效期。
# 3. 前端获取到验证码，等待用户输入验证码之后进行提交请求。提交请求中包含用户输入的验证码以及刚才生成的uuid。
# 4. 后端拿到uuid以及用户输入的验证码内容。根据uuid取出Redis中保存的值，如果值为空，那么说明验证码已经过期；
#    如果值不为空，取出值和前端传过来的用户输入的验证码内容进行比价，如果相等，那么就验证码输入正确，否则验证输入错误，将结果返回给前端。
# 5. 前端收到后的响应，如果验证码正确，则显示提交成功，否则重新请求后端生成验证码，然后重复上述步骤。


class Captcha:
    def __init__(self):
        self.CAPTCHA = []
        self.CAPTCHA_length = 0

    def append(self, uuid, text):
        self.CAPTCHA_length += 1
        self.CAPTCHA.append({uuid: text})
        print({uuid: text})
        if self.CAPTCHA_length >= 100:
            self.CAPTCHA.pop(0)
            self.CAPTCHA_length -= 1

    def verify(self, uuid_, text_):
        for captcha in self.CAPTCHA:
            if uuid_ in captcha:
                print(captcha[uuid_])
                if text_.lower() == captcha[uuid_].lower():
                    return True
        else:
            return False


if __name__ == "__main__":
    cap = Captcha()
    cap.append("111111", "adfddsf")
    print(cap.verify("11111", "adfddsf"))