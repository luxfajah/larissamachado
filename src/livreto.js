// ==========================================================================
// LIVRETO VIRTUAL INTERATIVO 3D (20x20cm SQUARE FLIPBOOK)
// ==========================================================================

export const bookletPages = [
  { src: './livreto/Capa.jpg', title: 'Capa Frontal' },
  { src: './livreto/Verso capa.jpg', title: 'Verso da Capa' },
  { src: './livreto/1.jpg', title: 'Página 01' },
  { src: './livreto/2.jpg', title: 'Página 02' },
  { src: './livreto/3.jpg', title: 'Página 03' },
  { src: './livreto/4.jpg', title: 'Página 04' },
  { src: './livreto/5.jpg', title: 'Página 05' },
  { src: './livreto/6.jpg', title: 'Página 06' },
  { src: './livreto/7.jpg', title: 'Página 07' },
  { src: './livreto/8.jpg', title: 'Página 08' },
  { src: './livreto/9.jpg', title: 'Página 09' },
  { src: './livreto/10.jpg', title: 'Página 10' },
  { src: './livreto/11.jpg', title: 'Página 11' },
  { src: './livreto/12.jpg', title: 'Página 12' },
  { src: './livreto/Frente Contra Capa.jpg', title: 'Frente Contra Capa' },
  { src: './livreto/Contra Capa.jpg', title: 'Contra Capa' },
];

let currentSpreadIndex = 0; // Spread 0 = Capa, Spread 1 = Pág 1-2, etc.

