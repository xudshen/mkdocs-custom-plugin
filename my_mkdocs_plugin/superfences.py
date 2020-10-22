import re


def _escape(txt):
    """Basic html escaping."""

    txt = txt.replace('&', '&amp;')
    txt = txt.replace('<', '&lt;')
    txt = txt.replace('>', '&gt;')
    return txt

def fence_kotlin_run_format(source, language, class_name, options, md, **kwargs):

    classes = kwargs['classes']
    id_value = kwargs['id_value']
    attrs = kwargs['attrs']

    if class_name:
        classes.insert(0, class_name)

    id_value = ' id="{}"'.format(id_value) if id_value else ''
    classes = ' class="{}"'.format(' '.join(classes)) if classes else ''
    attrs = ' ' + ' '.join('{k}="{v}"'.format(k=k, v=v) for k, v in attrs.items()) if attrs else ''

    """Format source as div."""
    k_attrs = {"data-executable": "true",
             "match-brackets": "true",
             "highlight-on-fly": "true",
             "data-autocomplete": "true",
             "auto-indent": "true"}
    srcs = []
    enter_body = False
    for line in _escape(source).split("\n"):
        skip_line = False
        if not re.match(r"^(\s*//[\s\S]*)|(\s*)$", line):
            enter_body = True
        if not enter_body:
            try:
                kotlin_ver = re.search(r"^\s*//\s*kotlin:\s?(\d+.\d+.\d+)\s*$", line).group(1)
                if kotlin_ver:
                    skip_line = True
                    k_attrs["data-version"] = kotlin_ver
            except:
                pass
            try:
                kotlin_ver = re.search(r"^\s*//\s*arrow:\s?(\d+.\d+.\d+)\s*$", line).group(1)
                if kotlin_ver:
                    skip_line = True
                    k_attrs["data-arrow-version"] = kotlin_ver
            except:
                pass
            try:
                kotlin_ver = re.search(r"^\s*//\s*exec:\s?(none|true|incremental)\s*$", line).group(
                    1)
                if kotlin_ver == "true" or kotlin_ver == "incremental":
                    skip_line = True
                    k_attrs["data-executable"] = kotlin_ver
                elif kotlin_ver == "none":
                    skip_line = True
                    del k_attrs["data-executable"]
            except:
                pass
            try:
                range_str = re.search(r"^\s*//\s*range:\s?(\d+,\d+)\s*$", line).group(1)
                if range_str:
                    skip_line = True
                    k_attrs["from"] = range_str.split(",")[0]
                    k_attrs["to"] = range_str.split(",")[1]
            except:
                pass
        if not skip_line:
            srcs.append(line)

    k_attrs = ' '.join('{k}="{v}"'.format(k=k, v=v) for k, v in k_attrs.items()) if k_attrs else ''
    return '<div%s%s%s %s>%s</div>' % (id_value, classes, attrs, k_attrs, "\n".join(srcs))

# if __name__ == "__main__":
#     print(fence_kotlin_run_format("""
# //kotlin: 1.3.40
# //arrow: 123.0.0
# //exec: incremental
# //range: 0,10
#
#         fun helloworld() {
#             println("hello world!")
#         }
#             """, None, "hehe", None, None))
