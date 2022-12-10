window.addEventListener('load', function () {
    let menuItemOptions = document.getElementsByClassName('menu-item-option');
    let menuItemTitles = document.getElementsByClassName('menu-item-title');
    for (let i = 0; i < menuItemOptions.length; i++) {
        menuItemOptions[i].addEventListener(
            'click',
            function (event) {
                event.preventDefault();
                for (let j = 0; j < menuItemOptions.length; j++) {
                    menuItemOptions[j].classList.remove('active');
                }
                menuItemOptions[i].classList.add('active');
            },
            false
        );
    }
    for (let i = 0; i < menuItemTitles.length; i++) {
        menuItemTitles[i].addEventListener(
            'click',
            function (event) {
                event.preventDefault();
                for (let j = 0; j < menuItemTitles.length; j++) {
                    menuItemTitles[j].classList.remove('active');
                }
                menuItemTitles[i].classList.add('active');
            },
            false
        );
    }
});