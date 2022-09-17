from django.core.exceptions import ValidationError


def phone_number_validator(value):
    if value.isdecimal() == False:
        msg = '\'-\'을 제외한 숫자만 입력해주세요.'
        raise ValidationError(msg)

    if len(value) > 11 or len(value) < 10:
        msg = '핸드폰번호는 10자리 또는 11자리만 가능합니다.'
        raise ValidationError(msg)

    start_number = ['010', '011', '016', '017', '018', '019']
    if value[0:3] not in start_number:
        msg = '정확하게 입력해주세요.'
        raise ValidationError(msg)


def zipcode_validator(value):
    if len(value) != 5:
        msg = '정확하게 입력해주세요.'
        raise ValidationError(msg)

    if value.isdecimal() == False:
        msg = ' 정확하게 입력해주세요.'
        raise ValidationError(msg)

