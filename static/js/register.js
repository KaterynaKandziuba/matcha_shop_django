$(document).ready(function () {
    let loginCheck = false;
    let pwdCheck = false;
    let pwdRepeatCheck = false;
    let emailCheck = false;

    $('#login').blur(function () {
        let loginVal = $('#login').val();
        let loginR = /^[a-zA-z]+[a-zA-z0-9_]{5,15}$/;
        if (loginR.test(loginVal)) {
            $.ajax({
                url: '/account/ajax_reg',
                data: 'login=' + loginVal,
                success: function (result) {
                    if (result.message === 'Busy') {
                        $('#login-err').text('Login is busy')
                        loginCheck = false;
                    } else {
                        loginCheck = true
                        $('#login-err').text('')
                    }
                }
            });
        } else {
            $('#login-err').text('Login cannot be used')
            pwdCheck = false;
        }
    })

    $('#pwd').blur(function () {
        let pass1X = $('#pwd').val();
        let pass1R = /^(?=.*[a-z])(?=.*[A-Z])(?=.*[0-9])[a-zA-z0-9_]{8,}$/;
        if (pass1R.test(pass1X)) {
            $('#pwd-err').text('')
            pwdCheck = true;
        } else {
            pwdCheck = false;
            $('#pwd-err').text('Should contain at least 8 symbols, number, uppercase and lowercase letter')
        }
    })

    $('#pwd-repeat').blur(function () {
        let pass1X = $('#pwd').val();
        let pass2X = $('#pwd-repeat').val();
        if (pass1X === pass2X) {
            $('#pwd-repeat-err').text('')
            pwdRepeatCheck = true;
        } else {
            pwdRepeatCheck = false;
            $('#pwd-repeat-err').text('Passwords differ')
        }
    })

    $('#email').blur(function () {
        let emailX = $('#email').val();
        let emailR = /^([a-z0-9_-]+\.)*[a-z0-9_-]+@[a-z0-9_-]+(\.[a-z0-9_-]+)*\.[a-z]{2,6}$/;
        if (emailR.test(emailX)) {
            $('#email-err').text('')
            emailCheck = true;
        } else {
            emailCheck = false;
            $('#email-err').text('Email is wrong')
        }
    })

    $('#submit-btn').click(function () {
        alert('Clicked!')

        if (pwdCheck && pwdCheck && pwdRepeatCheck && emailCheck) {
            alert('OK')
            $('#form-register').attr('onsubmit', 'return true');
        } else {
            $('#form-register').attr('onsubmit', 'return false');
            alert('NOT OK')
            alert('Form contains wrong data')
        }
    });
});