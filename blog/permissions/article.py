from combojsonapi.permission import (PermissionForPatch, PermissionMixin,
                                     PermissionUser)
from flask_combo_jsonapi.exceptions import AccessDenied
from flask_login import current_user

from blog.models import Article


class ArticlePatchPermission(PermissionMixin):
    """Describe permission for patch Article.
    Example request:
    curl --location --request PATCH 'http://127.0.0.1:5010/api/articles/3/' \
    --header 'Content-Type: application/json' \
    --data-raw
        {
          "data": {
            "type": "article",
            "id": "3",
            "attributes": {
              "text": "string",
              "title": "string"
            }
          }
        }
    """

    PATCH_AVAILABLE_FIELDS = (
        'title',
        'text',
    )

    def patch_permission(self, *args, user_permission: PermissionUser = None, **kwargs) -> PermissionForPatch:
        self.permission_for_patch.allow_columns = (self.PATCH_AVAILABLE_FIELDS, 10)
        return self.permission_for_patch

    def patch_data(self, *args, data=None, obj=None, user_permission: PermissionUser = None, **kwargs) -> dict:
        if obj.author_id == current_user.id or current_user.is_staff:
            permission_for_patch = user_permission.permission_for_patch_permission(model=Article)
            return {
                k: v
                for k, v in data.items()
                if k in permission_for_patch.columns
            }
        else:
            raise AccessDenied("no access")
