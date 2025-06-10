document.addEventListener('DOMContentLoaded', function () {
    const flash = document.getElementById('flash-message');
    if (flash) {
        setTimeout(() => {
            flash.classList.add('hide');
        }, 3000);
    }
});
