from rest_framework.views import APIView
from django.utils import timezone
from ipaddress import ip_address as ip_addr


class BaseLoggingMixin:
    def initial(self, request, *args, **kwargs):
        self.log = {'datetime_requested_at': timezone.now()}
        return super().initial(request, *args, **kwargs)
    
    
    def finalize_response(self, request, response, *args, **kwargs):
        response = super().finalize_response(request, response, *args, **kwargs)
        self.log.update({
            'remote_address': self._get_ip_address(request)
        })
        self.handle_log()
        return response
    
    def handle_log(self):
        raise NotImplementedError

    def _get_ip_address(self, request):
        ip_address = request.META.get('HTTP_X_FORWARDED_FOR', None)
        if ip_address:
            ip_address = ip_address.split(',')[0]
        else:
            ip_address = request.META.get('REMOTE_ADDR', '').split(',')[0]
            
        possibles = (ip_address.lstrip('[').split(']')[0],
                     ip_address.split(':')[0])
        
        for address in possibles:
            try:
                return str(ip_addr(address))
            except:
                pass
        return ip_address