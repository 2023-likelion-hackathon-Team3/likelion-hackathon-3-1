from django import forms
from .models import hospital


class hospitalForm(forms.ModelForm):
    class Meta:
        model = hospital  # 연결할 모델 클래스
        fields = ["name"]  # 폼에서 사용할 필드 지정 (다른 필드도 추가 가능)
        widgets = {
            "name": forms.Select(attrs={"class": "select2"}),
        }
