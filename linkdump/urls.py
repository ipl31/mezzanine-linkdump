from django.conf.urls import url
from linkdump.views import (link_dump_list,
                            link_dump_tag_list,
                            link_dump_redirect)


urlpatterns = [
    url("^$", link_dump_list, name="link_dump_list"),
    url("^category/(?P<category>.*)/$", link_dump_list,
        name="link_dump_list"),
    url("^tags/(?P<keyword_slug>.*)/$", link_dump_tag_list,
        name="link_dump_tag_list"),
    url("^(?P<dump_slug>.*)/$", link_dump_redirect,
        name="link_dump_redirect"),
    ]
