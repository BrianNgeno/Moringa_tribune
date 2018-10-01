from django.test import TestCase
from .models import Editor,Article,Tags
import datetime as dt
# Create your tests here.

class EditorTestClass(TestCase):
    # setup self instance of editor
    def setUp(self):
        self.Brian = Editor(first_name='Brian',last_name='Ngeno',email='bkn.ngeno@gmail.com')

    '''
    test instance
    '''
    def test_instance(self):
        self.assertTrue(isinstance(self.Brian,Editor))

    # def tearDown(self):
    #     Editor.objects.all().delete()

    '''
    test save editor
    '''
    def test_save_method(self):
        self.Brian.save_editor()
        editors = Editor.objects.all()
        self.assertTrue(len(editors)>0)

    '''
    test delete editor
    '''

    def test_delete_method(self):
        self.Brian.save_editor()
        self.Brian.delete_editor()
        editors = Editor.objects.all()
        self.assertTrue(len(editors)==0)

    '''
    test display editor
    '''

    def test_display(self):
        self.Brian.save_editor()
        editors = Editor.objects.get(first_name ='Brian')
        self.assertEqual(editors.first_name,'Brian')
    '''
    test update editor
    '''

    def test_update_single(self):
        self.Brian.save_editor()
        new = Editor.objects.filter(first_name='Brian').update(first_name='Nick')
        editors = Editor.objects.get(first_name='Nick')
        self.assertEqual(editors.first_name,'Nick')

class ArticleTestCLass(TestCase):
    '''
    setup self instance of Article
    '''
    def setUp(self):
        Brian = Editor(first_name='Brian',last_name='Ngeno',email='bkn.ngeno@gmail.com')
        Brian.save_editor()
        self.Music = Article(title='Music',post='music is a southing sound that moves souls',editor=Brian)
    
    ''' 
    test instance of article
    '''
    def test_instance(self):
       self.assertTrue(isinstance(self.Music,Article))


    # def tearDown(self):
    #    Article.objects.all().delete()
    '''
    test save article
    '''

    def test_save_article(self):
        self.Music.save_article()
        articles = Article.objects.all()
        self.assertTrue(len(articles)>0)

    '''
    test delete article
    '''

    def test_delete_article(self):
        self.Music.save_article()
        self.Music.delete_article()
        articles = Article.objects.all()
        self.assertTrue(len(articles)==0)
    '''
    test for update articles
    '''
    def test_update_article(self):
        self.Music.save_article()
        dist = Article.objects.filter(title='Music').update(title='Business')
        brand = Article.objects.get(title='Business')
        self.assertEqual(brand.title,'Business')

    def test_get_news_today(self):
        test_date = '2017-03-17'
        date = dt.datetime.strptime(test_date, '%Y-%m-%d').date()
        news_by_date = Article.days_news(date)
        self.assertTrue(len(news_by_date) == 0)

class TagsTestClass(TestCase):
    '''
    test setup of tags
    '''
    def setUp(self):
        self.New = Tags(name='New')

    '''
    test instance of tag
    '''
    def test_instance(self):
        self.assertTrue(isinstance(self.New,Tags))

    # def tearDown(self):
    #     Tags.objects.all().delete()
    '''
    test to assertain save tags
    '''
    def test_save_tags(self):
        self.New.save_tags()
        tag = Tags.objects.all()
        self.assertTrue(len(tag)>0)
    '''
    test to assert that delete is working
    '''
    def test_delete_tags(self):
        self.New.save_tags()
        self.New.delete_tags()
        tag = Tags.objects.all()
        self.assertTrue(len(tag)== 0)

    '''
    test to assert that tags update
    '''
    def test_update_tags(self):
        self.New.save_tags()
        new = Tags.objects.filter(name='New').update(name='outdated')
        tag = Tags.objects.get(name='outdated')
        self.assertEqual(tag.name,'outdated')   



    