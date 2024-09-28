/**
* Template Name: NiceAdmin
* Updated: Nov 17 2023 with Bootstrap v5.3.2
* Template URL: https://bootstrapmade.com/nice-admin-bootstrap-admin-html-template/
* Author: BootstrapMade.com
* License: https://bootstrapmade.com/license/
*/
(function() {
  "use strict";

  /**
   * Easy selector helper function
   */
  const select = (el, all = false) => {
    el = el.trim()
    if (all) {
      return [...document.querySelectorAll(el)]
    } else {
      return document.querySelector(el)
    }
  }

  /**
   * Easy event listener function
   */
  const on = (type, el, listener, all = false) => {
    if (all) {
      select(el, all).forEach(e => e.addEventListener(type, listener))
    } else {
      select(el, all).addEventListener(type, listener)
    }
  }

  /**
   * Easy on scroll event listener 
   */
  const onscroll = (el, listener) => {
    el.addEventListener('scroll', listener)
  }

  /**
   * Sidebar toggle
   */
  if (select('.toggle-sidebar-btn')) {
    on('click', '.toggle-sidebar-btn', function(e) {
      select('body').classList.toggle('toggle-sidebar')
    })
  }

  /**
   * Search bar toggle
   */
  if (select('.search-bar-toggle')) {
    on('click', '.search-bar-toggle', function(e) {
      select('.search-bar').classList.toggle('search-bar-show')
    })
  }

  /**
   * Navbar links active state on scroll
   */
  let navbarlinks = select('#navbar .scrollto', true)
  const navbarlinksActive = () => {
    let position = window.scrollY + 200
    navbarlinks.forEach(navbarlink => {
      if (!navbarlink.hash) return
      let section = select(navbarlink.hash)
      if (!section) return
      if (position >= section.offsetTop && position <= (section.offsetTop + section.offsetHeight)) {
        navbarlink.classList.add('active')
      } else {
        navbarlink.classList.remove('active')
      }
    })
  }
  window.addEventListener('load', navbarlinksActive)
  onscroll(document, navbarlinksActive)

  /**
   * Toggle .header-scrolled class to #header when page is scrolled
   */
  let selectHeader = select('#header')
  if (selectHeader) {
    const headerScrolled = () => {
      if (window.scrollY > 100) {
        selectHeader.classList.add('header-scrolled')
      } else {
        selectHeader.classList.remove('header-scrolled')
      }
    }
    window.addEventListener('load', headerScrolled)
    onscroll(document, headerScrolled)
  }

  /**
   * Back to top button
   */
  let backtotop = select('.back-to-top')
  if (backtotop) {
    const toggleBacktotop = () => {
      if (window.scrollY > 100) {
        backtotop.classList.add('active')
      } else {
        backtotop.classList.remove('active')
      }
    }
    window.addEventListener('load', toggleBacktotop)
    onscroll(document, toggleBacktotop)
  }

  /**
   * Initiate tooltips
   */
  var tooltipTriggerList = [].slice.call(document.querySelectorAll('[data-bs-toggle="tooltip"]'))
  var tooltipList = tooltipTriggerList.map(function(tooltipTriggerEl) {
    return new bootstrap.Tooltip(tooltipTriggerEl)
  })

  /**
   * Initiate quill editors
   */
  if (select('.quill-editor-default')) {
    new Quill('.quill-editor-default', {
      theme: 'snow'
    });
  }

  if (select('.quill-editor-bubble')) {
    new Quill('.quill-editor-bubble', {
      theme: 'bubble'
    });
  }

  if (select('.quill-editor-full')) {
    new Quill(".quill-editor-full", {
      modules: {
        toolbar: [
          [{
            font: []
          }, {
            size: []
          }],
          ["bold", "italic", "underline", "strike"],
          [{
              color: []
            },
            {
              background: []
            }
          ],
          [{
              script: "super"
            },
            {
              script: "sub"
            }
          ],
          [{
              list: "ordered"
            },
            {
              list: "bullet"
            },
            {
              indent: "-1"
            },
            {
              indent: "+1"
            }
          ],
          ["direction", {
            align: []
          }],
          ["link", "image", "video"],
          ["clean"]
        ]
      },
      theme: "snow"
    });
  }

  /**
   * Initiate TinyMCE Editor
   */
  const useDarkMode = window.matchMedia('(prefers-color-scheme: dark)').matches;
  const isSmallScreen = window.matchMedia('(max-width: 1023.5px)').matches;

  tinymce.init({
    selector: 'textarea.tinymce-editor',
    plugins: 'preview importcss searchreplace autolink autosave save directionality code visualblocks visualchars fullscreen image link media template codesample table charmap pagebreak nonbreaking anchor insertdatetime advlist lists wordcount help charmap quickbars emoticons',
    editimage_cors_hosts: ['picsum.photos'],
    menubar: 'file edit view insert format tools table help',
    toolbar: 'undo redo | bold italic underline strikethrough | fontfamily fontsize blocks | alignleft aligncenter alignright alignjustify | outdent indent |  numlist bullist | forecolor backcolor removeformat | pagebreak | charmap emoticons | fullscreen  preview save print | insertfile image media template link anchor codesample | ltr rtl',
    toolbar_sticky: true,
    toolbar_sticky_offset: isSmallScreen ? 102 : 108,
    autosave_ask_before_unload: true,
    autosave_interval: '30s',
    autosave_prefix: '{path}{query}-{id}-',
    autosave_restore_when_empty: false,
    autosave_retention: '2m',
    image_advtab: true,
    link_list: [{
        title: 'My page 1',
        value: 'https://www.tiny.cloud'
      },
      {
        title: 'My page 2',
        value: 'http://www.moxiecode.com'
      }
    ],
    image_list: [{
        title: 'My page 1',
        value: 'https://www.tiny.cloud'
      },
      {
        title: 'My page 2',
        value: 'http://www.moxiecode.com'
      }
    ],
    image_class_list: [{
        title: 'None',
        value: ''
      },
      {
        title: 'Some class',
        value: 'class-name'
      }
    ],
    importcss_append: true,
    file_picker_callback: (callback, value, meta) => {
      /* Provide file and text for the link dialog */
      if (meta.filetype === 'file') {
        callback('https://www.google.com/logos/google.jpg', {
          text: 'My text'
        });
      }

      /* Provide image and alt text for the image dialog */
      if (meta.filetype === 'image') {
        callback('https://www.google.com/logos/google.jpg', {
          alt: 'My alt text'
        });
      }

      /* Provide alternative source and posted for the media dialog */
      if (meta.filetype === 'media') {
        callback('movie.mp4', {
          source2: 'alt.ogg',
          poster: 'https://www.google.com/logos/google.jpg'
        });
      }
    },
    templates: [{
        title: 'New Table',
        description: 'creates a new table',
        content: '<div class="mceTmpl"><table width="98%%"  border="0" cellspacing="0" cellpadding="0"><tr><th scope="col"> </th><th scope="col"> </th></tr><tr><td> </td><td> </td></tr></table></div>'
      },
      {
        title: 'Starting my story',
        description: 'A cure for writers block',
        content: 'Once upon a time...'
      },
      {
        title: 'New list with dates',
        description: 'New List with dates',
        content: '<div class="mceTmpl"><span class="cdate">cdate</span><br><span class="mdate">mdate</span><h2>My List</h2><ul><li></li><li></li></ul></div>'
      }
    ],
    template_cdate_format: '[Date Created (CDATE): %m/%d/%Y : %H:%M:%S]',
    template_mdate_format: '[Date Modified (MDATE): %m/%d/%Y : %H:%M:%S]',
    height: 600,
    image_caption: true,
    quickbars_selection_toolbar: 'bold italic | quicklink h2 h3 blockquote quickimage quicktable',
    noneditable_class: 'mceNonEditable',
    toolbar_mode: 'sliding',
    contextmenu: 'link image table',
    skin: useDarkMode ? 'oxide-dark' : 'oxide',
    content_css: useDarkMode ? 'dark' : 'default',
    content_style: 'body { font-family:Helvetica,Arial,sans-serif; font-size:16px }'
  });

  /**
   * Initiate Bootstrap validation check
   */
  var needsValidation = document.querySelectorAll('.needs-validation')

  Array.prototype.slice.call(needsValidation)
    .forEach(function(form) {
      form.addEventListener('submit', function(event) {
        if (!form.checkValidity()) {
          event.preventDefault()
          event.stopPropagation()
        }

        form.classList.add('was-validated')
      }, false)
    })

  /**
   * Initiate Datatables
   */
  const datatables = select('.datatable', true)
  datatables.forEach(datatable => {
    new simpleDatatables.DataTable(datatable, {
      perPageSelect: [5, 10, 15, ["All", -1]],
      columns: [{
          select: 2,
          sortSequence: ["desc", "asc"]
        },
        {
          select: 3,
          sortSequence: ["desc"]
        },
        {
          select: 4,
          cellClass: "green",
          headerClass: "red"
        }
      ]
    });
  })

  /**
   * Autoresize echart charts
   */
  const mainContainer = select('#main');
  if (mainContainer) {
    setTimeout(() => {
      new ResizeObserver(function() {
        select('.echart', true).forEach(getEchart => {
          echarts.getInstanceByDom(getEchart).resize();
        })
      }).observe(mainContainer);
    }, 200);
  }

})();

