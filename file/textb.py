#/usr/bin/env python
# -*- coding: utf-8 -*-
from textblob import *
import sys

t = sys.argv[1]
t = t.decode('utf-8')
testimonial = TextBlob(t)
print testimonial.sentiment.polarity
print testimonial.sentiment.subjectivity
