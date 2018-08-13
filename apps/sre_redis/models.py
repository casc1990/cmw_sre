from django.db import models
from datetime import datetime
class Instance(models.Model):
    '''实例类'''
    ip = models.GenericIPAddressField(verbose_name=u'IP')
    port = models.IntegerField(default=3306,verbose_name=u'端口')
    max_memory = models.IntegerField(default=0,verbose_name=u'分配内存')
    create_time = models.DateTimeField(default=datetime.now,verbose_name=u'创建时间')
    update_time = models.DateTimeField(default=datetime.now,verbose_name=u'更新时间')

    class Meta:
        app_label = u'sre_redis'
        ordering = ['ip']
        db_table = 'instance'
        verbose_name = u'实例'
        verbose_name_plural = verbose_name

    def __unicode__(self):
        return self.ip
