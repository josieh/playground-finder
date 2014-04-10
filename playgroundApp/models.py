from django.db import models

# Create your models here.
class User(models.Model):
    UserID = models.CharField(unique=True, null=False, max_length=200)
    Name = models.CharField(null=False, max_length=200)
    Description = models.TextField()
    Zipcode = models.IntegerField(null=True)
    Age = models.IntegerField(null= True)
    isMom = models.BooleanField()
    isDad = models.BooleanField()
    isGrandparent = models.BooleanField()
    isOther = models.BooleanField()
    FavoritesID = models.IntegerField(null=True)
    Image = models.TextField()

    class Meta(object):
        verbose_name_plural = "Users"
        #ordering = ('userID',)
    def __unicode__(self):
        return unicode(self.UserID)
    def save(self, *args, **kwargs):
        self.UserID = self.UserID.upper()
        super(User, self).save(*args, **kwargs)
        
class FavoritePlaygroundLookup(models.Model):
    UserID = models.CharField(unique=True, null=False, max_length=200)
    PlaygroundID = models.IntegerField(unique=True, null=False)
    
    class Meta(object):
        verbose_name_plural = "Favorites"
        #ordering = ('userID',)
    def __unicode__(self):
        return unicode(self.UserID)
    def save(self, *args, **kwargs):
        self.UserID = self.UserID.upper()
        super(User, self).save(*args, **kwargs)
        
class Playground(models.Model):
    PlaygroundID = models.IntegerField(unique=True, null=False)
    Name = models.TextField()
    Street = models.TextField()
    Zipcode = models.IntegerField()
    Handicap = models.BooleanField()
    AgeID = models.IntegerField()
    SchoolDistrictID = models.IntegerField()
    Hours = models.TextField()
    isCertified = models.BooleanField()
    FeaturesID = models.IntegerField()
    Image = models.TextField()
    SafetyFeaturesID = models.IntegerField()
    TransportFeaturesID = models.IntegerField()
    GeoCoordinateLat = models.DecimalField(max_digits=12, decimal_places =10)
    GeoCoordinateLon = models.DecimalField(max_digits=12, decimal_places =10)

    class Meta(object):
        verbose_name_plural = "Playgrounds"
        #ordering = ('UserID',)
    def __unicode__(self):
        return unicode(self.PlaygroundID)
    def save(self, *args, **kwargs):
        super(Playground, self).save(*args, **kwargs)

class SchoolDistrict(models.Model):
    SchoolDistrictID = models.IntegerField(unique=True, null=False)
    DistrictName = models.TextField()
    ZipcodeStart = models.IntegerField()
    ZipcodeEnd = models.IntegerField()
    #I am not sure if we need GeoCoordinates or how to model them. Want to be able
    #to have the area on a map that a school district covers. GeoCodes the best way?
    GeoCoordinates = models.DecimalField(max_digits=12, decimal_places =10)

    class Meta(object):
        verbose_name_plural = "School Districts"
        #ordering = ('UserID',)
    def __unicode__(self):
        return unicode(self.SchoolDistrictID)
    def save(self, *args, **kwargs):
        self.SchoolDistrictID = self.SchoolDistrictID.upper()
        super(SchoolDistrict, self).save(*args, **kwargs)

class Age(models.Model):
    AgeID = models.IntegerField(unique=True, null=False)
    Infant = models.BooleanField()
    Toddler = models.BooleanField()
    PreSchooler = models.BooleanField()
    SchoolAged = models.BooleanField()
    PreTeen = models.BooleanField()

    class Meta(object):
        verbose_name_plural = "Ages"
        #ordering = ('UserID',)
    def __unicode__(self):
        return unicode(self.AgeID)
    def save(self, *args, **kwargs):
        #self.AgeID = self.AgeID.upper()
        super(Age, self).save(*args, **kwargs)

