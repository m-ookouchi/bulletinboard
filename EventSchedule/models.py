from django.db import models

class EventSchedule(models.Model):
    # イベント名
    event_name = models.CharField('Event Name', max_length=100)
    # 場所(集合場所)
    place = models.CharField('Place', max_length=100)
    # 対象者
    target_person = models.CharField('Target', max_length=100, null=True, blank=True)
    # 詳細情報
    detail_info = models.TextField('Detail', max_length=1000, null=True, blank=True)
    # 予定日
    schedule_daytime = models.DateTimeField('Schedule')
    # 予備日
    preparation_daytime = models.DateTimeField('Preparation', null=True, blank=True)
    # 実施日
    implementation_datetime = models.DateTimeField('Implemantation', null=True, blank=True)
    # 備考
    remarks = models.TextField('Remark', max_length=1000, null=True, blank=True)

    def __str__(self):
        return self.event_name