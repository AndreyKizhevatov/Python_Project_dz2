#!/usr/bin/env python
# -*- coding: utf-8 -*-

from pprint import pprint

sites = {
    'Moscow': (550, 370),
    'London': (510, 510),
    'Paris': (480, 480),}

distances = dict()

moscow = sites['Moscow']
london = sites['London']
paris = sites['Paris']
moscow_london = ((moscow[0] - london[0]) **2 + (moscow[1]-london[1]) **2) ** .5
moscow_paris = ((moscow[0] - paris[0])**2 + (moscow[1] - paris[1]) **2) ** .5

distances['Moscow'] = {}
distances['Moscow']['London'] = moscow_london
distances['Moscow']['Paris'] = moscow_paris

london_paris = ((paris[0] - london[0]) **2 + (paris[1]-london[1]) **2) ** .5

distances['London'] = {}
distances['London']['Moscow'] = moscow_london
distances['London']['Paris'] = london_paris

distances['Paris'] = {}
distances['Paris']['Moscow'] = moscow_london
distances['Paris']['London'] = london_paris

pprint(distances)












