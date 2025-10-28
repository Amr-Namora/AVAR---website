// Get the modal

var modal = document.getElementById('myModal');

// Get the image and insert it inside the modal
var img = document.getElementById('myImage');
var modalContent = document.querySelector('.modal-content');

// Get the <span> element that closes the modal
var closeBtn = document.querySelector('.close-btn');

// When the user clicks the image, open the modal
img.onclick = function() {
    modal.style.display = 'block';
}

// When the user clicks on <span> (x), close the modal
closeBtn.onclick = function() {
    modal.style.display = 'none';
}

// When the user clicks anywhere outside of the modal, close it
window.onclick = function(event) {
    if (event.target == modal) {
        modal.style.display = 'none';
    }
}



var modal2 = document.getElementById('myModal2');

// Get the image and insert it inside the modal
var img2 = document.getElementById('mySearch');
var modalContent2 = document.querySelector('.modal-content2');

// Get the <span> element that closes the modal
var closeBtn2 = document.querySelector('.close-btn2');

// When the user clicks the image, open the modal
img2.onclick = function() {
    modal2.style.display = 'block';
}

// When the user clicks on <span> (x), close the modal
closeBtn2.onclick = function() {
    modal2.style.display = 'none';
}

// When the user clicks anywhere outside of the modal, close it
window.onclick = function(event1) {
    if (event1.target == modal2) {
        modal2.style.display = 'none';
    }
}




function calculateWidthById(id) {
    const element = document.getElementById(id);
    if (!element) {
        return;
    }
    const width = element.offsetWidth;
    return width;
}

let scrollContainer = document.querySelector(".gallery");

let backBtn = document.getElementById("prev");

let nextBtn = document.getElementById("next");

scrollContainer.addEventListener("wheel", (evt) => {
    evt.preventDefault();
    scrollContainer.scrollLeft += evt.deltay;
    scrollContainer.style.scrollBehavior = "auto";
});


nextBtn.addEventListener("click", () => {
    scrollContainer.style.scrollBehavior = "smooth";
    scrollContainer.scrollLeft += calculateWidthById('im');
});


backBtn.addEventListener("click", () => {
    scrollContainer.style.scrollBehavior = "smooth";
    scrollContainer.scrollLeft -= calculateWidthById('im');
});

document.getElementById('love-img').addEventListener('click', function () {
    this.classList.toggle('active');
    document.getElementById('favoret').textContent = this.classList.contains('active') ? 'تمت الاضافة' : 'أضف للمفضلة';
});

document.getElementById('city').addEventListener('change', function () {
    const mainValue = this.value;
    const dependentSelect = document.getElementById('Madena');

    let options = [];
    if (mainValue === 'دمشق') {
        options = ['الشام', 'الحميدية', 'المرجة', 'المزة', 'كفرسوسة'];
    } else if (mainValue === 'ريف دمشق') {
        options = ['دوما', 'حرستا', 'جرمانا', 'صحنايا', 'قطنا'];
    } else if (mainValue === 'حلب') {
        options = ['القدود الحلبية', 'الجامع الأموي', 'قلعة حلب', 'سوق المدينة', 'العرقوب'];
    } else if (mainValue === 'حمص') {
        options = ['تلبيسة', 'الرستن', 'المخور', 'كفرلاها', 'الزعفرانة'];
    } else if (mainValue === 'حماة') {
        options = ['مصياف', 'سلحب', 'محردة', 'صوران', 'كرناز'];
    } else if (mainValue === 'اللاذقية') {
        options = ['جبلة', 'القرداحة', 'الحفة', 'رأس البسيط', 'كسب'];
    } else if (mainValue === 'طرطوس') {
        options = ['بانياس', 'القدموس', 'الدريكيش', 'صافيتا', 'الشيخ بدر'];
    } else if (mainValue === 'إدلب') {
        options = ['اريحا', 'جسر الشغور', 'معرة النعمان', 'كفرنبل', 'سرمين'];
    } else if (mainValue === 'السويداء') {
        options = ['شهبا', 'القريا', 'سلخد', 'أم ضبيب', 'عرى'];
    } else if (mainValue === 'درعا') {
        options = ['نوى', 'جاسم', 'طفس', 'داعل', 'انخل'];
    } else if (mainValue === 'دير الزور') {
        options = ['البوكمال', 'الميادين', 'الصور', 'الكسرة', 'التبني'];
    } else if (mainValue === 'الحسكة') {
        options = ['رأس العين', 'القامشلي', 'الدرباسية', 'عامودا', 'المالكية'];
    } else if (mainValue === 'الرقة') {
        options = ['تل أبيض', 'سلوك', 'عين عروس', 'خربة الرز', 'الجزيرة'];
    } else if (mainValue === 'القنيطرة') {
        options = ['جباتا الخشب', 'خان أرنبة', 'القحطانية', 'بئر عجم', 'جباتا'];
    }
    dependentSelect.innerHTML = options.map(option => `<option value="${option}">${option}</option>`).join('');
});
