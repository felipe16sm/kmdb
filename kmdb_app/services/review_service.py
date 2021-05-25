from django.shortcuts import get_object_or_404
import ipdb
from kmdb_app.models import Movie, Review

class ReviewServices():
    @staticmethod
    def get_review_by_id(review_id):
        return get_object_or_404(Review, id=review_id)
    
    @staticmethod
    def get_reviews_by_movie(movie):
        review = Review.objects.filter(movie=movie)
        return review

    # @staticmethod
    # def update_comment(comment_data):
    #     comment = ReviewServices.get_review_by_id(comment_data['comment_id'])
    #     comment.comment = comment_data['comment']
    #     comment.save()
    #     return comment


    # @staticmethod
    # def create_review(comment_data, movie, user):
    #     return Comment.objects.create(comment=comment_data['comment'], movie=movie, user=user)
