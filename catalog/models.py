from django.db import models
from django.urls import reverse
from json import dumps, loads


# Create your models here.
class Pack(models.Model):
    """
    Це типу пак (набір) з тестами.
    Має містити список питань
    """
    name = models.CharField(max_length=50, default="PackName", help_text="Name of pack")
    reward = models.IntegerField(default=0, help_text="Reward in Paisons")
    difficulty = models.IntegerField(default=0, help_text="Difficult of pack")
    color = models.CharField(max_length=30, default="green")
    pack_class = models.CharField(max_length=30, default="0")

    def __str__(self):
        return str(self.name) + " pack"

    def count_of_questions(self):
        return self.question_set.count()


class Question(models.Model):
    """
    А це типу саме питання.
    Містить питання, список (як бінарник..) відповідей, індекс правильної.

    """
    quest_pack = models.ForeignKey(Pack, default=0, on_delete=models.CASCADE)
    question = models.TextField(max_length=1000, default="Question", help_text="Question`s text")
    answers_json = models.CharField(max_length=300, default="answers", help_text="List of answers converted to json")
    index_of_correct = models.IntegerField(default=0, help_text="Index of correct answer")
    count_of_correct = models.IntegerField(default=0, help_text="Count of correct answers")
    count_of_incorrect = models.IntegerField(default=0, help_text="Count of incorrect answers")

    def get_answers(self):
        return loads(self.answers_json)

    def get_html_question(self):
        i = 0
        string = self.question[:]
        while i < len(string):
            if string[i] == "\n":
                string = string[:i] + "<br>" + string[i + 1:]
            i += 1
        return string

    def get_absolute_url(self):
        """
        Returns the url to access a particular instance of MyModelName.
        """
        return reverse('model-detail-view', args=[str(self.id)])

    def __str__(self):
        """
        String for representing the MyModelName object (in Admin site etc.)
        """
        return f"{self.question[:30]}..."
