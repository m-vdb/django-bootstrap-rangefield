from django import forms

from bootstrap_rangefield.widget import RangeWidget


class RangeField(forms.MultiValueField):
    default_error_messages = {} # TODO
    default_min = 0
    default_max = 10

    def __init__(self, field_class, widget=forms.TextInput, min_value=None, max_value=None, *args, **kwargs):
        self.min_value = min_value or self.default_min
        self.max_value = max_value or self.default_max
        self.fields = (field_class(), field_class()) # TODO

        if not 'initial' in kwargs:
            kwargs['initial'] = [self.min_value, self.min_value]

        super(RangeField, self).__init__(
            fields=fields, widget=RangeWidget(self.min_value, self.max_value), *args, **kwargs
        )

    def compress(self, data_list):
        if data_list: # TODO
            return [
                self.fields[0].clean(data_list[0]),
                self.fields[1].clean(data_list[1])
            ]

        return None
