from django.core.exceptions import ValidationError


def plants_validator(value):
    if len(value) != 6:
        msg = '물주기 코드는 6자리만 입력 가능합니다.'
        raise ValidationError(msg)


def watering_validator(value):
    if len(value) != 16:
        msg = '정확하게 입력해주세요.'
        raise ValidationError(msg)


def moisture_validator(value):
    if value > 100 or value < 0:
        msg = '정확하게 입력해주세요.'
        raise ValidationError(msg)