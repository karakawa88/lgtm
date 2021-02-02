from lgtm import core

def main():
    dic = {
        'name': 'RobinFooter',
        'stock': 1280
    };
    print(core.func(**dic))
    print('CircleCIテスト')
    print('CircleCIテスト PullRequestのテスト')
    core.cli()

if __name__ == '__main__':
    main()
