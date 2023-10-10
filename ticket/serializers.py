from .models import Ticket, Answer, Feedback
from rest_framework import serializers
from rest_framework.exceptions import ValidationError


class TicketSerializer(serializers.ModelSerializer):
    class Meta:
        model = Ticket
        fields = ('author', 'description', 'message', 'status', 'created_at', 'id')

        def create(self, validated_data):
            author = validated_data.get('author')
            description = validated_data.get('description')
            message = validated_data.get('message')
            status = validated_data.get('status')


            try:
                ticket = Ticket.objects.create(author=author,
                                            description=description,
                                            message=message,
                                            status=status,
                                            )
            except ValidationError as e:
                raise serializers.ValidationError({'author': e})
            return ticket

        def update(self, instance, validated_data):
            instance.description = validated_data.get('title', instance.description)
            instance.message = validated_data.get('title', instance.message)
            return instance


class AnswerSerializer(serializers.ModelSerializer):
    class Meta:
        model = Answer
        fields = ('ticket_id', 'answer')

        def create(self, validated_data):
            ticket_id = validated_data.get('ticket_id')
            answer = validated_data.get('answer')


            try:
                answer = Answer.objects.create(ticket_id=ticket_id,
                                            answer=answer,
                                            )
            except ValidationError as e:
                raise serializers.ValidationError({'answer': e})
            return answer


class FeedbackSerializer(serializers.ModelSerializer):
    class Meta:
        model = Feedback
        fields = ('answer_id', 'feedback')

        def create(self, validated_data):
            answer_id = validated_data.get('answer_id')
            feedback = validated_data.get('feedback')

            try:
                feedback = Feedback.objects.create(answer_id=answer_id,
                                                feedback=feedback,
                                                )
            except ValidationError as e:
                raise serializers.ValidationError({'feedback': e})
            return feedback