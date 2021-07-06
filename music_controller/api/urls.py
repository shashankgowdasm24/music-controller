from django.db import router
from django.urls import path
from django.urls.conf import include
from .views import  GameGenericApiView, GameViewset, GamesDataModel,ArticleViewSetGeneric, ArticleModelViewSet, RoomView, CreateRoomView, GetRoom, JoinRoom, UserInRoom, LeaveRoom, UpdateView, article_list, ArticleData, GetArticles, article_detail, ModifyArticleData, GenericApiView, ArticleViewSet
from rest_framework.routers import DefaultRouter

router = DefaultRouter()
router.register('article', ArticleViewSet, basename='article')

router1 = DefaultRouter()
router1.register('aricle-generic', ArticleViewSetGeneric,
                 basename='aricle-generic')

router2 = DefaultRouter()
router2.register('aricle-model', ArticleModelViewSet,
                 basename='aricle-model')

router3 = DefaultRouter()
router3.register('game-model', GamesDataModel, basename='game-model')

router4 = DefaultRouter()
router4.register('normal-game', GameViewset, basename='normal-game')

urlpatterns = [
    path('viewsetgame/', include(router3.urls)),
    path('room', RoomView.as_view()),
    path('create-room', CreateRoomView.as_view()),
    path('get-room', GetRoom.as_view()),
    path('join-room', JoinRoom.as_view()),
    path('user-in-room', UserInRoom.as_view()),
    path('leave-room', LeaveRoom.as_view()),
    path('update-room', UpdateView.as_view()),
    path('article-data/', ArticleData.as_view()),
    path('get-articles/', GetArticles.as_view()),
    path('article/', article_list),
    path('detail/<int:pk>/', article_detail),
    path('article-data/<int:pk>/', ModifyArticleData.as_view()),
    path('generic-article-data/', GenericApiView.as_view()),
    path('generic-article-data/<int:id>/', GenericApiView.as_view()),
    path('viewset/', include(router.urls)),
    path('viewsetgeneric/', include(router1.urls)),
    path('viewsetmodel/', include(router2.urls)),
    path('viewsetNormal/', include(router4.urls)),
    path('game-generic-view/', GameGenericApiView.as_view())
]
