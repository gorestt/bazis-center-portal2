
from django import forms
from .models import OrderQueue, Document, Report

class OrderForm(forms.ModelForm):
    class Meta:
        model = OrderQueue
        fields = ['title', 'description', 'priority', 'status', 'executor']

class DocumentForm(forms.ModelForm):
    class Meta:
        model = Document
        fields = ['title', 'access', 'file']
        labels = {
            'title': 'Название',
            'access': 'Доступ',
            'file': 'Файл',
        }

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['title'].widget.attrs.update({'class': 'form-control'})
        self.fields['access'].widget.attrs.update({'class': 'form-select'})
        self.fields['file'].widget.attrs.update({'class': 'form-control'})

class ReportForm(forms.ModelForm):
    class Meta:
        model = Report
        fields = ['report_type', 'period_to']
        labels = {
            'report_type': 'Тип отчёта',
            'period_to': 'Дата окончания периода',
        }

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['report_type'].widget.attrs.update({'class': 'form-select'})
        self.fields['period_to'].widget.attrs.update({'class': 'form-control', 'type': 'date'})
