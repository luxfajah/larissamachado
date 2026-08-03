import re

ts_path = 'src/main.ts'
with open(ts_path, 'r', encoding='utf-8') as f:
    ts = f.read()

start_marker = '  // ==========================================================================\n  // INSTAGRAM STORIES FULLSCREEN MODAL INTERACTION'
end_marker = '  // Setup scaling resize event'

new_ts_code = '''  // ==========================================================================
  // INSTAGRAM STORIES FULLSCREEN MODAL INTERACTION (REAL IMAGES)
  // ==========================================================================
  const storiesModal = document.getElementById('instagram-stories-modal');
  const btnCloseStories = document.getElementById('btn-close-stories');
  const storyProgressRow = document.getElementById('story-progress-row');
  const storySlideContent = document.getElementById('story-slide-content');
  const storyTapLeft = document.getElementById('story-tap-left');
  const storyTapRight = document.getElementById('story-tap-right');

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
  let storyTimer: any = null;

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

    clearTimeout(storyTimer);
    storyTimer = setTimeout(() => {
      if (slideIdx < storyImgs.length - 1) {
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
    const storyImgs = storiesData[activeStoryKey];
    if (storyImgs && activeStorySlideIdx < storyImgs.length - 1) {
      activeStorySlideIdx++;
      renderStorySlide(activeStoryKey, activeStorySlideIdx);
    } else {
      closeStoriesModal();
    }
  });

  // ==========================================================================
  // INDIVIDUAL POST CAROUSELS HANDLER
  // ==========================================================================
  document.querySelectorAll('[data-post-carousel]').forEach(box => {
    const pid = box.getAttribute('data-post-carousel');
    const prevBtn = box.querySelector('.prev-card-btn');
    const nextBtn = box.querySelector('.next-card-btn');
    const imgs = box.querySelectorAll('.carousel-img');
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

'''

idx_start = ts.find(start_marker)
idx_end = ts.find(end_marker)

if idx_start != -1 and idx_end != -1:
    ts = ts[:idx_start] + new_ts_code + ts[idx_end:]
    with open(ts_path, 'w', encoding='utf-8') as f:
        f.write(ts)
    print('Updated src/main.ts successfully!')
else:
    print('Markers not found in main.ts!')
