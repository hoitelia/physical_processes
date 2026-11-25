import streamlit as st
import numpy as np
import pandas as pd
import plotly.graph_objects as go
from plotly.subplots import make_subplots
import math

# Настройка страницы
st.set_page_config(
    page_title="Механика - Моделирование",
    page_icon="📐",
    layout="wide"
)

# Добавляем стили
st.markdown("""
    <style>
    .formula-container {
        font-size: 2rem; 
        text-align: center; 
        background: white;
        padding: 1.5rem; 
        border-radius: 15px; 
        margin: 1rem 0 2rem 0;
        box-shadow: 0 10px 30px rgba(102, 126, 234, 0.2);
        border-left: 5px solid #667eea;
        border-right: 5px solid #764ba2;
        position: relative;
        overflow: hidden;
        transition: all 0.3s ease;
    }
    .formula-container:hover {
        transform: scale(1.02);
        box-shadow: 0 10px 40px rgba(102, 126, 234, 0.3);
    }
    .formula-text {
        font-weight: 700;
        color: #2d3748;
        font-size: 2.2rem;
        display: inline-block;
        padding: 0 1rem;
        background: linear-gradient(135deg, #667eea 0%, #764ba2 100%);
        -webkit-background-clip: text;
        -webkit-text-fill-color: transparent;
        background-clip: text;
    }
    .info-box {
        background: linear-gradient(135deg, #667eea20 0%, #764ba220 100%);
        padding: 1.5rem;
        border-radius: 10px;
        margin-bottom: 2rem;
        border: 1px solid #667eea40;
    }
    .info-box h3 {
        color: #667eea;
        margin-top: 0;
    }
    .info-box p {
        color: #333;
        font-size: 1.1rem;
    }
    .card {
        background: linear-gradient(135deg, #667eea 0%, #764ba2 100%);
        padding: 1.5rem;
        border-radius: 10px;
        color: white;
        box-shadow: 0 4px 6px rgba(0,0,0,0.1);
    }
    .card h4 {
        color: white;
        margin-top: 0;
    }
    .card p {
        color: rgba(255,255,255,0.9);
    }
    .parameter-slider {
        margin-bottom: 1rem;
    }
    </style>
""", unsafe_allow_html=True)

# Навигационная цепочка
st.markdown("""
    <div style='background: #f0f2f6; padding: 0.5rem 1rem; border-radius: 5px; margin-bottom: 1rem;'>
        <a href="/" target="_self" style='text-decoration: none; color: #667eea;'>Главная</a> / 
        <span style='color: #764ba2;'>Механическое движение</span>
    </div>
""", unsafe_allow_html=True)

# Заголовок
st.title("📐 Механическое движение")
st.markdown("""
    <div class="info-box">
        <h3>📝 Описание раздела</h3>
        <p>
            Механика — раздел физики, изучающий движение тел и взаимодействие между ними.
            В этом разделе вы можете моделировать различные виды механического движения:
            равномерное и равноускоренное движение, движение под углом к горизонту,
            колебания и многое другое.
        </p>
    </div>
""", unsafe_allow_html=True)

# Создаем вкладки для разных видов движения
tab1, tab2, tab3, tab4, tab5 = st.tabs([
    "📈 Равноускоренное движение",
    "🎯 Движение под углом",
    "🔄 Колебания",
    "⚡ Импульс и энергия",
    "📊 Сравнение движений"
])

