from django import forms
from .models import Item 

class ItemForm(forms.ModelForm):

    class Meta:
        model = Item
        fields = ['item_name', 'item_desc', 'item_price', 'item_image']
        widgets = {
            "item_name":forms.TextInput(attrs={"placeholder":"Enter item name","required":True}),
            "item_desc":forms.Textarea(attrs={"placeholder":"Enter item description","required":True}),
            "item_price":forms.NumberInput(attrs={"placeholder":"Enter item price","required":True}),
            "item_image":forms.URLInput(attrs={"required":False})
        }
    
    def clean_item_price(self):
        price = self.cleaned_data.get('item_price')
        if price is not None and price < 0:
            raise forms.ValidationError("Price cannot be negative or Null.")
        return price
    
    def clean(self):
        cleaned = super().clean()
        name = cleaned.get('item_name')
        desc = cleaned.get('item_desc')
        if name and desc and name.lower() in desc.lower():
            self.add_error('item_desc', "Description should not contain the item name.")
        return cleaned