from django.urls import path
from .views import RoomView, CreateRoomView, GetRoom, JoinRoom, UserInRoom, LeaveRoom, UpdateView, article_list, ArticleData, GetArticles, article_detail, ModifyArticleData, GenericApiView

urlpatterns = [
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
    path('generic-article-data/<int:id>/', GenericApiView.as_view())
]
