from rest_framework import serializers

from src.apps.quizzes.models.answer import Answer
from src.apps.quizzes.models.question import Question
from src.apps.quizzes.models.quiz import Quizzes
from src.apps.quizzes.models.user_response import UserResponse


class AnswerSerializer(serializers.ModelSerializer):
    your_answer = serializers.SerializerMethodField()
    is_correct = serializers.SerializerMethodField()

    class Meta:
        model = Answer
        fields = ('answer_text', 'your_answer', 'is_correct')

    def get_your_answer(self, obj):
        user = self.context['request'].user
        try:
            your_answer = UserResponse.objects.get(user=user, question=obj.question).answer.answer_text
        except UserResponse.DoesNotExist:
            your_answer = None
        return your_answer

    def get_is_correct(self, obj):
        user = self.context['request'].user
        try:
            is_correct = UserResponse.objects.get(user=user, question=obj.question).is_correct
        except UserResponse.DoesNotExist:
            is_correct = None
        return is_correct


class QuestionSerializer(serializers.ModelSerializer):
    answers = serializers.SerializerMethodField()

    class Meta:
        model = Question
        fields = ('id', 'title', 'answers')

    def get_answers(self, obj):
        context = {'request': self.context.get('request')}
        answers = obj.answers.filter(is_right=True)
        return AnswerSerializer(answers, many=True, context=context).data


class QuizSerializer(serializers.ModelSerializer):
    questions = serializers.SerializerMethodField()

    result = serializers.SerializerMethodField()

    class Meta:
        model = Quizzes
        fields = ('title', 'questions', 'result')

    def get_questions(self, obj):
        context = {'request': self.context.get('request')}
        questions = obj.questions.all()
        return QuestionSerializer(questions, many=True, context=context).data

    def get_result(self, obj):
        user = self.context['request'].user

        total_correct = UserResponse.objects.filter(user=user, question__quiz=obj, is_correct=True).count()
        total_incorrect = UserResponse.objects.filter(user=user, question__quiz=obj, is_correct=False).count()
        total_count = Question.objects.filter(quiz=obj).count()
        total_unanswered = total_count - (total_correct + total_incorrect)
        result = {
            'total_correct': total_correct,
            'total_incorrect': total_incorrect,
            'total_unanswered': total_unanswered
        }
        return result
