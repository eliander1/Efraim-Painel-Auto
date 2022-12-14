import pandas as pd
from datetime import date
import openpyxl

passageiros_em_transito = pd.read_excel('Planilhas/Efraimtur_Passageiros em  trânsito.xlsx', engine="openpyxl", sheet_name='Controle Passagens')

# ADICIONAR O DATA VOLTA
def Check_in_Aberto():
    passageiros = []

    for i, data in enumerate(passageiros_em_transito['DATA IDA']):
        str_data_ida = str(data).replace(' 00:00:00', '')
        date_data_ida = date(day=int(str_data_ida.split('-')[2]), month=int(str_data_ida.split('-')[1]), year=int(str_data_ida.split('-')[0]))
        data_checkin = date_data_ida - date.today()

        if 0 <= data_checkin.days < 3:
            passageiro = (str_data_ida, passageiros_em_transito['CIA / LOCALIZADOR'].iloc[i], passageiros_em_transito['PASSAGEIRO'].iloc[i])
            passageiros.append(passageiro)


    ## Adicionando Checkin da volta

    for i, data in enumerate(passageiros_em_transito['DATA VOLTA']):
        str_data_volta = str(data).replace(' 00:00:00', '')
        date_data_ida = date(day=int(str_data_volta.split('-')[2]), month=int(str_data_volta.split('-')[1]), year=int(str_data_volta.split('-')[0]))
        data_checkin = date_data_ida - date.today()

        if 0 <= data_checkin.days < 3:
            passageiro = (str_data_volta, passageiros_em_transito['CIA / LOCALIZADOR'].iloc[i], passageiros_em_transito['PASSAGEIRO'].iloc[i])
            passageiros.append(passageiro)

    df = pd.DataFrame(passageiros, columns=['DATA DE EMBARQUE', 'CIA / LOCALIZADOR', 'PASSAGEIRO'])
    print(df)
    df.to_excel('Planilhas/planilhas_do_sistema/checkin_aberto.xlsx', index=False, sheet_name='Checkin Aberto2')

