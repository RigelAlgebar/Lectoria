import pandas as pd
import os

text = open("https://github.com/RigelAlgebar/Lectoria/tree/master/src/pages/input-files/Doc1.txt","r")
text = text.read()

df = pd.read_csv("https://github.com/RigelAlgebar/Lectoria/tree/master/src/pages/input-files/Doc1.csv",sep = ',', header = None, skiprows = 1)
df2 = pd.read_csv("https://github.com/RigelAlgebar/Lectoria/tree/master/src/pages/input-files/Doc2.csv",sep = ',', header = None, skiprows = 1)

df[0] = df[0].fillna("nulo")
df2[0] = df2[0].fillna("nulo")

def correct_syntax(s):
    replaced = ""
    try:
        string = s.lower()
        if "efectiv" in string or "caja" in string or "banco" in string:
            replaced += "Caja y bancos"
            return replaced
        elif "total activ" in string or "suma de los activ" in string or "activo tot" in string:
            if len(string.split()) == 2:
                return "Total activo"
            else:
                return string
        elif "total pasiv" in string or "suma de los pasivos" in string or "pasivo tot" in string:
            if len(string.split()) == 2:
                return "Total pasivo"
            else:
                return string
        elif "total patrimonio" in string or "suma de los patrimonios" in string or "patrimonio total" in string or "capital contable" in string:
            replaced += "Total patrimonio"
            return replaced
        elif "costo de venta" in string or "costos de venta" in string or "costos por ventas" in string or "costo de actividades ordinarias" in string or "costos" in string:
            replaced += "Costo de ventas"
            return replaced
        elif "ventas" in string or "ventas por operacion" in string or "ingresos por operacion" in string or "ingresos operacionales" in string or "ventas brutas" in string or "ingreso por actividades ordinarias" in string:
            replaced += "Ventas"
            return replaced
        elif "ganancia brut" in string or "utilidad brut" in string or "perdida brut" in string:
            replaced += "Utilidad bruta"
            return replaced
        elif "utilidad operacional" in string or "perdida operacional" in string or "resultado de la operacion" in string:
            replaced += "Utilidad operacional"
            return replaced
        elif "utilidad antes de impuesto" in string or "perdida antes de impuesto" in string:
            replaced += "Utilidad antes de impuestos"
            return replaced
        elif "utilidad neta" in string or "perdida neta" in string:
            replaced += "Utilidad neta"
            return replaced
        else:
            return s
    except:
        pass

df[0] = df[0].apply(lambda x : correct_syntax(x))
df2[0] = df2[0].apply(lambda x : correct_syntax(x))

def final_table(dataframe):
    return dataframe[dataframe[0].isin(["Caja y bancos","Total activo","Total pasivo","Total patrimonio","Ventas",
    "Costo de ventas","Utilidad bruta","Utilidad operacional","Utilidad antes de impuestos","Utilidad neta"])]

def concat_tables(a,b):
    a = final_table(a)
    b = final_table(b)
    df_concat = pd.concat([a,b])[[0,2]].transpose()
    headers =df_concat.iloc[0]
    final = pd.DataFrame(df_concat.values[1:], columns=headers)
    return final

final = concat_tables(df,df2)

def to_negative(string):
    if "(" in string:
        return "-" + string.split("(")[1].split(")")[0]
    else:
        return string

final.loc[0] = final.loc[0].apply(lambda x : to_negative(x))

def unidad_medida(x):
    unidad = ""
    if "millon" in x:
        unidad += "Millones"
    if "miles" in x:
        unidad += "Miles"
    if "peso" in x:
        unidad += " de pesos"
    if "dolar" in x:
        unidad += " de dólares"
    if "colombia" in x:
        unidad += " colombianos"
    if "mexican" in x:
        unidad += " mexicanos"
    if "chile" in x:
        unidad += " chilenos"
    return unidad

def get_fecha(x):
    fecha = ""
    if "2019" in x:
        fecha += "2019"
    elif "2018" in x:
        fecha += "2018"
    else:
        fecha += "campo vacío"
    return fecha

def insert_cols(dataframe):
    try:
        dataframe.insert(0, "Fecha", get_fecha(text))
    except:
        dataframe.insert(0, "Fecha", "N/A")
    try:
        dataframe.insert(1, "Unidades de medida", unidad_medida(text))
    except:
        dataframe.insert(1, "Unidades de medida", "N/A")

insert_cols(final)
path = 'https://github.com/RigelAlgebar/Lectoria/tree/master/src/pages/output-files'
output_file = os.path.join(path,'key_fields.csv')
final.to_csv(output_file, index=False)
