from typing import Optional, Union, Any
from typing import Callable, NoReturn
from typing import Sequence, Iterable, List, Tuple
from typing import Dict
from typing import TypeVar, Generic, NewType, Type
from typing import IO, TextIO, BinaryIO

import click


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
    pass




