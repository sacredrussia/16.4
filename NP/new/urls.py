from django.urls import path
from .views import PostsList, ProductDetail, NewsCreate, ArticleCreate, NewsUpdate, ArticleUpdate, NewsDelete, \
    ArticleDelete, CategoryListView, subscribe
from django.views.decorators.cache import cache_page

urlpatterns = [
    path('', cache_page(300)(PostsList.as_view()), name='post_list'),
    path('<int:pk>', ProductDetail.as_view(), name='product_detail'),
    path('news/create/', NewsCreate.as_view(), name='news_create'),
    path('article/create/', ArticleCreate.as_view(), name='article_create'),
    path('news/<int:pk>/edit/', NewsUpdate.as_view(), name='news_update'),
    path('article/<int:pk>/edit/', ArticleUpdate.as_view(), name='article_update'),
    path('news/<int:pk>/delete/', NewsDelete.as_view(), name='news_delete'),
    path('article/<int:pk>/delete/', ArticleDelete.as_view(), name='article_delete'),
    path('categories/<int:pk>/', CategoryListView.as_view(), name='category_list'),
    path('categories/<int:pk>/subscribe', subscribe, name='subscribe')

]
