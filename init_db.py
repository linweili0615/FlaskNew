#!/usr/bin/env python3
# -*- coding: utf-8 -*-
from apps.auth.models import *
from apps.test.models import *

from apps import create_app

app = create_app()
app_ctx = app.app_context()
with app_ctx:
    db.create_all()