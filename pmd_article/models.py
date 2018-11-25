from django.db import models

# Create your models here.
class ArticleInfo(models.Model):
    """
    博客文章的模型类
    包括标题、内容、总字数、创建日期、最后修改日期、是否删除
    """
    a_title = models.CharField(max_length=30)
    a_content = models.TextField()
    a_word_count = models.CharField(max_length=10, null=True, blank=True)
    a_ct_time = models.DateTimeField(auto_created=True)
    a_ch_time = models.DateTimeField(auto_now=True)
    a_is_delete = models.BooleanField(default=False)

    def __str__(self):
        return self.a_title


class ImageInfo(models.Model):
    """
    博客文章内的图片
    包括图片、所属文章
    """
    i_name = models.CharField(max_length=10, default="一张图片")
    i_image = models.CharField(max_length=30, default="null")
    i_is_delete = models.BooleanField(default=False)
    i_article = models.ForeignKey(ArticleInfo, on_delete=models.CASCADE)