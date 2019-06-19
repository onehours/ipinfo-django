from django.shortcuts import render, HttpResponse
from ipapp.lib.qqwry import qqwry


# Create your views here.

def index(request):
    # print(request.__dict__)
    ip = request.META.get('REMOTE_ADDR')
    czip = qqwry.CzIp()
    str = czip.get_addr_by_ip(ip).split()

    if 'curl' in request.META.get('HTTP_USER_AGENT'):


        msg = """IP	: {}
地址	: {}
运营商	: {}
""".format(ip, str[0], str[1])
    else:
#         msg = """
# <pre>IP	: {}
# 地址	: {}
# 运营商	: {}
# </pre>""".format(ip,str[0], str[1])
        dic = {
            'ip' : ip,
            'add': str[0],
            'isp': str[1],
        }
        return  render(request,'index.html',{'dic':dic})

    return HttpResponse(msg)


def getip(request):
    msg = request.META.get('REMOTE_ADDR')
    return HttpResponse(msg + '\n')


def seach(request, ip):
    czip = qqwry.CzIp()
    str = czip.get_addr_by_ip(ip).split()

    if 'curl' in request.META.get('HTTP_USER_AGENT'):

        msg = """IP	: {}
    地址	: {}
    运营商	: {}
    """.format(ip, str[0], str[1])
    else:
        #         msg = """
        # <pre>IP	: {}
        # 地址	: {}
        # 运营商	: {}
        # </pre>""".format(ip,str[0], str[1])
        dic = {
            'ip': ip,
            'add': str[0],
            'isp': str[1],
        }
        return render(request, 'index.html', {'dic': dic})

    return HttpResponse(msg)
