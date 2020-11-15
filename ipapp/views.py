from django.shortcuts import render, HttpResponse
from ipapp.lib.qqwry import qqwry
from ipapp.lib.ip2region import ip2


def index(request):
    # ip = request.META.get('REMOTE_ADDR')
    ip = request.META.get('HTTP_X_FORWARDED_FOR')
    if not ip:
        ip = '223.5.5.5'
    ip_dict = ip2.ip2region(ip)
    print(ip_dict)
    czip = qqwry.CzIp()
    ip_dict2 = czip.getip(ip)
    print(ip_dict2)

    if 'curl' in request.META.get('HTTP_USER_AGENT'):
        msg = f"""IP	: {ip}
地址    : {ip_dict['country']} | {ip_dict['region']}| {ip_dict['city']}
运营商  : {ip_dict['isp']}
数据二  : {ip_dict2['city']} | {ip_dict2['isp']}
"""
    else:
        dic = {
            'ip': ip,
            'add': f"{ip_dict['country']} | {ip_dict['region']}| {ip_dict['city']}",
            'isp': ip_dict['isp'],
            'data2': f"{ip_dict2['city']} | {ip_dict2['isp']}"
        }
        return render(request, 'index.html', {'dic': dic})

    return HttpResponse(msg)


def getip(request):
    ip = request.META.get('REMOTE_ADDR')
    ip = request.META.get('HTTP_X_FORWARDED_FOR')
    if not ip:
        ip = '223.5.5.5'
    if ',' in ip:
        ip = ip.split(',')[0]
    ip_dict = ip2.ip2region(ip)
    czip = qqwry.CzIp()
    ip_dict2 = czip.getip(ip)
    msg = f"{ip}  {ip_dict2['city']}  {ip_dict2['isp']}"
    return HttpResponse(msg + "\n")


def seach(request, ip):
    ip_dict = ip2.ip2region(ip)

    czip = qqwry.CzIp()
    ip_dict2 = czip.getip(ip)

    if 'curl' in request.META.get('HTTP_USER_AGENT'):
        msg = f"""IP	: {ip}
地址    : {ip_dict['country']} | {ip_dict['region']}| {ip_dict['city']}
运营商  : {ip_dict['isp']}
数据二  : {ip_dict2['city']} | {ip_dict2['isp']}
"""
    else:
        dic = {
            'ip': ip,
            'add': f"{ip_dict['country']} | {ip_dict['region']}| {ip_dict['city']}",
            'isp': ip_dict['isp'],
            'data2': f"{ip_dict2['city']} | {ip_dict2['isp']}"
        }
        return render(request, 'index.html', {'dic': dic})

    return HttpResponse(msg)
