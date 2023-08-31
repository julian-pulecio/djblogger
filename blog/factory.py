import factory
from factory.faker import faker
from django.contrib.auth.models import User
from .models import Post

FAKE = faker.Faker()

class PostFactory(factory.django.DjangoModelFactory):
    class Meta:
        model = Post
    
    title = factory.Faker('sentence', nb_words=12)
    sub_title = factory.Faker('sentence', nb_words=12)
    slug = factory.Faker('slug')
    author = User.objects.get_or_create(username='admin')[0]
    status = Post.Status.PUBLISHED

    @factory.lazy_attribute
    def content(self):
        return '\n'.join([ FAKE.paragraph(nb_sentences=30) for _ in range(5)])
