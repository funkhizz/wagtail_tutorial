# Complex data type

# StreamFields

from wagtail.core import blocks


class TitleAndTextBlock(blocks.StructBlock):
    # Title and Text
    title = blocks.CharBlock(required=True, help_text="Add your title")
    text = blocks.TextBlock(required=True, help_text="Add additional text")

    class Meta:
        template = 'streams/title_text_block.html'
        icon = "edit"
        label = "Title&Text"


class RichTextBlock(blocks.RichTextBlock):
    # Rich Text with all features
    class Meta:
        template = "streams/richtext_block.html"
        icon = "doc"
        label = "Full RichText"


class SimpleRichTextBlock(blocks.RichTextBlock):
    # Rich Text with 3(limited) features
    def __init__(self, required=True, help_text=None, editor='default', features=None, **kwargs):
        super().__init__(**kwargs)
        self.features = [
            "bold",
            "italic",
            "link"
        ]

    class Meta:
        template = "streams/richtext_block.html"
        icon = "edit"
        label = "Simple RichText"