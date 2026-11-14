function getCookie(name) {

    const cookies = document.cookie.split(';');

    for (let cookie of cookies) {

        cookie = cookie.trim();

        if (cookie.startsWith(name + '=')) {
            return cookie.substring(name.length + 1);
        }
    }

    return null;
}

function testCookies() {

    const unprotected = getCookie('unprotected_cookie');

    const protectedCookie = getCookie('protected_cookie');

    const unprotectedResult = document.getElementById('unprotected');

    const protectedResult = document.getElementById('protected');

    if (unprotected !== null) {

        unprotectedResult.innerHTML =
            'EXPOSED: ' + unprotected;

        unprotectedResult.className = 'danger-text';

    } else {

        unprotectedResult.innerHTML =
            'Not Found';

    }

    if (protectedCookie === null) {

        protectedResult.innerHTML =
            'PROTECTED: JavaScript cannot access this cookie';

        protectedResult.className = 'success';

    } else {

        protectedResult.innerHTML =
            'EXPOSED: ' + protectedCookie;

    }
}

testCookies();