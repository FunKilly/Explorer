from .plan import Plan

def plan(request):
    return {'plan': Plan(request)}