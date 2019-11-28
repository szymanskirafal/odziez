from django.test import RequestFactory, TestCase
from django.urls import reverse
from django.utils import timezone
from django.views import generic, View


#from ..forms import ArticleForm
#from ..models import Article
from clothes.models import KindOfClothe, Manufacturer
from employees.models import Job, Position
from employees.views import EmployeeDetailView


class TestEmployeeDetailView(TestCase):

    def test_view_inherits_from_correct_class(self):
        class_expected = generic.DetailView
        class_given = EmployeeDetailView().__class__.__base__
        self.assertEqual(class_expected, class_given)

    def test_kind_available_for_returns_correct_for_job_with_one_position(self):
        """
        kinds_available = KindOfClothe.objects.all().filter(
            (Q(available_for=self.object.job.position_1) | Q(available_for=self.object.job.position_2))
            )
        """
        position_1 = Position.objects.create(name = 'Nalewkowy')
        position_2 = Position.objects.create(name = 'Kasjer')
        manufacturer = Manufacturer.objects.create(
            name = 'Zakład Produkcji Odzieży',
            email = 'zpo@zpo.pl',
            )
        job = Job.objects.create(
            name = 'Nalewkowy 100',
            position_1 = position_1,
            size_of_position_1 = 1.00,
            )
        """

        kind_1 = KindOfClothe.objects.create(
            name = 'spodnie',
            description = 'spodnie długie',
            months_to_exchange = 12,
            available_for = position_1,
            manufacturer = manufacturer,
            )
        kind_2 = KindOfClothe.objects.create(
            name = 'koszula',
            description = 'koszula biała',
            months_to_exchange = 12,
            available_for = position_1,
            manufacturer = manufacturer,
            )
        """
        print('----------- here')






"""
    def test_view_get_method_runs_another_view(self):
        view_class_expected = ArticleDetailJustDisplayView
        url = '/fake-url'
        request = RequestFactory().get(url)
        in_the_past = timezone.now() - timezone.timedelta(days = 1)
        article_published = Article.objects.create(
            title = 'tre',
            body = 'test',
            pub_date = in_the_past,
        )
        pk = article_published.pk
        response = ArticleDetailView.get(self, request, pk = pk)
        view_used_after_get = response.__dict__['context_data']['view']
        view_class_given = view_used_after_get.__class__
        self.assertEqual(view_class_expected, view_class_given)

    def test_view_post_method_runs_another_view(self):
        view_class_expected = ArticleDetailAddCommentView
        url = '/fake-url'
        request = RequestFactory().post(url)
        in_the_past = timezone.now() - timezone.timedelta(days = 1)
        article_published = Article.objects.create(
            title = 'tre',
            body = 'test',
            pub_date = in_the_past,
        )
        pk = article_published.pk
        response = ArticleDetailView.post(self, request, pk = pk)
        view_used_after_post = response.context_data['view']
        view_class_given = view_used_after_post.__class__
        self.assertEqual(view_class_expected, view_class_given)
"""
