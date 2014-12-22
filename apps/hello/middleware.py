from models import RequestInfo
from django.utils import timezone
import pickle


class RequestsToDataBase(object):
	def process_request(self, request):
		pickledRequest = pickle.dumps(request.REQUEST)
		ri = RequestInfo(pickled_request=pickledRequest)
		ri.save()