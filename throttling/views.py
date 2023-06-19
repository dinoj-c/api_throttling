from django.http import HttpResponse


def throttling_example(request):

    return HttpResponse("This is a throttling enabled response!")
