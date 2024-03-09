# banco de dados remoto para salvar dados de treinamento de IA cheira peido

## como instalar?

para utilizar essa maravilha, você primeiro precisa preparar o seu ambiente virtual python.

```
python3 -m venv .venv
```

após isso você entra no ambiente virtual.

```
source .venv/bin/activate
```

aí você instala as bibliotecas necessárias.

```
pip install -r requirements.txt
```

## como usar?

para iniciar o servidor e começar a receber entradas (lá ele), você precisa rodar o arquivo `main.py`

```
python3 main.py
```

qualquer request post para a rota `/registrar_medicao` terá seu body salvo junto de uma timestamp, então não tem necessidade de mexer com data e hora no client.

para dar uma checada rápida nos dados, você pode acessar a rota `/pegar_medicoes`.

caso você precise acessar essa api por um dispositivo que não esteja na mesma rede, que é meu caso, você pode usar algumas ferramentas de port forwarding.

```
ngrok http 5000
```

agora, para extrair os dados necessários no bme ai studio, você pode rodar o arquivo `baixar_dados.py`.

```
python3 baixar_dados.json
```

ao rodar esse comando, você vai ser bem-vindo com um menu que se tudo der certo, você vai terminar com um arquivo que se parece mais ou menos com isso:

```csv
Timestamp,cavalo,vaca
1709940620,True,False
1709940621,True,False
1709940621,True,False
1709940621,True,False
1709940621,True,False
1709940621,True,False
1709940625,False,False
1709940625,False,False
```

## créditos

eu, joão, piovezan, chatgpt e deus :D
