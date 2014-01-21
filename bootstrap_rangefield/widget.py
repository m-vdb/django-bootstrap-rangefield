from django import forms

# TODO template + javascript

class RangeWidget(forms.TextInput):

    def __init__(self, min_value, max_value, attrs=None):
        super(RangeWidget, self).__init__(attrs)
        self.min_value = min_value
        self.max_value = max_value

    def render(self, name, value, attrs=None):
        attrs = attrs or {}
        value = value or [self.min_value, self.min_value]
        attrs["data-slider-value"] = str(value)

        return super(RangeWidget, self).render(name, value, attrs)
