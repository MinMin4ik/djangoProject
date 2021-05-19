"""djangoProject URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URL conf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin
from django.contrib.staticfiles.urls import staticfiles_urlpatterns
from django.urls import path, include
from django.views.decorators.csrf import csrf_exempt
from django.views.generic import RedirectView
from rest_framework_simplejwt import views as jwt_views

urlpatterns = [
                  path('admin/', admin.site.urls),
                  path('api/', include('api.rest_shop.urls')),
                  path('graphql/', csrf_exempt(GraphQLView.as_view(graphiql=True))),
                  path('', include('shop.urls')),
                  path('', include('social_django.urls', namespace='social')),
                  path('api/token/', jwt_views.TokenObtainPairView.as_view(), name='token_obtain_pair'),
                  path('api/token/refresh/', jwt_views.TokenRefreshView.as_view(), name='token_refresh'),
                  path('favicon.ico', RedirectView.as_view(url='/static/img/favicon.ico')),
                  # media connecting
              ] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT) + \
              staticfiles_urlpatterns()
# debug toolbar
if settings.DEBUG:
    # by default type is text-plain, thus browser reject working with
    import mimetypes

    mimetypes.add_type("application/javascript", ".js", True)
    import debug_toolbar

    urlpatterns.append(path('__debug__/', include(debug_toolbar.urls)))

# end debug toolbar
