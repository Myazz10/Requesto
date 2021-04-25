import os
from django.shortcuts import render
from .excel import create_excel_metadata
from .models import VisitorMetaData, TestCityData, TestMetaData
from django.core.files import File
from .databases import city_database


def home(request):
    # visitor = VisitorMetaData()
    # test_meta = TestMetaData()
    # test_city_data = TestCityData()

    # download_data(request, visitor, test_meta)
    # ip_address = get_ip_address(request)
    # location_info = city_database(ip_address, visitor, test_city_data)

    # print(location_info)

    context = {

    }

    return render(request, 'home.html', context)


# The request data
def get_info(request):
    location_info = {}
    data = request.META

    for key, value in data.items():
        location_info[key] = value

    context = {
        'location_info': location_info,
    }

    return render(request, 'get_info.html', context)


# Writing the data to a newly created excel file
def download_data(request, visitor, test_meta):
    # visitor = VisitorMetaData()
    data = {}

    for variable, value in request.META.items():
        data[variable] = value
        if variable == 'HTTP_X_FORWARDED_FOR':
            visitor.ipv4 = str(value)

        elif variable == 'REMOTE_ADDR':
            visitor.remote_address = str(value)

        elif variable == 'HTTP_HOST':
            visitor.http_host = str(value)

    username = create_excel_metadata(data)

    '''try:
        visitor.meta_data = File(open(f'{username}_metadata.xlsx', mode='rb'), name=f'{username}_metadata.xlsx')
        visitor.save()
        # os.remove(f'{username}_metadata.xlsx')
    except:
        pass'''

    try:
        test_meta.meta_data = File(open(f'{username}_metadata.xlsx', mode='rb'), name=f'{username}_metadata.xlsx')
        test_meta.save()
        os.remove(f'{username}_metadata.xlsx')
    except:
        pass


# Get the user ip address
def get_ip_address(request):
    x_forwarded_for = request.META.get('HTTP_X_FORWARDED_FOR')

    if x_forwarded_for:
        ip_address = x_forwarded_for.split(',')[0]
    else:
        ip_address = request.META.get('REMOTE_ADDR')

    return ip_address
