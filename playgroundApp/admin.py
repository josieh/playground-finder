__author__ = 'hails'
from django.contrib import admin
from models import User, Playground, SchoolDistrict, Age, School, UserReview, SafetyFeatures, Features, TransportationFeatures
from django import forms

class UserAdmin(admin.ModelAdmin):
    search_fields = ('UserID',)
    fieldsets = (
        (None, {
            'fields': ('UserID', 'Name', 'Zipcode', 'Age', 'isWorkingMom',
                        'isWorkingDad', 'isStayMom', 'isStayDad', 'isGrandma',
                        'isOther', 'FavoritesID','swing')
        }),
        ('Advanced options', {
            'classes': ('collapse',),
            'fields': ()
        }),
    )
class PlaygroundAdmin(admin.ModelAdmin):
    search_fields = ('PlaygroundID',)
    fieldsets = (
        (None, {
            'fields': ('playgroundID', 'name', 'street', 'zipcode', 'handicap',
            'schoolDistrictID', 'hours', 'image', 'latLon')
        }),
    )
class SchoolDistrictAdmin(admin.ModelAdmin):
    search_fields = ('SchoolDistrictID',)
    fieldsets = (
        (None, {
            'fields': ('SchoolDistrictID', 'DistrictName', 'ZipcodeStart', 'ZipcodeEnd',
            'GeoCoordinates')
        }),
    )
class AgeAdmin(admin.ModelAdmin):
    search_fields = ('AgeID',)
    fieldsets = (
        (None, {
            'fields': ('AgeID', 'ZeroTwo', 'TwoFour', 'FourSix', 'SixEight', 'EightTen',
            'TenTwelve', 'TwelveFourteen')
        }),
    )
class SchoolAdmin(admin.ModelAdmin):
    search_fields = ('SchoolID',)
    fieldsets = (
        (None, {
            'fields': ('SchoolID', 'Name', 'SchoolDistrictID')
        }),
    )
class UserReviewAdmin(admin.ModelAdmin):
    search_fields = ('ReviewID',)
    fieldsets = (
        (None, {
            'fields': ('ReviewID', 'PlaygroundID', 'UserID', 'Stars', 'Review')
        }),
    )
class SafetyFeaturesAdmin(admin.ModelAdmin):
    search_fields = ('PlaygroundID',)
    fieldsets = (
        (None, {
           'fields': ('PlaygroundID', 'ProximityToHighway', 'Fenced')
        }),
    )
class TransportationFeaturesAdmin(admin.ModelAdmin):
    search_fields = ('PlaygroundID',)
    fieldsets = (
        (None, {
            'fields': ('PlaygroundID', 'BikePath', 'HikingTrail', 'AdjacentParking',
            'NearbyParking', 'NoParking', 'ProximityToBus')
        }),
    )
class FeaturesAdmin(admin.ModelAdmin):
    search_fields = ('PlaygroundID',)
    fieldsets = (
        (None, {
           'fields': ('PlaygroundID', 'Swing', 'Slide', 'MonkeyBars', 'SandBox', 'Field',
           'PicnicTable', 'Bathrooms', 'ChangingStation', 'Shade', 'BasketballCourt',
           'Baseball')
        }),
    )

admin.site.register(User, UserAdmin)
admin.site.register(Playground, PlaygroundAdmin)
admin.site.register(SchoolDistrict, SchoolDistrictAdmin)
admin.site.register(Age, AgeAdmin)
admin.site.register(School, SchoolAdmin)
admin.site.register(UserReview, UserReviewAdmin)
admin.site.register(SafetyFeatures, SafetyFeaturesAdmin)
admin.site.register(Features, FeaturesAdmin)
admin.site.register(TransportationFeatures, TransportationFeaturesAdmin)