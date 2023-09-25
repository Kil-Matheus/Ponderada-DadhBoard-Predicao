import streamlit as st
import pandas as pd
from pycaret.regression import load_model, predict_model

# Load trained Pipeline
model = load_model("minha_api")

# Crie o aplicativo Streamlit
st.title("Previsão de Acidentes")
st.write("Insira os dados abaixo para prever o número de acidentes.")

# Formulário para inserção de dados
data = st.date_input("Data:")
km = st.number_input("Quilômetros percorridos:")
bicicleta = st.number_input("Bicicletas:")
caminhao = st.number_input("Caminhões:")
moto = st.number_input("Motos:")
onibus = st.number_input("Ônibus:")
outros = st.number_input("Outros:")
tracao_animal = st.number_input("Tração Animal:")
trator_maquinas = st.number_input("Trator/Máquinas:")
utilitarios = st.number_input("Utilitários:")
Autopista_Fernao_Dias = st.number_input("Autopista Fernão Dias:")
Autopista_Fluminense = st.number_input("Autopista Fluminense:")
Autopista_Litoral_Sul = st.number_input("Autopista Litoral Sul:")
Autopista_Planalto_Sul = st.number_input("Autopista Planalto Sul:")
Autopista_Regis_Bittencourt = st.number_input("Autopista Regis Bittencourt:")
Concebra = st.number_input("Concebra:")
Concepa = st.number_input("Concepa:")
Concer = st.number_input("Concer:")
Cro = st.number_input("Cro:")
Crt = st.number_input("Crt:")
ECO050 = st.number_input("ECO050:")
ECO101 = st.number_input("ECO101:")
Ecoponte = st.number_input("Ecoponte:")
Ecoriominas = st.number_input("Ecoriominas:")
Ecosul = st.number_input("Ecosul:")
Ecovias_do_Araguaia = st.number_input("Ecovias do Araguaia:")
Ecovias_do_Cerrado = st.number_input("Ecovias do Cerrado:")
MSVIA = st.number_input("MSVIA:")
Novadutra = st.number_input("Novadutra:")
RIOSP = st.number_input("RIOSP:")
Rodovia_do_Aco = st.number_input("Rodovia do Aço:")
Transbrasiliana = st.number_input("Transbrasiliana:")
VIA040 = st.number_input("VIA040:")
Via_Bahia = st.number_input("Via Bahia:")
Via_Brasil = st.number_input("Via Brasil:")
Via_Costeira = st.number_input("Via Costeira:")
Via_Sul = st.number_input("Via Sul:")
BA = st.number_input("BA:")
CW = st.number_input("CW:")
DF = st.number_input("DF:")
ES = st.number_input("ES:")
GO = st.number_input("GO:")
MG = st.number_input("MG:")
MS = st.number_input("MS:")
MT = st.number_input("MT:")
PA = st.number_input("PA:")
PR = st.number_input("PR:")
RJ = st.number_input("RJ:")
RS = st.number_input("RS:")
SC = st.number_input("SC:")
SP = st.number_input("SP:")
accidents = st.number_input("Acidentes:")

# Botão para fazer a previsão
if st.button("Fazer Previsão"):
    # Crie um dicionário com os dados de entrada
    input_data = {
        "data": data,
        "km": km,
        "bicicleta": bicicleta,
        "caminhao": caminhao,
        "moto": moto,
        "onibus": onibus,
        "outros": outros,
        "tracao_animal": tracao_animal,
        "trator_maquinas": trator_maquinas,
        "utilitarios": utilitarios,
        "Autopista_Fernao_Dias": Autopista_Fernao_Dias,
        "Autopista_Fluminense": Autopista_Fluminense,
        "Autopista_Litoral_Sul": Autopista_Litoral_Sul,
        "Autopista_Planalto_Sul": Autopista_Planalto_Sul,
        "Autopista_Regis_Bittencourt": Autopista_Regis_Bittencourt,
        "Concebra": Concebra,
        "Concepa": Concepa,
        "Concer": Concer,
        "Cro": Cro,
        "Crt": Crt,
        "ECO050": ECO050,
        "ECO101": ECO101,
        "Ecoponte": Ecoponte,
        "Ecoriominas": Ecoriominas,
        "Ecosul": Ecosul,
        "Ecovias_do_Araguaia": Ecovias_do_Araguaia,
        "Ecovias_do_Cerrado": Ecovias_do_Cerrado,
        "MSVIA": MSVIA,
        "Novadutra": Novadutra,
        "RIOSP": RIOSP,
        "Rodovia_do_Aco": Rodovia_do_Aco,
        "Transbrasiliana": Transbrasiliana,
        "VIA040": VIA040,
        "Via_Bahia": Via_Bahia,
        "Via_Brasil": Via_Brasil,
        "Via_Costeira": Via_Costeira,
        "Via_Sul": Via_Sul,
        "BA": BA,
        "CW": CW,
        "DF": DF,
        "ES": ES,
        "GO": GO,
        "MG": MG,
        "MS": MS,
        "MT": MT,
        "PA": PA,
        "PR": PR,
        "RJ": RJ,
        "RS": RS,
        "SC": SC,
        "SP": SP,
        "accidents": accidents
    }

    # Faça a previsão usando o modelo
    input_data = pd.DataFrame([input_data])
    input_data.rename(columns=lambda x: x.replace("_", " "), inplace=True)
    predictions = predict_model(model, data=input_data)

    # Exiba a previsão
    prediction_label = predictions["prediction_label"].iloc[0]
    st.write(f"Previsão de Acidentes: {prediction_label}")