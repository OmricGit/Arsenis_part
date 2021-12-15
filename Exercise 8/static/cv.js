function ChangeHeaderOnLoad(){
    document.getElementById("Title").innerHTML="Omri Canaan CV";
}
function thankyou() {
    document.getElementById("Button").innerHTML = "Thank you for visiting";
}
function Namevalidation() {
    var check = 0;
        var inpObj = document.getElementById(x);
        if (!inpObj.checkValidity()) {
            check = check +1 ;
            inpObjBAD = document.getElementById(x);


