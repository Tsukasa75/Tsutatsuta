from django import forms

from .models import CustomUser, Address
from django.contrib.auth.forms import UserCreationForm

class SignUpForm(UserCreationForm):
    class Meta:
        model = CustomUser
        fields = ("email", "password1", "password2")
    
    def __init__(self, *args, **kwargs):
        super(SignUpForm, self).__init__(*args, **kwargs)
        self.fields['email'].required = True

class UserProfileForm(forms.ModelForm):
    class Meta:
        model = CustomUser
        fields = ["icon", "username", "user_id", "gakubu", "gakka", "introduce"]
        labels = {
            "icon": "画像",
            "username": "ユーザーネーム",
            "user_id": "ユーザーID",
            "gakubu": "学部",
            "gakka": "学科",
            "introduce": "自己紹介文",
        }


class UserDeleteForm(forms.ModelForm):
    class Meta:
        model = CustomUser
        fields = "__all__"

class UserAddressForm(forms.ModelForm):
    class Meta:
        model = Address
        fields = ["first_name", "last_name", "first_name_kana", "last_name_kana", "post", "prefecture", "city", "house_number", "building"]
        labels = {
            "first_name": "名",
            "last_name": "姓",
            "first_name_kana": "名（カナ）",
            "last_name_kana": "姓（カナ）",
            "post": "郵便番号",
            "prefecture": "都道府県",
            "city": "市町村",
            "house_number": "番地",
            "building": "建物",
        }
        widgets = {
                "first_name": forms.TextInput(attrs={'placeholder': 'つた村'}),
                "last_name": forms.TextInput(attrs={'placeholder': 'つた子'}),
                "first_name_kana": forms.TextInput(attrs={'placeholder': 'ツタムラ'}),
                "last_name_kana": forms.TextInput(attrs={'placeholder': 'ツタコ'}),
        }


class AvailableProductsForm(forms.Form):
    show_available = forms.BooleanField(
        label="販売中のみ表示",
        label_suffix="",
        required=False,
        initial=False,
        widget=forms.CheckboxInput(),
    )


class OnTransactionProductsForm(forms.Form):
    show_available = forms.BooleanField(
        label="出品中のみ表示",
        label_suffix="",
        required=False,
        initial=False,
        widget=forms.CheckboxInput(),
    )
