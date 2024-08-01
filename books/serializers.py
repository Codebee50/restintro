from rest_framework import serializers
from .models import Book

class BookSerializer(serializers.ModelSerializer):
    price = serializers.SerializerMethodField()
    intro = serializers.SerializerMethodField()
    
    class Meta: 
        model = Book
        fields = '__all__'
    
    
    def get_intro(self, obj):
        return f'Name {obj.name} written by {obj.author}'
        
    def get_price(self, obj):
        return int(obj.number_of_pages) * int(obj.number_of_chapters)