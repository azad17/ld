
class HeaderExtendMiddleware():

    def __init__(self,get_response):
        self.get_response = get_response

    def __call__(self, request):
        response = self.get_response(request)
        response["app_version"]="1.2"
        return response

