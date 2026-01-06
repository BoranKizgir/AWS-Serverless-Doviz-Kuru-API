Python 3.12.4 (tags/v3.12.4:8e8a4ba, Jun  6 2024, 19:30:16) [MSC v.1940 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
>>> import json
... import boto3
... 
... def lambda_handler(event, context):
...     dynamodb = boto3.resource('dynamodb')
...     table = dynamodb.Table('DovizKurTablosu')
...     
...     # Simüle edilmiş döviz verisi (İleride bir API'den çekilebilir)
...     doviz_verisi = {
...         'DovizCinsi': 'USD',
...         'Birim': 'Amerikan Dolari',
...         'Deger': '43.04'
...     }
...     
...     # Veriyi DynamoDB'ye kaydet
...     table.put_item(Item=doviz_verisi)
...     
...     return {
...         'statusCode': 200,
...         'body': json.dumps(f"Basarili! {doviz_verisi['DovizCinsi']} kuru {doviz_verisi['Deger']} olarak guncellendi.")
