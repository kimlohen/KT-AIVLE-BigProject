from storages.backends.s3boto3 import S3Boto3Storage

SECRET_KEY = 'SECRET_KEY'

# MYSQL
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.mysql',
        'NAME': "BACKEND", # 연동할 DB 이름
        'USER': 'root',
        'PASSWORD': 'password',
        'HOST':'AWS RDS HOST',
        'PORT': '3306',        
    }
}

# AWS
AWS_ACCESS_KEY_ID = 'AWS Access key ID' # .csv 파일에 있는 내용을 입력 Access key ID
AWS_SECRET_ACCESS_KEY = 'AWS Secret Access key' # .csv 파일에 있는 내용을 입력 Secret access key
AWS_REGION = 'ap-northeast-2'

# S3 Storages
AWS_STORAGE_BUCKET_NAME = 'bigproj-bucket' # 설정한 버킷 이름
AWS_S3_CUSTOM_DOMAIN = '%s.s3.%s.amazonaws.com' % (AWS_STORAGE_BUCKET_NAME,AWS_REGION)

class MediaStorage(S3Boto3Storage):
    location = 'media'
    file_overwrite = False

# Gmail 설정
EMAIL_HOST_USER = "email" # 발신할 이메일
EMAIL_HOST_PASSWORD = "password"    # 발신할 메일의 비밀번호

openai_apiKey = "OpenAI API key"
