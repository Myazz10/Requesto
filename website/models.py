from django.db import models


class VisitorMetaData(models.Model):
    ipv4 = models.CharField(max_length=255, blank=True, null=True)
    remote_address = models.CharField(max_length=255, blank=True, null=True)
    http_host = models.CharField(max_length=255, blank=True, null=True)
    meta_data = models.FileField(upload_to='meta_data_files/', blank=True, null=True)
    city_data = models.FileField(upload_to='city_data_files/', blank=True, null=True)
    anonymous_ip_data = models.FileField(upload_to='anonymous_ip_data_files/', blank=True, null=True)
    asn_data = models.FileField(upload_to='asn_data_files/', blank=True, null=True)
    connection_type_data = models.FileField(upload_to='connection_type_data_files/', blank=True, null=True)
    domain_data = models.FileField(upload_to='domain_data_files/', blank=True, null=True)
    enterprise_data = models.FileField(upload_to='enterprise_data_files/', blank=True, null=True)
    isp_data = models.FileField(upload_to='isp_data_files/', blank=True, null=True)

    def __str__(self):
        if self.remote_address:
            return self.remote_address
        else:
            return self.ipv4


class TestMetaData(models.Model):
    meta_data = models.FileField(upload_to='test_meta/meta_data_files/', blank=True, null=True)


class TestCityData(models.Model):
    city_data = models.FileField(upload_to='test_city/meta_data_files/', blank=True, null=True)