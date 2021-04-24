import os
from django.shortcuts import render
from .excel import create_excel_metadata
from .models import VisitorMetaData
from django.core.files import File
from .databases import city_database


def home(request):
    visitor = VisitorMetaData()

    download_data(request, visitor)
    ip_address = get_ip_address(request)
    location_info = city_database(ip_address, visitor)

    # print(location_info)

    context = {

    }

    return render(request, 'home.html', context)


# Writing the data to a newly created excel file
def download_data(request, visitor):
    # visitor = VisitorMetaData()
    data = {}

    for variable, value in request.META.items():
        data[variable] = value
        if variable == 'HTTP_X_FORWARDED_FOR':
            visitor.ipv4 = value

        elif variable == 'REMOTE_ADDR':
            visitor.remote_address = value

        elif variable == 'HTTP_HOST':
            visitor.http_host = value

    username = create_excel_metadata(data)

    try:
        visitor.meta_data = File(open(f'{username}_metadata.xlsx', mode='rb'), name=f'{username}_metadata.xlsx')
        visitor.save()
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
