from datetime import datetime, timedelta



class DatasBr:
    def __init__(self):
        self.momento_cadastro = datetime.today()


    def mes_cadastro(self):
        meses_do_ano = ['Janeiro','Fevereiro','Março','Abril','Maio','Junho','Julho','Agosto','Setembro','Outubro','Novembro','Dezembro']
        mes = self.momento_cadastro.month -1
        return meses_do_ano[mes]

     
    def dia_semana(self):
        dia_semana = ['Segunda','Terça','Quarta','Quinta','Sexta','Sábado','Domingo']
        dia = self.momento_cadastro.weekday()
        return dia_semana[dia]


    def format_data(self):
        data_formatada = self.momento_cadastro.strftime("%d/%m/%Y %H:%M")  
        return data_formatada  

    
    def tempo_cadastro(self):
        tempo = (datetime.today() + timedelta(days=30, hours=18)) - self.momento_cadastro
        return tempo
        