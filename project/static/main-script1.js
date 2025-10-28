const middleBar = document.getElementById('mid-options');
middleBar.addEventListener('click', function(event) {
    const target = event.target;
    if (target.tagName === 'LI') {
        // التحقق إذا كان العنصر مضغوطًا بالفعل
        if (target.style.backgroundColor === 'aqua') {
            target.style.backgroundColor = '';
            target.style.color = '';
        } else {
            const listItems = middleBar.querySelectorAll('a');
            listItems.forEach(li => {
                a.style.backgroundColor = ''; // إعادة لون الخلفية لجميع العناصر
                a.style.color = ''; // إعادة لون النص
            });
            target.style.backgroundColor = 'aqua'; // تغيير لون الخلفية
            target.style.color = 'black'; // تغيير لون النص
        }
    }
});

