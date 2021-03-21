from typing import Optional, Union, Any
from typing import Callable, NoReturn
from typing import Sequence, Iterable, List, Tuple
from typing import Dict
from typing import TypeVar, Generic, NewType, Type
from typing import IO, TextIO, BinaryIO

import click
from PIL import Image, ImageDraw, ImageFont
from lgtm.image_source import get_image

OUTPUT_NAME = 'output.jpg'
OUTPUT_FORMAT = 'JPEG'
# 画像に対するテキストの描画領域の割合
MAX_RATIO = 0.8

#フォントの格納先のパスは実行環境に合わせて変更する
# FONT_NAME = '/Library/Fonts/Charter.ttc'
# FONT_NAME = '/Library/Fonts/Times New Roman.ttf'
FONT_NAME = '/usr/local/share/fonts/TakaoMincho.ttf'
# テキストの色
FONT_COLOR_WHITE = (0, 0, 0, 0)
# フォントの最大サイズと最小サイズ
FONT_MAX_SIZE = 256
FONT_MIN_SIZE = 12

def save_with_message(fp: BinaryIO, message: str) -> None:
    """画像にテキストを描画しファイルに書き出す。
    Args:
        fp (BinaryIO): 画像のファイルオブジェクト
        message (str): 画像に描画するテキスト
    """
    img = Image.open(fp)
    draw = ImageDraw.Draw(img)
    image_width, image_height = img.size
    message_area_width, message_area_height = (
        image_width * MAX_RATIO,
        image_height * MAX_RATIO
    )

    for font_size in range(FONT_MAX_SIZE, FONT_MIN_SIZE, -1):
        font = ImageFont.truetype(FONT_NAME, font_size)
        text_width, text_height = draw.textsize(message, font=font)
        w, h = (
            message_area_width - text_width,
            message_area_height - text_height
        )
        if w > 0 and h > 0:
            position = (
                (image_width - message_area_width) / 2,
                (image_height - message_area_height) / 2,
            )
            draw.text(position, message, font=font, fill=FONT_COLOR_WHITE)
            break
    img.save(OUTPUT_NAME, OUTPUT_FORMAT)

@click.command()
@click.option('--message', '-m', default='LGTM',
        show_default=True, help='画像に乗せるメッセージ')
@click.argument('keyword')
def cli(message: str, keyword: str) -> None:
    """LGTM画像生成プログラム"""
    lgtm(message, keyword)
    print(f'message={message}, keyword={keyword}')
#     click.echo('LGTM')

def lgtm(message: str, keyword: str) -> None:
    """画像のURL・パス・キーワードを指定して画像を取得してLGTMを行う関数。
    Args:
        message (str): 画像に描画するメッセージ
        keyword (str): 画像を取得するURL, ローカルパス, キーワード
    """
    fp = get_image(keyword)
    save_with_message(fp, message)


