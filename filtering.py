# coding: utf-8
def filter(stations, sfilter=lambda s: True, pfilter=lambda p: True):
    filtered_list = []
    for s in stations:
        if not station_filter(s):
            continue
        for p in s.projects:
            if project_filter(p):
                filtered_list.append(s)
                break
    return filtered_list
    
def f(stations, sf=lambda s: True, pf=lambda p: True):
    filtered_list = []
    for s in stations:
        if not sf(s):
            continue
        for p in s.projects:
            if pf(p):
                filtered_list.append(s)
                break
    return filtered_list
    
    
