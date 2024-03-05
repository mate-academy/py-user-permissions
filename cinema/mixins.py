from django.http import Http404


class PermissionMixin:
    def get_permissions(self):
        if self.action in ["retrieve", "update", "partial_update", "destroy"]:
            raise Http404
        return super().get_permissions()
