from django.shortcuts import render, HttpResponse, redirect
from django.forms.models import model_to_dict
from tupuqo import models
from utils import pagination
from utils import urlhandle
import time, json
import requests
import sys
from bs4 import BeautifulSoup
import difflib
import re

# @auth

def debug(request):
    if request.method == 'GET':
        return render(request, 'tupuqo/debug.html')

    elif request.method == 'POST':
        ret = {
            'status': True,
            'error': None,
            'data': None
        }
        inputHost = request.POST.get('inputHost')
        query_from = request.POST.get('query_from')
        query = request.POST.get('query')

        if query_from == '':
            query_from = 'web'
        else:
            query_from = query_from

        params = {
            'queryString': query,
            'queryFrom': query_from,
        }

        params_utf16 = urlhandle.urlencode(params, 'utf-16le', 'ignore')

        headers = {"Content-type": "application/x-www-form-urlencoded;charset=UTF-16LE"}

        try:
            resp = requests.post(inputHost, data=params_utf16, headers=headers, timeout=3)
            # print(resp.text)
            status = resp.reason
            if status != 'OK':
                # print(sys.stderr, query, status)
                ret['error'] = 'Error:未知的请求类型'
                ret['status'] = False
                return ret

            data = BeautifulSoup(resp.content.decode('utf-16le'),"html.parser")
            ret['data'] = data.prettify()

        except Exception as e:
            # print(e)
            # print(sys.stderr, sys.exc_info()[0], sys.exc_info()[1])
            ret['error'] = "Error:" + str(e)
            ret['status'] = False
        return HttpResponse(json.dumps(ret))


def debug_diff(request):
    ret = {
        'status': True,
        'error': None,
        'data': None
    }
    inputHost = request.POST.get('inputHost')
    query_from = request.POST.get('query_from')

    inputHost_diff = request.POST.get('inputHost_diff')
    query_from_diff = request.POST.get('query_from_diff')

    query = request.POST.get('query')

    if query_from == '':
        query_from = 'web'
    else:
        query_from = query_from

    if query_from_diff == '':
        query_from_diff = 'web'
    else:
        query_from_diff = query_from_diff


    params = {
        'queryString': query,
        'queryFrom': query_from,
    }

    params_diff = {
        'queryString': query,
        'queryFrom': query_from_diff,
    }

    params_utf16 = urlhandle.urlencode(params, 'utf-16le', 'ignore')

    params_diff_utf16 = urlhandle.urlencode(params_diff, 'utf-16le', 'ignore')

    headers = {"Content-type": "application/x-www-form-urlencoded;charset=UTF-16LE"}

    try:
        resp = requests.post(inputHost, data=params_utf16, headers=headers, timeout=3)
        resp_diff = requests.post(inputHost_diff, data=params_diff_utf16, headers=headers, timeout=3)
        status = resp.reason
        status_diff = resp_diff.reason

        if status != 'OK' or status_diff != 'OK':
            # print(sys.stderr, query, status, status_diff)
            ret['error'] = 'Error:未知的请求类型'
            ret['status'] = False
            return ret

        data = BeautifulSoup(resp.content.decode('utf-16le'),"html.parser")
        data_diff = BeautifulSoup(resp_diff.content.decode('utf-16le'),"html.parser")

        diff = difflib.HtmlDiff()

        ret['data'] = diff.make_table(data.prettify().splitlines(), data_diff.prettify().splitlines()).replace(
            'nowrap="nowrap"', '')

    except Exception as e:
        # print(e)
        # print(sys.stderr, sys.exc_info()[0], sys.exc_info()[1])
        ret['error'] = "Error:" + str(e)
        ret['status'] = False
    return HttpResponse(json.dumps(ret))

# @auth
def debug_save(request):
    user_id = "zhangjingjun"
    # user_id = request.COOKIES.get('uid')
    ret = {
        'status': True,
        'error': None,
        'data': None
    }
    inputHost = request.POST.get('inputHost')
    inputExpId = request.POST.get('inputExpId')
    query_from = request.POST.get('query_from')
    query = request.POST.get('query')

    try:
        models.DebugQo.objects.create(host_ip=inputHost, exp_id=inputExpId, query_from=query_from, query=query,
                                      user_fk_id=user_id)

        ret['inputHost'] = inputHost
        ret['inputExpId'] = inputExpId
        ret['query_from'] = query_from
        ret['query'] = query
    except Exception as e:
        ret['error'] = "Error:" + str(e)
        # print(e)
        ret['status'] = False
    return HttpResponse(json.dumps(ret))


# @auth
def debug_del(request):
    ret = {
        'status': True,
        'error': None,
        'data': None
    }
    req_id = request.POST.get('line_id')
    try:
        models.DebugQo.objects.filter(id=req_id).delete()
    except Exception as e:
        ret['status'] = False
        ret['error'] = "Error:" + str(e)
        # print(e)
    return HttpResponse(json.dumps(ret))




