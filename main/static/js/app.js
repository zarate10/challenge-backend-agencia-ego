let data = window.data 
const $ = (element) => document.querySelector(element);

document.addEventListener('DOMContentLoaded', () => {
    
    // Menú toggle
    let btnMenu = document.getElementById('btn-toggle-menu')
    let menuOpen = false 
    btnMenu.addEventListener('click', () => {
      
        menuOpen = !menuOpen

        if (menuOpen) { 
            $('#menu-txt').innerHTML = 'Cerrar';
            $('#icon-menu').className = "fa-solid fa-x";
            document.body.style.overflow = 'hidden';
            setTimeout(() => {
                $('.menu-bg').style.display = 'flex'
                $('.menu-bg').style.animation = 'showToggleMenu 0.5s';
                $('.menu-bg').style.opacity = 1
            }, 200)

        } else { 
            $('#menu-txt').innerHTML = 'Menú';
            $('#icon-menu').className = 'fa-solid fa-bars';
            document.body.style.overflowY = 'scroll';
            setTimeout(() => {
                $('.menu-bg').style.animation = 'hiddenToggleMenu 0.3s';
                $('.menu-bg').style.opacity = 0
                setTimeout(() => {            
                    $('.menu-bg').style.display = 'none'
                }, 100)
            }, 200)
        }
    })

});