import streamlit as st
import numpy as np
import pandas as pd
import plotly.graph_objects as go
from plotly.subplots import make_subplots

# Настройка страницы
st.set_page_config(
    page_title="Закон Ома - Моделирование",
    page_icon="⚡",
    layout="wide"
)

# Навигационная цепочка
st.markdown("""
    <div style='background: #f0f2f6; padding: 0.5rem 1rem; border-radius: 5px; margin-bottom: 1rem;'>
        <a href="/" target="_self" style='text-decoration: none; color: #667eea;'>Главная</a> / 
        <span style='color: #764ba2;'>Закон Ома</span>
    </div>
""", unsafe_allow_html=True)

# Заголовок с описанием
st.title("⚡ Закон Ома")
st.markdown("""
    <div style='background: linear-gradient(90deg, #667eea20 0%, #764ba220 100%); 
                padding: 1.5rem; border-radius: 10px; margin-bottom: 2rem;'>
        <h3>📝 Описание модели</h3>
        <p style='font-size: 1.1rem;'>
            Закон Ома устанавливает связь между напряжением (U), силой тока (I) и сопротивлением (R) 
            в электрической цепи. Это фундаментальный закон электротехники, который гласит: 
            <strong>сила тока в участке цепи прямо пропорциональна напряжению и обратно пропорциональна сопротивлению</strong>.
        </p>
        <p style='font-size: 1.2rem; text-align: center; background: linear-gradient(90deg, #667eea20 0%, #764ba220 100%); padding: 1rem; border-radius: 5px;'>
            <strong>I = U / R</strong>
        </p>
    </div>
""", unsafe_allow_html=True)

# Боковая панель с параметрами
with st.sidebar:
    st.title("⚙️ Параметры")
    st.markdown("---")
    
    # Выбор режима моделирования
    mode = st.radio(
        "Режим моделирования:",
        ["Фиксированное сопротивление", "Фиксированное напряжение", "3D визуализация"],
        help="Выберите, какой параметр будет постоянным"
    )
    
    st.markdown("---")
    
    # Дополнительные настройки
    st.subheader("🎨 Настройки отображения")
    show_grid = st.checkbox("Показать сетку", value=True)
    show_legend = st.checkbox("Показать легенду", value=True)
    
    # Цветовая схема
    color_scheme = st.selectbox(
        "Цветовая схема",
        ["Красный", "Синий", "Зеленый", "Фиолетовый"]
    )
    
    color_map = {
        "Красный": "#ff4b4b",
        "Синий": "#4b4bff",
        "Зеленый": "#4bff4b",
        "Фиолетовый": "#9b4bff"
    }
    
    st.markdown("---")
    
    # Кнопка сброса
    if st.button("🔄 Сбросить параметры"):
        st.session_state.clear()
        st.rerun()

# Основной контент
tab1, tab2, tab3 = st.tabs(["📊 Моделирование", "📚 Теория", "📝 Примеры"])

