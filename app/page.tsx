export default function BritishTVHub() {
  const topShows = [
    { title: "Count of Monte Cristo", platform: "PBS", genre: "Drama · Period", desc: "A sweeping adaptation of Alexandre Dumas' classic tale of revenge and redemption in 19th century France." },
    { title: "Riot Women", platform: "BritBox", genre: "Drama · Historical", desc: "A powerful drama following women fighting for their rights during a pivotal moment in British history." },
    { title: "Brokenwood Mysteries", platform: "Acorn", genre: "Crime · Mystery", desc: "A charming New Zealand detective series with clever mysteries set in a quirky small town, starring Neill Rea as the unconventional Detective Shepherd." },
    { title: "Murdoch Mysteries", platform: "Acorn", genre: "Crime · Period", desc: "Detective William Murdoch uses cutting-edge forensic techniques to solve crimes in 1900s Toronto." },
    { title: "Miss Scarlet and the Duke", platform: "PBS", genre: "Crime · Period", desc: "A headstrong Victorian woman becomes London's first female private detective in this witty mystery series." },
  ];

  const trendingShows = [
    { emoji: "⚖️", title: "Grace", genre: "Crime · Drama", platform: "BritBox", badge: null, desc: "A dark detective series following a troubled DCI solving brutal murder cases while battling personal demons." },
    { emoji: "🕯️", title: "The Lady", genre: "Drama · Mystery", platform: "Acorn", badge: null, desc: "A gripping drama about power, scandal, and hidden secrets unraveling within British high society." },
    { emoji: "🌴", title: "Death in Paradise", genre: "Crime · Comedy", platform: "BritBox", badge: "Season 15", desc: "A new season of the Caribbean-set crime series featuring clever weekly murder mysteries." },
    { emoji: "🏡", title: "Hope Street", genre: "Crime · Drama", platform: "Acorn", badge: null, desc: "A small-town police drama focused on community policing and personal stories in Northern Ireland." },
    { emoji: "🌊", title: "After the Flood", genre: "Thriller · Mystery", platform: "PBS", badge: null, desc: "A mystery thriller where a devastating flood exposes a suspicious death and buried secrets in a quiet town." },
    { emoji: "🔬", title: "Silent Witness", genre: "Crime · Procedural", platform: "BritBox", badge: null, desc: "A long-running forensic crime drama where pathologists uncover the truth behind complex murder cases." },
    { emoji: "🧩", title: "Murdoch Mysteries", genre: "Crime · Period", platform: "Acorn", badge: null, desc: "A classic detective series where early forensic science is used to solve inventive murder cases in 1900s Toronto." },
  ];

  return (
    <div className="min-h-screen bg-[#120706] text-[#f5ead7]">
      {/* Hero Section */}
      <section className="relative min-h-screen overflow-hidden border-b border-[#5e3417] bg-[#120706]">
        {/* Dark textured gradient background */}
        <div className="absolute inset-0 bg-[radial-gradient(circle_at_center,rgba(255,188,92,0.12),transparent_40%),linear-gradient(to_bottom,rgba(0,0,0,0.5),rgba(0,0,0,0.85))]" />
        <div className="absolute inset-0 opacity-25 [background-image:radial-gradient(rgba(201,159,78,0.15)_1px,transparent_1px)] [background-size:20px_20px]" />
        {/* Subtle noise texture overlay */}
        <div className="absolute inset-0 opacity-[0.03] [background-image:url('data:image/svg+xml,%3Csvg viewBox=%220 0 200 200%22 xmlns=%22http://www.w3.org/2000/svg%22%3E%3Cfilter id=%22noise%22%3E%3CfeTurbulence type=%22fractalNoise%22 baseFrequency=%220.65%22 numOctaves=%223%22 stitchTiles=%22stitch%22/%3E%3C/filter%3E%3Crect width=%22100%25%22 height=%22100%25%22 filter=%22url(%23noise)%22/%3E%3C/svg%3E')]" />
        {/* Vignette effect */}
        <div className="absolute inset-0 bg-[radial-gradient(ellipse_at_center,transparent_0%,rgba(18,7,6,0.4)_70%,rgba(18,7,6,0.8)_100%)]" />

        {/* FIXED: header stacks nicely on mobile */}
        <header className="relative z-10 border-b border-[#5e3417] bg-[#2a120a]/95 backdrop-blur shadow-[0_2px_20px_-2px_rgba(184,150,62,0.3),0_1px_0_0_rgba(184,150,62,0.15)]">
          <div className="mx-auto flex max-w-7xl items-center justify-between px-4 py-4 sm:px-6 sm:py-5 lg:px-10">
            <div className="flex items-center gap-3 text-base sm:text-xl font-semibold tracking-tight text-[#f7e8d2]">
              <span className="text-[#d9a63d]">▱</span>
              <span>British TV Dramas & Mysteries</span>
            </div>

            <nav className="hidden items-center gap-10 text-base uppercase tracking-[0.2em] text-[#ead8be] md:flex">
              <a href="#home" className="transition hover:text-white">Home</a>
              <a href="#about" className="transition hover:text-white">About</a>
              <a href="#contact" className="transition hover:text-white">Contact</a> <a href="/partner.html">Partner</a>
            </nav>

            {/* FIXED: hide button on small screens so header doesn't overflow */}
            <a
              href="https://www.facebook.com/britishtelevisionhub"
              target="_blank"
              rel="noreferrer"
              className="hidden sm:inline-flex rounded-sm border border-[#b11f4b] bg-[#b11f4b] px-5 py-3 text-sm font-semibold uppercase tracking-[0.18em] text-white transition hover:bg-[#c42355]"
            >
              Follow on Facebook
            </a>
          </div>
        </header>

        <div id="home" className="relative z-10 mx-auto flex max-w-7xl items-center px-4 py-12 sm:px-6 sm:py-20 lg:min-h-[calc(100vh-88px)] lg:px-10">
          <div className="mx-auto max-w-4xl text-center">
            <div className="mb-6 sm:mb-8 flex items-center justify-center gap-4 text-sm uppercase tracking-[0.35em] text-[#c99f4e]">
              <span className="h-px w-10 sm:w-16 bg-[#8b6322]" />
              <span>Est. for British TV fans</span>
              <span className="h-px w-10 sm:w-16 bg-[#8b6322]" />
            </div>

            {/* FIXED: smaller base font size on mobile */}
            <h1 className="font-serif text-4xl leading-tight text-[#f7ead7] sm:text-6xl lg:text-8xl">
              Your Cozy Guide to the Best British TV
            </h1>

            <div className="mt-4 sm:mt-5 font-serif text-2xl sm:text-3xl sm:text-4xl italic text-[#d9a63d]">
              Classics & New Favorites
            </div>

            <p className="mx-auto mt-6 sm:mt-8 max-w-3xl text-lg sm:text-xl leading-8 sm:leading-9 text-[#eadbc8]">
              Discover the best British mysteries, hidden gems, and fan favorites.
            </p>

            <p className="mx-auto mt-4 sm:mt-6 max-w-3xl text-base sm:text-lg italic leading-7 sm:leading-8 text-[#c99f4e]">
              Join 4,000+ fans sharing daily recommendations, debates, and hidden gems.
            </p>

            <div className="mt-6 sm:mt-8 text-xs sm:text-sm uppercase tracking-[0.22em] text-[#d9a63d]">
              Daily posts • Polls • Recommendations • No spoilers
            </div>

            {/* FIXED: buttons are full-width on mobile, side-by-side on sm+ */}
            <div className="mt-8 sm:mt-10 flex flex-col items-center justify-center gap-4 sm:flex-row">
              <a
                href="https://www.facebook.com/britishtelevisionhub"
                target="_blank"
                rel="noreferrer"
                className="w-full sm:min-w-[320px] rounded-sm border border-[#b11f4b] bg-[#b11f4b] px-8 py-4 text-center text-sm font-semibold uppercase tracking-[0.25em] text-white transition hover:bg-[#c42355]"
              >
                Follow Us on Facebook
              </a>
              <a
                href="#top-shows"
                className="w-full sm:min-w-[320px] rounded-sm border-2 border-[#d9a63d] bg-transparent px-8 py-4 text-center text-sm font-semibold uppercase tracking-[0.25em] text-[#d9a63d] transition hover:bg-[#d9a63d]/10 hover:text-white"
              >
                Browse Top Shows
              </a>
            </div>

            {/* FIXED: stats always 3-col but with smaller text on mobile */}
            <div className="mt-10 sm:mt-16 grid grid-cols-3 gap-4 sm:gap-8 border-t border-[#5e3417] pt-8 sm:pt-10">
              <div>
                <div className="font-serif text-3xl sm:text-5xl text-[#d9a63d]">4K+</div>
                <div className="mt-2 text-xs sm:text-sm uppercase tracking-[0.25em] text-[#d7c5af]">Followers</div>
              </div>
              <div>
                <div className="font-serif text-3xl sm:text-5xl text-[#d9a63d]">100+</div>
                <div className="mt-2 text-xs sm:text-sm uppercase tracking-[0.25em] text-[#d7c5af]">Series Covered</div>
              </div>
              <div>
                <div className="font-serif text-3xl sm:text-5xl text-[#d9a63d]">Daily</div>
                <div className="mt-2 text-xs sm:text-sm uppercase tracking-[0.25em] text-[#d7c5af]">New Content</div>
              </div>
            </div>
          </div>
        </div>
      </section>

      {/* Trending Radar Section */}
      <section className="border-t border-[#3a1a1a] bg-[#1a0a0a] py-12 sm:py-16 px-4 sm:px-6">
        <div className="mx-auto max-w-3xl">
          <div className="mb-2 flex items-center gap-3">
            <span className="h-2 w-2 animate-pulse rounded-full bg-red-700" />
            <p className="font-sans text-xs uppercase tracking-[3px] text-[#b8963e]">
              Updated every Monday
            </p>
          </div>
          <h2 className="font-serif text-4xl sm:text-5xl font-normal text-[#f0e6d3]">
            Trending Radar
          </h2>
          <p className="mt-1 font-serif italic text-[#b8963e]">
            {"This Week's Most-Watched British Dramas & Mysteries"}
          </p>
          <div className="my-4 h-px w-14 bg-[#b8963e]" />
          <p className="text-lg sm:text-2xl text-[#c8b89a]">
            {"Here's this week's Trending Radar featuring the most-watched British dramas and mysteries right now. Updated every Monday, this guide highlights what viewers are bingeing across crime, thriller, and character-driven British television."}
          </p>
          <div className="mt-8">
            {trendingShows.map((show, i) => (
              <div key={i}>
                <div className="flex items-start gap-3 sm:gap-4 py-4 transition-colors duration-200 hover:bg-[#251212] -mx-4 px-4 rounded">
                  <span className="w-5 sm:w-6 text-left font-sans text-sm text-[#b8963e] pt-1">{i + 1}</span>
                  <span className="text-base pt-1">{show.emoji}</span>
                  <div className="flex-1 min-w-0">
                    <div className="flex flex-wrap items-center gap-2 sm:gap-3">
                      <span className="font-serif text-xl sm:text-2xl text-[#f0e6d3]">{show.title}</span>
                      {show.badge && <span className="font-sans text-xs text-[#b8963e]">({show.badge})</span>}
                      <span className="rounded-sm bg-[#5a1624] px-2 py-0.5 font-sans text-xs uppercase tracking-wider text-[#d9a63d]">
                        {show.platform}
                      </span>
                    </div>
                    <p className="mt-1 font-sans text-xs uppercase tracking-wider text-[#8a7a5e]">{show.genre}</p>
                    <p className="mt-2 font-sans text-base sm:text-xl text-[#c8b89a] leading-relaxed">{show.desc}</p>
                  </div>
                </div>
                {i < trendingShows.length - 1 && (
                  <div className="h-px bg-gradient-to-r from-transparent via-[#b8963e] to-transparent opacity-50" />
                )}
              </div>
            ))}
          </div>
        </div>
      </section>

      {/* About Section */}
      <section id="about" className="border-b border-[#5e3417] bg-[#2a120a]">
        <div className="mx-auto max-w-7xl px-4 sm:px-6 py-14 sm:py-20 lg:px-10">
          <div className="text-center">
            <h2 className="font-serif text-3xl sm:text-4xl text-[#f7ead7] sm:text-6xl">Why We Love British TV</h2>
            <div className="mt-6 flex items-center justify-center gap-5 text-[#c99f4e]">
              <span className="h-px w-24 bg-[#8b6322]" />
              <span className="text-xl">♡</span>
              <span className="h-px w-24 bg-[#8b6322]" />
            </div>
          </div>

          <div className="mt-12 sm:mt-16 grid gap-10 sm:gap-12 lg:grid-cols-[1.15fr_0.85fr]">
            <div className="space-y-5 sm:space-y-6 text-lg sm:text-xl leading-[1.9] text-[#f0dfcb]">
              <p>
                Welcome to the definitive Facebook destination for British TV fans.
              </p>
              <p>
                We are a passionate community dedicated to celebrating the finest dramas and mysteries that British television has to offer.
              </p>
              <p>
                {"From the cobbled streets of Inspector Morse's Oxford to the windswept moors of Vera's Northumberland."}
              </p>
              <p>
                {"From the drawing rooms of Downton Abbey to the tense interrogation rooms of Line of Duty — we cover it all."}
              </p>
              <p>
                {"Whether you're a devotee of Agatha Christie's timeless whodunits or captivated by the latest contemporary thrillers, you'll find your people here."}
              </p>
              <p className="text-[#d9a63d] font-medium">
                {"Join 4,000+ fellow enthusiasts who share your love for great British telly."}
              </p>

              <div className="flex flex-wrap gap-3 pt-4">
                {["Classic Dramas", "Modern Mysteries", "Fan Community", "Daily Updates"].map((item) => (
                  <span
                    key={item}
                    className="rounded-sm border border-[#8b6322] px-4 py-3 text-sm uppercase tracking-[0.18em] text-[#d9a63d]"
                  >
                    {item}
                  </span>
                ))}
              </div>
            </div>

            <div className="space-y-6">
              {[
                {
                  title: "Curated Content",
                  text: "Hand-picked recommendations spanning decades of British television, from beloved classics to the newest releases.",
                  icon: "☷",
                },
                {
                  title: "Vibrant Community",
                  text: "A growing family of British TV fans who share reviews, debate favourites, and discover hidden gems together.",
                  icon: "◌",
                },
                {
                  title: "Daily Engagement",
                  text: "Polls, ratings, discussions, and featured posts that keep the conversation alive every single day.",
                  icon: "☆",
                },
              ].map((card) => (
                <div key={card.title} className="rounded-sm border border-[#b8963e]/40 bg-[#3a1a10] p-6 sm:p-8 shadow-lg">
                  <div className="flex gap-4 sm:gap-5">
                    <div className="flex h-14 w-14 shrink-0 items-center justify-center border border-[#d9a63d] bg-[#2a120a] text-3xl text-[#d9a63d]">
                      {card.icon}
                    </div>
                    <div>
                      <h3 className="font-serif text-2xl sm:text-3xl text-[#f7ead7]">{card.title}</h3>
                      <p className="mt-3 text-base sm:text-xl leading-7 sm:leading-8 text-[#e4cfb7]">{card.text}</p>
                    </div>
                  </div>
                </div>
              ))}
            </div>
          </div>
        </div>
      </section>

      {/* Top Shows Section */}
      <section id="top-shows" className="border-b border-[#5e3417] bg-[#120706]">
        <div className="mx-auto max-w-7xl px-4 sm:px-6 py-14 sm:py-20 lg:px-10">
          <div className="text-center">
            <h2 className="font-serif text-3xl sm:text-4xl text-[#f7ead7] sm:text-6xl">{"The 5 British Mysteries Everyone's Talking About This Week"}</h2>
            <div className="mt-6 flex items-center justify-center gap-5 text-[#c99f4e]">
              <span className="h-px w-24 bg-[#8b6322]" />
              <span className="text-xl">✦</span>
              <span className="h-px w-24 bg-[#8b6322]" />
            </div>
            <p className="mx-auto mt-8 max-w-4xl text-lg sm:text-2xl leading-8 sm:leading-9 text-[#e8d5bf]">
              The British dramas and mysteries our community is watching, debating, and recommending right now.
            </p>
            <p className="mx-auto mt-5 max-w-3xl text-sm sm:text-lg uppercase tracking-[0.18em] text-[#d9a63d]">
              Updated weekly based on what fans are watching right now.
            </p>
          </div>

          {/* FIXED: 1 col on mobile, 2 on md, 5 on lg */}
          <div className="mt-14 grid gap-6 grid-cols-1 md:grid-cols-2 lg:grid-cols-5">
            {topShows.map((show) => (
              <div key={show.title} className="flex h-full flex-col rounded-sm border border-[#5e3417] bg-[#2a120a] p-6 shadow-lg transition-all duration-200 hover:bg-[#3a1a10] hover:border-[#8b6322]">
                <h3 className="font-serif text-xl font-bold leading-tight text-[#f7ead7]">{show.title}</h3>
                <p className="mt-2 text-xs uppercase tracking-wider text-[#8a7a5e]">{show.genre}</p>
                <p className="mt-3 flex-1 text-sm leading-6 text-[#e4cfb7]">{show.desc}</p>
                <div className="mt-4 flex flex-wrap items-center gap-2">
                  <span className="text-xs uppercase tracking-wider text-[#8a7a5e]">Watch on:</span>
                  <span className="rounded-sm bg-[#5a1624] px-2 py-0.5 text-xs uppercase tracking-wider text-[#d9a63d]">
                    {show.platform}
                  </span>
                </div>
              </div>
            ))}
          </div>
        </div>
      </section>

      {/* Hidden Gems Section */}
      <section className="border-b border-[#5e3417] bg-[#2a120a]">
        <div className="mx-auto max-w-7xl px-4 sm:px-6 py-14 sm:py-20 lg:px-10">
          <div className="text-center">
            <h2 className="font-serif text-3xl sm:text-4xl text-[#f7ead7] sm:text-6xl">Hidden Gems You Missed</h2>
            <div className="mt-6 flex items-center justify-center gap-5 text-[#c99f4e]">
              <span className="h-px w-24 bg-[#8b6322]" />
              <span className="text-xl">✧</span>
              <span className="h-px w-24 bg-[#8b6322]" />
            </div>
            <p className="mx-auto mt-8 max-w-4xl text-lg sm:text-2xl leading-8 sm:leading-9 text-[#e8d5bf]">
              Underrated British dramas and mysteries worth discovering next.
            </p>
          </div>

          <div className="mx-auto mt-14 grid max-w-5xl gap-6 grid-cols-1 md:grid-cols-3">
            {["McDonald & Dodds", "Annika", "Blue Lights"].map((show) => (
              <div key={show} className="rounded-sm border border-[#5e3417] bg-[#3a1a10] p-6 shadow-lg">
                <h3 className="font-serif text-2xl sm:text-3xl text-[#f7ead7]">{show}</h3>
                <p className="mt-4 text-base sm:text-lg leading-7 sm:leading-8 text-[#e4cfb7]">
                  A smart pick for viewers ready to try something beyond the usual favorites.
                </p>
              </div>
            ))}
          </div>
        </div>
      </section>

      {/* Cozy Shows Section */}
      <section className="border-b border-[#5e3417] bg-[#0f0504]">
        <div className="mx-auto max-w-7xl px-4 sm:px-6 py-14 sm:py-20 lg:px-10">
          <div className="text-center">
            <h2 className="font-serif text-3xl sm:text-4xl text-[#f7ead7] sm:text-6xl">Best Cozy Shows for the Weekend</h2>
            <div className="mt-6 flex items-center justify-center gap-5 text-[#c99f4e]">
              <span className="h-px w-24 bg-[#8b6322]" />
              <span className="text-xl">❋</span>
              <span className="h-px w-24 bg-[#8b6322]" />
            </div>
            <p className="mx-auto mt-8 max-w-4xl text-lg sm:text-2xl leading-8 sm:leading-9 text-[#e8d5bf]">
              Comfort-watch favorites for tea, blankets, and one more episode.
            </p>
          </div>

          {/* Horizontal scrolling showcase */}
          <div className="mt-14 overflow-x-auto pb-4 -mx-4 sm:-mx-6 px-4 sm:px-6 scrollbar-thin scrollbar-track-[#1a0a0a] scrollbar-thumb-[#5e3417]">
            <div className="flex gap-0 min-w-max">
              {[
                { 
                  num: "01", 
                  title: "Count of Monte Cristo", 
                  mood: "Perfect for a rainy Sunday", 
                  genre: "Drama · Period", 
                  platform: "PBS",
                  whyPicked: "Epic storytelling that rewards patient viewers with unforgettable drama."
                },
                { 
                  num: "02", 
                  title: "Riot Women", 
                  mood: "When you want something powerful", 
                  genre: "Drama · Historical", 
                  platform: "BritBox",
                  whyPicked: "Bold, inspiring, and impossible to look away from."
                },
                { 
                  num: "03", 
                  title: "Brokenwood Mysteries", 
                  mood: "Lighthearted mystery evening", 
                  genre: "Crime · Mystery", 
                  platform: "Acorn",
                  whyPicked: "Charming mysteries with just the right amount of quirk."
                },
                { 
                  num: "04", 
                  title: "Murdoch Mysteries", 
                  mood: "Cozy period piece marathon", 
                  genre: "Crime · Period", 
                  platform: "Acorn",
                  whyPicked: "Clever cases and Victorian charm make every episode a treat."
                },
                { 
                  num: "05", 
                  title: "Miss Scarlet and the Duke", 
                  mood: "Perfect for a Friday night in", 
                  genre: "Crime · Period", 
                  platform: "PBS",
                  whyPicked: "Witty, romantic, and delightfully binge-worthy."
                },
              ].map((show, index) => (
                <div 
                  key={show.title} 
                  className={`flex min-w-[300px] sm:min-w-[400px] border-l-4 border-[#d9a63d] transition-all duration-200 hover:brightness-125 ${
                    index % 2 === 0 ? 'bg-[#1a0a08]' : 'bg-[#241210]'
                  }`}
                >
                  {/* Large number */}
                  <div className="flex w-16 sm:w-28 shrink-0 items-center justify-center border-r border-[#3a1a10]">
                    <span className="font-serif text-4xl sm:text-6xl font-bold text-[#d9a63d]/80">{show.num}</span>
                  </div>
                  
                  {/* Content */}
                  <div className="flex-1 p-5 sm:p-8">
                    <h3 className="font-serif text-2xl sm:text-3xl font-bold text-[#f7ead7]">{show.title}</h3>
                    
                    <div className="mt-2 flex flex-wrap items-center gap-3">
                      <span className="rounded-full bg-[#2a1a12] px-3 py-1 text-xs uppercase tracking-wider text-[#c99f4e]">
                        {show.mood}
                      </span>
                    </div>
                    
                    <p className="mt-3 text-sm uppercase tracking-wider text-[#8a7a5e]">{show.genre}</p>
                    
                    <p className="mt-4 font-serif text-base sm:text-lg italic text-[#d9a63d]">
                      {`"${show.whyPicked}"`}
                    </p>
                    
                    <div className="mt-5 flex items-center gap-2">
                      <span className="text-xs uppercase tracking-wider text-[#8a7a5e]">Where to Watch:</span>
                      <span className="rounded-sm bg-[#5a1624] px-2 py-0.5 text-xs uppercase tracking-wider text-[#d9a63d]">
                        {show.platform}
                      </span>
                    </div>
                  </div>
                </div>
              ))}
            </div>
          </div>
          
          {/* Scroll hint */}
          <div className="mt-4 flex items-center justify-center gap-2 text-sm text-[#8a7a5e]">
            <span>Scroll to explore</span>
            <span className="animate-pulse">→</span>
          </div>
        </div>
      </section>

      {/* What to Watch Section */}
      <section className="border-b border-[#5e3417] bg-[#2a120a]">
        <div className="mx-auto max-w-5xl px-4 sm:px-6 py-14 sm:py-20 lg:px-10">
          <div className="text-center">
            <h2 className="font-serif text-3xl sm:text-4xl text-[#f7ead7] sm:text-6xl">What Should You Watch Next?</h2>
            <div className="mt-6 flex items-center justify-center gap-5 text-[#c99f4e]">
              <span className="h-px w-24 bg-[#8b6322]" />
              <span className="text-xl">★</span>
              <span className="h-px w-24 bg-[#8b6322]" />
            </div>
            <p className="mx-auto mt-8 max-w-3xl text-lg sm:text-2xl leading-8 sm:leading-9 text-[#e8d5bf]">
              Start with one of these picks and tell us what you think on Facebook.
            </p>
          </div>

          <div className="mx-auto mt-14 grid max-w-5xl gap-6 grid-cols-1 md:grid-cols-3">
            {["Count of Monte Cristo", "Shetland", "Unforgotten"].map((show) => (
              <div key={show} className="rounded-sm border border-[#5e3417] bg-[#120706] p-6 shadow-lg">
                <h3 className="font-serif text-2xl sm:text-3xl text-[#f7ead7]">{show}</h3>
                <p className="mt-4 text-base sm:text-lg leading-7 sm:leading-8 text-[#e4cfb7]">
                  A great place to start if you want a strong recommendation from the community.
                </p>
              </div>
            ))}
          </div>
        </div>
      </section>

      {/* Contact Section */}
      <section id="contact" className="bg-[#120706]">
        <div className="mx-auto max-w-5xl px-4 sm:px-6 py-14 sm:py-20 lg:px-10">
          <div className="text-center">
            <h2 className="font-serif text-3xl sm:text-4xl text-[#f7ead7] sm:text-6xl">{"Let's Talk Telly"}</h2>
            <div className="mt-6 flex items-center justify-center gap-5 text-[#c99f4e]">
              <span className="h-px w-24 bg-[#8b6322]" />
              <span className="text-xl">◦</span>
              <span className="h-px w-24 bg-[#8b6322]" />
            </div>
            <p className="mx-auto mt-8 max-w-3xl text-lg sm:text-2xl leading-8 sm:leading-9 text-[#e8d5bf]">
              Want to chat about your favourite British dramas and mysteries? Join the conversation on our social channels!
            </p>
          </div>

          <div className="mx-auto mt-14 max-w-3xl space-y-6">
            <div className="rounded-sm border border-[#5e3417] bg-[#2a120a] p-6 sm:p-8 shadow-lg">
              <div className="flex gap-4 sm:gap-5">
                <div className="flex h-14 w-14 shrink-0 items-center justify-center border border-[#8b6322] bg-[#5a1624] text-2xl text-[#d9a63d]">
                  f
                </div>
                <div>
                  <h3 className="font-serif text-2xl sm:text-3xl text-[#f7ead7]">Facebook Community</h3>
                  <p className="mt-3 text-base sm:text-xl leading-7 sm:leading-8 text-[#e4cfb7]">
                    Join the conversation—daily polls, debates, and must-watch recommendations.
                  </p>
                </div>
              </div>
            </div>

            <div className="text-center text-sm uppercase tracking-[0.22em] text-[#d9a63d]">
              New posts every day
            </div>

            <div className="rounded-sm border border-[#7a2434] bg-[#5a1624] p-8 sm:p-10 text-center shadow-xl">
              <p className="mx-auto max-w-3xl text-lg sm:text-2xl italic leading-8 sm:leading-9 text-[#f3dfcb]">
                {"\"The best way to connect with us is through our Facebook community. We're always happy to hear from fellow British telly enthusiasts!\""}
              </p>
              <div className="mt-8">
                <a
                  href="https://www.facebook.com/britishtelevisionhub"
                  target="_blank"
                  rel="noreferrer"
                  className="inline-flex rounded-sm border border-[#d23c68] bg-[#b11f4b] px-8 py-4 text-sm font-semibold uppercase tracking-[0.25em] text-white transition hover:bg-[#c42355]"
                >
                  Visit Our Page
                </a>
              </div>
            </div>
          </div>
        </div>
      </section>
    </div>
  );
}
