# -*- coding: utf-8 -*-
#
#   Copyright 2018 Nick Boultbee
#   This file is part of squeeze-alexa.
#
#   squeeze-alexa is free software: you can redistribute it and/or modify
#   it under the terms of the GNU General Public License as published by
#   the Free Software Foundation, either version 3 of the License, or
#   (at your option) any later version.
#
#   See LICENSE for full license

import os

from squeezealexa import _

AN_UNTRANSLATED_STRING = "foobar baz"


def test_gettext_basic():
    assert _(AN_UNTRANSLATED_STRING) == AN_UNTRANSLATED_STRING


def test_gettext_known_british():
    lang = os.environ["LANG"]
    os.environ["LANG"] = "en_GB.utf8"
    assert _("favorites") == "favourites"
    os.environ["LANG"] = lang
