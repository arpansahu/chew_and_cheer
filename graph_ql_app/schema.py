import graphene
from graphene_django import DjangoObjectType, DjangoListField
# from graphql_auth import mutations, relay

from crud_django_form.models import Item

from graph_ql_app.models import Category, Quizzes, Question, Answer
# from graphql_auth.schema import UserQuery, MeQuery


class ItemType(DjangoObjectType):
    class Meta:
        model = Item
        fields = ('id', 'name', 'description', 'price')


# Now we will generate a query like this
# type Query{
#     me: User
# }

class Query(graphene.ObjectType):
    all_items = graphene.List(ItemType)

    def resolve_all_items(root, info):
        return Item.objects.all()


class ItemMutationCreate(graphene.Mutation):
    class Arguments:
        name = graphene.String(required=True)
        description = graphene.String(required=True)
        price = graphene.Float(required=True)

    item = graphene.Field(ItemType)

    @classmethod
    def mutate(cls, root, info, name, description, price):
        item = Item(name=name, description=description, price=price)
        item.save()
        return ItemMutationCreate(item=item)


class ItemMutationUpdation(graphene.Mutation):
    class Arguments:
        id = graphene.ID(required=True)
        name = graphene.String(required=True)
        description = graphene.String(required=True)
        price = graphene.Float(required=True)

    item = graphene.Field(ItemType)

    @classmethod
    def mutate(cls, root, info, name, id, description, price):
        item = Item.objects.get(id=id)
        item.name = name
        item.description = description
        item.price = price
        print(item)
        item.save()
        return ItemMutationUpdation(item=item)


class ItemMutationDelete(graphene.Mutation):
    class Arguments:
        id = graphene.ID()

    item = graphene.Field(ItemType)

    @classmethod
    def mutate(cls, root, info, id):
        item = Item.objects.get(id=id)
        deleted_object = item
        item.delete()
        return deleted_object


class Mutation(graphene.ObjectType):
    create_item = ItemMutationCreate.Field()
    update_item = ItemMutationUpdation.Field()
    delete_item = ItemMutationDelete.Field()


schema = graphene.Schema(query=Query, mutation=Mutation)


# ------------------------------------------------------------------------------------
class CategoryType(DjangoObjectType):
    class Meta:
        model = Category
        fields = ("id", "name")


class QuizzesType(DjangoObjectType):
    class Meta:
        model = Quizzes
        fields = ("id", "title", "category", "quiz")


class QuestionType(DjangoObjectType):
    class Meta:
        model = Question
        fields = ("id", "title", "quiz", "difficulty")


class AnswerType(DjangoObjectType):
    class Meta:
        model = Answer
        fields = ("question", "answer_text")


class Query2(graphene.ObjectType):
    all_questions = graphene.Field(QuestionType, id=graphene.Int())
    all_answers = graphene.List(AnswerType, id=graphene.Int())

    quiz = graphene.String()
    # all_quizzes = DjangoListField(QuizzesType)
    all_quizzes = graphene.List(QuizzesType)
    all_quizzes_with_id = graphene.Field(QuizzesType, id=graphene.Int())

    def resolve_quiz(root, info):
        return f"This is raw anonymous string questions"

    def resolve_all_quizzes(root, info):
        print(Quizzes.objects.all())
        return Quizzes.objects.all()

    def resolve_all_quizzes_with_id(root, info, id):
        return Quizzes.objects.get(pk=id)

    def resolve_all_questions(root, info, id):
        return Question.objects.get(pk=id)

    def resolve_all_answers(root, info, id):
        return Answer.objects.filter(question=id)


# It created a new object
class CategoryMutationCreate(graphene.Mutation):
    class Arguments:
        name = graphene.String(required=True)

    category = graphene.Field(CategoryType)

    @classmethod
    def mutate(cls, root, info, name):
        category = Category(name=name)
        category.save()
        return CategoryMutationCreate(category=category)


# It Updated the Object
class CategoryMutationUpdation(graphene.Mutation):
    class Arguments:
        id = graphene.ID()
        name = graphene.String(required=True)

    category = graphene.Field(CategoryType)

    @classmethod
    def mutate(cls, root, info, name, id):
        category = Category.objects.get(id=id)
        category.name = name
        category.save()
        return CategoryMutationUpdation(category=category)


# I deletes a new object
class CategoryMutationDelete(graphene.Mutation):
    class Arguments:
        id = graphene.ID()

    category = graphene.Field(CategoryType)

    @classmethod
    def mutate(cls, root, info, id):
        category = Category.objects.get(id=id)
        deleted_object = category
        category.delete()
        return deleted_object


class Mutation2(graphene.ObjectType):
    create_category = CategoryMutationCreate.Field()
    update_category = CategoryMutationUpdation.Field()
    delete_category = CategoryMutationDelete.Field()


schema2 = graphene.Schema(query=Query2, mutation=Mutation2)


# --------------------User Authentication-----------
# Commented out due to Django 4.x compatibility issues with graphql_auth
# class QueryUserAuthentication(UserQuery, MeQuery, graphene.ObjectType):
#     pass


# class AuthMutation(graphene.ObjectType):
#     register = mutations.Register.Field()
#     verify_account = mutations.VerifyAccount.Field()
#     resend_activation_email = mutations.ResendActivationEmail.Field()
#     send_password_reset_email = mutations.SendPasswordResetEmail.Field()
#     password_reset = mutations.PasswordReset.Field()
#     password_set = mutations.PasswordSet.Field()  # For passwordless registration
#     password_change = mutations.PasswordChange.Field()
#     update_account = mutations.UpdateAccount.Field()
#     # update_account = relay.UpdateAccount.Field()
#     archive_account = mutations.ArchiveAccount.Field()
#     delete_account = mutations.DeleteAccount.Field()
#     send_secondary_email_activation = mutations.SendSecondaryEmailActivation.Field()
#     verify_secondary_email = mutations.VerifySecondaryEmail.Field()
#     swap_emails = mutations.SwapEmails.Field()
#     remove_secondary_email = mutations.RemoveSecondaryEmail.Field()

#     # django-graphql-jwt inheritances
#     token_auth = mutations.ObtainJSONWebToken.Field()
#     verify_token = mutations.VerifyToken.Field()
#     refresh_token = mutations.RefreshToken.Field()
#     revoke_token = mutations.RevokeToken.Field()


# class Mutation3(AuthMutation, graphene.ObjectType):
#     pass


# schema_user_authentication = graphene.Schema(query=QueryUserAuthentication, mutation=Mutation3)
