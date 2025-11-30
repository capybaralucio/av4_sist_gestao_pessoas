from rest_framework import routers
from django.urls import path, include
from .views import ProjetoViewSet, TarefaViewSet

router = routers.DefaultRouter()
router.register(r'projetos', ProjetoViewSet)
router.register(r'tarefas', TarefaViewSet)

urlpatterns = [
    path('', include(router.urls)),
]
