import streamlit as st
import numpy as np
import pandas as pd
import plotly.graph_objects as go
from plotly.subplots import make_subplots
import math

# Настройка страницы
st.set_page_config(
    page_title="Оптика - Моделирование",
    page_icon="💡",
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
    </style>
""", unsafe_allow_html=True)

# Навигационная цепочка
st.markdown("""
    <div style='background: #f0f2f6; padding: 0.5rem 1rem; border-radius: 5px; margin-bottom: 1rem;'>
        <a href="/" target="_self" style='text-decoration: none; color: #667eea;'>Главная</a> / 
        <span style='color: #764ba2;'>Оптика</span>
    </div>
""", unsafe_allow_html=True)

# Заголовок
st.title("💡 Оптика")
st.markdown("""
    <div class="info-box">
        <h3>📝 Описание раздела</h3>
        <p>
            Оптика — раздел физики, изучающий природу света, оптические явления и взаимодействие света с веществом.
            В этом разделе вы можете моделировать различные оптические явления: преломление света, 
            прохождение через линзы, интерференцию и дифракцию.
        </p>
    </div>
""", unsafe_allow_html=True)

# Создаем вкладки для разных оптических явлений
tab1, tab2, tab3, tab4 = st.tabs([
    "🔍 Преломление света", 
    "🔬 Линзы", 
    "🌈 Интерференция",
    "📐 Дифракция"
])

with tab1:
    st.header("Преломление света (Закон Снеллиуса)")
    
    col1, col2 = st.columns([1, 2])
    
    with col1:
        st.markdown("""
        <div class="card" style="margin-bottom: 1rem;">
            <h4 style="color: white; margin-top: 0;">Закон преломления</h4>
            <p style="color: rgba(255,255,255,0.9);">
                n₁·sin(θ₁) = n₂·sin(θ₂)
            </p>
            <p style="color: rgba(255,255,255,0.8); font-size: 0.9rem;">
                где:<br>
                θ₁ - угол падения<br>
                θ₂ - угол преломления<br>
                n₁, n₂ - показатели преломления сред
            </p>
        </div>
        """, unsafe_allow_html=True)
        
        # Параметры для преломления
        n1 = st.selectbox("Среда 1 (падающий луч)", 
                          ["Воздух (n=1.00)", "Вода (n=1.33)", "Стекло (n=1.50)", "Алмаз (n=2.42)"])
        n2 = st.selectbox("Среда 2 (преломленный луч)", 
                          ["Воздух (n=1.00)", "Вода (n=1.33)", "Стекло (n=1.50)", "Алмаз (n=2.42)"])
        
        # Преобразуем выбор в числовые значения
        n_values = {
            "Воздух (n=1.00)": 1.00,
            "Вода (n=1.33)": 1.33,
            "Стекло (n=1.50)": 1.50,
            "Алмаз (n=2.42)": 2.42
        }
        n1_val = n_values[n1]
        n2_val = n_values[n2]
        
        angle_incident = st.slider("Угол падения θ₁ (градусы)", 0, 89, 45, 1)
        
        # Расчет угла преломления по закону Снеллиуса
        theta1_rad = math.radians(angle_incident)
        try:
            theta2_rad = math.asin((n1_val / n2_val) * math.sin(theta1_rad))
            theta2_deg = math.degrees(theta2_rad)
            
            # Явление полного внутреннего отражения
            if n1_val > n2_val and (n1_val / n2_val) * math.sin(theta1_rad) > 1:
                st.warning("⚠️ Полное внутреннее отражение! Свет не проходит во вторую среду.")
                theta2_deg = 90
        except:
            st.warning("⚠️ Полное внутреннее отражение! Свет не проходит во вторую среду.")
            theta2_deg = 90
        
        st.info(f"**Угол преломления θ₂:** {theta2_deg:.1f}°")
        
        # Отношение скоростей
        st.markdown("""
        <div style="background: #f0f2f6; padding: 1rem; border-radius: 5px; margin-top: 1rem;">
            <p style="margin: 0; color: #333;">
                <strong>Отношение скоростей света:</strong><br>
                v₁/v₂ = n₂/n₁ = {:.3f}
            </p>
        </div>
        """.format(n2_val/n1_val), unsafe_allow_html=True)
    
    with col2:
        # Создаем визуализацию преломления
        fig = go.Figure()
        
        # Границы сред
        fig.add_shape(type="line", x0=-10, y0=0, x1=10, y1=0,
                     line=dict(color="black", width=2))
        
        # Нормаль
        fig.add_shape(type="line", x0=0, y0=-5, x1=0, y1=5,
                     line=dict(color="gray", width=1, dash="dash"))
        
        # Падающий луч
        x_incident = [-5 * math.cos(theta1_rad), 0]
        y_incident = [5 * math.sin(theta1_rad), 0]
        fig.add_trace(go.Scatter(
            x=x_incident, y=y_incident,
            mode='lines+markers',
            name='Падающий луч',
            line=dict(color='blue', width=3),
            marker=dict(size=8, symbol='circle')
        ))
        
        # Преломленный луч
        if theta2_deg < 90:
            x_refracted = [0, 5 * math.cos(theta2_rad)]
            y_refracted = [0, -5 * math.sin(theta2_rad)]
            fig.add_trace(go.Scatter(
                x=x_refracted, y=y_refracted,
                mode='lines+markers',
                name='Преломленный луч',
                line=dict(color='red', width=3),
                marker=dict(size=8, symbol='circle')
            ))
        
        # Отраженный луч (для полного внутреннего отражения)
        if theta2_deg >= 90:
            x_reflected = [0, -5 * math.cos(theta1_rad)]
            y_reflected = [0, -5 * math.sin(theta1_rad)]
            fig.add_trace(go.Scatter(
                x=x_reflected, y=y_reflected,
                mode='lines+markers',
                name='Отраженный луч',
                line=dict(color='orange', width=3, dash='dash'),
                marker=dict(size=8, symbol='circle')
            ))
        
        # Подписи сред
        fig.add_annotation(x=5, y=2.5, text="Среда 1", showarrow=False, font=dict(size=14))
        fig.add_annotation(x=5, y=-2.5, text="Среда 2", showarrow=False, font=dict(size=14))
        
        fig.update_layout(
            title="Визуализация преломления света",
            xaxis_title="X",
            yaxis_title="Y",
            xaxis_range=[-6, 6],
            yaxis_range=[-4, 4],
            height=500,
            showlegend=True,
            plot_bgcolor='rgba(240,240,240,0.5)'
        )
        
        fig.update_xaxes(showgrid=True, gridwidth=1, gridcolor='LightGray')
        fig.update_yaxes(showgrid=True, gridwidth=1, gridcolor='LightGray')
        
        st.plotly_chart(fig, use_container_width=True)

with tab2:
    st.header("Линзы")
    
    col1, col2 = st.columns([1, 2])
    
    with col1:
        st.markdown("""
        <div class="card" style="margin-bottom: 1rem;">
            <h4 style="color: white; margin-top: 0;">Формула тонкой линзы</h4>
            <p style="color: rgba(255,255,255,0.9);">
                1/F = 1/d₀ + 1/d₁
            </p>
            <p style="color: rgba(255,255,255,0.8); font-size: 0.9rem;">
                где:<br>
                F - фокусное расстояние<br>
                d₀ - расстояние до предмета<br>
                d₁ - расстояние до изображения
            </p>
        </div>
        """, unsafe_allow_html=True)
        
        lens_type = st.radio("Тип линзы", ["Собирающая (F > 0)", "Рассеивающая (F < 0)"])
        
        if lens_type == "Собирающая (F > 0)":
            F = st.slider("Фокусное расстояние F (см)", 5, 50, 20, 1)
        else:
            F = -st.slider("Фокусное расстояние F (см)", 5, 50, 20, 1)
        
        d0 = st.slider("Расстояние до предмета d₀ (см)", 1, 100, 30, 1)
        
        # Расчет положения изображения
        try:
            d1 = 1 / (1/F - 1/d0) if abs(1/F - 1/d0) > 0.001 else float('inf')
            
            # Расчет увеличения
            magnification = -d1/d0 if d1 != float('inf') else 0
            
            st.info(f"""
            **Характеристики изображения:**
            - Расстояние до изображения: {d1:.1f} см
            - Увеличение: {abs(magnification):.2f}x
            - Изображение: {'действительное' if d1 > 0 else 'мнимое'}, 
              {'перевернутое' if magnification < 0 else 'прямое'}, 
              {'увеличенное' if abs(magnification) > 1 else 'уменьшенное' if abs(magnification) < 1 else 'того же размера'}
            """)
            
        except:
            st.error("Ошибка расчета. Предмет в фокусе?")
            d1 = float('inf')
            magnification = 0
    
    with col2:
        # Визуализация линзы
        fig = go.Figure()
        
        # Рисуем линзу
        if F > 0:
            # Собирающая линза
            x_lens = [0, 0]
            y_lens = [-3, 3]
            fig.add_trace(go.Scatter(
                x=x_lens, y=y_lens,
                mode='lines',
                name='Линза',
                line=dict(color='black', width=3)
            ))
            # Фокусы
            fig.add_shape(type="line", x0=F, y0=-0.2, x1=F, y1=0.2,
                         line=dict(color="red", width=2))
            fig.add_shape(type="line", x0=-F, y0=-0.2, x1=-F, y1=0.2,
                         line=dict(color="red", width=2))
            fig.add_annotation(x=F, y=0.5, text="F", showarrow=False)
            fig.add_annotation(x=-F, y=0.5, text="F", showarrow=False)
        else:
            # Рассеивающая линза
            x_lens = [0, 0]
            y_lens = [-3, 3]
            fig.add_trace(go.Scatter(
                x=x_lens, y=y_lens,
                mode='lines',
                name='Линза',
                line=dict(color='black', width=3, dash='dash')
            ))
            # Мнимые фокусы
            fig.add_shape(type="line", x0=abs(F), y0=-0.2, x1=abs(F), y1=0.2,
                         line=dict(color="red", width=2, dash='dash'))
            fig.add_shape(type="line", x0=-abs(F), y0=-0.2, x1=-abs(F), y1=0.2,
                         line=dict(color="red", width=2, dash='dash'))
            fig.add_annotation(x=abs(F), y=0.5, text="F", showarrow=False)
            fig.add_annotation(x=-abs(F), y=0.5, text="F", showarrow=False)
        
        # Предмет
        fig.add_trace(go.Scatter(
            x=[-d0, -d0], y=[0, 1],
            mode='lines+markers',
            name='Предмет',
            line=dict(color='blue', width=3),
            marker=dict(size=8, symbol='square')
        ))
        
        # Изображение
        if d1 != float('inf') and abs(d1) < 100:
            image_height = 1 * abs(magnification)
            if d1 > 0:
                x_image = d1
                y_image = [0, image_height] if magnification > 0 else [0, -image_height]
            else:
                x_image = d1
                y_image = [0, image_height] if magnification > 0 else [0, -image_height]
            
            fig.add_trace(go.Scatter(
                x=[x_image, x_image], y=y_image,
                mode='lines+markers',
                name='Изображение',
                line=dict(color='green', width=3),
                marker=dict(size=8, symbol='triangle-up')
            ))
        
        fig.update_layout(
            title="Ход лучей в линзе",
            xaxis_title="Расстояние (см)",
            yaxis_title="Высота (см)",
            xaxis_range=[-50, 50],
            yaxis_range=[-5, 5],
            height=500,
            showlegend=True
        )
        
        fig.update_xaxes(showgrid=True, gridwidth=1, gridcolor='LightGray')
        fig.update_yaxes(showgrid=True, gridwidth=1, gridcolor='LightGray')
        
        st.plotly_chart(fig, use_container_width=True)

with tab3:
    st.header("Интерференция света")
    
    col1, col2 = st.columns([1, 2])
    
    with col1:
        st.markdown("""
        <div class="card" style="margin-bottom: 1rem;">
            <h4 style="color: white; margin-top: 0;">Условие интерференции</h4>
            <p style="color: rgba(255,255,255,0.9);">
                Δd = k·λ - максимум<br>
                Δd = (2k+1)·λ/2 - минимум
            </p>
        </div>
        """, unsafe_allow_html=True)
        
        wavelength = st.slider("Длина волны λ (нм)", 380, 750, 550, 10)
        d_slits = st.slider("Расстояние между щелями d (мкм)", 1, 100, 20, 1)
        L = st.slider("Расстояние до экрана L (м)", 0.5, 5.0, 1.0, 0.1)
        
        # Конвертация единиц
        wavelength_m = wavelength * 1e-9
        d_slits_m = d_slits * 1e-6
        
        # Расчет положения максимумов
        x_max = []
        intensity = []
        for k in range(-5, 6):
            if k != 0:
                x = k * wavelength_m * L / d_slits_m
                x_max.append(x * 100)  # в см
                intensity.append(1.0)
        
        # Цвет в зависимости от длины волны
        if wavelength < 450:
            color = 'violet'
        elif wavelength < 500:
            color = 'blue'
        elif wavelength < 570:
            color = 'green'
        elif wavelength < 620:
            color = 'orange'
        else:
            color = 'red'
    
    with col2:
        # Визуализация интерференционной картины
        fig = make_subplots(rows=2, cols=1, 
                           subplot_titles=("Интерференционная картина на экране", 
                                         "Распределение интенсивности"))
        
        # Создаем интерференционную картину
        x = np.linspace(-5, 5, 1000)  # в см
        x_m = x / 100  # в метрах
        
        # Интенсивность для двух щелей
        beta = (np.pi * d_slits_m * x_m) / (wavelength_m * L)
        I = (np.cos(beta))**2
        
        # Нормируем интенсивность
        I = I / np.max(I)
        
        # Рисуем интерференционные полосы
        for i in range(len(x)-1):
            fig.add_trace(
                go.Scatter(
                    x=[x[i], x[i+1]],
                    y=[I[i], I[i+1]],
                    mode='lines',
                    line=dict(color=color, width=2),
                    showlegend=False
                ),
                row=2, col=1
            )
        
        # Добавляем маркеры для максимумов
        fig.add_trace(
            go.Scatter(
                x=x_max,
                y=[1.0] * len(x_max),
                mode='markers',
                marker=dict(size=10, color='red', symbol='star'),
                name='Максимумы',
                showlegend=True
            ),
            row=2, col=1
        )
        
        # Визуализация полос на экране
        y_pixels = np.linspace(-0.5, 0.5, 100)
        X, Y = np.meshgrid(x, y_pixels)
        Z = np.tile(I, (100, 1))
        
        fig.add_trace(
            go.Heatmap(
                x=x,
                y=y_pixels,
                z=Z,
                colorscale='Viridis',
                showscale=False,
                name='Интерференционные полосы'
            ),
            row=1, col=1
        )
        
        fig.update_layout(
            height=600,
            showlegend=True,
            title_text=f"Интерференция света (λ={wavelength} нм, d={d_slits} мкм)"
        )
        
        fig.update_xaxes(title_text="Положение на экране x (см)", row=1, col=1)
        fig.update_yaxes(title_text="y (см)", row=1, col=1)
        fig.update_xaxes(title_text="Положение на экране x (см)", row=2, col=1)
        fig.update_yaxes(title_text="Интенсивность I (отн. ед.)", row=2, col=1)
        
        st.plotly_chart(fig, use_container_width=True)
        
        st.info(f"""
        **Параметры интерференции:**
        - Длина волны: {wavelength} нм ({color})
        - Период интерференционной картины: {(wavelength_m * L / d_slits_m * 100):.2f} см
        - Количество наблюдаемых максимумов: {len(x_max)}
        """)

with tab4:
    st.header("Дифракция на щели")
    
    col1, col2 = st.columns([1, 2])
    
    with col1:
        st.markdown("""
        <div class="card" style="margin-bottom: 1rem;">
            <h4 style="color: white; margin-top: 0;">Дифракция Фраунгофера</h4>
            <p style="color: rgba(255,255,255,0.9);">
                I(θ) = I₀·(sin(β)/β)²
            </p>
            <p style="color: rgba(255,255,255,0.8); font-size: 0.9rem;">
                где β = (π·a·sin(θ))/λ
            </p>
        </div>
        """, unsafe_allow_html=True)
        
        wavelength_diff = st.slider("Длина волны λ (нм)", 380, 750, 550, 10, key="diff_wl")
        slit_width = st.slider("Ширина щели a (мкм)", 10, 200, 50, 5)
        L_diff = st.slider("Расстояние до экрана L (м)", 0.5, 5.0, 1.0, 0.1, key="diff_L")
        
        # Конвертация
        wavelength_m = wavelength_diff * 1e-9
        slit_width_m = slit_width * 1e-6
        
        # Расчет углов и интенсивности
        theta = np.linspace(-0.1, 0.1, 1000)  # радианы
        beta = (np.pi * slit_width_m * np.sin(theta)) / wavelength_m
        
        # Интенсивность для дифракции на одной щели
        I_diff = (np.sin(beta) / (beta + 1e-10))**2
        I_diff = I_diff / np.max(I_diff)
        
        # Положение на экране
        x_diff = L_diff * np.tan(theta) * 100  # в см
        
        # Положение минимумов
        minima_pos = []
        for k in range(1, 4):
            theta_min = np.arcsin(k * wavelength_m / slit_width_m)
            if not np.isnan(theta_min):
                x_min = L_diff * np.tan(theta_min) * 100
                minima_pos.append(x_min)
    
    with col2:
        fig = go.Figure()
        
        # График интенсивности
        fig.add_trace(go.Scatter(
            x=x_diff,
            y=I_diff,
            mode='lines',
            name='Интенсивность',
            line=dict(color='blue', width=3),
            fill='tozeroy',
            fillcolor='rgba(102, 126, 234, 0.3)'
        ))
        
        # Отметить минимумы
        for i, x_min in enumerate(minima_pos):
            fig.add_shape(
                type="line",
                x0=x_min, y0=0,
                x1=x_min, y1=0.1,
                line=dict(color="red", width=2, dash="dash")
            )
            fig.add_annotation(
                x=x_min, y=0.15,
                text=f"min {i+1}",
                showarrow=False,
                font=dict(size=10, color="red")
            )
            
            if x_min > 0:
                fig.add_shape(
                    type="line",
                    x0=-x_min, y0=0,
                    x1=-x_min, y1=0.1,
                    line=dict(color="red", width=2, dash="dash")
                )
                fig.add_annotation(
                    x=-x_min, y=0.15,
                    text=f"min {i+1}",
                    showarrow=False,
                    font=dict(size=10, color="red")
                )
        
        fig.update_layout(
            title=f"Дифракционная картина (щель {slit_width} мкм, λ={wavelength_diff} нм)",
            xaxis_title="Положение на экране x (см)",
            yaxis_title="Интенсивность I (отн. ед.)",
            height=500,
            showlegend=True,
            hovermode='x'
        )
        
        fig.update_xaxes(showgrid=True, gridwidth=1, gridcolor='LightGray')
        fig.update_yaxes(showgrid=True, gridwidth=1, gridcolor='LightGray')
        
        st.plotly_chart(fig, use_container_width=True)
        
        # Информация о дифракции
        st.info(f"""
        **Характеристики дифракции:**
        - Ширина центрального максимума: {2*L_diff*np.arcsin(wavelength_m/slit_width_m)*100:.2f} см
        - Положение первого минимума: ±{minima_pos[0] if minima_pos else 0:.2f} см
        - Угловая ширина центрального максимума: {2*np.degrees(np.arcsin(wavelength_m/slit_width_m)):.2f}°
        """)

# Добавляем теоретическую справку
st.markdown("---")
st.header("📚 Теоретическая справка")

with st.expander("Основные формулы оптики", expanded=False):
    col1, col2, col3 = st.columns(3)
    
    with col1:
        st.markdown("""
        ### Закон преломления
        **n₁·sin(θ₁) = n₂·sin(θ₂)**
        
        *Закон Снеллиуса*
        
        ### Показатель преломления
        **n = c/v**
        
        *c - скорость света в вакууме*
        *v - скорость света в среде*
        """)
    
    with col2:
        st.markdown("""
        ### Формула линзы
        **1/F = 1/d₀ + 1/d₁**
        
        ### Увеличение линзы
        **Γ = -d₁/d₀ = h₁/h₀**
        
        *F - фокусное расстояние*
        *d₀ - расстояние до предмета*
        *d₁ - расстояние до изображения*
        """)
    
    with col3:
        st.markdown("""
        ### Интерференция
        **Δd = k·λ** - максимум
        **Δd = (2k+1)λ/2** - минимум
        
        ### Дифракция
        **a·sin(θ) = k·λ** - минимум
        
        *a - ширина щели*
        *λ - длина волны*
        """)

# Footer
st.markdown("---")
st.markdown("""
    <div style='text-align: center; color: gray; padding: 1rem;'>
        <p>💡 Моделирование оптических явлений | Версия 1.0.0</p>
        <p>Используйте вкладки для выбора различных оптических явлений</p>
    </div>
""", unsafe_allow_html=True)