export function initFlipbook() {
  const container = document.getElementById('flipbook-viewport');
  const prevBtn = document.getElementById('flipbook-prev');
  const nextBtn = document.getElementById('flipbook-next');
  const counterEl = document.getElementById('flipbook-counter');
  const fullscreenBtn = document.getElementById('flipbook-fullscreen');
  const thumbsToggleBtn = document.getElementById('flipbook-thumbs-toggle');
  const thumbsDrawer = document.getElementById('flipbook-thumbs-drawer');
  const thumbsList = document.getElementById('flipbook-thumbs-list');

  if (!container) return;

  const totalSpreads = 9;

  function renderSpread(spreadIndex, isAnimated = true) {
    currentSpreadIndex = Math.max(0, Math.min(spreadIndex, totalSpreads - 1));

    // Clear viewport
    container.innerHTML = '';

    const stage = document.createElement('div');
    stage.className = 'flipbook-book-stage';
    if (isAnimated) {
      stage.classList.add('flipbook-turn-anim');
    }

    const spineShadow = document.createElement('div');
    spineShadow.className = 'flipbook-spine-shadow';

    // Left Page Index
    let leftIndex = null;
    let rightIndex = null;

    if (currentSpreadIndex === 0) {
      leftIndex = null;
      rightIndex = 0; // Capa
    } else if (currentSpreadIndex === totalSpreads - 1) {
      leftIndex = 15; // Contra Capa
      rightIndex = null;
    } else {
      leftIndex = (currentSpreadIndex - 1) * 2 + 1;
      rightIndex = leftIndex + 1;
    }

    // Render Left Page
    const leftPage = document.createElement('div');
    leftPage.className = `flipbook-page left-page ${leftIndex === null ? 'empty-page' : ''}`;
    if (leftIndex !== null && bookletPages[leftIndex]) {
      const img = document.createElement('img');
      img.src = bookletPages[leftIndex].src;
      img.alt = bookletPages[leftIndex].title;
      leftPage.appendChild(img);

      // Page click to turn prev
      leftPage.addEventListener('click', () => {
        if (currentSpreadIndex > 0) renderSpread(currentSpreadIndex - 1);
      });
    }

    // Render Right Page
    const rightPage = document.createElement('div');
    rightPage.className = `flipbook-page right-page ${rightIndex === null ? 'empty-page' : ''}`;
    if (rightIndex !== null && bookletPages[rightIndex]) {
      const img = document.createElement('img');
      img.src = bookletPages[rightIndex].src;
      img.alt = bookletPages[rightIndex].title;
      rightPage.appendChild(img);

      // Page click to turn next
      rightPage.addEventListener('click', () => {
        if (currentSpreadIndex < totalSpreads - 1) renderSpread(currentSpreadIndex + 1);
      });
    }

    stage.appendChild(leftPage);
    stage.appendChild(spineShadow);
    stage.appendChild(rightPage);
    container.appendChild(stage);

    // Update Counter & Controls
    updateControls();
    highlightThumbnail();
  }

  function updateControls() {
    if (prevBtn) prevBtn.disabled = currentSpreadIndex === 0;
    if (nextBtn) nextBtn.disabled = currentSpreadIndex === totalSpreads - 1;

    if (counterEl) {
      if (currentSpreadIndex === 0) {
        counterEl.textContent = 'Capa Frontal (1 de 16)';
      } else if (currentSpreadIndex === totalSpreads - 1) {
        counterEl.textContent = 'Contra Capa (16 de 16)';
      } else {
        const p1 = (currentSpreadIndex - 1) * 2 + 2;
        const p2 = p1 + 1;
        counterEl.textContent = `Páginas ${p1} - ${p2} de 16`;
      }
    }
  }

  // Thumbnails render
  if (thumbsList && thumbsList.children.length === 0) {
    bookletPages.forEach((page, idx) => {
      const thumb = document.createElement('div');
      thumb.className = 'flipbook-thumb-item';
      thumb.dataset.pageIndex = idx;
      
      const img = document.createElement('img');
      img.src = page.src;
      img.alt = page.title;
      
      const label = document.createElement('span');
      label.textContent = idx === 0 ? 'Capa' : idx === 15 ? 'Verso' : `${idx}`;

      thumb.appendChild(img);
      thumb.appendChild(label);

      thumb.addEventListener('click', () => {
        let targetSpread = 0;
        if (idx === 0) targetSpread = 0;
        else if (idx === 15) targetSpread = totalSpreads - 1;
        else targetSpread = Math.floor((idx - 1) / 2) + 1;

        renderSpread(targetSpread);
      });

      thumbsList.appendChild(thumb);
    });
  }

  function highlightThumbnail() {
    if (!thumbsList) return;
    const items = thumbsList.querySelectorAll('.flipbook-thumb-item');
    items.forEach((item) => item.classList.remove('active'));

    let activePageIdx = 0;
    if (currentSpreadIndex === 0) activePageIdx = 0;
    else if (currentSpreadIndex === totalSpreads - 1) activePageIdx = 15;
    else activePageIdx = (currentSpreadIndex - 1) * 2 + 1;

    const targetThumb = thumbsList.querySelector(`[data-page-index="${activePageIdx}"]`);
    if (targetThumb) {
      targetThumb.classList.add('active');
      targetThumb.scrollIntoView({ behavior: 'smooth', block: 'nearest', inline: 'center' });
    }
  }

  // Event Listeners
  if (prevBtn) {
    prevBtn.addEventListener('click', () => {
      if (currentSpreadIndex > 0) renderSpread(currentSpreadIndex - 1);
    });
  }

  if (nextBtn) {
    nextBtn.addEventListener('click', () => {
      if (currentSpreadIndex < totalSpreads - 1) renderSpread(currentSpreadIndex + 1);
    });
  }

  if (fullscreenBtn) {
    fullscreenBtn.addEventListener('click', () => {
      const flipbookSlide = document.getElementById('slide-livreto');
      if (!document.fullscreenElement) {
        if (flipbookSlide && flipbookSlide.requestFullscreen) {
          flipbookSlide.requestFullscreen();
        }
      } else {
        if (document.exitFullscreen) {
          document.exitFullscreen();
        }
      }
    });
  }

  if (thumbsToggleBtn && thumbsDrawer) {
    thumbsToggleBtn.addEventListener('click', () => {
      thumbsDrawer.classList.toggle('open');
      thumbsToggleBtn.classList.toggle('active');
    });
  }

  // Keyboard navigation
  window.addEventListener('keydown', (e) => {
    const flipbookSlide = document.getElementById('slide-livreto');
    if (!flipbookSlide || !flipbookSlide.classList.contains('active')) return;

    if (e.key === 'ArrowLeft') {
      if (currentSpreadIndex > 0) renderSpread(currentSpreadIndex - 1);
    } else if (e.key === 'ArrowRight') {
      if (currentSpreadIndex < totalSpreads - 1) renderSpread(currentSpreadIndex + 1);
    }
  });

  // Initial render
  renderSpread(0, false);
}
