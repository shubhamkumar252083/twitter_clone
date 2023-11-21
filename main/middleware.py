# middleware.py
import time

class RequestTimingMiddleware:
    def __init__(self, get_response):
        self.get_response = get_response

    def __call__(self, request):
        # Code to be executed for each request before
        # the view (and later middleware) are called.
        start_time = time.time()
        print(f"@@@@@@@@@@@@@ --> Request started at: {start_time}")

        response = self.get_response(request)

        # Code to be executed for each request/response after
        # the view is called.

        end_time = time.time()
        elapsed_time = end_time - start_time

        print(f"@@@@@@@@@@@@@ --> Request completed at: {end_time}")
        print(f"Elapsed time: {elapsed_time} seconds")

        return response
