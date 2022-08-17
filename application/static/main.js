const cardsWrapper = document.getElementById('cards-wrapper');
const dropdown = document.querySelectorAll('.dropdown');
const dropdownContent = document.querySelectorAll('.dropdown-content');
const childDropdown = document.querySelectorAll('.child-dropdown');
const childDropdownContent = document.querySelectorAll(
  '.child-dropdown-content'
);
const authForm = document.querySelector('#auth-form');
const passwordForm = document.querySelector('#pass-form');
const passFormRecoveryBtn = document.querySelector('#recovery');
const registrationBtnOnRecovery = document.querySelector(
  '#registration-on-recovery'
);
const emailForm = document.querySelector('#email-form');
const registerForm = document.querySelector('#register-form');
const authLinktoClick = document.querySelector('#auth-link');
const recoveryButton = document.querySelector('.recovery');
const registrationButton = document.querySelector('#registration-on-auth');
const registrationButtonOnEmail = document.querySelector(
  '#registration-on-email'
);

let id = (id) => document.getElementById(id);
let classes = (classes) => document.getElementsByClassName(classes);
let email = id('email'),
  enterBtn = id('enter'),
  emailFld = id('email'),
  passFld = id('pass'),
  password = id('pass'),
  firstName = id('first_name'),
  lastName = id('last_name'),
  region = id('region'),
  school = id('school'),
  grade = id('grade'),
  recoveryEmail = id('recovery_email'),
  recoveryPass = id('recovery_password'),
  repeatRecPass = id('repeat_pass'),
  registeringEmail = id('register_email'),
  newPassword = id('new_password'),
  repeatPassword = id('repeat_new_pass'),
  registrationBtn = id('registration-button'),
  successPage = id('successful-registration'),
  recoveryTab = id('successful-recovery-tab'),
  recoveryAgainBtn = id('send-to-recovery-again'),
  authContainer = id('auth-container'),
  successPassPage = id('successful-pass-change'),
  successIcon = classes('success-icon'),
  failureIcon = classes('failure-icon'),
  errorMessage = classes('email-msg'),
  myProfile = id('my-profile'),
  profileOptionTwo = id('profile-option-two');

// --------------- Filters

// filter btns
const filterBtns = document.querySelectorAll('.sorting .filter-buttons');

// filter containers
const filterContainers = document.querySelectorAll('.filter-container');

window.addEventListener('load', () => {
  filterBtns[0].addEventListener('click', () => {
    removeActiveFilter(filterContainers[1], filterContainers[2]);
    filterContainers[0].classList.toggle('active-filter');
  });
  filterBtns[1].addEventListener('click', () => {
    removeActiveFilter(filterContainers[0], filterContainers[2]);
    filterContainers[1].classList.toggle('active-filter');
  });
  filterBtns[2].addEventListener('click', () => {
    removeActiveFilter(filterContainers[0], filterContainers[1]);
    filterContainers[2].classList.toggle('active-filter');
  });
});

const removeActiveFilter = (item1, item2) => {
  if (item1.classList.contains('active-filter')) {
    item1.classList.remove('active-filter');
  }
  if (item2.classList.contains('active-filter')) {
    item2.classList.remove('active-filter');
  }
};

const contentContainerItems = document.querySelectorAll(
  '.content-container .item'
);
const contentContainerAuthors = document.querySelectorAll(
  '.content-container .tag'
);

window.addEventListener('load', () => {
  contentContainerItems.forEach((button) => {
    button.addEventListener('click', () => {
      button.classList.toggle('chosen');
    });
  });
  contentContainerAuthors.forEach((author) => {
    author.addEventListener('click', () => {
      author.classList.toggle('clicked');
    });
  });
});

