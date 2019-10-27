function toPage(url, par){
  //par = _self
  window.open(url, par);
}


function valid(form) {
	const email = form.email.value;
	const password = form.password.value;
	var text = ""
	// email validate
	var re = /^(([^<>()\[\]\\.,;:\s@"]+(\.[^<>()\[\]\\.,;:\s@"]+)*)|(".+"))@((\[[0-9]{1,3}\.[0-9]{1,3}\.[0-9]{1,3}\.[0-9]{1,3}\])|(([a-zA-Z\-0-9]+\.)+[a-zA-Z]{2,}))$/;
    var result = re.test(String(email).toLowerCase());
    if (result) {
    	text += "correct email!\n";
      label_password.style.color = "black";
  	} else {
	    label_email.style.color = "red";
	    return false;
  	}
  	// password validate
  	if (password == "lol123"){
  		text += "corret_password";
  	}
  	else {
  		label_password.style.color = 'red';
  		return false
  	}
  	alert(text);
    toPage("MyCabinet_page.html")
  	return true;
}


function Red(id) {
	var element = document.getElementById(id);
	element.style.color = "red";
}


function to_black_color(element){
	element.style.color = 'black';
}
