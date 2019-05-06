





<!DOCTYPE html>
<html lang="en">
  <head>
    <meta charset="utf-8">
  <link rel="dns-prefetch" href="https://assets-cdn.github.com">
  <link rel="dns-prefetch" href="https://avatars0.githubusercontent.com">
  <link rel="dns-prefetch" href="https://avatars1.githubusercontent.com">
  <link rel="dns-prefetch" href="https://avatars2.githubusercontent.com">
  <link rel="dns-prefetch" href="https://avatars3.githubusercontent.com">
  <link rel="dns-prefetch" href="https://github-cloud.s3.amazonaws.com">
  <link rel="dns-prefetch" href="https://user-images.githubusercontent.com/">



  <link crossorigin="anonymous" href="https://assets-cdn.github.com/assets/frameworks-521cbf980c80.css" integrity="sha512-Uhy/mAyAx1HfsenmjQ85ASpOk5bjt2Ay03pNeixXIvkHlEm5S+N4u0HWfDGhvsGYx4bGyviXWGGPZeIffqYcNA==" media="all" rel="stylesheet" />
  <link crossorigin="anonymous" href="https://assets-cdn.github.com/assets/github-f75b395c95ee.css" integrity="sha512-91s5XJXuYfLeHJoeobMe4FgEnU0IIJNpD/SfZ5MQOVZ7CnKZ4/KLOusHqNFqOJVJVBWgJ9G+6w+jxVVpJ1aKxw==" media="all" rel="stylesheet" />
  
  
  
  

  <meta name="viewport" content="width=device-width">
  
  <title>python-fire/guide.md at master · google/python-fire</title>
  <link rel="search" type="application/opensearchdescription+xml" href="/opensearch.xml" title="GitHub">
  <link rel="fluid-icon" href="https://github.com/fluidicon.png" title="GitHub">
  <meta property="fb:app_id" content="1401488693436528">

    
    <meta content="https://avatars0.githubusercontent.com/u/1342004?s=400&amp;v=4" property="og:image" /><meta content="GitHub" property="og:site_name" /><meta content="object" property="og:type" /><meta content="google/python-fire" property="og:title" /><meta content="https://github.com/google/python-fire" property="og:url" /><meta content="python-fire - Python Fire is a library for automatically generating command line interfaces (CLIs) from absolutely any Python object." property="og:description" />

  <link rel="assets" href="https://assets-cdn.github.com/">
  <link rel="web-socket" href="wss://live.github.com/_sockets/VjI6MjMyNTkzNjg0OjBmYzFkN2Q5ZjE1ZWQ3YmYyMjZjZTI1MmQxMmQ5MThkZDc5ZWNkMjdlMTA0NTBkNTNiN2I5MTNjYjkyNzkxMTk=--b46688cca312b62cacae0fad29b8e1446a5dd846">
  <meta name="pjax-timeout" content="1000">
  <link rel="sudo-modal" href="/sessions/sudo_modal">
  <meta name="request-id" content="D212:156F9:1A927B5:27BCACB:5A728AC9" data-pjax-transient>
  

  <meta name="selected-link" value="repo_source" data-pjax-transient>

    <meta name="google-site-verification" content="KT5gs8h0wvaagLKAVWq8bbeNwnZZK1r1XQysX3xurLU">
  <meta name="google-site-verification" content="ZzhVyEFwb7w3e0-uOTltm8Jsck2F5StVihD0exw2fsA">
  <meta name="google-site-verification" content="GXs5KoUUkNCoaAZn7wPN-t01Pywp9M3sEjnt_3_ZWPc">
    <meta name="google-analytics" content="UA-3769691-2">

<meta content="collector.githubapp.com" name="octolytics-host" /><meta content="github" name="octolytics-app-id" /><meta content="https://collector.githubapp.com/github-external/browser_event" name="octolytics-event-url" /><meta content="D212:156F9:1A927B5:27BCACB:5A728AC9" name="octolytics-dimension-request_id" /><meta content="sea" name="octolytics-dimension-region_edge" /><meta content="iad" name="octolytics-dimension-region_render" /><meta content="26454595" name="octolytics-actor-id" /><meta content="jingxu94" name="octolytics-actor-login" /><meta content="b787a8381cfa71648dafbd0b4a8158605200baae95bf2d59093c000d869c6822" name="octolytics-actor-hash" />
<meta content="https://github.com/hydro_browser_events" name="hydro-events-url" />
<meta content="/&lt;user-name&gt;/&lt;repo-name&gt;/blob/show" data-pjax-transient="true" name="analytics-location" />




  <meta class="js-ga-set" name="dimension1" content="Logged In">


  

      <meta name="hostname" content="github.com">
  <meta name="user-login" content="jingxu94">

      <meta name="expected-hostname" content="github.com">
    <meta name="js-proxy-site-detection-payload" content="NmFjZDA3YTk2YTVkZDkyYzU4NzE5ZDViYTVhYzQzZmI2OGE2ZjQ5NDM5ZTEzNjg4ZDQ1Y2YwOGRhMmU4ZmFhYXx7InJlbW90ZV9hZGRyZXNzIjoiNDcuOTEuMjAuMTUiLCJyZXF1ZXN0X2lkIjoiRDIxMjoxNTZGOToxQTkyN0I1OjI3QkNBQ0I6NUE3MjhBQzkiLCJ0aW1lc3RhbXAiOjE1MTc0NTYwNzQsImhvc3QiOiJnaXRodWIuY29tIn0=">

    <meta name="enabled-features" content="UNIVERSE_BANNER,MULTIPLE_ATTRIBUTION,FREE_TRIALS,MARKETPLACE_HERO_CARD_UPLOADER,MARKETPLACE_IMAGE_OPTIM,CONTRIBUTOR_FLAGGED_CONTENT">

  <meta name="html-safe-nonce" content="289ba78fd1197702f4513be1a4d8e68e760be7fd">

  <meta http-equiv="x-pjax-version" content="87b5f3f15ad833b10b740788960f60e0">
  

      <link href="https://github.com/google/python-fire/commits/master.atom" rel="alternate" title="Recent Commits to python-fire:master" type="application/atom+xml">

  <meta name="description" content="python-fire - Python Fire is a library for automatically generating command line interfaces (CLIs) from absolutely any Python object.">
  <meta name="go-import" content="github.com/google/python-fire git https://github.com/google/python-fire.git">

  <meta content="1342004" name="octolytics-dimension-user_id" /><meta content="google" name="octolytics-dimension-user_login" /><meta content="82729529" name="octolytics-dimension-repository_id" /><meta content="google/python-fire" name="octolytics-dimension-repository_nwo" /><meta content="true" name="octolytics-dimension-repository_public" /><meta content="false" name="octolytics-dimension-repository_is_fork" /><meta content="82729529" name="octolytics-dimension-repository_network_root_id" /><meta content="google/python-fire" name="octolytics-dimension-repository_network_root_nwo" /><meta content="false" name="octolytics-dimension-repository_explore_github_marketplace_ci_cta_shown" />


    <link rel="canonical" href="https://github.com/google/python-fire/blob/master/docs/guide.md" data-pjax-transient>


  <meta name="browser-stats-url" content="https://api.github.com/_private/browser/stats">

  <meta name="browser-errors-url" content="https://api.github.com/_private/browser/errors">

  <link rel="mask-icon" href="https://assets-cdn.github.com/pinned-octocat.svg" color="#000000">
  <link rel="icon" type="image/x-icon" class="js-site-favicon" href="https://assets-cdn.github.com/favicon.ico">

<meta name="theme-color" content="#1e2327">


  <meta name="u2f-support" content="true">

  </head>

  <body class="logged-in env-production page-blob">
    

  <div class="position-relative js-header-wrapper ">
    <a href="#start-of-content" tabindex="1" class="bg-black text-white p-3 show-on-focus js-skip-to-content">Skip to content</a>
    <div id="js-pjax-loader-bar" class="pjax-loader-bar"><div class="progress"></div></div>

    
    
    



        
<header class="Header  f5" role="banner">
  <div class="d-flex px-3 flex-justify-between container-lg">
    <div class="d-flex flex-justify-between">
      <a class="header-logo-invertocat" href="https://github.com/" data-hotkey="g d" aria-label="Homepage" data-ga-click="Header, go to dashboard, icon:logo">
  <svg aria-hidden="true" class="octicon octicon-mark-github" height="32" version="1.1" viewBox="0 0 16 16" width="32"><path fill-rule="evenodd" d="M8 0C3.58 0 0 3.58 0 8c0 3.54 2.29 6.53 5.47 7.59.4.07.55-.17.55-.38 0-.19-.01-.82-.01-1.49-2.01.37-2.53-.49-2.69-.94-.09-.23-.48-.94-.82-1.13-.28-.15-.68-.52-.01-.53.63-.01 1.08.58 1.23.82.72 1.21 1.87.87 2.33.66.07-.52.28-.87.51-1.07-1.78-.2-3.64-.89-3.64-3.95 0-.87.31-1.59.82-2.15-.08-.2-.36-1.02.08-2.12 0 0 .67-.21 2.2.82.64-.18 1.32-.27 2-.27.68 0 1.36.09 2 .27 1.53-1.04 2.2-.82 2.2-.82.44 1.1.16 1.92.08 2.12.51.56.82 1.27.82 2.15 0 3.07-1.87 3.75-3.65 3.95.29.25.54.73.54 1.48 0 1.07-.01 1.93-.01 2.2 0 .21.15.46.55.38A8.013 8.013 0 0 0 16 8c0-4.42-3.58-8-8-8z"/></svg>
</a>


    </div>

    <div class="HeaderMenu d-flex flex-justify-between flex-auto">
      <div class="d-flex">
            <div class="">
              <div class="header-search scoped-search site-scoped-search js-site-search" role="search">
  <!-- '"` --><!-- </textarea></xmp> --></option></form><form accept-charset="UTF-8" action="/google/python-fire/search" class="js-site-search-form" data-scoped-search-url="/google/python-fire/search" data-unscoped-search-url="/search" method="get"><div style="margin:0;padding:0;display:inline"><input name="utf8" type="hidden" value="&#x2713;" /></div>
    <label class="form-control header-search-wrapper js-chromeless-input-container">
        <a href="/google/python-fire/blob/master/docs/guide.md" class="header-search-scope no-underline">This repository</a>
      <input type="text"
        class="form-control header-search-input js-site-search-focus js-site-search-field is-clearable"
        data-hotkey="s"
        name="q"
        value=""
        placeholder="Search"
        aria-label="Search this repository"
        data-unscoped-placeholder="Search GitHub"
        data-scoped-placeholder="Search"
        autocapitalize="off">
        <input type="hidden" class="js-site-search-type-field" name="type" >
    </label>
</form></div>

            </div>

          <ul class="d-flex pl-2 flex-items-center text-bold list-style-none" role="navigation">
            <li>
              <a href="/pulls" aria-label="Pull requests you created" class="js-selected-navigation-item HeaderNavlink px-2" data-ga-click="Header, click, Nav menu - item:pulls context:user" data-hotkey="g p" data-selected-links="/pulls /pulls/assigned /pulls/mentioned /pulls">
                Pull requests
</a>            </li>
            <li>
              <a href="/issues" aria-label="Issues you created" class="js-selected-navigation-item HeaderNavlink px-2" data-ga-click="Header, click, Nav menu - item:issues context:user" data-hotkey="g i" data-selected-links="/issues /issues/assigned /issues/mentioned /issues">
                Issues
</a>            </li>
                <li>
                  <a href="/marketplace" class="js-selected-navigation-item HeaderNavlink px-2" data-ga-click="Header, click, Nav menu - item:marketplace context:user" data-selected-links=" /marketplace">
                    Marketplace
</a>                </li>
            <li>
              <a href="/explore" class="js-selected-navigation-item HeaderNavlink px-2" data-ga-click="Header, click, Nav menu - item:explore" data-selected-links="/explore /trending /trending/developers /integrations /integrations/feature/code /integrations/feature/collaborate /integrations/feature/ship showcases showcases_search showcases_landing /explore">
                Explore
</a>            </li>
          </ul>
      </div>

      <div class="d-flex">
        
<ul class="user-nav d-flex flex-items-center list-style-none" id="user-links">
  <li class="dropdown js-menu-container">
    <span class="d-inline-block  px-2">
      

    </span>
  </li>

  <li class="dropdown js-menu-container">
    <details class="dropdown-details details-reset js-dropdown-details d-flex px-2 flex-items-center">
      <summary class="HeaderNavlink"
         aria-label="Create new…"
         data-ga-click="Header, create new, icon:add">
        <svg aria-hidden="true" class="octicon octicon-plus float-left mr-1 mt-1" height="16" version="1.1" viewBox="0 0 12 16" width="12"><path fill-rule="evenodd" d="M12 9H7v5H5V9H0V7h5V2h2v5h5z"/></svg>
        <span class="dropdown-caret mt-1"></span>
      </summary>

      <ul class="dropdown-menu dropdown-menu-sw">
        
<a class="dropdown-item" href="/new" data-ga-click="Header, create new repository">
  New repository
</a>

  <a class="dropdown-item" href="/new/import" data-ga-click="Header, import a repository">
    Import repository
  </a>

<a class="dropdown-item" href="https://gist.github.com/" data-ga-click="Header, create new gist">
  New gist
</a>

  <a class="dropdown-item" href="/organizations/new" data-ga-click="Header, create new organization">
    New organization
  </a>



  <div class="dropdown-divider"></div>
  <div class="dropdown-header">
    <span title="google/python-fire">This repository</span>
  </div>
    <a class="dropdown-item" href="/google/python-fire/issues/new" data-ga-click="Header, create new issue">
      New issue
    </a>

      </ul>
    </details>
  </li>

  <li class="dropdown js-menu-container">

    <details class="dropdown-details details-reset js-dropdown-details d-flex pl-2 flex-items-center">
      <summary class="HeaderNavlink name mt-1"
        aria-label="View profile and more"
        data-ga-click="Header, show menu, icon:avatar">
        <img alt="@jingxu94" class="avatar float-left mr-1" src="https://avatars3.githubusercontent.com/u/26454595?s=40&amp;v=4" height="20" width="20">
        <span class="dropdown-caret"></span>
      </summary>

      <ul class="dropdown-menu dropdown-menu-sw">
        <li class="dropdown-header header-nav-current-user css-truncate">
          Signed in as <strong class="css-truncate-target">jingxu94</strong>
        </li>

        <li class="dropdown-divider"></li>

        <li><a class="dropdown-item" href="/jingxu94" data-ga-click="Header, go to profile, text:your profile">
          Your profile
        </a></li>
        <li><a class="dropdown-item" href="/jingxu94?tab=stars" data-ga-click="Header, go to starred repos, text:your stars">
          Your stars
        </a></li>
          <li><a class="dropdown-item" href="https://gist.github.com/" data-ga-click="Header, your gists, text:your gists">Your Gists</a></li>

        <li class="dropdown-divider"></li>

        <li><a class="dropdown-item" href="https://help.github.com" data-ga-click="Header, go to help, text:help">
          Help
        </a></li>

        <li><a class="dropdown-item" href="/settings/profile" data-ga-click="Header, go to settings, icon:settings">
          Settings
        </a></li>

        <li><!-- '"` --><!-- </textarea></xmp> --></option></form><form accept-charset="UTF-8" action="/logout" class="logout-form" method="post"><div style="margin:0;padding:0;display:inline"><input name="utf8" type="hidden" value="&#x2713;" /><input name="authenticity_token" type="hidden" value="aXGY71QTIWWfvwZ35iBqsWDnGw5uNYK+yKJqmdag0PEcyeMhsdd9OMYk2VK2AxyZrv9DrOlzBBgmNU2w6ddXEQ==" /></div>
          <button type="submit" class="dropdown-item dropdown-signout" data-ga-click="Header, sign out, icon:logout">
            Sign out
          </button>
        </form></li>
      </ul>
    </details>
  </li>
