from mkdocs.plugins import BasePlugin


class MyMkDocsPlugin(BasePlugin):
    """

    """

# from bs4 import BeautifulSoup
#
#
# class MarkdownCustomPlugin(BasePlugin):
#     def on_post_page(self, output_content, config, **kwargs):
#         soup = BeautifulSoup(output_content, 'html.parser')
#         mermaids = soup.find_all("div", class_="kotlin-run")
#         hasMermaid = 0
#         for mermaid in mermaids:
#             hasMermaid = 1
#
#         if (hasMermaid == 1):
#             new_tag = soup.new_tag("script", src=".https://unpkg.com/kotlin-playground@1")
#             soup.body.append(new_tag)
#
#         return str(soup)
