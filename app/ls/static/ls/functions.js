var WidgetTitle = document.getElementsByClassName("widget_title");

function showTitle() {
//     console.log(document.getElementsByClassName("vege_img")[0])
    WidgetTitle[0].style.display = "block";
}
function closeTitle() {
    WidgetTitle[0].style.display = "none";
}

function showMobileMenu() {
    var MobileMenuUL = document.getElementsByClassName("mobile_menu_ul")[0];
    MobileMenuUL.style.display = "block";
//     console.log(MobileMenuUL)
}

function delFromCompare(cl,veg,name) {
    var del_input = document.getElementsByClassName(cl)[0].parentElement;
    const request = new XMLHttpRequest();
    const url = "/delcompare/";
    const params = "veg_type=" + veg+"&name="+name;
    request.open("POST", url, true);
    request.setRequestHeader("Content-type", "application/x-www-form-urlencoded");
    request.setRequestHeader("x-csrf-token", "fetch");

    request.addEventListener("readystatechange", () => {
        if (request.readyState === 4 && request.status === 200) {
            del_input.style.display = "none";
        }
    });
    request.send(params);
}
