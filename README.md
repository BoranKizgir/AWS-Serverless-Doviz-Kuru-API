# AWS-Serverless-D-viz-Kuru-API
Bu proje, AWS üzerinde sunucusuz (serverless) bir mimari kullanarak döviz kurlarını kaydeden ve bir API üzerinden sunan bir uygulamadır.



## Mimari Yapı


1. **Amazon API Gateway:** Kullanıcının HTTP isteğini karşılar.
2. **AWS Lambda:** İş mantığını yürütür (Dış API'den veri çeker ve işler).
3. **Amazon DynamoDB:** Döviz kurlarını NoSQL formatında saklar.
4. **IAM:** Servisler arası güvenli yetkilendirmeyi sağlar.

## Özellikler
- **Serverless:** Sunucu yönetimi gerektirmez, sadece çalıştığı kadar maliyet çıkarır.
- **Ölçeklenebilir:** İstek sayısı arttıkça AWS otomatik olarak ölçeklenir.
- **Free-Tier Friendly:** Tamamen ücretsiz katman limitleri dahilindedir.

## Kurulum
1. DynamoDB'de `DovizKurTablosu` adında bir tablo oluşturuldu (Partition Key: `DovizCinsi`).
2. Lambda fonksiyonu oluşturuldu.
3. Lambda'ya `AmazonDynamoDBFullAccess` izni verildi.
4. API Gateway (HTTP API) tetikleyicisi eklendi.

## Geliştirme Planı
- [ ] Gerçek bir döviz kuru API'si entegrasyonu (TCMB veya ExchangeRate API).
- [ ] Frontend (HTML/JS) eklenerek verilerin görselleştirilmesi.
