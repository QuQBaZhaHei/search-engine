from .models import RenGongZhiNeng,JiBingFangZhi,KeXueYuanLi,BaiDuCiTiao,ShengWuShengMing,ShiPingAnQuan,XinXiTongXin,YangShenBaoJian,ZiRanDiLi

from haystack import indexes


class ZiRanDiLiIndex(indexes.SearchIndex, indexes.Indexable):
   #类名必须为需要检索的Model_name+Index，这里需要检索RenGongZhiNeng，所以创建RenGongZhiNengIndex
   text = indexes.CharField(document=True, use_template=True)#创建一个text字段
   #其它字段
   title=indexes.CharField(model_attr='title')
   link = indexes.CharField(model_attr='link')
   content = indexes.CharField(model_attr='content')
   origin = indexes.CharField(model_attr='origin')
   date = indexes.CharField(model_attr='date')
   writer = indexes.CharField(model_attr='writer')

   def get_model(self):#重载get_model方法，必须要有！
       return ZiRanDiLi

   def index_queryset(self, using=None):
       return self.get_model().objects.all()

class YangShenBaoJianIndex(indexes.SearchIndex, indexes.Indexable):
   #类名必须为需要检索的Model_name+Index，这里需要检索RenGongZhiNeng，所以创建RenGongZhiNengIndex
   text = indexes.CharField(document=True, use_template=True)#创建一个text字段
   #其它字段
   title=indexes.CharField(model_attr='title')
   link = indexes.CharField(model_attr='link')
   content = indexes.CharField(model_attr='content')
   origin = indexes.CharField(model_attr='origin')
   date = indexes.CharField(model_attr='date')
   writer = indexes.CharField(model_attr='writer')

   def get_model(self):#重载get_model方法，必须要有！
       return YangShenBaoJian

   def index_queryset(self, using=None):
       return self.get_model().objects.all()


class RenGongZhiNengIndex(indexes.SearchIndex, indexes.Indexable):
   #类名必须为需要检索的Model_name+Index，这里需要检索RenGongZhiNeng，所以创建RenGongZhiNengIndex
   text = indexes.CharField(document=True, use_template=True)#创建一个text字段
   #其它字段
   title=indexes.CharField(model_attr='title')
   link = indexes.CharField(model_attr='link')
   content = indexes.CharField(model_attr='content')
   origin = indexes.CharField(model_attr='origin')
   date = indexes.CharField(model_attr='date')
   writer = indexes.CharField(model_attr='writer')

   def get_model(self):#重载get_model方法，必须要有！
       return RenGongZhiNeng

   def index_queryset(self, using=None):
       return self.get_model().objects.all()


class JiBingFangZhiIndex(indexes.SearchIndex, indexes.Indexable):
   #类名必须为需要检索的Model_name+Index，这里需要检索RenGongZhiNeng，所以创建RenGongZhiNengIndex
   text = indexes.CharField(document=True, use_template=True)#创建一个text字段
   #其它字段
   title=indexes.CharField(model_attr='title')
   link = indexes.CharField(model_attr='link')
   content = indexes.CharField(model_attr='content')
   origin = indexes.CharField(model_attr='origin')
   date = indexes.CharField(model_attr='date')
   writer = indexes.CharField(model_attr='writer')

   def get_model(self):#重载get_model方法，必须要有！
       return JiBingFangZhi

   def index_queryset(self, using=None):
       return self.get_model().objects.all()


class KeXueYuanLiIndex(indexes.SearchIndex, indexes.Indexable):
   #类名必须为需要检索的Model_name+Index，这里需要检索RenGongZhiNeng，所以创建RenGongZhiNengIndex
   text = indexes.CharField(document=True, use_template=True)#创建一个text字段
   #其它字段
   title=indexes.CharField(model_attr='title')
   link = indexes.CharField(model_attr='link')
   content = indexes.CharField(model_attr='content')
   origin = indexes.CharField(model_attr='origin')
   date = indexes.CharField(model_attr='date')
   writer = indexes.CharField(model_attr='writer')

   def get_model(self):#重载get_model方法，必须要有！
       return KeXueYuanLi

   def index_queryset(self, using=None):
       return self.get_model().objects.all()

class BaiDuCiTiaoIndex(indexes.SearchIndex, indexes.Indexable):
   #类名必须为需要检索的Model_name+Index，这里需要检索RenGongZhiNeng，所以创建RenGongZhiNengIndex
   text = indexes.CharField(document=True, use_template=True)#创建一个text字段
   #其它字段
   title=indexes.CharField(model_attr='title')
   link = indexes.CharField(model_attr='link')
   content = indexes.CharField(model_attr='content')
   origin = indexes.CharField(model_attr='origin')
   date = indexes.CharField(model_attr='date')
   writer = indexes.CharField(model_attr='writer')

   def get_model(self):#重载get_model方法，必须要有！
       return BaiDuCiTiao

   def index_queryset(self, using=None):
       return self.get_model().objects.all()


class ShengWuShengMingIndex(indexes.SearchIndex, indexes.Indexable):
   #类名必须为需要检索的Model_name+Index，这里需要检索RenGongZhiNeng，所以创建RenGongZhiNengIndex
   text = indexes.CharField(document=True, use_template=True)#创建一个text字段
   #其它字段
   title=indexes.CharField(model_attr='title')
   link = indexes.CharField(model_attr='link')
   content = indexes.CharField(model_attr='content')
   origin = indexes.CharField(model_attr='origin')
   date = indexes.CharField(model_attr='date')
   writer = indexes.CharField(model_attr='writer')

   def get_model(self):#重载get_model方法，必须要有！
       return ShengWuShengMing

   def index_queryset(self, using=None):
       return self.get_model().objects.all()


class ShiPingAnQuanIndex(indexes.SearchIndex, indexes.Indexable):
   #类名必须为需要检索的Model_name+Index，这里需要检索RenGongZhiNeng，所以创建RenGongZhiNengIndex
   text = indexes.CharField(document=True, use_template=True)#创建一个text字段
   #其它字段
   title=indexes.CharField(model_attr='title')
   link = indexes.CharField(model_attr='link')
   content = indexes.CharField(model_attr='content')
   origin = indexes.CharField(model_attr='origin')
   date = indexes.CharField(model_attr='date')
   writer = indexes.CharField(model_attr='writer')

   def get_model(self):#重载get_model方法，必须要有！
       return ShiPingAnQuan

   def index_queryset(self, using=None):
       return self.get_model().objects.all()


class XinXiTongXinIndex(indexes.SearchIndex, indexes.Indexable):
   #类名必须为需要检索的Model_name+Index，这里需要检索RenGongZhiNeng，所以创建RenGongZhiNengIndex
   text = indexes.CharField(document=True, use_template=True)#创建一个text字段
   #其它字段
   title=indexes.CharField(model_attr='title')
   link = indexes.CharField(model_attr='link')
   content = indexes.CharField(model_attr='content')
   origin = indexes.CharField(model_attr='origin')
   date = indexes.CharField(model_attr='date')
   writer = indexes.CharField(model_attr='writer')

   def get_model(self):#重载get_model方法，必须要有！
       return XinXiTongXin

   def index_queryset(self, using=None):
       return self.get_model().objects.all()

def search(keyword):
    return