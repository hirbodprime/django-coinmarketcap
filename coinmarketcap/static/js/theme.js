$(document).ready(function () {
        let cookieTheme = localStorage.getItem("theme");
        console.log(cookieTheme);
        if (cookieTheme){
            meta_choice = document.getElementsByTagName("meta")[3].content = cookieTheme;
            console.log(meta_choice);
            if(cookieTheme == 'light'){
                $('#light').prop("selected",true)
            }else if (cookieTheme == 'dark'){
                $('#dark').prop("selected",true)
            }
        }
        $('#theme').change(function(){
        
            const theme = document.getElementById("theme").value;
            meta_choice = document.getElementsByTagName("meta")[3].content = theme;
            localStorage.setItem("theme",meta_choice);
            if(theme == 'light'){
                $('#light').prop("selected",true)
            }else if (theme == 'dark'){
                $('#dark').prop("selected",true)
            }
    })
})