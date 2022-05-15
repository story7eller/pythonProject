import matplotlib.pyplot as plt
with plt.xkcd(): # эфект рисования от руки
    plt.pie([70, 10, 10, 10], labels=('В коммкнтариях', 'В Ираке', 'В Сирии', 'В Авганистане'))
    plt.title('Гду ведутся самые ожесточенные бои?')
    plt.show()
              