import os
import geoip2.database
from django.core.files import File
from .excel import create_excel_city_data

# Database Reader Exceptions
# --> FileNotFoundError
# --> ValueError
# --> maxminddb.InvalidDatabaseError
# --> AddressNotFoundError

"""
If the database file does not exist or is not readable, the constructor will raise a FileNotFoundError. If the IP 
address passed to a method is invalid, a ValueError will be raised. If the file is invalid or there is a bug in the 
reader, a maxminddb.InvalidDatabaseError will be raised with a description of the problem. If an IP address is not in 
the database, a AddressNotFoundError will be raised. 
"""


def city_database(ip_address, visitor, test_city_data):
    location_info = {}

    # This creates a Reader object. You should use the same object
    # across multiple requests as creation of it is expensive.
    try:
        username = None
        with geoip2.database.Reader('geo_ip/city/GeoLite2-City.mmdb') as reader:
            # Replace "city" with the method corresponding to the database
            # that you are using, e.g., "country".
            # response = reader.city('72.252.231.177')
            response = reader.city(ip_address)

            """if visitor.remote_address:
                username = create_excel_city_data(response, visitor.remote_address)
            else:
                username = create_excel_city_data(response, visitor.ipv4)

            try:
                visitor.city_data = File(open(f'{username}_city_data.xlsx', mode='rb'), name=f'{username}_city_data.xlsx')
                visitor.save()
                os.remove(f'{username}_city_data.xlsx')
            except:
                pass"""

            username = create_excel_city_data(response, visitor.ipv4)

            try:
                test_city_data.city_data = File(open(f'{username}_city_data.xlsx', mode='rb'), name=f'{username}_city_data.xlsx')
                test_city_data.save()
                os.remove(f'{username}_city_data.xlsx')
            except:
                pass
    except IOError:
        print('Database not found!\n')
    except Exception:
        location_info = None
        switch = 1
        print("Error ip used here...\n")

    return location_info


def anonymous_ip_database(ip_address):
    # This creates a Reader object. You should use the same object
    # across multiple requests as creation of it is expensive.
    with geoip2.database.Reader('geo_ip/anonymous/GeoIP2-Anonymous-IP-Test.mmdb') as reader:
        response = reader.anonymous_ip('72.252.231.177')
        print(response.is_anonymous)
        # True
        print(response.is_anonymous_vpn)
        # False
        print(response.is_hosting_provider)
        # False
        print(response.is_public_proxy)
        # False
        print(response.is_residential_proxy)
        # False
        print(response.is_tor_exit_node)
        # True
        print(response.ip_address)
        # '203.0.113.0'
        print(response.network)
        # IPv4Network('203.0.113.0/24')


def asn_database(ip_address):
    # This creates a Reader object. You should use the same object
    # across multiple requests as creation of it is expensive.
    with geoip2.database.Reader('geo_ip/asn/GeoLite2-ASN.mmdb') as reader:
        response = reader.asn('72.252.231.177')
        print(response.autonomous_system_number)
        # 1221
        print(response.autonomous_system_organization)
        # 'Telstra Pty Ltd'
        print(response.ip_address)
        # '203.0.113.0'
        print(response.network)
        # IPv4Network('203.0.113.0/24')


def connection_type_database(ip_address):
    # This creates a Reader object. You should use the same object
    # across multiple requests as creation of it is expensive.
    with geoip2.database.Reader('geo_ip/connection-type/GeoIP2-Connection-Type-Test.mmdb') as reader:
        response = reader.connection_type('72.252.231.177')
        print(response.connection_type)
        # 'Corporate'
        print(response.ip_address)
        # '203.0.113.0'
        print(response.network)
        # IPv4Network('203.0.113.0/24')


def domain_database(ip_address):
    # This creates a Reader object. You should use the same object
    # across multiple requests as creation of it is expensive.
    with geoip2.database.Reader('geo_ip/domain/GeoIP2-Domain-Test.mmdb') as reader:
        response = reader.domain('72.252.231.177')
        print(response.domain)
        # 'umn.edu'
        print(response.ip_address)
        # '203.0.113.0'


def enterprise_database(ip_address):
    # This creates a Reader object. You should use the same object
    # across multiple requests as creation of it is expensive.
    with geoip2.database.Reader('geo_ip/enterprise/GeoIP2-Enterprise-Test.mmdb') as reader:
        # Use the .enterprise method to do a lookup in the Enterprise database
        response = reader.enterprise('72.252.231.177')

        print(response.country.confidence)
        # 99
        print(response.country.iso_code)
        # 'US'
        print(response.country.name)
        # 'United States'
        print(response.country.names['zh-CN'])
        # u'美国'
        print(response.subdivisions.most_specific.name)
        # 'Minnesota'
        print(response.subdivisions.most_specific.iso_code)
        # 'MN'
        print(response.subdivisions.most_specific.confidence)
        # 77
        print(response.city.name)
        # 'Minneapolis'
        print(response.country.confidence)
        # 11
        print(response.postal.code)
        # '55455'
        print(response.location.accuracy_radius)
        # 50
        print(response.location.latitude)
        # 44.9733
        print(response.location.longitude)
        # -93.2323
        print(response.traits.network)
        # IPv4Network('203.0.113.0/24')


def isp_database(ip_address):
    # This creates a Reader object. You should use the same object
    # across multiple requests as creation of it is expensive.
    with geoip2.database.Reader('geo_ip/isp/GeoIP2-ISP-Test.mmdb') as reader:
        response = reader.isp('72.252.231.177')
        print(response.autonomous_system_number)
        # 1221
        print(response.autonomous_system_organization)
        # 'Telstra Pty Ltd'
        print(response.isp)
        # 'Telstra Internet'
        print(response.organization)
        # 'Telstra Internet'
        print(response.ip_address)
        # '203.0.113.0'
        print(response.network)
        # IPv4Network('203.0.113.0/24')
