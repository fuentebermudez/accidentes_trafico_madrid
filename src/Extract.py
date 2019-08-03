import requests
import os
import pandas as pd


def extrae_datos_ayuntamiento(url,path_salida,n_item=0,id_archivo=""):
    
    directory=path_salida

    example_headers = {'User-Agent':'Mozilla/5.0 (Windows NT 10.0; WOW64; rv:50.0) Gecko/20100101 Firefox/50.0'}
    response=requests.get(url,headers=example_headers)

    response=response.json()
    accidentes_trafico_años=response["result"]["items"][n_item]["distribution"]
    year=1
    for año in accidentes_trafico_años:
        URL_xlsx=año["accessURL"]
        nombre=año["title"]
        with open((directory+ "\\" +nombre+"_" + id_archivo + ".xlsx"), 'wb') as f:
            response = requests.get(URL_xlsx,headers=example_headers)
            f.write(response.content)
            f.close()
        year=year+1



def carga_accidentes(directory):
    files=os.listdir(directory)
    files=[directory+ '\\' +file for file in files if "accidentes" in file]
    data=[]
    for file in files:
        content=pd.read_excel(file)
        content.columns=['FECHA','RANGO HORARIO','DIA SEMANA','DISTRITO','LUGAR ACCIDENTE','Nº','Nº PARTE','CPFA Granizo','CPFA Hielo','CPFA Lluvia','CPFA Niebla','CPFA Seco','CPFA Nieve','CPSV Mojada','CPSV Aceite','CPSV Barro','CPSV Grava Suelta','CPSV Hielo','CPSV Seca Y Limpia','VICTIMAS','TIPO ACCIDENTE','Tipo Vehiculo','TIPO PERSONA','SEXO','LESIVIDAD','Tramo Edad']
        data.append(content)
    merged_data=pd.concat(data)
    return merged_data

def carga_informes_policiales(directory):
    
    files=os.listdir(directory)
    files=[directory+ '\\' +file for file in files if "policia" in file]
    data=[]
    for file in files:
        content=pd.read_excel(file,sheet_name='ALCOHOLEMIAS')
        content.columns=['TIPOS','N_PRUEBAS']
        totales=content[content['TIPOS']=='TOTAL']
        totales=totales.assign(AÑO=file.split(".")[1][1:])
        data.append(totales)
    pruebas_alcoholemia=pd.concat(data)
    return pruebas_alcoholemia