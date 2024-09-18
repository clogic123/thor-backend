from ninja import Swagger

from contrib.django.ninja.main import ContribNinjaAPI
from contrib.django.ninja.parser import CamelParser
from contrib.django.ninja.renderer.case import CamelCaseRenderer

app = ContribNinjaAPI(
    docs=Swagger(
        settings={"persistAuthorization": True, "filter": True, "tryItOutEnabled": True}
    ),
    renderer=CamelCaseRenderer(),
    parser=CamelParser(),
)
