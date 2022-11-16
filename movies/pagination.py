from rest_framework import pagination
from rest_framework.response import Response
import environ
env=environ.Env(
    DEBUG=(bool, False)
)
class CustomPagination(pagination.PageNumberPagination):
    def get_paginated_response(self, data):
        print("pagination",self.__dict__)
        array=[]
        for x in range(self.page.paginator.num_pages):
            array.append({
                "label":x+1,
                "link":"{host}/api/movies/?page={page}".format(page=x+1,host=env("HOST")),
                "active":self.page.number==x+1
            })
        return Response({
            'links': [
                {
                    "label":"previous",
                'link': self.get_previous_link(),
                },
                *array
                ,
                {
                    "label":"next",
                    
                'link': self.get_next_link(),
                }
            ],
            'total': self.page.paginator.count,
            'entries': data
        })