import streamlit as st
import numpy as np
import pandas as pd
from datetime import datetime
import json
import os

def save_session_state(filename="session_state.json"):
    """Сохранение состояния сессии в файл"""
    state = {
        key: value for key, value in st.session_state.items()
        if not key.startswith("_")  # Исключаем служебные ключи
    }
    
    # Преобразуем numpy типы в обычные Python типы
    for key, value in state.items():
        if isinstance(value, np.integer):
            state[key] = int(value)
        elif isinstance(value, np.floating):
            state[key] = float(value)
        elif isinstance(value, np.ndarray):
            state[key] = value.tolist()
    
    with open(filename, 'w', encoding='utf-8') as f:
        json.dump(state, f, ensure_ascii=False, indent=2)
    
    return filename

def load_session_state(filename="session_state.json"):
    """Загрузка состояния сессии из файла"""
    if os.path.exists(filename):
        with open(filename, 'r', encoding='utf-8') as f:
            state = json.load(f)
            for key, value in state.items():
                st.session_state[key] = value
        return True
    return False

def format_engineering_notation(value, unit=""):
    """Форматирование числа в инженерной нотации"""
    prefixes = {
        -12: "п",  # пико
        -9: "н",   # нано
        -6: "мк",  # микро
        -3: "м",   # милли
        0: "",
        3: "к",    # кило
        6: "М",    # мега
        9: "Г",    # гига
        12: "Т"    # тера
    }
    
    if value == 0:
        return f"0 {unit}"
    
    exp = int(np.floor(np.log10(abs(value)) / 3) * 3)
    exp = max(min(exp, 12), -12)
    
    value_exp = value / (10 ** exp)
    prefix = prefixes.get(exp, f"e{exp}")
    
    return f"{value_exp:.3g} {prefix}{unit}"

def calculate_power(U, I, R):
    """Расчет мощности всеми способами"""
    results = {
        "P = U × I": U * I if U and I else None,
        "P = I² × R": I**2 * R if I and R else None,
        "P = U² / R": U**2 / R if U and R and R != 0 else None
    }
    return results

def validate_parameters(U=None, I=None, R=None):
    """Проверка корректности параметров"""
    errors = []
    warnings = []
    
    if R is not None and R <= 0:
        errors.append("Сопротивление должно быть положительным числом")
    elif R is not None and R > 1e6:
        warnings.append("Очень большое сопротивление (> 1 МОм)")
    
    if U is not None and U < 0:
        errors.append("Напряжение не может быть отрицательным")
    elif U is not None and U > 1000:
        warnings.append("Высокое напряжение (> 1000 В)")
    
    if I is not None and I < 0:
        errors.append("Ток не может быть отрицательным")
    elif I is not None and I > 100:
        warnings.append("Большой ток (> 100 А)")
    
    return errors, warnings

def create_circuit_diagram(U, R, I, P):
    """Создание ASCII схемы электрической цепи"""
    diagram = f"""
    ╔══════════════════════════════════════════════════════════╗
    ║                    ЭЛЕКТРИЧЕСКАЯ СХЕМА                  ║
    ╠══════════════════════════════════════════════════════════╣
    ║                                                          ║
    ║    ┌─────[ Источник U = {U:>6.1f} В ]─────┐              ║
    ║    │                                      │              ║
    ║    │    ╔════════════════════════════╗    │              ║
    ║    └────╢ Резистор R = {R:>6.1f} Ом   ╟────┘              ║
    ║         ╚════════════════════════════╝                   ║
    ║                                                          ║
    ║    Ток: I = {I:>8.3f} А                                  ║
    ║    Мощность: P = {P:>8.2f} Вт                             ║
    ║                                                          ║
    ╚══════════════════════════════════════════════════════════╝
    """
    return diagram

def get_process_description(process_name):
    """Получение описания физического процесса"""
    descriptions = {
        "Закон Ома": {
            "description": "Исследование зависимости между напряжением, током и сопротивлением",
            "formula": "I = U / R",
            "applications": ["Расчет цепей", "Проектирование электроники", "Анализ энергопотребления"],
            "history": "Открыт Георгом Омом в 1827 году"
        },
        "Механическое движение": {
            "description": "Моделирование движения тел под действием сил",
            "formula": "F = m × a, s = v₀t + at²/2",
            "applications": ["Баллистика", "Машиностроение", "Спортивная наука"],
            "history": "Законы Ньютона (1687)"
        },
        "Термодинамика": {
            "description": "Изучение тепловых процессов и свойств веществ",
            "formula": "PV = nRT, ΔU = Q - A",
            "applications": ["Теплотехника", "Химическая технология", "Энергетика"],
            "history": "Развита в XIX веке (Карно, Клаузиус, Больцман)"
        }
    }
    return descriptions.get(process_name, {"description": "Описание не найдено"})