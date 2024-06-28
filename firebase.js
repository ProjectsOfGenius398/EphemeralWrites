import { initializeApp} from "./firebase-app.js";
import {getAuth, signInWithEmailAndPassword } from "./firebase-auth.js";

const firebaseConfig = {
    apiKey: "AIzaSyBNMrV_gECqN64WMUcBXSWU8b6G0fYMKtg",
    authDomain: "ephemeralwrites-37041.firebaseapp.com",
    projectId: "ephemeralwrites-37041",
    storageBucket: "ephemeralwrites-37041.appspot.com",
    messagingSenderId: "924593794076",
    appId: "1:924593794076:web:7d576604653a4a6142c3d9",
    measurementId: "G-W0KCEXCVS5"
};
// Initialize Firebase
const app = initializeApp(firebaseConfig);
const auth = getAuth(app);

// Function to show login popup
function showLoginPopup() {
  Swal.fire({
    title: 'Login',
    html:
      '<input id="swal-input-email" class="swal2-input" placeholder="Email">' +
      '<input id="swal-input-password" type="password" class="swal2-input" placeholder="Password">',
    showCancelButton: true,
    confirmButtonText: 'Sign In',
    cancelButtonText: 'Cancel',
    showLoaderOnConfirm: true,
    preConfirm: () => {
      const email = document.getElementById('swal-input-email').value;
      const password = document.getElementById('swal-input-password').value;
      return signInWithEmailAndPassword(auth, email, password)
        .then((userCredential) => {
          const user = userCredential.user;
          return user;
        })
        .catch((error) => {
          Swal.showValidationMessage(`Authentication failed: ${error.message}`);
        });
    },
    allowOutsideClick: () => !Swal.isLoading()
  }).then((result) => {
    if (result.isConfirmed) {
      Swal.fire({
        title: 'Logged In!',
        icon: 'success'
      });
    }
  });
}