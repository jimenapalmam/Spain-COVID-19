## FIRST PROGRAMM FOR DATA ANALISYS FOR COVID-19

# Import packages
import pandas as pd
import matplotlib as plt

# Import file
df = pd.read_csv('serie_historica_acumulados.csv', encoding='utf-8')
print(df.head(50))

# See missing data in columns
missing_data = df.isnull()
print(missing_data)

#_Count missing values in each column
for column in missing_data.columns.values.tolist():
    print(column)
    print(missing_data[column].value_counts())
    print("")

#Deal with missing data
#Replace NaN for 0 values
df.fillna(0, inplace=True)
print(df.head())

# Correct data format
print(df.dtypes) # DAta format is correct

#Dummy indicator for CCAA
dummy_variable_1 = pd.get_dummies(df["CCAA"])
print(dummy_variable_1.head())

    #Eliminate tex columns
dummy_variable_1.drop("Los datos de estas comunidades son datos de "
                      "prevalencia (personas ingresadas a fecha de hoy). No "
                      "reflejan el total de personas que han sido "
                      "hospitalizadas o ingresadas en UCI\xa0 a lo largo del "
                    "periodo de notificación(CL(UCIs)-CM-MD-MC)",
                      axis= 1, inplace=True)

dummy_variable_1.drop("NOTA: El objetivo de los datos que se publican en esta "
                    "web es saber el número de casos acumulados a la fecha y "
                    "que por tanto no se puede deducir que la diferencia entre "
                    "un día y el anterior es el número de casos nuevos ya que "
                    "esos casos pueden haber sido recuperados de fechas "
                    "anteriores. Cualquier inferencia que se haga sobre las "
                    "diferencias de un día para otro deben hacerse con "
                    "precaución y son únicamente la responsabilidad el autor.",
                      axis= 1, inplace=True)

dummy_variable_1.drop(0, axis= 1, inplace=True)
print(dummy_variable_1.columns.values)

    #Give a right name for each column
dummy_variable_1.rename(columns={'AN':'ANDALUCIA','AR':'ARAGON',
                                 'AS':'ASTURIAS',
                                 'CB':'CANTABRIA','CE':'CEUTA',
                                 'CL':'CASTILLA Y LEON',
                                 'CM':'CASTILLA Y LA MANCHA',
                                 'CN':'NAVARRA', 'CT':'CATALUÑA',
                                 'EX':'EXTREMADURA','GA':'GALICIA',
                                 'IB':'ISLAS BALEARES',
                                 'MD':'MADRID','MC':'MURCIA','ML':'MELILLA',
                                 'NC':'CANARIAS','PV':'PAIS VASCO',
                                 'RI':'RIOJA','VC':'COMUNIDAD VALENCIANA'},
                                inplace=True)

print(dummy_variable_1.columns.values)

    #Merge dummy_variable_1 with Dataframe
df=pd.concat([df, dummy_variable_1], axis = 1)
print(df.head())