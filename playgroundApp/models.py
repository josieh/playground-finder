from django.db import models

# Create your models here.
class User(models.Model):
    userID = models.CharField(unique=True, null=False, max_length=200)
    name = models.CharField(null=False, max_length=200)
    description = models.TextField()
    zipcode = models.IntegerField(null=True)
    age = models.IntegerField(null= True)
    isMom = models.BooleanField()
    isDad = models.BooleanField()
    isGrandparent = models.BooleanField()
    isOther = models.BooleanField()
    favoritesID = models.IntegerField(null=True)
    image = models.TextField()

    class Meta(object):
        verbose_name_plural = "Users"
        #ordering = ('userID',)
    def __unicode__(self):
        return unicode(self.userID)
    def save(self, *args, **kwargs):
        self.userID = self.userID.upper()
        super(User, self).save(*args, **kwargs)
        
class Playground(models.Model):
    playgroundID = models.IntegerField(blank=True, null=True)
    name = models.TextField()
    street = models.TextField()
    zipcode = models.IntegerField()
    handicap = models.BooleanField(default=False, blank=True)
    schoolDistrictID = models.IntegerField(blank=True, default=2, null=True)
    hours = models.TextField(null=True, default="Dusk To Dawn", blank=True)
    image = models.TextField(blank=True)
    #should not be required, but we need to figure out how to get lat/lon from address
    latLon = models.CharField(max_length=25, blank=True)
    infant = models.BooleanField(default=False, blank=True)
    toddler = models.BooleanField(default=False, blank=True)
    preSchooler = models.BooleanField(default=False, blank=True)
    schoolAged = models.BooleanField(default=False, blank=True)
    preTeen = models.BooleanField(default=False, blank=True)
    swing = models.BooleanField(default=False, blank=True)
    slide = models.BooleanField(default=False, blank=True)
    monkeyBars = models.BooleanField(default=False, blank=True)
    sandBox = models.BooleanField(default=False, blank=True)
    field = models.BooleanField(default=False, blank=True)
    picnicTable = models.BooleanField(default=False, blank=True)
    bathrooms = models.BooleanField(default=False, blank=True)
    changingStation = models.BooleanField(default=False, blank=True)
    shade = models.BooleanField(default=False, blank=True)
    basketballCourt = models.BooleanField(default=False, blank=True)
    baseball = models.BooleanField(default=False, blank=True)
    proximityToHighway = models.IntegerField(default=0, blank=True, null=True)
    fenced = models.BooleanField(default=False, blank=True)
    bikePath = models.BooleanField(default=False, blank=True)
    hikingTrail = models.BooleanField(default=False, blank=True)
    adjacentParking = models.BooleanField(default=False, blank=True)
    nearbyParking = models.BooleanField(default=False, blank=True)
    noParking = models.BooleanField(default=False, blank=True)
    proximityToBus = models.IntegerField(default=0, blank=True, null=True)

    class Meta(object):
        verbose_name_plural = "Playgrounds"
        #ordering = ('UserID',)
    def __unicode__(self):
        return unicode(self.playgroundID)
    def save(self, *args, **kwargs):
        super(Playground, self).save(*args, **kwargs)

class SchoolDistrict(models.Model):
    schoolDistrictID = models.IntegerField(unique=True, null=False)
    districtname = models.TextField()
    zipcodeStart = models.IntegerField()
    zipcodeEnd = models.IntegerField()
    #I am not sure if we need GeoCoordinates or how to model them. Want to be able
    #to have the area on a map that a school district covers. GeoCodes the best way?
    geoCoordinates = models.DecimalField(max_digits=12, decimal_places =10)

    class Meta(object):
        verbose_name_plural = "School Districts"
        #ordering = ('UserID',)
    def __unicode__(self):
        return unicode(self.schoolDistrictID)
    def save(self, *args, **kwargs):
        self.schoolDistrictID = self.schoolDistrictID.upper()
        super(SchoolDistrict, self).save(*args, **kwargs)

class Age(models.Model):
    ageID = models.IntegerField(unique=True, null=False)
    infant = models.BooleanField()
    toddler = models.BooleanField()
    preSchooler = models.BooleanField()
    schoolAged = models.BooleanField()
    preTeen = models.BooleanField()

    class Meta(object):
        verbose_name_plural = "Ages"
        #ordering = ('UserID',)
    def __unicode__(self):
        return unicode(self.ageID)
    def save(self, *args, **kwargs):
        #self.ageID = self.ageID.upper()
        super(Age, self).save(*args, **kwargs)

