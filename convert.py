import glob
import os
import re
import shutil

import yaml
from bs4 import BeautifulSoup, Tag


def versions():
    nav_all = [{"Home": "index.md"}]
    for path in glob.glob('sources/*'):
        nav = convert(path)
        nav_all.append(nav)
        copy_doc(path)

    update_nav({'nav': nav_all})


def convert(path):
    return gen_nav(path)


def gen_nav_item(path, lines, line_index=0, last_indent_len=0):
    nav = []
    line_total = len(lines)
    while line_index < line_total:
        line = lines[line_index]
        match = re.search(f'<p>(　+)<a href="(.+)">(.+)</a></p>', line)
        if match:
            indent, href, name = match.groups()

            indent_len = len(indent)
            if last_indent_len != 0:
                if last_indent_len < indent_len:
                    line_index, _nav = gen_nav_item(path, lines, line_index,
                                                    indent_len)
                    last = nav[-1]
                    key = list(last.keys())[0]
                    _nav.insert(0, {key: last[key]})
                    nav[-1][key] = _nav
                    continue
                elif last_indent_len > indent_len:
                    break
            href = os.path.join(*href.split('/'))
            content = gen_content(os.path.join(path, href))
            md = gen_file(
                os.path.join(path.replace("sources", "docs"), href),
                content)
            nav.append({name: md})

            last_indent_len = indent_len

        line_index += 1

    return line_index, nav


def gen_nav(path):
    version = path.split(os.sep)[1]
    with open(os.path.join(path, "_Index.html"), 'r', encoding='gbk') as f:
        lines = f.readlines()

    _, nav = gen_nav_item(path, lines)

    return {version: {' ': nav}}


def gen_content(href):
    depth = len(href.split(os.sep)) - 2
    soup = parse(href)
    content = soup.find("div", id="content")
    for child in content.children:  # type: Tag
        if not isinstance(child, Tag):
            continue
        if child.name == "script":
            child.decompose()
        if child.attrs is not None and child.attrs.get("id") == 'left_menu':
            child.decompose()

    for item in content.find_all("p", class_="back_to_top_link"):  # type: Tag
        if item:
            item.decompose()
    for item in content.find_all("script"):  # type: Tag
        if item:
            item.decompose()
    item = content.find("div", id="left_menu")  # type: Tag
    if item:
        item.decompose()
    item = content.find("div", class_="nav-links-list")  # type: Tag
    if item:
        item.decompose()

    lines = []

    def gen_sub_content(item: Tag, index=1):
        for child in item.children:  # type: Tag
            if not isinstance(child, Tag):
                continue
            if (child.name == f"h{index}" and child.attrs is not None and
                    'title' in child.attrs.get("class")):
                title = child.text.replace("◇ ", "")
                lines.append("#" * index + "# " + title + "\n")
            elif (child.attrs is not None and
                  "panel" in child.attrs.get("id", "")):
                gen_sub_content(child, index + 1)
            else:
                sub = str(child).replace('.html">', '/">')
                if depth == 1:
                    sub, _ = re.subn('href="([^\.])', 'href="../\\1', sub)
                else:
                    sub, _ = re.subn('href="', 'href="../', sub)
                # sub = str(child).replace('href="', 'href="../')
                lines.append(sub + "\n")

    gen_sub_content(content)

    return lines


def gen_file(path, content):
    dirname = os.path.dirname(path)
    basename = os.path.basename(path)
    basename = basename.replace(".html", ".md")
    if not os.path.exists(dirname):
        os.makedirs(dirname, exist_ok=True)
    file = os.path.join(dirname, basename)
    with open(file, mode="w", encoding="utf-8") as fp:
        fp.writelines(content)

    return file.split(os.sep, 1)[1].replace(os.sep, "/")


def parse(path) -> BeautifulSoup:
    with open(path, mode='r', encoding='gbk') as fp:
        soup = BeautifulSoup(fp, 'html.parser')
    return soup


def update_nav(new_nav):
    with open('mkdocs_base.yml', 'r', encoding='utf8') as fp:
        base = fp.read()

    with open('mkdocs.yml', 'w', encoding='utf8') as fp:
        new = yaml.safe_dump(new_nav, allow_unicode=True)
        fp.write(base + new)


def copy_doc(path):
    for file in glob.glob(os.path.join(path, '*.h')):
        dst = os.sep.join(["docs", *file.split(os.sep)[1:]])
        with open(file, 'r', encoding='gbk') as f1:
            with open(dst, 'w', encoding='utf8') as f2:
                f2.write(f1.read())
    for file in glob.glob(os.path.join(path, '*.xml')):
        dst = os.sep.join(["docs", *file.split(os.sep)[1:]])
        shutil.copy(file, dst)


if __name__ == "__main__":
    versions()
