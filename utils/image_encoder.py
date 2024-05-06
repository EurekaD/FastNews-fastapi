import base64
import io

from PIL import Image


def pil_to_bytes(image: Image):

    # 将 PIL Image 转换为字节流
    image_byte_array = io.BytesIO()
    image.save(image_byte_array, format="PNG")

    # 获取字节流的二进制数据
    image_data = image_byte_array.getvalue()

    # 将二进制数据进行 Base64 编码
    base64_encoded_image = base64.b64encode(image_data).decode("utf-8")

    return base64_encoded_image
