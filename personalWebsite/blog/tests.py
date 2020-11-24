import datetime

from django.test import TestCase
from django.utils import timezone
from django.urls import reverse

from .models import Article

# Create your tests here.
def create_article(title, days):
    """
    Creates an article of given title published given days from now
    (negative for past, positive for future)
    """
    time = timezone.now() + datetime.timedelta(days=days)
    return Article.objects.create(title=title, pub_date=time, last_modified=time)

class BlogIndexViewTests(TestCase):
    def test_no_articles(self):
        """
        If no articles exist, an appropriate message is displayed
        """

        response = self.client.get(reverse('blog:index'))

        self.assertEquals(response.status_code, 200)
        self.assertContains(response, "No articles are available.")
        self.assertQuerysetEqual(response.context['articles'], [])

    def test_future_articles(self):
        """
        If future articles exist, it is not displayed.
        """

        create_article('future article', 10)

        response = self.client.get(reverse('blog:index'))

        self.assertEquals(response.status_code, 200)
        self.assertContains(response, "No articles are available.")
        self.assertQuerysetEqual(response.context['articles'], [])

    def test_past_articles(self):
        """
        If past articles exist, it will be displayed
        """
        create_article('past article', -10)

        response = self.client.get(reverse('blog:index'))

        self.assertEquals(response.status_code, 200)
        self.assertQuerysetEqual(
            response.context['articles'],
            ['<Article: past article>',])

    def test_past_and_future_articles(self):
        """
        If past and future articles exist, only past articles will be displayed
        """

        create_article('past article', -10)
        create_article('future article', 10)

        response = self.client.get(reverse('blog:index'))

        self.assertEquals(response.status_code, 200)
        self.assertQuerysetEqual(
            response.context['articles'],
            ['<Article: past article>',])

    def test_two_past_articles(self):
        """
        If multiple past articles exist, display them by pub_date descending
        """

        create_article('older article', -10)
        create_article('newer article', -5)

        response = self.client.get(reverse('blog:index'))

        self.assertEquals(response.status_code, 200)
        self.assertQuerysetEqual(
            response.context['articles'],
            ['<Article: newer article>', '<Article: older article>',])

    def test_article_link(self):
        """
        If an article appears, it should have a link to it's article page
        """

        article = create_article('article', -10)

        response = self.client.get(reverse('blog:index'))

        self.assertEquals(response.status_code, 200)
        self.assertContains(response, "/blog/"+str(article.id))
