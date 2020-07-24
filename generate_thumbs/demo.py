import os
import json
import sys

from PIL import Image

Image.MAX_IMAGE_PIXELS = None

def generate_conf(dir):
    dic = {
        'dir': dir,
        'result': {}
    }
    for file in os.listdir(dir):
        ext = os.path.splitext(file)[1]
        if ext not in ['.jpg', '.png', '.jpeg', '.bmp']:
            continue
        dic.get('result')[file] = ''
    with open('./demo.conf', 'w') as f:
        f.write(json.dumps(dic))
    print('>>>请在 demo.conf 中完成图片大小配置')
    res = input('>>>配置完成请输入1:')
    return res

def resize_image():
    with open('./demo.conf', 'r') as f:
        conf = json.loads(f.readlines()[0])
        dir = conf.get('dir')
        result = conf.get('result')
        for key, value in result.items():
            image_full_path = os.path.join(dir, key)

            if not value:
                raise '{0} 大小配置为空，请修改后重试'
            if 'x' not in value:
                raise '{0} 格式配置有误，正确格式为 "width x height" 请修改后重试'

            size = int(value.split('x')[0].split(' ')), int(value.split('x')[1].split(' '))
            im = Image.open(image_full_path)
            im.thumbnail(size)
            save_image_dir = os.path.join(dir, 'thumb')

            if not os.path.exists(dir):
                os.makedirs(dir)

            save_image_path = os.path.join(save_image_dir, key)
            im.save(save_image_path)
    print('>>>', '图片生成缩略图完成，请到{0}文件夹中查看'.format(save_image_dir))

if __name__ == "__main__":
    args = sys.argv
    if len(args) < 2:
        raise '请输入有效的图片文件夹地址'
    dir = args[1]
    res = generate_conf(dir)

    flag = True
    while flag:
        if res and int(res) == 1:
            resize_image()
            flag = False
        else:
            res = input('>>>你输入的值有误，请重新输入。配置完成请输入1：')