// piechart

let progressBar = document.querySelector(".circular-progress");
let progressBar1 = document.querySelector(".circular-progress1");
let progressBar2 = document.querySelector(".circular-progress2");
let progressBar3 = document.querySelector(".circular-progress3");
let progressBar4 = document.querySelector(".circular-progress4");
let progressBar5 = document.querySelector(".circular-progress5");
let progressBar6 = document.querySelector(".circular-progress6");
let progressBar7 = document.querySelector(".circular-progress7");
let progressBar8 = document.querySelector(".circular-progress8");
let progressBar9 = document.querySelector(".circular-progress9");
let valueContainer = document.querySelector(".value-container");
let valueContainer1 = document.querySelector(".value-container1");
let valueContainer2 = document.querySelector(".value-container2");
let valueContainer3 = document.querySelector(".value-container3");
let valueContainer4 = document.querySelector(".value-container4");
let valueContainer5 = document.querySelector(".value-container5");
let valueContainer6 = document.querySelector(".value-container6");
let valueContainer7 = document.querySelector(".value-container7");
let valueContainer8 = document.querySelector(".value-container8");
let valueContainer9 = document.querySelector(".value-container9");



let progressValue = 0;
let progressValue1 = 0;
let progressValue2 = 0;
let progressValue3 = 0;
let progressValue4 = 0;
let progressValue5 = 0;
let progressValue6 = 0;
let progressValue7 = 0;
let progressValue8 = 0;
let progressValue9 = 0;