class School(models.Model):
    SchoolID = models.IntegerField(unique=True, null=False)
    Name = models.TextField()
    SchoolDistrictID = models.IntegerField(unique=False)

    class Meta(object):
        verbose_name_plural = "Schools"
        #ordering = ('UserID',)
    def __unicode__(self):
        return unicode(self.SchoolID)
    def save(self, *args, **kwargs):
        self.SchoolID = self.SchoolID.upper()
        super(School, self).save(*args, **kwargs)

class UserReview(models.Model):
    ReviewID = models.IntegerField(unique=True, null=False)
    PlaygroundID = models.IntegerField(null=False)
    UserID = models.CharField(max_length=200)
    Stars = models.IntegerField()
    Review = models.TextField(max_length=1000)

    class Meta(object):
        verbose_name_plural = "User Reviews"
        #ordering = ('UserID',)
    def __unicode__(self):
        return unicode(self.ReviewID)
    def save(self, *args, **kwargs):
        self.ReviewID = self.ReviewID.upper()
        super(UserReview, self).save(*args, **kwargs)

class Features(models.Model):
    PlaygroundID = models.IntegerField(unique=True, null=False)
    Swing = models.IntegerField()
    Slide = models.IntegerField()
    MonkeyBars = models.IntegerField()
    SandBox = models.IntegerField()
    Field = models.IntegerField()
    PicnicTable = models.IntegerField()
    Bathrooms = models.IntegerField()
    ChangingStation = models.IntegerField()
    Shade = models.IntegerField()
    BasketballCourt = models.IntegerField()
    Baseball = models.IntegerField()

    class Meta(object):
        verbose_name_plural = "Features"
        #ordering = ('UserID',)
    def __unicode__(self):
        return unicode(self.PlaygroundID)
    def save(self, *args, **kwargs):
        self.PlaygroundID = self.PlaygroundID.upper()
        super(Features, self).save(*args, **kwargs)

class SafetyFeatures(models.Model):
    PlaygroundID = models.IntegerField(unique=True, null=False)
    ProximityToHighway = models.IntegerField()
    Fenced = models.BooleanField()

    class Meta(object):
        verbose_name_plural = "Safety Features"
        #ordering = ('UserID',)
    def __unicode__(self):
        return unicode(self.PlaygroundID)
    def save(self, *args, **kwargs):
        self.PlaygroundID = self.PlaygroundID.upper()
        super(SafetyFeatures, self).save(*args, **kwargs)

class TransportationFeatures(models.Model):
    PlaygroundID = models.IntegerField(unique=True, null=False)
    BikePath = models.BooleanField()
    HikingTrail = models.BooleanField()
    AdjacentParking = models.BooleanField()
    NearbyParking = models.BooleanField()
    NoParking = models.BooleanField()
    ProximityToBus = models.IntegerField()

    class Meta(object):
        verbose_name_plural = "Transportation Features"
        #ordering = ('UserID',)
    def __unicode__(self):
        return unicode(self.PlaygroundID)
    def save(self, *args, **kwargs):
        self.PlaygroundID = self.PlaygroundID.upper()
        super(TransportationFeatures, self).save(*args, **kwargs)

class SuggestPlayground(models.Model):
    SuggestionID = models.IntegerField(unique=True, null=False)
    PlaygroundName = models.TextField()
    Address = models.TextField()
    Description = models.CharField(max_length=1000)
    Image = models.TextField()
    Swing = models.IntegerField()
    Slide = models.IntegerField()
    MonkeyBars = models.IntegerField()
    SandBox = models.IntegerField()
    Field = models.IntegerField()
    PicnicTable = models.IntegerField()
    Bathrooms = models.IntegerField()
    ChangingStation = models.IntegerField()
    Shade = models.IntegerField()
    BasketballCourt = models.IntegerField()
    Baseball = models.IntegerField()    

    class Meta(object):
        verbose_name_plural = "Suggested Playgrounds"
        #ordering = ('UserID',)
    def __unicode__(self):
        return unicode(self.SuggestiontID)
    def save(self, *args, **kwargs):
        self.SuggestionID = self.SuggestionID.upper()
        super(SuggestPlayground, self).save(*args, **kwargs)