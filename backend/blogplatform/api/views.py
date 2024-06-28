import rest_framework.viewsets

import api.serializers
import user.models


class ProfileViewSet(rest_framework.viewsets.ReadOnlyModelViewSet):
    queryset = user.models.UserProfile.objects.all()
    serializer_class = api.serializers.ProfileSerializer