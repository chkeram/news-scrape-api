import unittest

from news_api.data.schemas import Article


class ModelsTest(unittest.TestCase):

    def test_article_schema(self):
        article = Article(
            body="body",
            author=["author1", "author2"],
            headline="headline",
            url="url",
            genre="genre",
            source="source"
        )
        self.assertEqual(article.author, "author1, author2")