with tab1:
    st.header("Равноускоренное прямолинейное движение")
    
    col1, col2 = st.columns([1, 2])
    
    with col1:
        st.markdown("""
        <div class="card" style="margin-bottom: 1rem;">
            <h4>Основные формулы</h4>
            <p>
                v = v₀ + at<br>
                s = v₀t + at²/2<br>
                v² = v₀² + 2as
            </p>
        </div>
        """, unsafe_allow_html=True)
        
        # Параметры движения
        v0 = st.number_input("Начальная скорость v₀ (м/с)", value=10.0, step=1.0)
        a = st.number_input("Ускорение a (м/с²)", value=2.0, step=0.5)
        t_max = st.slider("Время движения t (с)", 1, 20, 10, 1)
        
        # Расчет
        t = np.linspace(0, t_max, 100)
        v = v0 + a * t
        s = v0 * t + 0.5 * a * t**2
        
        # Конечные значения
        v_final = v0 + a * t_max
        s_final = v0 * t_max + 0.5 * a * t_max**2
        
        st.info(f"""
        **Результаты:**
        - Конечная скорость: {v_final:.1f} м/с
        - Пройденный путь: {s_final:.1f} м
        - Средняя скорость: {(v0 + v_final)/2:.1f} м/с
        """)
    
    with col2:
        # Создаем графики
        fig = make_subplots(rows=2, cols=1, 
                           subplot_titles=("График скорости v(t)", "График пути s(t)"))
        
        # График скорости
        fig.add_trace(
            go.Scatter(x=t, y=v, mode='lines', name='v(t)',
                      line=dict(color='#667eea', width=3)),
            row=1, col=1
        )
        
        # График пути
        fig.add_trace(
            go.Scatter(x=t, y=s, mode='lines', name='s(t)',
                      line=dict(color='#764ba2', width=3)),
            row=2, col=1
        )
        
        # Отметим начальную и конечную точки
        fig.add_trace(
            go.Scatter(x=[0], y=[v0], mode='markers', 
                      marker=dict(size=10, color='red'),
                      name='Начальная скорость', showlegend=False),
            row=1, col=1
        )
        
        fig.add_trace(
            go.Scatter(x=[t_max], y=[v_final], mode='markers',
                      marker=dict(size=10, color='green'),
                      name='Конечная скорость', showlegend=False),
            row=1, col=1
        )
        
        fig.update_layout(height=600, showlegend=True,
                         title_text="Кинематические графики")
        
        fig.update_xaxes(title_text="Время t (с)", row=1, col=1)
        fig.update_yaxes(title_text="Скорость v (м/с)", row=1, col=1)
        fig.update_xaxes(title_text="Время t (с)", row=2, col=1)
        fig.update_yaxes(title_text="Путь s (м)", row=2, col=1)
        
        fig.update_xaxes(showgrid=True, gridwidth=1, gridcolor='LightGray')
        fig.update_yaxes(showgrid=True, gridwidth=1, gridcolor='LightGray')
        
        st.plotly_chart(fig, use_container_width=True)