</ul>


        <!-- '"` --><!-- </textarea></xmp> --></option></form><form accept-charset="UTF-8" action="/logout" class="sr-only right-0" method="post"><div style="margin:0;padding:0;display:inline"><input name="utf8" type="hidden" value="&#x2713;" /><input name="authenticity_token" type="hidden" value="Wn7ynByS4zsW3GP4QE9fVDFOxmdy1y/KOoa1QTgifosvxolS+Va/Zk9HvN0QbCl8/1aexfWRqWzUEZJoB1X5aw==" /></div>
          <button type="submit" class="dropdown-item dropdown-signout" data-ga-click="Header, sign out, icon:logout">
            Sign out
          </button>
</form>      </div>
    </div>
  </div>
</header>

      

  </div>

  <div id="start-of-content" class="show-on-focus"></div>

    <div id="js-flash-container">
</div>



  <div role="main" class="application-main ">
        <div itemscope itemtype="http://schema.org/SoftwareSourceCode" class="">
    <div id="js-repo-pjax-container" data-pjax-container >
      




  



  <div class="pagehead repohead instapaper_ignore readability-menu experiment-repo-nav  ">
    <div class="repohead-details-container clearfix container">

      <ul class="pagehead-actions">
  <li>
        <!-- '"` --><!-- </textarea></xmp> --></option></form><form accept-charset="UTF-8" action="/notifications/subscribe" class="js-social-container" data-autosubmit="true" data-remote="true" method="post"><div style="margin:0;padding:0;display:inline"><input name="utf8" type="hidden" value="&#x2713;" /><input name="authenticity_token" type="hidden" value="uzyMET64EbjhDfmkh/XYFBRyhtfqpvrThvgWEbwwS8KZGpxy6bWTdW8e4S0YU3KLBoucftscm7Jf85EdaS9Wig==" /></div>      <input class="form-control" id="repository_id" name="repository_id" type="hidden" value="82729529" />

        <div class="select-menu js-menu-container js-select-menu">
          <a href="/google/python-fire/subscription"
            class="btn btn-sm btn-with-count select-menu-button js-menu-target"
            role="button"
            aria-haspopup="true"
            aria-expanded="false"
            aria-label="Toggle repository notifications menu"
            data-ga-click="Repository, click Watch settings, action:blob#show">
            <span class="js-select-button">
                <svg aria-hidden="true" class="octicon octicon-eye" height="16" version="1.1" viewBox="0 0 16 16" width="16"><path fill-rule="evenodd" d="M8.06 2C3 2 0 8 0 8s3 6 8.06 6C13 14 16 8 16 8s-3-6-7.94-6zM8 12c-2.2 0-4-1.78-4-4 0-2.2 1.8-4 4-4 2.22 0 4 1.8 4 4 0 2.22-1.78 4-4 4zm2-4c0 1.11-.89 2-2 2-1.11 0-2-.89-2-2 0-1.11.89-2 2-2 1.11 0 2 .89 2 2z"/></svg>
                Watch
            </span>
          </a>
          <a class="social-count js-social-count"
            href="/google/python-fire/watchers"
            aria-label="272 users are watching this repository">
            272
          </a>

        <div class="select-menu-modal-holder">
          <div class="select-menu-modal subscription-menu-modal js-menu-content">
            <div class="select-menu-header js-navigation-enable" tabindex="-1">
              <svg aria-label="Close" class="octicon octicon-x js-menu-close" height="16" role="img" version="1.1" viewBox="0 0 12 16" width="12"><path fill-rule="evenodd" d="M7.48 8l3.75 3.75-1.48 1.48L6 9.48l-3.75 3.75-1.48-1.48L4.52 8 .77 4.25l1.48-1.48L6 6.52l3.75-3.75 1.48 1.48z"/></svg>
              <span class="select-menu-title">Notifications</span>
            </div>

              <div class="select-menu-list js-navigation-container" role="menu">

                <div class="select-menu-item js-navigation-item selected" role="menuitem" tabindex="0">
                  <svg aria-hidden="true" class="octicon octicon-check select-menu-item-icon" height="16" version="1.1" viewBox="0 0 12 16" width="12"><path fill-rule="evenodd" d="M12 5l-8 8-4-4 1.5-1.5L4 10l6.5-6.5z"/></svg>
                  <div class="select-menu-item-text">
                    <input checked="checked" id="do_included" name="do" type="radio" value="included" />
                    <span class="select-menu-item-heading">Not watching</span>
                    <span class="description">Be notified when participating or @mentioned.</span>
                    <span class="js-select-button-text hidden-select-button-text">
                      <svg aria-hidden="true" class="octicon octicon-eye" height="16" version="1.1" viewBox="0 0 16 16" width="16"><path fill-rule="evenodd" d="M8.06 2C3 2 0 8 0 8s3 6 8.06 6C13 14 16 8 16 8s-3-6-7.94-6zM8 12c-2.2 0-4-1.78-4-4 0-2.2 1.8-4 4-4 2.22 0 4 1.8 4 4 0 2.22-1.78 4-4 4zm2-4c0 1.11-.89 2-2 2-1.11 0-2-.89-2-2 0-1.11.89-2 2-2 1.11 0 2 .89 2 2z"/></svg>
                      Watch
                    </span>
                  </div>
                </div>

                <div class="select-menu-item js-navigation-item " role="menuitem" tabindex="0">
                  <svg aria-hidden="true" class="octicon octicon-check select-menu-item-icon" height="16" version="1.1" viewBox="0 0 12 16" width="12"><path fill-rule="evenodd" d="M12 5l-8 8-4-4 1.5-1.5L4 10l6.5-6.5z"/></svg>
                  <div class="select-menu-item-text">
                    <input id="do_subscribed" name="do" type="radio" value="subscribed" />
                    <span class="select-menu-item-heading">Watching</span>
                    <span class="description">Be notified of all conversations.</span>
                    <span class="js-select-button-text hidden-select-button-text">
                      <svg aria-hidden="true" class="octicon octicon-eye" height="16" version="1.1" viewBox="0 0 16 16" width="16"><path fill-rule="evenodd" d="M8.06 2C3 2 0 8 0 8s3 6 8.06 6C13 14 16 8 16 8s-3-6-7.94-6zM8 12c-2.2 0-4-1.78-4-4 0-2.2 1.8-4 4-4 2.22 0 4 1.8 4 4 0 2.22-1.78 4-4 4zm2-4c0 1.11-.89 2-2 2-1.11 0-2-.89-2-2 0-1.11.89-2 2-2 1.11 0 2 .89 2 2z"/></svg>
                        Unwatch
                    </span>
                  </div>
                </div>

                <div class="select-menu-item js-navigation-item " role="menuitem" tabindex="0">
                  <svg aria-hidden="true" class="octicon octicon-check select-menu-item-icon" height="16" version="1.1" viewBox="0 0 12 16" width="12"><path fill-rule="evenodd" d="M12 5l-8 8-4-4 1.5-1.5L4 10l6.5-6.5z"/></svg>
                  <div class="select-menu-item-text">
                    <input id="do_ignore" name="do" type="radio" value="ignore" />
                    <span class="select-menu-item-heading">Ignoring</span>
                    <span class="description">Never be notified.</span>
                    <span class="js-select-button-text hidden-select-button-text">
                      <svg aria-hidden="true" class="octicon octicon-mute" height="16" version="1.1" viewBox="0 0 16 16" width="16"><path fill-rule="evenodd" d="M8 2.81v10.38c0 .67-.81 1-1.28.53L3 10H1c-.55 0-1-.45-1-1V7c0-.55.45-1 1-1h2l3.72-3.72C7.19 1.81 8 2.14 8 2.81zm7.53 3.22l-1.06-1.06-1.97 1.97-1.97-1.97-1.06 1.06L11.44 8 9.47 9.97l1.06 1.06 1.97-1.97 1.97 1.97 1.06-1.06L13.56 8l1.97-1.97z"/></svg>
                        Stop ignoring
                    </span>
                  </div>
                </div>

              </div>

            </div>
          </div>
        </div>
</form>
  </li>

  <li>
    
  <div class="js-toggler-container js-social-container starring-container ">
    <!-- '"` --><!-- </textarea></xmp> --></option></form><form accept-charset="UTF-8" action="/google/python-fire/unstar" class="starred js-social-form" method="post"><div style="margin:0;padding:0;display:inline"><input name="utf8" type="hidden" value="&#x2713;" /><input name="authenticity_token" type="hidden" value="IFwBU6m82UUpPjCFBdlNo79BVXnQAVmSVmAWDEXj0iBejdEUZoa+ipbC8KxDMtJnXhFxcODSWY81l+6EpjAY8A==" /></div>
      <input type="hidden" name="context" value="repository"></input>
      <button
        type="submit"
        class="btn btn-sm btn-with-count js-toggler-target"
        aria-label="Unstar this repository" title="Unstar google/python-fire"
        data-ga-click="Repository, click unstar button, action:blob#show; text:Unstar">
        <svg aria-hidden="true" class="octicon octicon-star" height="16" version="1.1" viewBox="0 0 14 16" width="14"><path fill-rule="evenodd" d="M14 6l-4.9-.64L7 1 4.9 5.36 0 6l3.6 3.26L2.67 14 7 11.67 11.33 14l-.93-4.74z"/></svg>
        Unstar
      </button>
        <a class="social-count js-social-count" href="/google/python-fire/stargazers"
           aria-label="8292 users starred this repository">
          8,292
        </a>
</form>
    <!-- '"` --><!-- </textarea></xmp> --></option></form><form accept-charset="UTF-8" action="/google/python-fire/star" class="unstarred js-social-form" method="post"><div style="margin:0;padding:0;display:inline"><input name="utf8" type="hidden" value="&#x2713;" /><input name="authenticity_token" type="hidden" value="dHDQprU8n14W6xxhRYLvBSZ4Z6fya0N3XDz54XSLEwe//cge3u5+G8m5jybiihiF7mL/raEsAZtsIZR2iozrBg==" /></div>
      <input type="hidden" name="context" value="repository"></input>
      <button
        type="submit"
        class="btn btn-sm btn-with-count js-toggler-target"
        aria-label="Star this repository" title="Star google/python-fire"
        data-ga-click="Repository, click star button, action:blob#show; text:Star">
        <svg aria-hidden="true" class="octicon octicon-star" height="16" version="1.1" viewBox="0 0 14 16" width="14"><path fill-rule="evenodd" d="M14 6l-4.9-.64L7 1 4.9 5.36 0 6l3.6 3.26L2.67 14 7 11.67 11.33 14l-.93-4.74z"/></svg>
        Star
      </button>
        <a class="social-count js-social-count" href="/google/python-fire/stargazers"
           aria-label="8292 users starred this repository">
          8,292
        </a>
</form>  </div>

  </li>

  <li>
          <!-- '"` --><!-- </textarea></xmp> --></option></form><form accept-charset="UTF-8" action="/google/python-fire/fork" class="btn-with-count" method="post"><div style="margin:0;padding:0;display:inline"><input name="utf8" type="hidden" value="&#x2713;" /><input name="authenticity_token" type="hidden" value="jWRFxrnJNt42dhgyJoY87pS28rKY5zM9VG6/Eu6FF+tDEmrjppoTVitZizI5xBqA2610MBKV+nxHHrUcz2bMlg==" /></div>
            <button
                type="submit"
                class="btn btn-sm btn-with-count"
                data-ga-click="Repository, show fork modal, action:blob#show; text:Fork"
                title="Fork your own copy of google/python-fire to your account"
                aria-label="Fork your own copy of google/python-fire to your account">
              <svg aria-hidden="true" class="octicon octicon-repo-forked" height="16" version="1.1" viewBox="0 0 10 16" width="10"><path fill-rule="evenodd" d="M8 1a1.993 1.993 0 0 0-1 3.72V6L5 8 3 6V4.72A1.993 1.993 0 0 0 2 1a1.993 1.993 0 0 0-1 3.72V6.5l3 3v1.78A1.993 1.993 0 0 0 5 15a1.993 1.993 0 0 0 1-3.72V9.5l3-3V4.72A1.993 1.993 0 0 0 8 1zM2 4.2C1.34 4.2.8 3.65.8 3c0-.65.55-1.2 1.2-1.2.65 0 1.2.55 1.2 1.2 0 .65-.55 1.2-1.2 1.2zm3 10c-.66 0-1.2-.55-1.2-1.2 0-.65.55-1.2 1.2-1.2.65 0 1.2.55 1.2 1.2 0 .65-.55 1.2-1.2 1.2zm3-10c-.66 0-1.2-.55-1.2-1.2 0-.65.55-1.2 1.2-1.2.65 0 1.2.55 1.2 1.2 0 .65-.55 1.2-1.2 1.2z"/></svg>
              Fork
            </button>
</form>
    <a href="/google/python-fire/network" class="social-count"
       aria-label="433 users forked this repository">
      433
    </a>
  </li>
</ul>

      <h1 class="public ">
  <svg aria-hidden="true" class="octicon octicon-repo" height="16" version="1.1" viewBox="0 0 12 16" width="12"><path fill-rule="evenodd" d="M4 9H3V8h1v1zm0-3H3v1h1V6zm0-2H3v1h1V4zm0-2H3v1h1V2zm8-1v12c0 .55-.45 1-1 1H6v2l-1.5-1.5L3 16v-2H1c-.55 0-1-.45-1-1V1c0-.55.45-1 1-1h10c.55 0 1 .45 1 1zm-1 10H1v2h2v-1h3v1h5v-2zm0-10H2v9h9V1z"/></svg>
  <span class="author" itemprop="author"><a href="/google" class="url fn" rel="author">google</a></span><!--
--><span class="path-divider">/</span><!--
--><strong itemprop="name"><a href="/google/python-fire" data-pjax="#js-repo-pjax-container">python-fire</a></strong>

</h1>

    </div>
    
