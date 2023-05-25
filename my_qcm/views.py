from django.shortcuts import render, redirect
from .models import Quiz, QuizQuestion, Option, QuizResult,Question
from django.contrib.auth.decorators import login_required
from django.contrib import messages

@login_required
def start_quiz(request, quiz_id):
    quiz = Quiz.objects.get(id=quiz_id)
    questions = QuizQuestion.objects.filter(quiz=quiz).select_related('question')
    total_questions = questions.count()
    context = {'quiz': quiz, 'questions': questions, 'total_questions': total_questions}
    return render(request, 'qcm_app/start_quiz.html', context)

@login_required
def submit_quiz(request, quiz_id):
    if request.method == 'POST':
        quiz = Quiz.objects.get(id=quiz_id)
        questions = QuizQuestion.objects.filter(quiz=quiz).select_related('question')
        total_questions = questions.count()
        score = 0

        for question in questions:
            selected_option_id = request.POST.get(f'question_{question.id}')
            selected_option = Option.objects.get(id=selected_option_id)

            if selected_option.is_correct:
                score += 1

        QuizResult.objects.create(quiz=quiz, user=request.user, score=score, total_questions=total_questions)
        messages.success(request, 'Quiz submitted successfully!')
        return redirect('quiz_result', quiz_id=quiz_id)

    return redirect('home')

@login_required
def quiz_result(request, quiz_id):
    quiz = Quiz.objects.get(id=quiz_id)
    quiz_results = QuizResult.objects.filter(quiz=quiz, user=request.user)
    context = {'quiz': quiz, 'quiz_results': quiz_results}
    return render(request, 'qcm_app/quiz_result.html', context)