from django.shortcuts import get_object_or_404
import ipdb
from kmdb_app.models import Movie, Comment

class CommentServices():
    @staticmethod
    def get_comment_by_id(comment_id):
        return get_object_or_404(Comment, id=comment_id)
    
    @staticmethod
    def get_comment_by_movie(movie):
        comment = Comment.objects.filter(movie=movie)
        return comment

    @staticmethod
    def update_comment(comment_data):
        comment = CommentServices.get_comment_by_id(comment_data['comment_id'])
        comment.comment = comment_data['comment']
        comment.save()
        return comment
        

    @staticmethod
    def create_comment(comment_data, movie, user):
        return Comment.objects.create(comment=comment_data['comment'], movie=movie, user=user)
