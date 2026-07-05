from pathlib import Path
import re

root = Path(r"c:\Users\Hiikey\Videos\brunzal")
html_files = list(root.glob('*.html'))
menu_old = re.compile(
    r'<li class="menu-item-has-children"><a href="#">Blog</a>\s*<ul class="sub-menu">\s*'
    r'<li><a href="blog.html">Blog List</a></li>\s*'
    r'<li><a href="blog-2.html">Blog Grid</a></li>\s*'
    r'<li><a href="blog-details.html">Insight Details</a></li>\s*'
    r'</ul>\s*</li>',
    re.M,
)
menu_new = '<li><a href="blog.html">Blog</a></li>'
for path in html_files:
    text = path.read_text(encoding='utf-8')
    if menu_old.search(text):
        text = menu_old.sub(menu_new, text)
        path.write_text(text, encoding='utf-8')
        print(f'Updated menu in {path.name}')

blog = root / 'blog.html'
text = blog.read_text(encoding='utf-8')
start = text.find('                    <div class="row gy-80">')
end = text.find('                    <div class="pagination__wrap mt-60">', start)
if start == -1 or end == -1:
    raise RuntimeError('Cannot find blog post section markers in blog.html')
new_posts = '''                    <div class="row gy-80">
                        <div class="col-12">
                            <div class="blog__post-item list-style">
                                <div class="blog__post-thumb">
                                    <a href="blog-details.html"><img src="assets/img/blog/blog-s-1-1.jpg" alt="img"></a>
                                </div>
                                <div class="blog__post-meta">
                                    <ul class="list-wrap">
                                        <li>
                                            <a href="blog-details.html">
                                                <img src="assets/img/blog/blog-author-1-1.jpg" alt="img">
                                            </a>
                                            <div class="content">
                                                <p>EquiRise</p>
                                                <a href="blog-details.html">by EquiRise</a>
                                            </div>
                                        </li>
                                        <li>
                                            <div class="content">
                                                <p>Published</p>
                                                <a href="blog-details.html">April 12, 2025</a>
                                            </div>
                                        </li>
                                        <li>
                                            <div class="content">
                                                <p>Discussion</p>
                                                <a href="blog-details.html">Join the community</a>
                                            </div>
                                        </li>
                                        <li>
                                            <div class="content">
                                                <p>Read</p>
                                                <a href="blog-details.html">13,245 views</a>
                                            </div>
                                        </li>
                                    </ul>
                                </div>
                                <div class="blog__post-content">
                                    <h3 class="title"><a href="blog-details.html">Strengthening Inclusive Institutional Systems</a></h3>
                                    <p class="text">How EquiRise supports governance, leadership, and efficiency in institutions to deliver equitable and sustainable services.</p>
                                    <div class="blog__post-bottom">
                                        <a href="blog-details.html" class="btn btn-three">Continue reading</a>
                                    </div>
                                </div>
                            </div>
                        </div>
                        <div class="col-12">
                            <div class="blog__post-item list-style">
                                <div class="blog__post-thumb">
                                    <a href="blog-details-2.html"><img src="assets/img/blog/blog-s-1-2.jpg" alt="img"></a>
                                    <a href="https://www.youtube.com/watch?v=vvNwlRLjLkU" class="vid-play-btn popup-video">
                                        <div class="fas fa-play"></div>
                                    </a>
                                </div>
                                <div class="blog__post-meta">
                                    <ul class="list-wrap">
                                        <li>
                                            <a href="blog-details-2.html">
                                                <img src="assets/img/blog/blog-author-1-2.jpg" alt="img">
                                            </a>
                                            <div class="content">
                                                <p>EquiRise</p>
                                                <a href="blog-details-2.html">by EquiRise</a>
                                            </div>
                                        </li>
                                        <li>
                                            <div class="content">
                                                <p>Published</p>
                                                <a href="blog-details-2.html">May 3, 2025</a>
                                            </div>
                                        </li>
                                        <li>
                                            <div class="content">
                                                <p>Discussion</p>
                                                <a href="blog-details-2.html">Join the community</a>
                                            </div>
                                        </li>
                                        <li>
                                            <div class="content">
                                                <p>Read</p>
                                                <a href="blog-details-2.html">8,930 views</a>
                                            </div>
                                        </li>
                                    </ul>
                                </div>
                                <div class="blog__post-content">
                                    <h3 class="title"><a href="blog-details-2.html">Delivering Climate Resilience Through Local Partnerships</a></h3>
                                    <p class="text">A practical look at how community partnerships and institutional support build resilient systems for climate adaptation.</p>
                                    <div class="blog__post-bottom">
                                        <a href="blog-details-2.html" class="btn btn-three">Continue reading</a>
                                    </div>
                                </div>
                            </div>
                        </div>
                        <div class="col-12">
                            <div class="blog__post-item list-style">
                                <div class="blog__post-thumb tg-swiper__slider" id="blogSlider" data-swiper-options='{"loop": true, "autoplay": { "delay": 1000 }}'>
                                    <div class="swiper-wrapper">
                                        <div class="swiper-slide">
                                            <a href="blog-details-3.html"><img src="assets/img/blog/blog-s-1-1.jpg" alt="Blog_Image"></a>
                                        </div>
                                        <div class="swiper-slide">
                                            <a href="blog-details-3.html"><img src="assets/img/blog/blog-s-1-2.jpg" alt="Blog_Image"></a>
                                        </div>
                                        <div class="swiper-slide">
                                            <a href="blog-details-3.html"><img src="assets/img/blog/blog-s-1-3.jpg" alt="Blog_Image"></a>
                                        </div>
                                    </div>
                                    <div class="slider-arrows">
                                        <button data-slider-prev="#blogSlider" class="slider-arrow slider-prev">
                                            <svg width="8" height="14" viewBox="0 0 8 14" fill="none" xmlns="http://www.w3.org/2000/svg">
                                            <path d="M6.375 13L1.43561 8.06061C0.852272 7.47727 0.852272 6.52273 1.43561 5.93939L6.375 1" stroke="currentcolor" stroke-width="2" stroke-miterlimit="10" stroke-linecap="round" stroke-linejoin="round"/>
                                            </svg>
                                        </button>
                                        <button data-slider-next="#blogSlider" class="slider-arrow slider-next">
                                            <svg width="8" height="14" viewBox="0 0 8 14" fill="none" xmlns="http://www.w3.org/2000/svg">
                                                <path d="M1.625 13L6.56439 8.06061C7.14773 7.47727 7.14773 6.52273 6.56439 5.93939L1.625 1" stroke="currentcolor" stroke-width="2" stroke-miterlimit="10" stroke-linecap="round" stroke-linejoin="round"/>
                                            </svg>
                                        </button>
                                    </div>
                                </div>
                                <div class="blog__post-meta">
                                    <ul class="list-wrap">
                                        <li>
                                            <a href="blog-details-3.html">
                                                <img src="assets/img/blog/blog-author-1-3.jpg" alt="img">
                                            </a>
                                            <div class="content">
                                                <p>EquiRise</p>
                                                <a href="blog-details-3.html">by EquiRise</a>
                                            </div>
                                        </li>
                                        <li>
                                            <div class="content">
                                                <p>Published</p>
                                                <a href="blog-details-3.html">June 1, 2025</a>
                                            </div>
                                        </li>
                                        <li>
                                            <div class="content">
                                                <p>Discussion</p>
                                                <a href="blog-details-3.html">Join the community</a>
                                            </div>
                                        </li>
                                        <li>
                                            <div class="content">
                                                <p>Read</p>
                                                <a href="blog-details-3.html">11,120 views</a>
                                            </div>
                                        </li>
                                    </ul>
                                </div>
                                <div class="blog__post-content">
                                    <h3 class="title"><a href="blog-details-3.html">Transforming Procurement and Supply Chain Governance</a></h3>
                                    <p class="text">Insights on building transparent procurement systems that improve accountability and value across public and private sectors.</p>
                                    <div class="blog__post-bottom">
                                        <a href="blog-details-3.html" class="btn btn-three">Continue reading</a>
                                    </div>
                                </div>
                            </div>
                        </div>
                        <div class="col-12">
                            <div class="blog__post-item list-style">
                                <div class="blog__post-thumb">
                                    <a href="blog-details-4.html"><img src="assets/img/blog/blog-s-1-4.jpg" alt="img"></a>
                                </div>
                                <div class="blog__post-meta">
                                    <ul class="list-wrap">
                                        <li>
                                            <a href="blog-details-4.html">
                                                <img src="assets/img/blog/blog-author-1-4.jpg" alt="img">
                                            </a>
                                            <div class="content">
                                                <p>EquiRise</p>
                                                <a href="blog-details-4.html">by EquiRise</a>
                                            </div>
                                        </li>
                                        <li>
                                            <div class="content">
                                                <p>Published</p>
                                                <a href="blog-details-4.html">July 8, 2025</a>
                                            </div>
                                        </li>
                                        <li>
                                            <div class="content">
                                                <p>Discussion</p>
                                                <a href="blog-details-4.html">Join the community</a>
                                            </div>
                                        </li>
                                        <li>
                                            <div class="content">
                                                <p>Read</p>
                                                <a href="blog-details-4.html">9,640 views</a>
                                            </div>
                                        </li>
                                    </ul>
                                </div>
                                <div class="blog__post-content">
                                    <h3 class="title"><a href="blog-details-4.html">Building Capacity for Sustainable Growth</a></h3>
                                    <p class="text">How targeted learning and institutional capacity-building drive institutional change and lasting outcomes.</p>
                                    <div class="blog__post-bottom">
                                        <a href="blog-details-4.html" class="btn btn-three">Continue reading</a>
                                    </div>
                                </div>
                            </div>
                        </div>
                    </div>'''
