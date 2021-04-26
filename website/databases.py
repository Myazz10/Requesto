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
    city_info = {}

    # This creates a Reader object. You should use the same object
    # across multiple requests as creation of it is expensive.
    try:
        username = None
        with geoip2.database.Reader('geo_ip/city/GeoLite2-City.mmdb') as reader:
            # Replace "city" with the method corresponding to the database
            # that you are using, e.g., "country".
            # response = reader.city('72.252.231.177')
            response = reader.city(ip_address)
            try:
                city_info['Country ISO Code'] = str(response.country.iso_code)
            except:
                pass

            try:
                city_info['Country Name'] = str(response.country.name)
            except:
                pass

            try:
                city_info['Specific Location'] = str(response.subdivisions.most_specific.name)
            except:
                pass

            try:
                city_info['Specific Location ISO CODE'] = str(response.subdivisions.most_specific.iso_code)
            except:
                pass

            try:
                city_info['City Name'] = str(response.city.name)
            except:
                pass

            try:
                city_info['Postal Code'] = str(response.postal.code)
            except:
                pass

            try:
                city_info['Location: Latitude'] = str(response.location.latitude)
            except:
                pass

            try:
                city_info['Location: Longitude'] = str(response.location.longitude)
            except:
                pass

            try:
                city_info['Traits Network'] = str(response.traits.network)
            except:
                pass

            print(response.country.iso_code)
            'US'
            print(response.country.name)
            # 'United States'
            print(response.subdivisions.most_specific.name)
            # 'Minnesota'
            print(response.subdivisions.most_specific.iso_code)
            # 'MN'
            print(response.city.name)
            # 'Minneapolis'
            print(response.postal.code)
            # '55455'
            print(response.location.latitude)
            # 44.9733
            print(response.location.longitude)
            # -93.2323
            print(response.traits.network)

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

            """username = create_excel_city_data(response, visitor.ipv4)

            try:
                test_city_data.city_data = File(open(f'{username}_city_data.xlsx', mode='rb'), name=f'{username}_city_data.xlsx')
                test_city_data.save()
                os.remove(f'{username}_city_data.xlsx')
            except:
                pass"""
    except IOError:
        print('Database not found!\n')
    except Exception:
        switch = 1
        print("Error ip used here...\n")

    return city_info


def anonymous_ip_database(ip_address):
    anonymous_info = {}
    # This creates a Reader object. You should use the same object
    # across multiple requests as creation of it is expensive.
    try:
        with geoip2.database.Reader('geo_ip/anonymous/GeoIP2-Anonymous-IP-Test.mmdb') as reader:
            response = reader.anonymous_ip(ip_address)
            try:
                anonymous_info['Is Anonymous'] = str(response.is_anonymous)
            except:
                pass

            try:
                anonymous_info['Is Anonymous VPN'] = str(response.is_anonymous_vpn)
            except:
                pass

            try:
                anonymous_info['Is Hosting Provider'] = str(response.is_hosting_provider)
            except:
                pass

            try:
                anonymous_info['Is Public Proxy'] = str(response.is_public_proxy)
            except:
                pass

            try:
                anonymous_info['Is Residential Proxy'] = str(response.is_residential_proxy)
            except:
                pass

            try:
                anonymous_info['Is Tor Exit Node'] = str(response.is_tor_exit_node)
            except:
                pass

            try:
                anonymous_info['IP Address'] = str(response.ip_address)
            except:
                pass

            try:
                anonymous_info['Network'] = str(response.network)
            except:
                pass

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
    except IOError:
        print('Database not found!\n')
    except Exception:
        print("Error ip used here...\n")

    return anonymous_info


def asn_database(ip_address):
    asn_info = {}
    # This creates a Reader object. You should use the same object
    # across multiple requests as creation of it is expensive.
    try:
        with geoip2.database.Reader('geo_ip/asn/GeoLite2-ASN.mmdb') as reader:
            response = reader.asn(ip_address)
            try:
                asn_info['System Number'] = str(response.autonomous_system_number)
            except:
                pass

            try:
                asn_info['System Organization'] = str(response.autonomous_system_organization)
            except:
                pass

            try:
                asn_info['IP Address'] = str(response.ip_address)
            except:
                pass

            try:
                asn_info['Network'] = str(response.network)
            except:
                pass

            print(response.autonomous_system_number)
            # 1221
            print(response.autonomous_system_organization)
            # 'Telstra Pty Ltd'
            print(response.ip_address)
            # '203.0.113.0'
            print(response.network)
            # IPv4Network('203.0.113.0/24')
    except IOError:
        print('Database not found!\n')
    except Exception:
        print("Error ip used here...\n")

    return asn_info


