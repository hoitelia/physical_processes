import streamlit as st
from PIL import Image
import numpy as np
import plotly.graph_objects as go
from datetime import datetime

# Настройка страницы
st.set_page_config(
    page_title="Моделирование физических процессов",
    page_icon="🔬",
    layout="wide",
    initial_sidebar_state="expanded"
)

# Кастомные CSS стили
st.markdown("""
    <style>
    .main-header {
        text-align: center;
        padding: 2rem;
        background: linear-gradient(90deg, #667eea 0%, #764ba2 100%);
        color: white;        border-radius: 10px;
        margin-bottom: 2rem;
    }
    .process-card {
        background: linear-gradient(135deg, #667eea 0%, #764ba2 100%);
        padding: 1.5rem;
        border-radius: 10px;
        margin-bottom: 1rem;
        transition: transform 0.3s ease;
        color: white;
        box-shadow: 0 4px 6px rgba(0,0,0,0.1);
    }
    .process-card:hover {
        transform: translateY(-5px);
        box-shadow: 0 6px 12px rgba(0,0,0,0.15);
    }
    .process-card h3 {
        color: white !important;
        margin-top: 0;
        font-size: 1.5rem;
    }
    .process-card p {
        color: rgba(255, 255, 255, 0.9) !important;
        margin: 0.5rem 0;
    }
    .process-card strong {
        color: white !important;
    }
    .feature-badge {
        display: inline-block;
        background: rgba(255, 255, 255, 0.2);
        color: white;
        padding: 0.3rem 0.8rem;
        border-radius: 20px;
        font-size: 0.8rem;
        margin: 0.2rem;
        border: 1px solid rgba(255, 255, 255, 0.3);
    }
    .stat-card {
        background: white;
        padding: 1rem;
        border-radius: 8px;
        text-align: center;
        box-shadow: 0 2px 4px rgba(0,0,0,0.1);
        color: #333;
    }
    .stButton > button {
        background: white;
        color: #667eea;
        border: 2px solid #667eea;
        padding: 0.5rem 1rem;
        border-radius: 5px;
        cursor: pointer;
        width: 100%;
        font-weight: bold;
        transition: all 0.3s ease;
    }
    .stButton > button:hover {
        background: #667eea;
        color: white;
        transform: translateY(-2px);
        box-shadow: 0 4px 6px rgba(0,0,0,0.1);
    }
    .stButton > button:disabled {
        background: #e0e0e0;
        color: #999;
        border-color: #ccc;
        cursor: not-allowed;
    }
    .info-box {
        background: white;
        padding: 2rem;
        border-radius: 10px;
        box-shadow: 0 2px 4px rgba(0,0,0,0.1);
        color: #333;
    }
    .info-box h3 {
        color: #667eea;
    }
    .info-box ul {
        color: #333;
    }
    .info-box li {
        color: #333;
        margin: 0.5rem 0;
    }
    .stats-box {
        background: linear-gradient(135deg, #667eea 0%, #764ba2 100%);
        padding: 1rem;
        border-radius: 10px;
        color: white;
        text-align: center;
    }
    .stats-box h4 {
        color: white;
        margin: 0 0 0.5rem 0;
    }
    .stats-box p {
        color: rgba(255, 255, 255, 0.9);
        margin: 0.2rem 0;
    }
    .timeline-item {
        background: white;
        padding: 1rem;
        border-radius: 8px;
        box-shadow: 0 2px 4px rgba(0,0,0,0.1);
        margin: 0.5rem 0;
        color: #333;
    }
    .timeline-item strong {
        color: #667eea;
    }
    </style>
""", unsafe_allow_html=True)

# Заголовок
st.markdown("""
    <div class="main-header">
        <h1>🔬 Моделирование физических процессов</h1>
        <p style="font-size: 1.2rem;">Интерактивная платформа для визуализации и изучения физических явлений</p>
    </div>
""", unsafe_allow_html=True)

# Боковая панель с информацией
with st.sidebar:
    st.image("https://img.icons8.com/fluency/96/00020/physics.png", width=100)
    st.title("📊 Навигация")
    st.markdown("---")
    
    # Статистика проекта
    st.subheader("📈 Статистика")
    col1, col2 = st.columns(2)
    with col1:
        st.metric("Моделей", "3/6", "+3 в планах")
    
    st.markdown("---")
    
    # Информация о проекте
    st.subheader("ℹ️ О проекте")
    st.info("""
    **Версия:** 1.0.0  
    **Статус:** В разработке  
    **Последнее обновление:** Февраль 2026
    """)
    

# Основной контент
st.markdown("## 🎯 О проекте")

# Описание проекта в две колонки
col1, col2 = st.columns([2, 1])

with col1:
    st.markdown("""
    <div class="info-box">
        <h3>🚀 Наша миссия</h3>
        <p>Сделать изучение физики увлекательным и наглядным с помощью современных технологий визуализации. Наша платформа позволяет экспериментировать с физическими законами в интерактивном режиме, меняя параметры и наблюдая за результатами в реальном времени.</p>
        <h3 style="margin-top: 2rem; color: white;">✨ Ключевые возможности</h3>
        <ul>
            <li>Интерактивные 3D визуализации</li>
            <li>Настройка параметров в реальном времени</li>
            <li>Детальная теоретическая справка</li>
            <li>Экспорт результатов и графиков</li>
            <li>Пошаговое объяснение процессов</li>
        </ul>
    </div>
    """, unsafe_allow_html=True)

