from django.db import models


class Recommendation(models.Model):
    """
    Keeps AI recommendation with user (target) 
    """
    # user who asked a recommendation 
    asker = models.ForeignKey('accounts.DatingUser',
                              on_delete=models.CASCADE,
                              related_name='asked_recommendations')
    # user was compared with current user 
    target = models.ForeignKey('accounts.DatingUser',
                               on_delete=models.CASCADE,
                               related_name='received_recommendations')
    # text AI answer from API
    content = models.TextField()
    # datetime when asker asked a recommendation
    asked = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ['asked']
