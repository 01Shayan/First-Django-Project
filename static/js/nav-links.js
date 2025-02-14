const navLinks = document.querySelector('.nav-links')
function onToggleMenu(e){
    e.name = e.name === 'menu' ? 'close' : 'menu'
    // navLinks.classList.toggle('md:invisible')
    // navLinks.classList.toggle('hidden')
    navLinks.classList.toggle('top-[70px]')
}