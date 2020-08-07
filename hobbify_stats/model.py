#!/usr/bin/env python
"""This script contains the necessary method to consult the score of a date and update it"""
import querys

def relative_freq(username, date):
    """ This function returns a number between 0 and 1 that is named
        relative frequency. After,  realize a conversion to numbers between 0 and 4
        for use in the  heatmap development in ReactJS
    """

    total = querys.count_intances_pending(username, date)[0]
    done = querys.count_intances_done(username, date)[0]
    value = 0
    if total != 0:
        score = done / total
        if score == 0:
            value = 0
        elif  0 < score <= 0.25:
            value = 1
        elif  0.25 < score <= 0.5:
            value = 2
        elif  0.5 < score <= 0.75:
            value = 3
        else:
            value = 4
        querys.insert_score(value, date, username)
    else:
        print("[INFO] No se ha logrador registrar nuevas frecuencias ")

def array_score(username, date):
    """Return elements in a dictionary for use as json object"""
    tupla_username = querys.all_score(username, date)
    print(tupla_username)
    score_list = []
    for i in tupla_username:
        score_list.append({'score' : i[0], 'date': i[1].strftime('%Y/%m/%d')})
    print(score_list)
    return score_list
