from haystack.views import SearchView
from .models import *


class MySeachView(SearchView):
    def extra_context(self):  # 重载extra_context来添加额外的context内容
        context = super(MySeachView, self).extra_context()
        contexts=self.results._result_cache
        for i in range(contexts.__len__()):
            if contexts[i]==None:
                break
        side_list = RenGongZhiNeng.objects.filter(content='content').order_by('id')[:8]
        self.num=i
        return context
