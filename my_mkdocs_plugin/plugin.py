from bs4 import BeautifulSoup
from mkdocs.plugins import BasePlugin


class MyMkDocsPlugin(BasePlugin):
    def on_post_page(self, output_content, config, **kwargs):
        soup = BeautifulSoup(output_content, 'html.parser')
        mermaids = soup.find_all("div", class_="mermaids")
        kotlin_runs = soup.find_all("div", class_="kotlin-run")

        if mermaids:
            new_tag = soup.new_tag("script", src="https://code.jquery.com/jquery-3.4.1.min.js")
            soup.body.append(new_tag)

            new_tag = soup.new_tag("script")
            new_tag.string = """
$(document).on('load', function () {
  mermaid.initialize();
});
            """
            soup.body.append(new_tag)

        if kotlin_runs:
            new_tag = soup.new_tag("script")
            new_tag.string = """
kotlinPlaygroundOptions = {
};
document.addEventListener('DOMContentLoaded', function() {
  ArrowPlayground('.kotlin-run', kotlinPlaygroundOptions);
});
            """
            soup.body.append(new_tag)

        return str(soup)
