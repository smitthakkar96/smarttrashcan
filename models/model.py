from mongoengine import *
import connect
class dustbin_data(DynamicDocument):
    geolocation = GeoPointField()
    suffix = StringField()
    completeness = StringField()
    weight = StringField(default=0)

class codes(DynamicDocument):
    code = StringField()
