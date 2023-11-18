export function validateFullName(name){
    let flag = true;
    const fullNameRegex = /^[a-zA-Z ]+$/;
    if (
        name === '' || 
        name == null ||
        fullNameRegex.test(name) == false
    ){
        flag = false;
    }
    return flag;
}

export function validatePhoneNumber(number) {
    let flag = true;
    const phoneRegex = /^\d{10}$/;
    if (
        number === '' ||
        number == null ||
        phoneRegex.test(number) == false
    ){
        flag = false;
    }
    return flag;
}

export function validateEmail(email) {
    let flag = true;
    const emailRegex = /^\w+([\.-]?\w+)*@\w+([\.-]?\w+)*(\.\w{2,3})+$/;
    if (
        email === '' ||
        email == null ||
        emailRegex.test(email) == false
    ){
        flag = false;
    }
    return flag;
}

export function validateUrl(url){
    let flag = true;
    const urlRegex = 
    /[-a-zA-Z0-9@:%_\+.~#?&//=]{2,256}\.[a-z]{2,4}\b(\/[-a-zA-Z0-9@:%_\+.~#?&//=]*)?/gi;
    if (
        url === '' ||
        url == null ||
        urlRegex.test(url) == false
    ){
        flag = false;
    }
    return flag;
}

export function validateSummary(summary){
    let flag = true;
    if (summary.length > 500){
        flag = false;
    }
    return flag;
}

export function validateInput(input){
    let flag = true;
    if (input === '' || input == null){
        flag = false;
    }
    return flag;
}