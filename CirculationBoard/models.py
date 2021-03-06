from django.db import models


class CirculationBoard(models.Model):
    # タイトル
    title = models.CharField('Title', max_length=200)
    # 開始日
    start_date = models.DateField('Start Date')
    # 回収日
    end_date = models.DateField('End Date', null=True, blank=True)

    def __str__(self):
        return self.title
