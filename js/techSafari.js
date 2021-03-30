function mission1(){
	var sm=document.getElementById("ms")
	var sm3=document.getElementById("ms2")
	var rd1=document.getElementById("readmore")
	var sm2=document.getElementById("vis")
	a=sm.innerHTML
	b=sm3.innerHTML
	sm.innerHTML=b
	sm3.innerHTML=a
}
function notify(){
	var sm1=document.getElementById("notify")
	var sm2=document.getElementById("notify2")
	var rd=document.getElementById("readmoreN")
	a=sm1.innerHTML;
	b=sm2.innerHTML;
	sm1.innerHTML=b
	sm2.innerHTML=a
}
function vission(){
	var sm1=document.getElementById("vis")
	var sm2=document.getElementById("vis2")
	var rd=document.getElementById("readmoreV")
	a=sm1.innerHTML;
	b=sm2.innerHTML;
	sm1.innerHTML=b
	sm2.innerHTML=a
}
function check(input) {
					if (input.value != document.getElementById('npass').value) {
						input.setCustomValidity('Password Must be Matching.');
					} else {
						// input is valid -- reset the error message
						input.setCustomValidity('');
					}
}