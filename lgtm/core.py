import click

@click.command()
@click.option('--message', '-m', default='LGTM',
        show_default=True, help='画像に乗せるメッセージ')
@click.argument('keyword')
def cli(message, keyword):
    """LGTM画像生成プログラム"""
    lgtm(message, keyword)
    print(f'message={message}, keyword={keyword}')
#     click.echo('LGTM')

def lgtm(message, keyword):
    pass