with tab2:
    st.header("Движение тела, брошенного под углом к горизонту")
    
    col1, col2 = st.columns([1, 2])
    
    with col1:
        st.markdown("""
        <div class="card" style="margin-bottom: 1rem;">
            <h4>Траектория полета</h4>
            <p>
                x = v₀·cos(α)·t<br>
                y = v₀·sin(α)·t - gt²/2<br>
                Время полета: T = 2v₀·sin(α)/g<br>
                Дальность: L = v₀²·sin(2α)/g<br>
                Высота: H = v₀²·sin²(α)/(2g)
            </p>
        </div>
        """, unsafe_allow_html=True)
        
        # Параметры
        v0 = st.number_input("Начальная скорость v₀ (м/с)", value=20.0, step=1.0, key="proj_v0")
        angle = st.slider("Угол броска α (градусы)", 1, 89, 45, 1)
        g = st.selectbox("Ускорение свободного падения g", 
                         ["Земля (9.8 м/с²)", "Луна (1.62 м/с²)", "Марс (3.71 м/с²)"])
        
        g_values = {
            "Земля (9.8 м/с²)": 9.8,
            "Луна (1.62 м/с²)": 1.62,
            "Марс (3.71 м/с²)": 3.71
        }
        g_val = g_values[g]
        
        # Перевод угла в радианы
        alpha = math.radians(angle)
        
        # Расчет параметров полета
        T = 2 * v0 * math.sin(alpha) / g_val
        L = v0**2 * math.sin(2*alpha) / g_val
        H = (v0**2 * (math.sin(alpha))**2) / (2 * g_val)
        
        # Траектория
        t = np.linspace(0, T, 100)
        x = v0 * np.cos(alpha) * t
        y = v0 * np.sin(alpha) * t - 0.5 * g_val * t**2
        
        st.info(f"""
        **Параметры полета:**
        - Время полета: {T:.2f} с
        - Дальность: {L:.2f} м
        - Максимальная высота: {H:.2f} м
        - Начальная скорость по X: {v0*np.cos(alpha):.2f} м/с
        - Начальная скорость по Y: {v0*np.sin(alpha):.2f} м/с
        """)
    
    with col2:
        fig = go.Figure()
        
        # Траектория
        fig.add_trace(go.Scatter(
            x=x, y=y,
            mode='lines',
            name='Траектория',
            line=dict(color='#667eea', width=4),
            fill='tozeroy',
            fillcolor='rgba(102, 126, 234, 0.2)'
        ))
        
        # Начальная точка
        fig.add_trace(go.Scatter(
            x=[0], y=[0],
            mode='markers',
            marker=dict(size=12, color='red'),
            name='Старт'
        ))
        
        # Конечная точка
        fig.add_trace(go.Scatter(
            x=[L], y=[0],
            mode='markers',
            marker=dict(size=12, color='green'),
            name='Финиш'
        ))
        
        # Векторы скорости
        scale = 0.5
        fig.add_annotation(
            x=0, y=0,
            ax=scale * v0 * np.cos(alpha),
            ay=scale * v0 * np.sin(alpha),
            xref="x", yref="y",
            axref="x", ayref="y",
            text="v₀",
            showarrow=True,
            arrowhead=2,
            arrowsize=1,
            arrowwidth=2,
            arrowcolor='red'
        )
        
        fig.update_layout(
            title=f"Траектория полета (α={angle}°, v₀={v0} м/с)",
            xaxis_title="Расстояние x (м)",
            yaxis_title="Высота y (м)",
            height=500,
            showlegend=True,
            hovermode='x'
        )
        
        fig.update_xaxes(showgrid=True, gridwidth=1, gridcolor='LightGray')
        fig.update_yaxes(showgrid=True, gridwidth=1, gridcolor='LightGray')
        
        # Устанавливаем одинаковый масштаб осей
        max_range = max(L, H) * 1.1
        fig.update_xaxes(range=[0, max_range])
        fig.update_yaxes(range=[0, max_range])
        
        st.plotly_chart(fig, use_container_width=True)
        
        # Оптимальный угол
        st.markdown("""
        <div style='background: #f0f2f6; padding: 1rem; border-radius: 5px; margin-top: 1rem;'>
            <p style='margin:0; color:#333;'>
                <strong>Интересный факт:</strong> Максимальная дальность полета достигается при угле 45° 
                (при отсутствии сопротивления воздуха).
            </p>
        </div>
        """, unsafe_allow_html=True)

