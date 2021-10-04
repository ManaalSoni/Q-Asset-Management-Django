from .views import AssetRequestByUser, AssetView, CreateAssetRequestView, RegisterAPI, UserAPIView, LoginAPIView,AllUsersView
from django.urls import path, include
from knox import views as knox_views
from AssetManagement import views

urlpatterns = [
    path('register/', RegisterAPI.as_view()),
    path('login/', LoginAPIView.as_view()),
    path('user/', UserAPIView.as_view()),
    path('logout/', knox_views.LogoutView.as_view(), name='knox_logout'),
    
    path('assets/', views.AssetsView.as_view()),
    path('assets/<int:id>/',views.AssetView.as_view()),
    path('assetRequests/', views.AssetRequestView.as_view()),
    path('createAssetRequest/', views.CreateAssetRequestView.as_view()),
    path('assetRequests/<uuid:requestId>/', views.ApproveAssetRequest.as_view()),
    path('assetRequests/<int:employeeId>/', views.AssetRequestByUser.as_view()),
    path('allUsers/', views.AllUsersView.as_view()),
    path('activateUser/<int:id>/', views.ActivateUser.as_view()),
] 