text = text[:start] + new_posts + text[end:]
blog.write_text(text, encoding='utf-8')
print('Updated blog.html posts')

# Update sidebar recent posts and tags on blog.html if present
text = blog.read_text(encoding='utf-8')
text = text.replace('Institutional strengthening for inclusive impact', 'Strengthening Inclusive Institutional Systems')
text = text.replace('Climate resilience through local action', 'Delivering Climate Resilience Through Local Partnerships')
text = text.replace('Procurement systems that improve accountability', 'Transforming Procurement and Supply Chain Governance')
blog.write_text(text, encoding='utf-8')

path = root / 'blog-details.html'
text = path.read_text(encoding='utf-8')
text = re.sub(
    r'<h4 class="box-top-title pe-xl-5">.*?</h4>',
    '<h4 class="box-top-title pe-xl-5">EquiRise partners with institutions to improve governance, service delivery, and inclusive systems.</h4>',
    text,
    flags=re.S,
    count=1,
)
text = text.replace(
    '<h3 class="title mb-3">What EquiRise Consulting Offers</h3>',
    '<h3 class="title mb-3">Strengthening Inclusive Institutional Systems</h3>',
)
text = text.replace(
    '<p class="mb-50">EquiRise Consulting Limited provides practical advisory, training, and research support for institutions, businesses, and communities seeking inclusive growth.</p>',
    '<p class="mb-50">EquiRise helps institutions improve governance, service delivery, and organizational systems through inclusive advisory and capacity-building.</p>',
)
text = text.replace(
    '<h3 class="title mt-55 mb-20"> Practical impact and resource management</h3>',
    '<h3 class="title mt-55 mb-20">Inclusive systems for sustainable programming</h3>',
)
text = text.replace('href="blog-2.html" class="nav-btn prev"', 'href="blog.html" class="nav-btn prev"')
text = text.replace('href="blog-2.html" class="nav-btn next"', 'href="blog-details-2.html" class="nav-btn next"')
path.write_text(text, encoding='utf-8')
print('Updated blog-details.html')

