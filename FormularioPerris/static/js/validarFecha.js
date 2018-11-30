function checkFecha() {
	
	var fecha = document.getElementById("fechaNac").value;
	fecha = fecha.replace('-','');
	fecha = new Date(fecha.slice(5,9),fecha.slice(2,4),fecha.slice(0,2));
	fecha=fecha.getTime();
	var diff_ms = Date.now()-fecha;
    if(diff_ms < 565442310233) { fechaNac.setCustomValidity("Menor de edad"); return false; } 
    fechaNac.setCustomValidity();
}