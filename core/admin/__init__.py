# -*- coding: utf-8 -*-

"""

    This file is part of the GSM Mine Shop project.

    Copyright (c) 2019 GSM MINE GROUP LLC.

    For the full copyright and license information, please view the LICENSE
    file that was distributed with this source code.

    Developed by Outboss Development Team <support@outboss.io>

"""

from __future__ import unicode_literals

from django.utils.translation import ugettext_lazy as _
from django.contrib import admin

from .design import DesignAdmin
from .design_image import DesignImageAdmin
from .user_category import UserCategoryAdmin
from .design_category import DesignCategoryAdmin
from .country import CountryAdmin


admin.site.index_title = _('Inicio')
admin.site.site_header = _('Ecommerce Design Admin')
admin.site.site_title = _('Ecommerce Design Admin')