<nav class="reponav js-repo-nav js-sidenav-container-pjax container"
     itemscope
     itemtype="http://schema.org/BreadcrumbList"
     role="navigation"
     data-pjax="#js-repo-pjax-container">

  <span itemscope itemtype="http://schema.org/ListItem" itemprop="itemListElement">
    <a href="/google/python-fire" class="js-selected-navigation-item selected reponav-item" data-hotkey="g c" data-selected-links="repo_source repo_downloads repo_commits repo_releases repo_tags repo_branches repo_packages /google/python-fire" itemprop="url">
      <svg aria-hidden="true" class="octicon octicon-code" height="16" version="1.1" viewBox="0 0 14 16" width="14"><path fill-rule="evenodd" d="M9.5 3L8 4.5 11.5 8 8 11.5 9.5 13 14 8 9.5 3zm-5 0L0 8l4.5 5L6 11.5 2.5 8 6 4.5 4.5 3z"/></svg>
      <span itemprop="name">Code</span>
      <meta itemprop="position" content="1">
</a>  </span>

    <span itemscope itemtype="http://schema.org/ListItem" itemprop="itemListElement">
      <a href="/google/python-fire/issues" class="js-selected-navigation-item reponav-item" data-hotkey="g i" data-selected-links="repo_issues repo_labels repo_milestones /google/python-fire/issues" itemprop="url">
        <svg aria-hidden="true" class="octicon octicon-issue-opened" height="16" version="1.1" viewBox="0 0 14 16" width="14"><path fill-rule="evenodd" d="M7 2.3c3.14 0 5.7 2.56 5.7 5.7s-2.56 5.7-5.7 5.7A5.71 5.71 0 0 1 1.3 8c0-3.14 2.56-5.7 5.7-5.7zM7 1C3.14 1 0 4.14 0 8s3.14 7 7 7 7-3.14 7-7-3.14-7-7-7zm1 3H6v5h2V4zm0 6H6v2h2v-2z"/></svg>
        <span itemprop="name">Issues</span>
        <span class="Counter">29</span>
        <meta itemprop="position" content="2">
</a>    </span>

  <span itemscope itemtype="http://schema.org/ListItem" itemprop="itemListElement">
    <a href="/google/python-fire/pulls" class="js-selected-navigation-item reponav-item" data-hotkey="g p" data-selected-links="repo_pulls /google/python-fire/pulls" itemprop="url">
      <svg aria-hidden="true" class="octicon octicon-git-pull-request" height="16" version="1.1" viewBox="0 0 12 16" width="12"><path fill-rule="evenodd" d="M11 11.28V5c-.03-.78-.34-1.47-.94-2.06C9.46 2.35 8.78 2.03 8 2H7V0L4 3l3 3V4h1c.27.02.48.11.69.31.21.2.3.42.31.69v6.28A1.993 1.993 0 0 0 10 15a1.993 1.993 0 0 0 1-3.72zm-1 2.92c-.66 0-1.2-.55-1.2-1.2 0-.65.55-1.2 1.2-1.2.65 0 1.2.55 1.2 1.2 0 .65-.55 1.2-1.2 1.2zM4 3c0-1.11-.89-2-2-2a1.993 1.993 0 0 0-1 3.72v6.56A1.993 1.993 0 0 0 2 15a1.993 1.993 0 0 0 1-3.72V4.72c.59-.34 1-.98 1-1.72zm-.8 10c0 .66-.55 1.2-1.2 1.2-.65 0-1.2-.55-1.2-1.2 0-.65.55-1.2 1.2-1.2.65 0 1.2.55 1.2 1.2zM2 4.2C1.34 4.2.8 3.65.8 3c0-.65.55-1.2 1.2-1.2.65 0 1.2.55 1.2 1.2 0 .65-.55 1.2-1.2 1.2z"/></svg>
      <span itemprop="name">Pull requests</span>
      <span class="Counter">6</span>
      <meta itemprop="position" content="3">
</a>  </span>

    <a href="/google/python-fire/projects" class="js-selected-navigation-item reponav-item" data-hotkey="g b" data-selected-links="repo_projects new_repo_project repo_project /google/python-fire/projects">
      <svg aria-hidden="true" class="octicon octicon-project" height="16" version="1.1" viewBox="0 0 15 16" width="15"><path fill-rule="evenodd" d="M10 12h3V2h-3v10zm-4-2h3V2H6v8zm-4 4h3V2H2v12zm-1 1h13V1H1v14zM14 0H1a1 1 0 0 0-1 1v14a1 1 0 0 0 1 1h13a1 1 0 0 0 1-1V1a1 1 0 0 0-1-1z"/></svg>
      Projects
      <span class="Counter" >0</span>
</a>


  <a href="/google/python-fire/pulse" class="js-selected-navigation-item reponav-item" data-selected-links="repo_graphs repo_contributors dependency_graph pulse /google/python-fire/pulse">
    <svg aria-hidden="true" class="octicon octicon-graph" height="16" version="1.1" viewBox="0 0 16 16" width="16"><path fill-rule="evenodd" d="M16 14v1H0V0h1v14h15zM5 13H3V8h2v5zm4 0H7V3h2v10zm4 0h-2V6h2v7z"/></svg>
    Insights
</a>

</nav>


  </div>

<div class="container new-discussion-timeline experiment-repo-nav  ">
  <div class="repository-content ">

    
  <a href="/google/python-fire/blob/9bff9d01ce16589201f57ffef27ea84744951c11/docs/guide.md" class="d-none js-permalink-shortcut" data-hotkey="y">Permalink</a>

  <!-- blob contrib key: blob_contributors:v21:5147c9a005ddd961e02acd886a571708 -->

  <div class="file-navigation js-zeroclipboard-container">
    
<div class="select-menu branch-select-menu js-menu-container js-select-menu float-left">
  <button class=" btn btn-sm select-menu-button js-menu-target css-truncate" data-hotkey="w"
    
    type="button" aria-label="Switch branches or tags" aria-expanded="false" aria-haspopup="true">
      <i>Branch:</i>
      <span class="js-select-button css-truncate-target">master</span>
  </button>

  <div class="select-menu-modal-holder js-menu-content js-navigation-container" data-pjax>

    <div class="select-menu-modal">
      <div class="select-menu-header">
        <svg aria-label="Close" class="octicon octicon-x js-menu-close" height="16" role="img" version="1.1" viewBox="0 0 12 16" width="12"><path fill-rule="evenodd" d="M7.48 8l3.75 3.75-1.48 1.48L6 9.48l-3.75 3.75-1.48-1.48L4.52 8 .77 4.25l1.48-1.48L6 6.52l3.75-3.75 1.48 1.48z"/></svg>
        <span class="select-menu-title">Switch branches/tags</span>
      </div>

      <div class="select-menu-filters">
        <div class="select-menu-text-filter">
          <input type="text" aria-label="Filter branches/tags" id="context-commitish-filter-field" class="form-control js-filterable-field js-navigation-enable" placeholder="Filter branches/tags">
        </div>
        <div class="select-menu-tabs">
          <ul>
            <li class="select-menu-tab">
              <a href="#" data-tab-filter="branches" data-filter-placeholder="Filter branches/tags" class="js-select-menu-tab" role="tab">Branches</a>
            </li>
            <li class="select-menu-tab">
              <a href="#" data-tab-filter="tags" data-filter-placeholder="Find a tag…" class="js-select-menu-tab" role="tab">Tags</a>
            </li>
          </ul>
        </div>
      </div>

      <div class="select-menu-list select-menu-tab-bucket js-select-menu-tab-bucket" data-tab-filter="branches" role="menu">

        <div data-filterable-for="context-commitish-filter-field" data-filterable-type="substring">


            <a class="select-menu-item js-navigation-item js-navigation-open "
               href="/google/python-fire/blob/copybara/docs/guide.md"
               data-name="copybara"
               data-skip-pjax="true"
               rel="nofollow">
              <svg aria-hidden="true" class="octicon octicon-check select-menu-item-icon" height="16" version="1.1" viewBox="0 0 12 16" width="12"><path fill-rule="evenodd" d="M12 5l-8 8-4-4 1.5-1.5L4 10l6.5-6.5z"/></svg>
              <span class="select-menu-item-text css-truncate-target js-select-menu-filter-text">
                copybara
              </span>
            </a>
            <a class="select-menu-item js-navigation-item js-navigation-open "
               href="/google/python-fire/blob/gh-pages/docs/guide.md"
               data-name="gh-pages"
               data-skip-pjax="true"
               rel="nofollow">
              <svg aria-hidden="true" class="octicon octicon-check select-menu-item-icon" height="16" version="1.1" viewBox="0 0 12 16" width="12"><path fill-rule="evenodd" d="M12 5l-8 8-4-4 1.5-1.5L4 10l6.5-6.5z"/></svg>
              <span class="select-menu-item-text css-truncate-target js-select-menu-filter-text">
                gh-pages
              </span>
            </a>
            <a class="select-menu-item js-navigation-item js-navigation-open "
               href="/google/python-fire/blob/issue29-fire-without-edits/docs/guide.md"
               data-name="issue29-fire-without-edits"
               data-skip-pjax="true"
               rel="nofollow">
              <svg aria-hidden="true" class="octicon octicon-check select-menu-item-icon" height="16" version="1.1" viewBox="0 0 12 16" width="12"><path fill-rule="evenodd" d="M12 5l-8 8-4-4 1.5-1.5L4 10l6.5-6.5z"/></svg>
              <span class="select-menu-item-text css-truncate-target js-select-menu-filter-text">
                issue29-fire-without-edits
              </span>
            </a>
            <a class="select-menu-item js-navigation-item js-navigation-open selected"
               href="/google/python-fire/blob/master/docs/guide.md"
               data-name="master"
               data-skip-pjax="true"
               rel="nofollow">
              <svg aria-hidden="true" class="octicon octicon-check select-menu-item-icon" height="16" version="1.1" viewBox="0 0 12 16" width="12"><path fill-rule="evenodd" d="M12 5l-8 8-4-4 1.5-1.5L4 10l6.5-6.5z"/></svg>
              <span class="select-menu-item-text css-truncate-target js-select-menu-filter-text">
                master
              </span>
            </a>
        </div>

          <div class="select-menu-no-results">Nothing to show</div>
      </div>

      <div class="select-menu-list select-menu-tab-bucket js-select-menu-tab-bucket" data-tab-filter="tags">
        <div data-filterable-for="context-commitish-filter-field" data-filterable-type="substring">


            <a class="select-menu-item js-navigation-item js-navigation-open "
              href="/google/python-fire/tree/v0.1.2/docs/guide.md"
              data-name="v0.1.2"
              data-skip-pjax="true"
              rel="nofollow">
              <svg aria-hidden="true" class="octicon octicon-check select-menu-item-icon" height="16" version="1.1" viewBox="0 0 12 16" width="12"><path fill-rule="evenodd" d="M12 5l-8 8-4-4 1.5-1.5L4 10l6.5-6.5z"/></svg>
              <span class="select-menu-item-text css-truncate-target" title="v0.1.2">
                v0.1.2
              </span>
            </a>
            <a class="select-menu-item js-navigation-item js-navigation-open "
              href="/google/python-fire/tree/v0.1.1/docs/guide.md"
              data-name="v0.1.1"
              data-skip-pjax="true"
              rel="nofollow">
              <svg aria-hidden="true" class="octicon octicon-check select-menu-item-icon" height="16" version="1.1" viewBox="0 0 12 16" width="12"><path fill-rule="evenodd" d="M12 5l-8 8-4-4 1.5-1.5L4 10l6.5-6.5z"/></svg>
              <span class="select-menu-item-text css-truncate-target" title="v0.1.1">
                v0.1.1
              </span>
            </a>
            <a class="select-menu-item js-navigation-item js-navigation-open "
              href="/google/python-fire/tree/v0.1.0/docs/guide.md"
              data-name="v0.1.0"
              data-skip-pjax="true"
              rel="nofollow">
              <svg aria-hidden="true" class="octicon octicon-check select-menu-item-icon" height="16" version="1.1" viewBox="0 0 12 16" width="12"><path fill-rule="evenodd" d="M12 5l-8 8-4-4 1.5-1.5L4 10l6.5-6.5z"/></svg>
              <span class="select-menu-item-text css-truncate-target" title="v0.1.0">
                v0.1.0
              </span>
            </a>
        </div>

        <div class="select-menu-no-results">Nothing to show</div>
      </div>

    </div>
  </div>
</div>

    <div class="BtnGroup float-right">
      <a href="/google/python-fire/find/master"
            class="js-pjax-capture-input btn btn-sm BtnGroup-item"
            data-pjax
            data-hotkey="t">
        Find file
      </a>
      <button aria-label="Copy file path to clipboard" class="js-zeroclipboard btn btn-sm BtnGroup-item tooltipped tooltipped-s" data-copied-hint="Copied!" type="button">Copy path</button>
    </div>
    <div class="breadcrumb js-zeroclipboard-target">
      <span class="repo-root js-repo-root"><span class="js-path-segment"><a href="/google/python-fire" data-pjax="true"><span>python-fire</span></a></span></span><span class="separator">/</span><span class="js-path-segment"><a href="/google/python-fire/tree/master/docs" data-pjax="true"><span>docs</span></a></span><span class="separator">/</span><strong class="final-path">guide.md</strong>
    </div>
  </div>


  
  <div class="commit-tease">
      <span class="float-right">
        <a class="commit-tease-sha" href="/google/python-fire/commit/84c5a46d94c91e64a9ccb6550e8ac8ce278fad25" data-pjax>
          84c5a46
        </a>
        <relative-time datetime="2017-07-17T20:40:19Z">Jul 17, 2017</relative-time>
      </span>
      <div>
        <img alt="@dbieber" class="avatar" height="20" src="https://avatars3.githubusercontent.com/u/892765?s=40&amp;v=4" width="20" />
        <a href="/dbieber" class="user-mention" rel="contributor">dbieber</a>
          <a href="/google/python-fire/commit/84c5a46d94c91e64a9ccb6550e8ac8ce278fad25" class="message" data-pjax="true" title="- Rename doc to docs in preparation for adding mkdocs support.
- Adds additional public documentation to Python Fire.

Copybara generated commit for Python Fire.

