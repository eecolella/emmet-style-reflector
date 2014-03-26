# emmet-style-reflector

## Dependency

Obviously, [Emmet] (https://github.com/sergeche/emmet-sublime)

## Description

Reflect Emmet HTML expansion in Sass/LESS

## How to use

[![Alt text for your video](https://raw.githubusercontent.com/eecolella/emmet-style-reflector/master/YouTubeImage.jpg)](http://www.youtube.com/watch?v=38fPtsf_Lew)

## Expansions tested

* Child: ```html div>ul>li ```

```sass
div {

  ul {

    li {

    }

  }

}
```

* Sibling: ```html div+p+bq ```

```sass
div {

}

p {

}

bq {

}
```

* Climb-up: ```html div+div>p>span+em^blockquote ```

```sass
div {

}

div {

    p {

        span {

        }

        em {

        }

    }

    blockquote {

    }

}
```

* Grouping: ```html div>(header>ul>li*2>a)+footer>p ```

```sass
div {

    header {

        ul {

            li {

                a {

                }

            }

        }

    }

    footer {

        p {

        }

    }

}
```

* Video demo: ```html header>(ul#menu>li*5>a)^div#home>div.rensponsive960>div.box>div.title+div.body ``` 

```sass
header {

  #menu {

    li {

      a {

      }

    }

  }

}

#home {

  .rensponsive960 {

    .box {

      .title {

      }

      .body {

      }

    }

  }

}
```

* Extreme: ```html div>(header[title="Hello world!"]>ul#menu>li.menuItem$@-*5>a)+footer{bla bla bla}^script ``` 


```sass
div {

    header {

        #menu {

            .menuItem {

                a {

                }

            }

        }

    }

    footer {

    }

}

script {

}
```
