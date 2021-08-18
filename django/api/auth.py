from rest_framework_simplejwt.serializers import TokenObtainPairSerializer, TokenRefreshSerializer
from django.contrib.auth.models import User

# Hasura > JWT Specifics
class HasuraTokenObtainPairSerializer(TokenObtainPairSerializer):
    @classmethod
    def get_token(cls, user):
        token = super().get_token(user)
        token['user_name'] = user.username
        token['user_email'] = user.email
        token['https://hasura.io/jwt/claims'] = {}
        token['https://hasura.io/jwt/claims']['x-hasura-allowed-roles'] = [g.name for g in user.groups.all()]

        def get_default_group(user):
            ret_group = None
            if hasattr(user, "profile"):
                ret_group = user.profile.default_group
            elif user.groups:
                ret_group = user.groups.first()

            return ret_group

        default_group = get_default_group(user)

        token['https://hasura.io/jwt/claims']['x-hasura-default-role'] = default_group.name
        token['https://hasura.io/jwt/claims']['x-hasura-default-role-id'] = default_group.id


        token['https://hasura.io/jwt/claims']['x-hasura-user-id'] = str(user.id)

        return token


class ValidateTokenRefreshSerializer(TokenRefreshSerializer):
    # Validate user account is active, and the user role matches the issued JWT
    # Based on: https://github.com/SimpleJWT/django-rest-framework-simplejwt/issues/193
    error_msg = 'No active account found with the given credentials'

    def validate(self, attrs):
        token_payload = token_backend.decode(attrs['refresh'])
        try:
            user = User.objects.get(pk=token_payload['user_id'])
        except User.DoesNotExist:
            print('User does not exist')
            raise exceptions.AuthenticationFailed(
                self.error_msg, 'no_active_account'
            )

        if not user.is_active or user.email != token_payload['user_email']:
            print('Email Does Not Exist / Non-Active')
            raise exceptions.AuthenticationFailed(
                self.error_msg, 'no_active_account'
            )

        if user.profile.role != token_payload['https://hasura.io/jwt/claims']['x-hasura-default-role']:
            print(user.profile.role)
            print(token_payload['https://hasura.io/jwt/claims']
                  ['x-hasura-default-role'])
            print('Roles Dont Match')
            raise exceptions.AuthenticationFailed(
                self.error_msg, 'no_active_account'
            )

        return super().validate(attrs)
