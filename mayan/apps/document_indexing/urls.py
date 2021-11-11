from __future__ import unicode_literals

from django.conf.urls import url

from .api_views import (
    APIDocumentIndexListView, APIIndexListView,
    APIIndexNodeInstanceDocumentListView, APIIndexTemplateListView,
    APIIndexTemplateView, APIIndexView
)
from .views import (
    DocumentIndexNodeListView, DocumentTypeIndexesView, IndexInstanceNodeView,
    IndexListView, IndexesRebuildView, SetupIndexDocumentTypesView,
    SetupIndexCreateView, SetupIndexDeleteView, SetupIndexEditView,
    SetupIndexListView, SetupIndexRebuildView, SetupIndexTreeTemplateListView,
    TemplateNodeCreateView, TemplateNodeDeleteView, TemplateNodeEditView
)

urlpatterns = [
    url(
        regex=r'^setup/document_types/(?P<pk>\d+)/index_templates/$',
        view=DocumentTypeIndexesView.as_view(),
        name='document_type_index_templates'
    ),
    url(
        regex=r'^setup/index/list/$', view=SetupIndexListView.as_view(),
        name='index_setup_list'
    ),
    url(
        regex=r'^setup/index/create/$', view=SetupIndexCreateView.as_view(),
        name='index_setup_create'
    ),
    url(
        regex=r'^setup/index/(?P<pk>\d+)/edit/$',
        view=SetupIndexEditView.as_view(), name='index_setup_edit'
    ),
    url(
        regex=r'^setup/index/(?P<pk>\d+)/delete/$',
        view=SetupIndexDeleteView.as_view(), name='index_setup_delete'
    ),
    url(
        regex=r'^setup/index/(?P<pk>\d+)/template/$',
        view=SetupIndexTreeTemplateListView.as_view(), name='index_setup_view'
    ),
    url(
        regex=r'^setup/index/(?P<pk>\d+)/document_types/$',
        view=SetupIndexDocumentTypesView.as_view(),
        name='index_setup_document_types'
    ),
    url(
        regex=r'^setup/index/(?P<pk>\d+)/rebuild/$',
        view=SetupIndexRebuildView.as_view(), name='index_setup_rebuild'
    ),
    url(
        regex=r'^setup/template/node/(?P<pk>\d+)/create/child/$',
        view=TemplateNodeCreateView.as_view(), name='template_node_create'
    ),
    url(
        regex=r'^setup/template/node/(?P<pk>\d+)/edit/$',
        view=TemplateNodeEditView.as_view(), name='template_node_edit'
    ),
    url(
        regex=r'^setup/template/node/(?P<pk>\d+)/delete/$',
        view=TemplateNodeDeleteView.as_view(), name='template_node_delete'
    ),

    url(
        regex=r'^index/list/$', view=IndexListView.as_view(), name='index_list'
    ),
    url(
        regex=r'^instance/node/(?P<pk>\d+)/$',
        view=IndexInstanceNodeView.as_view(), name='index_instance_node_view'
    ),

    url(
        regex=r'^indexes/rebuild/$', view=IndexesRebuildView.as_view(),
        name='rebuild_index_instances'
    ),
    url(
        regex=r'^list/for/document/(?P<pk>\d+)/$',
        view=DocumentIndexNodeListView.as_view(), name='document_index_list'
    ),
]

api_urls = [
    url(
        regex=r'^indexes/node/(?P<pk>[0-9]+)/documents/$',
        view=APIIndexNodeInstanceDocumentListView.as_view(),
        name='index-node-documents'
    ),
    url(
        regex=r'^indexes/template/(?P<pk>[0-9]+)/$',
        view=APIIndexTemplateView.as_view(), name='index-template-detail'
    ),
    url(
        regex=r'^indexes/(?P<pk>[0-9]+)/$', view=APIIndexView.as_view(),
        name='index-detail'
    ),
    url(
        regex=r'^indexes/(?P<pk>[0-9]+)/template/$',
        view=APIIndexTemplateListView.as_view(), name='index-template-detail'
    ),
    url(
        regex=r'^indexes/$', view=APIIndexListView.as_view(), name='index-list'
    ),
    url(
        regex=r'^documents/(?P<pk>[0-9]+)/indexes/$',
        view=APIDocumentIndexListView.as_view(), name='document-index-list'
    ),
]
