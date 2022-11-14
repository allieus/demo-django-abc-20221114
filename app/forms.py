from django import forms
from app.models import Comment


class CommentForm(forms.ModelForm):
    class Meta:
        model = Comment
        # 유저에게 입력받을 필드만 명시
        fields = ["message"]