with tab3:
    st.header("Гармонические колебания")
    
    col1, col2 = st.columns([1, 2])
    
    with col1:
        st.markdown("""
        <div class="card" style="margin-bottom: 1rem;">
            <h4>Уравнение колебаний</h4>
            <p>
                x = A·sin(ωt + φ)<br>
                v = Aω·cos(ωt + φ)<br>
                a = -Aω²·sin(ωt + φ)<br>
                ω = 2π/T = 2πf
            </p>
        </div>
        """, unsafe_allow_html=True)
        
        # Параметры колебаний
        A = st.slider("Амплитуда A (м)", 0.1, 5.0, 1.0, 0.1)
        f = st.slider("Частота f (Гц)", 0.1, 5.0, 1.0, 0.1)
        phi = st.slider("Начальная фаза φ (градусы)", 0, 360, 0, 15)
        
        # Расчет
        omega = 2 * np.pi * f
        T = 1 / f
        t = np.linspace(0, 3*T, 300)
        
        x = A * np.sin(omega * t + np.radians(phi))
        v = A * omega * np.cos(omega * t + np.radians(phi))
        a = -A * omega**2 * np.sin(omega * t + np.radians(phi))
        
        st.info(f"""
        **Характеристики:**
        - Период T = {T:.3f} с
        - Циклическая частота ω = {omega:.3f} рад/с
        - Максимальная скорость: {A*omega:.3f} м/с
        - Максимальное ускорение: {A*omega**2:.3f} м/с²
        """)
    
    with col2:
        fig = make_subplots(rows=3, cols=1,
                           subplot_titles=("Смещение x(t)", "Скорость v(t)", "Ускорение a(t)"))
        
        # Смещение
        fig.add_trace(
            go.Scatter(x=t, y=x, mode='lines', name='x(t)',
                      line=dict(color='#667eea', width=3)),
            row=1, col=1
        )
        
        # Скорость
        fig.add_trace(
            go.Scatter(x=t, y=v, mode='lines', name='v(t)',
                      line=dict(color='#764ba2', width=3)),
            row=2, col=1
        )
        
        # Ускорение
        fig.add_trace(
            go.Scatter(x=t, y=a, mode='lines', name='a(t)',
                      line=dict(color='#ff6b6b', width=3)),
            row=3, col=1
        )
        
        # Горизонтальные линии для амплитуд
        fig.add_hline(y=A, line_dash="dash", line_color="gray", row=1, col=1)
        fig.add_hline(y=-A, line_dash="dash", line_color="gray", row=1, col=1)
        
        fig.update_layout(height=700, showlegend=False,
                         title_text="Гармонические колебания")
        
        fig.update_xaxes(title_text="Время t (с)", row=3, col=1)
        fig.update_xaxes(title_text="", row=1, col=1)
        fig.update_xaxes(title_text="", row=2, col=1)
        
        fig.update_yaxes(title_text="x (м)", row=1, col=1)
        fig.update_yaxes(title_text="v (м/с)", row=2, col=1)
        fig.update_yaxes(title_text="a (м/с²)", row=3, col=1)
        
        fig.update_xaxes(showgrid=True, gridwidth=1, gridcolor='LightGray')
        fig.update_yaxes(showgrid=True, gridwidth=1, gridcolor='LightGray')
        
        st.plotly_chart(fig, use_container_width=True)

with tab4:
    st.header("Импульс и энергия")
    
    col1, col2 = st.columns([1, 2])
    
    with col1:
        st.markdown("""
        <div class="card" style="margin-bottom: 1rem;">
            <h4>Законы сохранения</h4>
            <p>
                <strong>Импульс:</strong> p = mv<br>
                <strong>Кинетическая энергия:</strong> Eₖ = mv²/2<br>
                <strong>Потенциальная энергия:</strong> Eₚ = mgh<br>
                <strong>Полная энергия:</strong> E = Eₖ + Eₚ
            </p>
        </div>
        """, unsafe_allow_html=True)
        
        # Параметры
        m = st.number_input("Масса тела m (кг)", value=2.0, step=0.5)
        h = st.slider("Высота h (м)", 0, 50, 20, 1)
        g_energy = st.selectbox("Ускорение свободного падения g", 
                                ["Земля (9.8 м/с²)", "Луна (1.62 м/с²)", "Марс (3.71 м/с²)"],
                                key="energy_g")
        
        g_energy_val = {
            "Земля (9.8 м/с²)": 9.8,
            "Луна (1.62 м/с²)": 1.62,
            "Марс (3.71 м/с²)": 3.71
        }[g_energy]
        
        # Расчет энергии
        Ep_max = m * g_energy_val * h
        v_max = math.sqrt(2 * g_energy_val * h)
        Ek_max = m * v_max**2 / 2
        
        # Для графика
        y = np.linspace(0, h, 50)
        Ep = m * g_energy_val * y
        Ek = Ep_max - Ep
        E_total = Ep + Ek
        
        st.info(f"""
        **Энергетические характеристики:**
        - Макс. потенциальная энергия: {Ep_max:.2f} Дж
        - Макс. кинетическая энергия: {Ek_max:.2f} Дж
        - Макс. скорость: {v_max:.2f} м/с
        - Полная энергия: {E_total[0]:.2f} Дж
        """)
    
    with col2:
        fig = go.Figure()
        
        # Потенциальная энергия
        fig.add_trace(go.Scatter(
            x=Ep, y=y,
            mode='lines',
            name='Потенциальная энергия Eₚ',
            line=dict(color='#667eea', width=3),
            fill='tozerox',
            fillcolor='rgba(102, 126, 234, 0.3)'
        ))
        
        # Кинетическая энергия
        fig.add_trace(go.Scatter(
            x=Ek, y=y,
            mode='lines',
            name='Кинетическая энергия Eₖ',
            line=dict(color='#764ba2', width=3),
            fill='tozerox',
            fillcolor='rgba(118, 75, 162, 0.3)'
        ))
        
        # Полная энергия
        fig.add_trace(go.Scatter(
            x=E_total, y=y,
            mode='lines',
            name='Полная энергия E',
            line=dict(color='#ff6b6b', width=2, dash='dash')
        ))
        
        fig.update_layout(
            title=f"Изменение энергии при падении (m={m} кг, h={h} м)",
            xaxis_title="Энергия E (Дж)",
            yaxis_title="Высота y (м)",
            height=500,
            showlegend=True,
            hovermode='y'
        )
        
        fig.update_xaxes(showgrid=True, gridwidth=1, gridcolor='LightGray')
        fig.update_yaxes(showgrid=True, gridwidth=1, gridcolor='LightGray')
        
        # Инвертируем ось Y для правильного отображения высоты
        fig.update_yaxes(autorange="reversed")
        
        st.plotly_chart(fig, use_container_width=True)

