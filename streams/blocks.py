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