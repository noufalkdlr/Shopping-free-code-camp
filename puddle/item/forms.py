from django import forms

from .models import Item, Category

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
    category = forms.ModelChoiceField(
    queryset=Category.objects.all(),
    empty_label="Select an existing category",
    required=False,  # Make it optional
    widget=forms.Select(attrs={'class': 'form-control'})
    )


    new_category = forms.CharField(
    max_length=255,
    required=False,  # Optional field
    widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Or enter a new category'})
    )

    class Meta:
        model = Item
        fields = ('category', 'name', 'description', 'price', 'image',)
        widgets = {
            'category': forms.Select(attrs={
                'class': INPUT_CLASSES
            }),
            'name': forms.TextInput(attrs={
                'class': 'form-control', 'placeholder': 'Enter name'
            }),
            'description': forms.Textarea(attrs={
                'class': 'form-control-textarea', 'placeholder': 'Enter Description'
            }),
            'price': forms.TextInput(attrs={
                'class': 'form-control', 'placeholder': 'Enter Price'
            }),
            'image': forms.FileInput(attrs={
            })
        }
    def clean(self):
        cleaned_data = super().clean()
        category = cleaned_data.get('category')
        new_category = cleaned_data.get('new_category')

        if not category and not new_category:
            raise forms.ValidationError("You must either select an existing category or enter a new one.")

        return cleaned_data




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

