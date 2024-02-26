let exampleModal = document.querySelector("#exampleModal");
exampleModal.addEventListener("show.bs.modal", function (event) {
	let button = event.relatedTarget;
	let value = button.getAttribute("data-bs-whatever");

	let img_charters = exampleModal.querySelector("img.card-img-top");
	img_charters.setAttribute("src", "img/build/" + value);
});

function addOnWheel(elem, handler) {
    if (elem.addEventListener) {
        if ('onwheel' in document) {
            elem.addEventListener("wheel", handler);
        } else if ('onmousewheel' in document) {
            elem.addEventListener("mousewheel", handler);
        } else {
            elem.addEventListener("MozMousePixelScroll", handler);
        }
    } else {
        elem.attachEvent("onmousewheel", handler);
    }
}

function dragElement(elmnt) {
    let pos1 = 0, pos2 = 0, pos3 = 0, pos4 = 0;
    if (document.getElementById(elmnt.id + "header")) {
        document.getElementById(elmnt.id + "header").onmousedown = dragMouseDown;
    } else {
        elmnt.onmousedown = dragMouseDown;
    }

    function dragMouseDown(e) {
        e = e || window.event;
        e.preventDefault();
        pos3 = e.clientX;
        pos4 = e.clientY;
        document.onmouseup = closeDragElement;
        document.onmousemove = elementDrag;
    }

    function elementDrag(e) {
        e = e || window.event;
        e.preventDefault();
        pos1 = pos3 - e.clientX;
        pos2 = pos4 - e.clientY;
        pos3 = e.clientX;
        pos4 = e.clientY;
        elmnt.style.top = (elmnt.offsetTop - pos2) + "px";
        elmnt.style.left = (elmnt.offsetLeft - pos1) + "px";
    }

    function closeDragElement() {
        document.onmouseup = null;
        document.onmousemove = null;
    }
}

let scale = 1;
addOnWheel(exampleModal, function (e) {
    let delta = e.deltaY || e.detail || e.wheelDelta;
    if (delta > 0) scale += 0.05;
    else scale -= 0.05;
    exampleModal.style.transform = exampleModal.style.WebkitTransform = exampleModal.style.MsTransform = 'scale(' + scale + ')';
    e.preventDefault();
});
dragElement(exampleModal);
