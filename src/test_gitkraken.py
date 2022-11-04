data = """
server {
    listen       80;
    server_name  test%s.mobio.vn;

    location /mobile-cms {
        alias /home/projects/www_%s/mobile-cms/;
        #try_files $uri $uri/ /index.html;
        expires 1s;
    }
    location /micro-sites/ {
        alias /home/projects/www_%s/micro-sites/;
        try_files $uri $uri/ /index.html;
        expires 1s;
    }
}
"""
for x in range(1):
    print(data % (x, x, x))
