/**
 * Branding Presentation Template Engine
 * Handles slide navigation, keyboard controls, wheel navigation, 16:9 viewport scaling,
 * interactive table of contents, and Slide 14 applications tab switching.
 */

import './index.css';
// @ts-ignore
import { initFlipbook } from './livreto';

document.addEventListener('DOMContentLoaded', () => {
  initFlipbook();

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

  // Responsive Viewport: Occupy 100% width and height like a web application
  function handleResize() {
    if (!presentationContainer) return;
    
    presentationContainer.style.width = '100%';
    presentationContainer.style.height = '100%';
    presentationContainer.style.top = '0';
    presentationContainer.style.left = '0';
    presentationContainer.style.transform = 'none';

    // Ensure full-bleed mockup/gallery images fill 100% of screen without margins
    const fullBleedImgs = document.querySelectorAll('.full-bleed-slide-img, .mockup-full-bleed-img');
    fullBleedImgs.forEach((img) => {
      const htmlImg = img as HTMLElement;
      htmlImg.style.width = '100%';
      htmlImg.style.height = '100%';
      htmlImg.style.left = '0';
      htmlImg.style.top = '0';
      htmlImg.style.objectFit = 'cover';
    });
  }

  // Single Page 1015 Gallery Logic (No animations, instant step change)
  let gallery1015Index = 0;

  function updateGallery1015Item(index: number) {
    const slide = document.getElementById('slide-1015-gallery');
    if (!slide) return;
    const items = slide.querySelectorAll('.gallery-1015-item');
    items.forEach((item, idx) => {
      if (idx === index) {
        item.classList.add('active');
      } else {
        item.classList.remove('active');
      }
    });
    const counter = slide.querySelector('#gallery-current-num');
    const totalSpan = slide.querySelector('#gallery-total-num');
    if (counter) {
      counter.textContent = String(index + 1).padStart(2, '0');
    }
    if (totalSpan) {
      totalSpan.textContent = String(items.length).padStart(2, '0');
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

    // Reset gallery item when entering 1015 gallery slide
    const activeSlideId = slides[index]?.id;
    if (activeSlideId === 'slide-1015-gallery') {
      gallery1015Index = 0;
      updateGallery1015Item(0);
    }

    // Update dynamic body & container theme to eliminate letterboxing and blend smoothly
    const activeSlide = slides[index];
    if (activeSlide) {
      const theme = activeSlide.getAttribute('data-theme') || 'off-white';
      
      if (theme === 'dark-petrol') {
        document.body.style.backgroundColor = '#1C262B';
        if (presentationContainer) presentationContainer.style.backgroundColor = '#1C262B';
        document.body.classList.add('hud-dark');
      } else if (theme === 'sand-paper') {
        document.body.style.backgroundColor = '#F4F0EA';
        if (presentationContainer) presentationContainer.style.backgroundColor = '#F4F0EA';
        document.body.classList.remove('hud-dark');
      } else if (theme === 'neutral-grey') {
        document.body.style.backgroundColor = '#ECE9E3';
        if (presentationContainer) presentationContainer.style.backgroundColor = '#ECE9E3';
        document.body.classList.remove('hud-dark');
      } else {
        document.body.style.backgroundColor = '#FAF9F6';
        if (presentationContainer) presentationContainer.style.backgroundColor = '#FAF9F6';
        document.body.classList.remove('hud-dark');
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

  // Navigation handlers with inner gallery progression on slide-1015-gallery
  function nextSlide() {
    const activeId = slides[currentSlideIndex]?.id;
    if (activeId === 'slide-1015-gallery') {
      const slide = document.getElementById('slide-1015-gallery');
      const itemsCount = slide ? slide.querySelectorAll('.gallery-1015-item').length : 18;
      if (gallery1015Index < itemsCount - 1) {
        gallery1015Index++;
        updateGallery1015Item(gallery1015Index);
        return;
      }
    }

    if (currentSlideIndex < totalSlides - 1) {
      goToSlide(currentSlideIndex + 1);
    }
  }

  // Prev navigation handlers with inner gallery regression on slide-1015-gallery
  function prevSlide() {
    const activeId = slides[currentSlideIndex]?.id;
    if (activeId === 'slide-1015-gallery') {
      if (gallery1015Index > 0) {
        gallery1015Index--;
        updateGallery1015Item(gallery1015Index);
        return;
      }
    }

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

  appTabs.forEach((tab) => {
    tab.addEventListener('click', (e) => {
      e.stopPropagation();
      
      // Get target application name
      const targetApp = tab.getAttribute('data-app');
      if (!targetApp) return;

      // Update active tab button style
      appTabs.forEach(t => t.classList.remove('active'));
      tab.classList.add('active');

      // Find current and next panels
      const currentPanel = document.querySelector('.app-panel.active') as HTMLElement | null;
      const nextPanel = document.getElementById(`panel-${targetApp}`) as HTMLElement | null;

      if (!nextPanel || currentPanel === nextPanel) return;

      // Trigger exit animation on current panel
      if (currentPanel) {
        currentPanel.classList.add('exiting');
        currentPanel.classList.remove('active');
        // Clean up exiting class after animation completes
        setTimeout(() => {
          currentPanel.classList.remove('exiting');
        }, 520);
      }

      // Trigger enter animation on next panel
      nextPanel.classList.add('active');
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

  // Drive Explorer Interactive Folder Switcher
  const sidebarItems = document.querySelectorAll('.sidebar-folder-item');
  const detailPanels = document.querySelectorAll('.folder-detail-panel');
  const breadcrumbActive = document.querySelector('.active-bc');

  sidebarItems.forEach((item) => {
    item.addEventListener('click', (e) => {
      e.stopPropagation();
      const folderId = item.getAttribute('data-folder');
      
      // Update sidebar active states
      sidebarItems.forEach((sb) => sb.classList.remove('active'));
      item.classList.add('active');

      // Update detail panel active states
      detailPanels.forEach((panel) => panel.classList.remove('active'));
      const targetPanel = document.getElementById(`folder-detail-${folderId}`);
      if (targetPanel) {
        targetPanel.classList.add('active');
      }

      // Update breadcrumb text
      const folderNameEl = item.querySelector('.sf-name');
      if (folderNameEl && breadcrumbActive) {
        breadcrumbActive.textContent = folderNameEl.textContent || 'Pasta';
      }
    });
  });

  // ==========================================================================
  // INSTAGRAM STORIES FULLSCREEN MODAL INTERACTION (REAL IMAGES)
  // ==========================================================================
  const storiesModal = document.getElementById('instagram-stories-modal');
  const btnCloseStories = document.getElementById('btn-close-stories');
  const storyProgressRow = document.getElementById('story-progress-row');
  const storySlideContent = document.getElementById('story-slide-content');
  const storyTapLeft = document.getElementById('story-tap-left');
  const storyTapRight = document.getElementById('story-tap-right');
  const storyBtnPrev = document.getElementById('story-btn-prev');
  const storyBtnNext = document.getElementById('story-btn-next');

  const storiesData: Record<string, string[]> = {
    '1': [
      './redes-sociais/Destaque 1.1.jpg',
      './redes-sociais/Destaque 1.2.jpg',
      './redes-sociais/Destaque 1.3.jpg',
      './redes-sociais/Destaque 1.4.jpg'
    ],
    '2': [
      './redes-sociais/Destaque 2.jpg'
    ]
  };

  let activeStoryKey: '1' | '2' = '1';
  let activeStorySlideIdx = 0;

  function renderStorySlide(storyKey: '1' | '2', slideIdx: number) {
    const storyImgs = storiesData[storyKey];
    if (!storyImgs || !storyImgs[slideIdx]) return;
    const imgUrl = storyImgs[slideIdx];

    if (storyProgressRow) {
      storyProgressRow.innerHTML = storyImgs.map((_, idx) => `
        <div class="story-prog-bar">
          <div class="story-prog-fill" style="width: ${idx <= slideIdx ? '100%' : '0%'};"></div>
        </div>
      `).join('');
    }

    if (storySlideContent) {
      storySlideContent.innerHTML = `<img src="${imgUrl}" alt="Story" style="width:100%; height:100%; object-fit:contain; border-radius:12px;">`;
    }
  }

  function openStoriesModal(storyKey: '1' | '2') {
    activeStoryKey = storyKey;
    activeStorySlideIdx = 0;
    if (storiesModal) {
      storiesModal.classList.add('active');
      renderStorySlide(activeStoryKey, activeStorySlideIdx);
    }
  }

  function closeStoriesModal() {
    if (storiesModal) {
      storiesModal.classList.remove('active');
    }
  }

  document.querySelectorAll('[data-story]').forEach(el => {
    el.addEventListener('click', (e) => {
      e.stopPropagation();
      const storyVal = el.getAttribute('data-story');
      if (storyVal === '1' || storyVal === '2') {
        openStoriesModal(storyVal);
      }
    });
  });

  btnCloseStories?.addEventListener('click', (e) => {
    e.stopPropagation();
    closeStoriesModal();
  });

  function prevStorySlide() {
    if (activeStorySlideIdx > 0) {
      activeStorySlideIdx--;
      renderStorySlide(activeStoryKey, activeStorySlideIdx);
    }
  }

  function nextStorySlide() {
    const storyImgs = storiesData[activeStoryKey];
    if (storyImgs && activeStorySlideIdx < storyImgs.length - 1) {
      activeStorySlideIdx++;
      renderStorySlide(activeStoryKey, activeStorySlideIdx);
    } else {
      closeStoriesModal();
    }
  }

  storyTapLeft?.addEventListener('click', (e) => {
    e.stopPropagation();
    prevStorySlide();
  });

  storyTapRight?.addEventListener('click', (e) => {
    e.stopPropagation();
    nextStorySlide();
  });

  storyBtnPrev?.addEventListener('click', (e) => {
    e.stopPropagation();
    prevStorySlide();
  });

  storyBtnNext?.addEventListener('click', (e) => {
    e.stopPropagation();
    nextStorySlide();
  });

  // ==========================================================================
  // INDIVIDUAL POST CAROUSELS HANDLER (inside iPhone mockup)
  // ==========================================================================
  document.querySelectorAll('[data-post-carousel]').forEach(box => {
    const pid = box.getAttribute('data-post-carousel');
    // Buttons may be inside ig-post-carousel-viewport (new style)
    const prevBtn = box.querySelector('.prev-card-btn, .ig-carousel-prev');
    const nextBtn = box.querySelector('.next-card-btn, .ig-carousel-next');
    const imgs = box.querySelectorAll('.carousel-img');
    // Dots may be inside ig-carousel-dots or card-dots-row
    const dots = box.querySelectorAll('.card-dot');
    const postImg = document.getElementById(`post-img-${pid}`) as HTMLImageElement;

    let currentIdx = 0;
    const total = imgs.length;

    function updateCarousel() {
      imgs.forEach((img, idx) => {
        if (idx === currentIdx) {
          img.classList.add('active');
          if (postImg && img instanceof HTMLImageElement) {
            postImg.src = img.src;
          }
        } else {
          img.classList.remove('active');
        }
      });
      dots.forEach((dot, idx) => {
        if (idx === currentIdx) {
          dot.classList.add('active');
        } else {
          dot.classList.remove('active');
        }
      });

      if (prevBtn instanceof HTMLElement) {
        if (currentIdx === 0) {
          prevBtn.style.opacity = '0.3';
          prevBtn.style.pointerEvents = 'none';
        } else {
          prevBtn.style.opacity = '1';
          prevBtn.style.pointerEvents = 'auto';
        }
      }

      if (nextBtn instanceof HTMLElement) {
        if (currentIdx === total - 1) {
          nextBtn.style.opacity = '0.3';
          nextBtn.style.pointerEvents = 'none';
        } else {
          nextBtn.style.opacity = '1';
          nextBtn.style.pointerEvents = 'auto';
        }
      }
    }

    prevBtn?.addEventListener('click', (e) => {
      e.stopPropagation();
      if (currentIdx > 0) {
        currentIdx--;
        updateCarousel();
      }
    });

    nextBtn?.addEventListener('click', (e) => {
      e.stopPropagation();
      if (currentIdx < total - 1) {
        currentIdx++;
        updateCarousel();
      }
    });
  });

  // Setup scaling resize event
  window.addEventListener('resize', handleResize);
  
  // Initialize Presentation
  handleResize();
  goToSlide(0);

  // Focus window on load to ensure keyboard navigation works immediately
  window.focus();
});
