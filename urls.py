# -*- coding: utf-8 -*-
#
# Copyright © 2009-2011 Alexander Kojevnikov <alexander@kojevnikov.com>
#
# muspy is free software: you can redistribute it and/or modify
# it under the terms of the GNU Affero General Public License as published by
# the Free Software Foundation, either version 3 of the License, or
# (at your option) any later version.
#
# muspy is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU Affero General Public License for more details.
#
# You should have received a copy of the GNU Affero General Public License
# along with muspy.  If not, see <http://www.gnu.org/licenses/>.

from django.conf.urls.defaults import *
from django.contrib.auth.views import login
from django.views.generic.base import RedirectView, TemplateView

from app.forms import SignInForm


urlpatterns = patterns('app.views',
    (r'^$', 'index'),
    (r'^activate$', 'activate'),
    (r'^about$', TemplateView.as_view(template_name='about.html')),
    (r'^artist/([0-9a-f\-]+)$', 'artist'),
    (r'^artists$', 'artists'),
    (r'^artists-add$', 'artists_add'),
    (r'^artists-remove$', 'artists_remove'),
    (r'^blog$', RedirectView.as_view(url='http://kojevnikov.com/tag/muspy.html')),
    (r'^blog/feed$', RedirectView.as_view(url='http://kojevnikov.com/muspy.xml')),
    (r'^calendar$', 'calendar'),
    (r'^contact$', TemplateView.as_view(template_name='contact.html')),
    (r'^cover$', 'cover'),
    (r'^delete$', 'delete'),
    (r'^faq$', TemplateView.as_view(template_name='faq.html')),
    (r'^feed$', 'feed'),
    (r'^feed/(?P<id>\d+)$', RedirectView.as_view(url='/feed?id=%(id)s')),
    (r'^ical$', 'ical'),
    (r'^ical/(?P<id>\d+)$', RedirectView.as_view(url='/ical?id=%(id)s')),
    (r'^import$', 'import_artists'),
    (r'^releases$', 'releases'),
    (r'^reset$', 'reset'),
    (r'^settings$', 'settings'),
    (r'^signin$', login, {'authentication_form': SignInForm, 'template_name': 'signin.html'}),
    (r'^signout$', 'signout'),
    (r'^signup$', 'signup'),
    (r'^sitemap.xml$', 'sitemap'),
    (r'^star$', 'star'),
    (r'^unsubscribe$', 'unsubscribe'),
    (r'blog|\.php', 'forbidden'), # Hello, vulnerability scan bots!
)

urlpatterns += patterns('',
    (r'^api/1/', include('api.urls')),
)
