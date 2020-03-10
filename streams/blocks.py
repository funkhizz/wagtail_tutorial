# Complex data type

# StreamFields

from wagtail.core import blocks
from wagtail.images.blocks import ImageChooserBlock

class TitleAndTextBlock(blocks.StructBlock):
    # Title and Text
    title = blocks.CharBlock(required=True, help_text="Add your title")
    text = blocks.TextBlock(required=True, help_text="Add additional text")

    class Meta:
        template = 'streams/title_text_block.html'
        icon = "edit"
        label = "Title&Text"


class CardBlock(blocks.StructBlock):
    title = blocks.CharBlock(required=True, help_text="Add your title")

    cards = blocks.ListBlock(
        blocks.StructBlock(
            [
                ("image", ImageChooserBlock(required=True)),
                ("title", blocks.CharBlock(required=True, max_length=40)),
                ("text", blocks.CharBlock(required=True, max_length=200)),
                ("button_page", blocks.PageChooserBlock(required=False)),
                ("button_url", blocks.URLBlock(required=False, help_text="If the button page exists use it first")),
            ]
        )
    )

    class Meta:
        template = "streams/card_block.html"
        icon = "placeholder"
        label = "Staff Cards"


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


class CTABlock(blocks.StructBlock):
    # Call action section

    title = blocks.CharBlock(required=True, max_length=50)
    text = blocks.RichTextBlock(requored=True, features=["bold", "italic"])
    button_page = blocks.PageChooserBlock(required=False)
    button_url = blocks.URLBlock(required=False)
    button_text = blocks.CharBlock(required=True, default='Learn more', max_length=30)

    class Meta:
        template = "streams/cta_block.html"
        icon = "placeholer"
        label = "Call to Action"
