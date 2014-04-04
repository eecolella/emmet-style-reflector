# emmet-style-reflector

## Dependency

Obviously, [Emmet] (https://github.com/sergeche/emmet-sublime)

## Description

Reflect Emmet HTML expansion in Sass/LESS

## How to use 

[![Alt text for your video](https://raw.githubusercontent.com/eecolella/emmet-style-reflector/master/YouTubeImage.jpg)](http://www.youtube.com/watch?v=38fPtsf_Lew)


## Changelogs
#### v1.0.2
* tag without class and id will have ">"

## Expansions tested

* Child: ``` #first>ul>li ```

```sass
#first {

    >ul {

        >li {

        }

    }

}
```

* Sibling: ``` div+p+blockquote ```

```sass
>div {

}

>p {

}

>blockquote {

}
```

* Climb-up: ``` #first+#second>p>span+em^blockquote ```

```sass
#first {

}

#second {

    >p {

        >span {

        }

        >em {

        }

    }

    >blockquote {

    }

}
```

* Grouping: ``` #first>(header>ul>li*2>a)+footer>p ```

```sass
#first {

    header {

        >ul {

            >li {

                >a {

                }

            }

        }

    }

    footer {

        >p {

        }

    }

}
```

* Video demo: ``` header>(ul#menu>li*5>a)^div#home>div.rensponsive960>div.box>div.title+div.body ``` 

```sass
header {

    #menu {

        >li {

            >a {

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

* Extreme: ``` #first>(header[title="Hello world!"]>ul#menu>li.menuItem$@-*5>a)+footer{bla bla bla}^script ``` 


```sass
#first {

    header {

        #menu {

            .menuItem {

                >a {

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
