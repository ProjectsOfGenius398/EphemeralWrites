 import { auth, signInWithEmailAndPassword } from './firebase-init.js';

        function showLogin() {
            Swal.fire({
                title: 'Login',
                html: `<input type="email" id="email" class="swal2-input" placeholder="Email">
                       <input type="password" id="password" class="swal2-input" placeholder="Password">`,
                confirmButtonText: 'Sign in',
                focusConfirm: false,
                preConfirm: () => {
                    const email = Swal.getPopup().querySelector('#email').value;
                    const password = Swal.getPopup().querySelector('#password').value;
                    if (!email || !password) {
                        Swal.showValidationMessage(`Please enter email and password`);
                    }
                    return { email: email, password: password };
                }
            }).then((result) => {
                if (result.isConfirmed) {
                    const email = result.value.email;
                    const password = result.value.password;
                    signInWithEmailAndPassword(auth, email, password)
                        .then((userCredential) => {
                            Swal.fire(`Logged in as: ${userCredential.user.email}`);
                            // Handle successful login
                        })
                        .catch((error) => {
                            Swal.fire(`Error: ${error.message}`);
                        });
                }
            });
        }