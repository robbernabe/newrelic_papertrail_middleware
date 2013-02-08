import time
import socket
import newrelic.agent


class NewRelicPapertrailMiddleware(object):
    """
    Add a link to related logs in Papertrail via NewRelic custom parameters.

    This module will need to be added to MIDDLEWARE_CLASSES in Django settings
    in order to work.

    """

    def process_response(self, request, response):
        """
        Add the system hostname and current timestamp parameters

        """

        # Sample data we want to append
        hostname = str(socket.gethostname())
        timestamp = str(int(time.time()))

        # Papertrail Log Url
        log_url = "https://papertrailapp.com/systems/%s/events?time=%s" % (hostname, timestamp)

        # Add the custom parameters
        newrelic.agent.add_custom_parameter('log_url', log_url)

        return response
