# -*- coding:utf-8 -*-
# This is an auto-generated Django model module.
# You'll have to do the following manually to clean this up:
#   * Rearrange models' order
#   * Make sure each model has one field with primary_key=True
#   * Make sure each ForeignKey has `on_delete` set to the desired behavior.
#   * Remove `managed = False` lines if you wish to allow Django to create, modify, and delete the table
# Feel free to rename the models, but don't rename db_table values or field names.
from django.db import models


class RenGongZhiNeng(models.Model):
    title = models.CharField(max_length=50)
    link = models.CharField(max_length=255)
    content = models.TextField()
    origin = models.CharField(max_length=35, blank=True, null=True)
    date = models.CharField(max_length=35, blank=True, null=True)
    writer = models.CharField(max_length=20, blank=True, null=True)
    type = models.CharField(max_length=20, blank=True, null=True)

    class Meta:
        managed = True
        db_table = '人工智能'


class XinXiTongXin(models.Model):
    title = models.CharField(max_length=50)
    link = models.CharField(max_length=255)
    content = models.TextField()
    origin = models.CharField(max_length=35, blank=True, null=True)
    date = models.CharField(max_length=35, blank=True, null=True)
    writer = models.CharField(max_length=50, blank=True, null=True)
    type = models.CharField(max_length=20, blank=True, null=True)

    class Meta:
        managed = True
        db_table = '信息通信'


class YangShenBaoJian(models.Model):
    title = models.CharField(max_length=50)
    link = models.CharField(max_length=255)
    content = models.TextField()
    origin = models.CharField(max_length=35, blank=True, null=True)
    date = models.CharField(max_length=35, blank=True, null=True)
    writer = models.CharField(max_length=20, blank=True, null=True)
    type = models.CharField(max_length=20, blank=True, null=True)

    class Meta:
        managed = True
        db_table = '养身保健'


class ShengWuShengMing(models.Model):
    title = models.CharField(max_length=50)
    link = models.CharField(max_length=255)
    content = models.TextField()
    origin = models.CharField(max_length=35, blank=True, null=True)
    date = models.CharField(max_length=35, blank=True, null=True)
    writer = models.CharField(max_length=20, blank=True, null=True)
    type = models.CharField(max_length=20, blank=True, null=True)

    class Meta:
        managed = True
        db_table = '生物生命'


class JiBingFangZhi(models.Model):
    title = models.CharField(max_length=50)
    link = models.CharField(max_length=255)
    content = models.TextField()
    origin = models.CharField(max_length=35, blank=True, null=True)
    date = models.CharField(max_length=35, blank=True, null=True)
    writer = models.CharField(max_length=50, blank=True, null=True)
    type = models.CharField(max_length=20, blank=True, null=True)

    class Meta:
        managed = True
        db_table = '疾病防治'


class BaiDuCiTiao(models.Model):
    title = models.CharField(max_length=50)
    link = models.CharField(max_length=255)
    content = models.TextField()
    origin = models.CharField(max_length=35, blank=True, null=True)
    date = models.CharField(max_length=35, blank=True, null=True)
    writer = models.CharField(max_length=20, blank=True, null=True)
    type = models.CharField(max_length=20, blank=True, null=True)

    class Meta:
        managed = True
        db_table = '百度词条'


class KeXueYuanLi(models.Model):
    title = models.CharField(max_length=50)
    link = models.CharField(max_length=255)
    content = models.TextField()
    origin = models.CharField(max_length=35, blank=True, null=True)
    date = models.CharField(max_length=35, blank=True, null=True)
    writer = models.CharField(max_length=20, blank=True, null=True)
    type = models.CharField(max_length=20, blank=True, null=True)

    class Meta:
        managed = True
        db_table = '科学原理'


class ZiRanDiLi(models.Model):
    title = models.CharField(max_length=50)
    link = models.CharField(max_length=255)
    content = models.TextField()
    origin = models.CharField(max_length=35, blank=True, null=True)
    date = models.CharField(max_length=35, blank=True, null=True)
    writer = models.CharField(max_length=20, blank=True, null=True)
    type = models.CharField(max_length=20, blank=True, null=True)

    class Meta:
        managed = True
        db_table = '自然地理'


class ShiPingAnQuan(models.Model):
    title = models.CharField(max_length=50)
    link = models.CharField(max_length=255)
    content = models.TextField()
    origin = models.CharField(max_length=35, blank=True, null=True)
    date = models.CharField(max_length=35, blank=True, null=True)
    writer = models.CharField(max_length=50, blank=True, null=True)
    type = models.CharField(max_length=20, blank=True, null=True)

    class Meta:
        managed = True
        db_table = '食品安全'
