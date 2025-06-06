from django.urls import path

from . import views

urlpatterns = [
    path("login", views.CustomLoginView.as_view(), name="login"),
    path("signup", views.SignUpView.as_view(), name="signup"),
    path("signup_auth/<int:pk>", views.SignUpAuthView.as_view(), name="signup_auth"),
    path(
        "signup_auth/<int:pk>/resend",
        views.SignupResendEmailView.as_view(),
        name="signup_resend",
    ),
    path("signup_done/<int:pk>", views.SignUpDoneView.as_view(), name="signup_done"),
    path(
        "password_reset", views.CustomPasswordResetView.as_view(), name="password_reset"
    ),
    path(
        "password_reset/done",
        views.CustomPasswordResetDoneView.as_view(),
        name="password_reset_done",
    ),
    path(
        "password_reset/<uidb64>/<token>",
        views.CustomPasswordResetConfirmView.as_view(),
        name="password_reset_confirm",
    ),
    path(
        "password_reset/complete",
        views.CustomPasswordResetCompleteView.as_view(),
        name="password_reset_complete",
    ),
    path("", views.index, name="index"),
    path("profile/<str:username>/", views.profile, name="profile"),
    path("home_profile/<str:username>/", views.home_profile, name="home_profile"),
    path("user_settings/<str:username>/", views.user_settings, name="user_settings"),
    path("edit_profile/<str:username>", views.edit_profile, name="edit_profile"),
    path("home/", views.home_view, name="home"),
    path(
        "product_description/<int:product_id>/",
        views.product_description,
        name="product_description",
    ),
    path("edit_profile/<str:username>/", views.edit_profile, name="edit_profile"),
    path("edit_address/<str:username>/", views.edit_address, name="edit_address"),
    path("delete_profile/<str:username>/", views.delete_profile, name="delete_profile"),
    path("delete_confirm/", views.delete_confirm, name="delete_confirm"),
    path("liked_products/<str:username>/", views.liked_products, name="liked_products"),
    path(
        "bought_products/<str:username>", views.bought_products, name="bought_products"
    ),
    path(
        "payment_information/<str:username>/",
        views.payment_information,
        name="payment_information",
    ),
    path("create_card/<str:username>/", views.create_card, name="create_card"),
    path("payment/<str:username>/<int:product_id>/", views.payment, name="payment"),
    path("payment_post/", views.payment_post, name="payment_post"),
    path("payment_compelete/<str:username>/<int:product_id>/", views.payment_complete, name="payment_complete"),
    path("thanks/", views.thanks, name="thanks"),
    path(
        "exhibited_products/<str:username>/",
        views.exhibited_products,
        name="exhibited_products",
    ),
    path("payment_information/", views.payment_information, name="payment_information"),
    path("create_card/", views.create_card, name="create-card-information"),
    path("privacy_policy/<str:username>/", views.privacy_policy, name="privacy_policy"),
    path("rules/<str:username>/", views.rules, name="rules"),
    path(
        "all_product_profile/<str:username>",
        views.all_product_profile,
        name="all_product_profile",
    ),
    path("like_product/", views.like_product, name="like_product"),
    path("sell/", views.sell, name="sell"),
    path("temporary/", views.temporary, name="temporary"),
    path("logout/", views.LogoutView.as_view(), name="logout"),
]