PiperOrigin-RevId: 162004265
Change-Id: I356c966d74d2270cc59abaff7238913339d17609
Reviewed-on: https://team-review.git.corp.google.com/82464
Reviewed-by: David Bieber &lt;dbieber@google.com&gt;">- Rename doc to docs in preparation for adding mkdocs support.</a>
      </div>

    <div class="commit-tease-contributors">
      <button type="button" class="btn-link muted-link contributors-toggle" data-facebox="#blob_contributors_box">
        <strong>1</strong>
         contributor
      </button>
      
    </div>

    <div id="blob_contributors_box" style="display:none">
      <h2 class="facebox-header" data-facebox-id="facebox-header">Users who have contributed to this file</h2>
      <ul class="facebox-user-list" data-facebox-id="facebox-description">
          <li class="facebox-user-list-item">
            <img alt="@dbieber" height="24" src="https://avatars2.githubusercontent.com/u/892765?s=48&amp;v=4" width="24" />
            <a href="/dbieber">dbieber</a>
          </li>
      </ul>
    </div>
  </div>


  <div class="file">
    <div class="file-header">
  <div class="file-actions">

    <div class="BtnGroup">
      <a href="/google/python-fire/raw/master/docs/guide.md" class="btn btn-sm BtnGroup-item" id="raw-url">Raw</a>
        <a href="/google/python-fire/blame/master/docs/guide.md" class="btn btn-sm js-update-url-with-hash BtnGroup-item" data-hotkey="b">Blame</a>
      <a href="/google/python-fire/commits/master/docs/guide.md" class="btn btn-sm BtnGroup-item" rel="nofollow">History</a>
    </div>

        <a class="btn-octicon tooltipped tooltipped-nw"
           href="x-github-client://openRepo/https://github.com/google/python-fire?branch=master&amp;filepath=docs%2Fguide.md"
           aria-label="Open this file in GitHub Desktop"
           data-ga-click="Repository, open with desktop, type:windows">
            <svg aria-hidden="true" class="octicon octicon-device-desktop" height="16" version="1.1" viewBox="0 0 16 16" width="16"><path fill-rule="evenodd" d="M15 2H1c-.55 0-1 .45-1 1v9c0 .55.45 1 1 1h5.34c-.25.61-.86 1.39-2.34 2h8c-1.48-.61-2.09-1.39-2.34-2H15c.55 0 1-.45 1-1V3c0-.55-.45-1-1-1zm0 9H1V3h14v8z"/></svg>
        </a>

          <!-- '"` --><!-- </textarea></xmp> --></option></form><form accept-charset="UTF-8" action="/google/python-fire/edit/master/docs/guide.md" class="inline-form js-update-url-with-hash" method="post"><div style="margin:0;padding:0;display:inline"><input name="utf8" type="hidden" value="&#x2713;" /><input name="authenticity_token" type="hidden" value="Jd3tGPQtOxd+/VQD5wXxzoaXuArt72jQ7VbiduZmOsh5IA/o94aCeUacx7HYyLDfUwOABcCv8RBQ35V0PWqsFA==" /></div>
            <button class="btn-octicon tooltipped tooltipped-nw" type="submit"
              aria-label="Fork this project and edit the file" data-hotkey="e" data-disable-with>
              <svg aria-hidden="true" class="octicon octicon-pencil" height="16" version="1.1" viewBox="0 0 14 16" width="14"><path fill-rule="evenodd" d="M0 12v3h3l8-8-3-3-8 8zm3 2H1v-2h1v1h1v1zm10.3-9.3L12 6 9 3l1.3-1.3a.996.996 0 0 1 1.41 0l1.59 1.59c.39.39.39 1.02 0 1.41z"/></svg>
            </button>
</form>
        <!-- '"` --><!-- </textarea></xmp> --></option></form><form accept-charset="UTF-8" action="/google/python-fire/delete/master/docs/guide.md" class="inline-form" method="post"><div style="margin:0;padding:0;display:inline"><input name="utf8" type="hidden" value="&#x2713;" /><input name="authenticity_token" type="hidden" value="ulM02nP5tuT4LE72W7Q+EWdqWMRT/EJXZB0FAoDodUJIGvef0YpJ0PENeNvaPLqkK55sGGHwwiNaDoUbbPBaQA==" /></div>
          <button class="btn-octicon btn-octicon-danger tooltipped tooltipped-nw" type="submit"
            aria-label="Fork this project and delete the file" data-disable-with>
            <svg aria-hidden="true" class="octicon octicon-trashcan" height="16" version="1.1" viewBox="0 0 12 16" width="12"><path fill-rule="evenodd" d="M11 2H9c0-.55-.45-1-1-1H5c-.55 0-1 .45-1 1H2c-.55 0-1 .45-1 1v1c0 .55.45 1 1 1v9c0 .55.45 1 1 1h7c.55 0 1-.45 1-1V5c.55 0 1-.45 1-1V3c0-.55-.45-1-1-1zm-1 12H3V5h1v8h1V5h1v8h1V5h1v8h1V5h1v9zm1-10H2V3h9v1z"/></svg>
          </button>
</form>  </div>

  <div class="file-info">
      715 lines (515 sloc)
      <span class="file-info-divider"></span>
    17 KB
  </div>
</div>

    
  <div id="readme" class="readme blob instapaper_body">
    <article class="markdown-body entry-content" itemprop="text"><h2><a href="#the-python-fire-guide" aria-hidden="true" class="anchor" id="user-content-the-python-fire-guide"><svg aria-hidden="true" class="octicon octicon-link" height="16" version="1.1" viewBox="0 0 16 16" width="16"><path fill-rule="evenodd" d="M4 9h1v1H4c-1.5 0-3-1.69-3-3.5S2.55 3 4 3h4c1.45 0 3 1.69 3 3.5 0 1.41-.91 2.72-2 3.25V8.59c.58-.45 1-1.27 1-2.09C10 5.22 8.98 4 8 4H4c-.98 0-2 1.22-2 2.5S3 9 4 9zm9-3h-1v1h1c1 0 2 1.22 2 2.5S13.98 12 13 12H9c-.98 0-2-1.22-2-2.5 0-.83.42-1.64 1-2.09V6.25c-1.09.53-2 1.84-2 3.25C6 11.31 7.55 13 9 13h4c1.45 0 3-1.69 3-3.5S14.5 6 13 6z"></path></svg></a>The Python Fire Guide</h2>
<h3><a href="#introduction" aria-hidden="true" class="anchor" id="user-content-introduction"><svg aria-hidden="true" class="octicon octicon-link" height="16" version="1.1" viewBox="0 0 16 16" width="16"><path fill-rule="evenodd" d="M4 9h1v1H4c-1.5 0-3-1.69-3-3.5S2.55 3 4 3h4c1.45 0 3 1.69 3 3.5 0 1.41-.91 2.72-2 3.25V8.59c.58-.45 1-1.27 1-2.09C10 5.22 8.98 4 8 4H4c-.98 0-2 1.22-2 2.5S3 9 4 9zm9-3h-1v1h1c1 0 2 1.22 2 2.5S13.98 12 13 12H9c-.98 0-2-1.22-2-2.5 0-.83.42-1.64 1-2.09V6.25c-1.09.53-2 1.84-2 3.25C6 11.31 7.55 13 9 13h4c1.45 0 3-1.69 3-3.5S14.5 6 13 6z"></path></svg></a>Introduction</h3>
<p>Welcome to the Python Fire guide! Python Fire is a Python library that will turn
any Python component into a command line interface with just a single call to
<code>Fire</code>.</p>
<p>Let's get started!</p>
<h3><a href="#installation" aria-hidden="true" class="anchor" id="user-content-installation"><svg aria-hidden="true" class="octicon octicon-link" height="16" version="1.1" viewBox="0 0 16 16" width="16"><path fill-rule="evenodd" d="M4 9h1v1H4c-1.5 0-3-1.69-3-3.5S2.55 3 4 3h4c1.45 0 3 1.69 3 3.5 0 1.41-.91 2.72-2 3.25V8.59c.58-.45 1-1.27 1-2.09C10 5.22 8.98 4 8 4H4c-.98 0-2 1.22-2 2.5S3 9 4 9zm9-3h-1v1h1c1 0 2 1.22 2 2.5S13.98 12 13 12H9c-.98 0-2-1.22-2-2.5 0-.83.42-1.64 1-2.09V6.25c-1.09.53-2 1.84-2 3.25C6 11.31 7.55 13 9 13h4c1.45 0 3-1.69 3-3.5S14.5 6 13 6z"></path></svg></a>Installation</h3>
<p>To install Python Fire from pypi, run:</p>
<p><code>pip install fire</code></p>
<p>Alternatively, to install Python Fire from source, clone the source and run:</p>
<p><code>python setup.py install</code></p>
<h3><a href="#hello-world" aria-hidden="true" class="anchor" id="user-content-hello-world"><svg aria-hidden="true" class="octicon octicon-link" height="16" version="1.1" viewBox="0 0 16 16" width="16"><path fill-rule="evenodd" d="M4 9h1v1H4c-1.5 0-3-1.69-3-3.5S2.55 3 4 3h4c1.45 0 3 1.69 3 3.5 0 1.41-.91 2.72-2 3.25V8.59c.58-.45 1-1.27 1-2.09C10 5.22 8.98 4 8 4H4c-.98 0-2 1.22-2 2.5S3 9 4 9zm9-3h-1v1h1c1 0 2 1.22 2 2.5S13.98 12 13 12H9c-.98 0-2-1.22-2-2.5 0-.83.42-1.64 1-2.09V6.25c-1.09.53-2 1.84-2 3.25C6 11.31 7.55 13 9 13h4c1.45 0 3-1.69 3-3.5S14.5 6 13 6z"></path></svg></a>Hello World</h3>
<h5><a href="#version-1-firefire" aria-hidden="true" class="anchor" id="user-content-version-1-firefire"><svg aria-hidden="true" class="octicon octicon-link" height="16" version="1.1" viewBox="0 0 16 16" width="16"><path fill-rule="evenodd" d="M4 9h1v1H4c-1.5 0-3-1.69-3-3.5S2.55 3 4 3h4c1.45 0 3 1.69 3 3.5 0 1.41-.91 2.72-2 3.25V8.59c.58-.45 1-1.27 1-2.09C10 5.22 8.98 4 8 4H4c-.98 0-2 1.22-2 2.5S3 9 4 9zm9-3h-1v1h1c1 0 2 1.22 2 2.5S13.98 12 13 12H9c-.98 0-2-1.22-2-2.5 0-.83.42-1.64 1-2.09V6.25c-1.09.53-2 1.84-2 3.25C6 11.31 7.55 13 9 13h4c1.45 0 3-1.69 3-3.5S14.5 6 13 6z"></path></svg></a>Version 1: <code>fire.Fire()</code></h5>
<p>The easiest way to use Fire is to take any Python program, and then simply call
<code>fire.Fire()</code> at the end of the program. This will expose the full contents of
the program to the command line.</p>
<div class="highlight highlight-source-python"><pre><span class="pl-k">import</span> fire

<span class="pl-k">def</span> <span class="pl-en">hello</span>(<span class="pl-smi">name</span>):
  <span class="pl-k">return</span> <span class="pl-s"><span class="pl-pds">'</span>Hello <span class="pl-c1">{name}</span>!<span class="pl-pds">'</span></span>.format(<span class="pl-v">name</span><span class="pl-k">=</span>name)

<span class="pl-k">if</span> <span class="pl-c1">__name__</span> <span class="pl-k">==</span> <span class="pl-s"><span class="pl-pds">'</span>__main__<span class="pl-pds">'</span></span>:
  fire.Fire()</pre></div>
<p>Here's how we can run our program from the command line:</p>
<div class="highlight highlight-source-shell"><pre>$ python example.py hello World
Hello World<span class="pl-k">!</span></pre></div>
<h5><a href="#version-2-firefirefn" aria-hidden="true" class="anchor" id="user-content-version-2-firefirefn"><svg aria-hidden="true" class="octicon octicon-link" height="16" version="1.1" viewBox="0 0 16 16" width="16"><path fill-rule="evenodd" d="M4 9h1v1H4c-1.5 0-3-1.69-3-3.5S2.55 3 4 3h4c1.45 0 3 1.69 3 3.5 0 1.41-.91 2.72-2 3.25V8.59c.58-.45 1-1.27 1-2.09C10 5.22 8.98 4 8 4H4c-.98 0-2 1.22-2 2.5S3 9 4 9zm9-3h-1v1h1c1 0 2 1.22 2 2.5S13.98 12 13 12H9c-.98 0-2-1.22-2-2.5 0-.83.42-1.64 1-2.09V6.25c-1.09.53-2 1.84-2 3.25C6 11.31 7.55 13 9 13h4c1.45 0 3-1.69 3-3.5S14.5 6 13 6z"></path></svg></a>Version 2: <code>fire.Fire(&lt;fn&gt;)</code></h5>
<p>Let's modify our program slightly to only expose the <code>hello</code> function to the
command line.</p>
<div class="highlight highlight-source-python"><pre><span class="pl-k">import</span> fire

<span class="pl-k">def</span> <span class="pl-en">hello</span>(<span class="pl-smi">name</span>):
  <span class="pl-k">return</span> <span class="pl-s"><span class="pl-pds">'</span>Hello <span class="pl-c1">{name}</span>!<span class="pl-pds">'</span></span>.format(<span class="pl-v">name</span><span class="pl-k">=</span>name)

<span class="pl-k">if</span> <span class="pl-c1">__name__</span> <span class="pl-k">==</span> <span class="pl-s"><span class="pl-pds">'</span>__main__<span class="pl-pds">'</span></span>:
  fire.Fire(hello)</pre></div>
<p>Here's how we can run this from the command line:</p>
<div class="highlight highlight-source-shell"><pre>$ python example.py World
Hello World<span class="pl-k">!</span></pre></div>
<p>Notice we no longer have to specify to run the <code>hello</code> function, because we
called <code>fire.Fire(hello)</code>.</p>
<h5><a href="#version-3-using-a-main" aria-hidden="true" class="anchor" id="user-content-version-3-using-a-main"><svg aria-hidden="true" class="octicon octicon-link" height="16" version="1.1" viewBox="0 0 16 16" width="16"><path fill-rule="evenodd" d="M4 9h1v1H4c-1.5 0-3-1.69-3-3.5S2.55 3 4 3h4c1.45 0 3 1.69 3 3.5 0 1.41-.91 2.72-2 3.25V8.59c.58-.45 1-1.27 1-2.09C10 5.22 8.98 4 8 4H4c-.98 0-2 1.22-2 2.5S3 9 4 9zm9-3h-1v1h1c1 0 2 1.22 2 2.5S13.98 12 13 12H9c-.98 0-2-1.22-2-2.5 0-.83.42-1.64 1-2.09V6.25c-1.09.53-2 1.84-2 3.25C6 11.31 7.55 13 9 13h4c1.45 0 3-1.69 3-3.5S14.5 6 13 6z"></path></svg></a>Version 3: Using a main</h5>
<p>We can alternatively write this program like this:</p>
<div class="highlight highlight-source-python"><pre><span class="pl-k">import</span> fire

<span class="pl-k">def</span> <span class="pl-en">hello</span>(<span class="pl-smi">name</span>):
  <span class="pl-k">return</span> <span class="pl-s"><span class="pl-pds">'</span>Hello <span class="pl-c1">{name}</span>!<span class="pl-pds">'</span></span>.format(<span class="pl-v">name</span><span class="pl-k">=</span>name)

<span class="pl-k">def</span> <span class="pl-en">main</span>():
  fire.Fire(hello)

<span class="pl-k">if</span> <span class="pl-c1">__name__</span> <span class="pl-k">==</span> <span class="pl-s"><span class="pl-pds">'</span>__main__<span class="pl-pds">'</span></span>:
  main()</pre></div>
<p>Or if we're using
<a href="https://setuptools.readthedocs.io/en/latest/pkg_resources.html#entry-points" rel="nofollow">entry points</a>,
then simply this:</p>
<div class="highlight highlight-source-python"><pre><span class="pl-k">import</span> fire

