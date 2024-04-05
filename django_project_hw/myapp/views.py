from django.shortcuts import render
from django.http import HttpResponse
import logging

logger = logging.getLogger(__name__)


# Create your views here.

def index(request):
    logger.info('пользователь посетил страницу myapp/index')
    return HttpResponse("""
        <a href="/">Основная</a>
        <a href="/about/">Обо мне</a>
        <h1>Главная страница</h1>
        <p>Добро пожаловать на главную страницу сайта.<p>
    """)


def about(request):
    logger.info('пользователь посетил страницу myapp/about')
    return HttpResponse("""
        <a href="/">Основная</a>
        <a href="/about/">Обо мне</a>
        <h1>Обо мне</h1>
        <p>Я создатель этой страницы.<p>
    """)
