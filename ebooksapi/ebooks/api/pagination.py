from rest_framework.pagination import PageNumberPagination


class SmallSetPagination(PageNumberPagination):
    # Class that extends pagination for use with the API. Allows for pages.

    page_size = 3