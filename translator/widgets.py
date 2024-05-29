import json
from django import forms
from django.utils.safestring import mark_safe

class TranslationEditor(forms.Textarea):
    class Media:
        js = (
            'translator/js/translator/translator.min.js',
            'translator/js/init_translator.js',
        )
        css = {
            'all': ('translation_editor/css/translation_editor.css',)
        }

    def render(self, name, value, attrs=None, renderer=None):
        if value is None:
            value = ''
        final_attrs = self.build_attrs(self.attrs, attrs)
        final_attrs['name'] = name
        final_attrs['class'] = 'translator'
        final_attrs['data-translation'] = 'true'
        html = [f'<textarea{forms.utils.flatatt(final_attrs)}>{forms.utils.escape(value)}</textarea>']
        return mark_safe('\n'.join(html))