<span class="pl-k">def</span> <span class="pl-en">hello</span>(<span class="pl-smi">name</span>):
  <span class="pl-k">return</span> <span class="pl-s"><span class="pl-pds">'</span>Hello <span class="pl-c1">{name}</span>!<span class="pl-pds">'</span></span>.format(<span class="pl-v">name</span><span class="pl-k">=</span>name)

<span class="pl-k">def</span> <span class="pl-en">main</span>():
  fire.Fire(hello)</pre></div>
<h3><a href="#exposing-multiple-commands" aria-hidden="true" class="anchor" id="user-content-exposing-multiple-commands"><svg aria-hidden="true" class="octicon octicon-link" height="16" version="1.1" viewBox="0 0 16 16" width="16"><path fill-rule="evenodd" d="M4 9h1v1H4c-1.5 0-3-1.69-3-3.5S2.55 3 4 3h4c1.45 0 3 1.69 3 3.5 0 1.41-.91 2.72-2 3.25V8.59c.58-.45 1-1.27 1-2.09C10 5.22 8.98 4 8 4H4c-.98 0-2 1.22-2 2.5S3 9 4 9zm9-3h-1v1h1c1 0 2 1.22 2 2.5S13.98 12 13 12H9c-.98 0-2-1.22-2-2.5 0-.83.42-1.64 1-2.09V6.25c-1.09.53-2 1.84-2 3.25C6 11.31 7.55 13 9 13h4c1.45 0 3-1.69 3-3.5S14.5 6 13 6z"></path></svg></a>Exposing Multiple Commands</h3>
<p>In the previous example, we exposed a single function to the command line. Now
we'll look at ways of exposing multiple functions to the command line.</p>
<h5><a href="#version-1-firefire-1" aria-hidden="true" class="anchor" id="user-content-version-1-firefire-1"><svg aria-hidden="true" class="octicon octicon-link" height="16" version="1.1" viewBox="0 0 16 16" width="16"><path fill-rule="evenodd" d="M4 9h1v1H4c-1.5 0-3-1.69-3-3.5S2.55 3 4 3h4c1.45 0 3 1.69 3 3.5 0 1.41-.91 2.72-2 3.25V8.59c.58-.45 1-1.27 1-2.09C10 5.22 8.98 4 8 4H4c-.98 0-2 1.22-2 2.5S3 9 4 9zm9-3h-1v1h1c1 0 2 1.22 2 2.5S13.98 12 13 12H9c-.98 0-2-1.22-2-2.5 0-.83.42-1.64 1-2.09V6.25c-1.09.53-2 1.84-2 3.25C6 11.31 7.55 13 9 13h4c1.45 0 3-1.69 3-3.5S14.5 6 13 6z"></path></svg></a>Version 1: <code>fire.Fire()</code></h5>
<p>The simplest way to expose multiple commands is to write multiple functions, and
then call Fire.</p>
<div class="highlight highlight-source-python"><pre><span class="pl-k">import</span> fire

<span class="pl-k">def</span> <span class="pl-en">add</span>(<span class="pl-smi">x</span>, <span class="pl-smi">y</span>):
  <span class="pl-k">return</span> x <span class="pl-k">+</span> y

<span class="pl-k">def</span> <span class="pl-en">multiply</span>(<span class="pl-smi">x</span>, <span class="pl-smi">y</span>):
  <span class="pl-k">return</span> x <span class="pl-k">*</span> y

<span class="pl-k">if</span> <span class="pl-c1">__name__</span> <span class="pl-k">==</span> <span class="pl-s"><span class="pl-pds">'</span>__main__<span class="pl-pds">'</span></span>:
  fire.Fire()</pre></div>
<p>We can use this like so:</p>
<div class="highlight highlight-source-shell"><pre>$ python example.py add 10 20
30
$ python example.py multiply 10 20
200</pre></div>
<p>You'll notice that Fire correctly parsed <code>10</code> and <code>20</code> as numbers, rather than
as strings. Read more about <a href="#argument-parsing">argument parsing here</a>.</p>
<h5><a href="#version-2-firefiredict" aria-hidden="true" class="anchor" id="user-content-version-2-firefiredict"><svg aria-hidden="true" class="octicon octicon-link" height="16" version="1.1" viewBox="0 0 16 16" width="16"><path fill-rule="evenodd" d="M4 9h1v1H4c-1.5 0-3-1.69-3-3.5S2.55 3 4 3h4c1.45 0 3 1.69 3 3.5 0 1.41-.91 2.72-2 3.25V8.59c.58-.45 1-1.27 1-2.09C10 5.22 8.98 4 8 4H4c-.98 0-2 1.22-2 2.5S3 9 4 9zm9-3h-1v1h1c1 0 2 1.22 2 2.5S13.98 12 13 12H9c-.98 0-2-1.22-2-2.5 0-.83.42-1.64 1-2.09V6.25c-1.09.53-2 1.84-2 3.25C6 11.31 7.55 13 9 13h4c1.45 0 3-1.69 3-3.5S14.5 6 13 6z"></path></svg></a>Version 2: <code>fire.Fire(&lt;dict&gt;)</code></h5>
<p>In version 1 we exposed all the program's functionality to the command line. By
using a dict, we can selectively expose functions to the command line.</p>
<div class="highlight highlight-source-python"><pre><span class="pl-k">import</span> fire

<span class="pl-k">def</span> <span class="pl-en">add</span>(<span class="pl-smi">x</span>, <span class="pl-smi">y</span>):
  <span class="pl-k">return</span> x <span class="pl-k">+</span> y

<span class="pl-k">def</span> <span class="pl-en">multiply</span>(<span class="pl-smi">x</span>, <span class="pl-smi">y</span>):
  <span class="pl-k">return</span> x <span class="pl-k">*</span> y

<span class="pl-k">if</span> <span class="pl-c1">__name__</span> <span class="pl-k">==</span> <span class="pl-s"><span class="pl-pds">'</span>__main__<span class="pl-pds">'</span></span>:
  fire.Fire({
      <span class="pl-s"><span class="pl-pds">'</span>add<span class="pl-pds">'</span></span>: add,
      <span class="pl-s"><span class="pl-pds">'</span>multiply<span class="pl-pds">'</span></span>: multiply,
  })</pre></div>
<p>We can use this in the same way as before:</p>
<div class="highlight highlight-source-shell"><pre>$ python example.py add 10 20
30
$ python example.py multiply 10 20
200</pre></div>
<h5><a href="#version-3-firefireobject" aria-hidden="true" class="anchor" id="user-content-version-3-firefireobject"><svg aria-hidden="true" class="octicon octicon-link" height="16" version="1.1" viewBox="0 0 16 16" width="16"><path fill-rule="evenodd" d="M4 9h1v1H4c-1.5 0-3-1.69-3-3.5S2.55 3 4 3h4c1.45 0 3 1.69 3 3.5 0 1.41-.91 2.72-2 3.25V8.59c.58-.45 1-1.27 1-2.09C10 5.22 8.98 4 8 4H4c-.98 0-2 1.22-2 2.5S3 9 4 9zm9-3h-1v1h1c1 0 2 1.22 2 2.5S13.98 12 13 12H9c-.98 0-2-1.22-2-2.5 0-.83.42-1.64 1-2.09V6.25c-1.09.53-2 1.84-2 3.25C6 11.31 7.55 13 9 13h4c1.45 0 3-1.69 3-3.5S14.5 6 13 6z"></path></svg></a>Version 3: <code>fire.Fire(&lt;object&gt;)</code></h5>
<p>Fire also works on objects, as in this variant. This is a good way to expose
multiple commands.</p>
<div class="highlight highlight-source-python"><pre><span class="pl-k">import</span> fire

<span class="pl-k">class</span> <span class="pl-en">Calculator</span>(<span class="pl-c1">object</span>):

  <span class="pl-k">def</span> <span class="pl-en">add</span>(<span class="pl-smi"><span class="pl-smi">self</span></span>, <span class="pl-smi">x</span>, <span class="pl-smi">y</span>):
    <span class="pl-k">return</span> x <span class="pl-k">+</span> y

  <span class="pl-k">def</span> <span class="pl-en">multiply</span>(<span class="pl-smi"><span class="pl-smi">self</span></span>, <span class="pl-smi">x</span>, <span class="pl-smi">y</span>):
    <span class="pl-k">return</span> x <span class="pl-k">*</span> y

<span class="pl-k">if</span> <span class="pl-c1">__name__</span> <span class="pl-k">==</span> <span class="pl-s"><span class="pl-pds">'</span>__main__<span class="pl-pds">'</span></span>:
  calculator <span class="pl-k">=</span> Calculator()
  fire.Fire(calculator)</pre></div>
<p>We can use this in the same way as before:</p>
<div class="highlight highlight-source-shell"><pre>$ python example.py add 10 20
30
$ python example.py multiply 10 20
200</pre></div>
<h5><a href="#version-4-firefireclass" aria-hidden="true" class="anchor" id="user-content-version-4-firefireclass"><svg aria-hidden="true" class="octicon octicon-link" height="16" version="1.1" viewBox="0 0 16 16" width="16"><path fill-rule="evenodd" d="M4 9h1v1H4c-1.5 0-3-1.69-3-3.5S2.55 3 4 3h4c1.45 0 3 1.69 3 3.5 0 1.41-.91 2.72-2 3.25V8.59c.58-.45 1-1.27 1-2.09C10 5.22 8.98 4 8 4H4c-.98 0-2 1.22-2 2.5S3 9 4 9zm9-3h-1v1h1c1 0 2 1.22 2 2.5S13.98 12 13 12H9c-.98 0-2-1.22-2-2.5 0-.83.42-1.64 1-2.09V6.25c-1.09.53-2 1.84-2 3.25C6 11.31 7.55 13 9 13h4c1.45 0 3-1.69 3-3.5S14.5 6 13 6z"></path></svg></a>Version 4: <code>fire.Fire(&lt;class&gt;)</code></h5>
<p>Fire also works on classes. This is another good way to expose multiple
commands.</p>
<div class="highlight highlight-source-python"><pre><span class="pl-k">import</span> fire

<span class="pl-k">class</span> <span class="pl-en">Calculator</span>(<span class="pl-c1">object</span>):

  <span class="pl-k">def</span> <span class="pl-en">add</span>(<span class="pl-smi"><span class="pl-smi">self</span></span>, <span class="pl-smi">x</span>, <span class="pl-smi">y</span>):
    <span class="pl-k">return</span> x <span class="pl-k">+</span> y

  <span class="pl-k">def</span> <span class="pl-en">multiply</span>(<span class="pl-smi"><span class="pl-smi">self</span></span>, <span class="pl-smi">x</span>, <span class="pl-smi">y</span>):
    <span class="pl-k">return</span> x <span class="pl-k">*</span> y

<span class="pl-k">if</span> <span class="pl-c1">__name__</span> <span class="pl-k">==</span> <span class="pl-s"><span class="pl-pds">'</span>__main__<span class="pl-pds">'</span></span>:
  fire.Fire(Calculator)</pre></div>
<p>We can use this in the same way as before:</p>
<div class="highlight highlight-source-shell"><pre>$ python example.py add 10 20
30
$ python example.py multiply 10 20
200</pre></div>
<p>Why might you prefer a class over an object? One reason is that you can pass
arguments for constructing the class too, as in this broken calculator example.</p>
<div class="highlight highlight-source-python"><pre><span class="pl-k">import</span> fire

<span class="pl-k">class</span> <span class="pl-en">BrokenCalculator</span>(<span class="pl-c1">object</span>):

  <span class="pl-k">def</span> <span class="pl-c1">__init__</span>(<span class="pl-smi"><span class="pl-smi">self</span></span>, <span class="pl-smi">offset</span><span class="pl-k">=</span><span class="pl-c1">1</span>):
      <span class="pl-c1">self</span>._offset <span class="pl-k">=</span> offset

  <span class="pl-k">def</span> <span class="pl-en">add</span>(<span class="pl-smi"><span class="pl-smi">self</span></span>, <span class="pl-smi">x</span>, <span class="pl-smi">y</span>):
    <span class="pl-k">return</span> x <span class="pl-k">+</span> y <span class="pl-k">+</span> <span class="pl-c1">self</span>._offset

  <span class="pl-k">def</span> <span class="pl-en">multiply</span>(<span class="pl-smi"><span class="pl-smi">self</span></span>, <span class="pl-smi">x</span>, <span class="pl-smi">y</span>):
    <span class="pl-k">return</span> x <span class="pl-k">*</span> y <span class="pl-k">+</span> <span class="pl-c1">self</span>._offset

<span class="pl-k">if</span> <span class="pl-c1">__name__</span> <span class="pl-k">==</span> <span class="pl-s"><span class="pl-pds">'</span>__main__<span class="pl-pds">'</span></span>:
  fire.Fire(BrokenCalculator)</pre></div>
<p>When you use a broken calculator, you get wrong answers:</p>
<div class="highlight highlight-source-shell"><pre>$ python example.py add 10 20
31
$ python example.py multiply 10 20
201</pre></div>
<p>But you can always fix it:</p>
<div class="highlight highlight-source-shell"><pre>$ python example.py add 10 20 --offset=0
30
$ python example.py multiply 10 20 --offset=0
200</pre></div>
<p>Unlike calling ordinary functions, which can be done both with positional
arguments and named arguments (--flag syntax), arguments to __init__
functions must be passed with the --flag syntax. See the section on
<a href="#calling-functions">calling functions</a> for more.</p>
<h3><a href="#grouping-commands" aria-hidden="true" class="anchor" id="user-content-grouping-commands"><svg aria-hidden="true" class="octicon octicon-link" height="16" version="1.1" viewBox="0 0 16 16" width="16"><path fill-rule="evenodd" d="M4 9h1v1H4c-1.5 0-3-1.69-3-3.5S2.55 3 4 3h4c1.45 0 3 1.69 3 3.5 0 1.41-.91 2.72-2 3.25V8.59c.58-.45 1-1.27 1-2.09C10 5.22 8.98 4 8 4H4c-.98 0-2 1.22-2 2.5S3 9 4 9zm9-3h-1v1h1c1 0 2 1.22 2 2.5S13.98 12 13 12H9c-.98 0-2-1.22-2-2.5 0-.83.42-1.64 1-2.09V6.25c-1.09.53-2 1.84-2 3.25C6 11.31 7.55 13 9 13h4c1.45 0 3-1.69 3-3.5S14.5 6 13 6z"></path></svg></a>Grouping Commands</h3>
<p>Here's an example of how you might make a command line interface with grouped
commands.</p>
<div class="highlight highlight-source-python"><pre><span class="pl-k">class</span> <span class="pl-en">IngestionStage</span>(<span class="pl-c1">object</span>):

  <span class="pl-k">def</span> <span class="pl-en">run</span>(<span class="pl-smi"><span class="pl-smi">self</span></span>):
    <span class="pl-k">return</span> <span class="pl-s"><span class="pl-pds">'</span>Ingesting! Nom nom nom...<span class="pl-pds">'</span></span>

