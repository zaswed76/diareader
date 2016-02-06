#!/usr/bin/env python
# -*- coding: utf-8 -*-

from program.langid.langid import LanguageIdentifier, model
identifier = LanguageIdentifier.from_modelstring(model, norm_probs=True)
print(identifier.classify("Дракон Мартин"))
