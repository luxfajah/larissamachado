/**
 * Branding Presentation Template Engine
 * Handles slide navigation, keyboard controls, wheel navigation, 16:9 viewport scaling,
 * interactive table of contents, and Slide 14 applications tab switching.
 */

import './index.css';

document.addEventListener('DOMContentLoaded', () => {
  const slides = document.querySelectorAll('.slide');
  const totalSlides = slides.length;
  let currentSlideIndex = 0;
  
  // Navigation elements
  const currentIndicator = document.getElementById('nav-current');
  const totalIndicator = document.getElementById('nav-total');
  const progressBar = document.getElementById('nav-progress-bar') as HTMLElement;
  const prevBtn = document.getElementById('btn-prev');
  const nextBtn = document.getElementById('btn-next');
  const presentationContainer = document.querySelector('.presentation-container') as HTMLElement;

  // Viewport scaling: scale 1920x1080 container to fit viewport or adapt responsively for mobile
  function handleResize() {
    if (!presentationContainer) return;
    
    const windowWidth = window.innerWidth;
    const windowHeight = window.innerHeight;
    
    // Scale fixed 16:9 canvas in landscape mode (both desktop and mobile!)
    const isLandscape = windowWidth > windowHeight;
    
    if (isLandscape) {
      const targetWidth = 1920;
      const targetHeight = 1080;
      const scale = Math.min(windowWidth / targetWidth, windowHeight / targetHeight);
      
      presentationContainer.style.width = `${targetWidth}px`;
      presentationContainer.style.height = `${targetHeight}px`;
      presentationContainer.style.top = '50%';
      presentationContainer.style.left = '50%';
      presentationContainer.style.transform = `translate(-50%, -50%) scale(${scale})`;
      presentationContainer.classList.remove('mobile-mode');

      // Update full-bleed images to fill 100% of screen width and height
      const fullBleedImgs = document.querySelectorAll('.full-bleed-slide-img');
      const imgWidth = windowWidth / scale;
      const imgHeight = windowHeight / scale;
      
      fullBleedImgs.forEach((img) => {
        const htmlImg = img as HTMLElement;
        htmlImg.style.width = `${imgWidth}px`;
        htmlImg.style.height = `${imgHeight}px`;
        htmlImg.style.left = `${(targetWidth - imgWidth) / 2}px`;
        htmlImg.style.top = `${(targetHeight - imgHeight) / 2}px`;
      });
    } else {
      // Mobile/tablet portrait adaptive fallback mode (blocked by orientation overlay)
      presentationContainer.style.width = '100%';
      presentationContainer.style.height = '100%';
      presentationContainer.style.top = '0';
      presentationContainer.style.left = '0';
      presentationContainer.style.transform = 'none';
      presentationContainer.classList.add('mobile-mode');

      // Reset styles
      const fullBleedImgs = document.querySelectorAll('.full-bleed-slide-img');
      fullBleedImgs.forEach((img) => {
        const htmlImg = img as HTMLElement;
        htmlImg.style.width = '100%';
        htmlImg.style.height = '100%';
        htmlImg.style.left = '0';
        htmlImg.style.top = '0';
      });
    }
  }

  // Slide navigation function
  function goToSlide(index: number) {
    if (index < 0 || index >= totalSlides) return;
    
    // Update classes on slides
    slides.forEach((slide, idx) => {
      slide.classList.remove('active', 'past', 'future');
      
      if (idx === index) {
        slide.classList.add('active');
      } else if (idx < index) {
        slide.classList.add('past');
      } else {
        slide.classList.add('future');
      }
    });



    // Update dynamic body theme (eliminate side letterboxing bars on wide screens)
    const activeSlide = slides[index];
    if (activeSlide) {
      const isDark = activeSlide.id === 'slide-01' || activeSlide.id === 'slide-18' || activeSlide.id === 'slide-19';
      if (isDark) {
        document.body.style.backgroundColor = '#2E2A6E';
        document.body.classList.add('hud-dark');
        presentationContainer.style.overflow = 'hidden';
      } else if (activeSlide.id === 'slide-10' || activeSlide.id === 'slide-11') {
        document.body.style.backgroundColor = '#f1eee9';
        document.body.classList.remove('hud-dark');
        presentationContainer.style.overflow = 'visible';
      } else if (activeSlide.id === 'slide-12') {
        document.body.style.backgroundColor = '#cfcdca';
        document.body.classList.remove('hud-dark');
        presentationContainer.style.overflow = 'visible';
      } else {
        document.body.style.backgroundColor = '#FAF9F6';
        document.body.classList.remove('hud-dark');
        presentationContainer.style.overflow = 'hidden';
      }
    }

    // Update index
    currentSlideIndex = index;
    
    // Update indicators
    if (currentIndicator) {
      currentIndicator.textContent = String(index + 1).padStart(2, '0');
    }
    if (totalIndicator) {
      totalIndicator.textContent = String(totalSlides).padStart(2, '0');
    }
    if (progressBar) {
      const percentage = ((index + 1) / totalSlides) * 100;
      progressBar.style.width = `${percentage}%`;
    }

    // Toggle button disabled states
    if (prevBtn) {
      if (index === 0) {
        prevBtn.setAttribute('disabled', 'true');
      } else {
        prevBtn.removeAttribute('disabled');
      }
    }
    if (nextBtn) {
      if (index === totalSlides - 1) {
        nextBtn.setAttribute('disabled', 'true');
      } else {
        nextBtn.removeAttribute('disabled');
      }
    }
  }

  // Navigation handlers
  function nextSlide() {
    if (currentSlideIndex < totalSlides - 1) {
      goToSlide(currentSlideIndex + 1);
    }
  }

  // Prev navigation
  function prevSlide() {
    if (currentSlideIndex > 0) {
      goToSlide(currentSlideIndex - 1);
    }
  }

  // Keyboard navigation
  window.addEventListener('keydown', (e) => {
    switch (e.key) {
      case 'ArrowRight':
      case 'Space':
      case ' ': // Space bar
      case 'Enter':
      case 'PageDown':
        e.preventDefault();
        nextSlide();
        break;
      case 'ArrowLeft':
      case 'Backspace':
      case 'PageUp':
        e.preventDefault();
        prevSlide();
        break;
      case 'Home':
        e.preventDefault();
        goToSlide(0);
        break;
      case 'End':
        e.preventDefault();
        goToSlide(totalSlides - 1);
        break;
    }
  });

  // Debounced scroll navigation to prevent fast scrolling through multiple slides
  let lastScrollTime = 0;
  const scrollCooldown = 900; // ms between slide changes via scroll

  window.addEventListener('wheel', (e) => {
    const currentTime = Date.now();
    if (currentTime - lastScrollTime < scrollCooldown) {
      return;
    }

    // Check if the scroll threshold is met to trigger navigation
    if (Math.abs(e.deltaY) > 30) {
      if (e.deltaY > 0) {
        nextSlide();
        lastScrollTime = currentTime;
      } else if (e.deltaY < 0) {
        prevSlide();
        lastScrollTime = currentTime;
      }
    }
  }, { passive: true });

  // Touch Swipe navigation for mobile/tablet presentation previewing
  let touchStartX = 0;
  let touchStartY = 0;

  window.addEventListener('touchstart', (e) => {
    touchStartX = e.changedTouches[0].screenX;
    touchStartY = e.changedTouches[0].screenY;
  }, { passive: true });

  window.addEventListener('touchend', (e) => {
    const touchEndX = e.changedTouches[0].screenX;
    const touchEndY = e.changedTouches[0].screenY;
    
    const deltaX = touchEndX - touchStartX;
    const deltaY = touchEndY - touchStartY;
    
    // Only register horizontal swipes if vertical movement is minimal
    if (Math.abs(deltaX) > 50 && Math.abs(deltaY) < 100) {
      if (deltaX < 0) {
        nextSlide();
      } else {
        prevSlide();
      }
    }
  }, { passive: true });

  // Button navigation listeners
  if (prevBtn) {
    prevBtn.addEventListener('click', (e) => {
      e.stopPropagation();
      prevSlide();
    });
  }

  if (nextBtn) {
    nextBtn.addEventListener('click', (e) => {
      e.stopPropagation();
      nextSlide();
    });
  }

  // Interactive Sumário (Slide 2) click items
  const indexItems = document.querySelectorAll('.index-item');
  indexItems.forEach((item) => {
    item.addEventListener('click', (e) => {
      e.stopPropagation();
      const targetStr = item.getAttribute('data-target');
      if (targetStr) {
        const targetIdx = parseInt(targetStr, 10);
        goToSlide(targetIdx);
      }
    });
  });

  // Slide 14: Applications Tab Switcher
  const appTabs = document.querySelectorAll('.app-tab-btn');
  const appPanels = document.querySelectorAll('.app-panel');

  appTabs.forEach((tab) => {
    tab.addEventListener('click', (e) => {
      e.stopPropagation();
      
      // Get target application name
      const targetApp = tab.getAttribute('data-app');
      if (!targetApp) return;

      // Update active tab button style
      appTabs.forEach(t => t.classList.remove('active'));
      tab.classList.add('active');

      // Update active panel display
      appPanels.forEach((panel) => {
        panel.classList.remove('active');
        if (panel.id === `panel-${targetApp}`) {
          panel.classList.add('active');
        }
      });
    });
  });

  // Fullscreen Logo Lightbox Modal Interaction
  const logoCleanBoxes = document.querySelectorAll('.logo-clean-box');
  const logoLightbox = document.getElementById('logo-lightbox');
  const lightboxImg = document.getElementById('lightbox-img') as HTMLImageElement;
  const lightboxCloseBtn = document.querySelector('.lightbox-close-btn');

  if (logoLightbox && lightboxImg) {
    logoCleanBoxes.forEach((box) => {
      box.addEventListener('click', (e) => {
        e.stopPropagation();
        const img = box.querySelector('img');
        if (img) {
          const imgSrc = img.getAttribute('src');
          if (imgSrc) {
            lightboxImg.src = imgSrc;
            logoLightbox.classList.add('active');
          }
        }
      });
    });

    const closeLightbox = () => {
      logoLightbox.classList.remove('active');
      setTimeout(() => {
        lightboxImg.src = '';
      }, 300);
    };

    if (lightboxCloseBtn) {
      lightboxCloseBtn.addEventListener('click', (e) => {
        e.stopPropagation();
        closeLightbox();
      });
    }

    logoLightbox.addEventListener('click', (e) => {
      if (e.target === logoLightbox) {
        closeLightbox();
      }
    });

    window.addEventListener('keydown', (e) => {
      if (e.key === 'Escape' && logoLightbox.classList.contains('active')) {
        closeLightbox();
      }
    });
  }

  // Slide 18: Interactive Direction Selection
  const btnSelectA = document.getElementById('btn-select-a');
  const btnSelectB = document.getElementById('btn-select-b');
  const successBox = document.getElementById('selection-success-box');
  const btnReset = document.getElementById('btn-reset-selection');
  const nextStepsContent = document.getElementById('next-steps-slide-content');

  const updateSelectionUI = (selectedOption: 'A' | 'B' | null) => {
    if (selectedOption === 'A') {
      btnSelectA?.classList.add('selected');
      btnSelectB?.classList.remove('selected');
      successBox?.classList.add('active');
      nextStepsContent?.classList.add('direction-a-active');
      nextStepsContent?.classList.remove('direction-b-active');
    } else if (selectedOption === 'B') {
      btnSelectB?.classList.add('selected');
      btnSelectA?.classList.remove('selected');
      successBox?.classList.add('active');
      nextStepsContent?.classList.add('direction-b-active');
      nextStepsContent?.classList.remove('direction-a-active');
    } else {
      btnSelectA?.classList.remove('selected');
      btnSelectB?.classList.remove('selected');
      successBox?.classList.remove('active');
      nextStepsContent?.classList.remove('direction-a-active', 'direction-b-active');
    }
  };

  // Check existing selection on load
  const savedSelection = localStorage.getItem('dra_larissa_brand_selection');
  if (savedSelection === 'A' || savedSelection === 'B') {
    updateSelectionUI(savedSelection as 'A' | 'B');
  }

  btnSelectA?.addEventListener('click', (e) => {
    e.stopPropagation();
    localStorage.setItem('dra_larissa_brand_selection', 'A');
    updateSelectionUI('A');
    setTimeout(() => {
      goToSlide(18); // slide 19 is index 18
    }, 1500);
  });

  btnSelectB?.addEventListener('click', (e) => {
    e.stopPropagation();
    localStorage.setItem('dra_larissa_brand_selection', 'B');
    updateSelectionUI('B');
    setTimeout(() => {
      goToSlide(18); // slide 19 is index 18
    }, 1500);
  });

  btnReset?.addEventListener('click', (e) => {
    e.stopPropagation();
    localStorage.removeItem('dra_larissa_brand_selection');
    updateSelectionUI(null);
  });

  // Setup scaling resize event
  window.addEventListener('resize', handleResize);
  
  // Initialize Presentation
  handleResize();
  goToSlide(0);

  // Focus window on load to ensure keyboard navigation works immediately
  window.focus();
});
