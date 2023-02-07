document.addEventListener("DOMContentLoaded", function(){
    
    const fadeIn = (el, timeout, display) => {
        el.style.opacity = 0;
        el.style.display = display || 'block';
        el.style.transition = `opacity ${timeout}ms`;
        setTimeout(() => {
            el.style.opacity = 1;
        }, 10);
        };
    const fadeOut = (el, timeout) => {
        el.style.opacity = 1;
        el.style.transition = `opacity ${timeout}ms`;
        el.style.opacity = 0;
        setTimeout(() => {
            el.style.display = 'none';
        }, timeout);
        };
    
    const search_input = document.getElementsByClassName("search-form__text")[0];
    const search_result = document.getElementsByClassName("ajax-search")[0];
    
    function show_search_res() {
        let search_value = search_input.value;
        if (search_value.length > 0) {
//             console.log(search_value);
            var inner_html = ''
            const request = new XMLHttpRequest();
            const url = "search/";
            const params = "sort_search=" + search_value;
            request.open("POST", url, true);
            request.setRequestHeader("Content-type", "application/x-www-form-urlencoded");
            request.setRequestHeader("x-csrf-token", "fetch");
            
            request.addEventListener("readystatechange", () => {
//             var SelectCity = document.getElementById("temp_city");
            if (request.readyState === 4 && request.status === 200) {
//                 console.log('Ответ сервера'+request.responseText);    
                var res = JSON.parse(request.response);
//                 console.log(res);
               for (var i=0;i<res.names.length;i+=1) {
//                    console.log(res.names[i]);
//                 SelectCity.innerHTML = '<label for="id_city">City:</label>'+request.responseText
                   inner_html = inner_html + '<li class="ajax-search__item"><a href="'+res.urls[i]+'" class="ajax-search__link" style="display: flex; align-items: center;"><img src="'+res.images[i]+'" style="width:50px; margin-right: 5px;"/>'+res.names[i]+'</a></li>'
               }
               search_result.innerHTML = inner_html;
               fadeIn(search_result, 200, 'block'); 
                }
            });
            request.send(params);
        } else {
            fadeOut(search_result,200);
        }
    }
    
//     console.log(search_input.value);
    search_input.oninput = show_search_res;
    //search_input.onclick = show_search_res;
        
    const alldoc = document.documentElement;
    const MobileMenu = document.getElementsByClassName("mobile_menu")[0];
    const MobileMenuUL = document.getElementsByClassName("mobile_menu_ul")[0];
    
    MobileMenu.addEventListener('click', e => {
        if (getComputedStyle(MobileMenuUL).display == 'none'){
            fadeIn(MobileMenuUL,200);
        }
    });
    
    alldoc.addEventListener('mouseup', e => {
        fadeOut(search_result,200);
        if (getComputedStyle(MobileMenuUL).display == 'block'){
            fadeOut(MobileMenuUL,200);
        }
    });
    
/***************** Thank's for Comment ************************************************************************************************************/
    const addCommentForm = document.forms.form_send_comment;
//     console.log(addCommentForm);
    const addCommentBlock = document.getElementsByClassName("add_comment_block")[0];
    if (addCommentForm) {
        addCommentForm.addEventListener('submit', sendFormValue);
    }
    function sendFormValue(event) {
        event.preventDefault();  
        const request = new XMLHttpRequest();
        const url = "send-comment/";
        const params = "from_name="+addCommentForm.from_name.value+"&from_email="+addCommentForm.from_email.value+"&message="+addCommentForm.message.value+"&sort="+addCommentForm.sort.value+"&veg_type="+addCommentForm.veg_type.value+"&veg_vids="+addCommentForm.veg_vids.value;
        request.open("POST", url, true);
        request.setRequestHeader("Content-type", "application/x-www-form-urlencoded");
        request.setRequestHeader("x-csrf-token", "fetch");
            
        request.addEventListener("readystatechange", () => {
            if (request.readyState === 4 && request.status === 200) {
                addCommentBlock.innerHTML = '<p>Спасибо за Ваш комментарий. После проверки он отобразится на сайте.</p>';
            }
        });
        request.send(params);
    }
    
/***************** Likes & Compare ************************************************************************************************************/
    var sort_name = document.querySelector('.sort_name');
    if (sort_name) { 
        sort_name = sort_name.innerText; 
    }
    var veg_type = document.querySelector('.veg_type');
    console.log(veg_type);
    if (veg_type) { 
        veg_type = veg_type.text; 
    }
        
    var likes_input = document.querySelector('.likes_input');
    if (likes_input) {
        likes_input.addEventListener('click', sendLikeValue);
    }
    function sendLikeValue(event) {
        event.preventDefault();
        const request = new XMLHttpRequest();
        const url = "vote/";
        const params ="veg_type="+veg_type+"&sort_name="+sort_name;
        console.log(params);
        request.open("POST", url, true);
        request.setRequestHeader("Content-type", "application/x-www-form-urlencoded");
        request.setRequestHeader("x-csrf-token", "fetch");
            
        request.addEventListener("readystatechange", () => {
            if (request.readyState === 4 && request.status === 200) {
                likes_input.style.display = 'none';
                document.getElementsByClassName("thank_like")[0].style.display = 'block';
            }
        });
        request.send(params);
    }
    
    var compare_input = document.querySelector('.compare_input');
    if (compare_input) {
        compare_input.addEventListener('click', sendCompareValue);
    }
    function sendCompareValue(event) {
        event.preventDefault();
        const request = new XMLHttpRequest();
        const url = "addcompare/";
        const params ="veg_type="+veg_type+"&sort_name="+sort_name;
        request.open("POST", url, true);
        request.setRequestHeader("Content-type", "application/x-www-form-urlencoded");
        request.setRequestHeader("x-csrf-token", "fetch");
            
        request.addEventListener("readystatechange", () => {
            if (request.readyState === 4 && request.status === 200) {
                compare_input.style.display = 'none';
                document.getElementsByClassName("thank_compare")[0].style.display = 'block';
            }
        });
        request.send(params);
    }
    
    
/***************** Go to TOP  ************************************************************************************************************/
    (function() {
        var goTopBtn = document.querySelector('.back_to_top');
        console.log(goTopBtn);
        var goTopBtn = document.querySelector('.back_to_top');
    
        window.addEventListener('scroll', trackScroll);
        goTopBtn.addEventListener('click', backToTop);
        
        function trackScroll() {
            var scrolled = window.pageYOffset;
            var coords = document.documentElement.clientHeight;

            if (scrolled > coords) {
            goTopBtn.classList.add('back_to_top-show');
            }
            if (scrolled < coords) {
            goTopBtn.classList.remove('back_to_top-show');
            }
        }
        
        function backToTop() {
            if (window.pageYOffset > 0) {
            window.scrollBy(0, -10);
            setTimeout(backToTop, 10);
            }
        }
    })();
});
