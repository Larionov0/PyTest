from django.db import models
from django.urls import reverse
from json import dumps, loads


# Create your models here.
class Pack(models.Model):
    """
    Це типу пак (набір) з тестами.
    Має містити список питань
    """
    name = models.CharField(max_length=50, help_text="Name of pack")
    questions_json = models.CharField(max_length=300, help_text="List of questions id-s converted to json")
    reward = models.IntegerField(help_text="Reward in Paisons")

    def __str__(self):
        return str(self.name) + " pack"


class Question(models.Model):
    """
    А це типу саме питання.
    Містить питання, список (як бінарник..) відповідей, індекс правильної.
    """
    """
    def __init__(self, *args, **kwargs):
        answers = kwargs.pop("answers")
        super().__init__(*args, **kwargs)
        self.set_answers(answers)
    """
    pack = models.ForeignKey(Pack)
    question = models.CharField(max_length=1000, help_text="Question`s text")
    answers_json = models.CharField(max_length=300, help_text="List of answers converted to json")
    index_of_correct = models.IntegerField(help_text="Index of correct answer")

    def set_answers(self, lst):
        self.answers = dumps(lst)

    def get_answers(self):
        return loads(self.answers)

    def get_absolute_url(self):
        """
        Returns the url to access a particular instance of MyModelName.
        """
        return reverse('model-detail-view', args=[str(self.id)])

    def __str__(self):
        """
        String for representing the MyModelName object (in Admin site etc.)
        """
        return f"{self.question}"
