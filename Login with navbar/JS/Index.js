function OpenWindowLogin(){
    document.getElementById("WindowNavbarButtonLogin").style.display="block"
}

function CloseWindowLogin(){
    document.getElementById("WindowNavbarButtonLogin").style.display="none"
}

function OpenWindowRegister(){
    document.getElementById("WindowNavbarButtonRegister").style.display="flex"
}

function CloseWindowRegister(){
    document.getElementById("WindowNavbarButtonRegister").style.display="none"
}


function login()
{
    let username = document.getElementById('Username').value
    let password = document.getElementById('Password').value
 
    if(username == "" && password =="1234")
    {
        window.location = ""
    }
    else{
        alert("Usuario y/o contraseña incorrecta. Vuelva a ingresar")
    }
}


