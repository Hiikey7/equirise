$root = Get-Location

$menuPattern = [regex]::new('<li\s+class="menu-item-has-children"\s*>\s*<a href="#">Blog</a>\s*<ul class="sub-menu">\s*<li>\s*<a href="blog.html">Blog List</a>\s*</li>\s*<li>\s*<a href="blog-2.html">Blog Grid</a>\s*</li>\s*<li>\s*<a href="blog-details.html">Insight Details</a>\s*</li>\s*</ul>\s*</li>', 'Singleline')
$menuReplacement = '<li><a href="blog.html">Blog</a></li>'

Get-ChildItem -Path *.html | ForEach-Object {
    $path = $_.FullName
    $text = Get-Content -Path $path -Raw
    $newText = $menuPattern.Replace($text, $menuReplacement)
    if ($newText -ne $text) {
        Set-Content -Path $path -Value $newText -Encoding UTF8
        Write-Host "Menu updated: $path"
    }
}

$blogFile = Join-Path $root 'blog.html'
$blogText = Get-Content -Path $blogFile -Raw
$startToken = '                    <div class="row gy-80">'
$endToken = '                    <div class="pagination__wrap mt-60">'
$startIndex = $blogText.IndexOf($startToken)
$endIndex = $blogText.IndexOf($endToken, $startIndex)
if ($startIndex -lt 0 -or $endIndex -lt 0) {
    Write-Error "Could not locate blog post section markers in blog.html"
    exit 1
}

$newPosts = @'
                    <div class="row gy-80">
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
                    </div>'@

$blogText = $blogText.Substring(0, $startIndex) + $newPosts + $blogText.Substring($endIndex)
Set-Content -Path $blogFile -Value $blogText -Encoding UTF8
Write-Host 'Updated blog.html posts'

$template = Get-Content -Path (Join-Path $root 'blog-details.html') -Raw
$articles = @(
    @{ id=2; title='Delivering Climate Resilience Through Local Partnerships'; summary='A practical look at how community partnerships and institutional support build resilient systems for climate adaptation.'; top='EquiRise helps institutions and communities build resilient systems for climate adaptation through partnership, planning, and operational support.' },
    @{ id=3; title='Transforming Procurement and Supply Chain Governance'; summary='Insights on building transparent procurement systems that improve accountability and value across public and private sectors.'; top='EquiRise helps government and business systems become more transparent, efficient, and resilient through better procurement governance.' },
    @{ id=4; title='Building Capacity for Sustainable Growth'; summary='How targeted learning and institutional capacity-building drive institutional change and lasting outcomes.'; top='EquiRise develops practical capacity-building programs that strengthen institutional performance and sustainable growth.' }
)

foreach ($article in $articles) {
    $out = [regex]::Replace($template, 'href="blog-details\.html"', "href=\"blog-details-$($article.id).html\"")
    $out = [regex]::Replace($out, '<h4 class="box-top-title pe-xl-5">.*?</h4>', "<h4 class=\"box-top-title pe-xl-5\">$($article.top)</h4>", [System.Text.RegularExpressions.RegexOptions]::Singleline)
    $out = [regex]::Replace($out, '<h3 class="title mb-3">What EquiRise Consulting Offers</h3>', "<h3 class=\"title mb-3\">$($article.title)</h3>")
    $out = [regex]::Replace($out, '<p class="mb-50">.*?</p>', "<p class=\"mb-50\">$($article.summary)</p>", [System.Text.RegularExpressions.RegexOptions]::Singleline)
    Set-Content -Path (Join-Path $root ("blog-details-$($article.id).html")) -Value $out -Encoding UTF8
    Write-Host "Created blog-details-$($article.id).html"
}
