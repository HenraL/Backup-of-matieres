a="""(function (b) {
    b.anvsoftJavaScriptSlideshowTemplate = b.aJSsTemplate = b.aJSsTemplate || {
      version: "1.0.0",
      global: b
    };
  })(window);
  (function () {
    aJSsTemplate.ExternalInterface = function (b) {
      this.globalPath = b.globalPath;
      this.container = b.container;
      this.commandDispatcher = b.commandDispatcher;
      this.copyright = b.copyright;
      this.movieWidth = b.movieWidth;
      this.movieHeight = b.movieHeight;
      this.startAutoPlay = b.startAutoPlay;
      this.continuum = b.continuum;
      this.clickToAutoPlay = b.clickToAutoPlay;
      this.randomPlayingPhotos = b.randomPlayingPhotos;
      this.enableURL = b.enableURL;
      this.movieBackgroundColor = b.movieBackgroundColor;
      this.loadStyle = b.loadStyle;
      this.anvsoftMenu = b.anvsoftMenu;
      this.frameRate = b.frameRate;
      var a = b.globalTitleXml;
      this.showTitle = a.getAttribute("showTitle");
      this.photoTitleColor = a
        .getAttribute("photoTitleColor")
        .replace(/0x/g, "#");
      this.photoTitleBackgroundColor = a
        .getAttribute("backgroundColor")
        .replace(/0x/g, "#");
      this.photoTitleAlpha = a.getAttribute("alpha") / 100;
      this.photoTitleAutoHide = a.getAttribute("autoHide");
      this.titleTextFont = a.getAttribute("titleTextFont");
      this.titleTextSize = a.getAttribute("titleTextSize");
      this.titleTextHeight = a.getAttribute("titleTextHeight");
      this.titleTextShadowColor = a
        .getAttribute("titleTextShadowColor")
        .replace(/0x/g, "#");
      this.titleTextShadowOffset = Number(
        a.getAttribute("titleTextShadowOffset")
      );
      this.titleTextShadowBlur = Number(a.getAttribute("titleTextShadowBlur"));
      this.titleTextAlign = a.getAttribute("titleTextAlign");
      this.musicPath = b.musicPath;
      this.musicStream = b.musicStream;
      this.musicLoop = b.musicLoop;
      this.musicAutoPlay = b.musicAutoPlay;
      this.topPadding = b.topPadding;
      this.bottomPadding = b.bottomPadding;
      this.leftPadding = b.leftPadding;
      this.rightPadding = b.rightPadding;
      a = b.globalDescriptionXml;
      this.enableDes = a.getAttribute("enable");
      this.desAlign = a.getAttribute("align");
      this.desBackgroundColor = a
        .getAttribute("backgroundColor")
        .replace(/0x/g, "#");
      this.desBackgroundAlpha = a.getAttribute("backgroundAlpha") / 100;
      this.desTextFont = a.getAttribute("defaultTextFont");
      this.desTextSize = a.getAttribute("defaultTextSize");
      this.desTextColor = a.getAttribute("defaultTextColor").replace(/0x/g, "#");
      this.desLineHeight = Number(a.getAttribute("lineHeight"));
      this.desTextShadowColor = a
        .getAttribute("desTextShadowColor")
        .replace(/0x/g, "#");
      this.desTextShadowOffset = Number(a.getAttribute("desTextShadowOffset"));
      this.desTextShadowBlur = Number(a.getAttribute("desTextShadowBlur"));
      this.videoAutoPlay = b.videoAutoPlay;
      this.bufferTime = b.bufferTime;
      this.videoControls = b.videoControls;
      this.desTextAlign = a.getAttribute("desTextAlign");
      a = b.thumbnailBasicXml;
      this.thumWidth = Number(a.getAttribute("thumWidth"));
      this.thumHeight = Number(a.getAttribute("thumHeight"));
      this.thumbnailBorderColor = a
        .getAttribute("borderColor")
        .replace(/0x/g, "#");
      this.currentBorderColor = a
        .getAttribute("currentBorderColor")
        .replace(/0x/g, "#");
      this.thumborder = Number(a.getAttribute("thumborder"));
      this.thumSpacing = Number(a.getAttribute("thumSpacing"));
      this.buttonColor = a.getAttribute("buttonColor").replace(/0x/g, "#");
      this.buttonCurrentColor = a
        .getAttribute("buttonCurrentColor")
        .replace(/0x/g, "#");
      this.buttonTriangleColor = a
        .getAttribute("buttonTriangleColor")
        .replace(/0x/g, "#");
      this.thumbnailArray = b.thumbnailArray;
      this.photoArray = b.photoArray;
      this.photoUrlArray = b.photoUrlArray;
      this.URLTarget = b.URLTarget;
      this.videoArray = b.videoArray;
      this.transitionArray = b.transitionArray;
      this.photoTimeArray = b.photoTimeArray;
      this.transitionTimeArray = b.transitionTimeArray;
      this.defineTransitionArray = b.defineTransitionArray;
      this.photoTitleArray = b.photoTitleArray;
      this.descriptionText = b.descriptionText;
      this.photoCount = this.photoArray.length;
      this.Play = function () {
        b.Play();
      };
      this.Pause = function () {
        b.Pause();
      };
      this.Previous = function () {
        b.Previous();
      };
      this.Next = function () {
        b.Next();
      };
      this.Show = function (a, d) {
        b.Show(a, d);
      };
      this.MusicPlay = function () {
        b.MusicPlay();
      };
      this.MusicPause = function () {
        b.MusicPause();
      };
    };
  })();
  (function () {
    aJSsTemplate.Main = function (b) {
      var b = new aJSsTemplate.ExternalInterface(b),
        a = b.container,
        c = window;
      new aJSsTemplate.JsTheme(b);
      new aJSsTemplate.JsMenu(b, a);
      c.onload = void 0;
    };
  })();
  (function () {
    aJSsTemplate.JsTheme = function (b) {
      var a = b.globalPath,
        c = b.container,
        d = b.movieWidth,
        f = b.movieHeight,
        e = b.movieBackgroundColor,
        h = b.thumbnailArray,
        j = b.photoArray,
        i = b.photoTitleColor,
        g = b.photoTitleArray,
        l = b.thumWidth,
        m = b.thumHeight,
        i = b.photoTitleColor,
        q = b.showTitle,
        n = b.titleTextFont,
        p = b.photoTitleBackgroundColor,
        k = b.photoTitleAlpha,
        r = b.titleTextSize,
        t = b.photoTitleAutoHide,
        s = b.desTextFont,
        v = b.descriptionText,
        x = b.desTextColor,
        T = b.desTextSize,
        K = b.desLineHeight,
        L = b.desAlign,
        M = b.desBackgroundColor,
        X = b.desBackgroundAlpha,
        Y = b.enableDes,
        I = b.topPadding,
        D = b.bottomPadding,
        y = b.leftPadding,
        z = b.rightPadding,
        w = b.thumbnailBorderColor,
        U = b.thumborder,
        P = b.thumSpacing,
        u = b.currentBorderColor,
        J = b.musicPath,
        Z = b.musicAutoPlay,
        da = b.titleTextShadowColor,
        $ = b.titleTextShadowOffset,
        ka = b.titleTextShadowBlur,
        la = b.desTextShadowColor,
        ma = b.desTextShadowOffset,
        ea = b.desTextShadowBlur,
        na = b.titleTextAlign,
        pa = b.desTextAlign,
        V = b.buttonColor,
        ia = b.buttonCurrentColor,
        aa = b.buttonTriangleColor,
        S,
        R,
        ja = document.createElement("div");
      c.appendChild(ja);
      ja.style.position = "absolute";
      ja.style.left = y + "px";
      ja.style.top = I + "px";
      ja.style.width = d - y - z + "px";
      var G = document.createElement("div");
      ja.appendChild(G);
      G.style.backgroundColor = p;
      G.style.opacity = k;
      var ba = document.createElement("div");
      ja.appendChild(ba);
      ba.style.position = "absolute";
      ba.style.backgroundColor = M;
      ba.style.opacity = X;
      p = document.createElement("div");
      c.appendChild(p);
      p.style.position = "absolute";
      p.style.left = y + "px";
      p.style.top = I + "px";
      p.style.width = d - y - z + "px";
      var A = document.createElement("div");
      p.appendChild(A);
      A.style.width = d - z - y - 10 + "px";
      A.style.color = i;
      A.style.fontFamily = n;
      A.style.overflow = "hidden";
      A.style.margin = "0px auto";
      A.style.padding = "5px";
      var W = document.createElement("p");
      A.appendChild(W);
      W.textContent = g[0];
      W.style.textAlign = na;
      W.style.margin = "0 auto";
      W.style.textShadow = $ + "px " + $ + "px " + ka + "px " + da;
      W.style.fontSize = r + "px";
      "true" == q
        ? ((A.style.display = "block"),
          (A.style.display = "" == W.textContent ? "none" : "block"),
          "true" == t &&
            ((A.style.display = "none"),
            (G.style.display = "none"),
            (c.onmouseover = function () {
              "" == W.textContent
                ? ((A.style.display = "none"), (G.style.display = "none"))
                : ((A.style.display = "block"),
                  (G.style.display = "block"),
                  (G.style.width = A.offsetWidth + "px"),
                  (G.style.height = A.offsetHeight + "px"));
            }),
            (c.onmouseout = function () {
              A.style.display = "none";
              G.style.display = "none";
            })))
        : (A.style.display = "none");
      G.style.width = A.offsetWidth + "px";
      G.style.height = A.offsetHeight + "px";
      var C = document.createElement("div");
      p.appendChild(C);
      C.style.position = "absolute";
      C.style.width = d - z - y - 10 + "px";
      C.style.color = x;
      C.style.fontFamily = s;
      C.style.overflow = "hidden";
      C.style.margin = "0 auto";
      C.style.textAlign = pa;
      C.style.padding = "5px";
      var ca = document.createElement("p");
      C.appendChild(ca);
      ca.innerHTML = v[0];
      ca.style.margin = "0 auto";
      ca.style.textShadow = ma + "px " + ma + "px " + ea + "px " + la;
      ca.style.lineHeight = K + "px";
      ca.style.fontSize = T + "px";
      "true" == Y
        ? ((C.style.display = "block"),
          (C.style.display = "" == ca.innerHTML ? "none" : "block"))
        : (C.style.display = "none");
      ba.style.width = C.offsetWidth + "px";
      ba.style.height = C.offsetHeight + "px";
      i = document.createElement("container");
      i.style.position = "absolute";
      c.appendChild(i);
      i.style.width = d + "px";
      i.style.height = m + 2 * U + "px";
      i.style.top = f - b.bottomPadding + b.topPadding + "px";
      i.style.left = "0px";
      i.style.backgroundColor = e;
      e = document.createElement("mainbox");
      c.appendChild(e);
      e.style.position = "absolute";
      e.style.left = y + "px";
      e.style.top = I + "px";
      e.style.width = d - y - z + "px";
      var N = document.createElement("music");
      e.appendChild(N);
      N.style.width = "30px";
      N.style.height = "30px";
      N.style.backgroundImage = "url(" + a + "res/sound.png)";
      N.style.cssFloat = "right";
      var F = new Image();
      e.appendChild(F);
      F.style.marginTop = (f - 2 * I - D - 22) / 2 + "px";
      F.src = a + "res/playb.png";
      F.style.width = "45px";
      F.style.height = "45px";
      F.style.display = "none";
      F.style.cssFloat = "left";
      F.style.display = "block";
      e = document.createElement("div");
      i.appendChild(e);
      e.id = "thumbody";
      e.style.margin = "0px auto";
      e.style.width = d - y - z + "px";
      var H = document.createElement("div");
      e.appendChild(H);
      H.style.position = "absolute";
      H.style.backgroundColor = V;
      H.style.borderRadius = "5px 0px 0px 5px";
      H.textContent = "<";
      H.style.fontSize = "20px";
      H.style.lineHeight = m + 2 * U + "px";
      H.style.color = aa;
      H.style.textAlign = "center";
      H.style.width = "15px";
      H.style.height = m + 2 * U + "px";
      var E = document.createElement("div");
      e.appendChild(E);
      E.style.position = "absolute";
      E.style.backgroundColor = V;
      E.style.borderRadius = "0px 5px 5px 0px";
      E.textContent = ">";
      E.style.fontSize = "20px";
      E.style.lineHeight = m + 2 * U + "px";
      E.style.color = aa;
      E.style.textAlign = "center";
      E.style.width = "15px";
      E.style.height = "56px";
      E.style.marginLeft = d - y - z - 15 + "px";
      E.style.height = m + 2 * U + "px";
      var O = document.createElement("div");
      e.appendChild(O);
      O.id = "photos";
      O.style.position = "absolute";
      O.style.marginLeft = 15 + P + "px";
      O.style.height = m + 2 * U + "px";
      O.style.width = d - y - z - 30 - 2 * P + "px";
      O.style.overflow = "hidden";
      var oa = d - y - z - 30 - 2 * P,
        aa = 0,
        e = 2 * U,
        i = document.createElement("div"),
        n = 0;
      O.appendChild(i);
      i.id = "showArea";
      var r = h.length,
        fa = parseInt((oa + P) / (l + e + P));
      if (b.photoCount > fa) {
        aa = (oa - fa * (l + e)) / (fa - 1);
        for (s = 0; s < b.photoCount; s++) {
          var B = new Image();
          B.style.width = l + "px";
          B.style.height = m + "px";
          B.style.display = "block";
          B.style.cssFloat = "left";
          B.style.cursor = "pointer";
          B.style.borderWidth = U + "px";
          B.style.borderStyle = "solid";
          B.style.borderColor = w;
          B.style.marginRight = 0 == (s + 1) % fa ? "0px" : aa + "px";
          B.src = a + h[s];
          B.alt = j[s];
          B.index = s;
          n = oa * Math.ceil(b.photoCount / fa);
          i.appendChild(B);
        }
        B.style.marginRight = "0px";
        i.style.width = n + "px";
        i.style.height = m + e + "px";
        var ra = n,
          ta = function () {
            O.scrollLeft -= oa;
          },
          ua = function () {
            O.scrollLeft += oa;
          };
        H.style.cursor = "pointer";
        E.style.cursor = "pointer";
        H.onmouseover = function () {
          H.style.backgroundColor = ia;
        };
        H.onclick = function () {
          setTimeout(ta, sa);
        };
        H.onmouseout = function () {
          H.style.backgroundColor = V;
        };
        E.onmouseover = function () {
          E.style.backgroundColor = ia;
        };
        E.onmouseout = function () {
          E.style.backgroundColor = V;
        };
        E.onclick = function () {
          setTimeout(ua, sa);
        };
      }
      if (b.photoCount <= fa) {
        for (s = 0; s < r; s++)
          (B = new Image()),
            (B.style.width = l + "px"),
            (B.style.height = m + "px"),
            (B.style.display = "block"),
            (B.style.cssFloat = "left"),
            (B.style.cursor = "pointer"),
            (B.style.borderWidth = U + "px"),
            (B.style.borderStyle = "solid"),
            (B.style.borderColor = w),
            (B.style.marginRight = P + "px"),
            (B.src = a + h[s]),
            (B.alt = j[s]),
            (B.index = s),
            (n += l + e + P),
            i.appendChild(B);
        B.style.marginRight = "0px";
        i.style.width = d - 30 - 2 * P - y - z;
        i.style.height = m + e + "px";
        ra = d - 30 - 2 * P - y - z;
        E.style.cursor = "pointer";
        H.style.cursor = "pointer";
        E.src = "res/goright2.gif";
        H.src = "res/goleft2.gif";
      }
      E.style.marginRight = d - y - 30 - 2 * P - ra + "px";
      var ga = 0,
        sa = 100,
        ha = i.getElementsByTagName("img"),
        qa = 0,
        qa = "true" == b.clickToAutoPlay ? 1 : 0;
      ha[0].style.borderColor = u;
      F.style.display = "true" == b.startAutoPlay ? "none" : "block";
      b.commandDispatcher.addEventListener("playCurrent", function (a) {
        R = a.index;
        W.textContent = g[R];
        ca.innerHTML = v[R];
        "true" == q
          ? ((A.style.display = "block"),
            (A.style.display = "" == W.textContent ? "none" : "block"),
            "true" == t &&
              ((A.style.display = "none"),
              (G.style.display = "none"),
              (c.onmouseover = function () {
                "" == W.textContent
                  ? ((A.style.display = "none"), (G.style.display = "none"))
                  : ((A.style.display = "block"),
                    (G.style.display = "block"),
                    (G.style.width = A.offsetWidth + "px"),
                    (G.style.height = A.offsetHeight + "px"));
              }),
              (c.onmouseout = function () {
                A.style.display = "none";
                G.style.display = "none";
              })))
          : (A.style.display = "none");
        "true" == Y
          ? ((C.style.display = "block"),
            (C.style.display = "" == ca.innerHTML ? "none" : "block"))
          : (C.style.display = "none");
        G.style.width = A.offsetWidth + "px";
        G.style.height = A.offsetHeight + "px";
        ba.style.width = C.offsetWidth + "px";
        ba.style.height = C.offsetHeight + "px";
        b.photoCount > fa &&
          (0 < R && 0 == R % fa && (O.scrollLeft += oa),
          0 == R && (O.scrollLeft -= ra));
        "bottom" == L &&
          ((C.style.top = f - C.offsetHeight - I - D + "px"),
          (ba.style.top = f - C.offsetHeight - I - D + "px"));
        for (a = 0; a < ha.length; a++) a !== S && (ha[a].style.borderColor = w);
        ha[R].style.borderColor = u;
        R >= b.photoCount - 1 &&
          "false" == b.continuum &&
          (F.style.display = "block");
      });
      F.style.cursor = "pointer";
      N.style.cursor = "pointer";
      F.onmouseover = function () {
        F.src = a + "res/playw.png";
      };
      F.onmouseout = function () {
        F.src = a + "res/playb.png";
      };
      F.onclick = function () {
        b.Play();
        F.style.display = "none";
      };
      "bottom" == L &&
        ((C.style.top = f - C.offsetHeight - I - D + "px"),
        (ba.style.top = f - C.offsetHeight - I - D + "px"));
      for (s = 0; s < ha.length; s++)
        (ha[s].onmouseover = function () {
          this.style.borderColor = u;
          S = this.index;
        }),
          (ha[s].onmouseout = function () {
            R !== S && (this.style.borderColor = w);
            S = "abc";
          }),
          (ha[s].onclick = function () {
            "true" == b.clickToAutoPlay
              ? (qa = 1)
              : ((qa = 0), (F.style.display = "block"));
            W.textContent = g[S];
            ca.innerHTML = v[S];
            b.Show(S, qa);
            "true" == b.clickToAutoPlay && (F.style.display = "none");
          });
      ga = 0;
      "" == J
        ? (N.style.display = "none")
        : "true" == Z
        ? ((N.style.backgroundPosition = "0 0"),
          (N.onclick = function () {
            0 == ga
              ? ((N.style.backgroundPosition = "100% 0"),
                b.MusicPause(),
                (ga = 1))
              : ((N.style.backgroundPosition = "0 0"), b.MusicPlay(), (ga = 0));
          }))
        : ((N.style.backgroundPosition = "100% 0"),
          (N.onclick = function () {
            0 == ga
              ? ((N.style.backgroundPosition = "0 0"), b.MusicPlay(), (ga = 1))
              : ((N.style.backgroundPosition = "100% 0"),
                b.MusicPause(),
                (ga = 0));
          }));
      b.commandDispatcher.addEventListener("soundPlayComplete", function () {
        N.style.backgroundPosition = "100% 0";
        ga = 1;
      });
      b.commandDispatcher.addEventListener("videoPlayEnded", function () {
        F.style.display = "none";
      });
    };
  })();
  (function () {
    aJSsTemplate.JsMenu = function (b, a) {
      var c = b.movieWidth,
        d = b.movieHeight,
        f = b.bottomPadding,
        e = b.rightPadding,
        h = b.copyright;
      if (
        null == b.anvsoftMenu ||
        ("anvsoftPFMTheme" != h &&
          "anvsoftUSSTheme" != h &&
          "anvsoftHSMTheme" != h)
      ) {
        var j;
        switch (h) {
          case "anvsoftPFMTheme":
            j = "Photo Slideshow Maker";
            break;
          case "anvsoftUSSTheme":
            j = "Ultra Slideshow";
            break;
          case "anvsoftHSMTheme":
            j = "HTML5 Slideshow Maker";
            break;
          case "anvsoftSWWTheme":
            j = "SlideWow";
            break;
          default:
            j = "Anvsoft Photo Slideshow";
        }
        var i = document.createElement("div");
        i.style.position = "absolute";
        i.style.cursor = "pointer";
        i.style.padding = "5px";
        i.style.backgroundColor = "rgba(0, 0, 0, 0.3)";
        i.style.textShadow = "1px 1px 1px #000";
        i.style.borderRadius = "5px";
        i.style.color = "#FFF";
        i.style.font = "normal normal 10px/12px verdana,tahoma,arial,sans-serif";
        i.textContent = j;
        a.appendChild(i);
        i.style.left = c - e - i.scrollWidth - 5 + "px";
        i.style.top = d - f - i.scrollHeight - 5 + "px";
        i.onclick = function () {
            var c=confirm("i.onclick (desactivated) line: 578 to 594.\nThe hidden links are:\n- http://www.photo-flash-maker.com/\n- http://www.ultraslideshow.com/\n- http://www.html5-slideshow-maker.com/\n- http://www.slidewow.com/\n- http://www.anvsoft.com/\nVoulez-vous ouvrir : http://www.photo-flash-maker.com/ ?")
            if (c===true){
                window.open("http://www.photo-flash-maker.com/",target="_blank");
                alert("Link opened");
            } else {
                alert("Link not opened");
            };
        //   switch (h) {
        //     case "anvsoftPFMTheme":
        //       window.open("http://www.photo-flash-maker.com/", "_self");
        //       break;
        //     case "anvsoftUSSTheme":
        //       window.open("http://www.ultraslideshow.com/", "_self");
        //       break;
        //     case "anvsoftHSMTheme":
        //       window.open("http://www.html5-slideshow-maker.com/", "_self");
        //       break;
        //     case "anvsoftSWWTheme":
        //       window.open("http://www.slidewow.com/", "_self");
        //       break;
        //     default:
        //       window.open("http://www.anvsoft.com/", "_self");
        //   }
        };
      }
    };
  })();
  (function (b) {
    function a(a, c, b) {
      for (
        var d = a.length, i = c.length, g, l, m, q, n, p, k = 0, r = 0;
        r < d;
        r++
      ) {
        g = a[r];
        l = a[r < d - 1 ? r + 1 : 0];
        k = g.y - l.y;
        g = l.x - g.x;
        l = Math.sqrt(k * k + g * g);
        k /= l;
        g /= l;
        l = m = a[0].x * k + a[0].y * g;
        for (var t = 1; t < d; t++)
          (p = a[t].x * k + a[t].y * g), p > m ? (m = p) : p < l && (l = p);
        q = n = c[0].x * k + c[0].y * g;
        for (t = 1; t < i; t++)
          (p = c[t].x * k + c[t].y * g), p > n ? (n = p) : p < q && (q = p);
        l < q ? ((l = q - m), (k = -k), (g = -g)) : (l -= n);
        if (0 <= l) return !1;
        l > b.overlap && ((b.overlap = l), (b.normal.x = k), (b.normal.y = g));
      }
      return b;
    }
    var c = (b.Quark = b.Quark || { version: "1.0.0", global: b }),
      d = function () {};
    c.inherit = function (a, c) {
      d.prototype = c.prototype;
      a.superClass = c.prototype;
      a.prototype = new d();
      a.prototype.constructor = a;
    };
    c.merge = function (a, c, b) {
      for (var d in c)
        if (!b || a.hasOwnProperty(d) || void 0 !== a[d]) a[d] = c[d];
      return a;
    };
    c.delegate = function (a, c) {
      var d = c || b;
      if (2 < arguments.length) {
        var j = Array.prototype.slice.call(arguments, 2);
        return function () {
          var c = Array.prototype.concat.apply(j, arguments);
          return a.apply(d, c);
        };
      }
      return function () {
        return a.apply(d, arguments);
      };
    };
    c.getDOM = function (a) {
      return document.getElementById(a);
    };
    c.createDOM = function (a, c) {
      var b = document.createElement(a),
        d;
      for (d in c) {
        var i = c[d];
        if ("style" == d) for (var g in i) b.style[g] = i[g];
        else b[d] = i;
      }
      return b;
    };
    c.use = function (a) {
      for (var a = a.split("."), c = b, d = 0; d < a.length; d++)
        var j = a[d], c = c[j] || (c[j] = {});
      return c;
    };
    (function (a) {
      var c = (a.ua = navigator.userAgent);
      a.isWebKit = /webkit/i.test(c);
      a.isMozilla = /mozilla/i.test(c);
      a.isIE = /msie/i.test(c);
      a.isFirefox = /firefox/i.test(c);
      a.isChrome = /chrome/i.test(c);
      a.isSafari = /safari/i.test(c) && !this.isChrome;
      a.isMobile = /mobile/i.test(c);
      a.isOpera = /opera/i.test(c);
      a.isIOS = /ios/i.test(c);
      a.isIpad = /ipad/i.test(c);
      a.isIpod = /ipod/i.test(c);
      a.isIphone = /iphone/i.test(c) && !this.isIpod;
      a.isAndroid = /android/i.test(c);
      a.supportStorage = "localStorage" in b;
      a.supportOrientation = "orientation" in b;
      a.supportDeviceMotion = "ondevicemotion" in b;
      a.supportTouch = "ontouchstart" in b;
      a.supportCanvas = null != document.createElement("canvas").getContext;
      a.cssPrefix = a.isWebKit
        ? "webkit"
        : a.isFirefox
        ? "Moz"
        : a.isOpera
        ? "O"
        : a.isIE
        ? "ms"
        : "";
    })(c);
    c.getElementOffset = function (a) {
      for (
        var c = a.offsetLeft, b = a.offsetTop;
        (a = a.offsetParent) && a != document.body && a != document;
  
      )
        (c += a.offsetLeft), (b += a.offsetTop);
      return { left: c, top: b };
    };
    c.createDOMDrawable = function (a, b) {
      var d = a.tagName || "div",
        j = b.image,
        i = a.width || (j && j.width),
        g = a.height || (j && j.height),
        l = c.createDOM(d);
      a.id && (l.id = a.id);
      l.style.position = "absolute";
      l.style.left = (a.left || 0) + "px";
      l.style.top = (a.top || 0) + "px";
      l.style.width = i + "px";
      l.style.height = g + "px";
      if ("canvas" == d)
        (l.width = i),
          (l.height = g),
          j &&
            ((d = l.getContext("2d")),
            (i = b.rect || [0, 0, i, g]),
            d.drawImage(
              j,
              i[0],
              i[1],
              i[2],
              i[3],
              a.x || 0,
              a.y || 0,
              a.width || i[2],
              a.height || i[3]
            ));
      else if (
        ((l.style.opacity = void 0 != a.alpha ? a.alpha : 1),
        (l.style.overflow = "hidden"),
        j && j.src)
      )
        (l.style.backgroundImage = "url(" + j.src + ")"),
          (l.style.backgroundPosition =
            -(a.rectX || 0) + "px " + -(a.rectY || 0) + "px");
      return l;
    };
    c.DEG_TO_RAD = Math.PI / 180;
    c.RAD_TO_DEG = 180 / Math.PI;
    c.hitTestPoint = function (a, c, b, d) {
      var a = a.getBounds(),
        i = a.length,
        g = c >= a.x && c <= a.x + a.width && b >= a.y && b <= a.y + a.height;
      if (g && d) {
        for (var d = 0, g = !1, l, m, q, n, p = 0; p < i; p++) {
          var k = a[p],
            r = a[(p + 1) % i];
          k.y == r.y &&
          b == k.y &&
          (k.x > r.x ? ((l = r.x), (m = k.x)) : ((l = k.x), (m = r.x)),
          c >= l && c <= m)
            ? (g = !0)
            : (k.y > r.y ? ((q = r.y), (n = k.y)) : ((q = k.y), (n = r.y)),
              b < q ||
                b > n ||
                ((k = ((b - k.y) * (r.x - k.x)) / (r.y - k.y) + k.x),
                k > c ? d++ : k == c && (g = !0)));
        }
        return g ? 0 : 1 == d % 2 ? 1 : -1;
      }
      return g ? 1 : -1;
    };
    c.hitTestObject = function (a, b, d) {
      a = a.getBounds();
      b = b.getBounds();
      return (a =
        a.x <= b.x + b.width &&
        b.x <= a.x + a.width &&
        a.y <= b.y + b.height &&
        b.y <= a.y + a.height) && d
        ? ((a = c.polygonCollision(b, b)), !1 !== a)
        : a;
    };
    c.polygonCollision = function (c, b) {
      var d = a(c, b, { overlap: -Infinity, normal: { x: 0, y: 0 } });
      return d ? a(b, c, d) : !1;
    };
    c.toString = function () {
      return "Quark";
    };
    c.trace = function () {
      var a = Array.prototype.slice.call(arguments);
      "undefined" != typeof console &&
        "undefined" != typeof console.log &&
        console.log(a.join(" "));
    };
    void 0 == b.Q && (b.Q = c);
    void 0 == b.trace && (b.trace = c.trace);
  })(window);
  (function () {
    var b = (Quark.Matrix = function (a, c, b, f, e, h) {
      this.a = a;
      this.b = c;
      this.c = b;
      this.d = f;
      this.tx = e;
      this.ty = h;
    });
    b.prototype.concat = function (a) {
      var c = this.a,
        b = this.c,
        f = this.tx;
      this.a = c * a.a + this.b * a.c;
      this.b = c * a.b + this.b * a.d;
      this.c = b * a.a + this.d * a.c;
      this.d = b * a.b + this.d * a.d;
      this.tx = f * a.a + this.ty * a.c + a.tx;
      this.ty = f * a.b + this.ty * a.d + a.ty;
      return this;
    };
    b.prototype.rotate = function (a) {
      var c = Math.cos(a),
        a = Math.sin(a),
        b = this.a,
        f = this.c,
        e = this.tx;
      this.a = b * c - this.b * a;
      this.b = b * a + this.b * c;
      this.c = f * c - this.d * a;
      this.d = f * a + this.d * c;
      this.tx = e * c - this.ty * a;
      this.ty = e * a + this.ty * c;
      return this;
    };
    b.prototype.scale = function (a, c) {
      this.a *= a;
      this.d *= c;
      this.tx *= a;
      this.ty *= c;
      return this;
    };
    b.prototype.translate = function (a, c) {
      this.tx += a;
      this.ty += c;
      return this;
    };
    b.prototype.identity = function () {
      this.a = this.d = 1;
      this.b = this.c = this.tx = this.ty = 0;
      return this;
    };
    b.prototype.invert = function () {
      var a = this.a,
        c = this.b,
        b = this.c,
        f = this.d,
        e = this.tx,
        h = a * f - c * b;
      this.a = f / h;
      this.b = -c / h;
      this.c = -b / h;
      this.d = a / h;
      this.tx = (b * this.ty - f * e) / h;
      this.ty = -(a * this.ty - c * e) / h;
      return this;
    };
    b.prototype.transformPoint = function (a, c, b) {
      var f = a.x * this.a + a.y * this.c + this.tx,
        e = a.x * this.b + a.y * this.d + this.ty;
      c && ((f = (f + 0.5) >> 0), (e = (e + 0.5) >> 0));
      if (b) return { x: f, y: e };
      a.x = f;
      a.y = e;
      return a;
    };
    b.prototype.clone = function () {
      return new b(this.a, this.b, this.c, this.d, this.tx, this.ty);
    };
    b.prototype.toString = function () {
      return (
        "(a=" +
        this.a +
        ", b=" +
        this.b +
        ", c=" +
        this.c +
        ", d=" +
        this.d +
        ", tx=" +
        this.tx +
        ", ty=" +
        this.ty +
        ")"
      );
    };
  })();
  (function () {
    var b = (Quark.Rectangle = function (a, c, b, f) {
      this.x = a;
      this.y = c;
      this.width = b;
      this.height = f;
    });
    b.prototype.intersects = function (a) {
      return (
        this.x <= a.x + a.width &&
        a.x <= this.x + this.width &&
        this.y <= a.y + a.height &&
        a.y <= this.y + this.height
      );
    };
    b.prototype.intersection = function (a) {
      var c = Math.max(this.x, a.x),
        d = Math.min(this.x + this.width, a.x + a.width);
      if (c <= d) {
        var f = Math.max(this.y, a.y),
          a = Math.min(this.y + this.height, a.y + a.height);
        if (f <= a) return new b(c, f, d - c, a - f);
      }
      return null;
    };
    b.prototype.union = function (a, c) {
      var d = Math.max(this.x + this.width, a.x + a.width),
        f = Math.max(this.y + this.height, a.y + a.height),
        e = Math.min(this.x, a.x),
        h = Math.min(this.y, a.y),
        d = d - e,
        f = f - h;
      if (c) return new b(e, h, d, f);
      this.x = e;
      this.y = h;
      this.width = d;
      this.height = f;
    };
    b.prototype.containsPoint = function (a, c) {
      return (
        this.x <= a &&
        a <= this.x + this.width &&
        this.y <= c &&
        c <= this.y + this.height
      );
    };
    b.prototype.clone = function () {
      return new b(this.x, this.y, this.width, this.height);
    };
    b.prototype.toString = function () {
      return (
        "(x=" +
        this.x +
        ", y=" +
        this.y +
        ", width=" +
        this.width +
        ", height=" +
        this.height +
        ")"
      );
    };
  })();
  (function () {
    Quark.KEY = {
      MOUSE_LEFT: 1,
      MOUSE_MID: 2,
      MOUSE_RIGHT: 3,
      BACKSPACE: 8,
      TAB: 9,
      NUM_CENTER: 12,
      ENTER: 13,
      RETURN: 13,
      SHIFT: 16,
      CTRL: 17,
      ALT: 18,
      PAUSE: 19,
      CAPS_LOCK: 20,
      ESC: 27,
      ESCAPE: 27,
      SPACE: 32,
      PAGE_UP: 33,
      PAGE_DOWN: 34,
      END: 35,
      HOME: 36,
      LEFT: 37,
      UP: 38,
      RIGHT: 39,
      DOWN: 40,
      PRINT_SCREEN: 44,
      INSERT: 45,
      DELETE: 46,
      ZERO: 48,
      ONE: 49,
      TWO: 50,
      THREE: 51,
      FOUR: 52,
      FIVE: 53,
      SIX: 54,
      SEVEN: 55,
      EIGHT: 56,
      NINE: 57,
      A: 65,
      B: 66,
      C: 67,
      D: 68,
      E: 69,
      F: 70,
      G: 71,
      H: 72,
      I: 73,
      J: 74,
      K: 75,
      L: 76,
      M: 77,
      N: 78,
      O: 79,
      P: 80,
      Q: 81,
      R: 82,
      S: 83,
      T: 84,
      U: 85,
      V: 86,
      W: 87,
      X: 88,
      Y: 89,
      Z: 90,
      CONTEXT_MENU: 93,
      NUM_ZERO: 96,
      NUM_ONE: 97,
      NUM_TWO: 98,
      NUM_THREE: 99,
      NUM_FOUR: 100,
      NUM_FIVE: 101,
      NUM_SIX: 102,
      NUM_SEVEN: 103,
      NUM_EIGHT: 104,
      NUM_NINE: 105,
      NUM_MULTIPLY: 106,
      NUM_PLUS: 107,
      NUM_MINUS: 109,
      NUM_PERIOD: 110,
      NUM_DIVISION: 111,
      F1: 112,
      F2: 113,
      F3: 114,
      F4: 115,
      F5: 116,
      F6: 117,
      F7: 118,
      F8: 119,
      F9: 120,
      F10: 121,
      F11: 122,
      F12: 123
    };
  })();
  (function () {
    var b = (Quark.EventManager = function () {
      this.keyState = {};
      this._evtHandlers = {};
    });
    b.prototype.registerStage = function (a, c, b, f) {
      this.register(a.context.canvas, c, { host: a, func: a._onEvent }, b, f);
    };
    b.prototype.unregisterStage = function (a, c) {
      this.unregister(a.context.canvas, c, a.onEvent);
    };
    b.prototype.register = function (a, c, b, f, e) {
      if (null == b || "function" == typeof b) b = { host: null, func: b };
      for (
        var h = { prevent: f, stop: e },
          j = this,
          f = function (a) {
            j._onEvent(a, h, b);
          },
          e = 0;
        e < c.length;
        e++
      ) {
        for (
          var i = c[e],
            g = this._evtHandlers[i] || (this._evtHandlers[i] = []),
            l = 0,
            m = !1;
          l < g.length;
          l++
        ) {
          var q = g[l];
          if (q.target == a && q.callback.func == b.func) {
            trace("duplicate callback");
            m = !0;
            break;
          }
        }
        m ||
          (g.push({ target: a, callback: b, handler: f }),
          a.addEventListener(i, f, !1));
      }
    };
    b.prototype.unregister = function (a, c, b) {
      for (var f = 0; f < c.length; f++)
        for (var e = c[f], h = this._evtHandlers[e], j = 0; j < h.length; j++) {
          var i = h[j];
          if (i.target == a && (i.callback.func == b || null == b)) {
            a.removeEventListener(e, i.handler);
            h.splice(j, 1);
            break;
          }
        }
    };
    b.prototype._onEvent = function (a, c, d) {
      var f = a,
        e = a.type;
      0 == a.type.indexOf("touch") &&
        ((f =
          a.touches && 0 < a.touches.length
            ? a.touches[0]
            : a.changedTouches && 0 < a.changedTouches.length
            ? a.changedTouches[0]
            : a),
        (f.type = e));
      if ("keydown" == e || "keyup" == e || "keypress" == e)
        this.keyState[a.keyCode] = e;
      null != d.func && d.func.call(d.host, f);
      b.stop(a, !c.prevent, !c.stop);
    };
    b.stop = function (a, c, b) {
      c || a.preventDefault();
      b ||
        (a.stopPropagation(),
        a.stopImmediatePropagation && a.stopImmediatePropagation());
    };
  })();
  (function () {
    var b = (Quark.EventDispatcher = function () {
      this._eventMap = {};
    });
    b.prototype.addEventListener = function (a, c) {
      var b = this._eventMap[a];
      null == b && (b = this._eventMap[a] = []);
      return -1 == b.indexOf(c) ? (b.push(c), !0) : !1;
    };
    b.prototype.removeEventListener = function (a, c) {
      var b = this._eventMap[a];
      if (null == b) return !1;
      for (var f = 0; f < b.length; f++)
        if (b[f] === c)
          return b.splice(f, 1), 0 == b.length && delete this._eventMap[a], !0;
      return !1;
    };
    b.prototype.removeEventListenerByType = function (a) {
      return null != this._eventMap[a] ? (delete this._eventMap[a], !0) : !1;
    };
    b.prototype.removeAllEventListeners = function () {
      this._eventMap = {};
    };
    b.prototype.dispatchEvent = function (a) {
      var c = this._eventMap[a.type];
      if (null == c) return !1;
      a.target || (a.target = this);
      for (var c = c.slice(), b = 0; b < c.length; b++) {
        var f = c[b];
        "function" == typeof f && f.call(this, a);
      }
      return !0;
    };
    b.prototype.hasEventListener = function (a) {
      a = this._eventMap[a];
      return null != a && 0 < a.length;
    };
    b.prototype.on = b.prototype.addEventListener;
    b.prototype.un = b.prototype.removeEventListener;
    b.prototype.fire = b.prototype.dispatchEvent;
  })();
  (function () {
    var b = (Quark.UIDUtil = { _counter: 0 });
    b.createUID = function (a) {
      var c = a.charCodeAt(a.length - 1);
      48 <= c && 57 >= c && (a += "_");
      return a + this._counter++;
    };
    b.displayObjectToString = function (a) {
      for (var c; null != a; a = a.parent) {
        var b = null != a.id ? a.id : a.name;
        c = null == c ? b : b + "." + c;
        if (a == a.parent) break;
      }
      return c;
    };
  })();
  (function () {
    function b(a, c) {
      for (var d = 0; d < a.children.length; d++) {
        var j = a.children[d];
        if (j.children) b(j, c);
        else if (null != c) {
          j = j.getBounds();
          c.globalAlpha = 0.2;
          c.beginPath();
          var i = j[0];
          c.moveTo(i.x - 0.5, i.y - 0.5);
          for (var g = 1; g < j.length; g++) {
            var l = j[g];
            c.lineTo(l.x - 0.5, l.y - 0.5);
          }
          c.lineTo(i.x - 0.5, i.y - 0.5);
          c.stroke();
          c.closePath();
          c.globalAlpha = 0.5;
          c.beginPath();
          c.rect((j.x >> 0) - 0.5, (j.y >> 0) - 0.5, j.width >> 0, j.height >> 0);
          c.stroke();
          c.closePath();
        } else
          j.drawable.domDrawable &&
            (j.drawable.domDrawable.style.border = "1px solid #f00");
      }
    }
    Quark.getUrlParams = function () {
      var a,
        c = {},
        b = window.location.href,
        d = b.indexOf("?");
      if (0 < d) {
        b = b.substring(d + 1).split("&");
        for (d = 0; (a = b[d]); d++)
          (a = b[d] = a.split("=")), (c[a[0]] = 1 < a.length ? a[1] : !0);
      }
      return c;
    };
    var a = document.getElementsByTagName("head")[0],
      c = a.getElementsByTagName("meta"),
      d = 0 < c.length ? c[c.length - 1].nextSibling : a.childNodes[0];
    Quark.addMeta = function (c) {
      var b = document.createElement("meta"),
        h;
      for (h in c) b.setAttribute(h, c[h]);
      a.insertBefore(b, d);
    };
    Quark.toggleDebugRect = function (a) {
      a.debug = !a.debug;
      a._render = a.debug
        ? function (c) {
            null != c.clear && c.clear(0, 0, a.width, a.height);
            Quark.Stage.superClass._render.call(a, c);
            c = a.context.context;
            null != c &&
              (c.save(),
              (c.lineWidth = 1),
              (c.strokeStyle = "#f00"),
              (c.globalAlpha = 0.5));
            b(a, c);
            null != c && c.restore();
          }
        : function (c) {
            null != c.clear && c.clear(0, 0, a.width, a.height);
            Quark.Stage.superClass._render.call(a, c);
          };
    };
  })();
  (function () {
    var b = (Quark.Timer = function (a) {
      this.interval = a || 50;
      this.paused = !1;
      this.info = { lastTime: 0, currentTime: 0, deltaTime: 0, realDeltaTime: 0 };
      this._startTime = 0;
      this._intervalID = null;
      this._listeners = [];
    });
    b.prototype.start = function () {
      if (null == this._intervalID) {
        this._startTime = this.info.lastTime = this.info.currentTime = Date.now();
        var a = this,
          c = function () {
            a._intervalID = setTimeout(c, a.interval);
            a._run();
          };
        c();
      }
    };
    b.prototype.stop = function () {
      clearTimeout(this._intervalID);
      this._intervalID = null;
      this._startTime = 0;
    };
    b.prototype.pause = function () {
      this.paused = !0;
    };
    b.prototype.resume = function () {
      this.paused = !1;
    };
    b.prototype._run = function () {
      if (!this.paused) {
        var a = this.info,
          c = (a.currentTime = Date.now());
        a.deltaTime = a.realDeltaTime = c - a.lastTime;
        for (var b = 0, f = this._listeners.length, e, h; b < f; b++)
          (e = this._listeners[b]),
            (h = e.__runTime || 0),
            0 == h
              ? e.step(this.info)
              : c > h &&
                (e.step(this.info), this._listeners.splice(b, 1), b--, f--);
        a.lastTime = c;
      }
    };
    b.prototype.delay = function (a, c) {
      this.addListener({ step: a, __runTime: Date.now() + c });
    };
    b.prototype.addListener = function (a) {
      if (null == a || "function" != typeof a.step)
        throw "Timer Error: The listener object must implement a step() method!";
      this._listeners.push(a);
    };
    b.prototype.removeListener = function (a) {
      a = this._listeners.indexOf(a);
      -1 < a && this._listeners.splice(a, 1);
    };
  })();
  (function () {
    var b = (Quark.ImageLoader = function (a) {
      b.superClass.constructor.call(this);
      this.loading = !1;
      this._index = -1;
      this._loaded = 0;
      this._images = {};
      this._totalSize = 0;
      this._loadHandler = Quark.delegate(this._loadHandler, this);
      this._addSource(a);
    });
    Quark.inherit(b, Quark.EventDispatcher);
    b.prototype.load = function (a) {
      this._addSource(a);
      this.loading || this._loadNext();
    };
    b.prototype._addSource = function (a) {
      if (a) {
        for (var a = a instanceof Array ? a : [a], c = 0; c < a.length; c++)
          this._totalSize += a[c].size || 0;
        this._source = this._source ? this._source.concat(a) : a;
      }
    };
    b.prototype._loadNext = function () {
      this._index++;
      if (this._index >= this._source.length)
        this.dispatchEvent({
          type: "complete",
          target: this,
          images: this._images
        }),
          (this._source = []),
          (this.loading = !1),
          (this._index = -1);
      else {
        var a = new Image();
        a.onload = this._loadHandler;
        a.src = this._source[this._index].src;
        this.loading = !0;
      }
    };
    b.prototype._loadHandler = function (a) {
      this._loaded++;
      var c = this._source[this._index];
      c.image = a.target;
      this._images[c.id || c.src] = c;
      this.dispatchEvent({ type: "loaded", target: this, image: c });
      this._loadNext();
    };
    b.prototype.getLoaded = function () {
      return this._loaded;
    };
    b.prototype.getTotal = function () {
      return this._source.length;
    };
    b.prototype.getLoadedSize = function () {
      var a = 0,
        c;
      for (c in this._images) a += this._images[c].size || 0;
      return a;
    };
    b.prototype.getTotalSize = function () {
      return this._totalSize;
    };
  })();
  (function () {
    var b = (Quark.Tween = function (c, b, f) {
      this.target = c;
      this.delay = this.time = 0;
      this.reverse = this.loop = this.paused = !1;
      this.interval = 0;
      this.ease = a.Linear.EaseNone;
      this.onComplete = this.onUpdate = this.onStart = this.next = null;
      this._oldProps = {};
      this._newProps = {};
      this._deltaProps = {};
      this._pausedStartTime = this._pausedTime = this._lastTime = this._startTime = 0;
      this._reverseFlag = 1;
      this._frameCount = this._frameTotal = 0;
      for (var e in b) {
        var h = c[e],
          j = b[e];
        void 0 !== h &&
          "number" == typeof h &&
          "number" == typeof j &&
          ((this._oldProps[e] = h),
          (this._newProps[e] = j),
          (this._deltaProps[e] = j - h));
      }
      for (e in f) this[e] = f[e];
    });
    b.prototype.setProps = function (a, b) {
      for (var f in a) this.target[f] = this._oldProps[f] = a[f];
      for (f in b)
        (this._newProps[f] = b[f]), (this._deltaProps[f] = b[f] - this.target[f]);
    };
    b.prototype._init = function () {
      this._startTime = Date.now() + this.delay;
      this._pausedTime = 0;
      0 < this.interval &&
        (this._frameTotal = Math.round(this.time / this.interval));
      b.add(this);
    };
    b.prototype.start = function () {
      this._init();
      this.paused = !1;
    };
    b.prototype.stop = function () {
      b.remove(this);
    };
    b.prototype.pause = function () {
      this.paused = !0;
      this._pausedStartTime = Date.now();
    };
    b.prototype.resume = function () {
      this.paused = !1;
      this._pausedTime += Date.now() - this._pausedStartTime;
    };
    b.prototype._update = function () {
      if (!this.paused) {
        var a = Date.now(),
          d = a - this._startTime - this._pausedTime;
        if (!(0 > d)) {
          if (0 == this._lastTime && null != this.onStart) this.onStart(this);
          this._lastTime = a;
          a =
            0 < this._frameTotal
              ? ++this._frameCount / this._frameTotal
              : d / this.time;
          1 < a && (a = 1);
          var d = this.ease(a),
            f;
          for (f in this._oldProps)
            this.target[f] =
              this._oldProps[f] + this._deltaProps[f] * this._reverseFlag * d;
          if (null != this.onUpdate) this.onUpdate(this, d);
          if (1 <= a) {
            if (this.reverse) {
              if (
                ((f = this._oldProps),
                (this._oldProps = this._newProps),
                (this._newProps = f),
                (this._startTime = Date.now()),
                (this._frameCount = 0),
                (this._reverseFlag *= -1),
                !this.loop)
              )
                this.reverse = !1;
            } else if (this.loop) {
              for (f in this._oldProps) this.target[f] = this._oldProps[f];
              this._startTime = Date.now();
              this._frameCount = 0;
            } else if (
              (b.remove(this),
              (f = this.next),
              null != f &&
                (f instanceof b ? ((a = f), (f = null)) : (a = f.shift()),
                null != a))
            )
              (a.next = f), a.start();
            if (null != this.onComplete) this.onComplete(this);
          }
        }
      }
    };
    b._tweens = [];
    b.step = function () {
      for (var a = this._tweens, b = a.length; 0 <= --b; ) a[b]._update();
    };
    b.add = function (a) {
      -1 == this._tweens.indexOf(a) && this._tweens.push(a);
      return this;
    };
    b.remove = function (a) {
      var b = this._tweens,
        a = b.indexOf(a);
      -1 < a && b.splice(a, 1);
      return this;
    };
    b.to = function (a, d, f) {
      a = new b(a, d, f);
      a._init();
      return a;
    };
    b.from = function (a, d, f) {
      d = new b(a, d, f);
      f = d._oldProps;
      d._oldProps = d._newProps;
      d._newProps = f;
      d._reverseFlag = -1;
      for (var e in d._oldProps) a[e] = d._oldProps[e];
      d._init();
      return d;
    };
    var a = (Quark.Easing = {
      Linear: {},
      Quadratic: {},
      Cubic: {},
      Quartic: {},
      Quintic: {},
      Sinusoidal: {},
      Exponential: {},
      Circular: {},
      Elastic: {},
      Back: {},
      Bounce: {}
    });
    a.Linear.EaseNone = function (a) {
      return a;
    };
    a.Quadratic.EaseIn = function (a) {
      return a * a;
    };
    a.Quadratic.EaseOut = function (a) {
      return -a * (a - 2);
    };
    a.Quadratic.EaseInOut = function (a) {
      return 1 > (a *= 2) ? 0.5 * a * a : -0.5 * (--a * (a - 2) - 1);
    };
    a.Cubic.EaseIn = function (a) {
      return a * a * a;
    };
    a.Cubic.EaseOut = function (a) {
      return --a * a * a + 1;
    };
    a.Cubic.EaseInOut = function (a) {
      return 1 > (a *= 2) ? 0.5 * a * a * a : 0.5 * ((a -= 2) * a * a + 2);
    };
    a.Quartic.EaseIn = function (a) {
      return a * a * a * a;
    };
    a.Quartic.EaseOut = function (a) {
      return -(--a * a * a * a - 1);
    };
    a.Quartic.EaseInOut = function (a) {
      return 1 > (a *= 2)
        ? 0.5 * a * a * a * a
        : -0.5 * ((a -= 2) * a * a * a - 2);
    };
    a.Quintic.EaseIn = function (a) {
      return a * a * a * a * a;
    };
    a.Quintic.EaseOut = function (a) {
      return (a -= 1) * a * a * a * a + 1;
    };
    a.Quintic.EaseInOut = function (a) {
      return 1 > (a *= 2)
        ? 0.5 * a * a * a * a * a
        : 0.5 * ((a -= 2) * a * a * a * a + 2);
    };
    a.Sinusoidal.EaseIn = function (a) {
      return -Math.cos((a * Math.PI) / 2) + 1;
    };
    a.Sinusoidal.EaseOut = function (a) {
      return Math.sin((a * Math.PI) / 2);
    };
    a.Sinusoidal.EaseInOut = function (a) {
      return -0.5 * (Math.cos(Math.PI * a) - 1);
    };
    a.Exponential.EaseIn = function (a) {
      return 0 == a ? 0 : Math.pow(2, 10 * (a - 1));
    };
    a.Exponential.EaseOut = function (a) {
      return 1 == a ? 1 : -Math.pow(2, -10 * a) + 1;
    };
    a.Exponential.EaseInOut = function (a) {
      return 0 == a
        ? 0
        : 1 == a
        ? 1
        : 1 > (a *= 2)
        ? 0.5 * Math.pow(2, 10 * (a - 1))
        : 0.5 * (-Math.pow(2, -10 * (a - 1)) + 2);
    };
    a.Circular.EaseIn = function (a) {
      return -(Math.sqrt(1 - a * a) - 1);
    };
    a.Circular.EaseOut = function (a) {
      return Math.sqrt(1 - --a * a);
    };
    a.Circular.EaseInOut = function (a) {
      return 1 > (a /= 0.5)
        ? -0.5 * (Math.sqrt(1 - a * a) - 1)
        : 0.5 * (Math.sqrt(1 - (a -= 2) * a) + 1);
    };
    a.Elastic.EaseIn = function (a) {
      var b,
        f = 0.1,
        e = 0.4;
      if (0 == a) return 0;
      if (1 == a) return 1;
      e || (e = 0.3);
      !f || 1 > f
        ? ((f = 1), (b = e / 4))
        : (b = (e / (2 * Math.PI)) * Math.asin(1 / f));
      return -(
        f *
        Math.pow(2, 10 * (a -= 1)) *
        Math.sin((2 * (a - b) * Math.PI) / e)
      );
    };
    a.Elastic.EaseOut = function (a) {
      var b,
        f = 0.1,
        e = 0.4;
      if (0 == a) return 0;
      if (1 == a) return 1;
      e || (e = 0.3);
      !f || 1 > f
        ? ((f = 1), (b = e / 4))
        : (b = (e / (2 * Math.PI)) * Math.asin(1 / f));
      return f * Math.pow(2, -10 * a) * Math.sin((2 * (a - b) * Math.PI) / e) + 1;
    };
    a.Elastic.EaseInOut = function (a) {
      var b,
        f = 0.1,
        e = 0.4;
      if (0 == a) return 0;
      if (1 == a) return 1;
      e || (e = 0.3);
      !f || 1 > f
        ? ((f = 1), (b = e / 4))
        : (b = (e / (2 * Math.PI)) * Math.asin(1 / f));
      return 1 > (a *= 2)
        ? -0.5 *
            f *
            Math.pow(2, 10 * (a -= 1)) *
            Math.sin((2 * (a - b) * Math.PI) / e)
        : 0.5 *
            f *
            Math.pow(2, -10 * (a -= 1)) *
            Math.sin((2 * (a - b) * Math.PI) / e) +
            1;
    };
    a.Back.EaseIn = function (a) {
      return a * a * (2.70158 * a - 1.70158);
    };
    a.Back.EaseOut = function (a) {
      return (a -= 1) * a * (2.70158 * a + 1.70158) + 1;
    };
    a.Back.EaseInOut = function (a) {
      return 1 > (a *= 2)
        ? 0.5 * a * a * (3.5949095 * a - 2.5949095)
        : 0.5 * ((a -= 2) * a * (3.5949095 * a + 2.5949095) + 2);
    };
    a.Bounce.EaseIn = function (b) {
      return 1 - a.Bounce.EaseOut(1 - b);
    };
    a.Bounce.EaseOut = function (a) {
      return (a /= 1) < 1 / 2.75
        ? 7.5625 * a * a
        : a < 2 / 2.75
        ? 7.5625 * (a -= 1.5 / 2.75) * a + 0.75
        : a < 2.5 / 2.75
        ? 7.5625 * (a -= 2.25 / 2.75) * a + 0.9375
        : 7.5625 * (a -= 2.625 / 2.75) * a + 0.984375;
    };
    a.Bounce.EaseInOut = function (b) {
      return 0.5 > b
        ? 0.5 * a.Bounce.EaseIn(2 * b)
        : 0.5 * a.Bounce.EaseOut(2 * b - 1) + 0.5;
    };
  })();
  (function () {
    var b = (Quark.Audio = function (a, c, d, f) {
      b.superClass.constructor.call(this);
      this.src = a;
      this.autoPlay = c && d;
      this.loop = f;
      this._playing = this._loaded = !1;
      this._evtHandler = Quark.delegate(this._evtHandler, this);
      this._element = document.createElement("audio");
      this._element.preload = c;
      a = a.substr(0, a.lastIndexOf("."));
      d = document.createElement("source");
      this._element.canPlayType("audio/mpeg")
        ? ((d.type = "audio/mpeg"), (d.src = a + ".mp3"))
        : ((d.type = "audio/ogg"), (d.src = a + ".ogg"));
      this._element.appendChild(d);
      c && this.load();
    });
    Quark.inherit(b, Quark.EventDispatcher);
    b.prototype.load = function () {
      this._element.addEventListener("progress", this._evtHandler, !1);
      this._element.addEventListener("ended", this._evtHandler, !1);
      this._element.addEventListener("error", this._evtHandler, !1);
      try {
        this._element.load();
      } catch (a) {
        trace(a);
      }
      this.progressCheck = setTimeout(function () {
        b._element.removeEventListener("progress", b._evtHandler);
        b._element.removeEventListener("error", b._evtHandler);
        b._loaded = !0;
        b.dispatchEvent({ type: "loaded", target: b });
        b.autoPlay && b.play();
        clearTimeout(b.progressCheck);
        b = b.progressCheck = null;
      }, 1e3);
      var b = this;
    };
    b.prototype._evtHandler = function (a) {
      clearTimeout(this.progressCheck);
      if ("progress" == a.type) {
        var b = 0,
          d = 0,
          f = a.target.buffered;
        if (f && 0 < f.length)
          for (b = f.length - 1; 0 <= b; b--) d = f.end(b) - f.start(b);
        if (1 <= d / a.target.duration || isNaN(a.target.duration))
          this._element.removeEventListener("progress", this._evtHandler),
            this._element.removeEventListener("error", this._evtHandler),
            (this._loaded = !0),
            this.dispatchEvent({ type: "loaded", target: this }),
            this.autoPlay && this.play();
      } else
        "ended" == a.type
          ? (this.dispatchEvent({ type: "ended", target: this }),
            this.loop ? this.play() : (this._playing = !1))
          : "error" == a.type && trace("Quark.Audio Error: " + a.target.src);
    };
    b.prototype.play = function () {
      this._loaded
        ? (this._element.play(), (this._playing = !0))
        : ((this.autoPlay = !0), this.load());
    };
    b.prototype.stop = function () {
      this._playing && (this._element.pause(), (this._playing = !1));
    };
    b.prototype.loaded = function () {
      return this._loaded;
    };
    b.prototype.playing = function () {
      return this._playing;
    };
  })();
  (function () {
    var b = (Quark.Drawable = function (a, b) {
      this.domDrawable = this.rawDrawable = null;
      this.set(a, b);
    });
    b.prototype.get = function (a, b) {
      if (null == b || null != b.canvas.getContext) return this.rawDrawable;
      null == this.domDrawable &&
        (this.domDrawable = Quark.createDOMDrawable(a, {
          image: this.rawDrawable
        }));
      return this.domDrawable;
    };
    b.prototype.set = function (a, b) {
      if (
        null == a
          ? 0
          : a instanceof HTMLImageElement ||
            a instanceof HTMLCanvasElement ||
            a instanceof HTMLVideoElement
      )
        this.rawDrawable = a;
      !0 === b
        ? (this.domDrawable = a)
        : this.domDrawable &&
          (this.domDrawable.style.backgroundImage =
            "url(" + this.rawDrawable.src + ")");
    };
  })();
  (function () {
    var b = (Quark.DisplayObject = function (a) {
      this.id = Quark.UIDUtil.createUID("DisplayObject");
      this.name = null;
      this.height = this.width = this.regY = this.regX = this.y = this.x = 0;
      this.scaleY = this.scaleX = this.alpha = 1;
      this.rotation = 0;
      this.transformEnabled = this.eventEnabled = this.visible = !0;
      this.useHandCursor = !1;
      this.context = this.parent = this.drawable = this.polyArea = null;
      this._depth = 0;
      this._lastState = {};
      this._stateList = "x y regX regY width height alpha scaleX scaleY rotation visible _depth".split(
        " "
      );
      Quark.merge(this, a, !0);
      a.mixin && Quark.merge(this, a.mixin, !1);
    });
    b.prototype.setDrawable = function (a) {
      null == this.drawable
        ? (this.drawable = new Quark.Drawable(a))
        : this.drawable.rawDrawable != a && this.drawable.set(a);
    };
    b.prototype.getDrawable = function (a) {
      return this.drawable && this.drawable.get(this, a);
    };
    b.prototype._update = function (a) {
      this.update(a);
    };
    b.prototype.update = function () {};
    b.prototype._render = function (a) {
      a = this.context || a;
      !this.visible || 0 >= this.alpha
        ? (null != a.hide && a.hide(this), this.saveState(["visible", "alpha"]))
        : (a.startDraw(),
          a.transform(this),
          this.render(a),
          a.endDraw(),
          this.saveState());
    };
    b.prototype.render = function (a) {
      a.draw(this, 0, 0, this.width, this.height, 0, 0, this.width, this.height);
    };
    b.prototype._onEvent = function (a) {
      if (null != this.onEvent) this.onEvent(a);
    };
    b.prototype.onEvent = null;
    b.prototype.saveState = function (a) {
      for (
        var a = a || this._stateList, b = this._lastState, d = 0, f = a.length;
        d < f;
        d++
      ) {
        var e = a[d];
        b["last" + e] = this[e];
      }
    };
    b.prototype.getState = function (a) {
      return this._lastState["last" + a];
    };
    b.prototype.propChanged = function () {
      for (
        var a = 0 < arguments.length ? arguments : this._stateList,
          b = 0,
          d = a.length;
        b < d;
        b++
      ) {
        var f = a[b];
        if (this._lastState["last" + f] != this[f]) return !0;
      }
      return !1;
    };
    b.prototype.hitTestPoint = function (a, b, d) {
      return Quark.hitTestPoint(this, a, b, d);
    };
    b.prototype.hitTestObject = function (a, b) {
      return Quark.hitTestObject(this, a, b);
    };
    b.prototype.localToGlobal = function (a, b) {
      var d = this.getConcatenatedMatrix();
      return { x: d.tx + a, y: d.ty + b };
    };
    b.prototype.globalToLocal = function (a, b) {
      var d = this.getConcatenatedMatrix().invert();
      return { x: d.tx + a, y: d.ty + b };
    };
    b.prototype.localToTarget = function (a, b, d) {
      a = this.localToGlobal(a, b);
      return d.globalToLocal(a.x, a.y);
    };
    b.prototype.getConcatenatedMatrix = function (a) {
      var b = new Quark.Matrix(1, 0, 0, 1, 0, 0);
      if (a == this) return b;
      for (var d = this; null != d.parent && d.parent != a; d = d.parent) {
        var f = 1,
          e = 0;
        0 != d.rotation % 360 &&
          ((e = d.rotation * Quark.DEG_TO_RAD),
          (f = Math.cos(e)),
          (e = Math.sin(e)));
        0 != d.regX && (b.tx -= d.regX);
        0 != d.regY && (b.ty -= d.regY);
        b.concat(
          new Quark.Matrix(
            f * d.scaleX,
            e * d.scaleX,
            -e * d.scaleY,
            f * d.scaleY,
            d.x,
            d.y
          )
        );
      }
      return b;
    };
    b.prototype.getBounds = function () {
      var a = this.width,
        b = this.height,
        d = this.getConcatenatedMatrix(),
        a = this.polyArea || [
          { x: 0, y: 0 },
          { x: a, y: 0 },
          { x: a, y: b },
          { x: 0, y: b }
        ],
        b = [],
        f = a.length,
        e,
        h,
        j,
        i,
        g;
      e = d.transformPoint(a[0], !0, !0);
      h = j = e.x;
      i = g = e.y;
      b[0] = e;
      for (var l = 1; l < f; l++)
        (e = d.transformPoint(a[l], !0, !0)),
          h > e.x ? (h = e.x) : j < e.x && (j = e.x),
          i > e.y ? (i = e.y) : g < e.y && (g = e.y),
          (b[l] = e);
      b.x = h;
      b.y = i;
      b.width = j - h;
      b.height = g - i;
      return b;
    };
    b.prototype.getCurrentWidth = function () {
      return Math.abs(this.width * this.scaleX);
    };
    b.prototype.getCurrentHeight = function () {
      return Math.abs(this.height * this.scaleY);
    };
    b.prototype.getStage = function () {
      for (var a = this; a.parent; ) a = a.parent;
      return a instanceof Quark.Stage ? a : null;
    };
    b.prototype.toString = function () {
      return Quark.UIDUtil.displayObjectToString(this);
    };
  })();
  (function () {
    var b = (Quark.DisplayObjectContainer = function (a) {
      this.eventChildren = !0;
      this.autoSize = !1;
      this.children = [];
      a = a || {};
      b.superClass.constructor.call(this, a);
      this.id = a.id || Quark.UIDUtil.createUID("DisplayObjectContainer");
      this.setDrawable(a.drawable || a.image || null);
      if (a.children)
        for (var c = 0; c < a.children.length; c++) this.addChild(a.children[c]);
    });
    Quark.inherit(b, Quark.DisplayObject);
    b.prototype.addChildAt = function (a, b) {
      0 > b ? (b = 0) : b > this.children.length && (b = this.children.length);
      var d = this.getChildIndex(a);
      if (-1 != d) {
        if (d == b) return this;
        this.children.splice(d, 1);
      } else a.parent && a.parent.removeChild(a);
      this.children.splice(b, 0, a);
      a.parent = this;
      if (this.autoSize) {
        var d = new Quark.Rectangle(
            0,
            0,
            this.rectWidth || this.width,
            this.rectHeight || this.height
          ),
          f = new Quark.Rectangle(
            a.x,
            a.y,
            a.rectWidth || a.width,
            a.rectHeight || a.height
          );
        d.union(f);
        this.width = d.width;
        this.height = d.height;
      }
      return this;
    };
    b.prototype.addChild = function (a) {
      for (var b = this.children.length, d = 0; d < arguments.length; d++)
        (a = arguments[d]), this.addChildAt(a, b + d);
      return this;
    };
    b.prototype.removeChildAt = function (a) {
      if (0 > a || a >= this.children.length) return !1;
      var b = this.children[a];
      null != b && (this.getStage().context.remove(b), (b.parent = null));
      this.children.splice(a, 1);
      return !0;
    };
    b.prototype.removeChild = function (a) {
      return this.removeChildAt(this.children.indexOf(a));
    };
    b.prototype.removeAllChildren = function () {
      for (; 0 < this.children.length; ) this.removeChildAt(0);
    };
    b.prototype.getChildAt = function (a) {
      return 0 > a || a >= this.children.length ? null : this.children[a];
    };
    b.prototype.getChildIndex = function (a) {
      return this.children.indexOf(a);
    };
    b.prototype.setChildIndex = function (a, b) {
      if (a.parent == this) {
        var d = this.children.indexOf(a);
        b != d && (this.children.splice(d, 1), this.children.splice(b, 0, a));
      }
    };
    b.prototype.swapChildren = function (a, b) {
      var d = this.getChildIndex(a),
        f = this.getChildIndex(b);
      this.children[d] = b;
      this.children[f] = a;
    };
    b.prototype.swapChildrenAt = function (a, b) {
      var d = this.getChildAt(a),
        f = this.getChildAt(b);
      this.children[a] = f;
      this.children[b] = d;
    };
    b.prototype.getChildById = function (a) {
      for (var b = 0, d = this.children.length; b < d; b++) {
        var f = this.children[b];
        if (f.id == a) return f;
      }
      return null;
    };
    b.prototype.removeChildById = function (a) {
      for (var b = 0, d = this.children.length; b < d; b++)
        if (this.children[b].id == a) return this.removeChildAt(b);
      return null;
    };
    b.prototype.sortChildren = function (a) {
      var b = a;
      "string" == typeof b &&
        (b = function (a, f) {
          return f[b] - a[b];
        });
      this.children.sort(b);
    };
    b.prototype.contains = function (a) {
      return -1 != this.getChildIndex(a);
    };
    b.prototype.getNumChildren = function () {
      return this.children.length;
    };
    b.prototype._update = function (a) {
      null != this.update && this.update(a);
      for (var b = this.children.slice(0), d = 0, f = b.length; d < f; d++) {
        var e = b[d];
        e._depth = d + 1;
        e._update(a);
      }
    };
    b.prototype.render = function (a) {
      b.superClass.render.call(this, a);
      for (var c = 0, d = this.children.length; c < d; c++)
        this.children[c]._render(a);
    };
    b.prototype.getObjectUnderPoint = function (a, b, d, f) {
      if (f) var e = [];
      for (var h = this.children.length - 1; 0 <= h; h--) {
        var j = this.children[h];
        if (
          !(
            null == j ||
            (!j.eventEnabled && void 0 == j.children) ||
            !j.visible ||
            0 >= j.alpha
          )
        )
          if (void 0 != j.children && j.eventChildren && 0 < j.getNumChildren()) {
            var i = j.getObjectUnderPoint(a, b, d, f);
            if (i)
              if (f) 0 < i.length && (e = e.concat(i));
              else return i;
            else if (0 <= j.hitTestPoint(a, b, d))
              if (f) e.push(j);
              else return j;
          } else if (0 <= j.hitTestPoint(a, b, d))
            if (f) e.push(j);
            else return j;
      }
      return f ? e : null;
    };
  })();
  (function () {
    var b = (Quark.Stage = function (a) {
      this.stageY = this.stageX = 0;
      this.paused = !1;
      this._eventTarget = null;
      a = a || {};
      b.superClass.constructor.call(this, a);
      this.id = a.id || Quark.UIDUtil.createUID("Stage");
      if (null == this.context) throw "Quark.Stage Error: context is required.";
      this.updatePosition();
    });
    Quark.inherit(b, Quark.DisplayObjectContainer);
    b.prototype.step = function (a) {
      this.paused || (this._update(a), this._render(this.context));
    };
    b.prototype._update = function (a) {
      for (var b = this.children.slice(0), d = 0, f = b.length; d < f; d++) {
        var e = b[d];
        e._depth = d + 1;
        e._update(a);
      }
      null != this.update && this.update(a);
    };
    b.prototype._render = function (a) {
      null != a.clear && a.clear(0, 0, this.width, this.height);
      b.superClass._render.call(this, a);
    };
    b.prototype._onEvent = function (a) {
      var b = a.pageX || a.clientX,
        d = a.pageY || a.clientY,
        b = (b - this.stageX) / this.scaleX,
        d = (d - this.stageY) / this.scaleY,
        f = this.getObjectUnderPoint(b, d, !0),
        e = this._eventTarget;
      a.eventX = b;
      a.eventY = d;
      null != e &&
        e != f &&
        ((a.lastEventTarget = e),
        (b =
          "mousemove" == a.type
            ? "mouseout"
            : "touchmove" == a.type
            ? "touchout"
            : null) && e._onEvent({ type: b }),
        (this._eventTarget = null));
      null != f &&
        f.eventEnabled &&
        ((a.eventTarget = e = this._eventTarget = f), f._onEvent(a));
      Quark.supportTouch ||
        (this.context.canvas.style.cursor =
          e && e.useHandCursor && e.eventEnabled ? "pointer" : "");
      if (null != this.onEvent) this.onEvent(a);
    };
    b.prototype.updatePosition = function () {
      var a = Quark.getElementOffset(this.context.canvas);
      this.stageX = a.left;
      this.stageY = a.top;
    };
  })();
  (function () {
    var b = (Quark.Bitmap = function (a) {
      this.image = null;
      this.rectHeight = this.rectWidth = this.rectY = this.rectX = 0;
      a = a || {};
      b.superClass.constructor.call(this, a);
      this.id = a.id || Quark.UIDUtil.createUID("Bitmap");
      this.setRect(a.rect || [0, 0, this.image.width, this.image.height]);
      this.setDrawable(this.image);
      this._stateList.push("rectX", "rectY", "rectWidth", "rectHeight");
    });
    Quark.inherit(b, Quark.DisplayObject);
    b.prototype.setRect = function (a) {
      this.rectX = a[0];
      this.rectY = a[1];
      this.rectWidth = this.width = a[2];
      this.rectHeight = this.height = a[3];
    };
    b.prototype.render = function (a) {
      a.draw(
        this,
        this.rectX,
        this.rectY,
        this.rectWidth,
        this.rectHeight,
        0,
        0,
        this.width,
        this.height
      );
    };
  })();
  (function () {
    var b = (Quark.MovieClip = function (a) {
      this.interval = 0;
      this.useFrames = this.paused = !1;
      this.currentFrame = 0;
      this._frames = [];
      this._frameLabels = {};
      this._frameDisObj = null;
      this._displayedCount = 0;
      a = a || {};
      b.superClass.constructor.call(this, a);
      this.id = a.id || Quark.UIDUtil.createUID("MovieClip");
      a.frames && this.addFrame(a.frames);
    });
    Quark.inherit(b, Quark.Bitmap);
    b.prototype.addFrame = function (a) {
      var b = this._frames.length;
      if (a instanceof Array)
        for (var d = 0; d < a.length; d++) this.setFrame(a[d], b + d);
      else this.setFrame(a, b);
      return this;
    };
    b.prototype.setFrame = function (a, b) {
      void 0 == b || b > this._frames.length
        ? (b = this._frames.length)
        : 0 > b && (b = 0);
      this._frames[b] = a;
      a.label && (this._frameLabels[a.label] = a);
      void 0 == a.interval && (a.interval = this.interval);
      0 == b && 0 == this.currentFrame && this.setRect(a.rect);
    };
    b.prototype.getFrame = function (a) {
      return "number" == typeof a ? this._frames[a] : this._frameLabels[a];
    };
    b.prototype.play = function () {
      this.paused = !1;
    };
    b.prototype.stop = function () {
      this.paused = !0;
    };
    b.prototype.gotoAndStop = function (a) {
      this.currentFrame = this.getFrameIndex(a);
      this.paused = !0;
    };
    b.prototype.gotoAndPlay = function (a) {
      this.currentFrame = this.getFrameIndex(a);
      this.paused = !1;
    };
    b.prototype.getFrameIndex = function (a) {
      if ("number" == typeof a) return a;
      for (
        var a = this._frameLabels[a], b = this._frames, d = 0;
        d < b.length;
        d++
      )
        if (a == b[d]) return d;
      return -1;
    };
    b.prototype.nextFrame = function (a) {
      var b = this._frames[this.currentFrame];
      0 < b.interval &&
        ((a = this._displayedCount + a),
        (this._displayedCount = b.interval > a ? a : 0));
      if (0 <= b.jump || "string" == typeof b.jump)
        if (0 == this._displayedCount || !b.interval)
          return (this.currentFrame = this.getFrameIndex(b.jump));
      return 0 < b.interval && 0 < this._displayedCount
        ? this.currentFrame
        : this.currentFrame >= this._frames.length - 1
        ? (this.currentFrame = 0)
        : ++this.currentFrame;
    };
    b.prototype._update = function (a) {
      var c = this._frames[this.currentFrame];
      c.stop
        ? this.stop()
        : (this.paused || this.nextFrame(this.useFrames ? 1 : a && a.deltaTime),
          this.setRect(c.rect),
          b.superClass._update.call(this, a));
    };
    b.prototype.render = function (a) {
      var b = this._frames[this.currentFrame].rect;
      a.draw(this, b[0], b[1], b[2], b[3], 0, 0, this.width, this.height);
    };
  })();
  (function () {
    var b = (Quark.Button = function (a) {
      this.state = b.UP;
      this.enabled = !0;
      a = a || {};
      b.superClass.constructor.call(this, a);
      this.id = a.id || Quark.UIDUtil.createUID("Button");
      this._skin = new Quark.MovieClip({ id: "skin", image: a.image });
      this.addChild(this._skin);
      this._skin.stop();
      this.eventChildren = !1;
      void 0 === a.useHandCursor && (this.useHandCursor = !0);
      a.up && this.setUpState(a.up);
      a.over && this.setOverState(a.over);
      a.down && this.setDownState(a.down);
      a.disabled && this.setDisabledState(a.disabled);
    });
    Quark.inherit(b, Quark.DisplayObjectContainer);
    b.UP = "up";
    b.OVER = "over";
    b.DOWN = "down";
    b.DISABLED = "disabled";
    b.prototype.setUpState = function (a) {
      a.label = b.UP;
      this._skin.setFrame(a, 0);
      this.upState = a;
      return this;
    };
    b.prototype.setOverState = function (a) {
      a.label = b.OVER;
      this._skin.setFrame(a, 1);
      this.overState = a;
      return this;
    };
    b.prototype.setDownState = function (a) {
      a.label = b.DOWN;
      this._skin.setFrame(a, 2);
      this.downState = a;
      return this;
    };
    b.prototype.setDisabledState = function (a) {
      a.label = b.DISABLED;
      this._skin.setFrame(a, 3);
      this.disabledState = a;
      return this;
    };
    b.prototype.setEnabled = function (a) {
      if (this.enabled == a) return this;
      (this.eventEnabled = this.enabled = a)
        ? 3 == this.currentFrame && this._skin.gotoAndStop(b.UP)
        : this.disabledState
        ? this._skin.gotoAndStop(b.DISABLED)
        : this._skin.gotoAndStop(b.state.UP);
      return this;
    };
    b.prototype.changeState = function (a) {
      if (this.state != a) {
        this.state = a;
        switch (a) {
          case b.OVER:
          case b.DOWN:
          case b.UP:
            this.enabled || (this.eventEnabled = this.enabled = !0);
            this._skin.gotoAndStop(a);
            break;
          case b.DISABLED:
            this.setEnabled(!1);
        }
        return this;
      }
    };
    b.prototype._onEvent = function (a) {
      if (this.enabled) {
        switch (a.type) {
          case "mousemove":
            this.overState && this.changeState(b.OVER);
            break;
          case "mousedown":
          case "touchstart":
          case "touchmove":
            this.downState && this.changeState(b.DOWN);
            break;
          case "mouseup":
            this.overState ? this.changeState(b.OVER) : this.changeState(b.UP);
            break;
          case "mouseout":
          case "touchout":
          case "touchend":
            this.upState && this.changeState(b.UP);
        }
        b.superClass._onEvent.call(this, a);
      }
    };
    b.prototype.setDrawable = function () {
      b.superClass.setDrawable.call(this, null);
    };
  })();
  (function () {
    var b = (Quark.Graphics = function (a) {
      a = a || {};
      b.superClass.constructor.call(this, a);
      this.id = Quark.UIDUtil.createUID("Graphics");
      this.lineWidth = 1;
      this.strokeStyle = "0";
      this.lineAlpha = 1;
      this.lineJoin = this.lineCap = null;
      this.miterLimit = 10;
      this.fillStyle = "0";
      this.fillAlpha = 1;
      this._actions = [];
      this._cache = null;
    });
    Quark.inherit(b, Quark.DisplayObject);
    b.prototype.lineStyle = function (a, b, d, f, e, h) {
      this._addAction(["lineWidth", (this.lineWidth = a || 1)]);
      this._addAction(["strokeStyle", (this.strokeStyle = b || "0")]);
      this._addAction(["lineAlpha", (this.lineAlpha = d || 1)]);
      void 0 != f && this._addAction(["lineCap", (this.lineCap = f)]);
      void 0 != e && this._addAction(["lineJoin", (this.lineJoin = e)]);
      void 0 != h && this._addAction(["miterLimit", (this.miterLimit = h)]);
      return this;
    };
    b.prototype.beginFill = function (a, b) {
      this._addAction(["fillStyle", (this.fillStyle = a)]);
      this._addAction(["fillAlpha", (this.fillAlpha = b || 1)]);
      return this;
    };
    b.prototype.endFill = function () {
      this._addAction(["stroke"]);
      this._addAction(["fill"]);
      return this;
    };
    b.prototype.beginLinearGradientFill = function (a, c, d, f, e, h) {
      a = b._getContext().createLinearGradient(a, c, d, f);
      c = 0;
      for (d = e.length; c < d; c++) a.addColorStop(h[c], e[c]);
      return this._addAction(["fillStyle", (this.fillStyle = a)]);
    };
    b.prototype.beginRadialGradientFill = function (a, c, d, f, e, h, j, i) {
      a = b._getContext().createRadialGradient(a, c, d, f, e, h);
      c = 0;
      for (d = j.length; c < d; c++) a.addColorStop(i[c], j[c]);
      return this._addAction(["fillStyle", (this.fillStyle = a)]);
    };
    b.prototype.beginBitmapFill = function (a, c) {
      return this._addAction([
        "fillStyle",
        (this.fillStyle = b._getContext().createPattern(a, c || ""))
      ]);
    };
    b.prototype.beginPath = function () {
      return this._addAction(["beginPath"]);
    };
    b.prototype.closePath = function () {
      return this._addAction(["closePath"]);
    };
    b.prototype.drawRect = function (a, b, d, f) {
      return this._addAction(["rect", a, b, d, f]);
    };
    b.prototype.drawRoundRectComplex = function (a, b, d, f, e, h, j, i) {
      this._addAction(["moveTo", a + e, b]);
      this._addAction(["lineTo", a + d - h, b]);
      this._addAction(["arc", a + d - h, b + h, h, -Math.PI / 2, 0, !1]);
      this._addAction(["lineTo", a + d, b + f - j]);
      this._addAction(["arc", a + d - j, b + f - j, j, 0, Math.PI / 2, !1]);
      this._addAction(["lineTo", a + i, b + f]);
      this._addAction(["arc", a + i, b + f - i, i, Math.PI / 2, Math.PI, !1]);
      this._addAction(["lineTo", a, b + e]);
      this._addAction(["arc", a + e, b + e, e, Math.PI, (3 * Math.PI) / 2, !1]);
      return this;
    };
    b.prototype.drawRoundRect = function (a, b, d, f, e) {
      return this.drawRoundRectComplex(a, b, d, f, e, e, e, e);
    };
    b.prototype.drawCircle = function (a, b, d) {
      return this._addAction(["arc", a + d, b + d, d, 0, 2 * Math.PI, 0]);
    };
    b.prototype.drawEllipse = function (a, b, d, f) {
      if (d == f) return this.drawCircle(a, b, d);
      var d = d / 2,
        f = f / 2,
        e = 0.5522847498307933 * d,
        h = 0.5522847498307933 * f,
        a = a + d,
        b = b + f;
      this._addAction(["moveTo", a + d, b]);
      this._addAction(["bezierCurveTo", a + d, b - h, a + e, b - f, a, b - f]);
      this._addAction(["bezierCurveTo", a - e, b - f, a - d, b - h, a - d, b]);
      this._addAction(["bezierCurveTo", a - d, b + h, a - e, b + f, a, b + f]);
      this._addAction(["bezierCurveTo", a + e, b + f, a + d, b + h, a + d, b]);
      return this;
    };
    b.prototype.render = function (a) {
      var c = a.context;
      null == c
        ? b.superClass.render.call(this, a)
        : null != this._cache
        ? c.drawImage(this._cache, 0, 0)
        : this._draw(c);
    };
    b.prototype._draw = function (a) {
      for (var b = 0, d = this._actions.length; b < d; b++) {
        var f = this._actions[b],
          e = f[0],
          h = 1 < f.length ? f.slice(1) : null;
        "function" == typeof a[e] ? a[e].apply(a, h) : (a[e] = f[1]);
      }
    };
    b.prototype.getDrawable = function (a) {
      null == this.drawable && this.setDrawable(this.toImage());
      return this.drawable.get(this, a);
    };
    b.prototype.cache = function (a) {
      var b = Quark.createDOM("canvas", {
        width: this.width,
        height: this.height
      });
      this._draw(b.getContext("2d"));
      this._cache = b;
      a && (this._cache = this.toImage());
      return this._cache;
    };
    b.prototype.uncache = function () {
      this._cache = null;
    };
    b.prototype.toImage = function (a) {
      var b = this._cache || this.cache(!0);
      if (b instanceof HTMLImageElement) return b;
      var d = new Image();
      d.src = b.toDataURL(a || "image/png");
      d.width = this.width;
      d.height = this.height;
      return d;
    };
    b.prototype.clear = function () {
      this._cache = this._actions.length = 0;
      this.lineWidth = 1;
      this.strokeStyle = "0";
      this.lineAlpha = 1;
      this.lineJoin = this.lineCap = null;
      this.miterLimit = 10;
      this.fillStyle = "0";
      this.fillAlpha = 1;
    };
    b.prototype._addAction = function (a) {
      this._actions.push(a);
      return this;
    };
    b._getContext = function () {
      var a = Quark.createDOM("canvas").getContext("2d");
      this._getContext = function () {
        return a;
      };
      return a;
    };
  })();
  (function () {
    var b = (Quark.Context = function (a) {
      if (null == a.canvas) throw "Quark.Context Error: canvas is required.";
      this.canvas = null;
      Quark.merge(this, a);
    });
    b.prototype.startDraw = function () {};
    b.prototype.draw = function () {};
    b.prototype.endDraw = function () {};
    b.prototype.transform = function () {};
    b.prototype.remove = function () {};
  })();
  (function () {
    var b = (Quark.CanvasContext = function (a) {
      b.superClass.constructor.call(this, a);
      this.context = this.canvas.getContext("2d");
    });
    Quark.inherit(b, Quark.Context);
    b.prototype.startDraw = function () {
      this.context.save();
    };
    b.prototype.draw = function (a) {
      var b = a.getDrawable(this);
      null != b &&
        ((arguments[0] = b),
        this.context.drawImage.apply(this.context, arguments));
    };
    b.prototype.endDraw = function () {
      this.context.restore();
    };
    b.prototype.transform = function (a) {
      var b = this.context;
      a instanceof Q.Stage
        ? (a._scaleX != a.scaleX &&
            ((a._scaleX = a.scaleX),
            (this.canvas.style.width = a._scaleX * a.width + "px")),
          a._scaleY != a.scaleY &&
            ((a._scaleY = a.scaleY),
            (this.canvas.style.height = a._scaleY * a.height + "px")))
        : ((0 != a.x || 0 != a.y) && b.translate(a.x, a.y),
          0 != a.rotation % 360 &&
            b.rotate((a.rotation % 360) * Quark.DEG_TO_RAD),
          (1 != a.scaleX || 1 != a.scaleY) && b.scale(a.scaleX, a.scaleY),
          (0 != a.regX || 0 != a.regY) && b.translate(-a.regX, -a.regY));
      0 < a.alpha && (b.globalAlpha *= a.alpha);
    };
    b.prototype.clear = function (a, b, d, f) {
      this.context.clearRect(a, b, d, f);
    };
  })();
  (function () {
    function b(a, b) {
      return b
        ? "" +
            ("translate3d(" +
              (a.x - a.regX) +
              "px, " +
              (a.y - a.regY) +
              "px, 0px)rotate3d(0, 0, 1, " +
              a.rotation +
              "deg)scale3d(" +
              a.scaleX +
              ", " +
              a.scaleY +
              ", 1)")
        : "" +
            ("translate(" +
              (a.x - a.regX) +
              "px, " +
              (a.y - a.regY) +
              "px)rotate(" +
              a.rotation +
              "deg)scale(" +
              a.scaleX +
              ", " +
              a.scaleY +
              ")");
    }
    var a = document.createElement("div"),
      c = void 0 != a.style[Quark.cssPrefix + "Transform"],
      d = void 0 != a.style[Quark.cssPrefix + "Perspective"],
      f = document.documentElement;
    if (d && "webkitPerspective" in f.style) {
      a.id = "test3d";
      var e = document.createElement("style");
      e.textContent = "@media (-webkit-transform-3d){#test3d{height:3px}}";
      document.head.appendChild(e);
      f.appendChild(a);
      d = 3 === a.offsetHeight;
      e.parentNode.removeChild(e);
      a.parentNode.removeChild(a);
    }
    Quark.supportTransform = c;
    Quark.supportTransform3D = d;
    if (c) {
      var h = (Quark.DOMContext = function (a) {
        h.superClass.constructor.call(this, a);
      });
      Quark.inherit(h, Quark.Context);
      h.prototype.draw = function (a) {
        if (!a._addedToDOM) {
          var b = a.parent,
            d = a.getDrawable(this);
          null == b && null == d.parentNode
            ? this.canvas.appendChild(d)
            : ((b = b.getDrawable(this)), d.parentNode != b && b.appendChild(d));
          a._addedToDOM = !0;
        }
      };
      h.prototype.transform = function (a) {
        var d = a.getDrawable(this);
        if (a.transformEnabled || !a._addedToDOM) {
          var e = Quark.cssPrefix,
            c = e + "TransformOrigin",
            e = e + "Transform",
            d = d.style;
          if (!d.display || a.propChanged("visible", "alpha"))
            d.display = !a.visible || 0 >= a.alpha ? "none" : "";
          if (!d.opacity || a.propChanged("alpha")) d.opacity = a.alpha;
          if (!d.backgroundPosition || a.propChanged("rectX", "rectY"))
            d.backgroundPosition = -a.rectX + "px " + -a.rectY + "px";
          if (!d.width || a.propChanged("width", "height"))
            (d.width = a.width + "px"), (d.height = a.height + "px");
          if (!d[c] || a.propChanged("regX", "regY"))
            d[c] = a.regX + "px " + a.regY + "px";
          if (
            !d[e] ||
            a.propChanged(
              "x",
              "y",
              "regX",
              "regY",
              "scaleX",
              "scaleY",
              "rotation"
            )
          )
            (c = Quark.supportTransform3D ? b(a, !0) : b(a, !1)), (d[e] = c);
          if (!d.zIndex || a.propChanged("_depth")) d.zIndex = a._depth;
        }
      };
      h.prototype.hide = function (a) {
        a.getDrawable(this).style.display = "none";
      };
      h.prototype.remove = function (a) {
        var b = a.getDrawable(this),
          d = b.parentNode;
        null != d && d.removeChild(b);
        a._addedToDOM = !1;
      };
    } else trace("Warn: DOMContext requires css transfrom support.");
  })();
  (function (b) {
    b.anvsoftJavaScriptSlideshow = b.aJSs = b.aJSs || {
      version: "1.0.0",
      global: b
    };
  })(window);
  (function () {
    aJSs.Events = {
      TRANSITION_OVER: "transitionOver",
      PLAY_CURRENT: "playCurrent",
      SOUND_PLAY_COMPLETE: "soundPlayComplete",
      PHOTO_MOUSE_OVER: "photoMouseOver",
      PHOTO_MOUSE_OUT: "photoMouseOut",
      PHOTO_LOAD_COMPLETE: "photoLoadComplete",
      PLAY_VIDEO: "playVideo",
      VIDEO_PLAY_ENDED: "videoPlayEnded",
      VIDEO_CLEAR: "videoClear",
      VIDEO_START_PLAY: "videoStartPlay",
      PLAY_NEXT: "playNext"
    };
  })();
  (function () {
    var b = aJSs,
      a = function () {
        this.handlers = {};
      };
    a.prototype = {
      constructor: a,
      addEventListener: function (a, b) {
        if (void 0 != a)
          "undefined" == typeof this.handlers[a] && (this.handlers[a] = []),
            this.handlers[a].push(b);
        else throw Error("undefined property events.");
      },
      dispatchEvent: function (a) {
        a.target || (a.target = this);
        if (this.handlers[a.type] instanceof Array)
          for (var b = this.handlers[a.type], e = 0, c = b.length; e < c; e++)
            b[e](a);
      },
      removeEventListener: function (a, b) {
        if (this.handlers[a] instanceof Array) {
          for (
            var e = this.handlers[a], c = 0, j = e.length;
            c < j && e[c] !== b;
            c++
          );
          e.splice(c, 1);
        }
      }
    };
    var c = new a();
    b.CommandDispatcher = {
      getInstance: function () {
        return c;
      }
    };
  })();
  (function () {
    aJSs.getParameters = {
      parameters: function () {
        var b = document.getElementsByTagName("script");
        try {
          for (
            var a = b[b.length - 1].src.split("?")[1].split("&"),
              b = {},
              c,
              d,
              f,
              e = 0,
              h = a.length;
            e < h;
            e++
          )
            (c = a[e].split("=")),
              (d = c[0]),
              (f = c[1]),
              "undefined" == typeof b[d]
                ? (b[d] = f)
                : ("string" == typeof b[d] && (b[d] = [b[d]]), b[d].push(f));
          return b;
        } catch (j) {
          return [];
        }
      }
    };
  })();
  (function () {
    aJSs.Music = function (b, a, c, d) {
      var f = "true" == d ? !0 : !1;
      this.soundAudio = new Quark.Audio(
        b,
        "true" == a ? !0 : !1,
        "true" == c ? !0 : !1,
        f
      );
      this.soundAudio.addEventListener(
        "ended",
        function () {
          f ||
            aJSs.CommandDispatcher.getInstance().dispatchEvent({
              type: aJSs.Events.SOUND_PLAY_COMPLETE
            });
        },
        !1
      );
      this.Playing = function () {
        return this.soundAudio.playing();
      };
      this.Play = function () {
        this.soundAudio.play();
      };
      this.Pause = function () {
        this.soundAudio.stop();
      };
    };
  })();
  (function () {
    aJSs.Video = function (b, a, c, d, f, e) {
      var a = "true" == a ? !0 : !1,
        d = "true" == d ? !0 : !1,
        b = b.substr(0, b.lastIndexOf(".")),
        h = document.createElement("video");
      h.width = f;
      h.height = e;
      try {
        h.buffered = c;
      } catch (j) {}
      h.autoplay = a;
      h.controls = d;
      h.loop = !1;
      h.preload = "none";
      c = document.createElement("source");
      h.appendChild(c);
      h.canPlayType &&
        ("" != h.canPlayType("video/mp4")
          ? ((c.type = "video/mp4"), (c.src = b + ".mp4"))
          : "" != h.canPlayType("video/ogg")
          ? ((c.type = "video/ogg"), (c.src = b + ".ogg"))
          : "" != h.canPlayType("video/webm")
          ? ((c.type = "video/webm"), (c.src = b + ".webm"))
          : alert("Your browser does not support the video tag."));
      a ? h.play() : h.pause();
      h.addEventListener(
        "ended",
        function () {
          aJSs.CommandDispatcher.getInstance().dispatchEvent({
            type: aJSs.Events.VIDEO_PLAY_ENDED
          });
        },
        !1
      );
      h.addEventListener(
        "playing",
        function () {
          aJSs.CommandDispatcher.getInstance().dispatchEvent({
            type: aJSs.Events.VIDEO_START_PLAY
          });
        },
        !1
      );
      return h;
    };
  })();
  (function () {
    aJSs.MaskEffect = function (b) {
      this.transTotal = 68;
      this.maskerFull = 0;
      var a = this,
        c,
        d;
      this.transition = function (a, b, d, c, i) {
        this.maskerFull = 0;
        if (a <= this.transTotal) this["mask" + a](b, d, c, i);
        else this.transition(68, b, d, c, i);
      };
      this.mask1 = function (f, e, h, j) {
        function i() {
          q = e * k * d;
          n = h * k * d;
          g.setRect([l, m, q, n]);
          k++;
          if (k > c || 1 == a.maskerFull)
            aJSs.CommandDispatcher.getInstance().dispatchEvent({
              type: aJSs.Events.TRANSITION_OVER
            }),
              g.setRect([0, 0, e, h]),
              clearInterval(p),
              (p = null);
        }
        var g = f.getChildAt(0),
          l = 0,
          m = 0,
          q = 0,
          n = 0;
        c = j * b;
        d = 1 / c;
        var p = setInterval(i, 1e3 / b),
          k = 1;
        i();
      };
      this.mask2 = function (f, e, h, j) {
        function i() {
          q = e * k * d;
          g.setRect([l, m, q, n]);
          k++;
          if (k > c || 1 == a.maskerFull)
            aJSs.CommandDispatcher.getInstance().dispatchEvent({
              type: "transitionOver"
            }),
              g.setRect([0, 0, e, h]),
              clearInterval(p),
              (p = null);
        }
        var g = f.getChildAt(0),
          l = 0,
          m = 0,
          q = 0,
          n = h;
        c = j * b;
        d = 1 / c;
        var p = setInterval(i, 1e3 / b),
          k = 1;
        i();
      };
      this.mask3 = function (f, e, h, j) {
        function i() {
          n = h * k * d;
          g.setRect([l, m, q, n]);
          k++;
          if (k > c || 1 == a.maskerFull)
            aJSs.CommandDispatcher.getInstance().dispatchEvent({
              type: "transitionOver"
            }),
              g.setRect([0, 0, e, h]),
              clearInterval(p),
              (p = null);
        }
        var g = f.getChildAt(0),
          l = 0,
          m = 0,
          q = e,
          n = 0;
        c = j * b;
        d = 1 / c;
        var p = setInterval(i, 1e3 / b),
          k = 1;
        i();
      };
      this.mask4 = function (f, e, h, j) {
        function i() {
          l = e * (1 - k * d);
          q = e * k * d;
          g.x = e * (1 - k * d);
          g.setRect([l, m, q, n]);
          k++;
          if (k > c || 1 == a.maskerFull)
            aJSs.CommandDispatcher.getInstance().dispatchEvent({
              type: "transitionOver"
            }),
              g.setRect([0, 0, e, h]),
              (g.x = 0),
              clearInterval(p),
              (p = null);
        }
        var g = f.getChildAt(0),
          l = e,
          m = 0,
          q = 0,
          n = h;
        c = j * b;
        d = 1 / c;
        var p = setInterval(i, 1e3 / b),
          k = 1;
        i();
      };
      this.mask5 = function (f, e, h, j) {
        function i() {
          m = h * (1 - k * d);
          n = h * k * d;
          g.y = h * (1 - k * d);
          g.setRect([l, m, q, n]);
          k++;
          if (k > c || 1 == a.maskerFull)
            aJSs.CommandDispatcher.getInstance().dispatchEvent({
              type: "transitionOver"
            }),
              g.setRect([0, 0, e, h]),
              (g.y = 0),
              clearInterval(p),
              (p = null);
        }
        var g = f.getChildAt(0),
          l = 0,
          m = h,
          q = e,
          n = 0;
        c = j * b;
        d = 1 / c;
        var p = setInterval(i, 1e3 / b),
          k = 1;
        i();
      };
      this.mask6 = function (f, e, h, j) {
        function i() {
          n = e * x * d;
          g.setRect([m, q, n, p]);
          k = e * (1 - x * d);
          t = e * x * d;
          l.x = e * (1 - x * d);
          l.setRect([k, r, t, s]);
          x++;
          if (x > c || 1 == a.maskerFull)
            aJSs.CommandDispatcher.getInstance().dispatchEvent({
              type: "transitionOver"
            }),
              g.setRect([0, 0, e, h]),
              f.removeChild(l),
              clearInterval(v),
              (v = null);
        }
        var g = f.getChildAt(0),
          l = new Quark.Bitmap({
            id: "targetBitmap2",
            image: g.image,
            rect: [0, 0, 0, 0]
          });
        f.addChild(l);
        var m = 0,
          q = 0,
          n = 0,
          p = h,
          k = e,
          r = 0,
          t = 0,
          s = h;
        c = j * b;
        d = 1 / (2 * c);
        var v = setInterval(i, 1e3 / b),
          x = 1;
        i();
      };
      this.mask7 = function (f, e, h, j) {
        function i() {
          p = h * x * d;
          g.setRect([m, q, n, p]);
          r = h * (1 - x * d);
          s = h * x * d;
          l.y = h * (1 - x * d);
          l.setRect([k, r, t, s]);
          x++;
          if (x > c || 1 == a.maskerFull)
            aJSs.CommandDispatcher.getInstance().dispatchEvent({
              type: "transitionOver"
            }),
              g.setRect([0, 0, e, h]),
              f.removeChild(l),
              clearInterval(v),
              (v = null);
        }
        var g = f.getChildAt(0),
          l = new Quark.Bitmap({
            id: "targetBitmap2",
            image: g.image,
            rect: [0, 0, 0, 0]
          });
        f.addChild(l);
        var m = 0,
          q = 0,
          n = e,
          p = 0,
          k = 0,
          r = h,
          t = e,
          s = 0;
        c = j * b;
        d = 1 / (2 * c);
        var v = setInterval(i, 1e3 / b),
          x = 1;
        i();
      };
      this.mask8 = function (f, e, h, j) {
        function i() {
          l = (e / 2) * (1 - k * d);
          q = e * k * d;
          g.x = (e / 2) * (1 - k * d);
          g.setRect([l, m, q, n]);
          k++;
          if (k > c || 1 == a.maskerFull)
            aJSs.CommandDispatcher.getInstance().dispatchEvent({
              type: "transitionOver"
            }),
              g.setRect([0, 0, e, h]),
              (g.x = 0),
              clearInterval(p),
              (p = null);
        }
        var g = f.getChildAt(0),
          l = e / 2,
          m = 0,
          q = 0,
          n = h;
        c = j * b;
        d = 1 / c;
        var p = setInterval(i, 1e3 / b),
          k = 1;
        i();
      };
      this.mask9 = function (f, e, h, j) {
        function i() {
          m = (h / 2) * (1 - k * d);
          n = h * k * d;
          g.y = (h / 2) * (1 - k * d);
          g.setRect([l, m, q, n]);
          k++;
          if (k > c || 1 == a.maskerFull)
            aJSs.CommandDispatcher.getInstance().dispatchEvent({
              type: "transitionOver"
            }),
              g.setRect([0, 0, e, h]),
              (g.y = 0),
              clearInterval(p),
              (p = null);
        }
        var g = f.getChildAt(0),
          l = 0,
          m = h / 2,
          q = e,
          n = 0;
        c = j * b;
        d = 1 / c;
        var p = setInterval(i, 1e3 / b),
          k = 1;
        i();
      };
      this.mask10 = function (f, e, h, j) {
        function i() {
          for (var b = 0; b < m; b++) {
            var j = b * q,
              i = q * r * d,
              l = h;
            f.getChildById("maskBitmap" + b).setRect([j, 0, i, l]);
          }
          r++;
          if (r > c || 1 == a.maskerFull) {
            aJSs.CommandDispatcher.getInstance().dispatchEvent({
              type: "transitionOver"
            });
            for (g.setRect([0, 0, e, h]); 1 < f.getNumChildren(); )
              f.removeChildAt(f.getNumChildren() - 1);
            clearInterval(k);
            k = null;
          }
        }
        for (
          var g = f.getChildAt(0), l = g.image, m = 16, q = e / m, n = 0;
          n < m;
          n++
        ) {
          var p = new Quark.Bitmap({
            id: "maskBitmap" + n,
            image: l,
            rect: [0, 0, 0, 0]
          });
          p.x = n * q;
          f.addChild(p);
        }
        c = j * b;
        d = 1 / c;
        var k = setInterval(i, 1e3 / b),
          r = 1;
        i();
      };
      this.mask11 = function (f, e, h, j) {
        function i() {
          for (var b = 0; b < m; b++) {
            var j = b * q,
              i = e,
              l = q * r * d;
            f.getChildById("maskBitmap" + b).setRect([0, j, i, l]);
          }
          r++;
          if (r > c || 1 == a.maskerFull) {
            aJSs.CommandDispatcher.getInstance().dispatchEvent({
              type: "transitionOver"
            });
            for (g.setRect([0, 0, e, h]); 1 < f.getNumChildren(); )
              f.removeChildAt(f.getNumChildren() - 1);
            clearInterval(k);
            k = null;
          }
        }
        for (
          var g = f.getChildAt(0), l = g.image, m = 16, q = h / m, n = 0;
          n < m;
          n++
        ) {
          var p = new Quark.Bitmap({
            id: "maskBitmap" + n,
            image: l,
            rect: [0, 0, 0, 0]
          });
          p.y = n * q;
          f.addChild(p);
        }
        c = j * b;
        d = 1 / c;
        var k = setInterval(i, 1e3 / b),
          r = 1;
        i();
      };
      this.mask12 = function (f, e, h, j) {
        function i() {
          for (n = 0; n < M; n++)
            (K = k.length),
              0 < K
                ? ((L = Math.floor(Math.random() * K)),
                  (k[L].visible = !0),
                  k.splice(L, 1))
                : (n = M);
          T++;
          if (T > c || 1 == a.maskerFull) {
            aJSs.CommandDispatcher.getInstance().dispatchEvent({
              type: aJSs.Events.TRANSITION_OVER
            });
            for (g.setRect([0, 0, e, h]); 1 < f.getNumChildren(); )
              f.removeChildAt(f.getNumChildren() - 1);
            clearInterval(x);
            x = null;
          }
        }
        for (
          var g = f.getChildAt(0),
            l = g.image,
            m = Math.ceil(e / 20),
            q = Math.ceil(h / 20),
            n = 0,
            p = 0,
            k = [],
            n = 0;
          20 > n;
          n++
        )
          for (p = 0; 20 > p; p++) {
            var r = m * n,
              t = q * p,
              s = m,
              v = q;
            r < e &&
              t < h &&
              (r > e - m && (s = e - r),
              t > h - q && (v = h - t),
              (s = new Quark.Bitmap({
                id: "maskBitmap" + n + p,
                image: l,
                rect: [r, t, s, v]
              })),
              (s.x = r),
              (s.y = t),
              (s.visible = !1),
              f.addChild(s),
              k.push(s));
          }
        c = j * b;
        d = 1 / c;
        var x = setInterval(i, 1e3 / b),
          T = 1,
          K = k.length,
          L,
          M = Math.round(K / c);
        1 > M && (M = 1);
        i();
      };
      this.mask13 = function (f, e, h, j) {
        function i() {
          l = (e / 2) * (1 - k * d);
          m = (h / 2) * (1 - k * d);
          q = e * k * d;
          n = h * k * d;
          g.x = (e / 2) * (1 - k * d);
          g.y = (h / 2) * (1 - k * d);
          g.setRect([l, m, q, n]);
          k++;
          if (k > c || 1 == a.maskerFull)
            aJSs.CommandDispatcher.getInstance().dispatchEvent({
              type: "transitionOver"
            }),
              g.setRect([0, 0, e, h]),
              (g.x = 0),
              (g.y = 0),
              clearInterval(p),
              (p = null);
        }
        var g = f.getChildAt(0),
          l = e / 2,
          m = h / 2,
          q = 0,
          n = 0;
        c = j * b;
        d = 1 / c;
        var p = setInterval(i, 1e3 / b),
          k = 1;
        i();
      };
      this.mask14 = function (a, b, d, c) {
        this.transition(68, a, b, d, c);
      };
      this.mask15 = function (a, b, d, c) {
        this.transition(68, a, b, d, c);
      };
      this.mask16 = function (a, b, d, c) {
        this.transition(68, a, b, d, c);
      };
      this.mask17 = function (a, b, d, c) {
        this.transition(68, a, b, d, c);
      };
      this.mask18 = function (a, b, d, c) {
        this.transition(68, a, b, d, c);
      };
      this.mask19 = function (a, b, d, c) {
        this.transition(68, a, b, d, c);
      };
      this.mask20 = function (a, b, d, c) {
        this.transition(68, a, b, d, c);
      };
      this.mask21 = function (f, e, h, j) {
        function i() {
          l = e * (1 - k * d);
          m = h * (1 - k * d);
          q = e * k * d;
          n = h * k * d;
          g.x = e * (1 - k * d);
          g.y = h * (1 - k * d);
          g.setRect([l, m, q, n]);
          k++;
          if (k > c || 1 == a.maskerFull)
            aJSs.CommandDispatcher.getInstance().dispatchEvent({
              type: "transitionOver"
            }),
              g.setRect([0, 0, e, h]),
              (g.x = 0),
              (g.y = 0),
              clearInterval(p),
              (p = null);
        }
        var g = f.getChildAt(0),
          l = e,
          m = h,
          q = 0,
          n = 0;
        c = j * b;
        d = 1 / c;
        var p = setInterval(i, 1e3 / b),
          k = 1;
        i();
      };
      this.mask22 = function (f, e, h, j) {
        function i() {
          l = e * (1 - k * d);
          m = 0;
          q = e * k * d;
          n = h * k * d;
          g.x = e * (1 - k * d);
          g.setRect([l, m, q, n]);
          k++;
          if (k > c || 1 == a.maskerFull)
            aJSs.CommandDispatcher.getInstance().dispatchEvent({
              type: "transitionOver"
            }),
              g.setRect([0, 0, e, h]),
              (g.x = 0),
              clearInterval(p),
              (p = null);
        }
        var g = f.getChildAt(0),
          l = e,
          m = 0,
          q = 0,
          n = 0;
        c = j * b;
        d = 1 / c;
        var p = setInterval(i, 1e3 / b),
          k = 1;
        i();
      };
      this.mask23 = function (f, e, h, j) {
        function i() {
          l = 0;
          m = h * (1 - k * d);
          q = e * k * d;
          n = h * k * d;
          g.y = h * (1 - k * d);
          g.setRect([l, m, q, n]);
          k++;
          if (k > c || 1 == a.maskerFull)
            aJSs.CommandDispatcher.getInstance().dispatchEvent({
              type: "transitionOver"
            }),
              g.setRect([0, 0, e, h]),
              (g.y = 0),
              clearInterval(p),
              (p = null);
        }
        var g = f.getChildAt(0),
          l = 0,
          m = h,
          q = 0,
          n = 0;
        c = j * b;
        d = 1 / c;
        var p = setInterval(i, 1e3 / b),
          k = 1;
        i();
      };
      this.mask24 = function (f, e, h, j) {
        function i() {
          r = (e / 2) * w * d;
          t = (h / 2) * w * d;
          g.setRect([p, k, r, t]);
          s = e / 2 + (e / 2) * (1 - w * d);
          v = 0;
          x = (e / 2) * w * d;
          T = (h / 2) * w * d;
          m.x = e / 2 + (e / 2) * (1 - w * d);
          m.setRect([s, v, x, T]);
          K = 0;
          L = h / 2 + (h / 2) * (1 - w * d);
          M = (e / 2) * w * d;
          X = (h / 2) * w * d;
          q.y = h / 2 + (h / 2) * (1 - w * d);
          q.setRect([K, L, M, X]);
          Y = e / 2 + (e / 2) * (1 - w * d);
          I = h / 2 + (h / 2) * (1 - w * d);
          D = (e / 2) * w * d;
          y = (h / 2) * w * d;
          n.x = e / 2 + (e / 2) * (1 - w * d);
          n.y = h / 2 + (h / 2) * (1 - w * d);
          n.setRect([Y, I, D, y]);
          w++;
          if (w > c || 1 == a.maskerFull) {
            aJSs.CommandDispatcher.getInstance().dispatchEvent({
              type: aJSs.Events.TRANSITION_OVER
            });
            for (g.setRect([0, 0, e, h]); 1 < f.getNumChildren(); )
              f.removeChildAt(f.getNumChildren() - 1);
            clearInterval(z);
            z = null;
          }
        }
        var g = f.getChildAt(0),
          l = g.image,
          m = new Quark.Bitmap({
            id: "targetBitmap2",
            image: l,
            rect: [0, 0, 0, 0]
          });
        f.addChild(m);
        var q = new Quark.Bitmap({
          id: "targetBitmap3",
          image: l,
          rect: [0, 0, 0, 0]
        });
        f.addChild(q);
        var n = new Quark.Bitmap({
          id: "targetBitmap4",
          image: l,
          rect: [0, 0, 0, 0]
        });
        f.addChild(n);
        var p = 0,
          k = 0,
          r = 0,
          t = 0,
          s = e,
          v = 0,
          x = 0,
          T = 0,
          K = 0,
          L = h,
          M = 0,
          X = 0,
          Y = e,
          I = h,
          D = 0,
          y = 0;
        c = j * b;
        d = 1 / c;
        var z = setInterval(i, 1e3 / b),
          w = 1;
        i();
      };
      this.mask25 = function (a, b, d, c) {
        this.transition(68, a, b, d, c);
      };
      this.mask26 = function (a, b, d, c) {
        this.transition(68, a, b, d, c);
      };
      this.mask27 = function (f, e, h, j) {
        function i() {
          for (var b = 0; b < m; b++) {
            var i = q * b,
              j = q;
            n[b].x > e - q && (j = e - n[b].x);
            var l = p[b] + ((h - p[b]) * x * d * h) / (h - p[b]);
            l < h && n[b].setRect([i, 0, j, l]);
          }
          x++;
          if (x > c || 1 == a.maskerFull) {
            aJSs.CommandDispatcher.getInstance().dispatchEvent({
              type: aJSs.Events.TRANSITION_OVER
            });
            for (g.setRect([0, 0, e, h]); 1 < f.getNumChildren(); )
              f.removeChildAt(f.getNumChildren() - 1);
            clearInterval(v);
            v = null;
          }
        }
        for (
          var g = f.getChildAt(0),
            l = g.image,
            m = 20,
            q = Math.ceil(e / m),
            n = [],
            p = [],
            k = 0;
          k < m;
          k++
        ) {
          p[k] = (h / 2) * Math.random();
          var r = q * k,
            t = q,
            s = p[k];
          r > e - q && (t = e - r);
          t = new Quark.Bitmap({
            id: "maskBitmap" + k,
            image: l,
            rect: [r, 0, t, s]
          });
          t.x = r;
          f.addChild(t);
          n.push(t);
        }
        c = j * b;
        d = 1 / c;
        var v = setInterval(i, 1e3 / b),
          x = 1;
        i();
      };
      this.mask28 = function (a, b, d, c) {
        this.transition(68, a, b, d, c);
      };
      this.mask29 = function (f, e, h, j) {
        function i() {
          g.alpha = m * d;
          m++;
          if (m > c || 1 == a.maskerFull)
            aJSs.CommandDispatcher.getInstance().dispatchEvent({
              type: aJSs.Events.TRANSITION_OVER
            }),
              (g.alpha = 1),
              clearInterval(l),
              (l = null);
        }
        var g = f.getChildAt(0);
        g.setRect([0, 0, e, h]);
        g.alpha = 0;
        c = j * b;
        d = 1 / c;
        var l = setInterval(i, 1e3 / b),
          m = 1;
        i();
      };
      this.mask30 = function (f, e, h, j) {
        function i() {
          l = e * (1 - k * d);
          q = e * k * d;
          g.setRect([l, m, q, n]);
          k++;
          if (k > c || 1 == a.maskerFull)
            aJSs.CommandDispatcher.getInstance().dispatchEvent({
              type: "transitionOver"
            }),
              g.setRect([0, 0, e, h]),
              (g.x = 0),
              clearInterval(p),
              (p = null);
        }
        var g = f.getChildAt(0),
          l = e,
          m = 0,
          q = 0,
          n = h;
        c = j * b;
        d = 1 / c;
        var p = setInterval(i, 1e3 / b),
          k = 1;
        i();
      };
      this.mask31 = function (f, e, h, j) {
        function i() {
          g.alpha = k * d;
          l = e * (1 - k * d);
          q = e * k * d;
          g.setRect([l, m, q, n]);
          k++;
          if (k > c || 1 == a.maskerFull)
            aJSs.CommandDispatcher.getInstance().dispatchEvent({
              type: "transitionOver"
            }),
              g.setRect([0, 0, e, h]),
              (g.x = 0),
              (g.alpha = 1),
              clearInterval(p),
              (p = null);
        }
        var g = f.getChildAt(0);
        g.alpha = 0;
        var l = e,
          m = 0,
          q = 0,
          n = h;
        c = j * b;
        d = 1 / c;
        var p = setInterval(i, 1e3 / b),
          k = 1;
        i();
      };
      this.mask32 = function (f, e, h, j) {
        function i() {
          q = e * k * d;
          g.setRect([l, m, q, n]);
          g.x = e * (1 - k * d);
          k++;
          if (k > c || 1 == a.maskerFull)
            aJSs.CommandDispatcher.getInstance().dispatchEvent({
              type: "transitionOver"
            }),
              g.setRect([0, 0, e, h]),
              (g.x = 0),
              clearInterval(p),
              (p = null);
        }
        var g = f.getChildAt(0);
        g.x = e;
        var l = 0,
          m = 0,
          q = 0,
          n = h;
        c = j * b;
        d = 1 / c;
        var p = setInterval(i, 1e3 / b),
          k = 1;
        i();
      };
      this.mask33 = function (f, e, h, j) {
        function i() {
          g.alpha = k * d;
          q = e * k * d;
          g.setRect([l, m, q, n]);
          g.x = e * (1 - k * d);
          k++;
          if (k > c || 1 == a.maskerFull)
            aJSs.CommandDispatcher.getInstance().dispatchEvent({
              type: "transitionOver"
            }),
              g.setRect([0, 0, e, h]),
              (g.x = 0),
              (g.alpha = 1),
              clearInterval(p),
              (p = null);
        }
        var g = f.getChildAt(0);
        g.x = e;
        var l = (g.alpha = 0),
          m = 0,
          q = 0,
          n = h;
        c = j * b;
        d = 1 / c;
        var p = setInterval(i, 1e3 / b),
          k = 1;
        i();
      };
      this.mask34 = function (f, e, h, j) {
        function i() {
          m = h * (1 - k * d);
          n = h * k * d;
          g.setRect([l, m, q, n]);
          k++;
          if (k > c || 1 == a.maskerFull)
            aJSs.CommandDispatcher.getInstance().dispatchEvent({
              type: "transitionOver"
            }),
              g.setRect([0, 0, e, h]),
              (g.y = 0),
              clearInterval(p),
              (p = null);
        }
        var g = f.getChildAt(0),
          l = 0,
          m = h,
          q = e,
          n = 0;
        c = j * b;
        d = 1 / c;
        var p = setInterval(i, 1e3 / b),
          k = 1;
        i();
      };
      this.mask35 = function (f, e, h, j) {
        function i() {
          g.alpha = k * d;
          m = h * (1 - k * d);
          n = h * k * d;
          g.setRect([l, m, q, n]);
          k++;
          if (k > c || 1 == a.maskerFull)
            aJSs.CommandDispatcher.getInstance().dispatchEvent({
              type: "transitionOver"
            }),
              g.setRect([0, 0, e, h]),
              (g.y = 0),
              (g.alpha = 1),
              clearInterval(p),
              (p = null);
        }
        var g = f.getChildAt(0),
          l = (g.alpha = 0),
          m = h,
          q = e,
          n = 0;
        c = j * b;
        d = 1 / c;
        var p = setInterval(i, 1e3 / b),
          k = 1;
        i();
      };
      this.mask36 = function (f, e, h, j) {
        function i() {
          g.y = h * (1 - k * d);
          n = h * k * d;
          g.setRect([l, m, q, n]);
          k++;
          if (k > c || 1 == a.maskerFull)
            aJSs.CommandDispatcher.getInstance().dispatchEvent({
              type: "transitionOver"
            }),
              g.setRect([0, 0, e, h]),
              (g.y = 0),
              clearInterval(p),
              (p = null);
        }
        var g = f.getChildAt(0);
        g.y = h;
        var l = 0,
          m = 0,
          q = e,
          n = 0;
        c = j * b;
        d = 1 / c;
        var p = setInterval(i, 1e3 / b),
          k = 1;
        i();
      };
      this.mask37 = function (f, e, h, j) {
        function i() {
          g.alpha = k * d;
          g.y = h * (1 - k * d);
          n = h * k * d;
          g.setRect([l, m, q, n]);
          k++;
          if (k > c || 1 == a.maskerFull)
            aJSs.CommandDispatcher.getInstance().dispatchEvent({
              type: "transitionOver"
            }),
              g.setRect([0, 0, e, h]),
              (g.y = 0),
              (g.alpha = 1),
              clearInterval(p),
              (p = null);
        }
        var g = f.getChildAt(0);
        g.alpha = 0;
        g.y = h;
        var l = 0,
          m = 0,
          q = e,
          n = 0;
        c = j * b;
        d = 1 / c;
        var p = setInterval(i, 1e3 / b),
          k = 1;
        i();
      };
      this.mask38 = function (f, e, h, j) {
        function i() {
          g.width = e * m * d;
          m++;
          if (m > c || 1 == a.maskerFull)
            aJSs.CommandDispatcher.getInstance().dispatchEvent({
              type: aJSs.Events.TRANSITION_OVER
            }),
              (g.width = e),
              clearInterval(l),
              (l = null);
        }
        var g = f.getChildAt(0);
        g.setRect([0, 0, e, h]);
        g.width = 0;
        c = j * b;
        d = 1 / c;
        var l = setInterval(i, 1e3 / b),
          m = 1;
        i();
      };
      this.mask39 = function (f, e, h, j) {
        function i() {
          g.alpha = m * d;
          g.width = e * m * d;
          m++;
          if (m > c || 1 == a.maskerFull)
            aJSs.CommandDispatcher.getInstance().dispatchEvent({
              type: aJSs.Events.TRANSITION_OVER
            }),
              (g.width = e),
              (g.alpha = 1),
              clearInterval(l),
              (l = null);
        }
        var g = f.getChildAt(0);
        g.setRect([0, 0, e, h]);
        g.alpha = 0;
        g.width = 0;
        c = j * b;
        d = 1 / c;
        var l = setInterval(i, 1e3 / b),
          m = 1;
        i();
      };
      this.mask40 = function (f, e, h, j) {
        function i() {
          g.x = (e / 2) * (1 - m * d);
          g.width = e * m * d;
          m++;
          if (m > c || 1 == a.maskerFull)
            aJSs.CommandDispatcher.getInstance().dispatchEvent({
              type: aJSs.Events.TRANSITION_OVER
            }),
              (g.width = e),
              (g.x = 0),
              clearInterval(l),
              (l = null);
        }
        var g = f.getChildAt(0);
        g.setRect([0, 0, e, h]);
        g.width = 0;
        g.x = e / 2;
        c = j * b;
        d = 1 / c;
        var l = setInterval(i, 1e3 / b),
          m = 1;
        i();
      };
      this.mask41 = function (f, e, h, j) {
        function i() {
          g.alpha = m * d;
          g.x = (e / 2) * (1 - m * d);
          g.width = e * m * d;
          m++;
          if (m > c || 1 == a.maskerFull)
            aJSs.CommandDispatcher.getInstance().dispatchEvent({
              type: aJSs.Events.TRANSITION_OVER
            }),
              (g.width = e),
              (g.x = 0),
              (g.alpha = 1),
              clearInterval(l),
              (l = null);
        }
        var g = f.getChildAt(0);
        g.setRect([0, 0, e, h]);
        g.width = 0;
        g.alpha = 0;
        g.x = e / 2;
        c = j * b;
        d = 1 / c;
        var l = setInterval(i, 1e3 / b),
          m = 1;
        i();
      };
      this.mask42 = function (f, e, h, j) {
        function i() {
          g.x = e * (1 - m * d);
          g.width = e * m * d;
          m++;
          if (m > c || 1 == a.maskerFull)
            aJSs.CommandDispatcher.getInstance().dispatchEvent({
              type: aJSs.Events.TRANSITION_OVER
            }),
              (g.width = e),
              (g.x = 0),
              clearInterval(l),
              (l = null);
        }
        var g = f.getChildAt(0);
        g.setRect([0, 0, e, h]);
        g.width = 0;
        g.x = e;
        c = j * b;
        d = 1 / c;
        var l = setInterval(i, 1e3 / b),
          m = 1;
        i();
      };
      this.mask43 = function (f, e, h, j) {
        function i() {
          g.alpha = m * d;
          g.x = e * (1 - m * d);
          g.width = e * m * d;
          m++;
          if (m > c || 1 == a.maskerFull)
            aJSs.CommandDispatcher.getInstance().dispatchEvent({
              type: aJSs.Events.TRANSITION_OVER
            }),
              (g.width = e),
              (g.x = 0),
              (g.alpha = 1),
              clearInterval(l),
              (l = null);
        }
        var g = f.getChildAt(0);
        g.setRect([0, 0, e, h]);
        g.width = 0;
        g.alpha = 0;
        g.x = e;
        c = j * b;
        d = 1 / c;
        var l = setInterval(i, 1e3 / b),
          m = 1;
        i();
      };
      this.mask44 = function (f, e, h, j) {
        function i() {
          g.height = h * m * d;
          m++;
          if (m > c || 1 == a.maskerFull)
            aJSs.CommandDispatcher.getInstance().dispatchEvent({
              type: aJSs.Events.TRANSITION_OVER
            }),
              (g.height = h),
              clearInterval(l),
              (l = null);
        }
        var g = f.getChildAt(0);
        g.setRect([0, 0, e, h]);
        g.height = 0;
        c = j * b;
        d = 1 / c;
        var l = setInterval(i, 1e3 / b),
          m = 1;
        i();
      };
      this.mask45 = function (f, e, h, j) {
        function i() {
          g.alpha = m * d;
          g.height = h * m * d;
          m++;
          if (m > c || 1 == a.maskerFull)
            aJSs.CommandDispatcher.getInstance().dispatchEvent({
              type: aJSs.Events.TRANSITION_OVER
            }),
              (g.height = h),
              (g.alpha = 1),
              clearInterval(l),
              (l = null);
        }
        var g = f.getChildAt(0);
        g.setRect([0, 0, e, h]);
        g.height = 0;
        g.alpha = 0;
        c = j * b;
        d = 1 / c;
        var l = setInterval(i, 1e3 / b),
          m = 1;
        i();
      };
      this.mask46 = function (f, e, h, j) {
        function i() {
          g.y = (h / 2) * (1 - m * d);
          g.height = h * m * d;
          m++;
          if (m > c || 1 == a.maskerFull)
            aJSs.CommandDispatcher.getInstance().dispatchEvent({
              type: aJSs.Events.TRANSITION_OVER
            }),
              (g.height = h),
              (g.y = 0),
              clearInterval(l),
              (l = null);
        }
        var g = f.getChildAt(0);
        g.setRect([0, 0, e, h]);
        g.height = 0;
        g.y = h / 2;
        c = j * b;
        d = 1 / c;
        var l = setInterval(i, 1e3 / b),
          m = 1;
        i();
      };
      this.mask47 = function (f, e, h, j) {
        function i() {
          g.alpha = m * d;
          g.y = (h / 2) * (1 - m * d);
          g.height = h * m * d;
          m++;
          if (m > c || 1 == a.maskerFull)
            aJSs.CommandDispatcher.getInstance().dispatchEvent({
              type: aJSs.Events.TRANSITION_OVER
            }),
              (g.height = h),
              (g.y = 0),
              (g.alpha = 1),
              clearInterval(l),
              (l = null);
        }
        var g = f.getChildAt(0);
        g.setRect([0, 0, e, h]);
        g.height = 0;
        g.alpha = 0;
        g.y = h / 2;
        c = j * b;
        d = 1 / c;
        var l = setInterval(i, 1e3 / b),
          m = 1;
        i();
      };
      this.mask48 = function (f, e, h, j) {
        function i() {
          g.y = h * (1 - m * d);
          g.height = h * m * d;
          m++;
          if (m > c || 1 == a.maskerFull)
            aJSs.CommandDispatcher.getInstance().dispatchEvent({
              type: aJSs.Events.TRANSITION_OVER
            }),
              (g.height = h),
              (g.y = 0),
              clearInterval(l),
              (l = null);
        }
        var g = f.getChildAt(0);
        g.setRect([0, 0, e, h]);
        g.height = 0;
        g.y = h;
        c = j * b;
        d = 1 / c;
        var l = setInterval(i, 1e3 / b),
          m = 1;
        i();
      };
      this.mask49 = function (f, e, h, j) {
        function i() {
          g.alpha = m * d;
          g.y = h * (1 - m * d);
          g.height = h * m * d;
          m++;
          if (m > c || 1 == a.maskerFull)
            aJSs.CommandDispatcher.getInstance().dispatchEvent({
              type: aJSs.Events.TRANSITION_OVER
            }),
              (g.height = h),
              (g.y = 0),
              (g.alpha = 1),
              clearInterval(l),
              (l = null);
        }
        var g = f.getChildAt(0);
        g.setRect([0, 0, e, h]);
        g.height = 0;
        g.alpha = 0;
        g.y = h;
        c = j * b;
        d = 1 / c;
        var l = setInterval(i, 1e3 / b),
          m = 1;
        i();
      };
      this.mask50 = function (f, e, h, j) {
        function i() {
          g.x = (e / 2) * (1 - m * d);
          g.y = (h / 2) * (1 - m * d);
          g.width = e * m * d;
          g.height = h * m * d;
          m++;
          if (m > c || 1 == a.maskerFull)
            aJSs.CommandDispatcher.getInstance().dispatchEvent({
              type: aJSs.Events.TRANSITION_OVER
            }),
              (g.width = e),
              (g.height = h),
              (g.x = 0),
              (g.y = 0),
              clearInterval(l),
              (l = null);
        }
        var g = f.getChildAt(0);
        g.setRect([0, 0, e, h]);
        g.width = 0;
        g.height = 0;
        g.x = e / 2;
        g.y = h / 2;
        c = j * b;
        d = 1 / c;
        var l = setInterval(i, 1e3 / b),
          m = 1;
        i();
      };
      this.mask51 = function (f, e, h, j) {
        function i() {
          g.alpha = m * d;
          g.x = (e / 2) * (1 - m * d);
          g.y = (h / 2) * (1 - m * d);
          g.width = e * m * d;
          g.height = h * m * d;
          m++;
          if (m > c || 1 == a.maskerFull)
            aJSs.CommandDispatcher.getInstance().dispatchEvent({
              type: aJSs.Events.TRANSITION_OVER
            }),
              (g.width = e),
              (g.height = h),
              (g.x = 0),
              (g.y = 0),
              (g.alpha = 1),
              clearInterval(l),
              (l = null);
        }
        var g = f.getChildAt(0);
        g.setRect([0, 0, e, h]);
        g.width = 0;
        g.height = 0;
        g.alpha = 0;
        g.x = e / 2;
        g.y = h / 2;
        c = j * b;
        d = 1 / c;
        var l = setInterval(i, 1e3 / b),
          m = 1;
        i();
      };
      this.mask52 = function (a, b, d) {
        a.getChildAt(0).setRect([0, 0, b, d]);
        aJSs.CommandDispatcher.getInstance().dispatchEvent({
          type: aJSs.Events.TRANSITION_OVER
        });
      };
      this.mask53 = function (a, b, d, c) {
        this.transition(68, a, b, d, c);
      };
      this.mask54 = function (a, b, d, c) {
        this.transition(68, a, b, d, c);
      };
      this.mask55 = function (a, b, d, c) {
        this.transition(68, a, b, d, c);
      };
      this.mask56 = function (a, b, d, c) {
        this.transition(68, a, b, d, c);
      };
      this.mask57 = function (a, b, d, c) {
        this.transition(68, a, b, d, c);
      };
      this.mask58 = function (a, b, d, c) {
        this.transition(68, a, b, d, c);
      };
      this.mask59 = function (a, b, d, c) {
        this.transition(68, a, b, d, c);
      };
      this.mask60 = function (a, b, d, c) {
        this.transition(68, a, b, d, c);
      };
      this.mask61 = function (a, b, d, c) {
        this.transition(68, a, b, d, c);
      };
      this.mask62 = function (a, b, d, c) {
        this.transition(68, a, b, d, c);
      };
      this.mask63 = function (a, b, d, c) {
        this.transition(68, a, b, d, c);
      };
      this.mask64 = function (a, b, d, c) {
        this.transition(68, a, b, d, c);
      };
      this.mask65 = function (a, b, d, c) {
        this.transition(68, a, b, d, c);
      };
      this.mask66 = function (a, b, d, c) {
        this.transition(68, a, b, d, c);
      };
      this.mask67 = function (a, b, d, c) {
        this.transition(68, a, b, d, c);
      };
      this.mask68 = function (f, e, h, j) {
        function i() {
          for (n = 0; n < w; n++)
            (k[n].width = x[n] * z * d),
              (k[n].height = T[n] * z * d),
              (k[n].x = s[n] + (r[n] - s[n]) * z * d),
              (k[n].y = v[n] + (t[n] - v[n]) * z * d);
          z++;
          if (z > c || 1 == a.maskerFull) {
            aJSs.CommandDispatcher.getInstance().dispatchEvent({
              type: aJSs.Events.TRANSITION_OVER
            });
            for (g.setRect([0, 0, e, h]); 1 < f.getNumChildren(); )
              f.removeChildAt(f.getNumChildren() - 1);
            clearInterval(y);
            y = null;
          }
        }
        for (
          var g = f.getChildAt(0),
            l = g.image,
            m = Math.ceil(e / 12),
            q = Math.ceil(h / 12),
            n = 0,
            p = 0,
            k = [],
            r = [],
            t = [],
            s = [],
            v = [],
            x = [],
            T = [],
            n = 0;
          12 > n;
          n++
        )
          for (p = 0; 12 > p; p++) {
            var K = m * n,
              L = q * p,
              M = m,
              X = q,
              Y = Math.random() * (e - m),
              I = Math.random() * (h - q);
            if (K < e && L < h) {
              K > e - m && (M = e - K);
              L > h - q && (X = h - L);
              var D = new Quark.Bitmap({
                id: "maskBitmap" + n + p,
                image: l,
                rect: [K, L, M, X]
              });
              D.x = Y;
              D.y = I;
              D.width = 0;
              D.height = 0;
              f.addChild(D);
              k.push(D);
              r.push(K);
              t.push(L);
              x.push(M);
              T.push(X);
              s.push(Y);
              v.push(I);
            }
          }
        c = j * b;
        d = 1 / c;
        var y = setInterval(i, 1e3 / b),
          z = 1,
          w = k.length;
        i();
      };
    };
  })();
  (function () {
    aJSs.JsXmlLoad = function (b) {
      var a = this;
      a.copyright = "Anvsoft";
      a.movieWidth = 0;
      a.movieHeight = 0;
      a.startAutoPlay = "";
      a.continuum = "";
      a.clickToAutoPlay = "";
      a.randomPlayingPhotos = "";
      a.enableURL = "";
      a.movieBackgroundColor = "";
      a.loadStyle = "";
      a.anvsoftMenu = "";
      a.frameRate = 0;
      a.globalTitleXml = "";
      a.musicPath = "";
      a.musicStream = "";
      a.musicLoop = "";
      a.musicAutoPlay = "";
      a.topPadding = 0;
      a.bottomPadding = 0;
      a.leftPadding = 0;
      a.rightPadding = 0;
      a.globalDescriptionXml = "";
      a.videoAutoPlay = "";
      a.bufferTime = "";
      a.videoControls = "";
      a.thumbnailBasicXml = "";
      a.thumbnailArray = [];
      a.photoArray = [];
      a.photoUrlArray = [];
      a.URLTarget = [];
      a.videoArray = [];
      a.transitionArray = [];
      a.photoTimeArray = [];
      a.transitionTimeArray = [];
      a.defineTransitionArray = [];
      a.photoTitleArray = [];
      a.descriptionText = [];
      var c = function (b) {
        b = b.documentElement;
        a.copyright = b.getAttribute("copyright");
        var d = b.getElementsByTagName("global")[0],
          c = d.getElementsByTagName("basic_property")[0];
        a.movieWidth = c.getAttribute("movieWidth");
        a.movieHeight = c.getAttribute("movieHeight");
        a.startAutoPlay = c.getAttribute("startAutoPlay");
        a.continuum = c.getAttribute("continuum");
        a.clickToAutoPlay = c.getAttribute("clickToAutoPlay");
        a.randomPlayingPhotos = c.getAttribute("randomPlayingPhotos");
        a.enableURL = c.getAttribute("enableURL");
        a.movieBackgroundColor = c
          .getAttribute("backgroundColor")
          .replace(/0x/g, "#");
        a.loadStyle = c.getAttribute("loadStyle");
        a.anvsoftMenu = c.getAttribute("anvsoftMenu");
        a.frameRate = c.getAttribute("frameRate");
        c = c.getAttribute("transitionArray");
        a.defineTransitionArray = "" == c ? null : c.split(",");
        a.globalTitleXml = d.getElementsByTagName("title_property")[0];
        c = d.getElementsByTagName("music_property")[0];
        a.musicPath = c.getAttribute("path");
        a.musicStream = c.getAttribute("stream");
        a.musicLoop = c.getAttribute("loop");
        a.musicAutoPlay = c.getAttribute("autoPlay");
        c = d.getElementsByTagName("photo_property")[0];
        a.topPadding = Number(c.getAttribute("topPadding"));
        a.bottomPadding = Number(c.getAttribute("bottomPadding"));
        a.leftPadding = Number(c.getAttribute("leftPadding"));
        a.rightPadding = Number(c.getAttribute("rightPadding"));
        a.globalDescriptionXml = d.getElementsByTagName(
          "description_property"
        )[0];
        d = d.getElementsByTagName("video_property")[0];
        a.videoAutoPlay = d.getAttribute("autoPlay");
        a.bufferTime = Number(d.getAttribute("bufferTime"));
        a.videoControls = d.getAttribute("controls");
        d = b.getElementsByTagName("thumbnail")[0];
        void 0 != d &&
          (a.thumbnailBasicXml = d.getElementsByTagName("basic_property")[0]);
        b = b.getElementsByTagName("album")[0].getElementsByTagName("slide");
        d = b.length;
        for (c = 0; c < d; c++) {
          a.thumbnailArray[c] = b[c].getAttribute("jpegURL");
          a.photoArray[c] = b[c].getAttribute("d_URL");
          a.photoUrlArray[c] = b[c].getAttribute("url");
          a.URLTarget[c] = b[c].getAttribute("URLTarget");
          a.videoArray[c] = b[c].getAttribute("v_URL");
          a.transitionArray[c] = b[c].getAttribute("transition");
          a.photoTimeArray[c] = b[c].getAttribute("phototime");
          a.transitionTimeArray[c] = b[c].getAttribute("transitiontime");
          a.photoTitleArray[c] = b[c].getAttribute("title");
          var e = b[c].childNodes[0];
          a.descriptionText[c] = void 0 != e ? e.nodeValue : "";
        }
      };
      try {
        var d = new ActiveXObject("Microsoft.XMLDOM");
      } catch (f) {
        try {
          d = document.implementation.createDocument("", "", null);
        } catch (e) {
          alert(e.message);
        }
      }
      try {
        (d.async = !1), d.load(b), c(d);
      } catch (h) {
        try {
          var j = new window.XMLHttpRequest();
          j.open("GET", b, !1);
          j.send(null);
          d = j.responseXML;
          c(d);
        } catch (i) {
          (d = new DOMParser().parseFromString(
            window.anvsoftJavaScriptSlideshowData,
            "text/xml"
          )),
            c(d);
        }
      }
    };
  })();
  (function () {
    aJSs.JsCompatibleTheme = function (b, a, c) {
      function d() {
        p--;
        0 >= p &&
          (clearInterval(r), k++, k > n - 1 && (k = 0), (s.src = c + e[k]));
      }
      var f = b.movieBackgroundColor,
        e = b.photoArray,
        h = b.photoUrlArray,
        j = b.photoTimeArray,
        i = b.transitionTimeArray,
        g = b.URLTarget,
        l = b.topPadding,
        m = b.bottomPadding,
        q = b.leftPadding,
        b = b.rightPadding,
        n = e.length,
        p = 0,
        k = 0,
        r = null,
        t = document.getElementById(a);
      t.style.backgroundColor = f;
      var a = t.offsetWidth,
        f = t.offsetHeight,
        q = a - q - b,
        l = f - l - m,
        m = Math.round((a - q) / 2),
        b = Math.round((f - l) / 2),
        s = new Image();
      t.appendChild(s);
      s.style.position = "absolute";
      s.style.width = q + "px";
      s.style.height = l + "px";
      s.style.left = m + "px";
      s.style.top = b + "px";
      s.src = c + e[k];
      s.onload = function () {
        p = parseInt(i[k]) + parseInt(j[k]);
        r = setInterval(d, 1e3);
      };
      s.onclick = function () {
        var a;
        switch (g[k]) {
          case "0":
            a = "_blank";
            break;
          case "1":
            a = "_parent";
            break;
          case "2":
            a = "_self";
            break;
          case "3":
            a = "_top";
            break;
          default:
            a = "_blank";
        }
        window.open(h[k], a);
      };
      var v = document.createElement("div");
      t.appendChild(v);
      v.style.position = "absolute";
      v.style.width = "250px";
      v.style.padding = "8px";
      v.style.backgroundColor = "#333";
      v.style.color = "#FFF";
      v.style.textAlign = "left";
      v.style.font = "normal normal 12px/16px verdana,tahoma,arial,sans-serif";
      v.innerHTML =
        "The browser you are using does not support HTML5. Now you are using the simple compatible mode. To get better user experience, please use HTML5 supported browser.";
      v.style.left = Math.round((a - v.offsetWidth) / 2) + "px";
      v.style.top = Math.round((f - v.offsetHeight) / 2) + "px";
      var x = setTimeout(function () {
        clearTimeout(x);
        x = null;
        t.removeChild(v);
      }, 1e4);
    };
  })();
  (function () {
    aJSs.JsBackground = function (b, a) {
      var c = b.movieBackgroundColor,
        d = new Quark.DisplayObjectContainer({ id: "backgroundBox" });
      d.autoSize = !0;
      a.addChild(d);
      if ("" != c) {
        var f = Quark.Bitmap,
          e = a.width,
          h = a.height,
          j = document.createElement("canvas");
        j.width = e;
        j.height = h;
        var i = j.getContext("2d");
        i.fillStyle = c;
        i.rect(0, 0, e, h);
        i.fill();
        c = new Image();
        c.src = j.toDataURL("image/png");
        c.width = e;
        c.height = h;
        f = new f({ id: "background", image: c });
        f.autoSize = !0;
        d.addChild(f);
      }
    };
  })();
  (function () {
    aJSs.JsPhoto = function (b, a, c) {
      function d() {
        aJSs.CommandDispatcher.getInstance().dispatchEvent({
          type: aJSs.Events.VIDEO_CLEAR
        });
        if ("" != x) {
          e();
          var a = new Image();
          a.src = c + x;
          a = new Quark.MovieClip({ image: a, id: "preloader", interval: 100 });
          a.addFrame([
            { rect: [0, 0, 25, 25] },
            { rect: [25, 0, 25, 25] },
            { rect: [50, 0, 25, 25] },
            { rect: [75, 0, 25, 25] },
            { rect: [100, 0, 25, 25] },
            { rect: [125, 0, 25, 25] }
          ]);
          a.x = t + (X - a.width) / 2;
          a.y = k + (Y - a.height) / 2;
          $.addChild(a);
        }
        z = y = 0;
        ia && ia.removeAllChildren();
        V.swapChildren(S, R);
        V.getChildIndex(S) > V.getChildIndex(R)
          ? ((aa = S), (ia = R))
          : ((aa = R), (ia = S));
        var b = new Image();
        b.onload = function () {
          e();
          y = 1;
          b.width = ka;
          b.height = la;
          var a = new Quark.Bitmap({
            id: "targetBitmap",
            image: b,
            rect: [0, 0, 0.001, 0.001]
          });
          a.useHandCursor = "true" == g && "" != i[u] ? !0 : !1;
          aa.addChild(a);
          U =
            0 == q[u]
              ? null == n
                ? Math.floor(Math.random() * da.transTotal) + 1
                : n[Math.floor(Math.random() * n.length)]
              : q[u];
          da.transition(U, aa, ka, la, p[u]);
          a.onEvent = function (a) {
            if ("mousedown" == a.type || "touchend" == a.type) {
              if ("true" == g && "" != i[u]) {
                switch (l[u]) {
                  case "0":
                    a = "_blank";
                    break;
                  case "1":
                    a = "_parent";
                    break;
                  case "2":
                    a = "_self";
                    break;
                  case "3":
                    a = "_top";
                    break;
                  default:
                    a = "_blank";
                }
                window.open(i[u], a);
              }
            } else
              "mousemove" == a.type || "touchmove" == a.type
                ? aJSs.CommandDispatcher.getInstance().dispatchEvent({
                    type: aJSs.Events.PHOTO_MOUSE_OVER
                  })
                : ("mouseout" == a.type || "touchout" == a.type) &&
                  aJSs.CommandDispatcher.getInstance().dispatchEvent({
                    type: aJSs.Events.PHOTO_MOUSE_OUT
                  });
          };
          aJSs.CommandDispatcher.getInstance().dispatchEvent({
            type: aJSs.Events.PHOTO_LOAD_COMPLETE,
            index: u
          });
        };
        b.src = c + j[u];
        aJSs.CommandDispatcher.getInstance().dispatchEvent({
          type: aJSs.Events.PLAY_CURRENT,
          index: u
        });
        u >= Z - 1 && "false" == K && "false" == v && I.Pause();
      }
      function f() {
        P--;
        try {
          Quark.getDOM("debugInfo").value = P;
        } catch (a) {}
        if (0 >= P || 1 == w)
          clearInterval(J),
            (J = null),
            0 == w
              ? "true" == v
                ? (u = Math.floor(Math.random() * Z))
                : u < Z - 1
                ? u++
                : (u = 0)
              : (w = 0),
            d();
      }
      function e() {
        if ("" != x) {
          var a = $.getChildById("preloader");
          null != a && $.removeChild(a);
        }
      }
      var h = b.frameRate,
        j = b.photoArray,
        i = b.photoUrlArray,
        g = b.enableURL,
        l = b.URLTarget,
        m = b.photoTimeArray,
        q = b.transitionArray,
        n = b.defineTransitionArray,
        p = b.transitionTimeArray,
        k = b.topPadding,
        r = b.bottomPadding,
        t = b.leftPadding,
        s = b.rightPadding,
        v = b.randomPlayingPhotos,
        x = b.loadStyle,
        T = b.startAutoPlay,
        K = b.continuum,
        L = b.videoAutoPlay,
        M = b.videoArray,
        X = a.width - t - s,
        Y = a.height - k - r,
        I = this,
        D = 0,
        y = 1,
        z = 1,
        w = 0,
        U = 0,
        P = 0,
        u = 0,
        J = null,
        Z = j.length;
      aJSs.CommandDispatcher.getInstance().addEventListener(
        aJSs.Events.TRANSITION_OVER,
        function () {
          z = 1;
          if (1 == D || 1 == w) (P = m[u] * h), (J = setInterval(f, 1e3 / h));
          "" != M[u] &&
            void 0 != M[u] &&
            0 == w &&
            ("true" == L && (clearInterval(J), (J = null)),
            aJSs.CommandDispatcher.getInstance().dispatchEvent({
              type: aJSs.Events.PLAY_VIDEO,
              index: u,
              width: X,
              height: Y
            }));
        }
      );
      aJSs.CommandDispatcher.getInstance().addEventListener(
        aJSs.Events.PLAY_NEXT,
        function () {
          I.Play();
        }
      );
      aJSs.CommandDispatcher.getInstance().addEventListener(
        aJSs.Events.VIDEO_START_PLAY,
        function () {
          I.Pause();
        }
      );
      var da = new aJSs.MaskEffect(h),
        $ = new Quark.DisplayObjectContainer({ id: "container" });
      $.autoSize = !0;
      a.addChild($);
      var ka = a.width - t - s,
        la = a.height - k - r,
        b = t,
        a = k,
        r = Quark.Bitmap,
        s = ka,
        ma = la,
        ea = "#DDD",
        na = document.createElement("canvas");
      na.width = s;
      na.height = ma;
      var pa = na.getContext("2d");
      pa.fillStyle = ea;
      pa.rect(0, 0, s, ma);
      pa.fill();
      ea = new Image();
      ea.src = na.toDataURL("image/png");
      ea.width = s;
      ea.height = ma;
      r = new r({ id: "photoBoxBg", image: ea });
      r.autoSize = !0;
      r.x = b;
      r.y = a;
      $.addChild(r);
      var V = new Quark.DisplayObjectContainer({
        id: "photoBox",
        x: b,
        y: a,
        width: ka,
        height: la
      });
      V.autoSize = !0;
      $.addChild(V);
      var ia,
        aa,
        S = new Quark.DisplayObjectContainer({ id: "aPhoto" }),
        R = new Quark.DisplayObjectContainer({ id: "bPhoto" });
      V.addChild(S);
      V.addChild(R);
      this.Play = function () {
        D = 1;
        1 == y && 1 == z
          ? (clearInterval(J), (J = null), u < Z - 1 ? u++ : (u = 0), d())
          : 1 == y && 0 == z
          ? ((w = 1), u < Z - 1 ? u++ : (u = 0), (da.maskerFull = 1))
          : (u < Z - 1 ? u++ : (u = 0), (w = 1));
      };
      this.Pause = function () {
        D = 0;
        null != J && (clearInterval(J), (J = null));
      };
      this.Previous = function (a) {
        D = a;
        0 < u ? u-- : (u = Z - 1);
        1 == y && 1 == z
          ? (clearInterval(J), (J = null), d())
          : 1 == y && 0 == z
          ? ((w = 1), (da.maskerFull = 1))
          : (w = 1);
      };
      this.Next = function (a) {
        D = a;
        u < Z - 1 ? u++ : (u = 0);
        1 == y && 1 == z
          ? (clearInterval(J), (J = null), d())
          : 1 == y && 0 == z
          ? ((w = 1), (da.maskerFull = 1))
          : (w = 1);
      };
      this.Show = function (a, b) {
        D = b;
        1 == y && 1 == z
          ? (clearInterval(J), (J = null), (u = a), d())
          : 1 == y && 0 == z
          ? ((w = 1), (u = a), (da.maskerFull = 1))
          : ((u = a), (w = 1));
      };
      "true" == T ? this.Show(0, 1) : this.Show(0, 0);
    };
  })();
  (function () {
    aJSs.JsMediaConsole = function (b, a, c, d) {
      function f() {
        void 0 != r &&
          (b.removeChild(r),
          void 0 != k && "videoCallPause" == t && (k.Play(), (t = "")),
          (r = void 0),
          e());
      }
      function e() {
        var a = document.getElementById("videoLoadText");
        a && b.removeChild(a);
      }
      var h = a.topPadding,
        j = a.leftPadding,
        c = a.musicPath,
        i = a.musicAutoPlay,
        g = a.musicLoop,
        l = a.musicStream,
        m = a.videoAutoPlay,
        q = a.bufferTime,
        n = a.videoArray,
        p = a.videoControls;
      if ("" != c) var k = new aJSs.Music(d + c, l, i, g);
      var r,
        t = "";
      aJSs.CommandDispatcher.getInstance().addEventListener(
        aJSs.Events.PLAY_VIDEO,
        function (a) {
          var c = a.index,
            e = a.width,
            a = a.height;
          void 0 != k && k.Playing() && (k.Pause(), (t = "videoCallPause"));
          r = new aJSs.Video(d + n[c], m, q, p, e, a);
          r.style.backgroundColor = "#000";
          r.style.position = "absolute";
          r.style.top = h + "px";
          r.style.left = j + "px";
          b.appendChild(r);
          c = document.getElementById("videoLoadText");
          null == c &&
            ((c = document.createElement("div")),
            (c.id = "videoLoadText"),
            (c.style.position = "absolute"),
            (c.style.top = h + 5 + "px"),
            (c.style.left = j + 5 + "px"),
            (c.style.font =
              "normal normal 11px/13px verdana,tahoma,arial,sans-serif"),
            (c.style.color = "#FFF"),
            (c.textContent = "Waiting..."),
            b.appendChild(c));
        }
      );
      aJSs.CommandDispatcher.getInstance().addEventListener(
        aJSs.Events.VIDEO_PLAY_ENDED,
        function () {
          f();
          aJSs.CommandDispatcher.getInstance().dispatchEvent({
            type: aJSs.Events.PLAY_NEXT
          });
        }
      );
      aJSs.CommandDispatcher.getInstance().addEventListener(
        aJSs.Events.VIDEO_CLEAR,
        function () {
          f();
        }
      );
      aJSs.CommandDispatcher.getInstance().addEventListener(
        aJSs.Events.VIDEO_START_PLAY,
        function () {
          e();
        }
      );
      this.MusicPlay = function () {
        k.Play();
      };
      this.MusicPause = function () {
        k.Pause();
      };
    };
  })();
  (function () {
    aJSs.JsMenu = function (b, a) {
      var c = b.topPadding,
        d = b.leftPadding,
        f = b.copyright;
      if (
        null == b.anvsoftMenu ||
        ("anvsoftPFMTheme" != f &&
          "anvsoftUSSTheme" != f &&
          "anvsoftHSMTheme" != f)
      ) {
        var e, h;
        switch (f) {
          case "anvsoftPFMTheme":
            h = "Powered by photo-flash-maker.com";
            e = 186;
            break;
          case "anvsoftUSSTheme":
            h = "Powered by ultraslideshow.com";
            e = 168;
            break;
          case "anvsoftHSMTheme":
            h = "Powered by html5-slideshow-maker.com";
            e = 210;
            break;
          case "anvsoftSWWTheme":
            h = "Powered by slidewow.com";
            e = 142;
            break;
          default:
            (h = "Powered by anvsoft.com"), (e = 136);
        }
        var j = new Quark.DisplayObjectContainer({ id: "menudBox" });
        j.autoSize = !0;
        j.x = d;
        j.y = c;
        a.addChild(j);
        var c = Quark.Bitmap,
          d = e,
          i = "#000",
          g = document.createElement("canvas");
        g.width = d;
        g.height = 20;
        var l = g.getContext("2d");
        l.fillStyle = i;
        l.rect(0, 0, d, 20);
        l.fill();
        i = new Image();
        i.src = g.toDataURL("image/png");
        i.width = d;
        i.height = 20;
        c = new c({ id: "copyrightBg", image: i });
        c.autoSize = !0;
        c.alpha = 0.3;
        j.addChild(c);
        c = Quark.Bitmap;
        d = e;
        i = "#FFF";
        g = h;
        h = document.createElement("canvas");
        h.width = d;
        h.height = 20;
        d = h.getContext("2d");
        d.font = "11px arial, sans-serif";
        d.textAlign = "start";
        d.textBaseline = "middle";
        d.fillStyle = i;
        d.fillText(g, 0, 10);
        d = g = d.measureText(g).width;
        i = new Image();
        i.src = h.toDataURL("image/png");
        i.width = d;
        i.height = 20;
        h = new c({ id: "copyrightText", image: i });
        h.useHandCursor = !0;
        h.autoSize = !0;
        h.x = Math.round((e - g) / 2);
        j.addChild(h);
        h.onEvent = function (a) {
            var c=confirm("h.event (desactivated) line: 4908 to 4926\nThe hidden links are:\n- http://www.photo-flash-maker.com/\n- http://www.ultraslideshow.com/\n- http://www.html5-slideshow-maker.com/\n- http://www.slidewow.com/\n- http://www.anvsoft.com/\nVoulez-vous ouvrir : http://www.ultraslideshow.com/ ?")
            if (c===true){
                window.open("http://www.photo-flash-maker.com/",target="_blank");
                alert("Link opened");
            } else {
                alert("Link not opened");
            };
        //   if ("mousedown" == a.type || "touchend" == a.type)
        //     switch (f) {
        //       case "anvsoftPFMTheme":
        //         window.open("http://www.photo-flash-maker.com/", "_self");
        //         break;
        //       case "anvsoftUSSTheme":
        //         window.open("http://www.ultraslideshow.com/", "_self");
        //         break;
        //       case "anvsoftHSMTheme":
        //         window.open("http://www.html5-slideshow-maker.com/", "_self");
        //         break;
        //       case "anvsoftSWWTheme":
        //         window.open("http://www.slidewow.com/", "_self");
        //         break;
        //       default:
        //         window.open("http://www.anvsoft.com/", "_self");
        //     }
        };
      }
    };
  })();
  (function () {
    aJSs.JsInterface = function (b, a, c, d, f) {
      this.globalPath = f;
      this.container = b;
      this.commandDispatcher = aJSs.CommandDispatcher.getInstance();
      this.copyright = a.copyright;
      this.movieWidth = a.movieWidth;
      this.movieHeight = a.movieHeight;
      this.startAutoPlay = a.startAutoPlay;
      this.continuum = a.continuum;
      this.clickToAutoPlay = a.clickToAutoPlay;
      this.randomPlayingPhotos = a.randomPlayingPhotos;
      this.enableURL = a.enableURL;
      this.movieBackgroundColor = a.movieBackgroundColor;
      this.loadStyle = a.loadStyle;
      this.anvsoftMenu = a.anvsoftMenu;
      this.frameRate = a.frameRate;
      this.globalTitleXml = a.globalTitleXml;
      this.musicPath = a.musicPath;
      this.musicStream = a.musicStream;
      this.musicLoop = a.musicLoop;
      this.musicAutoPlay = a.musicAutoPlay;
      this.topPadding = a.topPadding;
      this.bottomPadding = a.bottomPadding;
      this.leftPadding = a.leftPadding;
      this.rightPadding = a.rightPadding;
      this.globalDescriptionXml = a.globalDescriptionXml;
      this.videoAutoPlay = a.videoAutoPlay;
      this.bufferTime = a.bufferTime;
      this.videoControls = a.videoControls;
      this.thumbnailBasicXml = a.thumbnailBasicXml;
      this.thumbnailArray = a.thumbnailArray;
      this.photoArray = a.photoArray;
      this.photoUrlArray = a.photoUrlArray;
      this.URLTarget = a.URLTarget;
      this.videoArray = a.videoArray;
      this.transitionArray = a.transitionArray;
      this.photoTimeArray = a.photoTimeArray;
      this.transitionTimeArray = a.transitionTimeArray;
      this.defineTransitionArray = a.defineTransitionArray;
      this.photoTitleArray = a.photoTitleArray;
      this.descriptionText = a.descriptionText;
      this.Play = function () {
        c.Play();
      };
      this.Pause = function () {
        c.Pause();
      };
      this.Previous = function () {
        c.Previous();
      };
      this.Next = function () {
        c.Next();
      };
      this.Show = function (a, b) {
        c.Show(a, b);
      };
      this.MusicPlay = function () {
        d.MusicPlay();
      };
      this.MusicPause = function () {
        d.MusicPause();
      };
    };
  })();
  (function (b) {
    var a = aJSs.getParameters.parameters().xml_path,
      c = aJSs.getParameters.parameters().fs_path,
      d,
      f;
    void 0 == a
      ? void 0 == c
        ? ((d = "slides.xml"), (f = ""))
        : ((d = c + "/slides.xml"), (f = c + "/"))
      : ((d = a), (f = a.substr(0, a.lastIndexOf("/") + 1)));
    anvsoftJavaScriptSlideshow.init = function (a) {
      var c, j;
      if (b.document.createElement("canvas").getContext) {
        var a = Quark.getDOM(a),
          i = Quark.supportTouch
            ? ["touchstart", "touchmove", "touchend", "touchout"]
            : ["mousedown", "mousemove", "mouseup", "mouseout"],
          g = Quark.getUrlParams();
        void 0 == g.mode && (g.mode = 1);
        var l = a.clientWidth || a.offsetWidth,
          m = a.clientHeight || a.offsetHeight;
        1 == g.mode
          ? ((c = Quark.createDOM("canvas", { width: l, height: m })),
            a.appendChild(c),
            (j = new Quark.CanvasContext({ canvas: c })))
          : (j = new Quark.DOMContext({ canvas: a }));
        c = new Quark.Stage({ width: l, height: m, context: j });
        new Q.EventManager().registerStage(c, i);
        j = new aJSs.JsXmlLoad(d);
        new aJSs.JsBackground(j, c);
        i = new aJSs.JsPhoto(j, c, f);
        g = new aJSs.JsMediaConsole(a, j, c, f);
        new aJSs.JsMenu(j, c);
        l = new Q.Timer(1e3 / j.frameRate);
        l.addListener(c);
        l.start();
        j = new aJSs.JsInterface(a, j, i, g, f);
        new aJSsTemplate.Main(j);
      } else (c = new aJSs.JsXmlLoad(d)), new aJSs.JsCompatibleTheme(c, a, f);
    };
  })(window);
  """
content=""
mjsc=0
mjs="mjs=[\n"
lines=0
maxlines=15
f=open("lists.txt","w")
for i in a:
	if i=="\n":
		f.write("""mjs{}=\"\"\"{} \"\"\"\n""".format(mjsc,content))#mjs{}=\"\"\"{}\"\"\"\n.format(mjsc,content)
		content=""
		if lines==maxlines:mjs,lines=mjs+"mjs{},\n".format(mjsc),0
		else:mjs,lines=mjs+"mjs{},".format(mjsc),lines+1
		mjsc+=1
	else:
		if i=="\"":
			content+="\""
		else:
			content+=i
mjs+="]"
f.write("{}\n".format(mjs))
f.close()
