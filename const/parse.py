# author: Jedore (https://github.com/Jedore)
# date: 03/12/2024
# file: parse.py
# desc:

"""
头文件来自 6.7.7
"""

import re


def main():
    items = {}
    with open('ThostFtdcUserApiDataType.h', 'r', encoding='gbk') as fp:
        item = []
        name = ''
        key = ''
        for line in fp:
            line = line.strip()
            ret = re.match(r'^/+TFtdc(.+)是一个(.+)$', line)
            if ret:
                if not item:
                    items.pop(key, None)

                key = ret.group(1) + ' ' + ret.group(2)
                item = items.setdefault(key, [])

            ret = re.match(r'///([^/]+)', line)
            if ret:
                name = ret.group(1)

            ret = re.match(r'^#define (\S+) (\S+)', line)
            if ret:
                item.append((name, ret.group(1), ret.group(2)))

            ret = re.match(r'^typedef char (\S+);', line)
            if ret:
                if item:
                    item.append(ret.group(0))

    with open('../docs/const.md', 'w', encoding='utf8') as fp:
        fp.write('#CTP常量定义\n')
        fp.write('> CTPAPI 6.7.7\n\n')
        for index, item in enumerate(items.items()):
            name, consts = item
            fp.write(f'#### {index + 1}. {name.split()[0]}\n\n')
            fp.write(f'{name.split()[1]}\n\n')
            fp.write(f'`{consts[-1]}`\n\n')
            fp.write('|名称|宏定义|常量|\n')
            fp.write('|--|--|--|\n')
            for i in consts[:-1]:
                fp.write(f"""| {i[0]} | `{i[1]}` | `{i[2]}` |\n""")
            fp.write('\n')


if __name__ == '__main__':
    main()
