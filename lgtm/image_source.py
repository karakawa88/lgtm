from typing import Optional, Union, Any
from typing import Callable, NoReturn
from typing import Sequence, Iterable, List, Tuple
from typing import Dict
from typing import TypeVar, Generic, NewType, Type
from typing import IO, TextIO, BinaryIO

import requests
from pathlib import Path
from abc import ABCMeta, abstractmethod
from io import BytesIO

class AbstractImage(metaclass=ABCMeta):
    """抽象クラス
    Args:
    """
    def __init__(self) -> None:
        pass

    @abstractmethod
    def get_image(self) -> BinaryIO:
        """画像を取得して返す。
        Returns:
            BinaryIO: 画像のファイルオブジェクト
        """
        pass


class LocalImage(AbstractImage):
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

class RemoteImage(AbstractImage):
    """URLで指定しネットから画像を取得するクラス
    Args:
    Attributes:
        url (str): 画像のURL文字列
    """
    def __init__(self, url: str) -> None:
        self.__url = url

    @property
    def url(self) -> str:
        return self.__url

    @url.setter
    def url(self, url: str) -> None:
        self.__url = url

    def get_image(self) -> BinaryIO:
        """画像のファイルをURLから取得してそのFileオブジェクトを返す。
        Returns:
            BinaryIO: 画像のファイルオブジェクト
        """
        try:
            headers = {
                'User-Agent': 'PythonLoader'
            }
            res = requests.get(self.url, headers=headers)
            res.raise_for_status()
        except requests.exceptions.RequestException as ex:
            raise ex
        return BytesIO(res.content)

class _LoremFlickr(RemoteImage):
    """キーワードをもとにネットから画像を取得する。
    Args:
        keyword (str): キーワード
    """
    LOREM_FLICKR_URL = 'https://loremflickr.com'
    WIDTH = 1280
    HEIGHT = 768

    def __init__(self, keyword: str) -> None:
        super().__init__(self._build_url(_LoremFlickr.LOREM_FLICKR_URL,
            _LoremFlickr.WIDTH,
            _LoremFlickr.HEIGHT,
            keyword))

    def _build_url(self, url: str,
            width: int, height: int, keyword: str) -> str:
        return (
            f'{url}/{width}/{height}/{keyword}'
        )


KeywordImage = _LoremFlickr

