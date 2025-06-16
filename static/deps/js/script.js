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




    const burger = document.getElementById('burger');
    const menu = document.getElementById('menu');
    const menuLinks = document.querySelectorAll('.menu a');

    burger.addEventListener('click', () => {
        menu.classList.toggle('active');
    });

    // Закрытие меню при клике на ссылку
    menuLinks.forEach(link => {
        link.addEventListener('click', () => {
            menu.classList.remove('active');
        });
    });
