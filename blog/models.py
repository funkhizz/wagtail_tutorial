from django.db import models
from wagtail.core.models import Page, Orderable
from wagtail.admin.edit_handlers import FieldPanel, StreamFieldPanel, MultiFieldPanel, InlinePanel
from wagtail.core.fields import StreamField
from streams import blocks
from wagtail.images.edit_handlers import ImageChooserPanel
from wagtail.contrib.routable_page.models import RoutablePageMixin, route
from django.shortcuts import render
from wagtail.snippets.models import register_snippet
from modelcluster.fields import ParentalKey
from wagtail.snippets.edit_handlers import SnippetChooserPanel


class BlogAuthorOrderable(Orderable):
    """ allow to select one or more blog authors """

    page = ParentalKey("blog.BlogDetailPage", related_name="blog_authors")
    author = models.ForeignKey(
        "blog.BlogAuthor",
        on_delete=models.CASCADE,
    )

    panels = [
        SnippetChooserPanel("author"),
    ]

class BlogAuthor(models.Model):
    name = models.CharField(max_length=100)
    website = models.URLField(blank=True, null=True)
    image = models.ForeignKey(
        "wagtailimages.Image",
        on_delete=models.SET_NULL,
        null=True,
        blank=False,
        related_name="+"
    )

    panels = [
        MultiFieldPanel(
            [
                FieldPanel("name"),
                ImageChooserPanel("image")
            ], heading="Name and Image",
        ),
        MultiFieldPanel(
            [
                FieldPanel("website"),
            ], heading="Links"
        )
    ]

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = "Blog Author"
        verbose_name_plural = "Blog Authors"

register_snippet(BlogAuthor)

class BlogCategory(models.Model):
    """Blog Category for a snippet"""
    name = models.CharField(max_length=255)
    slug = models.SlugField(
        verbose_name="slug",
        allow_unicode=True,
        max_length=255,
        help_text="A slug to identify posts by this category"
    )

    class Meta:
        verbose_name = "Blog Category"
        verbose_name_plural = "Blog Categories"
        ordering = ["name"]

    def __str__(self):
        return self.name

    panels = [
        FieldPanel("name"),
        FieldPanel("slug")
    ]

register_snippet(BlogCategory)

class BlogListingPage(RoutablePageMixin, Page):
    # Listing page lists all the Blog Detail Pages

    template = "blog/blog_listing_page.html"

    custom_title = models.CharField(max_length=100, blank=False, null=False, help_text='Overwhites the defaul title')

    def get_context(self, request, *args, **kwargs):
        context = super().get_context(request, *args, **kwargs)
        context["posts"] = BlogDetailPage.objects.live().public()
        context["special_link"] = self.reverse_subpage('latest_posts')
        context["authors"] = BlogAuthor.objects.all()
        return context

    content_panels = Page.content_panels + [
        FieldPanel("custom_title"),
    ]

    @route(r'latest/$', name="latest_posts")
    def latest_posts(self, request, *args, **kwargs):
        context = self.get_context(request, *args, **kwargs)
        context["latest_posts"] = BlogDetailPage.objects.live().public()[:1]
        return render(request, 'blog/latest_posts.html', context)

    def get_sitemap_urls(self, request):  # Sitemap for routable page
        # Uncoment to have no sitemap for this page
        # reutrn []
        sitemap = super().get_sitemap_urls(request)
        sitemap.append(
            {
                "location": self.full_url + self.reverse_subpage("latest_posts"),
                "lastmod": (self.last_published_at or self.latest_revision_created_at)
            }
        )
        return sitemap


class BlogDetailPage(Page):
    # Blog Detail Page
    template = "blog/blog_detail_page.html"

    custom_title = models.CharField(max_length=100, blank=False, null=False, help_text='Overwhites the defaul title')
    blog_image = models.ForeignKey(
        "wagtailimages.Image",
        blank=False,
        null=True,
        related_name="+",
        on_delete=models.SET_NULL
    )

    content = StreamField(
        [
            ("title_text", blocks.TitleAndTextBlock()),
            ("full_richtext", blocks.RichTextBlock()),
            ("simple_richtext", blocks.SimpleRichTextBlock()),
            ("cards", blocks.CardBlock()),
            ("cta", blocks.CTABlock())
        ],
        null=True,
        blank=True
    )

    content_panels = Page.content_panels + [
        FieldPanel("custom_title"),
        ImageChooserPanel("blog_image"),
        MultiFieldPanel(
            [
                InlinePanel("blog_authors", label="Author", min_num=1, max_num=4)
            ], heading="Author(s)"
        ),
        StreamFieldPanel("content"),
    ]
