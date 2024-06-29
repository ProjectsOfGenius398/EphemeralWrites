import { initializeApp } from "firebase/app";
import { getAnalytics } from "firebase/analytics";
import { getAuth, signInWithEmailAndPassword, onAuthStateChanged } from "firebase/auth";
import { getFirestore, collection, addDoc, getDocs, serverTimestamp } from "firebase/firestore";

// Your web app's Firebase configuration
const firebaseConfig = {
  apiKey: "AIzaSyCX2sz_A0O_wOQIP38YB6_dBoJKt-klnho",
  authDomain: "ephemeralwrites-vid306.firebaseapp.com",
  projectId: "ephemeralwrites-vid306",
  storageBucket: "ephemeralwrites-vid306.appspot.com",
  messagingSenderId: "966518366890",
  appId: "1:966518366890:web:bc6aae29e0a1f5f0a926d3",
  measurementId: "G-MVV879D57G"
};

// Initialize Firebase
const app = initializeApp(firebaseConfig);
const analytics = getAnalytics(app);
const auth = getAuth(app);
const db = getFirestore(app);

export { auth, signInWithEmailAndPassword, onAuthStateChanged, db, collection, addDoc, getDocs, serverTimestamp };
