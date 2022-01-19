from django.contrib import admin
from django.urls import path
import tasks.views


urlpatterns = [
    path("admin/", admin.site.urls),
    path("tasks/", tasks.views.tasks_view),
    path("tasks/add-task/", tasks.views.add_task_view),
    path("tasks/delete-task/<int:task_index>", tasks.views.delete_task_view),
    path("tasks/complete-task/<int:task_index>", tasks.views.complete_task_view),
    path("completed/", tasks.views.completed_task_view),
]
