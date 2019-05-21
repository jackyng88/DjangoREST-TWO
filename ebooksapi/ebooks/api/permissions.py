from rest_framework import permissions


class IsAdminUserOrReadOnly(permissions.IsAdminUser):
    # Class for Admins

    def has_permission(self, request, view):
        '''
        is_admin is called from super().has_permission. Which is a function
        that returns a boolean value. True is returned request.user and
        request.user.is_staff are both true.

        For the return - if is_admin == True or the HTTP method of the request
        are in the list of SAFE_METHODS which are ['GET', 'HEAD', 'OPTIONS'],
        i.e. methods that won't change the data/content of the database.
        '''
        is_admin = super().has_permission(request, view)
        return request.method in permissions.SAFE_METHODS or is_admin


class IsReviewAuthorOrReadOnly(permissions.BasePermission):
    # Class for specific review authors of an ebook, i.e. does not allow
    # other authors to edit another authors review.

    def has_object_permission(self, request, view, obj):
        if request.method in permissions.SAFE_METHODS:
            return True
        
        return obj.review_author == request.user