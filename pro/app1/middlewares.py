def middlewares(get_response):
    def fun(request):
        print('Before Session Created')
        response=get_response(request)
        print('After Session Created')
        return response
    return fun