let progressEndValue = 10;
let progressEndValue1 = 30;
let progressEndValue2 = 40;
let progressEndValue3 = 60;
let progressEndValue4 = 80;
let progressEndValue5= 95;
let progressEndValue6= 75;
let progressEndValue7= 75;
let progressEndValue8= 75;
let progressEndValue9= 75;


let speed = 50;

let progress = setInterval(() => {
  progressValue++;
  // valueContainer.textContent = `${progressValue}%`;
  progressBar.style.background = `conic-gradient(
  #4154f1 ${progressValue * 3.6}deg,
  #cadcff ${progressValue * 3.6}deg
)`;
  if (progressValue == progressEndValue) {
    clearInterval(progress);
  }
}, speed);

let progress1= setInterval(() => {
  progressValue1++;
  // valueContainer1.textContent = `${progressValue1}%`;
  progressBar1.style.background = `conic-gradient(
  #4154f1 ${progressValue1 * 3.6}deg,
  #cadcff ${progressValue1 * 3.6}deg
)`;
  if (progressValue1 == progressEndValue1) {
    clearInterval(progress1);
  }
}, speed);

let progress2= setInterval(() => {
  progressValue2++;
  // valueContainer2.textContent = `${progressValue2}%`;
  progressBar2.style.background = `conic-gradient(
  #4154f1 ${progressValue2 * 3.6}deg,
  #cadcff ${progressValue2 * 3.6}deg
)`;
  if (progressValue2 == progressEndValue2) {
    clearInterval(progress2);
  }
}, speed);

let progress3= setInterval(() => {
  progressValue3++;
  // valueContainer3.textContent = `${progressValue3}%`;
  progressBar3.style.background = `conic-gradient(
  #4154f1 ${progressValue3 * 3.6}deg,
  #cadcff ${progressValue3 * 3.6}deg
)`;
  if (progressValue3 == progressEndValue3) {
    clearInterval(progress3);
  }
}, speed);

let progress4= setInterval(() => {
  progressValue4++;
  valueContainer4.textContent = `${progressValue4}%`;
  progressBar4.style.background = `conic-gradient(
  #4154f1 ${progressValue4 * 3.6}deg,
  #cadcff ${progressValue4 * 3.6}deg
)`;
  if (progressValue4 == progressEndValue4) {
    clearInterval(progress4);
  }
}, speed);

let progress5= setInterval(() => {
  progressValue5++;
  // valueContainer5.textContent = `${progressValue5}%`;
  progressBar5.style.background = `conic-gradient(
    #2eca6a ${progressValue5 * 3.6}deg,
    #e0f8e9 ${progressValue5 * 3.6}deg
)`;
  if (progressValue5 == progressEndValue5) {
    clearInterval(progress5);
  }
}, speed);

let progress6= setInterval(() => {
  progressValue6++;
  // valueContainer6.textContent = `${progressValue6}%`;
  progressBar6.style.background = `conic-gradient(
  #2eca6a ${progressValue6 * 3.6}deg,
  #e0f8e9 ${progressValue6 * 3.6}deg
)`;
  if (progressValue6 == progressEndValue6) {
    clearInterval(progress6);
  }
}, speed);

let progress7= setInterval(() => {
  progressValue7++;
  // valueContainer7.textContent = `${progressValue7}%`;
  progressBar7.style.background = `conic-gradient(
    #2eca6a ${progressValue7 * 3.6}deg,
    #e0f8e9 ${progressValue7 * 3.6}deg
)`;
  if (progressValue7 == progressEndValue7) {
    clearInterval(progress7);
  }
}, speed);

let progress8= setInterval(() => {
  progressValue8++;
  // valueContainer8.textContent = `${progressValue8}%`;
  progressBar8.style.background = `conic-gradient(
  #2eca6a  ${progressValue8 * 3.6}deg,
  #e0f8e9  ${progressValue8 * 3.6}deg
)`;
  if (progressValue8 == progressEndValue8) {
    clearInterval(progress8);
  }
}, speed);

let progress9= setInterval(() => {
  progressValue9++;
  valueContainer9.textContent = `${progressValue9}%`;
  progressBar9.style.background = `conic-gradient(
  #2eca6a ${progressValue9 * 3.6}deg,
  #e0f8e9 ${progressValue9 * 3.6}deg
)`;
  if (progressValue9 == progressEndValue9) {
    clearInterval(progress9);
  }
}, speed);