def connection_type_database(ip_address):
    connection_type_info = {}
    # This creates a Reader object. You should use the same object
    # across multiple requests as creation of it is expensive.
    try:
        with geoip2.database.Reader('geo_ip/connection-type/GeoIP2-Connection-Type-Test.mmdb') as reader:
            response = reader.connection_type(ip_address)
            try:
                connection_type_info['Connection Type'] = str(response.connection_type)
            except:
                pass

            try:
                connection_type_info['IP Address'] = str(response.ip_address)
            except:
                pass

            try:
                connection_type_info['Network'] = str(response.network)
            except:
                pass

            print(response.connection_type)
            # 'Corporate'
            print(response.ip_address)
            # '203.0.113.0'
            print(response.network)
            # IPv4Network('203.0.113.0/24')
    except IOError:
        print('Database not found!\n')
    except Exception:
        print("Error ip used here...\n")

    return connection_type_info


def domain_database(ip_address):
    domain_info = {}
    # This creates a Reader object. You should use the same object
    # across multiple requests as creation of it is expensive.
    try:
        with geoip2.database.Reader('geo_ip/domain/GeoIP2-Domain-Test.mmdb') as reader:
            response = reader.domain(ip_address)
            try:
                domain_info['Domain'] = str(response.domain)
            except:
                pass

            try:
                domain_info['IP Address'] = str(response.ip_address)
            except:
                pass

            print(response.domain)
            # 'umn.edu'
            print(response.ip_address)
            # '203.0.113.0'
    except IOError:
        print('Database not found!\n')
    except Exception:
        print("Error ip used here...\n")

    return domain_info


def enterprise_database(ip_address):
    enterprise_info = {}
    # This creates a Reader object. You should use the same object
    # across multiple requests as creation of it is expensive.
    try:
        with geoip2.database.Reader('geo_ip/enterprise/GeoIP2-Enterprise-Test.mmdb') as reader:
            # Use the .enterprise method to do a lookup in the Enterprise database
            response = reader.enterprise(ip_address)
            try:
                enterprise_info['Country Confidence'] = str(response.country.confidence)
            except:
                pass

            try:
                enterprise_info['Country ISO Code'] = str(response.country.iso_code)
            except:
                pass

            try:
                enterprise_info['Country Name'] = str(response.country.name)
            except:
                pass

            try:
                enterprise_info['Specific Location'] = str(response.subdivisions.most_specific.name)
            except:
                pass

            try:
                enterprise_info['Specific Location ISO CODE'] = str(response.subdivisions.most_specific.iso_code)
            except:
                pass

            try:
                enterprise_info['Specific Location ISO CODE Confidence'] = str(response.subdivisions.most_specific.confidence)
            except:
                pass

            try:
                enterprise_info['City Name'] = str(response.city.name)
            except:
                pass

            try:
                enterprise_info['Postal Code'] = str(response.postal.code)
            except:
                pass

            try:
                enterprise_info['Location: Latitude'] = str(response.location.latitude)
            except:
                pass

            try:
                enterprise_info['Location: Longitude'] = str(response.location.longitude)
            except:
                pass

            try:
                enterprise_info['Location: Accuracy Radius'] = str(response.location.accuracy_radius)
            except:
                pass

            try:
                enterprise_info['Traits Network'] = str(response.traits.network)
            except:
                pass

            print(response.country.confidence)
            # 99
            print(response.country.iso_code)
            # 'US'
            print(response.country.name)
            # 'United States'
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
    except IOError:
        print('Database not found!\n')
    except Exception:
        print("Error ip used here...\n")

    return enterprise_info


def isp_database(ip_address):
    isp_info = {}
    # This creates a Reader object. You should use the same object
    # across multiple requests as creation of it is expensive.
    try:
        with geoip2.database.Reader('geo_ip/isp/GeoIP2-ISP-Test.mmdb') as reader:
            response = reader.isp(ip_address)
            try:
                isp_info['Autonomous System Number'] = str(response.autonomous_system_number)
            except:
                pass

            try:
                isp_info['Autonomous System Organization'] = str(response.autonomous_system_organization)
            except:
                pass

            try:
                isp_info['Internet Service Provider'] = str(response.isp)
            except:
                pass

            try:
                isp_info['Organization'] = str(response.organization)
            except:
                pass

            try:
                isp_info['IP Address'] = str(response.ip_address)
            except:
                pass

            try:
                isp_info['Network'] = str(response.network)
            except:
                pass

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
    except IOError:
        print('Database not found!\n')
    except Exception:
        print("Error ip used here...\n")

    return isp_info
