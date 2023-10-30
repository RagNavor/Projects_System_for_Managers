from django.contrib.auth.models import Permission
from django.contrib.contenttypes.models import ContentType

creator_permission = Permission.objects.create(
    codename='creator_worspace',
    name='creator worspace'
)
area_lead_permission = Permission.objects.create(
    codename='area_lead_worspace',
    name='area lead worspace'
)
collaborator_permission = Permission.objects.create(
    codename='collaborator_worspace',
    name='collaborator worspace'
)