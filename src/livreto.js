// ==========================================================================
// REALISTIC 3D VIRTUAL FLIPBOOK ENGINE (COVVER.COM FULLSCREEN & 3D EFFECTS)
// ==========================================================================

export const bookletPages = [
  { src: './livreto/Capa.jpg', title: 'Capa Frontal (Pág 01)', pageNum: 1 },
  { src: './livreto/Verso capa.jpg', title: 'Verso da Capa (Pág 02)', pageNum: 2 },
  { src: './livreto/1.jpg', title: 'Página 03', pageNum: 3 },
  { src: './livreto/2.jpg', title: 'Página 04', pageNum: 4 },
  { src: './livreto/3.jpg', title: 'Página 05', pageNum: 5 },
  { src: './livreto/4.jpg', title: 'Página 06', pageNum: 6 },
  { src: './livreto/5.jpg', title: 'Página 07', pageNum: 7 },
  { src: './livreto/6.jpg', title: 'Página 08', pageNum: 8 },
  { src: './livreto/7.jpg', title: 'Página 09', pageNum: 9 },
  { src: './livreto/8.jpg', title: 'Página 10', pageNum: 10 },
  { src: './livreto/9.jpg', title: 'Página 11', pageNum: 11 },
  { src: './livreto/10.jpg', title: 'Página 12', pageNum: 12 },
  { src: './livreto/11.jpg', title: 'Página 13', pageNum: 13 },
  { src: './livreto/12.jpg', title: 'Página 14', pageNum: 14 },
  { src: './livreto/Frente Contra Capa.jpg', title: 'Frente Contra Capa (Pág 15)', pageNum: 15 },
  { src: './livreto/Contra Capa.jpg', title: 'Contra Capa (Pág 16)', pageNum: 16 },
];

// Spreads:
// Spread 0: Left = null, Right = Page 0 (Capa.jpg) -> Closed Front
// Spread 1: Left = Page 1 (Verso capa), Right = Page 2 (1.jpg) [Págs 2-3]
// Spread 2: Left = Page 3 (2.jpg), Right = Page 4 (3.jpg) [Págs 4-5]
// Spread 3: Left = Page 5 (4.jpg), Right = Page 6 (5.jpg) [Págs 6-7]
// Spread 4: Left = Page 7 (6.jpg), Right = Page 8 (7.jpg) [Págs 8-9]
// Spread 5: Left = Page 9 (8.jpg), Right = Page 10 (9.jpg) [Págs 10-11]
// Spread 6: Left = Page 11 (10.jpg), Right = Page 12 (11.jpg) [Págs 12-13]
// Spread 7: Left = Page 13 (12.jpg), Right = Page 14 (Frente Contra Capa) [Págs 14-15]
// Spread 8: Left = Page 15 (Contra Capa), Right = null -> Closed Back

let currentSpread = 0; // 0 to 8
let isTurning = false;
let isZoomed = false;
let showPrintGrid = false;