class School(models.Model):
    schoolID = models.IntegerField(unique=True, null=False)
    name = models.TextField()
    schoolDistrictID = models.IntegerField(unique=False)

    class Meta(object):
        verbose_name_plural = "Schools"
        #ordering = ('UserID',)
    def __unicode__(self):
        return unicode(self.schoolID)
    def save(self, *args, **kwargs):
        self.schoolID = self.schoolID.upper()
        super(School, self).save(*args, **kwargs)

class UserReview(models.Model):
    reviewID = models.IntegerField(unique=True, null=False)
    playgroundID = models.IntegerField(null=False)
    userID = models.CharField(max_length=200)
    stars = models.IntegerField()
    review = models.TextField(max_length=1000)

    class Meta(object):
        verbose_name_plural = "User Reviews"
        #ordering = ('UserID',)
    def __unicode__(self):
        return unicode(self.reviewID)
    def save(self, *args, **kwargs):
        self.reviewID = self.reviewID.upper()
        super(UserReview, self).save(*args, **kwargs)

class Features(models.Model):
    playgroundID = models.IntegerField(unique=True, null=False)
    swing = models.IntegerField()
    slide = models.IntegerField()
    monkeyBars = models.IntegerField()
    sandBox = models.IntegerField()
    field = models.IntegerField()
    picnicTable = models.IntegerField()
    bathrooms = models.IntegerField()
    changingStation = models.IntegerField()
    shade = models.IntegerField()
    basketballCourt = models.IntegerField()
    baseball = models.IntegerField()

    class Meta(object):
        verbose_name_plural = "Features"
        #ordering = ('UserID',)
    def __unicode__(self):
        return unicode(self.playgroundID)
    def save(self, *args, **kwargs):
        self.playgroundID = self.playgroundID.upper()
        super(Features, self).save(*args, **kwargs)

class SafetyFeatures(models.Model):
    playgroundID = models.IntegerField(unique=True, null=False)
    proximityToHighway = models.IntegerField()
    fenced = models.BooleanField()

    class Meta(object):
        verbose_name_plural = "Safety Features"
        #ordering = ('UserID',)
    def __unicode__(self):
        return unicode(self.playgroundID)
    def save(self, *args, **kwargs):
        self.playgroundID = self.playgroundID.upper()
        super(SafetyFeatures, self).save(*args, **kwargs)

class TransportationFeatures(models.Model):
    playgroundID = models.IntegerField(unique=True, null=False)
    bikePath = models.BooleanField()
    hikingTrail = models.BooleanField()
    adjacentParking = models.BooleanField()
    nearbyParking = models.BooleanField()
    noParking = models.BooleanField()
    proximityToBus = models.IntegerField()

    class Meta(object):
        verbose_name_plural = "Transportation Features"
        #ordering = ('UserID',)
    def __unicode__(self):
        return unicode(self.playgroundID)
    def save(self, *args, **kwargs):
        self.playgroundID = self.playgroundID.upper()
        super(TransportationFeatures, self).save(*args, **kwargs)

class SuggestPlayground(models.Model):
    suggestionID = models.IntegerField(unique=True, null=False)
    playgroundName = models.TextField()
    address = models.TextField()
    description = models.CharField(max_length=1000)
    image = models.TextField()
    swing = models.IntegerField()
    slide = models.IntegerField()
    monkeyBars = models.IntegerField()
    sandBox = models.IntegerField()
    field = models.IntegerField()
    picnicTable = models.IntegerField()
    bathrooms = models.IntegerField()
    changingStation = models.IntegerField()
    shade = models.IntegerField()
    basketballCourt = models.IntegerField()
    baseball = models.IntegerField()    

    class Meta(object):
        verbose_name_plural = "Suggested Playgrounds"
        #ordering = ('UserID',)
    def __unicode__(self):
        return unicode(self.suggestiontID)
    def save(self, *args, **kwargs):
        self.suggestionID = self.suggestionID.upper()
        super(SuggestPlayground, self).save(*args, **kwargs)