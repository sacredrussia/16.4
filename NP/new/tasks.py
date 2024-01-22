from celery import shared_task
import datetime
from django.dispatch import receiver
from django.template.loader import render_to_string
from django.core.mail import EmailMultiAlternatives

from django.conf import settings

from .models import Post, Category


@shared_task
def info_after_new_post(pk):
    post = Post.objects.get(pk=pk)
    categories = post.category.all()
    title = post.title
    subscribers_emails = []

    for category in categories:
        subscribers_user = category.subscribers.all()
        for sub_users in subscribers_user:
            subscribers_emails.append(sub_users.email)

    html_content = render_to_string(
        'post_created_email.html', {
            'text': f'{title}',
            'link': f'{settings.SITE_URL}/posts/{pk}'
        }
    )

    msg = EmailMultiAlternatives(
        subject=title,
        body='',
        from_email=settings.DEFAULT_FROM_EMAIL,
        to=subscribers_emails,
    )

    msg.attach_alternative(html_content, 'text/html')
    msg.send()


@shared_task
def sending_letter_every_week():
    todey = datetime.datetime.now()
    last_week = todey - datetime.timedelta(days=7)
    posts = Post.objects.filter(time_creation__gte=last_week)
    categories = set(posts.values_list('category__category', flat=True))
    subscribers = set(Category.objects.filter(category__in=categories).values_list('subscribers__email', flat=True))

    html_content = render_to_string(
        'daily_post.html',
        {
            'link': settings.SITE_URL,
            'posts': posts

        }
    )

    msg = EmailMultiAlternatives(
        subject='Статьи за неделю',
        body='',
        from_email=settings.DEFAULT_FROM_EMAIL,
        to=subscribers
    )

    msg.attach_alternative(html_content, 'text/html')
    msg.send()