with tab1:
    # Создаем две колонки для управления и визуализации
    col1, col2 = st.columns([1, 2])
    
    with col1:
        st.subheader("🔧 Управление параметрами")
        
        if mode == "Фиксированное сопротивление":
            R = st.slider("Сопротивление R (Ом)", 1.0, 100.0, 50.0, 1.0,
                         help="Постоянное сопротивление цепи")
            V_range = st.slider("Диапазон напряжения U (В)", 0.0, 100.0, (0.0, 100.0), 5.0)
            V_values = np.linspace(V_range[0], V_range[1], 100)
            I_values = V_values / R
            
            # Выбор точки на графике
            selected_U = st.slider("Выберите напряжение:", V_range[0], V_range[1], V_range[1]/2, 0.1)
            selected_I = selected_U / R
            
            st.info(f"📊 При R = {R} Ом, I = U / {R}")
            
        elif mode == "Фиксированное напряжение":
            V = st.slider("Напряжение U (В)", 1.0, 100.0, 50.0, 1.0,
                         help="Постоянное напряжение цепи")
            R_range = st.slider("Диапазон сопротивления R (Ом)", 0.1, 100.0, (0.1, 100.0), 5.0)
            R_values = np.linspace(R_range[0], R_range[1], 100)
            I_values = V / R_values
            
            # Выбор точки на графике
            selected_R = st.slider("Выберите сопротивление:", R_range[0], R_range[1], R_range[1]/2, 0.1)
            selected_I = V / selected_R
            
            st.info(f"📊 При U = {V} В, I = {V} / R")
            
        else:  # 3D визуализация
            st.markdown("""
            <div style='background: linear-gradient(90deg, #667eea20 0%, #764ba220 100%); padding: 1rem; border-radius: 5px; margin-bottom: 1rem;'>
                <h4 style='margin:0;'>🎯 Интерактивная 3D поверхность</h4>
                <p style='margin:0; font-size:0.9rem;'>Вращайте график для лучшего обзора</p>
            </div>
            """, unsafe_allow_html=True)
            
            V_3d = st.slider("Напряжение U (В)", 0.0, 100.0, 50.0, 1.0)
            R_3d = st.slider("Сопротивление R (Ом)", 0.1, 100.0, 25.0, 0.1)
            I_3d = V_3d / R_3d
            
            # Метрики
            col_m1, col_m2, col_m3 = st.columns(3)
            with col_m1:
                st.metric("Напряжение U", f"{V_3d} В")
            with col_m2:
                st.metric("Сопротивление R", f"{R_3d} Ом")
            with col_m3:
                st.metric("Ток I", f"{I_3d:.3f} А")
    
    with col2:
        st.subheader("📈 Визуализация")
        
        if mode == "Фиксированное сопротивление":
            fig = go.Figure()
            
            # Основная линия
            fig.add_trace(go.Scatter(
                x=V_values, y=I_values,
                mode='lines',
                name=f'I = U / {R}',
                line=dict(color=color_map[color_scheme], width=3),
                hovertemplate='U = %{x:.1f} В<br>I = %{y:.3f} А<extra></extra>'
            ))
            
            # Выбранная точка
            fig.add_trace(go.Scatter(
                x=[selected_U], y=[selected_I],
                mode='markers',
                marker=dict(size=15, color='red', symbol='circle'),
                name=f'U={selected_U:.1f}В, I={selected_I:.3f}А',
                hovertemplate='U = %{x:.1f} В<br>I = %{y:.3f} А<extra>Выбранная точка</extra>'
            ))
            
            fig.update_layout(
                title="Вольт-амперная характеристика",
                xaxis_title="Напряжение U (В)",
                yaxis_title="Ток I (А)",
                hovermode='x',
                height=500,
                showlegend=show_legend
            )
            
            if show_grid:
                fig.update_xaxes(showgrid=True, gridwidth=1, gridcolor='LightGray')
                fig.update_yaxes(showgrid=True, gridwidth=1, gridcolor='LightGray')
            
            fig.update_xaxes(range=[V_range[0], V_range[1]])
            fig.update_yaxes(range=[0, max(I_values) * 1.1])
            
        elif mode == "Фиксированное напряжение":
            fig = go.Figure()
            
            # Основная линия
            fig.add_trace(go.Scatter(
                x=R_values, y=I_values,
                mode='lines',
                name=f'I = {V} / R',
                line=dict(color=color_map[color_scheme], width=3),
                hovertemplate='R = %{x:.1f} Ом<br>I = %{y:.3f} А<extra></extra>'
            ))
            
            # Выбранная точка
            fig.add_trace(go.Scatter(
                x=[selected_R], y=[selected_I],
                mode='markers',
                marker=dict(size=15, color='red', symbol='circle'),
                name=f'R={selected_R:.1f}Ом, I={selected_I:.3f}А',
                hovertemplate='R = %{x:.1f} Ом<br>I = %{y:.3f} А<extra>Выбранная точка</extra>'
            ))
            
            fig.update_layout(
                title="Зависимость тока от сопротивления",
                xaxis_title="Сопротивление R (Ом)",
                yaxis_title="Ток I (А)",
                hovermode='x',
                height=500,
                showlegend=show_legend
            )
            
            if show_grid:
                fig.update_xaxes(showgrid=True, gridwidth=1, gridcolor='LightGray')
                fig.update_yaxes(showgrid=True, gridwidth=1, gridcolor='LightGray')
            
            fig.update_xaxes(range=[R_range[0], R_range[1]])
            fig.update_yaxes(range=[0, max(I_values) * 1.1])
            
        else:  # 3D визуализация
            # Создаем данные для поверхности
            R_surface = np.linspace(0.1, 100, 50)
            V_surface = np.linspace(0, 100, 50)
            R_grid, V_grid = np.meshgrid(R_surface, V_surface)
            I_grid = V_grid / R_grid
            
            fig = go.Figure(data=[
                go.Surface(
                    x=R_grid, y=V_grid, z=I_grid,
                    colorscale='Viridis',
                    opacity=0.9,
                    colorbar=dict(title="Ток I (A)"),
                    hovertemplate='R: %{x:.1f} Ом<br>U: %{y:.1f} В<br>I: %{z:.3f} А<extra></extra>'
                ),
                go.Scatter3d(
                    x=[R_3d], y=[V_3d], z=[I_3d],
                    mode='markers',
                    marker=dict(size=10, color='red'),
                    name='Текущая точка',
                    hovertemplate='R: %{x:.1f} Ом<br>U: %{y:.1f} В<br>I: %{z:.3f} А<extra>Текущие параметры</extra>'
                )
            ])
            
            fig.update_layout(
                title="3D визуализация закона Ома",
                scene=dict(
                    xaxis_title="Сопротивление R (Ом)",
                    yaxis_title="Напряжение U (В)",
                    zaxis_title="Ток I (А)",
                    camera=dict(eye=dict(x=1.5, y=1.5, z=1.5))
                ),
                height=600,
                showlegend=show_legend
            )
        
        st.plotly_chart(fig, use_container_width=True)
        
        # Дополнительная информация
        if mode != "3D визуализация":
            st.info(f"""
            **Текущие значения:**
            - Напряжение: {selected_U if mode == 'Фиксированное сопротивление' else V} В
            - Сопротивление: {R if mode == 'Фиксированное сопротивление' else selected_R} Ом
            - Ток: {selected_I:.3f} А
            - Мощность: {(selected_U if mode == 'Фиксированное сопротивление' else V) * selected_I:.2f} Вт
            """)

