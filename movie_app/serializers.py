from django.db.models import Avg
from rest_framework import serializers
from .models import Director, Movie, Review

class DirectorSerializer(serializers.ModelSerializer):
    class Meta:
        model = Director
        fields = '__all__'

    def to_representation(self, instance):
        rep = super().to_representation(instance)
        rep['movies_count'] = instance.movie_set.count()
        return rep


class ReviewSerializer(serializers.ModelSerializer):

    def to_representation(self, instance):
        rep = super().to_representation(instance)
        rep['movie'] = instance.movie.title

        return rep
    class Meta:
        model = Review
        fields = '__all__'


class MovieSerializer(serializers.ModelSerializer):
    reviews = ReviewSerializer(many=True, read_only=True)

    class Meta:
        model = Movie
        fields = '__all__'

    def to_representation(self, instance):
        rep = super().to_representation(instance)

        rep['director'] = instance.director.name
        rep['reviews_count'] = instance.review_set.count()
        rep['average_rating'] = instance.review_set.aggregate(Avg('stars'))['stars__avg']
        rep['reviews'] = [{'text': review.text, 'stars': review.stars} for review in instance.review_set.all()]

        return rep