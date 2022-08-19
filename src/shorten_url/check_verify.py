# import dnspython as dns
import dns.resolver
result = dns.resolver.resolve('ck.mobio.vn', 'CNAME')
for cnameval in result:
    print('cname target address:', cnameval.target)