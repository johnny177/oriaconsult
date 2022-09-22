function form_function() {
    if(!document.querySelector("#name").dataset.value) {
        alert("Please put your name.");
        return false;
    }
    if(!document.querySelector("#contact").dataset.value) {
        alert("Please put your phone number.");
        return false;
    }
    /* if(document.querySelector("#one-way").checked) {
        if(!document.querySelector("#depart_date").value) {
            alert("Please select departure date.");
            return false;
        }
    }
    if(document.querySelector("#round-trip").checked) {
        if(!document.querySelector("#depart_date").value) {
            alert("Please select departure date.");
            return false;
        }
        if(!document.querySelector("#return_date").value) {
            alert("Please select return date.");
            return false;
        } 
    }*/
}