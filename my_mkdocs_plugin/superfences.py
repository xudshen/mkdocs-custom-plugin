import re


def _escape(txt):
    """Basic html escaping."""

    txt = txt.replace('&', '&amp;')
    txt = txt.replace('<', '&lt;')
    txt = txt.replace('>', '&gt;')
    return txt


def fence_kotlin_run_format(source, language, css_class, options, md):
    """Format source as div."""
    attrs = {"data-executable": "true",
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
                    attrs["data-version"] = kotlin_ver
            except:
                pass
            try:
                kotlin_ver = re.search(r"^\s*//\s*arrow:\s?(\d+.\d+.\d+)\s*$", line).group(1)
                if kotlin_ver:
                    skip_line = True
                    attrs["data-arrow-version"] = kotlin_ver
            except:
                pass
            try:
                kotlin_ver = re.search(r"^\s*//\s*exec:\s?(none|true|incremental)\s*$", line).group(
                    1)
                if kotlin_ver == "true" or kotlin_ver == "incremental":
                    skip_line = True
                    attrs["data-executable"] = kotlin_ver
                elif kotlin_ver == "none":
                    skip_line = True
                    del attrs["data-executable"]
            except:
                pass
            try:
                range_str = re.search(r"^\s*//\s*range:\s?(\d+,\d+)\s*$", line).group(1)
                if range_str:
                    skip_line = True
                    attrs["from"] = range_str.split(",")[0]
                    attrs["to"] = range_str.split(",")[1]
            except:
                pass
        if not skip_line:
            srcs.append(line)

    return '<div class="%s" %s>%s</div>' % (
        css_class, " ".join(['%s="%s"' % (k, v) for k, v in attrs.items()]), "\n".join(srcs))

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
