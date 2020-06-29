from rest_framework import generics, permissions
from django.db.models import Q
from backend.callboard.models import Advert
from backend.callboard.serializers import AdvertListSerializer


class SearchAdvertListRestApi(generics.ListAPIView):
    '''Поиск в списке объявлений'''
    serializer_class = AdvertListSerializer
    permission_classes = [permissions.AllowAny]

    def get_queryset(self):
        search = self.request.GET.get('search')
        # print('====== search ========>',search)
        filter = []
        a = Q()
        a |= Q(subject__icontains=search)
        a |= Q(category__name__icontains=search)
        a |= Q(filter__name__icontains=search)
        # a |= Q(price=search) #ValidationError at /search/
        # value must be a decimal number.']
        # то есть если я делаю поиск и по числовым и текстовым, то при поиске текста
        # в числовом поле, даст ошибку
        # К сожалению функция isdigit не работает для чисел с плавающей точкой
        # и для отрицательных чисел. Так что для такой проверки можно
        # использовать следующую функцию, которая представляет собой
        # комбинацию из проверки isdigit и обычного конвертирования во float:
        # поэтому так:

        def is_digit(search):
            if search.isdigit():
                return True
            else:
                try:
                    float(search)
                    return True
                except ValueError:
                    return False
        if is_digit(search):
            a |= Q(price=search)

        filter.append(a)

        return Advert.objects.filter(*filter)
