credentials = {}

# Django secret key
credentials["SECRET_KEY"] = '4k=bt$!-jg$94toufi405h_ct48k=xeod@f(u4jpgb%u&cc9^1'

# Local machine Database
credentials['local_host'] = 'localhost'
credentials['local_port'] = '3306'
credentials['local_user'] = 'bookuser'
credentials['local_pwd'] = 'bookuser'
credentials['local_name'] = 'bookstore'

# AWS RDS MySQL Database
credentials['dev_host'] = 'bookstore-db.czjpnwmwrggk.us-east-2.rds.amazonaws.com'
credentials['dev_port'] = '3306'
credentials['dev_user'] = 'vissu'
credentials['dev_pwd'] = 'vissu6793'
credentials['dev_name'] = 'bookstore'

# AWS RDS MySQL Database
credentials['prod_host'] = 'bookstore-db.czjpnwmwrggk.us-east-2.rds.amazonaws.com'
credentials['prod_port'] = '3306'
credentials['prod_user'] = 'vissu'
credentials['prod_pwd'] = 'vissu6793'
credentials['prod_name'] = 'bookstore'

# Django Email backend settings
credentials['EMAIL_BACKEND'] = 'django.core.mail.backends.smtp.EmailBackend'
credentials['EMAIL_HOST'] = 'smtp.gmail.com'
credentials['EMAIL_PORT'] = 587
credentials['EMAIL_HOST_USER'] = 'djangoclient97@gmail.com'
credentials['EMAIL_HOST_PASSWORD'] = 'django@0621'
credentials['EMAIL_USE_TLS'] = True    # 587
credentials['EMAIL_USE_SSL'] = False   # 465

# Django celery backend settings
credentials['CELERY_BROKER_URL'] = 'redis://localhost:6379'
credentials['CELERY_RESULT_BACKEND'] = 'redis://localhost:6379'
credentials['CELERY_ACCEPT_CONTENT'] = ['application/json']
credentials['CELERY_TASK_SERIALIZER'] = 'json'
credentials['CELERY_RESULT_SERIALIZER'] = 'json'
credentials['CELERY_TIMEZONE'] = 'Africa/Nairobi'

# AWS S3 Settings
credentials['AWS_ACCESS_KEY_ID'] = 'AKIA4UHBMKKHP26SYYNR'
credentials['AWS_SECRET_ACCESS_KEY'] = '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'
credentials['AWS_STORAGE_BUCKET_NAME'] = 'bookstore-user-profile-images'
credentials['DEFAULT_FILE_STORAGE'] = 'storages.backends.s3boto3.S3Boto3Storage'
credentials['AWS_DEFAULT_ACL'] = None           # ACL means Access Control List. by default inherits the bucket permissions.
credentials['AWS_S3_FILE_OVERWRITE'] = True    # By default files with the same name will overwrite each other. True by default.
credentials['AWS_S3_REGION_NAME'] = 'us-east-2' # change to your region
credentials['STATICFILES_STORAGE'] = 'storages.backends.s3boto3.S3Boto3Storage'        # To serve static file like css, js from AWS S3.
