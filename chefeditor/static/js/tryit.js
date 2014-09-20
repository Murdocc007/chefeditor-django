
function onTryItClick() {   
    var content="";
    if (document.getElementById("css").value) {
        content = content+"<style  type='text/css'>"+document.getElementById("css").value+"</style>";   
    }
   /*if (document.getElementById("javscript").value) {
        content = content+"<script  type='text/javscript'>"+document.getElementById("javscript").value+"</sc"+"ript>";
    }*/
if (document.getElementById("html").value) {
        content = content+"<html>"+document.getElementById("html").value+"</html>"; 
    }
        var iframe = document.getElementById("myiframeid");
        
        var frameDoc = iframe.document;
        if (iframe.contentWindow)
            frameDoc = iframe.contentWindow.document;

        frameDoc.open();
        frameDoc.writeln(content);
        frameDoc.close();
        var script=iframe.contentWindow.document.createElement("script");
        script.type='text/javascript';
        script.innerHTML=document.getElementById("javascript").value;
        iframe.contentWindow.document.body.appendChild(script);
    }