<span class="pl-k">class</span> <span class="pl-en">DigestionStage</span>(<span class="pl-c1">object</span>):

  <span class="pl-k">def</span> <span class="pl-en">run</span>(<span class="pl-smi"><span class="pl-smi">self</span></span>, <span class="pl-smi">volume</span><span class="pl-k">=</span><span class="pl-c1">1</span>):
    <span class="pl-k">return</span> <span class="pl-s"><span class="pl-pds">'</span> <span class="pl-pds">'</span></span>.join([<span class="pl-s"><span class="pl-pds">'</span>Burp!<span class="pl-pds">'</span></span>] <span class="pl-k">*</span> volume)

  <span class="pl-k">def</span> <span class="pl-en">status</span>(<span class="pl-smi"><span class="pl-smi">self</span></span>):
    <span class="pl-k">return</span> <span class="pl-s"><span class="pl-pds">'</span>Satiated.<span class="pl-pds">'</span></span>

<span class="pl-k">class</span> <span class="pl-en">Pipeline</span>(<span class="pl-c1">object</span>):

  <span class="pl-k">def</span> <span class="pl-c1">__init__</span>(<span class="pl-smi"><span class="pl-smi">self</span></span>):
    <span class="pl-c1">self</span>.ingestion <span class="pl-k">=</span> IngestionStage()
    <span class="pl-c1">self</span>.digestion <span class="pl-k">=</span> DigestionStage()

  <span class="pl-k">def</span> <span class="pl-en">run</span>(<span class="pl-smi"><span class="pl-smi">self</span></span>):
    <span class="pl-c1">self</span>.ingestion.run()
    <span class="pl-c1">self</span>.digestion.run()

<span class="pl-k">if</span> <span class="pl-c1">__name__</span> <span class="pl-k">==</span> <span class="pl-s"><span class="pl-pds">'</span>__main__<span class="pl-pds">'</span></span>:
  fire.Fire(Pipeline)</pre></div>
<p>Here's how this looks at the command line:</p>
<div class="highlight highlight-source-shell"><pre>$ python example.py run
Ingesting<span class="pl-k">!</span> Nom nom nom...
Burp<span class="pl-k">!</span>
$ python example.py ingestion run
Ingesting<span class="pl-k">!</span> Nom nom nom...
$ python example.py digestion run
Burp<span class="pl-k">!</span>
$ python example.py digestion status
Satiated.</pre></div>
<p>You can nest your commands in arbitrarily complex ways, if you're feeling grumpy
or adventurous.</p>
<h3><a href="#accessing-properties" aria-hidden="true" class="anchor" id="user-content-accessing-properties"><svg aria-hidden="true" class="octicon octicon-link" height="16" version="1.1" viewBox="0 0 16 16" width="16"><path fill-rule="evenodd" d="M4 9h1v1H4c-1.5 0-3-1.69-3-3.5S2.55 3 4 3h4c1.45 0 3 1.69 3 3.5 0 1.41-.91 2.72-2 3.25V8.59c.58-.45 1-1.27 1-2.09C10 5.22 8.98 4 8 4H4c-.98 0-2 1.22-2 2.5S3 9 4 9zm9-3h-1v1h1c1 0 2 1.22 2 2.5S13.98 12 13 12H9c-.98 0-2-1.22-2-2.5 0-.83.42-1.64 1-2.09V6.25c-1.09.53-2 1.84-2 3.25C6 11.31 7.55 13 9 13h4c1.45 0 3-1.69 3-3.5S14.5 6 13 6z"></path></svg></a>Accessing Properties</h3>
<p>In the examples we've looked at so far, our invocations of <code>python example.py</code>
have all run some function from the example program. In this example, we simply
access a property.</p>
<div class="highlight highlight-source-python"><pre><span class="pl-k">from</span> airports <span class="pl-k">import</span> airports

<span class="pl-k">import</span> fire

<span class="pl-k">class</span> <span class="pl-en">Airport</span>(<span class="pl-c1">object</span>):

  <span class="pl-k">def</span> <span class="pl-c1">__init__</span>(<span class="pl-smi"><span class="pl-smi">self</span></span>, <span class="pl-smi">code</span>):
    <span class="pl-c1">self</span>.code <span class="pl-k">=</span> code
    <span class="pl-c1">self</span>.name <span class="pl-k">=</span> <span class="pl-c1">dict</span>(airports).get(<span class="pl-c1">self</span>.code)
    <span class="pl-c1">self</span>.city <span class="pl-k">=</span> <span class="pl-c1">self</span>.name.split(<span class="pl-s"><span class="pl-pds">'</span>,<span class="pl-pds">'</span></span>)[<span class="pl-c1">0</span>] <span class="pl-k">if</span> <span class="pl-c1">self</span>.name <span class="pl-k">else</span> <span class="pl-c1">None</span>

<span class="pl-k">if</span> <span class="pl-c1">__name__</span> <span class="pl-k">==</span> <span class="pl-s"><span class="pl-pds">'</span>__main__<span class="pl-pds">'</span></span>:
  fire.Fire(Airport)</pre></div>
<p>Now we can use this program to learn about airport codes!</p>
<div class="highlight highlight-source-shell"><pre>$ python example.py --code=JFK code
JFK
$ python example.py --code=SJC name
San Jose-Sunnyvale-Santa Clara, CA - Norman Y. Mineta San Jose International (SJC)
$ python example.py --code=ALB city
Albany-Schenectady-Troy</pre></div>
<p>By the way, you can find this
<a href="https://github.com/trendct-data/airports.py">airports module here</a>.</p>
<h3><a href="#chaining-function-calls" aria-hidden="true" class="anchor" id="user-content-chaining-function-calls"><svg aria-hidden="true" class="octicon octicon-link" height="16" version="1.1" viewBox="0 0 16 16" width="16"><path fill-rule="evenodd" d="M4 9h1v1H4c-1.5 0-3-1.69-3-3.5S2.55 3 4 3h4c1.45 0 3 1.69 3 3.5 0 1.41-.91 2.72-2 3.25V8.59c.58-.45 1-1.27 1-2.09C10 5.22 8.98 4 8 4H4c-.98 0-2 1.22-2 2.5S3 9 4 9zm9-3h-1v1h1c1 0 2 1.22 2 2.5S13.98 12 13 12H9c-.98 0-2-1.22-2-2.5 0-.83.42-1.64 1-2.09V6.25c-1.09.53-2 1.84-2 3.25C6 11.31 7.55 13 9 13h4c1.45 0 3-1.69 3-3.5S14.5 6 13 6z"></path></svg></a>Chaining Function Calls</h3>
<p>When you run a Fire CLI, you can take all the same actions on the <em>result</em> of
the call to Fire that you can take on the original object passed in.</p>
<p>For example, we can use our Airport CLI from the previous example like this:</p>
<div class="highlight highlight-source-shell"><pre>$ python example.py --code=ALB city upper
ALBANY-SCHENECTADY-TROY</pre></div>
<p>This works since <code>upper</code> is a method on all strings.</p>
<p>So, if you want to set up your functions to chain nicely, all you have to do is
have a class whose methods return self. Here's an example.</p>
<div class="highlight highlight-source-python"><pre><span class="pl-k">import</span> fire

<span class="pl-k">class</span> <span class="pl-en">BinaryCanvas</span>(<span class="pl-c1">object</span>):
  <span class="pl-s"><span class="pl-pds">"""</span>A canvas with which to make binary art, one bit at a time.<span class="pl-pds">"""</span></span>

  <span class="pl-k">def</span> <span class="pl-c1">__init__</span>(<span class="pl-smi"><span class="pl-smi">self</span></span>, <span class="pl-smi">size</span><span class="pl-k">=</span><span class="pl-c1">10</span>):
    <span class="pl-c1">self</span>.pixels <span class="pl-k">=</span> [[<span class="pl-c1">0</span>] <span class="pl-k">*</span> size <span class="pl-k">for</span> _ <span class="pl-k">in</span> <span class="pl-c1">range</span>(size)]
    <span class="pl-c1">self</span>._size <span class="pl-k">=</span> size
    <span class="pl-c1">self</span>._row <span class="pl-k">=</span> <span class="pl-c1">0</span>  <span class="pl-c"><span class="pl-c">#</span> The row of the cursor.</span>
    <span class="pl-c1">self</span>._col <span class="pl-k">=</span> <span class="pl-c1">0</span>  <span class="pl-c"><span class="pl-c">#</span> The column of the cursor.</span>

  <span class="pl-k">def</span> <span class="pl-c1">__str__</span>(<span class="pl-smi"><span class="pl-smi">self</span></span>):
    <span class="pl-k">return</span> <span class="pl-s"><span class="pl-pds">'</span><span class="pl-cce">\n</span><span class="pl-pds">'</span></span>.join(<span class="pl-s"><span class="pl-pds">'</span> <span class="pl-pds">'</span></span>.join(<span class="pl-c1">str</span>(pixel) <span class="pl-k">for</span> pixel <span class="pl-k">in</span> row) <span class="pl-k">for</span> row <span class="pl-k">in</span> <span class="pl-c1">self</span>.pixels)

  <span class="pl-k">def</span> <span class="pl-en">show</span>(<span class="pl-smi"><span class="pl-smi">self</span></span>):
    <span class="pl-c1">print</span>(<span class="pl-c1">self</span>)
    <span class="pl-k">return</span> <span class="pl-c1">self</span>

  <span class="pl-k">def</span> <span class="pl-en">move</span>(<span class="pl-smi"><span class="pl-smi">self</span></span>, <span class="pl-smi">row</span>, <span class="pl-smi">col</span>):
    <span class="pl-c1">self</span>._row <span class="pl-k">=</span> row <span class="pl-k">%</span> <span class="pl-c1">self</span>._size
    <span class="pl-c1">self</span>._col <span class="pl-k">=</span> col <span class="pl-k">%</span> <span class="pl-c1">self</span>._size
    <span class="pl-k">return</span> <span class="pl-c1">self</span>

  <span class="pl-k">def</span> <span class="pl-en">on</span>(<span class="pl-smi"><span class="pl-smi">self</span></span>):
    <span class="pl-k">return</span> <span class="pl-c1">self</span>.set(<span class="pl-c1">1</span>)

  <span class="pl-k">def</span> <span class="pl-en">off</span>(<span class="pl-smi"><span class="pl-smi">self</span></span>):
    <span class="pl-k">return</span> <span class="pl-c1">self</span>.set(<span class="pl-c1">0</span>)

  <span class="pl-k">def</span> <span class="pl-c1">set</span>(<span class="pl-smi"><span class="pl-smi">self</span></span>, <span class="pl-smi">value</span>):
    <span class="pl-c1">self</span>.pixels[<span class="pl-c1">self</span>._row][<span class="pl-c1">self</span>._col] <span class="pl-k">=</span> value
    <span class="pl-k">return</span> <span class="pl-c1">self</span>

<span class="pl-k">if</span> <span class="pl-c1">__name__</span> <span class="pl-k">==</span> <span class="pl-s"><span class="pl-pds">'</span>__main__<span class="pl-pds">'</span></span>:
  fire.Fire(BinaryCanvas)</pre></div>
<p>Now we can draw stuff :).</p>
<div class="highlight highlight-source-shell"><pre>$ python example.py move 3 3 on move 3 6 on move 6 3 on move 6 6 on move 7 4 on move 7 5 on __str__
0 0 0 0 0 0 0 0 0 0
0 0 0 0 0 0 0 0 0 0
0 0 0 0 0 0 0 0 0 0
0 0 0 1 0 0 1 0 0 0
0 0 0 0 0 0 0 0 0 0
0 0 0 0 0 0 0 0 0 0
0 0 0 1 0 0 1 0 0 0
0 0 0 0 1 1 0 0 0 0
0 0 0 0 0 0 0 0 0 0
0 0 0 0 0 0 0 0 0 0</pre></div>
<p>It's supposed to be a smiley face.</p>
<h3><a href="#can-we-make-an-even-simpler-example-than-hello-world" aria-hidden="true" class="anchor" id="user-content-can-we-make-an-even-simpler-example-than-hello-world"><svg aria-hidden="true" class="octicon octicon-link" height="16" version="1.1" viewBox="0 0 16 16" width="16"><path fill-rule="evenodd" d="M4 9h1v1H4c-1.5 0-3-1.69-3-3.5S2.55 3 4 3h4c1.45 0 3 1.69 3 3.5 0 1.41-.91 2.72-2 3.25V8.59c.58-.45 1-1.27 1-2.09C10 5.22 8.98 4 8 4H4c-.98 0-2 1.22-2 2.5S3 9 4 9zm9-3h-1v1h1c1 0 2 1.22 2 2.5S13.98 12 13 12H9c-.98 0-2-1.22-2-2.5 0-.83.42-1.64 1-2.09V6.25c-1.09.53-2 1.84-2 3.25C6 11.31 7.55 13 9 13h4c1.45 0 3-1.69 3-3.5S14.5 6 13 6z"></path></svg></a>Can we make an even simpler example than Hello World?</h3>
<p>Yes, this program is even simpler than our original Hello World example.</p>
<div class="highlight highlight-source-python"><pre><span class="pl-k">import</span> fire
english <span class="pl-k">=</span> <span class="pl-s"><span class="pl-pds">'</span>Hello World<span class="pl-pds">'</span></span>
spanish <span class="pl-k">=</span> <span class="pl-s"><span class="pl-pds">'</span>Hola Mundo<span class="pl-pds">'</span></span>
fire.Fire()</pre></div>
<p>You can use it like this:</p>
<div class="highlight highlight-source-shell"><pre>$ python example.py english
Hello World
$ python example.py spanish
Hola Mundo</pre></div>
<h3><a href="#calling-functions" aria-hidden="true" class="anchor" id="user-content-calling-functions"><svg aria-hidden="true" class="octicon octicon-link" height="16" version="1.1" viewBox="0 0 16 16" width="16"><path fill-rule="evenodd" d="M4 9h1v1H4c-1.5 0-3-1.69-3-3.5S2.55 3 4 3h4c1.45 0 3 1.69 3 3.5 0 1.41-.91 2.72-2 3.25V8.59c.58-.45 1-1.27 1-2.09C10 5.22 8.98 4 8 4H4c-.98 0-2 1.22-2 2.5S3 9 4 9zm9-3h-1v1h1c1 0 2 1.22 2 2.5S13.98 12 13 12H9c-.98 0-2-1.22-2-2.5 0-.83.42-1.64 1-2.09V6.25c-1.09.53-2 1.84-2 3.25C6 11.31 7.55 13 9 13h4c1.45 0 3-1.69 3-3.5S14.5 6 13 6z"></path></svg></a>Calling Functions</h3>
<p>Arguments to a constructor are passed by name using flag syntax <code>--name=value</code>.</p>
<p>For example, consider this simple class:</p>
<div class="highlight highlight-source-python"><pre><span class="pl-k">import</span> fire