with tab2:
    st.header("📚 Теоретические основы")
    
    col1, col2 = st.columns(2)
    
    with col1:
        st.markdown("""
        ### Закон Ома для участка цепи
        
        **Формулировка:**
        > Сила тока в участке цепи прямо пропорциональна напряжению на концах этого участка и обратно пропорциональна его сопротивлению.
        
        **Математическая запись:**
        ```
        I = U / R
        ```
        
        **Где:**
        - **I** — сила тока (Ампер, А)
        - **U** — напряжение (Вольт, В)
        - **R** — сопротивление (Ом, Ω)
        
        ### Единицы измерения
        - 1 Ампер = 1 Вольт / 1 Ом
        - 1 Вольт = 1 Ампер × 1 Ом
        - 1 Ом = 1 Вольт / 1 Ампер
        """)
        
    with col2:
        st.markdown("""
        ### Мощность в электрической цепи
        
        **Формула мощности:**
        ```
        P = U × I = I² × R = U² / R
        ```
        
        **Где:**
        - **P** — мощность (Ватт, Вт)
        
        ### Историческая справка
        Закон был открыт немецким физиком **Георгом Омом** в 1827 году. 
        Его работа "Die galvanische Kette, mathematisch bearbeitet" 
        (Гальваническая цепь, обработанная математически) заложила основы 
        теории электрических цепей.
        
        ### Практическое применение
        - Расчет электрических цепей
        - Проектирование электронных устройств
        - Анализ энергопотребления
        - Подбор компонентов
        """)

