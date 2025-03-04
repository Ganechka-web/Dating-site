from django.db import models


class Recommendation(models.Model):
    """
    Describes AI recommendation with user (target) 
    """
    target = models.ForeignKey('accounts.DatingUser',
                               on_delete=models.CASCADE,
                               related_name='recommendations')
    # text AI answer from API
    content = models.TextField()
    # datetime when answer was received
    asked = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ['asked']
