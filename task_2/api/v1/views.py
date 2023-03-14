import asyncio

import pandas
from rest_framework import views, status
from rest_framework.response import Response

from api.models import Product
from api.v1.serializers import (
    GetSerializer,
)
from wildberries_api.get_data import main


class ProductView(views.APIView):
    """Allows post with single article as a JSON or xlsx file with articles"""

    def object_create(self, products):
        """Create DRF Product instances"""
        prod_insts = []
        for product in products:
            prod_inst = Product.objects.create(
                article=product[0].article,
                brand=product[0].brand,
                title=product[0].title,
            )
            prod_insts.append(prod_inst)
        return prod_insts

    def post(self, request):
        # Check if file is uploaded
        if 'file' in request.FILES:
            file = request.FILES['file']
            if '.xlsx' not in file.name:
                return Response({'error': 'File extenshion should be .xlsx'})
            df = pandas.read_excel(file, header=None)
            # get the first column values
            articles = df.iloc[:, 0].tolist()

            products = asyncio.run(main(articles))
            try:
                prod_insts = self.object_create(products)
            except IndexError:
                return Response(
                    {'error': 'probably one of articles doesn\'t exist'}
                )

            # Serialize the products and return a JSON response
            serializer = GetSerializer(prod_insts, many=True)
            return Response(serializer.data, status=status.HTTP_200_OK)

        # Check if articles are passed as text
        elif request.data:
            articles = []
            article = request.data.get('article')
            if article:
                if not str(article).isnumeric():
                    return Response(
                        {'error': 'Article should be the whole number!'}
                    )

                articles.append(article)
            else:
                return Response(
                    {
                        'error': 'If you try to send article: check if input field name is article and article is the only one! If you send a file: you didn\'t attach a file'
                    }
                )

        else:
            return Response({'error': 'Please provide a file or articles.'})

        # Fetch the brand and title for each article using aiohttp and WildBerries API
        products = asyncio.run(main(articles))
        try:
            prod_insts = self.object_create(products)
        except IndexError:
            return Response({'error': 'article doesn\'t exist'})

        serializer = GetSerializer(prod_insts[0], many=False)
        return Response(serializer.data)
