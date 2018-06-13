# -*- coding:utf-8 -*-
import qrcode

# 方法一
# 实例化对象并保存
img = qrcode.make("http://www.github.com")
img.save("test1.png")


# 方法二
# 实例化对象并编写详细参数
qr = qrcode.QRCode(
    version=1,
    error_correction=qrcode.constants.ERROR_CORRECT_L,
    box_size=10,
    border=4,
    )

# 添加二维码信息
qr.add_data("http://www.github.com")
qr.make(fit=True)

# 编译并保存二维码图片
img = qr.make_image()
img.save("./test2.png")