#import logging
from tropo import *

class Transcription(Result):
    """
    Returned anytime a request is made to the Tropo Web API.
    Method: getValue
    (See https://www.tropo.com/docs/webapi/result.htm)

        { "result": {
            "transcription": String,
            "guid": String,
            "identifier": String } }
    """
    options_array = ['transcription','guid','identifier']

    def __init__(self, result_json):
        logging.info ("result POST data: %s" % result_json)
        result_data = jsonlib.loads(result_json)
        result_dict = result_data['result']

        for opt in self.options_array:
            if result_dict.get(opt, False):
                setattr(self, '_%s' % opt, result_dict[opt])

    def getValue(self):
        """
        Get the value of the previously POSTed Tropo action.
        """
        transcription = self._transcription
        logging.info("Transcription is: %s" % transcription)
        return transcription
