import click

@click.command()
def cli():
    """LGTM画像生成プログラム"""
    lgtm()
    click.echo('LGTM')

def lgtm():
    pass

def func(**kwargs):
    ret = ''
    for key, val in kwargs.items():
        ret = ret + f'key={key}, value={val}\n'
    return ret



