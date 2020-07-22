# -*- coding: utf-8 -*-
import os

import math
import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
import sympy as sp


# Глобальная переменная для записи названия графика
TITLE = ''
# Переменная, в которую мы записываем запускает ли функцию файл bot.py
BOT_PLOT = False
# Переменная, которая хранит путь к директории
PATH = os.path.abspath('')
# Переменная, в которую мы записываем будут ли строиться кресты погрешностей в функции plots_drawer
ERROR_BAR = False
# Глобальные переменные для записи названия Осей
LABEL = []
# Пер
ERRORS = [0, 0]


def data_conv(data_file):
    """
    Программа, которая конвертирует данные из таблицы в массив [x,y]
    :param data_file: название файла
    :return: [x,y]
    """
    global LABEL
    dataset = pd.read_excel(data_file)
    LABEL = dataset.columns
    d = np.array(dataset)
    x = d[:, 0]
    y = d[:, 1]
    return [x, y]


def plt_const(x, y):
    """
    Функция рассчитывает по МНК коэффициенты прямой по полученным координатам точек. Так же рассчитывает их погрешности.
    :param x: Массив абсцисс точек
    :param y: Массив оридинат точек
    :return: [значение углового коэфф a, значение коэфф b, значение погрешности a, значение погрешности b]
    """
    x = np.array(x)
    y = np.array(y)
    av_x = np.sum(x)/len(x)
    av_y = np.sum(y)/len(y)
    sigmas_x = np.sum(x*x)/len(x) - (np.sum(x)/len(x))**2
    sigmas_y = np.sum(y*y)/len(y) - (np.sum(y)/len(y))**2
    r = np.sum(x*y)/len(x) - av_x*av_y
    a = r/sigmas_x
    b = av_y - a*av_x
    try:
        d_a = 2 * math.sqrt((sigmas_y / sigmas_x - a ** 2) / (len(x) - 2))
        d_b = d_a * math.sqrt(sigmas_x + av_x ** 2)
    except Exception as e:
        print(e)
        d_a = 'error'
        d_b = 'error'
    return [a, b, d_a, d_b]


def const_dev(x, y):
    """
    Функция рассчитывает погрешности коэффициентов прямой по полученным координатам точек
    :param x: Массив абсцисс точек
    :param y: Массив оридинат точек
    :return:
    """
    return [plt_const(x, y)[2], plt_const(x, y)[3]]


def plots_drawer(x, y, tit, xlabel, ylabel, legend, pl_name, xerr, yerr, mnk, graph):
    """
    Функция строит графики n кривых, где x =[x_1, x_2, ..., x_n],
     y = [y_1, y_2, ..., y_n] и x_i и y_i - массивы координат кривых
    :param x: Массив из масивов координат по оси х для разных прямых
    :param y: Массив из масивов координат по оси y для разных прямых
    :param xlabel: Подпись оси х
    :param ylabel: Подпись оси y
    :param pl_name: Название файла для сохранения изображения
    :param xerr: погрешность по х
    :param yerr: погрешность по y
    :param mnk: type Bool, При True строится прямая мнк
    :param graph: Тип графика
    :return:
    """
    fig = plt.figure(dpi=300)
    ax = fig.add_subplot()
    a = []
    b = []
    x_ = []
    for i in range(0, len(x)):
        r = plt_const(x[i], y[i])
        a.append(r[0])
        b.append(r[1])
    if mnk:
        for i in range(0, len(x)):
            if xerr != 0 or yerr != 0:
                ax.errorbar(x[i], y[i], xerr=xerr, yerr=yerr, fmt='k+')
    for i in range(0, len(x)):
        delta = (max(x[i]) - min(x[i]))/len(x[i])
        x_.append([min(x[i]) - delta, max(x[i]) + delta])
        ax.plot(x[i], y[i], graph[i])
    if mnk:
        for i in range(0, len(x)):
            ax.plot(np.array(x_[i]), a[i]*(np.array(x_[i])) + b[i], '--')
    ax.set_xlabel(xlabel)
    ax.set_ylabel(ylabel)
    ax.legend(legend)
    ax.set_title(tit)
    ax.grid(True)
    # Находим координаты углов графика
    xmin, xmax = ax.get_xlim()
    ymin, ymax = ax.get_ylim()
    # matching arrowhead length and width
    dps = fig.dpi_scale_trans.inverted()
    bbox = ax.get_window_extent().transformed(dps)
    width, height = bbox.width, bbox.height
    # manual arrowhead width and length
    hw = 1. / 20. * (ymax - ymin)
    hl = 1. / 20. * (xmax - xmin)
    lw = .1  # axis line width
    ohg = 0.25  # arrow overhang
    # compute matching arrowhead length and width
    yhw = hw / (ymax - ymin) * (xmax - xmin) * height / width
    yhl = hl / (xmax - xmin) * (ymax - ymin) * width / height

    # draw x and y axis
    ax.arrow(xmin, ymin, xmax - xmin, 0., fc='k', ec='k', lw=lw,
             head_width=hw / 1.5, head_length=hl / 1.5, overhang=ohg,
             length_includes_head=True, clip_on=False, width=1e-5)

    ax.arrow(xmin, ymin, 0., ymax - ymin, fc='k', ec='k', lw=lw,
             head_width=yhw / 1.5, head_length=yhl / 1.5, overhang=ohg,
             length_includes_head=True, clip_on=False, width=1e-5)
    ax.minorticks_on()
    # Настраиваем основную стеку графика
    ax.grid(which='major', linestyle='-', linewidth='0.5', color='black')
    # Добавляем промежуточную сетку
    ax.grid(which='minor', linestyle=':', linewidth='0.5', color='black')
    plt.savefig(pl_name)
    plt.show()


def mnk_calc(data_file):
    """
    Функция считывает данные из таблицы и возвращает коэффициенты и погрешности
    :param data_file: Название файла с данными
    :return: [a - коэф. прямой, b - коэф. прямой, погрешность а, погрешность b]
    """
    dataset = pd.read_excel(data_file)
    d = np.array(dataset)
    a = []
    b = []
    x = []
    y = []
    d_a = []
    d_b = []
    for i in range(0, len(d[1, :] - 1), 2):
        r = plt_const(d[:, i], d[:, i + 1])
        x.append(d[:, i])
        y.append(d[:, i + 1])
        a.append(r[0])
        b.append(r[1])
        d_a.append(r[2])
        d_b.append(r[3])

    return [a, b, d_a, d_b]


def error_calc(equation, var_list, point_list, error_list):
    """

    :param equation: формула в формате, приемлемом для python
    :param var_list: список переменных
    :param point_list: список значений переменных в точке соответсвенно со списком переменных
    :param error_list: список погрешностей для каждой переменной соответсвенно со списком переменных
    :return: погрешность
    """
    sigma = 0  # Объявляем переменную
    for number in range(len(var_list)):
        elem = sp.Symbol(var_list[number])  # переводит символ в приемлемый формат для дифференцирования
        der = sp.diff(equation, elem)  # дифференцируем выражение equation по переменной elem
        for score in range(len(point_list)):  # задаем каждую переменную, чтобы подставить ее значение
            der = sp.lambdify(var_list[score], der, 'numpy')  # говорим, что функция будет конкретной переменной
            der = der(point_list[score])  # задаем функцию в строчном виде
        sigma += error_list[number] ** 2 * der ** 2  # считем погрешность

    return sigma
