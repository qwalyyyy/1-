import matplotlib.pyplot as plt

# Данные для столбчатого графика
categories = ['Январь', 'Февраль', 'Март', 'Апрель']
values = [40, 55, 70, 85]

# Данные для круговой диаграммы
labels = ['Продукт A', 'Продукт B', 'Продукт C', 'Продукт D']
sizes = [15, 30, 45, 10]

# Данные для линейного графика
x = [1, 2, 3, 4, 5]
y = [10, 20, 25, 30, 35]

# Создание подграфиков
fig, axs = plt.subplots(2, 2, figsize=(10, 8))

# Столбчатый график
axs[0, 0].bar(categories, values, color='skyblue')
axs[0, 0].set_xlabel('Месяцы')
axs[0, 0].set_ylabel('Значения')
axs[0, 0].set_title('Продажи по месяцам')

# Круговая диаграмма
axs[0, 1].pie(sizes, labels=labels, autopct='%1.1f%%', startangle=90)
axs[0, 1].set_title('Распределение продаж по продуктам')

# Линейный график
axs[1, 0].plot(x, y, marker='o', linestyle='-', color='green')
axs[1, 0].set_xlabel('Время')
axs[1, 0].set_ylabel('Значение')
axs[1, 0].set_title('Линейный график изменений')

# Убираем пустой подграфик
fig.delaxes(axs[1, 1])

# Настройка общего оформления
plt.tight_layout()
plt.show()
