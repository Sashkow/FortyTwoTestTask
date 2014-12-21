from models import RequestInfo

import pickle


class RequestsToDataBase(object):

	def process_request(self, request):
		# pickledRequest = pickle.dumps(request)
		ri = RequestInfo(pickled_request = "pickledRequest")
		ri.save()