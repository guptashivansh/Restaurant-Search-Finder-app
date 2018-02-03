from django.core.exceptions import ValidationError

def validate_even(value):
    if value % 2 != 0:
        raise ValidationError(
            '%(value)s is not an even number',
            params={'value': value},
        )

Categories=['Buffet','Fast Food']


def validate_category(value):
	cat=value.capitalize()
	if not value in Categories and not cat in Categories:
		raise ValidationError( f"{value} is not a valid Category")
	return cat