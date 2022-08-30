from django.contrib import messages
from django.contrib.auth.decorators import login_required

from django.http import HttpResponseRedirect
from django.shortcuts import render, get_object_or_404

from django.urls import reverse
from django.utils.decorators import method_decorator

from django.views.generic import RedirectView

from articleapp.models import Article

from likeapp.models import LikeRecord




@method_decorator(login_required, 'get')
class LikeArticleView(RedirectView):

    def get_redirect_url(self, *args, **kwargs):

        return reverse('articleapp:detail', kwargs={'pk': kwargs['pk']})

    def get(self, *args, **kwargs):
        user = self.request.user
        article = get_object_or_404(Article, pk=kwargs['pk'])
        like_list = LikeRecord.objects.all()
        like_user = {
            'like_user':like_list[1]
        }
        render(self.request, 'articleapp/detail.html', like_user)


        if LikeRecord.objects.filter(user=user, article=article).exists():
            LikeRecord.objects.filter(user=user, article=article).delete()
            if article.like != 0:
                article.like -= 1
                article.save()

                messages.add_message(self.request, messages.ERROR, '좋아요가 취소됐습니다.')

                # LikeRecord(user=user, article=article).get_deferred_fields()
                return super(LikeArticleView, self).get(self.request, *args, **kwargs)

        else:
            LikeRecord(user=user, article=article).save()

        article.like += 1
        article.save()
        messages.add_message(self.request, messages.SUCCESS, '좋아요가 반영됐습니다.')

        return super(LikeArticleView, self).get(self.request, *args, **kwargs)