with tab3:
    st.header("📝 Примеры расчетов")
    
    example_type = st.selectbox(
        "Выберите тип примера:",
        ["Расчет тока", "Расчет напряжения", "Расчет сопротивления", "Расчет мощности"]
    )
    
    if example_type == "Расчет тока":
        st.markdown("""
        ### Пример 1: Расчет силы тока
        
        **Условие:**  
        Электрическая цепь имеет напряжение 12 В и сопротивление 24 Ом. 
        Найдите силу тока в цепи.
        
        **Решение:**
        ```
        I = U / R = 12 В / 24 Ом = 0.5 А
        ```
        
        **Ответ:** Сила тока составляет 0.5 Ампер.
        """)
        
        # Интерактивный пример
        st.subheader("🔄 Попробуйте сами")
        ex_U = st.number_input("Напряжение U (В)", value=12.0, step=1.0)
        ex_R = st.number_input("Сопротивление R (Ом)", value=24.0, step=1.0, min_value=0.1)
        ex_I = ex_U / ex_R
        st.success(f"Ток I = {ex_I:.3f} А")
        
    elif example_type == "Расчет напряжения":
        st.markdown("""
        ### Пример 2: Расчет напряжения
        
        **Условие:**  
        Через резистор сопротивлением 10 Ом протекает ток 2 А. 
        Какое напряжение приложено к резистору?
        
        **Решение:**
        ```
        U = I × R = 2 А × 10 Ом = 20 В
        ```
        
        **Ответ:** Напряжение составляет 20 Вольт.
        """)
        
        # Интерактивный пример
        st.subheader("🔄 Попробуйте сами")
        ex_I = st.number_input("Ток I (А)", value=2.0, step=0.1)
        ex_R = st.number_input("Сопротивление R (Ом)", value=10.0, step=1.0, min_value=0.1)
        ex_U = ex_I * ex_R
        st.success(f"Напряжение U = {ex_U:.2f} В")
        
    elif example_type == "Расчет сопротивления":
        st.markdown("""
        ### Пример 3: Расчет сопротивления
        
        **Условие:**  
        При напряжении 220 В через прибор протекает ток 5 А. 
        Каково сопротивление прибора?
        
        **Решение:**
        ```
        R = U / I = 220 В / 5 А = 44 Ом
        ```
        
        **Ответ:** Сопротивление прибора равно 44 Ом.
        """)
        
        # Интерактивный пример
        st.subheader("🔄 Попробуйте сами")
        ex_U = st.number_input("Напряжение U (В)", value=220.0, step=10.0)
        ex_I = st.number_input("Ток I (А)", value=5.0, step=0.1, min_value=0.1)
        ex_R = ex_U / ex_I
        st.success(f"Сопротивление R = {ex_R:.2f} Ом")
        
    else:  # Расчет мощности
        st.markdown("""
        ### Пример 4: Расчет мощности
        
        **Условие:**  
        Электрический чайник работает от сети 220 В и потребляет ток 10 А. 
        Какова мощность чайника?
        
        **Решение:**
        ```
        P = U × I = 220 В × 10 А = 2200 Вт = 2.2 кВт
        ```
        
        **Ответ:** Мощность чайника составляет 2.2 кВт.
        """)
        
        # Интерактивный пример
        st.subheader("🔄 Попробуйте сами")
        ex_U = st.number_input("Напряжение U (В)", value=220.0, step=10.0)
        ex_I = st.number_input("Ток I (А)", value=10.0, step=0.5, min_value=0.1)
        ex_P = ex_U * ex_I
        st.success(f"Мощность P = {ex_P:.2f} Вт = {ex_P/1000:.2f} кВт")

# Footer
st.markdown("---")
st.markdown("""
    <div style='text-align: center; color: gray; padding: 1rem;'>
        <p>⚡ Моделирование закона Ома | Версия 1.0.0</p>
        <p>Используйте боковую панель для настройки параметров</p>
    </div>
""", unsafe_allow_html=True)