import xadmin
from .models import Instance

class InstanceAdmin(object):
    list_display = ['ip', 'port', 'max_memory', 'create_time', 'update_time']
    search_fields = ['ip', 'port', 'max_memory', 'create_time']
    list_filter = ['ip', 'port', 'max_memory', 'create_time']


xadmin.site.register(Instance,InstanceAdmin)