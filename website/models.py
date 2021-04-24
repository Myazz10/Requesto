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

    """all_users_profile = models.CharField(max_length=500, blank=True, null=True)
    COMMONPROGRAMFILES
    FPS_BROWSER_USER_PROFILE_STRING
    COMPUTERNAME:
    PROGRAMDATA
    ONLINESERVICES:
    SYSTEMDRIVE:
    USERDOMAIN:
    ONEDRIVECONSUMER
    ONEDRIVE:
    TMP:
    TEMP:
    PROGRAMFILES:
    WINDIR:
    USERDOMAIN_ROAMINGPROFILE:
    COMSPEC:
    PROCESSOR_LEVEL
    NUMBER_OF_PROCESSORS:
    PROCESSOR_ARCHITECTURE
    OS
    ASL.LOG:
    PROMPT:
    PROGRAMFILES(X86):
    PSMODULEPATH:
    PATHEXT
    PROCESSOR_IDENTIFIER:
    REGIONCODE
    EMAIL_USER:
    APPDATA:
    LOCALAPPDATA:
    SYSTEMROOT
    HOMEPATH
    LOGONSERVER:
    HOMEDRIVE:
    DRIVERDATA:
    PATH:
    PUBLIC:
    FPS_BROWSER_APP_PROFILE_STRING:
    PROCESSOR_REVISION:
    PLATFORMCODE:
    USERPROFILE:
    ALLUSERSPROFILE:
    USERNAME
    COMMONPROGRAMW6432:
    PROGRAMW6432:
    SERVER_NAME:
    GATEWAY_INTERFACE:
    SERVER_PORT:
    REMOTE_HOST
    CONTENT_LENGTH
    SCRIPT_NAME
    SERVER_PROTOCOL:
    SERVER_SOFTWARE:
    REQUEST_METHOD:
    PATH_INFO:
    REMOTE_ADDR:
    CONTENT_TYPE:
    HTTP_HOST:
    HTTP_CONNECTION:
    HTTP_CACHE_CONTROL:
    HTTP_SEC_CH_UA:
    HTTP_SEC_CH_UA_MOBILE:
    HTTP_UPGRADE_INSECURE_REQUESTS:
    HTTP_USER_AGENT:
    HTTP_ACCEPT:
    HTTP_SEC_FETCH_SITE:
    HTTP_SEC_FETCH_MODE:
    HTTP_SEC_FETCH_USER:
    HTTP_SEC_FETCH_DEST:
    HTTP_ACCEPT_ENCODING:
    HTTP_ACCEPT_LANGUAGE:
    HTTP_COOKIE:"""
    pass


