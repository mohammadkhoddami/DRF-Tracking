from django.contrib import admin
from .models import ApiRequestLog
# Register your models here.
@admin.register(ApiRequestLog)
class ApiRequestLogAdmin(admin.ModelAdmin):
    list_display = ('id', 'datetime_requested_at', 'response_ms', 'status_code',
                    'user', 'method',
                    'path', 'remote_address', 'host',
                    'query_params'
                    )