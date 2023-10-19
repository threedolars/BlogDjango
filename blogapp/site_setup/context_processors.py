from site_setup.models import SiteSetup


def context_process_exemple(request):
    return {
        'example': 'This was sended by context_process_exemple'
    }


def site_setup(request):
    setup = SiteSetup.objects.order_by('-id').first()

    return {
        'site_setup': setup,
    }
