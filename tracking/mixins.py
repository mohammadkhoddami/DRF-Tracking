from .base_mixins import BaseLoggingMixin
from .models import ApiRequestLog
class LoggingMixin(BaseLoggingMixin):
    def heandle_log(self):
        # ApiRequestLog(**self.log).save()
        print(self.log)