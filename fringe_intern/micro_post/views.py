import json
import uuid
from collections import OrderedDict
from django.http import HttpResponse
from django.views.decorators.csrf import csrf_exempt
from django.core.exceptions import ValidationError
from .models import User, Post


def render_json_response(request, data, status=None):
    """response を JSON で返却"""
    json_str = json.dumps(data, ensure_ascii=False, indent=2)
    callback = request.GET.get('callback')
    if not callback:
        callback = request.POST.get('callback')
    if callback:
        json_str = "%s(%s)" % (callback, json_str)
        response = HttpResponse(json_str, content_type='application/javascript; charset=UTF-8', status=status)
    else:
        response = HttpResponse(json_str, content_type='application/json; charset=UTF-8', status=status)
    return response

def post_list_to_json(objects, key):
    """ポストオブジェクトを JSON に変換"""
    posts = []
    for post in objects:
        if post.parent_post_id is None:
            post_dict = OrderedDict([
                ('id', str(post.id)),
                ('user_id', str(post.user_id.id)),
                ('text', post.text),
                ('comment_count', post.comment_count),
                ('posted_at', str(post.posted_at))
            ])
        else:
            post_dict = OrderedDict([
                ('id', str(post.id)),
                ('user_id', str(post.user_id.id)),
                ('text', post.text),
                ('parent_post_id', str(post.parent_post_id.id)),
                ('comment_count', post.comment_count),
                ('posted_at', str(post.posted_at))
            ])
        posts.append(post_dict)

    return OrderedDict([(key, posts)])

def insert_post(user_id, text, parent_post_id=None):
    """ポストをDBにインサート"""
    user_id = uuid.UUID(user_id)
    if parent_post_id is None:
        post = Post(user_id=User(id=user_id), text=text)
        post.full_clean()
        post.save()
    else:
        parent_post = Post.objects.get(id=uuid.UUID(parent_post_id))
        post = Post(user_id=User(id=user_id), text=text, parent_post_id=parent_post)
        post.full_clean()
        post.save()
        parent_post.comment_count += 1
        parent_post.save()

def post_list(request):
    """全てのポストを JSON で返す"""
    data = post_list_to_json(Post.objects.all(), "posts")
    return render_json_response(request, data)

@csrf_exempt
def post_create(request):
    """ポストを保存する"""
    try:
        param_json = json.loads(request.body)
        user_id = param_json['user_id']
        text = param_json['text']
        insert_post(user_id, text)
        return render_json_response(request, {"result": "OK"})
    except ValidationError as e:
        return render_json_response(request, {"result": "NG", "message": e.message_dict}, 400)
    except ValueError as e:
        return render_json_response(request, {"result": "NG", "message": str(e)}, 400)

def comment_list(request, post_id):
    """あるポストの全てのコメントを JSON で返す"""
    data = post_list_to_json(Post.objects.filter(parent_post_id=post_id), "comments")
    return render_json_response(request, data)

@csrf_exempt
def comment_create(request, post_id):
    """指定されたポストのコメントを保存する"""
    try:
        param_json = json.loads(request.body)
        user_id = param_json['user_id']
        text = param_json['text']
        insert_post(user_id, text, post_id)
        return render_json_response(request, {"result": "OK"})
    except ValidationError as e:
        return render_json_response(request, {"result": "NG", "message": e.message_dict}, 400)
    except ValueError as e:
        return render_json_response(request, {"result": "NG", "message": str(e)}, 400)
