#New Relic/Papertrail Django Middleware

Add a link in New Relic to related logs in Papertrail via custom parameters.

##Installation

Add the middleware class to your `MIDDLEWARE_CLASSES` in your Django settings:

    MIDDLEWARE_CLASSES = (
        'django.middleware.common.CommonMiddleware',
        'django.contrib.sessions.middleware.SessionMiddleware',
        'django.middleware.csrf.CsrfViewMiddleware',
        'django.contrib.auth.middleware.AuthenticationMiddleware',
        'django.contrib.messages.middleware.MessageMiddleware',
        'path.to.middleware.NewRelicPapertrailMiddleware',
    )

##Resources

* <http://help.papertrailapp.com/kb/integrations/new-relic>
* <https://newrelic.com/docs/python/python-transaction-api#add_custom_parameter>
* <https://docs.djangoproject.com/en/dev/topics/http/middleware/>
