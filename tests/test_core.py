import unittest
from click.testing import CliRunner

from lgtm import core

class LgtmTest(unittest.TestCase):
    def test_lgtm(self):
        """LGTMを行う関数lgtm()のテスト
        Raises:
            AssertionError テスト失敗
        """
        self.assertIsNone(core.lgtm('message', 'keyword'))

    def test_cli_params(self):
        """LGTMコマンドのオプションと引数がきちんと渡されているか確認。
        Raises:
            AssertionError コマンドエラーかオプション引数がきちんと渡されていない
        """
        message = 'LGTM'
        keyword = 'sample.jpg'
        test_result = f'message={message}, keyword={keyword}\n'
        runner = CliRunner()
        result = runner.invoke(core.cli, ['--message', message, keyword])
        print(result.output)
        self.assertTrue(result.exit_code == 0 and result.output == test_result)

