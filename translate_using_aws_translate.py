import boto3

translate = boto3.client(service_name='translate', region_name='us-east-1', use_ssl=True)

data = 'test translation'
result = translate.translate_text(Text=data,
                                  SourceLanguageCode="en", TargetLanguageCode="es")

print(result.get('TranslatedText'))
