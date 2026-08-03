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
  // INSTAGRAM STORIES FULLSCREEN MODAL INTERACTION
  // ==========================================================================
  const storiesModal = document.getElementById('instagram-stories-modal');
  const btnCloseStories = document.getElementById('btn-close-stories');
  const storyProgressRow = document.getElementById('story-progress-row');
  const storySlideContent = document.getElementById('story-slide-content');
  const storyTapLeft = document.getElementById('story-tap-left');
  const storyTapRight = document.getElementById('story-tap-right');

  const storiesData = {
    '1': {
      title: 'Comece aqui',
      slides: [
        {
          tag: 'BOAS-VINDAS',
          heading: 'Oi! Sou a Dra. Larissa Machado',
          text: 'Oftalmologista especialista em Plástica Ocular em Atibaia/SP. Seja muito bem-vindo(a) ao meu perfil!',
          bg: './fotos-ilustrativas/6.jpg',
          cta: 'Conheça minha filosofia ➔'
        },
        {
          tag: 'ESPECIALIDADE',
          heading: 'O que é Plástica Ocular?',
          text: 'Uma especialidade médica que une saúde, função e estética palpebral. O objetivo é renovar o olhar preservando a sua essência natural.',
          bg: './fotos-ilustrativas/persona.jpg',
          cta: 'Ver procedimentos ➔'
        },
        {
          tag: 'CUIDADO INDIVIDUALIZADO',
          heading: 'Rejuvenescer sem exageros',
          text: 'Não prometemos milagres nem transformações artificiais. Tratamos ptose, blefaroplastia e patologias com rigor cirúrgico.',
          bg: './fotos-ilustrativas/3.jpg',
          cta: 'Agendar Consulta ➔'
        }
      ]
    },
    '2': {
      title: 'Onde atendo',
      slides: [
        {
          tag: 'LOCALIZAÇÃO',
          heading: 'Consultório em Atibaia / SP',
          text: 'Atendimento presencial personalizado em espaço moderno, acolhedor e com total infraestrutura para sua avaliação ocular.',
          bg: './fotos-ilustrativas/2.jpg',
          cta: 'Ver endereço no Google Maps ➔'
        },
        {
          tag: 'EXPERIÊNCIA',
          heading: 'Avaliação Funcional & Estética',
          text: 'Cada consulta é um momento de escuta atenta para entender o que mudou no seu olhar antes de indicar qualquer procedimento.',
          bg: './fotos-ilustrativas/5.jpg',
          cta: 'Falar com a equipe ➔'
        },
        {
          tag: 'AGENDAMENTO',
          heading: 'Horários & Consultas',
          text: 'Para agendar sua consulta, clique no link da bio ou envie uma mensagem direta no WhatsApp. Será um prazer receber você!',
          bg: './fotos-ilustrativas/persona.jpg',
          cta: 'Enviar Mensagem no WhatsApp ➔'
        }
      ]
    }
  };

  let activeStoryKey: '1' | '2' = '1';
  let activeStorySlideIdx = 0;
  let storyTimer: any = null;

  function renderStorySlide(storyKey: '1' | '2', slideIdx: number) {
    const story = storiesData[storyKey];
    if (!story || !story.slides[slideIdx]) return;
    const slide = story.slides[slideIdx];

    // Render Progress Bars
    if (storyProgressRow) {
      storyProgressRow.innerHTML = story.slides.map((_, idx) => `
        <div class="story-prog-bar">
          <div class="story-prog-fill" style="width: ${idx <= slideIdx ? '100%' : '0%'};"></div>
        </div>
      `).join('');
    }

    // Render Canvas Content
    if (storySlideContent) {
      storySlideContent.style.backgroundImage = `linear-gradient(to bottom, rgba(0,0,0,0.3) 0%, rgba(28,38,43,0.85) 100%), url('${slide.bg}')`;
      storySlideContent.innerHTML = `
        <div>
          <span class="story-title-tag">${slide.tag}</span>
          <h3 class="story-heading">${slide.heading}</h3>
        </div>
        <div class="story-text">${slide.text}</div>
        <div class="story-sticker-cta">${slide.cta}</div>
      `;
    }

    // Auto Advance after 5 seconds
    clearTimeout(storyTimer);
    storyTimer = setTimeout(() => {
      if (slideIdx < story.slides.length - 1) {
        activeStorySlideIdx++;
        renderStorySlide(storyKey, activeStorySlideIdx);
      } else {
        closeStoriesModal();
      }
    }, 5000);
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
    clearTimeout(storyTimer);
    if (storiesModal) {
      storiesModal.classList.remove('active');
    }
  }

  // Story Trigger Click Handlers (Highlights on iPhone & Strategy Buttons)
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

  storyTapLeft?.addEventListener('click', (e) => {
    e.stopPropagation();
    if (activeStorySlideIdx > 0) {
      activeStorySlideIdx--;
      renderStorySlide(activeStoryKey, activeStorySlideIdx);
    }
  });

  storyTapRight?.addEventListener('click', (e) => {
    e.stopPropagation();
    const story = storiesData[activeStoryKey];
    if (story && activeStorySlideIdx < story.slides.length - 1) {
      activeStorySlideIdx++;
      renderStorySlide(activeStoryKey, activeStorySlideIdx);
    } else {
      closeStoriesModal();
    }
  });

  // ==========================================================================
  // FEED & 6 POSTS INTERACTIVE VIEWER LOGIC (SLIDE 2)
  // ==========================================================================
  const postsData = [
    {
      category: 'CONTEÚDO 1 [PREPARAÇÃO DA AUDIÊNCIA]',
      badgeTag: 'Preparação',
      title: '“Você parece cansado?”',
      cards: [
        'Card 1: Quantas vezes você já ouviu “você parece cansado” num dia em que, teoricamente, estava tudo bem?',
        'Card 2: Talvez, você relacione isso ao sono (e, em alguns momentos, pode até que seja mesmo). Mas há um outro ponto interessante para olharmos: quando a pálpebra superior perde firmeza, ela lança uma sombra discreta sobre o olho e muda a expressão que o seu rosto transmite. O olhar fica pesado, sério, abatido, mesmo que você não esteja dessa forma...',
        'Card 3: Dar nome a isso é importante para saber qual é o melhor caminho a seguir, ou seja, não é você que está sempre cansado, é a estrutura da pálpebra que se transformou com o tempo. E entender o que acontece vem sempre antes de decidir se (e quando) algo precisa ser feito.',
        'Card 4: Você reconhece isso no seu olhar?'
      ],
      caption: `<p>A gente aprende a culpar o cansaço por tudo o que aparece no rosto, mas nem sempre ele é o culpado. Com o tempo, a pálpebra superior perde firmeza e passa a projetar uma sombra discreta sobre o olho e é essa sombra que muda a mensagem que o seu rosto transmite. O olhar comunica cansaço, seriedade, abatimento, mesmo quando por dentro é o oposto...</p><p>Por isso, aqui no consultório, a ordem é sempre essa: entender primeiro o que te trouxe até aqui e decidir depois a melhor intervenção.</p><p><strong>Dra. Larissa · Oftalmologia · Plástica Ocular · CRM 197872-SP</strong></p>`
    },
    {
      category: 'CONTEÚDO 2 [EDUCACIONAL]',
      badgeTag: 'Educacional',
      title: 'Perguntas no Consultório',
      cards: [
        'Card 1: As perguntas que você faria se estivesse sentada no consultório (e o que eu te responderia)',
        'Card 2: <strong>"Dói?"</strong> Durante, não: a cirurgia é feita com anestesia local e sedação, você não sente dor. Depois, há um desconforto leve e inchaço nos primeiros dias, controlados com o que a gente orienta. Nada que costume tirar o sono... ok?',
        'Card 3: <strong>"Preciso de anestesia geral?"</strong> Na maioria dos casos, não. A blefaroplastia costuma ser feita com anestesia local e uma sedação leve. Você vai para casa no mesmo dia.',
        'Card 4: <strong>"Vou ficar com aparência artificial?"</strong> Esse é o medo mais comum e eu entendo. O objetivo nunca é mudar o seu rosto, é aliviar o peso da pálpebra preservando a sua expressão. Ou seja, a renovação do olhar com a sua identidade!',
        'Card 5: <strong>"Quanto tempo até voltar à rotina?"</strong> A maior parte das pessoas retoma atividades leves em poucos dias. O inchaço e os hematomas melhoram ao longo das primeiras uma a duas semanas. Eu explico o passo a passo antes, para você se planejar sem surpresas.',
        'Card 6: <strong>"Como sei se é o meu caso?"</strong> Só a avaliação responde isso. Nem todo incômodo precisa de cirurgia, às vezes é função, às vezes é estética, às vezes é só entender o que mudou. O primeiro passo é sempre olhar com calma. Por isso, a consulta é fundamental para o melhor direcionamento.'
      ],
      caption: `<p>Toda semana, as mesmas perguntas aparecem no consultório. E faz todo sentido: ninguém decide nada sobre os próprios olhos sem antes tirar o medo do caminho.</p><p>Então, reuni aqui as dúvidas que mais escuto. Respondi cada uma como respondo pessoalmente: com a informação que você precisa para pensar com clareza.</p><p>Você vai reparar que não tem "resultado garantido" nem "transformação". Tem explicação. Porque a decisão é sua... O meu papel é fazer você entender antes de decidir.</p><p>Ficou alguma pergunta de fora? Pode me mandar que eu respondo.</p><p><strong>Dra. Larissa · Oftalmologia · Plástica Ocular · CRM 197872-SP</strong></p>`
    },
    {
      category: 'CONTEÚDO 3 [EDUCACIONAL]',
      badgeTag: 'Educacional',
      title: '“E a cicatriz?”',
      cards: [
        'Card 1: “E a cicatriz?” é quase sempre a primeira pergunta. Faz todo sentido: ninguém quer trocar um incômodo por uma marca...',
        'Card 2: Na blefaroplastia da pálpebra superior, a incisão é planejada dentro da dobra natural da pálpebra. Com o olho aberto, essa dobra se esconde e a cicatriz se esconde com ela. Ou seja, meu trabalho sempre busca respeitar a anatomia do seu rosto, com muita técnica.',
        'Card 3: Não existe cirurgia sem cicatriz, e eu não vou dizer o contrário. O que existe é uma marca planejada. Qual outro medo te trava na hora de pensar no assunto? Pode perguntar.'
      ],
      caption: `<p>Essa é uma pergunta clássica que merece um espaço só dela. Passa para o lado e confira os cards acima!</p><p><strong>Dra. Larissa · Oftalmologia · Plástica Ocular · CRM 197872-SP</strong></p>`
    },
    {
      category: 'CONTEÚDO 4 [LOCAL DE ATENDIMENTO]',
      badgeTag: 'Localização',
      title: 'Local de Atendimento',
      cards: [
        'Card 1: Meu local de atendimento: <br><br><a href="https://share.google/9v6BVUdKtrHndWnxr" target="_blank" style="color:#00376B; font-weight:bold;">share.google/9v6BVUdKtrHndWnxr</a>'
      ],
      caption: `<p>Este é o meu local de atendimento atualmente.</p><p>Para agendamento de consultas, clique diretamente no link da bio.</p><p><strong>Dra. Larissa · Oftalmologia · Plástica Ocular · CRM 197872-SP</strong></p>`
    },
    {
      category: 'CONTEÚDO 5 [APRESENTAÇÃO PROFISSIONAL]',
      badgeTag: 'Institucional',
      title: 'Seja Bem-Vindo(a)',
      cards: [
        'Card 1: Talvez você não tenha chegado aqui procurando uma cirurgia. E tudo bem, eu também não começo por ela. Sou a Dra. Larissa, oftalmologista especialista em Plástica Ocular. Meu trabalho é entender por que o seu olhar mudou antes de falar em qualquer procedimento.',
        'Card 2: Às vezes, o que incomoda é função: a pálpebra que pesa, o campo de visão que diminui. Às vezes, é a sensação de que o rosto parou de mostrar como você se sente. Quase sempre, as duas coisas caminhando juntas.',
        'Card 3: O que eu não faço: prometer juventude, vender cirurgia ou transformar você em outra pessoa. O objetivo nunca é mudar quem você é, mas fazer o seu olhar voltar a te representar, quando isso fizer sentido.',
        'Card 4: Se você chegou até aqui, seja bem-vindo(a).'
      ],
      caption: `<p>Seja oficialmente bem-vindo por aqui. Meu objetivo nesta página é trazer informação embasada para você que tem interesse na temática.</p><p>Qualquer dúvida, por favor, meu direct está aberto para conversarmos.</p><p><strong>Dra. Larissa · Oftalmologia · Plástica Ocular · CRM 197872-SP</strong></p>`
    },
    {
      category: 'CONTEÚDO 6 [EDUCACIONAL SOBRE PLÁSTICA OCULAR]',
      badgeTag: 'Patologias',
      title: 'Saúde & Função Ocular',
      cards: [
        'Card Único: A plástica ocular não é só estética, ela também pode tratar doenças que afetam a sua saúde ocular. Três delas aparecem com frequência no consultório: Ptose, Tumores Palpebrais e Obstrução das Vias Lacrimais.'
      ],
      caption: `<p>Muita gente associa cirurgia de pálpebra a rejuvenescimento, mas a plástica ocular também trata condições que afetam a saúde e o funcionamento dos seus olhos.</p><p><strong>Ptose:</strong> é a queda da pálpebra superior. Com o tempo, ou por questões congênitas e neurológicas, o músculo que sustenta a pálpebra enfraquece, e ela passa a cobrir parte do olho. O incômodo raramente é só estético: a ptose reduz o campo de visão, obriga você a levantar a sobrancelha o dia inteiro para enxergar e cansa. A cirurgia reposiciona a pálpebra na altura certa, devolvendo abertura ao olhar e conforto à visão.</p><p><strong>Tumores palpebrais:</strong> nem toda "verruguinha" ou nódulo na pálpebra é inofensivo. Existem lesões benignas, mas também tumores que precisam de atenção, inclusive alguns tipos de câncer de pele, que são comuns nessa região por causa da exposição solar. A plástica ocular cuida da remoção da lesão e da reconstrução da pálpebra, preservando tanto a função (proteção do olho) quanto a estética. Avaliar cedo faz toda a diferença.</p><p><strong>Obstrução das vias lacrimais:</strong> quando o canal que drena a lágrima entope, ela não tem para onde ir. O resultado é o olho lacrimejando o tempo todo, secreção e infecções que voltam sempre. Não é frescura nem "olho sensível": é um problema de drenagem com solução cirúrgica, que reconstrói o caminho da lágrima e resolve o incômodo de vez.</p><p>Se você se reconheceu em algum desses sinais, o primeiro passo é entender o que está acontecendo.</p><p><strong>Dra. Larissa · Oftalmologia · Plástica Ocular · CRM 197872-SP</strong></p>`
    }
  ];

  let currentActivePostIdx = 0;
  let currentCardIdx = 0;

  const pvCatBadge = document.getElementById('pv-cat-badge');
  const pvCardCounter = document.getElementById('pv-card-counter');
  const pvCardText = document.getElementById('pv-card-text');
  const pvCaptionText = document.getElementById('pv-caption-text');
  const pvDotsRow = document.getElementById('pv-dots-row');
  const pvBtnPrevCard = document.getElementById('pv-btn-prev-card');
  const pvBtnNextCard = document.getElementById('pv-btn-next-card');

  function renderPostViewer(postIdx: number, cardIdx: number) {
    const post = postsData[postIdx];
    if (!post) return;

    // Update Header Badges
    if (pvCatBadge) pvCatBadge.textContent = post.category;
    if (pvCardCounter) pvCardCounter.textContent = `Card ${cardIdx + 1} de ${post.cards.length}`;

    // Update Card Content
    if (pvCardText) pvCardText.innerHTML = post.cards[cardIdx] || '';

    // Update Caption Text
    if (pvCaptionText) pvCaptionText.innerHTML = post.caption;

    // Update Dots Indicator
    if (pvDotsRow) {
      pvDotsRow.innerHTML = post.cards.map((_, idx) => `
        <div class="card-dot ${idx === cardIdx ? 'active' : ''}"></div>
      `).join('');
    }

    // Disable/Enable Nav Arrows
    if (pvBtnPrevCard) {
      if (cardIdx === 0) {
        pvBtnPrevCard.style.opacity = '0.3';
        pvBtnPrevCard.style.pointerEvents = 'none';
      } else {
        pvBtnPrevCard.style.opacity = '1';
        pvBtnPrevCard.style.pointerEvents = 'auto';
      }
    }

    if (pvBtnNextCard) {
      if (cardIdx === post.cards.length - 1) {
        pvBtnNextCard.style.opacity = '0.3';
        pvBtnNextCard.style.pointerEvents = 'none';
      } else {
        pvBtnNextCard.style.opacity = '1';
        pvBtnNextCard.style.pointerEvents = 'auto';
      }
    }
  }

  // Feed Tile Click Handlers
  const postTiles = document.querySelectorAll('.feed-post-tile');
  postTiles.forEach(tile => {
    tile.addEventListener('click', (e) => {
      e.stopPropagation();
      const idxStr = tile.getAttribute('data-post-idx');
      if (idxStr !== null) {
        currentActivePostIdx = parseInt(idxStr, 10);
        currentCardIdx = 0;
        
        postTiles.forEach(t => t.classList.remove('active'));
        tile.classList.add('active');

        renderPostViewer(currentActivePostIdx, currentCardIdx);
      }
    });
  });

  // Card Navigation Arrows
  pvBtnPrevCard?.addEventListener('click', (e) => {
    e.stopPropagation();
    if (currentCardIdx > 0) {
      currentCardIdx--;
      renderPostViewer(currentActivePostIdx, currentCardIdx);
    }
  });

  pvBtnNextCard?.addEventListener('click', (e) => {
    e.stopPropagation();
    const post = postsData[currentActivePostIdx];
    if (post && currentCardIdx < post.cards.length - 1) {
      currentCardIdx++;
      renderPostViewer(currentActivePostIdx, currentCardIdx);
    }
  });

  // Initial Post Render
  renderPostViewer(0, 0);

  // Setup scaling resize event
  window.addEventListener('resize', handleResize);
  
  // Initialize Presentation
  handleResize();
  goToSlide(0);

  // Focus window on load to ensure keyboard navigation works immediately
  window.focus();
});
