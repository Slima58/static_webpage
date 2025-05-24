import unittest
from markdown_object_parse import extract_markdown_images, extract_markdown_links

class TestObjectParse(unittest.TestCase):
    def test_image_parse(self):
        text = "This is text with a ![rick roll](https://i.imgur.com/aKaOqIh.gif) \
            and ![obi wan](https://i.imgur.com/fJRm4Vk.jpeg)"
        image_parse = extract_markdown_images(text)
        self.assertListEqual(
            [
                ("rick roll", "https://i.imgur.com/aKaOqIh.gif"),
                ("obi wan", "https://i.imgur.com/fJRm4Vk.jpeg")
            ],
            image_parse
        )

    def test_link_parse(self):
        text = "This is text with a link [to boot dev](https://www.boot.dev) and \
            [to youtube](https://www.youtube.com/@bootdotdev)"
        link_parse = extract_markdown_links(text)
        self.assertListEqual(
            [
                ("to boot dev", "https://www.boot.dev"),
                ("to youtube","https://www.youtube.com/@bootdotdev")
            ],
            link_parse
        )