<span class="pl-k">class</span> <span class="pl-en">Building</span>(<span class="pl-c1">object</span>):

  <span class="pl-k">def</span> <span class="pl-c1">__init__</span>(<span class="pl-smi"><span class="pl-smi">self</span></span>, <span class="pl-smi">name</span>, <span class="pl-smi">stories</span><span class="pl-k">=</span><span class="pl-c1">1</span>):
    <span class="pl-c1">self</span>.name <span class="pl-k">=</span> name
    <span class="pl-c1">self</span>.stories <span class="pl-k">=</span> <span class="pl-c1">1</span>

  <span class="pl-k">def</span> <span class="pl-en">climb_stairs</span>(<span class="pl-smi"><span class="pl-smi">self</span></span>, <span class="pl-smi">stairs_per_story</span><span class="pl-k">=</span><span class="pl-c1">10</span>):
    <span class="pl-k">for</span> story <span class="pl-k">in</span> <span class="pl-c1">range</span>(<span class="pl-c1">self</span>.stories):
      <span class="pl-k">for</span> stair <span class="pl-k">in</span> <span class="pl-c1">range</span>(<span class="pl-c1">1</span>, stairs_per_story):
        <span class="pl-k">yield</span> stair
        <span class="pl-k">yield</span> <span class="pl-s"><span class="pl-pds">'</span>Phew!<span class="pl-pds">'</span></span>
    <span class="pl-k">yield</span> <span class="pl-s"><span class="pl-pds">'</span>Done!<span class="pl-pds">'</span></span>

<span class="pl-k">if</span> <span class="pl-c1">__name__</span> <span class="pl-k">==</span> <span class="pl-s"><span class="pl-pds">'</span>__main__<span class="pl-pds">'</span></span>:
  fire.Fire(Building)</pre></div>
<p>We can instantiate it as follows: <code>python example.py --name="Sherrerd Hall"</code></p>
<p>Arguments to other functions may be passed positionally or by name using flag
syntax.</p>
<p>To instantiate a <code>Building</code> and then run the <code>climb_stairs</code> function, the
following commands are all valid:</p>
<div class="highlight highlight-source-shell"><pre>$ python example.py --name=<span class="pl-s"><span class="pl-pds">"</span>Sherrerd Hall<span class="pl-pds">"</span></span> --stories=3 climb_stairs 10
$ python example.py --name=<span class="pl-s"><span class="pl-pds">"</span>Sherrerd Hall<span class="pl-pds">"</span></span> climb_stairs --stairs_per_story=10
$ python example.py --name=<span class="pl-s"><span class="pl-pds">"</span>Sherrerd Hall<span class="pl-pds">"</span></span> climb_stairs --stairs-per-story 10
$ python example.py climb-stairs --stairs-per-story 10 --name=<span class="pl-s"><span class="pl-pds">"</span>Sherrerd Hall<span class="pl-pds">"</span></span></pre></div>
<p>You'll notice that hyphens and underscores (<code>-</code> and <code>_</code>) are interchangeable in
member names and flag names.</p>
<p>You'll also notice that the constructor's arguments can come after the
function's arguments or before the function.</p>
<p>You'll also notice that the equal sign between the flag name and its value is
optional.</p>
<h5><a href="#functions-with-varargs-and-kwargs" aria-hidden="true" class="anchor" id="user-content-functions-with-varargs-and-kwargs"><svg aria-hidden="true" class="octicon octicon-link" height="16" version="1.1" viewBox="0 0 16 16" width="16"><path fill-rule="evenodd" d="M4 9h1v1H4c-1.5 0-3-1.69-3-3.5S2.55 3 4 3h4c1.45 0 3 1.69 3 3.5 0 1.41-.91 2.72-2 3.25V8.59c.58-.45 1-1.27 1-2.09C10 5.22 8.98 4 8 4H4c-.98 0-2 1.22-2 2.5S3 9 4 9zm9-3h-1v1h1c1 0 2 1.22 2 2.5S13.98 12 13 12H9c-.98 0-2-1.22-2-2.5 0-.83.42-1.64 1-2.09V6.25c-1.09.53-2 1.84-2 3.25C6 11.31 7.55 13 9 13h4c1.45 0 3-1.69 3-3.5S14.5 6 13 6z"></path></svg></a>Functions with <code>*varargs</code> and <code>**kwargs</code></h5>
<p>Fire supports functions that take *varargs or **kwargs. Here's an example:</p>
<div class="highlight highlight-source-python"><pre><span class="pl-k">import</span> fire

<span class="pl-k">def</span> <span class="pl-en">order_by_length</span>(<span class="pl-k">*</span><span class="pl-smi">items</span>):
  <span class="pl-s"><span class="pl-pds">"""</span>Orders items by length, breaking ties alphabetically.<span class="pl-pds">"""</span></span>
  sorted_items <span class="pl-k">=</span> <span class="pl-c1">sorted</span>(items, <span class="pl-v">key</span><span class="pl-k">=</span><span class="pl-k">lambda</span> <span class="pl-smi">item</span>: (<span class="pl-c1">len</span>(<span class="pl-c1">str</span>(item)), <span class="pl-c1">str</span>(item)))
  <span class="pl-k">return</span> <span class="pl-s"><span class="pl-pds">'</span> <span class="pl-pds">'</span></span>.join(sorted_items)

<span class="pl-k">if</span> <span class="pl-c1">__name__</span> <span class="pl-k">==</span> <span class="pl-s"><span class="pl-pds">'</span>__main__<span class="pl-pds">'</span></span>:
  fire.Fire(order_by_length)</pre></div>
<p>To use it, we run:</p>
<div class="highlight highlight-source-shell"><pre>$ python example.py dog cat elephant
cat dog elephant</pre></div>
<p>You can use a separator to indicate that you're done providing arguments to a
function. All arguments after the separator will be used to process the result
of the function, rather than being passed to the function itself. The default
separator is the hyphen <code>-</code>.</p>
<p>Here's an example where we use a separator.</p>
<div class="highlight highlight-source-shell"><pre>$ python example.py dog cat elephant - upper
CAT DOG ELEPHANT</pre></div>
<p>Without the separator, upper would have been treated as another argument.</p>
<div class="highlight highlight-source-shell"><pre>$ python example.py dog cat elephant upper
cat dog upper elephant</pre></div>
<p>You can change the separator with the <code>--separator</code> flag. Flags are always
separated from your Fire command by an isolated <code>--</code>. Here's an example where we
change the separator.</p>
<div class="highlight highlight-source-shell"><pre>$ python example.py dog cat elephant X upper -- --separator=X
CAT DOG ELEPHANT</pre></div>
<p>Separators can be useful when a function accepts *varargs, **kwargs, or
default values that you don't want to specify. It is also important to remember
to change the separator if you want to pass <code>-</code> as an argument.</p>
<h3><a href="#argument-parsing" aria-hidden="true" class="anchor" id="user-content-argument-parsing"><svg aria-hidden="true" class="octicon octicon-link" height="16" version="1.1" viewBox="0 0 16 16" width="16"><path fill-rule="evenodd" d="M4 9h1v1H4c-1.5 0-3-1.69-3-3.5S2.55 3 4 3h4c1.45 0 3 1.69 3 3.5 0 1.41-.91 2.72-2 3.25V8.59c.58-.45 1-1.27 1-2.09C10 5.22 8.98 4 8 4H4c-.98 0-2 1.22-2 2.5S3 9 4 9zm9-3h-1v1h1c1 0 2 1.22 2 2.5S13.98 12 13 12H9c-.98 0-2-1.22-2-2.5 0-.83.42-1.64 1-2.09V6.25c-1.09.53-2 1.84-2 3.25C6 11.31 7.55 13 9 13h4c1.45 0 3-1.69 3-3.5S14.5 6 13 6z"></path></svg></a>Argument Parsing</h3>
<p>The types of the arguments are determined by their values, rather than by the
function signature where they're used. You can pass any Python literal from the
command line: numbers, strings, tuples, lists, dictionaries, (sets are only
supported in some versions of Python). You can also nest the collections
arbitrarily as long as they only contain literals.</p>
<p>To demonstrate this, we'll make a small example program that tells us the type
of any argument we give it:</p>
<div class="highlight highlight-source-python"><pre><span class="pl-k">import</span> fire
fire.Fire(<span class="pl-k">lambda</span> <span class="pl-smi">obj</span>: <span class="pl-c1">type</span>(obj).<span class="pl-c1">__name__</span>)</pre></div>
<p>And we'll use it like so:</p>
<div class="highlight highlight-source-shell"><pre>$ python example.py 10
int
$ python example.py 10.0
float
$ python example.py hello
str
$ python example.py <span class="pl-s"><span class="pl-pds">'</span>(1,2)<span class="pl-pds">'</span></span>
tuple
$ python example.py [1,2]
list
$ python example.py True
bool
$ python example.py {name: David}
dict</pre></div>
<p>You'll notice in that last example that bare-words are automatically replaced
with strings.</p>
<p>Be careful with your quotes! If you want to pass the string <code>"10"</code>, rather than
the int <code>10</code>, you'll need to either escape or quote your quotes. Otherwise Bash
will eat your quotes and pass an unquoted <code>10</code> to your Python program, where
Fire will interpret it as a number.</p>
<div class="highlight highlight-source-shell"><pre>$ python example.py 10
int
$ python example.py <span class="pl-s"><span class="pl-pds">"</span>10<span class="pl-pds">"</span></span>
int
$ python example.py <span class="pl-s"><span class="pl-pds">'</span>"10"<span class="pl-pds">'</span></span>
str
$ python example.py <span class="pl-s"><span class="pl-pds">"</span>'10'<span class="pl-pds">"</span></span>
str
$ python example.py <span class="pl-cce">\"</span>10<span class="pl-cce">\"</span>
str</pre></div>
<p>Be careful with your quotes! Remember that Bash processes your arguments first,
and then Fire parses the result of that.
If you wanted to pass the dict <code>{"name": "David Bieber"}</code> to your program, you
might try this:</p>
<div class="highlight highlight-source-shell"><pre>$ python example.py <span class="pl-s"><span class="pl-pds">'</span>{"name": "David Bieber"}<span class="pl-pds">'</span></span>  <span class="pl-c"><span class="pl-c">#</span> Good! Do this.</span>
dict
$ python example.py {<span class="pl-s"><span class="pl-pds">"</span>name<span class="pl-pds">"</span></span>:<span class="pl-s"><span class="pl-pds">'</span>"David Bieber"<span class="pl-pds">'</span></span>}  <span class="pl-c"><span class="pl-c">#</span> Okay.</span>
dict
$ python example.py {<span class="pl-s"><span class="pl-pds">"</span>name<span class="pl-pds">"</span></span>:<span class="pl-s"><span class="pl-pds">"</span>David Bieber<span class="pl-pds">"</span></span>}  <span class="pl-c"><span class="pl-c">#</span> Wrong. This is parsed as a string.</span>
str
$ python example.py {<span class="pl-s"><span class="pl-pds">"</span>name<span class="pl-pds">"</span></span>: <span class="pl-s"><span class="pl-pds">"</span>David Bieber<span class="pl-pds">"</span></span>}  <span class="pl-c"><span class="pl-c">#</span> Wrong. This isn't even treated as a single argument.</span>
<span class="pl-k">&lt;</span>error<span class="pl-k">&gt;</span>
$ python example.py <span class="pl-s"><span class="pl-pds">'</span>{"name": "Justin Bieber"}<span class="pl-pds">'</span></span>  <span class="pl-c"><span class="pl-c">#</span> Wrong. This is not the Bieber you're looking for. (The syntax is fine though :))</span>
dict</pre></div>
<h5><a href="#boolean-arguments" aria-hidden="true" class="anchor" id="user-content-boolean-arguments"><svg aria-hidden="true" class="octicon octicon-link" height="16" version="1.1" viewBox="0 0 16 16" width="16"><path fill-rule="evenodd" d="M4 9h1v1H4c-1.5 0-3-1.69-3-3.5S2.55 3 4 3h4c1.45 0 3 1.69 3 3.5 0 1.41-.91 2.72-2 3.25V8.59c.58-.45 1-1.27 1-2.09C10 5.22 8.98 4 8 4H4c-.98 0-2 1.22-2 2.5S3 9 4 9zm9-3h-1v1h1c1 0 2 1.22 2 2.5S13.98 12 13 12H9c-.98 0-2-1.22-2-2.5 0-.83.42-1.64 1-2.09V6.25c-1.09.53-2 1.84-2 3.25C6 11.31 7.55 13 9 13h4c1.45 0 3-1.69 3-3.5S14.5 6 13 6z"></path></svg></a>Boolean Arguments</h5>
<p>The tokens <code>True</code> and <code>False</code> are parsed as boolean values.</p>
<p>You may also specify booleans via flag syntax <code>--name</code> and <code>--noname</code>, which set
<code>name</code> to <code>True</code> and <code>False</code> respectively.</p>
<p>Continuing the previous example, we could run any of the following:</p>
<div class="highlight highlight-source-shell"><pre>$ python example.py --obj=True
bool
$ python example.py --obj=False
bool
$ python example.py --obj
bool
$ python example.py --noobj
bool</pre></div>
<p>Be careful with boolean flags! If a token other than another flag immediately
follows a flag that's supposed to be a boolean, the flag will take on the value
of the token rather than the boolean value. You can resolve this: by putting a
separator after your last flag, by explicitly stating the value of the boolean
flag (as in <code>--obj=True</code>), or by making sure there's another flag after any
boolean flag argument.</p>
<h3><a href="#using-fire-flags" aria-hidden="true" class="anchor" id="user-content-using-fire-flags"><svg aria-hidden="true" class="octicon octicon-link" height="16" version="1.1" viewBox="0 0 16 16" width="16"><path fill-rule="evenodd" d="M4 9h1v1H4c-1.5 0-3-1.69-3-3.5S2.55 3 4 3h4c1.45 0 3 1.69 3 3.5 0 1.41-.91 2.72-2 3.25V8.59c.58-.45 1-1.27 1-2.09C10 5.22 8.98 4 8 4H4c-.98 0-2 1.22-2 2.5S3 9 4 9zm9-3h-1v1h1c1 0 2 1.22 2 2.5S13.98 12 13 12H9c-.98 0-2-1.22-2-2.5 0-.83.42-1.64 1-2.09V6.25c-1.09.53-2 1.84-2 3.25C6 11.31 7.55 13 9 13h4c1.45 0 3-1.69 3-3.5S14.5 6 13 6z"></path></svg></a>Using Fire Flags</h3>
<p>Fire CLIs all come with a number of flags. These flags should be separated from
the Fire command by an isolated <code>--</code>. If there is at least one isolated <code>--</code>
argument, then arguments after the final isolated <code>--</code> are treated as flags,
whereas all arguments before the final isolated <code>--</code> are considered part of the
Fire command.</p>
<p>One useful flag is the <code>--interactive</code> flag. Use the <code>--interactive</code> flag on any
CLI to enter a Python REPL with all the modules and variables used in the
context where <code>Fire</code> was called already available to you for use. Other useful
variables, such as the result of the Fire command will also be available. Use
this feature like this: <code>python example.py -- --interactive</code>.</p>
<p>You can add the help flag to any command to see help and usage information. Fire
incorporates your docstrings into the help and usage information that it
generates. Fire will try to provide help even if you omit the isolated <code>--</code>
separating the flags from the Fire command, but may not always be able to, since
<code>help</code> is a valid argument name. Use this feature like this:
<code>python example.py -- --help</code>.</p>
<p>The complete set of flags available is shown below, in the reference section.</p>
<h3><a href="#reference" aria-hidden="true" class="anchor" id="user-content-reference"><svg aria-hidden="true" class="octicon octicon-link" height="16" version="1.1" viewBox="0 0 16 16" width="16"><path fill-rule="evenodd" d="M4 9h1v1H4c-1.5 0-3-1.69-3-3.5S2.55 3 4 3h4c1.45 0 3 1.69 3 3.5 0 1.41-.91 2.72-2 3.25V8.59c.58-.45 1-1.27 1-2.09C10 5.22 8.98 4 8 4H4c-.98 0-2 1.22-2 2.5S3 9 4 9zm9-3h-1v1h1c1 0 2 1.22 2 2.5S13.98 12 13 12H9c-.98 0-2-1.22-2-2.5 0-.83.42-1.64 1-2.09V6.25c-1.09.53-2 1.84-2 3.25C6 11.31 7.55 13 9 13h4c1.45 0 3-1.69 3-3.5S14.5 6 13 6z"></path></svg></a>Reference</h3>
<table>
<thead>
<tr>
<th align="left">Setup</th>
<th align="left">Command</th>
<th align="left">Notes</th>
</tr>
</thead>
<tbody>
<tr>
<td align="left">install</td>
<td align="left"><code>pip install fire</code></td>
<td align="left"></td>
</tr></tbody></table>
<h5><a href="#creating-a-cli" aria-hidden="true" class="anchor" id="user-content-creating-a-cli"><svg aria-hidden="true" class="octicon octicon-link" height="16" version="1.1" viewBox="0 0 16 16" width="16"><path fill-rule="evenodd" d="M4 9h1v1H4c-1.5 0-3-1.69-3-3.5S2.55 3 4 3h4c1.45 0 3 1.69 3 3.5 0 1.41-.91 2.72-2 3.25V8.59c.58-.45 1-1.27 1-2.09C10 5.22 8.98 4 8 4H4c-.98 0-2 1.22-2 2.5S3 9 4 9zm9-3h-1v1h1c1 0 2 1.22 2 2.5S13.98 12 13 12H9c-.98 0-2-1.22-2-2.5 0-.83.42-1.64 1-2.09V6.25c-1.09.53-2 1.84-2 3.25C6 11.31 7.55 13 9 13h4c1.45 0 3-1.69 3-3.5S14.5 6 13 6z"></path></svg></a>Creating a CLI</h5>
<table>
<thead>
<tr>
<th align="left">Creating a CLI</th>
<th align="left">Command</th>
<th align="left">Notes</th>
</tr>
</thead>
<tbody>
<tr>
<td align="left">import</td>
<td align="left"><code>import fire</code></td>
<td align="left"></td>
</tr>
<tr>
<td align="left">Call</td>
<td align="left"><code>fire.Fire()</code></td>
<td align="left">Turns the current module into a Fire CLI.</td>
</tr>
<tr>
<td align="left">Call</td>
<td align="left"><code>fire.Fire(component)</code></td>
<td align="left">Turns <code>component</code> into a Fire CLI.</td>
</tr></tbody></table>
<h5><a href="#flags" aria-hidden="true" class="anchor" id="user-content-flags"><svg aria-hidden="true" class="octicon octicon-link" height="16" version="1.1" viewBox="0 0 16 16" width="16"><path fill-rule="evenodd" d="M4 9h1v1H4c-1.5 0-3-1.69-3-3.5S2.55 3 4 3h4c1.45 0 3 1.69 3 3.5 0 1.41-.91 2.72-2 3.25V8.59c.58-.45 1-1.27 1-2.09C10 5.22 8.98 4 8 4H4c-.98 0-2 1.22-2 2.5S3 9 4 9zm9-3h-1v1h1c1 0 2 1.22 2 2.5S13.98 12 13 12H9c-.98 0-2-1.22-2-2.5 0-.83.42-1.64 1-2.09V6.25c-1.09.53-2 1.84-2 3.25C6 11.31 7.55 13 9 13h4c1.45 0 3-1.69 3-3.5S14.5 6 13 6z"></path></svg></a>Flags</h5>
<table>
<thead>
<tr>
<th align="left">Using a CLI</th>
<th align="left">Command</th>
<th align="left">Notes</th>
</tr>
</thead>
<tbody>
<tr>
<td align="left"><a href="/google/python-fire/blob/master/docs/using-cli.md#help-flag">Help</a></td>
<td align="left"><code>command -- --help</code></td>
<td align="left">Show help and usage information for the command.</td>
</tr>
<tr>
<td align="left"><a href="/google/python-fire/blob/master/docs/using-cli.md#interactive-flag">REPL</a></td>
<td align="left"><code>command -- --interactive</code></td>
<td align="left">Enter interactive mode.</td>
</tr>
<tr>
<td align="left"><a href="/google/python-fire/blob/master/docs/using-cli.md#separator-flag">Separator</a></td>
<td align="left"><code>command -- --separator=X</code></td>
<td align="left">This sets the separator to <code>X</code>. The default separator is <code>-</code>.</td>
</tr>
<tr>
<td align="left"><a href="/google/python-fire/blob/master/docs/using-cli.md#completion-flag">Completion</a></td>
<td align="left"><code>command -- --completion</code></td>
<td align="left">Generate a completion script for the CLI.</td>
</tr>
<tr>
<td align="left"><a href="/google/python-fire/blob/master/docs/using-cli.md#trace-flag">Trace</a></td>
<td align="left"><code>command -- --trace</code></td>
<td align="left">Gets a Fire trace for the command.</td>
</tr>
<tr>
<td align="left"><a href="/google/python-fire/blob/master/docs/using-cli.md#verbose-flag">Verbose</a></td>
<td align="left"><code>command -- --verbose</code></td>
<td align="left">Include private members in the output.</td>
</tr></tbody></table>
<p><em>Note that flags are separated from the Fire command by an isolated <code>--</code> arg.</em></p>
<h3><a href="#disclaimer" aria-hidden="true" class="anchor" id="user-content-disclaimer"><svg aria-hidden="true" class="octicon octicon-link" height="16" version="1.1" viewBox="0 0 16 16" width="16"><path fill-rule="evenodd" d="M4 9h1v1H4c-1.5 0-3-1.69-3-3.5S2.55 3 4 3h4c1.45 0 3 1.69 3 3.5 0 1.41-.91 2.72-2 3.25V8.59c.58-.45 1-1.27 1-2.09C10 5.22 8.98 4 8 4H4c-.98 0-2 1.22-2 2.5S3 9 4 9zm9-3h-1v1h1c1 0 2 1.22 2 2.5S13.98 12 13 12H9c-.98 0-2-1.22-2-2.5 0-.83.42-1.64 1-2.09V6.25c-1.09.53-2 1.84-2 3.25C6 11.31 7.55 13 9 13h4c1.45 0 3-1.69 3-3.5S14.5 6 13 6z"></path></svg></a>Disclaimer</h3>
<p>Python Fire is not an official Google product.</p>
</article>
  </div>

  </div>

  <button type="button" data-facebox="#jump-to-line" data-facebox-class="linejump" data-hotkey="l" class="d-none">Jump to Line</button>
  <div id="jump-to-line" style="display:none">
    <!-- '"` --><!-- </textarea></xmp> --></option></form><form accept-charset="UTF-8" action="" class="js-jump-to-line-form" method="get"><div style="margin:0;padding:0;display:inline"><input name="utf8" type="hidden" value="&#x2713;" /></div>
      <input class="form-control linejump-input js-jump-to-line-field" type="text" placeholder="Jump to line&hellip;" aria-label="Jump to line" autofocus>
      <button type="submit" class="btn">Go</button>