with tab5:
    st.header("Сравнение различных видов движения")
    
    # Выбор типа движения для сравнения
    col1, col2 = st.columns(2)
    
    with col1:
        motion1 = st.selectbox(
            "Движение 1",
            ["Равномерное", "Равноускоренное", "Гармонические колебания", "Под углом к горизонту"]
        )
    
    with col2:
        motion2 = st.selectbox(
            "Движение 2",
            ["Равномерное", "Равноускоренное", "Гармонические колебания", "Под углом к горизонту"],
            index=1
        )
    
    # Создаем общий график для сравнения
    fig = go.Figure()
    
    t_compare = np.linspace(0, 10, 100)
    
    # Функции для разных типов движения
    def get_position(motion_type, t):
        if motion_type == "Равномерное":
            return 2 * t
        elif motion_type == "Равноускоренное":
            return 0.5 * 2 * t**2
        elif motion_type == "Гармонические колебания":
            return 5 * np.sin(2 * np.pi * 0.2 * t)
        else:  # Под углом к горизонту
            return 20 * np.cos(np.radians(45)) * t
    
    y1 = get_position(motion1, t_compare)
    y2 = get_position(motion2, t_compare)
    
    # Цвета для графиков
    colors = ['#667eea', '#764ba2', '#ff6b6b', '#4ecdc4']
    
    fig.add_trace(go.Scatter(
        x=t_compare, y=y1,
        mode='lines',
        name=motion1,
        line=dict(color=colors[0], width=3)
    ))
    
    fig.add_trace(go.Scatter(
        x=t_compare, y=y2,
        mode='lines',
        name=motion2,
        line=dict(color=colors[1], width=3, dash='dash')
    ))
    
    fig.update_layout(
        title="Сравнение траекторий движения",
        xaxis_title="Время t (с)",
        yaxis_title="Перемещение x (м)",
        height=500,
        showlegend=True,
        hovermode='x'
    )
    
    fig.update_xaxes(showgrid=True, gridwidth=1, gridcolor='LightGray')
    fig.update_yaxes(showgrid=True, gridwidth=1, gridcolor='LightGray')
    
    st.plotly_chart(fig, use_container_width=True)
    
    # Таблица сравнения
    st.subheader("📊 Сравнительная таблица")
    
    comparison_data = {
        "Характеристика": ["Тип движения", "Уравнение движения", "Скорость", "Ускорение", "Примеры"],
        motion1: [
            motion1,
            {
                "Равномерное": "x = x₀ + vt",
                "Равноускоренное": "x = x₀ + v₀t + at²/2",
                "Гармонические колебания": "x = A·sin(ωt + φ)",
                "Под углом к горизонту": "x = v₀·cos(α)·t, y = v₀·sin(α)·t - gt²/2"
            }[motion1],
            {
                "Равномерное": "v = const",
                "Равноускоренное": "v = v₀ + at",
                "Гармонические колебания": "v = Aω·cos(ωt + φ)",
                "Под углом к горизонту": "vₓ = const, vᵧ = v₀·sin(α) - gt"
            }[motion1],
            {
                "Равномерное": "a = 0",
                "Равноускоренное": "a = const",
                "Гармонические колебания": "a = -ω²x",
                "Под углом к горизонту": "aₓ = 0, aᵧ = -g"
            }[motion1],
            {
                "Равномерное": "Автомобиль на шоссе",
                "Равноускоренное": "Разгон поезда",
                "Гармонические колебания": "Маятник, пружина",
                "Под углом к горизонту": "Спортивный снаряд"
            }[motion1]
        ],
        motion2: [
            motion2,
            {
                "Равномерное": "x = x₀ + vt",
                "Равноускоренное": "x = x₀ + v₀t + at²/2",
                "Гармонические колебания": "x = A·sin(ωt + φ)",
                "Под углом к горизонту": "x = v₀·cos(α)·t, y = v₀·sin(α)·t - gt²/2"
            }[motion2],
            {
                "Равномерное": "v = const",
                "Равноускоренное": "v = v₀ + at",
                "Гармонические колебания": "v = Aω·cos(ωt + φ)",
                "Под углом к горизонту": "vₓ = const, vᵧ = v₀·sin(α) - gt"
            }[motion2],
            {
                "Равномерное": "a = 0",
                "Равноускоренное": "a = const",
                "Гармонические колебания": "a = -ω²x",
                "Под углом к горизонту": "aₓ = 0, aᵧ = -g"
            }[motion2],
            {
                "Равномерное": "Автомобиль на шоссе",
                "Равноускоренное": "Разгон поезда",
                "Гармонические колебания": "Маятник, пружина",
                "Под углом к горизонту": "Спортивный снаряд"
            }[motion2]
        ]
    }
    
    df = pd.DataFrame(comparison_data)
    st.table(df)