# Create new detail pages

template = path.read_text(encoding='utf-8')

pages = [
    ('blog-details-2.html', 'Delivering Climate Resilience Through Local Partnerships', 'EquiRise helps communities design climate resilience partnerships that improve local systems, reduce risk, and support sustainable livelihoods.', 'Local climate resilience approaches are most effective when they are built on strong institutional partnerships, evidence-driven planning, and inclusive leadership.', 'blog-details.html', 'blog-details-3.html'),
    ('blog-details-3.html', 'Transforming Procurement and Supply Chain Governance', 'EquiRise supports procurement reform by strengthening transparency, risk management, and supplier performance across public and private sectors.', 'Stronger procurement systems reduce waste, improve accountability, and deliver better strategic outcomes for institutions and communities.', 'blog-details-2.html', 'blog-details-4.html'),
    ('blog-details-4.html', 'Building Capacity for Sustainable Growth', 'This article explores how targeted training, organizational learning, and leadership development drive lasting institutional change.', 'Capacity-building works best when it is aligned to real organizational priorities, practical tools, and inclusive stakeholder participation.', 'blog-details-3.html', 'blog.html'),
]

for filename, title, lead, section, prev, next_page in pages:
    page = template
    page = re.sub(r'<h4 class="box-top-title pe-xl-5">.*?</h4>', f'<h4 class="box-top-title pe-xl-5">{title} is powered by practical, inclusive advisory and grounded institutional strategy.</h4>', page, flags=re.S, count=1)
    page = page.replace('<h3 class="title mb-3">Strengthening Inclusive Institutional Systems</h3>', f'<h3 class="title mb-3">{title}</h3>')
    page = page.replace('<p class="mb-50">EquiRise helps institutions improve governance, service delivery, and organizational systems through inclusive advisory and capacity-building.</p>', f'<p class="mb-50">{lead}</p>')
    page = page.replace('<h3 class="title mt-55 mb-20">Inclusive systems for sustainable programming</h3>', f'<h3 class="title mt-55 mb-20">{section}</h3>')
    page = page.replace('href="blog-2.html" class="nav-btn prev"', f'href="{prev}" class="nav-btn prev"')
    page = page.replace('href="blog-2.html" class="nav-btn next"', f'href="{next_page}" class="nav-btn next"')
    page = page.replace('href="blog-details.html"', f'href="{filename}"')
    (root / filename).write_text(page, encoding='utf-8')
    print(f'Created {filename}')
