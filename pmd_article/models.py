from django.db import models

# Create your models here.
class ArticleInfo(models.Model):
    """
    博客文章的模型类
    包括标题、内容、总字数、背景图片、创建日期、最后修改日期、是否删除
    """
    pa_title = models.CharField(max_length=30)
    pa_content = models.TextField()
    pa_background = models.ImageField(null=True)
    pa_word_count = models.IntegerField()
    pa_ct_time = models.DateTimeField(auto_created=True)
    pa_ch_time = models.DateTimeField(auto_now=True)
    pa_is_delete = models.BooleanField(default=False)