</form>  </div>


  </div>
  <div class="modal-backdrop js-touch-events"></div>
</div>

    </div>
  </div>

  </div>

      
<div class="footer container-lg px-3" role="contentinfo">
  <div class="position-relative d-flex flex-justify-between py-6 mt-6 f6 text-gray border-top border-gray-light ">
    <ul class="list-style-none d-flex flex-wrap ">
      <li class="mr-3">&copy; 2018 <span title="0.18219s from unicorn-3496393735-0z32q">GitHub</span>, Inc.</li>
        <li class="mr-3"><a href="https://github.com/site/terms" data-ga-click="Footer, go to terms, text:terms">Terms</a></li>
        <li class="mr-3"><a href="https://github.com/site/privacy" data-ga-click="Footer, go to privacy, text:privacy">Privacy</a></li>
        <li class="mr-3"><a href="https://github.com/security" data-ga-click="Footer, go to security, text:security">Security</a></li>
        <li class="mr-3"><a href="https://status.github.com/" data-ga-click="Footer, go to status, text:status">Status</a></li>
        <li><a href="https://help.github.com" data-ga-click="Footer, go to help, text:help">Help</a></li>
    </ul>

    <a href="https://github.com" aria-label="Homepage" class="footer-octicon" title="GitHub">
      <svg aria-hidden="true" class="octicon octicon-mark-github" height="24" version="1.1" viewBox="0 0 16 16" width="24"><path fill-rule="evenodd" d="M8 0C3.58 0 0 3.58 0 8c0 3.54 2.29 6.53 5.47 7.59.4.07.55-.17.55-.38 0-.19-.01-.82-.01-1.49-2.01.37-2.53-.49-2.69-.94-.09-.23-.48-.94-.82-1.13-.28-.15-.68-.52-.01-.53.63-.01 1.08.58 1.23.82.72 1.21 1.87.87 2.33.66.07-.52.28-.87.51-1.07-1.78-.2-3.64-.89-3.64-3.95 0-.87.31-1.59.82-2.15-.08-.2-.36-1.02.08-2.12 0 0 .67-.21 2.2.82.64-.18 1.32-.27 2-.27.68 0 1.36.09 2 .27 1.53-1.04 2.2-.82 2.2-.82.44 1.1.16 1.92.08 2.12.51.56.82 1.27.82 2.15 0 3.07-1.87 3.75-3.65 3.95.29.25.54.73.54 1.48 0 1.07-.01 1.93-.01 2.2 0 .21.15.46.55.38A8.013 8.013 0 0 0 16 8c0-4.42-3.58-8-8-8z"/></svg>
</a>
    <ul class="list-style-none d-flex flex-wrap ">
        <li class="mr-3"><a href="https://github.com/contact" data-ga-click="Footer, go to contact, text:contact">Contact GitHub</a></li>
      <li class="mr-3"><a href="https://developer.github.com" data-ga-click="Footer, go to api, text:api">API</a></li>
      <li class="mr-3"><a href="https://training.github.com" data-ga-click="Footer, go to training, text:training">Training</a></li>
      <li class="mr-3"><a href="https://shop.github.com" data-ga-click="Footer, go to shop, text:shop">Shop</a></li>
        <li class="mr-3"><a href="https://github.com/blog" data-ga-click="Footer, go to blog, text:blog">Blog</a></li>
        <li><a href="https://github.com/about" data-ga-click="Footer, go to about, text:about">About</a></li>

    </ul>
  </div>
</div>



  <div id="ajax-error-message" class="ajax-error-message flash flash-error">
    <svg aria-hidden="true" class="octicon octicon-alert" height="16" version="1.1" viewBox="0 0 16 16" width="16"><path fill-rule="evenodd" d="M8.865 1.52c-.18-.31-.51-.5-.87-.5s-.69.19-.87.5L.275 13.5c-.18.31-.18.69 0 1 .19.31.52.5.87.5h13.7c.36 0 .69-.19.86-.5.17-.31.18-.69.01-1L8.865 1.52zM8.995 13h-2v-2h2v2zm0-3h-2V6h2v4z"/></svg>
    <button type="button" class="flash-close js-ajax-error-dismiss" aria-label="Dismiss error">
      <svg aria-hidden="true" class="octicon octicon-x" height="16" version="1.1" viewBox="0 0 12 16" width="12"><path fill-rule="evenodd" d="M7.48 8l3.75 3.75-1.48 1.48L6 9.48l-3.75 3.75-1.48-1.48L4.52 8 .77 4.25l1.48-1.48L6 6.52l3.75-3.75 1.48 1.48z"/></svg>
    </button>
    You can't perform that action at this time.
  </div>


    
    <script crossorigin="anonymous" integrity="sha512-XMGJvyy1pIQdZi6FwfzPUDXHfItIkA7EL3jK0uSro6JSF0Tp76YxJNtflJlhbeQxOHaIj144gWd+J2ZmFUgFiQ==" src="https://assets-cdn.github.com/assets/frameworks-5cc189bf2cb5.js"></script>
    
    <script async="async" crossorigin="anonymous" integrity="sha512-OgFKZNqWUcsiW0qcxBpBIFVyxD7dejmGFtIeBPKuIzFi7p+pRoV4M/iAPYWhIa/u7tRafeDYC4Jn+PZ4jKorYQ==" src="https://assets-cdn.github.com/assets/github-3a014a64da96.js"></script>
    
    
    
    
  <div class="js-stale-session-flash stale-session-flash flash flash-warn flash-banner d-none">
    <svg aria-hidden="true" class="octicon octicon-alert" height="16" version="1.1" viewBox="0 0 16 16" width="16"><path fill-rule="evenodd" d="M8.865 1.52c-.18-.31-.51-.5-.87-.5s-.69.19-.87.5L.275 13.5c-.18.31-.18.69 0 1 .19.31.52.5.87.5h13.7c.36 0 .69-.19.86-.5.17-.31.18-.69.01-1L8.865 1.52zM8.995 13h-2v-2h2v2zm0-3h-2V6h2v4z"/></svg>
    <span class="signed-in-tab-flash">You signed in with another tab or window. <a href="">Reload</a> to refresh your session.</span>
    <span class="signed-out-tab-flash">You signed out in another tab or window. <a href="">Reload</a> to refresh your session.</span>
  </div>
  <div class="facebox" id="facebox" style="display:none;">
  <div class="facebox-popup">
    <div class="facebox-content" role="dialog" aria-labelledby="facebox-header" aria-describedby="facebox-description">
    </div>
    <button type="button" class="facebox-close js-facebox-close" aria-label="Close modal">
      <svg aria-hidden="true" class="octicon octicon-x" height="16" version="1.1" viewBox="0 0 12 16" width="12"><path fill-rule="evenodd" d="M7.48 8l3.75 3.75-1.48 1.48L6 9.48l-3.75 3.75-1.48-1.48L4.52 8 .77 4.25l1.48-1.48L6 6.52l3.75-3.75 1.48 1.48z"/></svg>
    </button>
  </div>
</div>


  </body>
</html>

