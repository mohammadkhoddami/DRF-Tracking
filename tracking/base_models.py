from django.db import models
from django.conf import settings
from django.contrib.auth import get_user_model

class BaseApiRequestLog(models.Model):
    user = models.ForeignKey(get_user_model(), on_delete=models.SET_NULL, null=True, blank=True)
    username_persistent = models.CharField(max_length=getattr(settings, 'DRF_TRACKING_USERNAME_LEN', 200), null=True, blank=True)
    datetime_requested_at = models.DateTimeField(db_index=True)
    response_ms = models.PositiveIntegerField(default=0)
    path = models.CharField(max_length=getattr(settings, 'DRF_TRACKING_PATH_LEN', 200), db_index=True)
    view = models.CharField(max_length=getattr(settings, 'DRF_TRACKING_View_LEN', 200), null=True, blank=True, db_index=True)
    view_method = models.CharField(max_length=getattr(settings, 'DRF_TRACKING_VIEW_METHOD_LEN', 200), null=True, blank=True, db_index=True)
    remote_address = models.GenericIPAddressField()
    host = models.URLField()
    method = models.CharField(max_length=10)
    query_params = models.TextField(null=True, blank=True)
    data = models.TextField(null=True, blank=True)
    response = models.TextField(null=True, blank=True)
    errors = models.TextField(null=True, blank=True)
    status_code = models.PositiveIntegerField(null=True, blank=True, db_index=True)
    
    class Meta:
        abstract=True
        verbose_name = 'API Reuqest Log'
        
    def __str__(self):
        return f'{self.method} {self.path}'