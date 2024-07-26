#### **Python**
Самые популярные фреймворки для реализации HTTP API на языке Python - это Flask и Django.

Flask - микрофреймворк для создания приложений и REST API. Главная задача Flask - обрабатывать HTTP запросы и перенаправлять их на необходимую функцию в приложении. Приведем пример Flask приложения для REST API.

```python
# app.py
from flask import Flask, request, jsonify

app = Flask(__name__)

models = [
    { "id": 1, "exampleModelAttr": "attr1" },
    { "id": 2, "exampleModelAttr": "attr2" }
]

@app.get("/models")
def get_models():
    return jsonify(countries)

@app.post("/models")
def add_model():
    if not request.is_json:
        return { "error": "Request must be a json" }, 415
    model = request.get_json()
    model["id"] = new_id()
    models.append(model)
    return model, 201
```

Теперь посмотрим на Django - ещё один популярный фреймворк для создания REST API приложения.

Изначально требуется создать Django проект, затем добавить в settings.py используемые модули.

```python
# examplemodelsapi/settings.py
INSTALLED_APPS = [
    "django.contrib.admin",
    "django.contrib.auth",
    "django.contrib.contenttypes",
    "django.contrib.sessions",
    "django.contrib.messages",
    "django.contrib.staticfiles",
    "rest_framework",
    "countries",
]
```

Добавляем модели.

```python
# examplemodels/models.py
from django.db import models

class ExampleModel(models.Model):
    id = models.IntegerField()
    exampleModelAttr = model.CharField(max_length=100)
```

Не забываем накатывать миграции: `python manage.py makemigrations`, `python manage.py migrate`.

Пишем сериализаторы.

```python
# examplemodels/serializers.py
from rest_framework import serializers
from .models import ExampleModel

class ExampleModelSerializer(serializers.ModelSerializer):
    class Meta:
        model = ExampleModel
        fields = ["id", "exampleModelAttr"]
```

Добавим код представления (то, чего мы не делали в прошлых языках). Этот класс генерирует представления, необходимые для управления данными класса ExampleModel.

```python
from rest_framework import viewsets

from .models import ExampleModel
from .serializers import ExampleModelSerializer

class ExampleModelViewSet(viewsets.ModelViewSet):
    serializer_class = ExampleModelSerializer
    queryset = ExampleModel.objects.all()
```

Теперь обновим urls.py

```python
# examplemodels/urls.py
from django.urls import path, include
from rest_framework.routers import DefaultRouter

from .views import ExampleModelViewSet

router = DefaultRouter()
router.register(r"models", ExampleModelViewSet)

urlpatterns = [
    path("", include(router.urls))
]
```

```python
# examplemodelsapi/urls.py
from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path("admin/", admin.site.urls),
    path("", include("examplemodels.urls")),
]
```

Ура! Можно запускать: `python manage.py runserver`.