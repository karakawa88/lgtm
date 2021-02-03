import unittest
from click.testing import CliRunner

from lgtm import core

class LgtmTest(unittest.TestCase):
    def test_lgtm(self):
        """LGTMを行う関数lgtm()のテスト
        Raises:
            AssertionError テスト失敗
        """
        self.assertIsNone(core.lgtm())

    def test_cli_params(self):
        """LGTMコマンドのオプションと引数がきちんと渡されているか確認。
        Raises:
            AssertionError コマンドエラーかオプション引数がきちんと渡されていない
        """
        message = 'LGTM'
        keyword = 'sample.jpg'
        test_result = f'message={message}, keyword={keyword}'
        runner = CliRunner()
        result = runner.invoke(core.cli, ['--message', message, keyword])
        self.assertEqual(result.exit_code == 0 and result.output == test_result)

