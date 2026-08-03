css_path = 'src/index.css'
with open(css_path, 'r', encoding='utf-8') as f:
    css = f.read()

new_css_rules = """
/* ==========================================================================
   HERO PROFILE & INDIVIDUAL POST SLIDES STYLES
   ========================================================================== */

/* Hero Profile Page Layout (iPhone ~65% hero element) */
.hero-profile-layout {
  grid-template-columns: 480px 1fr !important;
  gap: 40px !important;
}

.hero-iphone-col {
  display: flex;
  justify-content: center;
  align-items: center;
}

.hero-iphone-frame {
  transform: scale(1.15);
  transform-origin: center;
  box-shadow: 0 30px 70px rgba(28, 38, 43, 0.28), 0 0 0 2px rgba(255, 255, 255, 0.15) !important;
}

.compact-strategy-list {
  gap: 12px !important;
}

.compact-strategy-list .strategy-card-item {
  padding: 12px 16px !important;
}

/* Individual Post Slide Layout */
.post-slide-layout {
  display: grid;
  grid-template-columns: 420px 1fr;
  gap: 36px;
  width: 100%;
  height: 100%;
  padding: 36px 48px;
  box-sizing: border-box;
  align-items: center;
}

.post-col-left {
  display: flex;
  justify-content: center;
  align-items: center;
  height: 100%;
}

.post-col-right {
  display: flex;
  flex-direction: column;
  justify-content: center;
  height: 100%;
  overflow-y: auto;
  padding-left: 10px;
}

.post-mockup-frame {
  transform: scale(1.08);
  transform-origin: center;
}

.ig-post-view {
  display: flex;
  flex-direction: column;
  height: 100%;
  background: #FFFFFF;
}

.ig-post-header {
  display: flex;
  align-items: center;
  padding: 8px 12px;
  gap: 8px;
  border-bottom: 1px solid rgba(0,0,0,0.05);
}

.ig-post-avatar {
  width: 28px;
  height: 28px;
  border-radius: 50%;
  object-fit: cover;
}

.ig-post-username {
  font-size: 13px;
  font-weight: 600;
  color: #000;
  flex: 1;
}

.ig-post-more {
  font-size: 11px;
  color: #8E8E8E;
  letter-spacing: 1px;
}

.ig-post-image-container {
  width: 100%;
  aspect-ratio: 1 / 1;
  background: #F0F0F0;
  display: flex;
  align-items: center;
  justify-content: center;
  overflow: hidden;
}

.ig-post-image-container img {
  width: 100%;
  height: 100%;
  object-fit: cover;
}

.ig-post-actions {
  display: flex;
  justify-content: space-between;
  align-items: center;
  padding: 8px 12px 4px 12px;
}

.ig-actions-left {
  display: flex;
  align-items: center;
  gap: 12px;
  color: #000;
}

.ig-actions-right {
  color: #000;
}

.ig-post-likes {
  padding: 0 12px;
  font-size: 12px;
  color: #000;
  margin-bottom: 4px;
}

.ig-post-caption-preview {
  padding: 0 12px 10px 12px;
  font-size: 11.5px;
  line-height: 1.4;
  color: #262626;
  white-space: nowrap;
  overflow: hidden;
  text-overflow: ellipsis;
}

.carousel-img {
  display: none;
  width: 100%;
  max-height: 380px;
  object-fit: contain;
  border-radius: 8px;
}

.carousel-img.active {
  display: block;
}

.card-display-viewport {
  width: 100%;
  display: flex;
  justify-content: center;
  align-items: center;
  min-height: 280px;
  background: #FAFAFA;
  border-radius: 8px;
  padding: 8px;
  box-sizing: border-box;
}

"""

if "/* HERO PROFILE & INDIVIDUAL POST SLIDES STYLES */" not in css:
    with open(css_path, 'a', encoding='utf-8') as f:
        f.write("\n" + new_css_rules)
    print('Appended CSS rules successfully!')
else:
    print('CSS rules already exist.')
