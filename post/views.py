from django.shortcuts import render
from django.shortcuts import render, get_object_or_404
from django.http import HttpResponseRedirect
from comments.models import Comment
from django.contrib.contenttypes.models import ContentType
from comments.forms import CommentForm
from .models import Posts
from datetime import datetime
# Create your views here.

def postList(request):
	queryset=Posts.objects.all().order_by("-timestamp")
	context={
	"title":"List",
	"data":queryset
	}
	return render(request, "post_list.html", context)


def postDetail(request,id):
	queryset=Posts.objects.filter(id=id)
	query1=	queryset.first()
	#comment line
	contenttype=ContentType.objects.get_for_model(query1.__class__)
	initial_data ={
	"content_type": contenttype,
	"object_id":query1.id
	}
	#print(query1.__class__.__name__)
	#print(query1.id)
	comment_form = CommentForm(request.POST or None, initial=initial_data)
	if comment_form.is_valid():
		content_type=ContentType.objects.get_for_model(query1.__class__)
		object_id=comment_form.cleaned_data.get("object_id")
		content_data=comment_form.cleaned_data.get("content")
		parent_id=request.POST.get('parent_id')
		if parent_id:
			parent_obj = Comment.objects.get(id=int(parent_id))
		else:
			parent_obj=None
		#print(parent_obj.content)	
		new_comment,created=Comment.objects.get_or_create(
									user=request.user,
									content_type=content_type,
									object_id=object_id,
									content=str(content_data),
									parent=parent_obj
									)
		return HttpResponseRedirect(request.path_info)
	print(datetime.now())	
	comments=Comment.objects.get_comments(query1).order_by("-publish")
	context={
	"title":"Details",
	"post":query1,
	#add to context
	"comments":comments,
	"comment_form":comment_form
	#"datetime":datetime.now()
	}
	return render(request, "post_detail.html", context)