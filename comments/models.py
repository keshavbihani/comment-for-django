from django.db import models
from django.conf import settings

from django.contrib.contenttypes.fields import GenericForeignKey
from django.contrib.contenttypes.models import ContentType

from django.contrib.contenttypes.models import ContentType

class CommentManager(models.Manager):
	def get_comments(self,queryset):
		contenttype=ContentType.objects.get_for_model(queryset.__class__)
		#print(contenttype)
		obj_id=queryset.id
		comments=super(CommentManager,self).filter(content_type=contenttype,object_id=obj_id)

		return comments
# Create your models here.
class Comment(models.Model):
	user = models.ForeignKey(settings.AUTH_USER_MODEL, default=1)
	#generic relation
	content_type = models.ForeignKey(ContentType, on_delete=models.CASCADE)
	object_id = models.PositiveIntegerField()
	content_object = GenericForeignKey('content_type', 'object_id')
	parent = models.ForeignKey("self",null=True,blank=True)
	content = models.TextField()
	publish = models.DateField(auto_now_add=True)


	objects=CommentManager()
	

	def __unicode__(self):
		return self.user.username

	def __str__(self):
		return self.user.username


		