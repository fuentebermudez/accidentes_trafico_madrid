
import requests

example_headers = {'User-Agent':'Mozilla/5.0 (Windows NT 10.0; WOW64; rv:50.0) Gecko/20100101 Firefox/50.0'}

url="https://datos.madrid.es/portal/site/egob/menuitem.ac61933d6ee3c31cae77ae7784f1a5a0/?vgnextoid=00149033f2201410VgnVCM100000171f5a0aRCRD&mgmtid=374512b9ace9f310VgnVCM100000171f5a0aRCRD&search=keyword/trafico&preview=full&format=json"
response=requests.get(url,headers=example_headers)
print(response.headers['content-type'])

#soup=bs4.BeautifulSoup(response.text,"html.parser")
response=response.json()
accidentes_trafico_años=response["result"]["items"][1]["distribution"]
year=1
for año in accidentes_trafico_años:
    URL_xlsx=año["accessURL"]
    with open(('D:\\borrar\\'+str(year)+".xlsx"), 'wb') as f:
        response = requests.get(URL_xlsx,headers=example_headers)
        print(response.headers)
        f.write(response.content)
        f.close()
    year=year+1