# Добавляем теоретическую справку
st.markdown("---")
st.header("📚 Теоретическая справка")

with st.expander("Основные формулы механики", expanded=False):
    col1, col2, col3 = st.columns(3)
    
    with col1:
        st.markdown("""
        ### Кинематика
        **Скорость:** v = ds/dt
        **Ускорение:** a = dv/dt
        
        **Равномерное движение:**
        s = vt
        
        **Равноускоренное движение:**
        v = v₀ + at
        s = v₀t + at²/2
        v² = v₀² + 2as
        """)
    
    with col2:
        st.markdown("""
        ### Динамика
        **2-й закон Ньютона:** F = ma
        **Сила тяжести:** F = mg
        **Сила упругости:** F = -kx
        **Сила трения:** F = μN
        
        ### Импульс
        **Импульс:** p = mv
        **Закон сохранения:** Σp = const
        """)
    
    with col3:
        st.markdown("""
        ### Энергия
        **Кинетическая:** Eₖ = mv²/2
        **Потенциальная:** 
        - Eₚ = mgh (гравитация)
        - Eₚ = kx²/2 (упругость)
        
        **Закон сохранения:** 
        E = Eₖ + Eₚ = const
        """)

# Footer
st.markdown("---")
st.markdown("""
    <div style='text-align: center; color: gray; padding: 1rem;'>
        <p>📐 Моделирование механического движения | Версия 1.0.0</p>
        <p>Используйте вкладки для выбора различных видов движения</p>
    </div>
""", unsafe_allow_html=True)