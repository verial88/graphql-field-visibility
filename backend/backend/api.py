from django.contrib.auth import get_user_model
import graphene
from graphene_django import DjangoObjectType


User = get_user_model()


class UserType(DjangoObjectType):
    """
    Single User GraphQL Type based on Django model.
    """
    class Meta:
        model = User
        fields = ('id', 'username', 'email')


class Query(graphene.ObjectType):
    user = graphene.Field(
        UserType, 
        id=graphene.Int(required=True),
        description='Gets single User by ID'
    )

    def resolve_user(self, info, id):
        return User.objects.get(id=id)


schema = graphene.Schema(query=Query)
