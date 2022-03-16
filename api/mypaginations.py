from rest_framework.pagination import PageNumberPagination, LimitOffsetPagination, CursorPagination


class MyPageNumberPagination(PageNumberPagination):
    page_size = 5
    page_query_param = 'pages'
    # page_size_query_param = 'records'
    # max_page_size = 7
    # last_page_strings = 'end'


class MyLimitOffsetPagination(LimitOffsetPagination):
    default_limit = 5
    # limit_query_param = 'mylimit'
    # offset_query_param = 'myoffset'


class MyLimitCursoragination(CursorPagination):
    page_size = 3
    ordering = 'id'
