

def getIdOfAuthenticatedUser(request):
    id=request.COOKIES.get('id')
    return int(id)