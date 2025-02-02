from django import forms

from .models import Item

# class NewItemForm(forms.ModelForm):
#     class Meta:
#         model = Item
#         exclude = ['is_sold','created_at']

#         widgets = {
#             'name':forms.TextInput(attrs={'class': 'form-control' , 'placeholder': 'Enter Name'}),
#             'category': forms.Select(attrs={'class': 'custom-select'}),
#             'description': forms.Textarea(attrs={'class': 'description-control'}),
#             'price':forms.TextInput(attrs={'class': 'form-control' , 'placeholder': 'Enter price'}),
#         }

INPUT_CLASSES = 'w-full py-4 px-6 rounded-xl border'

class NewItemForm(forms.ModelForm):
    class Meta:
        model = Item
        fields = ('category', 'name', 'description', 'price', 'image',)
        widgets = {
            'category': forms.Select(attrs={
                'class': INPUT_CLASSES
            }),
            'name': forms.TextInput(attrs={
                'class': INPUT_CLASSES
            }),
            'description': forms.Textarea(attrs={
                'class': INPUT_CLASSES
            }),
            'price': forms.TextInput(attrs={
                'class': INPUT_CLASSES
            }),
            'image': forms.FileInput(attrs={
                'class': INPUT_CLASSES
            })
        }

class EditItemForm(forms.ModelForm):
    class Meta:
        model = Item
        fields = ( 'name', 'description', 'price', 'image','is_sold',)
        widgets = {
            'name': forms.TextInput(attrs={
                'class': INPUT_CLASSES
            }),
            'description': forms.Textarea(attrs={
                'class': INPUT_CLASSES
            }),
            'price': forms.TextInput(attrs={
                'class': INPUT_CLASSES
            }),
            'image': forms.FileInput(attrs={
                'class': INPUT_CLASSES
            })
        }

