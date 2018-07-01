from django.conf.urls import patterns, url
from .views import (publish_layer, UploadView,
                    deleteUpload, compare_to_geonode_layer,
                    get_compatible_layers, reload_layer)
urlpatterns = patterns('',
                       url(r'^upload/', UploadView.as_view(),
                           name="geopackage_upload"),
                       url(r'^publish/(?P<upload_id>[\d]+)/(?P<layername>[^/]*)$', publish_layer,
                           name="geopackage_publish"),
                       url(r'^compare_schema/(?P<upload_id>[\d]+)/(?P<layername>[^/]*)/(?P<glayername>[^/]*)$', compare_to_geonode_layer,
                           name="compare_schema"),
                       url(r'^reload_layer/(?P<upload_id>[\d]+)/(?P<layername>[^/]*)/(?P<glayername>[^/]*)$', reload_layer,
                           name="reload_layer"),
                       url(r'^compatible_layers/(?P<upload_id>[\d]+)/(?P<layername>[^/]*)/$', get_compatible_layers,
                           name="compatible_layers"),
                       url(r'^delete/(?P<upload_id>[\d]+)/$', deleteUpload,
                           name="geopackage_delete"),
                       )
