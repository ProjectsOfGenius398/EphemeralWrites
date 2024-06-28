/*!
  * Bootstrap v5.3.3 (https://getbootstrap.com/)
  * Copyright 2011-2024 The Bootstrap Authors (https://github.com/twbs/bootstrap/graphs/contributors)
  * Licensed under MIT (https://github.com/twbs/bootstrap/blob/main/LICENSE)
  */

//Carousel code
document.addEventListener('DOMContentLoaded', () => {
    const header = document.getElementById('mainHeader');
    let lastScrollTop = 0;

    window.addEventListener('scroll', function () {
        const currentScroll = window.pageYOffset || document.documentElement.scrollTop;

        if (currentScroll > lastScrollTop) {
            // Scroll down
            header.classList.add('hidden');
        } else {
            // Scroll up
            header.classList.remove('hidden');
        }

        lastScrollTop = currentScroll <= 0 ? 0 : currentScroll; // For Mobile or negative scrolling
    }, false);

    // Ensure the header is not hidden when the carousel is moving
    const carousel = document.querySelector('#myCarousel');
    const observer = new IntersectionObserver((entries) => {
        entries.forEach(entry => {
            if (entry.intersectionRatio > 0) {
                header.classList.remove('hidden');
            }
        });
    }, { threshold: [0.1] });

    observer.observe(carousel);
});

//Poetry archive code
poemTitles = ["Under piles of rubble", "If walls could hear"];
poemContent = [
    "<div style='text-align: left;'>Under piles of rubble are dreams that shined,<br>Bodies upon bodies, we know the truth is not kind.<br>That’s what is war, this is half of what is seen,<br>But to stop this, have we really been keen?<br><br>“Did you hear the news? So many have died”,<br>And what will you do friend, watch and move aside?<br>For as long as we lived, governments have been sly<br>Yet the one thing they choose to for stats is outright lie.<br><br>Is war really needed, or started just for fun?<br>Do people really see everything under the sun?<br>For a show of power does it make an excuse?<br>And for the victims, does it make the noose?<br><br>Is war just a name, or something to frighten the weak?<br>Just for the joy of death, a reason do people seek?<br>Why do we do so, when it lacks a basic reason,<br>And when citizens object it, we define it as treason?<br><br>Palestine and Israel, is that all you care for?<br>Let’s say Ruso-Ukraine, why only the two war?<br>Putting one in war’s picture, that barely shows reality,<br>No matter the true victor, it ends as just a catastrophe.<br><br>“We gave them the money, what more can they need?”,<br>“Just remove their rations if their voice will exceed”.<br>Brother, they need the one who killed himself on a track,<br>Brother, all they want is the one who shot himself in the back.<br><br>Is this what war is, an endless show of force?<br>What is what war is, a comedy show or a history course?<br>Has war become this, a theatre watched by the rich?<br>Has war become so common that leaders say “which”?<br><br>Do soldiers know that they follow orders of barbarism?<br>Do people value themselves, or the selfish supporters of communism?<br>Do leaders know what happens to the ones who are innocent?<br>Do dictators know what is happening while they are vinolent?<br><br>Beneath the rubble's weight, where dreams once gleamed,<br>Lies truth so harsh, in shadows, it's redeemed.<br>In war's cruel grip, just half the horrors gleaned,<br>But heed this warning, are we truly keen?</div> <div style='text-align:right;'><br>By <i>Anantjit Chander</i><br>June 17 2023</div>",

    "<div style='text-align: left;'>If walls could hear what all could they know,<br>They’d know so much that I’ve forgotten.<br>If my walls could tell you all I’ve told them,<br>You’d never want to leave this room.<br>For you might call it your room of love,<br>Where you’re nothing but loved over and over.<br><br><br><br>If my dreams could become a world to be in,<br>You’d never want to leave for the real one.<br>For you’ll find so much about yourself,<br>You’d be mesmerized by what I think of you.<br>You’d forget all that’s in the real world,<br>For it’s impossible to replicate my dreams.<br><br><br><br>More than a million things untold to you are,<br>I feel like I live in an unfinished building.<br>A building I’m scared to work on,<br>In fears of destroying what holds on so tight.<br>A building which despite my intentions,<br>Would crumble at the slightest adjustment.<br><br><br><br>I fall to pieces at the hint of your name,<br>I fall to pieces when something reminds me.<br>For now everything reminds me of you,<br>Everything does.<br>Everything that you ever liked,<br>Everything we do like.<div style='text-align:right;'><br>By <i>Anantjit Chander</i><br>June 17 2023</div></div>"]
    ;

function showPopup(number) {
    Swal.fire({
        title: poemTitles[number],
        html: poemContent[number],
        showCloseButton: true,
        confirmButtonText: 'Exit poem',
    });
}

