# !/usr/bin/python3
# -*-coding:utf8-*-
from django.db import models
from django.utils.datetime_safe import datetime


class Community(models.Model):
    comm_type_choices = (
        (0, "创新创业类"),
        (1, "思想政治类"),
        (2, "体育竞技类"),
        (3, "文化艺术类"),
        (4, "学术科学类"),
        (5, "志愿公益类"),
    )
    community_type = models.IntegerField(choices=comm_type_choices, default=3, verbose_name="社团类型")
    name = models.CharField(max_length=15, default=None, null=True, blank=True, verbose_name="社团名称")


class Activity(models.Model):
    is_conventional_choices = (
        (0, "常规活动"),
        (1, "非常规活动")
    )
    act_type_choices = (
        (0, "教学培训, 研讨学习"),
        (1, "志愿公益, 社会实践"),
        (2, "内部建设")
    )
    act_area_choices = (
        (0, "品学楼, 立人楼"),
        (1, "图书馆, 时间广场"),
        (2, "学生活动中心, 成电会堂"),
        (3, "体育场, 体育馆"),
        (4, "校内其他场地"),
        (5, "校外"),
    )
    community = models.ForeignKey(Community, default=None, null=True, on_delete=models.SET_NULL, verbose_name="社团名称")
    name = models.CharField(max_length=20, default=None, null=True, blank=True, verbose_name="活动名称")
    is_conventional = models.IntegerField(default=0, choices=is_conventional_choices, verbose_name="是否常规")
    act_type = models.IntegerField(default=1, choices=act_type_choices, verbose_name="活动类型")
    act_area = models.IntegerField(default=0, choices=act_area_choices, verbose_name="活动地点")
    datetime = models.DateTimeField(default=datetime.now, verbose_name="活动日期")


class ActivityTime(models.Model):
    time_choices = (
        (0, "一～二节课(8:30~10:20)"),
        (1, "三～四节课(10:20～12:00)"),
        (2, "中午(12:00～14:30)"),
        (3, "五～六节课(14:30～16:20)"),
        (4, "七～八节课(16:20～18:00)"),
        (5, "18:00～19:30"),
        (6, "九～十节课(19:30～21:00)"),
        (7, "十～十一节课(20:20～22:00)"),
        (8, "十一节课后(22:00～23:00)"),
    )
    duration = models.IntegerField(default=2, choices=time_choices, verbose_name="活动时间")
    activity = models.ForeignKey(Activity, default=None, null=True, on_delete=models.SET_NULL, verbose_name="活动名称")
