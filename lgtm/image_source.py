from typing import Optional, Union, Any
from typing import Callable, NoReturn
from typing import Sequence, Iterable, List, Tuple
from typing import Dict
from typing import TypeVar, Generic, NewType, Type
from typing import IO, TextIO, BinaryIO

import requests
from pathlib import Path

class LocalImage():
    """ローカルなパスの画像を表すクラス
    Args:
        pathstr (str): 画像のパス文字列
    Attributes:
        path (Path): 画像のパス
    """
    def __init__(self, pathstr: str) -> None:
        path = Path(pathstr)
        if not path.exists():
            raise FileNotFoundError(f'画像ファイル[{pathstr}]は存在しません。')
        self.__path = path

    @property
    def path(self) -> Path:
        return self.__path
    @path.setter
    def path(self, path: Path) -> None:
        self.__path = path

    def get_image(self) -> BinaryIO:
        """画像のファイルをオープンしてそのFileオブジェクトを返す。
        Returns:
            File: 画像のファイルオブジェクト
        """
        return self.path.open('rb')

