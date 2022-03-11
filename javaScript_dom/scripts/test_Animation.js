function positionMessage() {
    if (!document.getElementById) return false;
    if (!document.getElementById("message")) return false;
    var elem = document.getElementById("message");
    elem.style.position = "absolute";
    elem.style.left = "50px";
    elem.style.top = "100px";
    //用 setTimeout 函数让5秒后执行 moveMessage 函数 
    //movement = setTimeout("mevoMessage()", 3000);
    
}

function addLoadEvent(func) {
    var oldonload = window.onload;
    if(typeof window.onload !="function"){
        window.onload = func;
    }else{
        window.onload = function(){
            oldonload();
            func();
        }
    }
}

function moveMessage(){
    if (!document.getElementById) return false;
    if (!document.getElementById("message")) return false;
    var elem = document.getElementById("message");
    elem.style.left = "200px";
}

addLoadEvent(positionMessage);
addLoadEvent(moveMessage);