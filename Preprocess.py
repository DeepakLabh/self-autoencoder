import re
import argparse

class process(object):
    def init(self, regex = None, data, lower = False, sent_keys=None):
        self.regex = regex
        self.data = data
        self.lower = lower
        self.sent_keys = sent_keys
        
    def clean(self):
    	if self.regex:
    		self.data[sent_keys] = self.data[sent_keys].apply(lambda x: re.sub(regex, ' ' x))
    	if self.lower:
    		self.data[sent_keys] = self.data[sent_keys].apply(lambda x: x.lower())

    	return data