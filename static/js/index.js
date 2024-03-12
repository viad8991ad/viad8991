var cards = document.querySelectorAll(".card-header");
cards.forEach(function(card) {
    card.addEventListener('click', function() {
        var expand = document.getElementById(card.id).getElementsByClassName("material-symbols-outlined")[0];
        var elem = document.getElementById("collapse_" + card.id);

		if(elem.classList.contains('show')) {
		    elem.classList.remove("show");
		    expand.textContent = "expand_more";
		} else {
		    expand.textContent = "expand_less";
		    elem.classList.add("show");
		}
	});
});
