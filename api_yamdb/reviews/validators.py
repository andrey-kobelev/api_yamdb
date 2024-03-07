import re

from django.conf import settings
from django.core.exceptions import ValidationError

INCORRECT_USERNAME = 'Имя {name} - недопустимо.'
BAD_USERNAME = (
    'Неверный формат имени {name}. '
    'Запрещенные символы: {characters}'
)


def username_validator(username):
    bad_characters = {
        character
        for character in username
        if not re.match(settings.USERNAME_PATTERN, character)
    }
    if bad_characters:
        raise ValidationError(
            BAD_USERNAME.format(
                name=username,
                characters=''.join(bad_characters)
            )
        )
    if username in settings.BAD_USERNAME_WORDS:
        raise ValidationError(INCORRECT_USERNAME.format(name=username))

    return username
