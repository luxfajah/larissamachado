// ==========================================================================
// REAL 3D VIRTUAL FLIPBOOK ENGINE (20x20cm SQUARE PAGES)
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

let currentSpread = 0; // 0 to 8
let isTurning = false;

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

  // Render static spread layout
  function renderBook() {
    container.innerHTML = '';

    const book = document.createElement('div');
    book.className = 'real-flipbook-3d';

    // Left base page
    const leftBase = document.createElement('div');
    leftBase.className = 'page-leaf base-leaf left-leaf';
    const leftImg = getPageForSpread(currentSpread, 'left');
    if (leftImg) {
      const img = document.createElement('img');
      img.src = leftImg.src;
      img.alt = leftImg.title;
      leftBase.appendChild(img);
      leftBase.addEventListener('click', turnPrev);
    } else {
      leftBase.classList.add('blank-leaf');
    }

    // Right base page
    const rightBase = document.createElement('div');
    rightBase.className = 'page-leaf base-leaf right-leaf';
    const rightImg = getPageForSpread(currentSpread, 'right');
    if (rightImg) {
      const img = document.createElement('img');
      img.src = rightImg.src;
      img.alt = rightImg.title;
      rightBase.appendChild(img);
      rightBase.addEventListener('click', turnNext);
    } else {
      rightBase.classList.add('blank-leaf');
    }

    // Spine center shadow
    const spine = document.createElement('div');
    spine.className = 'book-3d-spine';

    book.appendChild(leftBase);
    book.appendChild(spine);
    book.appendChild(rightBase);
    container.appendChild(book);

    updateUI();
  }

  function getPageForSpread(spread, side) {
    if (spread === 0) {
      return side === 'right' ? bookletPages[0] : null;
    }
    if (spread === totalSpreads - 1) {
      return side === 'left' ? bookletPages[15] : null;
    }
    const leftIdx = (spread - 1) * 2 + 1;
    const rightIdx = leftIdx + 1;
    return side === 'left' ? bookletPages[leftIdx] : bookletPages[rightIdx];
  }

  // Turn to Next Spread with 3D Leaf Rotation
  function turnNext() {
    if (isTurning || currentSpread >= totalSpreads - 1) return;
    isTurning = true;

    const book = container.querySelector('.real-flipbook-3d');
    if (!book) return;

    // Create 3D turning leaf moving from Right (0deg) to Left (-180deg)
    const turnLeaf = document.createElement('div');
    turnLeaf.className = 'page-leaf turning-leaf turn-forward';

    const frontFace = document.createElement('div');
    frontFace.className = 'leaf-face leaf-front';
    const frontImg = getPageForSpread(currentSpread, 'right');
    if (frontImg) {
      const img = document.createElement('img');
      img.src = frontImg.src;
      frontFace.appendChild(img);
    }

    const backFace = document.createElement('div');
    backFace.className = 'leaf-face leaf-back';
    const backImg = getPageForSpread(currentSpread + 1, 'left');
    if (backImg) {
      const img = document.createElement('img');
      img.src = backImg.src;
      backFace.appendChild(img);
    }

    const leafShadow = document.createElement('div');
    leafShadow.className = 'turning-leaf-shadow';

    turnLeaf.appendChild(frontFace);
    turnLeaf.appendChild(backFace);
    turnLeaf.appendChild(leafShadow);
    book.appendChild(turnLeaf);

    // Trigger 3D rotation
    requestAnimationFrame(() => {
      turnLeaf.style.transform = 'rotateY(-180deg)';
    });

    setTimeout(() => {
      currentSpread++;
      renderBook();
      isTurning = false;
    }, 550);
  }

  // Turn to Prev Spread with 3D Leaf Rotation
  function turnPrev() {
    if (isTurning || currentSpread <= 0) return;
    isTurning = true;

    const book = container.querySelector('.real-flipbook-3d');
    if (!book) return;

    // Create 3D turning leaf moving from Left (-180deg) to Right (0deg)
    const turnLeaf = document.createElement('div');
    turnLeaf.className = 'page-leaf turning-leaf turn-backward';
    turnLeaf.style.transform = 'rotateY(-180deg)';

    const frontFace = document.createElement('div');
    frontFace.className = 'leaf-face leaf-front';
    const frontImg = getPageForSpread(currentSpread - 1, 'right');
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

    const leafShadow = document.createElement('div');
    leafShadow.className = 'turning-leaf-shadow';

    turnLeaf.appendChild(frontFace);
    turnLeaf.appendChild(backFace);
    turnLeaf.appendChild(leafShadow);
    book.appendChild(turnLeaf);

    // Trigger 3D rotation
    requestAnimationFrame(() => {
      turnLeaf.style.transform = 'rotateY(0deg)';
    });

    setTimeout(() => {
      currentSpread--;
      renderBook();
      isTurning = false;
    }, 550);
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
        counterEl.textContent = 'Capa Frontal (1 de 16)';
      } else if (currentSpread === totalSpreads - 1) {
        counterEl.textContent = 'Contra Capa (16 de 16)';
      } else {
        const p1 = (currentSpread - 1) * 2 + 2;
        const p2 = p1 + 1;
        counterEl.textContent = `Páginas ${p1} - ${p2} de 16`;
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
      label.textContent = idx === 0 ? 'Capa' : idx === 15 ? 'Verso' : `${idx}`;

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

  // Listeners
  if (prevBtn) prevBtn.onclick = turnPrev;
  if (nextBtn) nextBtn.onclick = turnNext;

  if (fullscreenBtn) {
    fullscreenBtn.onclick = () => {
      const slide = document.getElementById('slide-livreto');
      if (!document.fullscreenElement) {
        slide?.requestFullscreen();
      } else {
        document.exitFullscreen();
      }
    };
  }

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
