from rest_framework import permissions


class UpdateOwnProfile(permissions.BasePermission):
    """Allow user to edit their own profile"""

    def has_object_permission(self, request, view, obj):
        """Chick the user is trying to edit their own profile"""
        if request.mathod in permissions.SAFE_METHODS:  # this mean: if the method is being used is http GET , then it
            # will be in the SAFE_METHOD
            return True

        return obj.id == request.user.id  # if the id of a user is match to the object of specific field user is
        # attempt to make changes on it,  this mean this user has this object and he can updated it. Otherwise if it
        # is not match is mean this object is not bellowing to this user and then it will return false. HTTP METHOD
        # 'DELETE', 'PUT, 'PATCH'.


