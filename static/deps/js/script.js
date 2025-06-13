document.querySelectorAll('.faq-question').forEach(button => {
    button.addEventListener('click', () => {
        const answer = button.nextElementSibling;

        // Закрываем другие открытые элементы
        document.querySelectorAll('.faq-answer').forEach(a => {
            if (a !== answer) {
                a.style.display = 'none';
            }
        });

        // Переключаем видимость текущего ответа
        answer.style.display = answer.style.display === 'block' ? 'none' : 'block';
    });
});