with col2:
    # Создаем простую анимацию/график для главного экрана
    x = np.linspace(0, 4*np.pi, 100)
    y1 = np.sin(x)
    y2 = np.cos(x)
    
    fig = go.Figure()
    fig.add_trace(go.Scatter(x=x, y=y1, mode='lines', name='Волновая функция 1', line=dict(color='#667eea')))
    fig.add_trace(go.Scatter(x=x, y=y2, mode='lines', name='Волновая функция 2', line=dict(color='#764ba2')))
    
    fig.update_layout(
        title="Пример визуализации",
        xaxis_title="Время",
        yaxis_title="Амплитуда",
        showlegend=True,
        height=300,
        margin=dict(l=0, r=0, t=40, b=0),
        plot_bgcolor='rgba(0,0,0,0)',
        paper_bgcolor='rgba(0,0,0,0)'
    )
    
    st.plotly_chart(fig, use_container_width=True)

# Доступные процессы
st.markdown("## 🔬 Доступные физические процессы")

# Создаем карточки процессов
col1, col2, col3 = st.columns(3)

with col1:
    st.markdown("""
    <div class="process-card">
        <h3 style="color: #667eea;">⚡ Закон Ома</h3>
        <p><strong>Статус:</strong> ✅ Активен</p>
        <p>Исследование зависимости между напряжением, током и сопротивлением в электрической цепи.</p>
        <p><span class="feature-badge">2D/3D</span> 
           <span class="feature-badge">Интерактив</span>
           <span class="feature-badge">Калькулятор</span></p>
        <a href="/Закон_Ома" target="_self">
            <button style="background: #667eea; color: white; border: none; 
                          padding: 0.5rem 1rem; border-radius: 5px; cursor: pointer;">
                Перейти к модели →
            </button>
        </a>
    </div>
    """, unsafe_allow_html=True)

with col2:
    st.markdown("""
    <div class="process-card">
        <h3 style="color: #667eea;">📐 Механическое движение</h3>
        <p><strong>Статус:</strong>  ✅ Активен</p>
        <p>Моделирование равноускоренного движения, брошенного тела и колебаний.</p>
        <p><span class="feature-badge">2D/3D</span> 
           <span class="feature-badge">Интерактив</span>
           <span class="feature-badge">Калькулятор</span></p>
    </div>
    """, unsafe_allow_html=True)

with col3:
    st.markdown("""
    <div class="process-card">
        <h3 style="color: #667eea;">🌡️ Термодинамика</h3>
        <p><strong>Статус:</strong> 🚧 В разработке</p>
        <p>Изучение тепловых процессов, уравнения состояния идеального газа.</p>
        <p><span class="feature-badge">Скоро</span></p>
    </div>
    """, unsafe_allow_html=True)

# Вторая строка процессов
col1, col2, col3 = st.columns(3)

with col1:
    st.markdown("""
    <div class="process-card">
        <h3 style="color: #667eea;">💡 Оптика</h3>
        <p><strong>Статус:</strong>  ✅ Активен</p>
        <p>Преломление света, линзы, интерференция и дифракция.</p>
        <p><span class="feature-badge">2D/3D</span> 
           <span class="feature-badge">Интерактив</span>
           <span class="feature-badge">Калькулятор</span></p>
    </div>
    """, unsafe_allow_html=True)

with col2:
    st.markdown("""
    <div class="process-card">
        <h3 style="color: #667eea;">🧲 Электромагнетизм</h3>
        <p><strong>Статус:</strong> 🚧 В разработке</p>
        <p>Магнитные поля, электромагнитная индукция, цепи переменного тока.</p>
        <p><span class="feature-badge">Скоро</span></p>
    </div>
    """, unsafe_allow_html=True)

with col3:
    st.markdown("""
    <div class="process-card">
        <h3 style="color: #667eea;">⚛️ Квантовая физика</h3>
        <p><strong>Статус:</strong> 🚧 В разработке</p>
        <p>Волновая функция, уровни энергии, туннельный эффект.</p>
        <p><span class="feature-badge">Скоро</span></p>
    </div>
    """, unsafe_allow_html=True)

# Форма обратной связи
st.markdown("## 💬 Обратная связь")
with st.expander("Хотите предложить новый процесс или сообщить об ошибке?"):
    with st.form("feedback_form"):
        name = st.text_input("Ваше имя")
        email = st.text_input("Email для ответа")
        feedback_type = st.selectbox("Тип обращения", ["Предложение", "Ошибка", "Вопрос", "Другое"])
        message = st.text_area("Сообщение")
        
        col1, col2 = st.columns(2)
        with col1:
            submitted = st.form_submit_button("Отправить")
        with col2:
            if submitted:
                st.success("Спасибо за обратную связь! Мы свяжемся с вами в ближайшее время.")

# Footer
st.markdown("---")
st.markdown("""
    <div style='text-align: center; color: gray; padding: 2rem;'>
        <p>🔬 Моделирование физических процессов с визуализацией | Версия 1.0.0</p>
        <p>Разработано с ❤️ для образования и науки</p>
    </div>
""", unsafe_allow_html=True)