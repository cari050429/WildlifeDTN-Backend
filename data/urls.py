from django.urls import path
from .views import ListData,  DeleteData, LoginView, post_view, LogoutView, CheckAuthenticationView, PictureDetailData, HumidityDetailData, TemperatureDetailData
from rest_framework_simplejwt import views as jwt_views

urlpatterns=[
    path('temperature/<int:pk>',TemperatureDetailData.as_view(), name='tempdetail'),
    path('humidity/<int:pk>',HumidityDetailData.as_view(), name='humiditydetail'),
    path('picture/<int:pk>',PictureDetailData.as_view(), name='picturedetail'),
    path('', ListData.as_view(), name='listdata'),
    path('delete/<int:pk>',DeleteData.as_view(), name='deletedetail'),
    path('login',LoginView.as_view(), name='login'),
    path('post', post_view, name='post'),
    path('authenticated',CheckAuthenticationView.as_view()),
    path('logout',LogoutView.as_view()),
    path('token/', jwt_views.TokenObtainPairView.as_view(), name ='token_obtain_pair'),
    path('token/refresh/', jwt_views.TokenRefreshView.as_view(), name ='token_refresh')
]