export function initFlipbook() {
  const container = document.getElementById('flipbook-viewport');
  const prevBtn = document.getElementById('flipbook-prev');
  const nextBtn = document.getElementById('flipbook-next');
  const counterEl = document.getElementById('flipbook-counter');
  const fullscreenBtn = document.getElementById('flipbook-fullscreen');
  const zoomBtn = document.getElementById('flipbook-zoom');
  const gridToggleBtn = document.getElementById('flipbook-grid-toggle');
  const thumbsToggleBtn = document.getElementById('flipbook-thumbs-toggle');
  const thumbsDrawer = document.getElementById('flipbook-thumbs-drawer');
  const thumbsList = document.getElementById('flipbook-thumbs-list');

  if (!container) return;

  const totalSpreads = 9;

  function renderBook() {
    container.innerHTML = '';

    const book = document.createElement('div');
    book.className = `real-flipbook-3d ${currentSpread === 0 ? 'is-closed-front' : ''} ${currentSpread === totalSpreads - 1 ? 'is-closed-back' : ''} ${isZoomed ? 'is-zoomed' : ''} ${showPrintGrid ? 'show-print-guides' : ''}`;

    if (currentSpread === 0) {
      // CLOSED FRONT COVER: Single Cover Page Centered
      const coverLeaf = document.createElement('div');
      coverLeaf.className = 'page-leaf single-cover-leaf right-leaf cover-closed';
      const img = document.createElement('img');
      img.src = bookletPages[0].src;
      img.alt = bookletPages[0].title;
      coverLeaf.appendChild(img);
      
      const clickBadge = document.createElement('div');
      clickBadge.className = 'cover-open-badge';
      clickBadge.innerHTML = '<span>Clique para abrir o livreto</span> →';
      coverLeaf.appendChild(clickBadge);

      addPrintGuides(coverLeaf);

      coverLeaf.addEventListener('click', turnNext);
      book.appendChild(coverLeaf);
    } else if (currentSpread === totalSpreads - 1) {
      // CLOSED BACK COVER: Single Back Cover Centered
      const backLeaf = document.createElement('div');
      backLeaf.className = 'page-leaf single-cover-leaf left-leaf cover-closed';
      const img = document.createElement('img');
      img.src = bookletPages[15].src;
      img.alt = bookletPages[15].title;
      backLeaf.appendChild(img);

      addPrintGuides(backLeaf);

      backLeaf.addEventListener('click', turnPrev);
      book.appendChild(backLeaf);
    } else {
      // OPEN BOOK: Dual Pages Side-by-Side (20x20cm Spread)
      const leftBase = document.createElement('div');
      leftBase.className = 'page-leaf base-leaf left-leaf';
      const leftImg = getPageForSpread(currentSpread, 'left');
      if (leftImg) {
        const img = document.createElement('img');
        img.src = leftImg.src;
        img.alt = leftImg.title;
        leftBase.appendChild(img);
        addPrintGuides(leftBase);
        leftBase.addEventListener('click', turnPrev);
      }

      const rightBase = document.createElement('div');
      rightBase.className = 'page-leaf base-leaf right-leaf';
      const rightImg = getPageForSpread(currentSpread, 'right');
      if (rightImg) {
        const img = document.createElement('img');
        img.src = rightImg.src;
        img.alt = rightImg.title;
        rightBase.appendChild(img);
        addPrintGuides(rightBase);
        rightBase.addEventListener('click', turnNext);
      }

      const spine = document.createElement('div');
      spine.className = 'book-3d-spine';

      book.appendChild(leftBase);
      book.appendChild(spine);
      book.appendChild(rightBase);
    }

    container.appendChild(book);
    updateUI();
  }

  function addPrintGuides(pageEl) {
    const bleedOverlay = document.createElement('div');
    bleedOverlay.className = 'print-bleed-overlay';
    bleedOverlay.innerHTML = '<span class="bleed-label">Sangria 3mm</span>';
    pageEl.appendChild(bleedOverlay);
  }

  function getPageForSpread(spread, side) {
    if (spread <= 0 || spread >= totalSpreads - 1) return null;
    const leftIdx = (spread - 1) * 2 + 1;
    const rightIdx = leftIdx + 1;
    return side === 'left' ? bookletPages[leftIdx] : bookletPages[rightIdx];
  }

  // Realistic 3D Turn Next
  function turnNext() {
    if (isTurning || currentSpread >= totalSpreads - 1) return;
    isTurning = true;

    const book = container.querySelector('.real-flipbook-3d');
    if (!book) return;

    const turnLeaf = document.createElement('div');
    turnLeaf.className = 'page-leaf turning-leaf turn-forward';

    const frontFace = document.createElement('div');
    frontFace.className = 'leaf-face leaf-front';
    const frontImg = currentSpread === 0 ? bookletPages[0] : getPageForSpread(currentSpread, 'right');
    if (frontImg) {
      const img = document.createElement('img');
      img.src = frontImg.src;
      frontFace.appendChild(img);
    }

    const backFace = document.createElement('div');
    backFace.className = 'leaf-face leaf-back';
    const backImg = getPageForSpread(currentSpread + 1, 'left') || bookletPages[15];
    if (backImg) {
      const img = document.createElement('img');
      img.src = backImg.src;
      backFace.appendChild(img);
    }

    const shadow = document.createElement('div');
    shadow.className = 'turning-leaf-shadow';

    turnLeaf.appendChild(frontFace);
    turnLeaf.appendChild(backFace);
    turnLeaf.appendChild(shadow);
    book.appendChild(turnLeaf);

    // Covver style 3D curl animation
    requestAnimationFrame(() => {
      turnLeaf.style.transform = 'rotateY(-180deg) scale(0.98)';
      setTimeout(() => {
        turnLeaf.style.transform = 'rotateY(-180deg) scale(1)';
      }, 300);
    });

    setTimeout(() => {
      currentSpread++;
      renderBook();
      isTurning = false;
    }, 600);
  }

  // Realistic 3D Turn Prev
  function turnPrev() {
    if (isTurning || currentSpread <= 0) return;
    isTurning = true;

    const book = container.querySelector('.real-flipbook-3d');
    if (!book) return;

    const turnLeaf = document.createElement('div');
    turnLeaf.className = 'page-leaf turning-leaf turn-backward';
    turnLeaf.style.transform = 'rotateY(-180deg)';

    const frontFace = document.createElement('div');
    frontFace.className = 'leaf-face leaf-front';
    const frontImg = getPageForSpread(currentSpread - 1, 'right') || bookletPages[0];
    if (frontImg) {
      const img = document.createElement('img');
      img.src = frontImg.src;
      frontFace.appendChild(img);
    }

    const backFace = document.createElement('div');
    backFace.className = 'leaf-face leaf-back';
    const backImg = getPageForSpread(currentSpread, 'left');
    if (backImg) {
      const img = document.createElement('img');
      img.src = backImg.src;
      backFace.appendChild(img);
    }

    const shadow = document.createElement('div');
    shadow.className = 'turning-leaf-shadow';

    turnLeaf.appendChild(frontFace);
    turnLeaf.appendChild(backFace);
    turnLeaf.appendChild(shadow);
    book.appendChild(turnLeaf);

    requestAnimationFrame(() => {
      turnLeaf.style.transform = 'rotateY(0deg) scale(0.98)';
      setTimeout(() => {
        turnLeaf.style.transform = 'rotateY(0deg) scale(1)';
      }, 300);
    });

    setTimeout(() => {
      currentSpread--;
      renderBook();
      isTurning = false;
    }, 600);
  }

  function goToSpread(targetSpread) {
    if (isTurning || targetSpread === currentSpread) return;
    currentSpread = Math.max(0, Math.min(targetSpread, totalSpreads - 1));
    renderBook();
  }

  function updateUI() {
    if (prevBtn) prevBtn.disabled = currentSpread === 0;
    if (nextBtn) nextBtn.disabled = currentSpread === totalSpreads - 1;

    if (counterEl) {
      if (currentSpread === 0) {
        counterEl.textContent = 'Livreto Fechado • Capa (Pág. 01)';
      } else if (currentSpread === totalSpreads - 1) {
        counterEl.textContent = 'Livreto Fechado • Contra Capa (Pág. 16)';
      } else {
        const leftPageNum = (currentSpread - 1) * 2 + 2;
        const rightPageNum = leftPageNum + 1;
        counterEl.textContent = `Páginas ${leftPageNum} - ${rightPageNum} de 16`;
      }
    }

    highlightThumb();
  }

  // Thumbnails List
  if (thumbsList && thumbsList.children.length === 0) {
    bookletPages.forEach((page, idx) => {
      const item = document.createElement('div');
      item.className = 'flipbook-thumb-item';
      item.dataset.pageIdx = idx;

      const img = document.createElement('img');
      img.src = page.src;
      img.alt = page.title;

      const label = document.createElement('span');
      label.textContent = idx === 0 ? 'Capa' : idx === 15 ? 'Verso' : `Pág ${idx + 1}`;

      item.appendChild(img);
      item.appendChild(label);

      item.addEventListener('click', () => {
        let spread = 0;
        if (idx === 0) spread = 0;
        else if (idx === 15) spread = totalSpreads - 1;
        else spread = Math.floor((idx - 1) / 2) + 1;

        goToSpread(spread);
      });

      thumbsList.appendChild(item);
    });
  }

  function highlightThumb() {
    if (!thumbsList) return;
    const items = thumbsList.querySelectorAll('.flipbook-thumb-item');
    items.forEach((it) => it.classList.remove('active'));

    let activeIdx = 0;
    if (currentSpread === 0) activeIdx = 0;
    else if (currentSpread === totalSpreads - 1) activeIdx = 15;
    else activeIdx = (currentSpread - 1) * 2 + 1;

    const activeItem = thumbsList.querySelector(`[data-page-idx="${activeIdx}"]`);
    if (activeItem) {
      activeItem.classList.add('active');
      activeItem.scrollIntoView({ behavior: 'smooth', block: 'nearest', inline: 'center' });
    }
  }

  // Event Listeners
  if (prevBtn) prevBtn.onclick = turnPrev;
  if (nextBtn) nextBtn.onclick = turnNext;

  if (zoomBtn) {
    zoomBtn.onclick = () => {
      isZoomed = !isZoomed;
      zoomBtn.classList.toggle('active', isZoomed);
      const book = container.querySelector('.real-flipbook-3d');
      if (book) {
        book.classList.toggle('is-zoomed', isZoomed);
      }
    };
  }

  if (gridToggleBtn) {
    gridToggleBtn.onclick = () => {
      showPrintGrid = !showPrintGrid;
      gridToggleBtn.classList.toggle('active', showPrintGrid);
      const book = container.querySelector('.real-flipbook-3d');
      if (book) {
        book.classList.toggle('show-print-guides', showPrintGrid);
      }
    };
  }

  // Fullscreen Handler
  if (fullscreenBtn) {
    fullscreenBtn.onclick = () => {
      const slide = document.getElementById('slide-livreto');
      if (!slide) return;

      if (!document.fullscreenElement) {
        if (slide.requestFullscreen) {
          slide.requestFullscreen();
        } else if (slide.webkitRequestFullscreen) {
          slide.webkitRequestFullscreen();
        }
      } else {
        if (document.exitFullscreen) {
          document.exitFullscreen();
        } else if (document.webkitExitFullscreen) {
          document.webkitExitFullscreen();
        }
      }
    };
  }

  const onFullscreenChange = () => {
    const slide = document.getElementById('slide-livreto');
    if (!slide) return;
    if (document.fullscreenElement === slide || document.webkitFullscreenElement === slide) {
      slide.classList.add('is-fullscreen');
    } else {
      slide.classList.remove('is-fullscreen');
    }
  };

  document.addEventListener('fullscreenchange', onFullscreenChange);
  document.addEventListener('webkitfullscreenchange', onFullscreenChange);

  if (thumbsToggleBtn && thumbsDrawer) {
    thumbsToggleBtn.onclick = () => {
      thumbsDrawer.classList.toggle('open');
      thumbsToggleBtn.classList.toggle('active');
    };
  }

  window.addEventListener('keydown', (e) => {
    const slide = document.getElementById('slide-livreto');
    if (!slide || !slide.classList.contains('active')) return;
    if (e.key === 'ArrowLeft') turnPrev();
    if (e.key === 'ArrowRight') turnNext();
  });

  renderBook();
}
