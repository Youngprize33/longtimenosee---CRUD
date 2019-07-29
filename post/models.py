from django.db import models

# Create your models here.
class Post(models.Model):
    title = models.CharField(max_length=50)
    body = models.TextField()
    pub_date = models.DateTimeField("data published")
    image = models.ImageField(upload_to='images/', blank=True)

    def __str__(self):
        return self.title

class Comment(models.Model):
    post = models.ForeignKey(Post, on_delete=models.CASCADE) #기본키와 ForeignKey 의 차이를 알아야 한다. 기본키는 고유하지만 Foreignkey 는 참조용으로 쓸 수 있다. pk(기본키)는 주민등록번호나 학수번호와 같은 느낌. post같은 경우 id가 기본키가 된다. foreignkey는  불필요한 정보를 삭제하기 위해서 학수번호의 정보만 찾게 해주는 키 (단순하게 만드는 키?) 
    #post의 글이 삭제되면 댓글들도 자동삭제 시키기 위해서 on_delete=models.CASCADE
    username = models.CharField(max_length=50)
    body = models.TextField()
    pub_date = models.DateTimeField("date published")

    def __str__(self):
        return self.body