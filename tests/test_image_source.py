from typing import Optional, Union, Any
from typing import Callable, NoReturn
from typing import Sequence, Iterable, List, Tuple
from typing import Dict
from typing import TypeVar, Generic, NewType, Type

import requests
import unittest
from lgtm.image_source import LocalImage, RemoteImage, KeywordImage

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

class RemoteImageTest(unittest.TestCase):
    def test_remote_image_get(self):
        with open('tests/data/1511881055.jpg', 'rb') as fp:
            test_img = fp.read()
        url = 'https://animekabegami.com/download?id=1511881055&width=1920&height=1080'
        rimage = RemoteImage(url)
        fp = rimage.get_image()
        img = fp.read()
        self.assertEqual(test_img, img)
        
    def test_remote_image_invalid_url(self):
#         with self.assertRaises(requests.exceptions.RequestException):
        with self.assertRaises(requests.exceptions.RequestException):
            url = 'https://hogehoge.com/hogehoge.jpg'
            rimage = RemoteImage(url)
            fp = rimage.get_image()


class KeywordImageTest(unittest.TestCase):
    def test_keyword_image_get(self):
        keyword = '画像'
        kimage = KeywordImage(keyword)
        img = kimage.get_image()
        self.assertTrue(img)


