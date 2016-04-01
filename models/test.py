from model import *
from mongoengine import *
dustbin=dustbin_data()
dustbin.completeness = "10"
dustbin.suffix = "cept"
dustbin.geolocation = [23.0375548,72.5480249]
dustbin.weight = "10"
dustbin.save()
