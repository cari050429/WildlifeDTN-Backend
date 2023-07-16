from django.urls import path
<<<<<<< HEAD
from .views import ListData,  DeleteData, LoginView, post_view, LogoutView, CheckAuthenticationView, PictureDetailData, HumidityDetailData, TemperatureDetailData, BlacklistTokenUpdateView, post_node_sensor
from rest_framework_simplejwt import views as jwt_views
=======
from rest_framework_simplejwt.views import TokenObtainPairView, TokenRefreshView
from .views import ListData,  DeleteData, LoginView, post_view, LogoutView, CheckAuthenticationView, PictureDetailData, HumidityDetailData, TemperatureDetailData
>>>>>>> 817bf847a5d16d192fd83ea1f5381a4f75c09b30

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
<<<<<<< HEAD
    path('token/', jwt_views.TokenObtainPairView.as_view(), name ='token_obtain_pair'),
    path('token/refresh/', jwt_views.TokenRefreshView.as_view(), name ='token_refresh'),
    path('logout/blacklist/', BlacklistTokenUpdateView.as_view(), name='blacklist'),
    path('post/sensor-node/', post_node_sensor, name="sensor-node")
]

=======
    path('token/', TokenObtainPairView.as_view(), name ='token_obtain_pair'),
    path('token/refresh/', TokenRefreshView.as_view(), name ='token_refresh')
]
>>>>>>> 817bf847a5d16d192fd83ea1f5381a4f75c09b30
