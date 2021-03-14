#0645632754
#import phone_iso3166
import pycountry
import tkinter
from phone_iso3166.country import phone_country
import phonenumbers
from phonenumbers import geocoder,carrier

number="33645632754"
code=phone_country(number)
print("code="+code)
C=pycountry.countries.get(alpha_2=code)
print("C={}".format(C))

print("getitng continent")
ch_number=phonenumbers.parse(number, "CH")#country name
print("ch_number={}".format(ch_number))
print("geocoder={}".format(geocoder.description_for_number(ch_number,"en")))


print("getting operator")
service_number=phonenumbers.parse(number,"RO")
print("carrier={}".format(carrier.name_for_number(service_number,"en")))
