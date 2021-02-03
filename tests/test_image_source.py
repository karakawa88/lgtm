from typing import Optional, Union, Any
from typing import Callable, NoReturn
from typing import Sequence, Iterable, List, Tuple
from typing import Dict
from typing import TypeVar, Generic, NewType, Type

import unittest
from lgtm.image_source import LocalImage

class LocalImageTest(unittest.TestCase):
    def test_local_image_file_not_found(self):
        """画像ファイルが存在しない場合例外をスローするか確認する
        Raises:
            AssertionError: ファイルが存在しないのに例外をスローしない
        """
        path = 'tests/data/image.png'
        with self.assertRaises(FileNotFoundError):
            LocalImage(path)

    def test_local_image_file(self):
        """画像ファイルが本当に読み込まれるかテスト。
        Raises:
            AssertionError: 画像ファイル読み込み成功
        """
        path = 'tests/data/image.jpg'
        with open(path, 'rb') as fp:
            image_data = fp.read()
        local_img = LocalImage(path)
        imgfp = local_img.get_image()
        result = imgfp.read()
        self.assertEqual(result, image_data)

